"""Formal FR-to-Python evidence checker: does not prove normative compliance."""
from __future__ import annotations

import ast
from dataclasses import asdict, dataclass
from pathlib import Path
import re
from typing import Any

import yaml

from .engine import DEFAULT_SCHEMAS, validate

CLAIMS = {'unassessed', 'partial', 'implemented'}
BINDING_RE = re.compile(r'^(prototype/[A-Za-z0-9_./-]+\.py)::([A-Za-z_][A-Za-z0-9_]*)$')


@dataclass(frozen=True)
class ImplementationDiagnostic:
    path: str
    code: str
    severity: str
    message: str
    line: int | None = None
    column: int | None = None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ImplementationResult:
    project: str
    documents: int
    claims: int
    bindings: int
    diagnostics: list[ImplementationDiagnostic]
    complete: bool

    @property
    def errors(self) -> int:
        return sum(d.severity == 'error' for d in self.diagnostics)

    @property
    def valid(self) -> bool:
        return self.complete and self.errors == 0

    def as_dict(self) -> dict[str, Any]:
        return {'type': 'FRImplementationEvidence', 'project': self.project,
                'documents': self.documents, 'claims': self.claims,
                'bindings': self.bindings, 'complete': self.complete,
                'valid': self.valid, 'errors': self.errors,
                'diagnostics': [d.as_dict() for d in self.diagnostics]}


def _frontmatter(src: str) -> dict[str, Any] | None:
    lines = src.splitlines()
    if not lines or lines[0].strip() != '---':
        return None
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == '---'), None)
    if end is None:
        return None
    try:
        meta = yaml.safe_load('\n'.join(lines[1:end]))
    except yaml.YAMLError:
        return None
    return meta if isinstance(meta, dict) else None


def _line(src: str, key: str) -> int | None:
    for index, line in enumerate(src.splitlines(), 1):
        if line.strip() == '---' and index > 1:
            break
        if line.startswith(key + ':'):
            return index
    return None


