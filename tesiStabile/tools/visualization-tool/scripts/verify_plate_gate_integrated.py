#!/usr/bin/env python3
"""Non-invasive visual regression: approved step 13 versus integrated renderer.

Extract the cumulative Turtle in each progressive step from the current
Markdown; render using the one-Turtle CORE+PROCESS entrypoint; inspect Mermaid
containment and compare with approved Appendix A. Never modify the Markdown.
"""
from __future__ import annotations
import argparse
import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from rdflib import Graph


def cumulative(markdown: str, number: int) -> str:
    pattern = {13:r'### 13\.2\b',14:r'### 14\.3\b',15:r'### 15\.3\b'}[number]
    m=re.search(pattern,markdown)
    if not m:raise ValueError(f'Non trovo il Turtle cumulativo del passo {number}')
    block=re.search(r'```turtle\s*\n(.*?)\n```',markdown[m.end():],re.S)
    if not block:raise ValueError(f'Turtle del passo {number} mancante')
    return block.group(1)+'\n'


def approved_graph(markdown: str) -> str:
    anchor='## Appendice A — Baseline grafica integrata del passo 13'
    start=markdown.find(anchor)
    if start<0:raise ValueError('Appendice A non trovata')
    m=re.search(r'```mermaid\s*\n(.*?)\n```',markdown[start:],re.S)
    if not m:raise ValueError('Mermaid approvato non trovato')
    return m.group(1)+'\n'


def container_paths(mermaid: str) -> list[tuple[str,tuple[str,...]]]:
    """Read nested Mermaid subgraphs from generated text, without editing it."""
    stack=[];result=[]
    for line in mermaid.splitlines():
        raw=line.strip()
        if raw.startswith('subgraph '):
            title=raw.split('[',1)[1] if '[' in raw else raw
            result.append((title,tuple(stack)))
            stack.append(title)
        elif raw=='end' and stack:
            stack.pop()
    return result


def nested_check(mermaid: str, node: str, parent: str) -> bool:
    return any(node in title and any(parent in ancestor for ancestor in ancestors)
               for title,ancestors in container_paths(mermaid))


