'use strict';
const vscode = require('vscode');
const path = require('path');
const fs = require('fs');
const cp = require('child_process');

const TYPE_FOLDERS = new Set(['01-macro-requirements', '02-decisions', '03-functional-requirements']);
let collection;
const timers = new Map();
const running = new Map();
const versions = new Map();
let output;

function contextFor(document) {
  if (document.uri.scheme !== 'file' || document.languageId !== 'markdown') return null;
  const file = document.uri.fsPath;
  const parent = path.dirname(file);
  const folder = path.basename(parent);
  if (!TYPE_FOLDERS.has(folder)) return null;
  if (path.basename(path.dirname(parent)) !== 'docs') return null;
  if (!fs.existsSync(file)) return null; // C9 R1B only saved-document identities, unsaved text allowed.
  const docs = path.dirname(parent);
  return {docs, relative: `${folder}/${path.basename(file)}`};
}

function frameworkRoot(document) {
  const config = vscode.workspace.getConfiguration('ddta', document.uri);
  let declared = config.get('frameworkModuleRoot', '').trim();
  if (declared) return declared;
  const candidates = [];
  for (const folder of vscode.workspace.workspaceFolders || []) {
    candidates.push(path.join(folder.uri.fsPath, 'projects', 'ddta-authoring-tool', 'prototype', 'generic-v01'));
    candidates.push(path.join(folder.uri.fsPath, 'prototype', 'generic-v01'));
    candidates.push(path.join(folder.uri.fsPath, '..', '..', 'prototype', 'generic-v01'));
  }
  // Pilot's docs at ddta-authoring-tool/pilots/<pilot>/docs.
  candidates.push(path.resolve(path.dirname(path.dirname(document.uri.fsPath)), '..', '..', 'prototype', 'generic-v01'));
  return candidates.find(p => fs.existsSync(path.join(p, 'ddta_tool', '__main__.py'))) || '';
}

function renderDiagnostics(document, payload) {
  const diagnostics = (payload.workspace && payload.workspace.diagnostics || []).filter(d => d.path === payload.snapshot);
  const seen = new Set();
  const mapped = [];
  for (const d of diagnostics) {
    const line = Math.max(0, (d.line || 1) - 1);
    const col = Math.max(0, (d.column || 1) - 1);
    const key = `${d.code}|${line}|${col}|${d.message}|${d.severity}`;
    if (seen.has(key)) continue;
    seen.add(key);
    const range = new vscode.Range(line, col, line, col + 1);
    const severity = d.severity === 'warning' ? vscode.DiagnosticSeverity.Warning : vscode.DiagnosticSeverity.Error;
    const item = new vscode.Diagnostic(range, d.message, severity);
    item.code = d.code;
    item.source = 'DDTA';
    mapped.push(item);
  }
  collection.set(document.uri, mapped);
}

function check(document) {
  const target = contextFor(document);
  if (!target) { if (collection) collection.delete(document.uri); return; }
  const cfg = vscode.workspace.getConfiguration('ddta', document.uri);
  const moduleRoot = frameworkRoot(document);
  if (!moduleRoot) {
    output.appendLine('DDTA: frameworkModuleRoot missing; set ddta.frameworkModuleRoot to prototype/generic-v01.');
    collection.delete(document.uri);
    return;
  }
  const python = cfg.get('pythonExecutable', 'python');
  const profile = cfg.get('profile', 'draft');
  const key = document.uri.toString();
  const version = document.version;
  versions.set(key, version);
  const previous = running.get(key);
  if (previous) previous.kill();
  const env = {...process.env, PYTHONPATH: moduleRoot + (process.env.PYTHONPATH ? path.delimiter + process.env.PYTHONPATH : '')};
  const processChild = cp.spawn(python, ['-m', 'ddta_tool', 'check-snapshot', target.docs, target.relative, '--profile', profile, '--json'],
    {env, windowsHide: true, stdio: ['pipe', 'pipe', 'pipe']});
  running.set(key, processChild);
  let stdout = '', stderr = '';
  processChild.stdout.setEncoding('utf8');
  processChild.stderr.setEncoding('utf8');
  processChild.stdout.on('data', chunk => { stdout += chunk; });
  processChild.stderr.on('data', chunk => { stderr += chunk; });
  processChild.on('error', error => { output.appendLine(`DDTA: cannot run Python: ${error.message}`); collection.delete(document.uri); });
  processChild.on('close', () => {
    if (running.get(key) !== processChild) return;
    running.delete(key);
    if (versions.get(key) !== version || document.isClosed) return;
    try {
      const payload = JSON.parse(stdout);
      if (!payload.workspace || !Array.isArray(payload.workspace.diagnostics)) throw new Error('Malformed DDTA workspace response');
      renderDiagnostics(document, payload);
    } catch (error) {
      collection.delete(document.uri);
      output.appendLine(`DDTA: check-snapshot failed: ${error.message}; ${stderr}`);
    }
  });
  processChild.stdin.on('error', () => {}); // Handles cancellation of superseded checks.
  processChild.stdin.end(Buffer.from(document.getText(), 'utf8'));
}

