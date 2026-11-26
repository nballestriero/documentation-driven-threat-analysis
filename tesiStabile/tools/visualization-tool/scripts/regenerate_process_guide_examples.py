#!/usr/bin/env python3
"""Rebuild 17 illustrative PROCESS Mermaid blocks strictly from adjacent Turtle.

The pipeline runs the existing CORE renderer with a *declared empty* RDF
baseline and uses a proposed PROCESS renderer. It does not infer relationships
from node labels or generate RDF. Generated Mermaid must be reviewed visually.
"""
from __future__ import annotations
import argparse,difflib,hashlib,json,os,re,shutil,subprocess,sys,tempfile
from datetime import datetime
from pathlib import Path
from rdflib import Graph,Namespace,RDF

MARK=re.compile(r'<!-- DDTA-PROCESS-EXAMPLE-(\d{2}) rule="([^"]+)" -->')
TURTLE=re.compile(r'(?m)^```turtle\s*\n(.*?)^```\s*$',re.S|re.M)
MERMAID=re.compile(r'(?m)^```mermaid\s*\n(.*?)^```\s*$',re.S|re.M)
CORE=Namespace('https://w3id.org/ddta/core#')
PROCESS=Namespace('https://w3id.org/ddta/process#')

def sha(v:bytes)->str:return hashlib.sha256(v).hexdigest().upper()

def gather(s:str):
    markers=list(MARK.finditer(s))
    if len(markers)!=17 or [int(x.group(1)) for x in markers]!=list(range(1,18)):
        raise ValueError('Attesi 17 marcatori univoci PROCESS-EXAMPLE-01..17 ordinati')
    res=[]
    for i,m in enumerate(markers):
        end=markers[i+1].start() if i<len(markers)-1 else len(s)
        sec=s[m.end():end];tt=list(TURTLE.finditer(sec));mm=list(MERMAID.finditer(sec))
        if len(tt)!=1 or len(mm)!=1 or tt[0].end()>mm[0].start():
            raise ValueError(f'ESEMPIO_{i+1:02d}: occorre un Turtle prima di un Mermaid')
        ttl=tt[0];graph=mm[0]
        span=(m.end()+graph.start(1),m.end()+graph.end(1))
        res.append({'number':i+1,'rule':m.group(2),'turtle':ttl.group(1),'old':graph.group(1),'span':span})
    return res

