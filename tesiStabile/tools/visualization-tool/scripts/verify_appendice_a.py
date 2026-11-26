#!/usr/bin/env python3
"""Rigenerazione reale e confronto strutturale del passo 13 approvato, senza alterare sorgenti.

Non copia il Mermaid approvato come output; lo usa soltanto come oracle indipendente.
Non normalizza differenze semantiche, grafiche, etichette, palette o archi.
"""
from __future__ import annotations
import argparse
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
sys.dont_write_bytecode = True
import tempfile
from pathlib import Path

TURTLE_PATTERN=r'### 13\.2 Turtle cumulativo[^\n]*\n.*?```turtle\n(.*?)\n```'
BASELINE_FILE=Path('tools/visualization-tool/tests/fixtures/plate_gate_passo13_approved.mmd')
BASELINE_SHA256='13D85ED70CAAC813ADACEFEFE9DABF80F558A93C28ACC6A3E23325906758FCA0'
GROUP_RE=re.compile(r'^\s*subgraph\s+(G_[0-9a-f]{14})\[(.*)\]\s*$')
CLASS_DEF_RE=re.compile(r'^\s*classDef\s+([A-Za-z_0-9]+)\s+(.+)$')
CLASS_RE=re.compile(r'^\s*class\s+([A-Za-z_0-9,]+)\s+([A-Za-z_0-9]+)\s*$')


def hashdata(data:bytes)->str:
    return hashlib.sha256(data).hexdigest().upper()


def extract(doc_text:str):
    t=re.search(TURTLE_PATTERN,doc_text,re.S)
    if not t:raise ValueError('Turtle cumulativo del passo 13 non trovato')
    return t.group(1)+'\n'


def render_canonical(approved: str, produced: str):
    """Canonicalizes ONLY opaque group IDs, indentation, unused classDefs, class id ordering.

    Checks all other Mermaid tokens verbatim, including labels/base64 SVG, edge styles,
    container hierarchy, links, fills, colors and linkStyle ordering.
    """
    expected=approved.splitlines();actual=produced.splitlines()
    e_groups=[GROUP_RE.match(x).groups() for x in expected if GROUP_RE.match(x)]
    a_groups=[GROUP_RE.match(x).groups() for x in actual if GROUP_RE.match(x)]
    if len(e_groups)!=len(a_groups):
        return None,None,{'reason':'Numero contenitori Mermaid diverso','expected':len(e_groups),'actual':len(a_groups)}
    # The group's structural location is checked again by the full line diff
    # after mapping; this matches only positional occurrences with identical labels.
    groups={}
    for (e_id,e_label),(a_id,a_label) in zip(e_groups,a_groups):
        if e_label!=a_label:
            return None,None,{'reason':'Etichette dei gruppi diverse','expected':e_label,'actual':a_label}
        if a_id in groups and groups[a_id]!=e_id:
            return None,None,{'reason':'Identita di gruppo duplicata','id':a_id}
        groups[a_id]=e_id
    if len(set(eid for eid,_ in e_groups))!=len(e_groups) or len(groups)!=len(a_groups):
        return None,None,{'reason':'Duplicazione ID di gruppo'}
    actual=[re.sub(r'G_[0-9a-f]{14}',lambda m:groups.get(m.group(),m.group()),line) for line in actual]

    def reduce(lines):
        lines=[line.strip() for line in lines if line.strip()]
        used={m.group(2) for line in lines if (m:=CLASS_RE.match(line))}
        result=[]
        for line in lines:
            m=CLASS_DEF_RE.match(line)
            if m and m.group(1) not in used:continue
            m=CLASS_RE.match(line)
            if m:line='class '+','.join(sorted(m.group(1).split(',')))+' '+m.group(2)
            result.append(line)
        return result
    return reduce(expected),reduce(actual),{'groupsMapped':len(groups),'changesPermitted':['group IDs','indentation','unused classDef','unordered class membership']}