def check_implementation_bindings(project: Path, schemas_dir: Path = DEFAULT_SCHEMAS) -> ImplementationResult:
    """Verify only declared FR->Python bindings; no coverage/compliance inference.

    DDTA-FR: FR-MR03-02-01
    DDTA-FR: FR-MR03-02-02
    """
    project = Path(project)
    diagnostics: list[ImplementationDiagnostic] = []
    complete = True
    documents = claims = bindings = 0
    known_fr: set[str] = set()
    declared_bindings: dict[str, set[str]] = {}

    def report(path: str, code: str, message: str, line: int | None = None) -> None:
        diagnostics.append(ImplementationDiagnostic(path, code, 'error', message, line, 1 if line else None))

    source_dir = project / 'docs' / '03-functional-requirements'
    if not source_dir.is_dir():
        report('', 'IMP-SCOPE', f'FunctionalRequirement directory absent: {source_dir}')
        return ImplementationResult(str(project), 0, 0, 0, diagnostics, False)
    try:
        files = sorted(source_dir.rglob('*.md'))
    except OSError as exc:
        report('', 'IMP-SCOPE', f'Cannot enumerate FR documents: {exc}')
        return ImplementationResult(str(project), 0, 0, 0, diagnostics, False)
    if not files:
        report('', 'IMP-SCOPE', 'No FunctionalRequirement documents in scope')
        return ImplementationResult(str(project), 0, 0, 0, diagnostics, False)

    for fr in files:
        documents += 1
        rel = fr.relative_to(project).as_posix()
        if fr.is_symlink():
            report(rel, 'IMP-SOURCE', 'Symlink FR is unsupported')
            complete = False
            continue
        try:
            src = fr.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            report(rel, 'IMP-SOURCE', f'Cannot read FR: {exc}')
            complete = False
            continue
        checked = validate(src, profile='strict', schemas_dir=schemas_dir)
        if not checked.valid:
            report(rel, 'IMP-FR-INVALID', 'FR must pass schema validation before artifact checking')
            complete = False
            continue
        meta = _frontmatter(src)
        if meta is None or meta.get('type') != 'FunctionalRequirement' or not isinstance(meta.get('id'), str):
            report(rel, 'IMP-FR-INVALID', 'Missing/invalid declared FR identity')
            complete = False
            continue
        claim = meta.get('implementationClaim', 'unassessed')
        items = meta.get('implementationBindings', [])
        if claim not in CLAIMS or not isinstance(items, list) or not all(isinstance(i, str) for i in items):
            report(rel, 'IMP-DECLARATION', 'Invalid FR implementation claim or bindings', _line(src, 'implementationClaim'))
            continue
        known_fr.add(meta['id'])
        declared_bindings[meta['id']] = set(items)
        if claim in {'partial', 'implemented'}:
            claims += 1
            if not items:
                report(rel, 'IMP-BINDINGS-MISSING', f'{claim} claim requires at least one binding',
                       _line(src, 'implementationClaim'))

        for item in items:
            bindings += 1
            marker_line = _line(src, 'implementationBindings')
            match = BINDING_RE.fullmatch(item)
            if not match:
                report(rel, 'IMP-BINDING-FORMAT', f'Unsupported binding {item!r}; expected prototype/.../*.py::symbol', marker_line)
                continue
            relative, symbol = match.groups()
            parts = Path(relative).parts
            if '..' in parts or '.' in parts or Path(relative).is_absolute():
                report(rel, 'IMP-BINDING-PATH', 'Path traversal/absolute path is not permitted', marker_line)
                continue
            target = project / relative
            try:
                scope = project.resolve(strict=True)
                resolved = target.resolve(strict=True)
                if not resolved.is_relative_to(scope) or any((project.joinpath(*parts[:i])).is_symlink() for i in range(1, len(parts)+1)):
                    report(rel, 'IMP-BINDING-PATH', f'Binding outside project or symlink: {relative}', marker_line)
                    continue
                if not resolved.is_file():
                    report(rel, 'IMP-BINDING-PATH', f'Binding is not a regular file: {relative}', marker_line)
                    continue
                text = resolved.read_text(encoding='utf-8')
                tree = ast.parse(text, filename=str(resolved))
            except (OSError, UnicodeError, SyntaxError) as exc:
                report(rel, 'IMP-ARTIFACT', f'Unusable Python artifact {relative}: {exc}', marker_line)
                continue
            symbols = [node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name == symbol]
            if len(symbols) != 1:
                report(rel, 'IMP-SYMBOL', f'Missing or ambiguous top-level symbol {symbol} in {relative}', marker_line)
                continue
            docstring = ast.get_docstring(symbols[0]) or ''
            tag = re.compile(r'^\s*DDTA-FR:\s*' + re.escape(meta['id']) + r'\s*$', re.MULTILINE)
            if not tag.search(docstring):
                report(rel, 'IMP-BACKLINK', f'{relative}::{symbol} has no DDTA-FR: {meta["id"]} in docstring', marker_line)

    # Reverse audit: every DDTA-FR tag in public Python source must name an
    # existing FR and that FR must declare the exact code symbol as a binding.
    # This checks documentation traceability, not function semantics.
    sources = project / 'prototype/generic-v01/ddta_tool'
    if not sources.is_dir():
        report('', 'IMP-CODE-SCOPE', f'Python source directory absent: {sources}')
        complete = False
    else:
        for artifact in sorted(sources.rglob('*.py')):
            relative = artifact.relative_to(project).as_posix()
            if artifact.is_symlink():
                report(relative, 'IMP-CODE-READ', 'Symlink Python source is unsupported')
                complete = False
                continue
            try:
                code_tree = ast.parse(artifact.read_text(encoding='utf-8'), filename=relative)
            except (OSError, UnicodeError, SyntaxError) as exc:
                report(relative, 'IMP-CODE-READ', f'Unusable Python source: {exc}')
                complete = False
                continue
            for node in code_tree.body:
                if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    continue
                docstring = ast.get_docstring(node) or ''
                for line in docstring.splitlines():
                    label = line.strip()
                    if not label.startswith('DDTA-FR:'):
                        continue
                    target_fr = label[len('DDTA-FR:'):].strip()
                    if not re.fullmatch(r'FR-[A-Za-z0-9-]+', target_fr):
                        report(relative, 'IMP-CODE-TAG-FORMAT', f'Invalid FR tag {label!r}', node.lineno)
                    elif target_fr not in known_fr:
                        report(relative, 'IMP-FR-UNKNOWN',
                               f'{node.name} references unknown FR {target_fr!r}', node.lineno)
                    elif f'{relative}::{node.name}' not in declared_bindings.get(target_fr, set()):
                        report(relative, 'IMP-BACKLINK-ORPHAN',
                               f'{node.name} tags {target_fr!r}, but the FR does not declare this symbol', node.lineno)

    diagnostics.sort(key=lambda d: (d.path, d.line or 0, d.code, d.message))
    return ImplementationResult(str(project), documents, claims, bindings, diagnostics, complete)