def run(args) -> int:
    repo=Path(args.repo_root).resolve()
    out=Path(args.out_dir).resolve()
    doc=repo/'examples/plate-gate/DDTA_TARGA_COSTRUZIONE_PROGRESSIVA.md'
    core=repo/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
    process=repo/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'
    pipe=repo/'tools/visualization-tool/scripts/pipeline.py'
    for path in (doc,core,process,pipe):
        if not path.is_file():raise FileNotFoundError(path)
    original=doc.read_bytes();markdown=original.decode('utf-8')
    appendix=approved_graph(markdown)
    out.mkdir(parents=True,exist_ok=True)
    (out/'APPENDICE_A_APPROVATA.md').write_text('```mermaid\n'+appendix+'```\n',encoding='utf-8')
    record={'docSha256':hashlib.sha256(original).hexdigest().upper(),'steps':{}}
    report=['# Regressione grafica integrata — plate gate','',
            f'Documento invariato (SHA256): `{record["docSha256"]}`','',
            'La baseline approvata è l’Appendice A del passo 13; la differenza byte-a-byte è informativa, non prova da sola una regressione semantica.','']
    for n in (13,14,15):
        work=out/f'PASSO_{n}'
        work.mkdir(exist_ok=True)
        data=cumulative(markdown,n)
        g=Graph().parse(data=data,format='turtle')
        ttl=work/'integrated_input.ttl'
        ttl.write_text(data,encoding='utf-8')
        result=subprocess.run([sys.executable,str(pipe),'--core-generator',str(pipe),
                               '--ttl',str(ttl),'--core-guide',str(core),'--process-guide',str(process),
                               '--out-dir',str(work/'GENERATO')],capture_output=True,text=True,encoding='utf-8',errors='replace')
        (work/'stdout.txt').write_text(result.stdout,encoding='utf-8')
        (work/'stderr.txt').write_text(result.stderr,encoding='utf-8')
        item={'triples':len(g),'exit':result.returncode,'errors':[],'checks':{}}
        if result.returncode:
            item['errors'].append('ERRORE_PIPELINE')
            report += [f'## Passo {n} — ERRORE_PIPELINE','',f'Triple: {len(g)}, exit: {result.returncode}.',
                       f'Consultare `PASSO_{n}/stderr.txt`.','']
        else:
            core_mmd=(work/'GENERATO/core/05_graph.mmd').read_text(encoding='utf-8')
            combo=(work/'GENERATO/core_process_compact/05_graph.mmd').read_text(encoding='utf-8')
            item['checks']={
                'coreWithoutProcessStep':'ProcessStep' not in core_mmd,
                'coreWithoutInternalOCRContracts':not any(nm in core_mmd for nm in ('CNN_OCRResultContract','Transformer_OCRResultContract')),
                'coreWithoutProcessOnlyOCRResources':not any(nm in core_mmd for nm in ('CNN + Attention-LSTM OCR','MobileNetV3 + Transformer OCR')),
                'ocrInternalContractsVisible':all(nm in combo for nm in ('CNN_OCRResultContract','Transformer_OCRResultContract')),
                'ocrContractsInsideOCRProcess':all(nested_check(combo,nm,'RecognizePlateNumberProcess') for nm in ('CNN_OCRResultContract','Transformer_OCRResultContract')),
                'coreSystemsPresent':all(nm in combo for nm in ('PlateRecognitionSystem','HumanReviewSystem','GateControlSystem','CameraSystem')),
                'humanReviewChannelVisible':'ProcessingToHumanReviewChannel' in combo,
                'invokesProcessVisible':'invokesProcess' in combo,
            }
            if n>=14:
                item['checks']['retrainingInsidePlateRecognitionSystem']=nested_check(core_mmd,'AutomaticOCRRetraining','PlateRecognitionSystem')
            if n>=15:
                item['checks']['manualIdentificationInsideHumanReviewSystem']=nested_check(core_mmd,'ManuallyIdentifyPlateNumber','HumanReviewSystem')
                item['checks']['manualToGateChannelVisible']='HumanToGateChannel' in combo
            if n==13:
                expected=appendix.replace('\r\n','\n').strip()+'\n'
                actual=combo.replace('\r\n','\n').strip()+'\n'
                item['byteIdenticalToAppendixA']=expected==actual
                if expected!=actual:
                    diff=''.join(difflib.unified_diff(expected.splitlines(keepends=True),actual.splitlines(keepends=True),fromfile='APPENDICE_A',tofile='GENERATO',n=3))
                    (work/'DIFF_APPENDICE_A.diff').write_text(diff,encoding='utf-8')
            issues=[k for k,v in item['checks'].items() if not v]
            item['errors']+=issues
            report += [f'## Passo {n} — '+('VERIFICHE PASS' if not issues else 'VERIFICHE DA RIVEDERE'),'',
                       f'Triple: {len(g)}; Mermaid: `PASSO_{n}/GENERATO/core_process_compact/05_graph.md`.','']
            if n==13:report.append(f'Confronto byte con Appendice A: **{"IDENTICO" if item["byteIdenticalToAppendixA"] else "DIFFERENTE"}** (consultare il diff se presente).\n')
            for key,value in item['checks'].items():report.append(f'- {"PASS" if value else "FAIL"} — `{key}`')
            report.append('')
        record['steps'][str(n)]=item
    if doc.read_bytes()!=original:raise RuntimeError('Il documento è cambiato durante la rigenerazione')
    (out/'REPORT.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (out/'REPORT.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    print('Report:',out/'REPORT.md')
    print('Passi:',{k:(v['exit'],len(v['errors'])) for k,v in record['steps'].items()})
    return 0 if all(not x['errors'] for x in record['steps'].values()) else 1


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo-root',required=True)
    ap.add_argument('--out-dir',required=True)
    a=ap.parse_args()
    try:raise SystemExit(run(a))
    except (ValueError,FileNotFoundError,RuntimeError) as exc:
        print('ERRORE:',exc,file=sys.stderr)
        raise SystemExit(2)

if __name__=='__main__':main()
