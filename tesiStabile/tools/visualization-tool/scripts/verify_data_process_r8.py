#!/usr/bin/env python3
"""Verify DATA-01 and the write projection. No external SHACL engine required."""
from pathlib import Path
import argparse, json, subprocess, sys, tempfile, hashlib
from rdflib import Graph, Namespace, RDF
TOOL=Path(__file__).resolve().parents[1]
ROOT=TOOL.parents[1]
sys.path.insert(0,str(TOOL/'src'))
from data_process_validation import violations
from verify_stored_content_r4 import block, rdf
C=Namespace('https://w3id.org/ddta/core#')
D=Namespace('https://w3id.org/ddta/data#')
P=Namespace('https://w3id.org/ddta/process#')
E=Namespace('https://example.org/ddta/plate-gate#')
X=Namespace('https://example.org/validation#')

def check(cond,msg):
    if not cond: raise AssertionError(msg)

def cases():
    for name,kind,contained,block_target,expected in [
        ('stable file',D.StableStore,True,False,False),
        ('stable block',D.StableStore,True,True,False),
        ('unplaced',D.RunningStore,False,False,False),
        ('running file',D.RunningStore,True,False,True),
        ('running block',D.RunningStore,True,True,True)]:
        g=Graph();g.add((X.store,RDF.type,kind));g.add((X.file,RDF.type,C.StoredContent));g.add((X.block,RDF.type,D.DataBlock));g.add((X.file,D.hasDataBlock,X.block))
        if contained:g.add((X.store,C.stores,X.file))
        # No explicit Operand type: targetSubjectsOf still catches a reference.
        g.add((X.operand,P.referencesStoredContent,X.block if block_target else X.file))
        check((not violations(g))==expected,name); print('PASS:',name)
    g=Graph();g.add((X.store,RDF.type,D.RunningStore));g.add((X.store,C.stores,X.nested));g.add((X.nested,C.stores,X.file));g.add((X.file,D.hasDataBlock,X.block));g.add((X.operand,P.referencesStoredContent,X.block));check(not violations(g),'nested stores');print('PASS: nested store and block')
    for pred,step,kind in [(D.readsFrom,D.ReadStep,D.StableStore),(D.writesTo,D.WriteStep,D.RunningStore),(D.writesTo,D.WriteStep,D.StableStore)]:
        g=Graph();g.add((X.store,RDF.type,kind));g.add((X.store,C.stores,X.file));g.add((X.step,RDF.type,step));g.add((X.step,pred,X.file));check(not violations(g),'access exception');print('PASS: access exception',pred,kind)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out-dir',type=Path,required=True);a=ap.parse_args();cases()
    doc=(ROOT/'examples/plate-gate/DDTA_TARGA_COSTRUZIONE_PROGRESSIVA.md').read_text(encoding='utf8')
    g15=rdf(block(doc,'### 15.3 Turtle cumulativo','turtle'));g16=rdf(block(doc,'### 16.3 Turtle cumulativo','turtle'));delta=rdf(block(doc,'### 16.2 Nuove dichiarazioni RDF','turtle'))
    check(len(g16)==191 and set(g16)-set(g15)==set(delta) and set(g15)<=set(g16),'RDF progression')
    check(set(g16)==set(Graph().parse(ROOT/'examples/plate-gate/PASSO16_DATA_R1.ttl',format='turtle')),'standalone TTL')
    check(not violations(g16),'step16 invalid');print('PASS: cumulative step 16')
    folder=a.out_dir/'step16';occ=json.loads((folder/'core/04_projection.json').read_text())['occurrences'];target=occ[str(E.OCRRetrainingConfigurationRuntime)];parent=occ[str(E.OCRRunningStore)]
    check(len(target)==len(parent)==1 and parent[0]['id'] in target[0]['path'],'write target containment')
    src='PX_'+hashlib.sha256(str(E.WriteOCRConfigurationStep).encode()).hexdigest()[:12]
    for view in ('compact','extended'):
        v=folder/f'core_process_{view}';m=(v/'05_graph.mmd').read_text();import re
        match=re.findall(r'^\s*'+src+r' --- (\w+) --> '+target[0]['id']+r'\s*$',m,re.M)
        check(len(match)==1 and match[0]+'(["writesTo"])' in m,'write edge')
        check(any(src+'[' in x and 'data:WriteStep' in x for x in m.splitlines()),'write type')
        trace=json.loads((v/'07_rdf_trace.json').read_text())['dataAccessReferences'];check({'stepIRI':str(E.WriteOCRConfigurationStep),'rdfPredicate':str(D.writesTo),'storedContentIRI':str(E.OCRRetrainingConfigurationRuntime)} in trace,'write trace')
    print('PASS: writesTo reaches existing contained occurrence')
    # Same actual pipeline must reject a mutated otherwise-valid graph before creating output.
    g16.remove((E.RetrainingThresholdOperand,P.referencesStoredContent,E.OCRRetrainingThresholdRuntime));g16.add((E.RetrainingThresholdOperand,P.referencesStoredContent,E.OCRRetrainingConfigurationFile))
    with tempfile.TemporaryDirectory() as temp:
        p=Path(temp);ttl=p/'invalid.ttl';g16.serialize(ttl,format='turtle');out=p/'out';pipe=TOOL/'scripts/pipeline.py'
        args=[sys.executable,str(pipe),'--core-generator',str(pipe),'--core-guide',str(ROOT/'ontologies/core/DDTA_CORE_VISUALIZATION.md'),'--process-guide',str(ROOT/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'),'--data-guide',str(ROOT/'ontologies/data/DDTA_DATA_VISUALIZATION.md'),'--ttl',str(ttl),'--out-dir',str(out)]
        for command in (args,args[:args.index('--data-guide')]+args[args.index('--data-guide')+2:]):
            result=subprocess.run(command,capture_output=True,text=True,encoding='utf8',errors='replace')
            check(result.returncode!=0 and 'ERROR DATA-01' in result.stderr and not out.exists(),'pipeline failed to reject invalid TTL before rendering')
        print('PASS: invalid plate-gate TTL blocked by actual pipeline, with and without --data-guide')
if __name__=='__main__':main()