def verify_embedded_process_examples(process_guide:Path,core_guide:Path):
    """Regenerate all approved PROCESS guide examples from their own Turtle."""
    sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'src'))
    import ddta_process
    content=process_guide.read_text(encoding='utf-8-sig')
    marker=r'<!-- DDTA-PROCESS-EXAMPLE-(\d+) rule="([^"]+)" -->'
    occurrences=list(re.finditer(marker,content))
    if len(occurrences)!=17:
        return {'total':len(occurrences),'passed':False,'mismatches':['attesi 17 esempi']}
    failures=[]
    for i,hit in enumerate(occurrences):
        section=content[hit.end():occurrences[i+1].start() if i+1<len(occurrences) else len(content)]
        turtle=re.search(r'```turtle\n(.*?)\n```',section,re.S)
        markdown=re.search(r'```mermaid\n(.*?)\n```',section,re.S)
        if turtle is None or markdown is None:
            failures.append(hit.group(1)+': blocco Turtle o Mermaid mancante')
            continue
        with tempfile.TemporaryDirectory(prefix='ddta-embedded-') as tmp:
            source=Path(tmp)/'input.ttl';source.write_text(turtle.group(1)+'\n',encoding='utf-8',newline='\n')
            ir=ddta_process.project(source,source,process_guide)
            fragment,diagnostics=ddta_process.ProcessRenderer(ir,process_guide,core_guide).render()
            output='%%{init: {"htmlLabels":true,"theme":"base","layout":"elk"}}%%\nflowchart TB\n\n'
            output+='    %% DDTA PROCESS: modular RDF projection (independent of CORE renderer)\n'+fragment
            if diagnostics['processLinkStylesRelative']:
                output+='\n'
                for style in diagnostics['processLinkStylesRelative']:
                    idx,color=style[:2];extra=style[2] if len(style)>2 else 'stroke-width:2.5px'
                    output+=f'    linkStyle {idx} stroke:{color},{extra}\n'
            if output.rstrip('\n') != markdown.group(1).rstrip('\n'):
                failures.append(hit.group(1)+': Mermaid non riproducibile')
    return {'total':len(occurrences),'passed':not failures,'mismatches':failures}