def run(command, env=None):
    r=subprocess.run(command,text=True,capture_output=True,encoding='utf8',errors='replace',env=env)
    if r.returncode:raise RuntimeError(f'Command failed (exit {r.returncode}): {r.stderr[-1800:]} {r.stdout[-800:]}')

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--guide',required=True,type=Path)
    ap.add_argument('--core-guide',required=True,type=Path)
    ap.add_argument('--core-src',required=True,type=Path,help='Directory containing package ddta_viz')
    ap.add_argument('--process-renderer',required=True,type=Path)
    ap.add_argument('--core-baseline',required=True,type=Path,help='Explicit Turtle with zero triples')
    ap.add_argument('--out-dir',required=True,type=Path)
    ap.add_argument('--mode',choices=('preview','check','apply'),default='preview')
    args=ap.parse_args(argv)
    for key in ('guide','core_guide','process_renderer','core_baseline'):
        setattr(args,key,getattr(args,key).resolve(strict=True))
    args.core_src=args.core_src.resolve(strict=True)
    if not (args.core_src/'ddta_viz/pipeline.py').is_file():raise ValueError('CORE renderer package missing')
    g0=Graph().parse(str(args.core_baseline),format='turtle')
    if len(g0)!=0:raise ValueError('Baseline CORE not empty: do not add fictitious RDF instances')
    content=args.guide.read_bytes();original=content.decode('utf-8-sig').replace('\r\n','\n')
    examples=gather(original)
    out=args.out_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    env=os.environ.copy();env['PYTHONPATH']=str(args.core_src)+(os.pathsep+env['PYTHONPATH'] if env.get('PYTHONPATH') else '')
    common=out/'CORE_EMPTY';common.mkdir(exist_ok=True)
    run([sys.executable,'-m','ddta_viz.pipeline','--guides-md',str(args.core_guide),'--ttl',str(args.core_baseline),'--out-dir',str(common)],env)
    graph_core=common/'05_graph.mmd'
    edits=[];reports=[]
    # Rendering runs twice in independent output dirs. The first output is published
    # only if it matches the second byte-for-byte.
    for item in examples:
        number=item['number'];folder=out/f'ESEMPIO_{number:02d}';folder.mkdir(parents=True,exist_ok=True)
        src=folder/'source.ttl';src.write_text(item['turtle'],encoding='utf8',newline='\n')
        rdf=Graph().parse(str(src),format='turtle')
        left=folder/'first';right=folder/'second'
        command=[sys.executable,str(args.process_renderer),'--core-ttl',str(args.core_baseline),
                 '--core-guide',str(args.core_guide),'--process-ttl',str(src),
                 '--process-guide',str(args.guide),'--core-mermaid',str(graph_core)]
        for dest in (left,right):run(command+['--out-dir',str(dest)])
        mmd=(left/'05_graph.mmd').read_bytes()
        if mmd!=(right/'05_graph.mmd').read_bytes():raise RuntimeError(f'ESEMPIO_{number:02d}: nondeterministic Mermaid')
        body=mmd.decode('utf8')
        (folder/'05_graph.mmd').write_bytes(mmd)
        (folder/'05_graph.md').write_text('```mermaid\n'+body.rstrip('\n')+'\n```\n',encoding='utf8',newline='\n')
        edits.append((item['span'][0],item['span'][1],body))
        reports.append({'example':f'ESEMPIO_{number:02d}','rule':item['rule'],'triples':len(rdf),'graphSha256':sha(mmd),
                        'deterministic':True,'drift':body!=item['old']})
        print(f'ESEMPIO_{number:02d}: {len(rdf)} triple, drift={body!=item["old"]}, deterministic=True',flush=True)
    updated=original
    for start,end,body in reversed(edits):updated=updated[:start]+body+updated[end:]
    bom=content.startswith(b'\xef\xbb\xbf');crlf=b'\r\n' in content
    data=(b'\xef\xbb\xbf' if bom else b'')+(updated.replace('\n','\r\n') if crlf else updated).encode('utf8')
    (out/'DDTA_PROCESS_VISUALIZATION_RIGENERATA.md').write_bytes(data)
    diff=''.join(difflib.unified_diff(original.splitlines(True),updated.splitlines(True),
                                      fromfile='GUIDA_PROCESS_ATTUALE',tofile='GUIDA_PROCESS_RIGENERATA'))
    (out/'GUIDA_PROCESS_DIFF.patch').write_text(diff,encoding='utf8',newline='\n')
    report={'rules':len(examples),'drift':sum(r['drift'] for r in reports),'deterministic':True,'guideSha256Before':sha(content),
            'guideSha256Candidate':sha(data),'coreBaselineTriples':0,'examples':reports}
    (out/'REPORT.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf8',newline='\n')
    print(json.dumps({k:v for k,v in report.items() if k!='examples'},indent=2,ensure_ascii=False),flush=True)
    if args.mode=='check' and data!=content:
        print('CHECK FAIL: regenerated Mermaid differs from current guide',file=sys.stderr);return 2
    if args.mode=='apply':
        if args.guide.read_bytes()!=content:raise RuntimeError('Guide edited during regeneration')
        backup=args.guide.with_name(args.guide.name+'.BACKUP_'+datetime.now().strftime('%Y%m%d_%H%M%S'))
        shutil.copy2(args.guide,backup);args.guide.write_bytes(data)
        print('APPLIED:',args.guide,'BACKUP:',backup)
    return 0

if __name__=='__main__':
    try:sys.exit(main())
    except (OSError,ValueError,RuntimeError) as e:
        print('ERROR:',e,file=sys.stderr);sys.exit(1)
