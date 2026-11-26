#!/usr/bin/env python3
"""Rigenera Mermaid da Turtle incorporati nella guida CORE, mediante il renderer DDTA.

Ogni blocco `<!-- DDTA-EXAMPLE-NN -->` precede un Turtle e il Mermaid da rigenerare.
Nessuna tripla RDF e' ricostruita da Mermaid. Le regole grafiche sono quelle nella guida.
"""
from __future__ import annotations
import argparse, difflib, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from datetime import datetime
from pathlib import Path
from rdflib import Graph, Namespace, RDF

MARK = re.compile(r'<!-- DDTA-EXAMPLE-(\d{2})\b[^\n]*-->')
TURTLE = re.compile(r'(?m)^```turtle\s*\n(.*?)^```\s*$', re.S | re.M)
MERMAID = re.compile(r'(?m)^```mermaid\s*\n(.*?)^```\s*$', re.S | re.M)
CORE = Namespace('https://w3id.org/ddta/core#')


def sha(data:bytes)->str:return hashlib.sha256(data).hexdigest()


def get_examples(text):
    markers=list(MARK.finditer(text))
    if len(markers)!=26 or [int(m.group(1)) for m in markers]!=list(range(1,27)):
        raise ValueError('Attesi marcatori univoci DDTA-EXAMPLE-01..26 in ordine')
    result=[]
    for idx, mark in enumerate(markers):
        end=markers[idx+1].start() if idx<25 else len(text)
        section=text[mark.end():end]
        turtle=TURTLE.search(section)
        mermaid=MERMAID.search(section)
        if not turtle or not mermaid or mermaid.start()<=turtle.end():
            raise ValueError(f'ESEMPIO_{idx+1:02d}: Turtle e Mermaid in ordine non trovati')
        if len(list(MERMAID.finditer(section)))!=1:
            raise ValueError(f'ESEMPIO_{idx+1:02d}: numero Mermaid imprevisto')
        turtle_abs=(mark.end()+turtle.start(1), mark.end()+turtle.end(1))
        mm_abs=(mark.end()+mermaid.start(1), mark.end()+mermaid.end(1))
        result.append({'id':f'ESEMPIO_{idx+1:02d}','ttl':text[turtle_abs[0]:turtle_abs[1]],'old':text[mm_abs[0]:mm_abs[1]],'span':mm_abs})
    return result