function schedule(document, immediate = false) {
  const key = document.uri.toString();
  if (timers.has(key)) clearTimeout(timers.get(key));
  const ms = immediate ? 0 : vscode.workspace.getConfiguration('ddta', document.uri).get('debounceMs', 350);
  timers.set(key, setTimeout(() => { timers.delete(key); check(document); }, ms));
}

async function ddtaCompletions(document, position) {
  if (!contextFor(document)) return [];
  const moduleRoot = frameworkRoot(document);
  if (!moduleRoot) return [];
  const cfg = vscode.workspace.getConfiguration('ddta', document.uri);
  const python = cfg.get('pythonExecutable', 'python');
  return new Promise(resolve => {
    const env = {...process.env, PYTHONPATH: moduleRoot + (process.env.PYTHONPATH ? path.delimiter + process.env.PYTHONPATH : '')};
    const proc = cp.spawn(python, ['-m', 'ddta_tool', 'suggest', '--line', String(position.line + 1), '--column', String(position.character + 1), '--json'], {env, windowsHide:true, stdio:['pipe','pipe','pipe']});
    let data = '';
    proc.stdout.setEncoding('utf8');
    proc.stdout.on('data', chunk => {data += chunk;});
    proc.on('error', e => {output.appendLine('DDTA suggest: '+e.message); resolve([]);});
    proc.on('close', () => {
      try {
        const result = JSON.parse(data);
        resolve((result.items || []).map(entry => {
          const item = new vscode.CompletionItem(entry.label, entry.kind === 'value' ? vscode.CompletionItemKind.Value : vscode.CompletionItemKind.Field);
          item.insertText = entry.insertText;
          return item;
        }));
      } catch (e) {output.appendLine('DDTA suggest: '+e.message); resolve([]);}
    });
    proc.stdin.on('error', () => {});
    proc.stdin.end(Buffer.from(document.getText(), 'utf8'));
  });
}

function activate(context) {
  collection = vscode.languages.createDiagnosticCollection('DDTA');
  context.subscriptions.push(vscode.languages.registerCompletionItemProvider({language: 'markdown', scheme: 'file'}, {provideCompletionItems: ddtaCompletions}, ':', ' '));
  output = vscode.window.createOutputChannel('DDTA Pilot');
  context.subscriptions.push(collection, output);
  context.subscriptions.push(vscode.workspace.onDidOpenTextDocument(d => schedule(d, true)));
  context.subscriptions.push(vscode.workspace.onDidChangeTextDocument(e => schedule(e.document)));
  context.subscriptions.push(vscode.workspace.onDidSaveTextDocument(d => schedule(d, true)));
  context.subscriptions.push(vscode.workspace.onDidCloseTextDocument(d => {
    const key = d.uri.toString();
    if (timers.has(key)) clearTimeout(timers.get(key));
    timers.delete(key);
    if (running.has(key)) running.get(key).kill();
    running.delete(key); versions.delete(key); collection.delete(d.uri);
  }));
  context.subscriptions.push(vscode.commands.registerCommand('ddta.checkCurrent', () => {
    const doc = vscode.window.activeTextEditor?.document;
    if (doc) schedule(doc, true);
  }));
  for (const doc of vscode.workspace.textDocuments) schedule(doc, true);
}
function deactivate() {
  for (const t of timers.values()) clearTimeout(t);
  for (const p of running.values()) p.kill();
}
module.exports = {activate, deactivate};