def main(argv=None):
    ap=argparse.ArgumentParser(description='Confronto rigoroso baseline grafica del passo 13')
    ap.add_argument('--repo-root',required=True,type=Path)
    ap.add_argument('--out-dir',required=True,type=Path)
    a=ap.parse_args(argv)
    repo=a.repo_root.resolve()
    doc=repo/'examples/plate-gate/DDTA_TARGA_COSTRUZIONE_PROGRESSIVA.md'
    if not doc.is_file():ap.error(f'File progressivo mancante: {doc}')
    original=doc.read_bytes();ttl=extract(original.decode('utf-8-sig'))
    baseline=repo/BASELINE_FILE
    if not baseline.is_file():ap.error(f'Fixture approvata assente: {baseline}')
    approved=baseline.read_text(encoding='utf-8-sig')
    if hashdata(approved.encode('utf-8'))!=BASELINE_SHA256:
        ap.error(f'SHA256 della fixture non corrispondente al riferimento approvato: {baseline}')
    out=a.out_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    source=out/'PASSO13_ORIGINALE.ttl';source.write_text(ttl,encoding='utf8',newline='\n')
    (out/'RIFERIMENTO_PASSO13.mmd').write_text(approved,encoding='utf8',newline='\n')
    (out/'RIFERIMENTO_PASSO13.md').write_text('```mermaid\n'+approved+'```\n',encoding='utf8',newline='\n')
    tool=repo/'tools/visualization-tool'
    run=out/'RIGENERATO'
    cmd=[sys.executable,str(tool/'scripts/pipeline.py'),
         '--core-generator',str(tool/'scripts/pipeline.py'),
         '--core-guide',str(repo/'ontologies/core/DDTA_CORE_VISUALIZATION.md'),
         '--process-guide',str(repo/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'),
         '--ttl',str(source),'--out-dir',str(run)]
    cp=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace',
                      env={**os.environ, 'PYTHONDONTWRITEBYTECODE':'1'})
    (out/'PIPELINE_STDOUT.txt').write_text(cp.stdout,encoding='utf8')
    (out/'PIPELINE_STDERR.txt').write_text(cp.stderr,encoding='utf8')
    produced_file=run/'core_process_compact/05_graph.mmd'
    report={'sourceSha256':hashdata(original),'ttlSha256':hashdata(ttl.encode('utf8')),
            'approvedSha256':hashdata(approved.encode('utf8')), 'baselineFile':str(baseline.relative_to(repo)),'exitCode':cp.returncode,
            'sourceUnchanged':doc.read_bytes()==original,
            'generated':produced_file.is_file(), 'exactText':False,'visualStructureEquivalent':False}
    if cp.returncode==0 and produced_file.is_file():
        produced=produced_file.read_text(encoding='utf-8')
        expected_norm=approved.replace('\r\n','\n')
        actual_norm=produced.replace('\r\n','\n')
        report['exactText']=expected_norm==actual_norm
        e,a,meta=render_canonical(expected_norm,actual_norm)
        report.update(meta)
        if e is not None:
            report['visualStructureEquivalent']=e==a
            diff='\n'.join(difflib.unified_diff(e,a,'PASSO13_RIFERIMENTO','GENERATOR_CORRENTE',n=2))+'\n'
            (out/'DIFFERENZE_GRAFICHE.diff').write_text(diff,encoding='utf8')
            report['canonicalSha256']={'reference':hashdata(('\n'.join(e)+'\n').encode()),
                                        'generated':hashdata(('\n'.join(a)+'\n').encode())}
    report['embeddedExamples']=verify_embedded_process_examples(repo/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md',repo/'ontologies/core/DDTA_CORE_VISUALIZATION.md')
    report['passed']=report['visualStructureEquivalent'] and report['sourceUnchanged'] and cp.returncode==0 and report['embeddedExamples']['passed']
    (out/'REPORT.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    msg=['# Verifica grafica del passo 13','',
         f"- **Equivalenza grafica verificata:** {'PASS' if report['visualStructureEquivalent'] else 'FAIL'}",
         f"- **Identità testuale normalizzando solo EOL:** {'PASS' if report['exactText'] else 'DIFFERENTE'}",
         f"- **Pipeline completata:** {'PASS' if cp.returncode==0 else 'FAIL'}",
         f"- **Documento originale invariato:** {'PASS' if report['sourceUnchanged'] else 'FAIL'}",
         f"- **Esempi guida PROCESS:** {report['embeddedExamples']['total']} controllati, {'PASS' if report['embeddedExamples']['passed'] else 'FAIL'}",
         '- **Input:** un Turtle cumulativo completo, estratto dal passo 13',
         '- **Nota:** la pipeline standard riproduce direttamente la baseline approvata; nessun profilo alternativo.',
         '- **Criterio di equivalenza grafica:** identici contenitori ordinati, nodi, etichette, icone, connessioni, stili e linkStyle. Sono ignorati soltanto ID opachi di gruppi, rientri, ordine dei membri di un medesimo `class` e definizioni CSS mai usate.',
         '- **Regressioni:** una qualsiasi altra differenza causa FAIL. Non si copia mai il Mermaid approvato nel percorso RIGENERATO.',
         '',f"- [Mermaid rigenerato](RIGENERATO/core_process_compact/05_graph.md)",
         '- [Mermaid riferimento](RIFERIMENTO_PASSO13.md)',
         '- [Differenze semantico-grafiche](DIFFERENZE_GRAFICHE.diff)',
         '- [Log pipeline](PIPELINE_STDERR.txt)','']
    (out/'REPORT.md').write_text('\n'.join(msg),encoding='utf8')
    print(json.dumps(report,indent=2,ensure_ascii=False))
    print('REPORT:',out/'REPORT.md')
    return 0 if report['passed'] else 1

if __name__=='__main__':sys.exit(main())