def runner(repo,guide,ttl,view,out):
    src=repo/'tools/visualization-tool/src'
    if not (src/'ddta_viz/pipeline.py').exists():
        raise FileNotFoundError(f'Pipeline DDTA non trovata: {src}')
    env=os.environ.copy();env['PYTHONPATH']=str(src)+(os.pathsep+env['PYTHONPATH'] if env.get('PYTHONPATH') else '')
    cmd=[sys.executable,'-m','ddta_viz.pipeline','--guides-md',str(guide),'--ttl',str(ttl),'--view',view,'--out-dir',str(out)]
    r=subprocess.run(cmd,env=env,cwd=repo,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='utf-8',errors='replace')
    if r.returncode!=0:raise RuntimeError(f'Renderer: {r.stdout}')
    return (out/'05_graph.mmd').read_text(encoding='utf-8'),json.loads((out/'06_diagnostics.json').read_text(encoding='utf-8'))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo-root',type=Path,required=True)
    p.add_argument('--guide',type=Path,required=True)
    p.add_argument('--out-dir',type=Path,required=True)
    p.add_argument('--mode',choices=['preview','check','apply'],default='preview')
    p.add_argument('--allow-incomplete-endpoints',action='store_true',help='Consenti esempi didattici incompleti, segnalandoli nel report')
    a=p.parse_args();repo=a.repo_root.resolve();guide=a.guide.resolve();out=a.out_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    data=guide.read_bytes();bom=data.startswith(b'\xef\xbb\xbf');crlf=b'\r\n' in data
    s=data.decode('utf-8-sig').replace('\r\n','\n')
    rules_guide=repo/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
    if not rules_guide.is_file():raise FileNotFoundError(f'Guida delle regole YAML non trovata: {rules_guide}')
    rule_rx=re.compile(r'(?ms)^```yaml ddta-visualization\s*\n.*?^```\s*$')
    if rule_rx.findall(s)!=rule_rx.findall(rules_guide.read_text(encoding='utf-8-sig')):
        raise ValueError('Le regole YAML della candidata non corrispondono alla guida installata: sincronizzazione bloccata')
    examples=get_examples(s);changes=[];report=[]
    src_lib=repo/'tools/visualization-tool/src'
    sys.path.insert(0,str(src_lib))
    from ddta_viz.extract_guides import extract_guides
    from ddta_viz.compile_rules import compile_rules
    from ddta_viz.catalog import Catalog
    from ddta_viz.project_view import project
    from ddta_viz.render_mermaid import render
    from ddta_viz.common import dump_json, load_graph
    rules_out=out/'rules';rules_out.mkdir(exist_ok=True)
    rules_yaml=rules_out/'01_rules_extracted.yaml'
    extract_guides([rules_guide],rules_yaml)
    compiled=rules_out/'02_rules_compiled.yaml'
    compile_rules([rules_yaml],compiled)
    catalog=Catalog([compiled])
    for i,item in enumerate(examples,1):
        case=out/item['id'];case.mkdir(parents=True,exist_ok=True)
        ttl=case/'source.ttl';ttl.write_text(item['ttl'],encoding='utf-8',newline='\n')
        g=load_graph([ttl])
        endpoints=[]
        for channel in sorted(g.subjects(RDF.type,CORE.CommunicationChannel),key=str):
            sources=list(g.objects(channel,CORE.hasSource));targets=list(g.objects(channel,CORE.hasDestination))
            if len(sources)!=1 or len(targets)!=1:
                endpoints.append({'channel':str(channel),'hasSource':len(sources),'hasDestination':len(targets)})
        view='functional-flow' if i in (13,26) else 'association'
        ir1=project(g,catalog,view=view,strict=False)
        first=render(ir1,catalog)
        ir2=project(g,catalog,view=view,strict=False)
        second=render(ir2,catalog)
        if first!=second:raise RuntimeError(f'{item["id"]}: non deterministico')
        if not first.strip() or 'flowchart' not in first:
            raise RuntimeError(f'{item["id"]}: Mermaid vuoto/non valido')
        body=first if first.endswith('\n') else first+'\n'
        (case/'05_graph.mmd').write_text(body,encoding='utf-8',newline='\n')
        (case/'05_graph.md').write_text('```mermaid\n'+body+'```\n',encoding='utf-8',newline='\n')
        dump_json(ir1,case/'04_projection.json')
        start,end=item['span'];changes.append((start,end,body))
        warnings=[d for d in ir1.get('diagnostics',[]) if d.get('severity')=='warning']
        report.append({'id':item['id'],'triples':len(g),'view':view,'sameAsGuide':body==item['old'],
                       'sha256':sha(body.encode()),'warnings':warnings,'endpointIssues':endpoints})
        print(f'{item["id"]}: {len(g)} triple; diff={body!=item["old"]}; avvisi={len(warnings)}; estremita mancanti={len(endpoints)}',flush=True)
    updated=s
    for start,end,body in reversed(changes):updated=updated[:start]+body+updated[end:]
    txt=updated.replace('\n','\r\n') if crlf else updated
    new=(b'\xef\xbb\xbf' if bom else b'')+txt.encode('utf-8')
    cand=out/'DDTA_CORE_VISUALIZATION_CANDIDATA.md';cand.write_bytes(new)
    diff=''.join(difflib.unified_diff(s.splitlines(True),updated.splitlines(True),fromfile='TESI/ontologies/core/DDTA_CORE_VISUALIZATION.md',tofile='candidate/DDTA_CORE_VISUALIZATION.md'))
    (out/'GUIDA_CORE.diff').write_text(diff,encoding='utf-8')
    all_incomplete=sum(bool(r['endpointIssues']) for r in report)
    result={'source':str(guide),'sourceSHA256':sha(data),'candidateSHA256':sha(new),'count':len(report),
            'drift':sum(not r['sameAsGuide'] for r in report),'incompleteExamples':all_incomplete,
            'deterministic':True,'examples':report}
    (out/'REPORT.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('RISULTATO:',json.dumps({k:v for k,v in result.items() if k!='examples'},ensure_ascii=False,indent=2),flush=True)
    if a.mode=='check':
        if new!=data:sys.exit(2)
        if all_incomplete and not a.allow_incomplete_endpoints:sys.exit(3)
    if a.mode=='apply':
        if all_incomplete and not a.allow_incomplete_endpoints:
            raise RuntimeError('Esempi con canali senza estremita obbligatorie: applicazione bloccata')
        if guide.read_bytes()!=data:raise RuntimeError('La guida e cambiata durante la generazione')
        backup=guide.with_name(guide.name+'.BACKUP_'+datetime.now().strftime('%Y%m%d_%H%M%S'))
        shutil.copy2(guide,backup)
        guide.write_bytes(new)
        print('APPLICATO:',guide,'BACKUP:',backup)
    return 0

if __name__=='__main__':sys.exit(main())
