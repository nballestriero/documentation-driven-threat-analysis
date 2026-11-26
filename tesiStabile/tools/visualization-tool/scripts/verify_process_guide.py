#!/usr/bin/env python3
"""Regression test from guide's 17 Turtle examples to deterministic PROCESS Mermaid.
No repository modifications. Does not invoke CORE pipeline and does not assert
full CORE+PROCESS composed output to be correct.
"""
from pathlib import Path
import re,sys,tempfile
if '--help' in sys.argv[1:] or '-h' in sys.argv[1:]:
    print('usage: verify_process_guide.py [-h]')
    print('Verifica in sola lettura i 17 esempi PROCESS contro la guida grafica.')
    raise SystemExit(0)
sys.dont_write_bytecode = True

root=Path(__file__).resolve().parents[1]
repo=root.parents[1]
sys.path.insert(0,str(root/'src'))
import ddta_process as engine
process_guide=repo/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'
core_guide=repo/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
source=process_guide.read_text(encoding='utf8')
markers=list(re.finditer(r'<!-- DDTA-PROCESS-EXAMPLE-(\d+) rule="[^"]+" -->',source))
if len(markers)!=17 or [int(m.group(1)) for m in markers]!=list(range(1,18)):
    raise ValueError('Attesi esattamente 17 esempi ordinati')
with tempfile.TemporaryDirectory(prefix='ddta-r3-regression-') as folder:
    tmp=Path(folder)
    (tmp/'core_empty.ttl').write_text('@prefix ddta: <https://w3id.org/ddta/core#> .\n',encoding='utf8',newline='\n')
    for idx,m in enumerate(markers):
        part=source[m.end():markers[idx+1].start() if idx+1<len(markers) else len(source)]
        tt=re.search(r'```turtle\s*\n(.*?)\n```',part,re.S)
        mm=re.search(r'```mermaid\s*\n(.*?)\n```',part,re.S)
        if not tt or not mm:raise ValueError('Esempio incompleto: '+str(idx+1))
        (tmp/'source.ttl').write_text(tt.group(1)+'\n',encoding='utf8',newline='\n')
        ir=engine.project(tmp/'core_empty.ttl',tmp/'source.ttl',process_guide)
        frag,diag=engine.ProcessRenderer(ir,process_guide,core_guide,'compact',False).render()
        style=''.join(f'    linkStyle {spec[0]} stroke:{spec[1]},{spec[2] if len(spec)>2 else "stroke-width:2.5px"}\n'
                      for spec in diag['processLinkStylesRelative'])
        merged=('%%{init: {"htmlLabels":true,"theme":"base","layout":"elk"}}%%\n'
                'flowchart TB\n\n'
                '    %% DDTA PROCESS: modular RDF projection (independent of CORE renderer)\n'
                +frag+('\n'+style if style else ''))
        if merged != mm.group(1).rstrip('\n')+'\n':
            raise ValueError('Drift nel Mermaid della guida: ESEMPIO_%02d' % (idx+1))
        if idx == 1: # fixture: contiene una reference a risorsa
            refs=[v for v in ir['operands'].values() if v.get('resourceReferences')]
            if not refs:raise ValueError('Esempio02 non esercita referencesResource')
            opt,_=engine.ProcessRenderer(ir,process_guide,core_guide,'compact',True).render()
            if 'referencesResource' not in opt:raise ValueError('Estensione grafica riferimenti non funziona')
        print('PASS: ESEMPIO_%02d' % (idx+1))
if not hasattr(engine.ProcessRenderer,'draw_code_reference'):
    raise ValueError('Regressione: supporto CodeReference assente')
print('=== PASS 17/17 ESEMPI; CodeReference presente; referencesResource opzionale ===')
