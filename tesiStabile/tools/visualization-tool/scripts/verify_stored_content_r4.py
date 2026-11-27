#!/usr/bin/env python3
"""Verify independent vocabularies and regenerate the StoredContent examples.

This is a visual and authoring regression test, not an OWL compiler or a SHACL reasoner.
It uses the actual pipeline and the RDF/Markdown embedded in the current guides.
"""
from pathlib import Path
import argparse, difflib, json, re, subprocess, sys
import yaml
from rdflib import Graph, Namespace, RDF

TOOL=Path(__file__).resolve().parents[1]
ROOT=TOOL.parents[1]
CORE=Namespace('https://w3id.org/ddta/core#')
PROCESS=Namespace('https://w3id.org/ddta/process#')
DATA=Namespace('https://w3id.org/ddta/data#')
EX=Namespace('https://example.org/ddta/plate-gate#')
D=Namespace('https://example.org/ddta/data-example#')

def check(cond, message):
    if not cond: raise AssertionError(message)

def block(text, anchor, language):
    section=text.split(anchor,1)[1]
    return re.search(r'```'+re.escape(language)+r'\s*\n(.*?)\n```',section,re.S).group(1).rstrip('\n')+'\n'

def rdf(text): return Graph().parse(data=text,format='turtle')

def same_text(path, text):
    check(path.read_text(encoding='utf-8').rstrip('\n')==text.rstrip('\n'),f'Graph drift: {path}')

def inputs():
    docs={m:(ROOT/f'ontologies/{m}/DDTA_{m.upper()}.md').read_text(encoding='utf-8') for m in ('core','process','data')}
    rules={m:re.findall(r'```yaml (?:ddta-ontology|ontology-validation)\s*\n(.*?)\n```',t,re.S) for m,t in docs.items()}
    records={m:[yaml.safe_load(x) for x in re.findall(r'```yaml ddta-ontology\s*\n(.*?)\n```',t,re.S)] for m,t in docs.items()}
    names={m:{v['iri'] for r in rec for v in ([r] if r.get('iri') else r.get('properties',[]))} for m,rec in records.items()}
    refs={m:set(re.findall(r'\b(?:ddta|process|data):[A-Za-z][A-Za-z0-9_]*','\n'.join(rules[m]))) for m in docs}
    for m in ('core','process','data'):
        allowed=names['core']|names[m]
        check(refs[m]<=allowed,f'Undeclared or cross-module normative reference in {m}: {refs[m]-allowed}')
    cls=next(r for r in records['data'] if r.get('iri')=='data:DataBlock')
    check(cls['subClassOf']=='ddta:StoredContent','Incorrect DataBlock specialization')
    props={v['iri']:v for r in records['process'] for v in r.get('properties',[])}
    ref=props['process:referencesStoredContent']
    check(ref['domain']=='process:Operand' and ref['range']=='ddta:StoredContent','Wrong reference signature')
    check(props['process:referencesResource']['range']=='ddta:Resource','referencesResource changed')
    check(props['process:usesConfiguration']['range']=='ddta:Resource','usesConfiguration changed')
    dprops={v['iri']:v for r in records['data'] for v in r.get('properties',[])}
    for name in ('readsFrom','writesTo'):
        check(dprops['data:'+name]['range']=='ddta:StoredContent','DATA range changed: '+name)
    doc=(ROOT/'examples/plate-gate/DDTA_TARGA_COSTRUZIONE_PROGRESSIVA.md').read_text(encoding='utf-8')
    t13=block(doc,'### 13.2 Turtle cumulativo','turtle')
    t14=block(doc,'### 14.3 Turtle cumulativo','turtle')
    t15=block(doc,'### 15.3 Turtle cumulativo','turtle')
    g13,g14,g15=map(rdf,(t13,t14,t15))
    check((len(g13),len(g14),len(g15))==(132,177,186),'Unexpected cumulative RDF counts')
    check(set(g13)<=set(g14)<=set(g15),'Progression loses RDF statements')
    for n,prev,current in [(14,g13,g14),(15,g14,g15)]:
        d=rdf(block(doc,f'### {n}.2 Nuove dichiarazioni RDF','turtle'))
        check(set(d)==set(current)-set(prev),f'Delta mismatch at step {n}')
    check(set(g15)==set(Graph().parse(ROOT/'examples/plate-gate/PASSO15_DATA_R1.ttl')),'Standalone TTL differs from progressive example')
    approved={'data:StableStore','data:RunningStore','data:DataBlock','data:hasDataBlock','data:ReadStep','data:readsFrom','data:WriteStep','data:writesTo'}
    statuses={v['iri']:v['status'] for rec in records['data'] for v in ([rec] if rec.get('iri') else rec.get('properties',[]))}
    check({n for n,v in statuses.items() if v=='approved'}==approved,'Unapproved DATA declaration promoted or approved declaration lost')
    check(set(statuses)==approved and all(v=='approved' for v in statuses.values()),'DATA vocabulary must contain exactly eight approved declarations')
    check(set(g15.triples((None,DATA.readsFrom,None)))=={(EX.ReadOCRConfigurationStep,DATA.readsFrom,EX.OCRRetrainingConfigurationFile)},'Expected exactly the declared read')
    check((EX.ReadOCRConfigurationStep,RDF.type,DATA.ReadStep) in g15,'Missing ReadStep type')
    check(not list(g15.triples((None,DATA.writesTo,None))) ,'Unexpected write at step 15')
    q1=block(docs['data'],'**Query diagnostica illustrativa DATA-01','sparql')
    q4=block(docs['data'],'**Query diagnostica illustrativa DATA-04','sparql')
    check(not list(g15.query(q1)) and not list(g15.query(q4)),'Declared placement/access incomplete')
    negative=Graph();[negative.add(t) for t in g15]
    negative.remove((EX.OCRRetrainingConfigurationRuntime,DATA.hasDataBlock,EX.OCRRetrainingThresholdRuntime))
    check((EX.RetrainingThresholdOperand,EX.OCRRetrainingThresholdRuntime) in [tuple(r) for r in negative.query(q1)],'Missing placement diagnostic failed')
    negative.remove((EX.ReadOCRConfigurationStep,DATA.readsFrom,EX.OCRRetrainingConfigurationFile))
    check((EX.ReadOCRConfigurationStep,) in [tuple(r) for r in negative.query(q4)],'Missing read target diagnostic failed')
    expected={(EX.DisagreementCountOperand,PROCESS.referencesStoredContent,EX.OCRDisagreementCounterRuntime),(EX.RetrainingThresholdOperand,PROCESS.referencesStoredContent,EX.OCRRetrainingThresholdRuntime)}
    for g in (g14,g15):
        check(set(g.triples((None,PROCESS.referencesStoredContent,None)))==expected,'Reference identities changed')
        for operand,_,target in expected:
            check((target,RDF.type,CORE.StoredContent) in g,'Missing generic StoredContent type')
            check((target,RDF.type,CORE.Resource) not in g,'StoredContent wrongly typed Resource')
            check(not list(g.subjects(CORE.makesAvailable,target)),'StoredContent wrongly exposed as Resource')
            check(not list(g.objects(operand,PROCESS.referencesResource)),'Obsolete resource reference')
        check(not list(g.objects(EX.CheckOCRRetrainingThreshold,PROCESS.usesConfiguration)),'usesConfiguration targets content')
    for _,_,target in expected: check((target,RDF.type,DATA.DataBlock) in g15,'Missing DATA specialization')
    q=block(doc,'### 14.4 Query SPARQL','sparql');sel=Graph()
    for row in g14.query(q):sel.add(tuple(row))
    check(len(sel)==102 and expected<=set(sel),'Selective query misses references')
    # The DATA ontology example exercises a block as a read/write target without PROCESS.
    data_example=rdf(block(docs['data'],'## 9. Esempi integrativi','turtle'))
    for anchor,step in [('### 6.3 Interrogazioni SPARQL',D.ReadCounter),('### 7.3 Interrogazioni SPARQL',D.WriteCounter)]:
        rows=list(data_example.query(block(docs['data'],anchor,'sparql')))
        check((step,D.CounterValue,D.OperationalContentStore) in [tuple(r) for r in rows], 'Indirect Store lookup failed: '+anchor)
    pv=(ROOT/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md').read_text(encoding='utf-8')
    dv=(ROOT/'ontologies/data/DDTA_DATA_VISUALIZATION.md').read_text(encoding='utf-8')
    specs={
      'step14':(t14,True,True,block(doc,'### 14.7 Mermaid integrato','mermaid')),
      'step14_selected':(sel.serialize(format='turtle'),True,True,block(doc,'### 14.5 Mermaid PROCESS','mermaid')),
      'step15':(t15,True,True,block(doc,'### 15.4 Mermaid integrato','mermaid')),
      'step16':(block(doc,'### 16.3 Turtle cumulativo','turtle'),True,True,block(doc,'### 16.4 Mermaid integrato','mermaid')),
      'process_guide':(block(pv,'<!-- DDTA-PROCESS-INTEGRATED-EXAMPLE-01','turtle'),False,True,block(pv,'<!-- DDTA-PROCESS-INTEGRATED-EXAMPLE-01','mermaid')),
      'data_guide':(block(dv,'## 7. Esempio integrativo','turtle'),True,False,block(dv,'## 7. Esempio integrativo','mermaid')),
      'read_guide_data':(block(dv,'### 10.1 CORE + DATA','turtle'),True,False,block(dv,'### 10.1 CORE + DATA','mermaid')),
      'read_guide_integrated':(block(dv,'### 10.2 CORE + DATA + PROCESS','turtle'),True,True,block(dv,'### 10.2 CORE + DATA + PROCESS','mermaid')),
      'write_guide_data':(block(dv,'### 12.1 CORE + DATA','turtle'),True,False,block(dv,'### 12.1 CORE + DATA','mermaid')),
      'write_guide_integrated':(block(dv,'### 12.2 CORE + DATA + PROCESS','turtle'),True,True,block(dv,'### 12.2 CORE + DATA + PROCESS','mermaid')),
    }
    return specs

def run_pipeline(ttl, output, data, process):
    pipe=TOOL/'scripts/pipeline.py';core=ROOT/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
    args=[sys.executable,str(pipe)]
    if process:
        args+=['--core-generator',str(pipe),'--core-guide',str(core),'--process-guide',str(ROOT/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md')]
    else: args+=['--guides-md',str(core)]
    if data:args+=['--data-guide',str(ROOT/'ontologies/data/DDTA_DATA_VISUALIZATION.md')]
    args+=['--ttl',str(ttl),'--out-dir',str(output)]
    subprocess.run(args,check=True)

def check_read_edge(mmd,src,dst):
    matches=re.findall(r'^\s*'+re.escape(src)+r' --- (\w+) --> '+re.escape(dst)+r'\s*$',mmd,re.M)
    check(len(matches)==1,'Read edge missing or duplicated')
    label=matches[0]
    check(label+'(["readsFrom"])' in mmd,'Read label missing')
    check('stroke:#374151,stroke-width:1.8px,stroke-dasharray:6 4' in mmd,'Read style missing')

def validate_outputs(out,specs,r3_reference=None):
    for name,(_,_,process,expected) in specs.items():
        folder=out/name; target=folder/'core_process_extended/05_graph.mmd' if process else folder/'05_graph.mmd'
        same_text(target,expected)
        if process:
            man=json.loads((folder/'manifest.json').read_text())
            check(man['deterministicByteForByte'] and man['coreOnlyByteForByte'],'Pipeline deterministic regression failed: '+name)
        print('REFERENCE OK:',name,flush=True)
    for name in ('step14','step14_selected','step15','process_guide'):
        folder=out/name
        occ=json.loads((folder/'core/04_projection.json').read_text())['occurrences']
        if name in ('step14','step14_selected','step15'):
            pairs=[('OCRRetrainingThresholdRuntime','OCRRetrainingConfigurationRuntime'),('OCRDisagreementCounterRuntime','OCRRuntimeState'),('OCRRuntimeState','OCRRunningStore'),('OCRRetrainingConfigurationRuntime','OCRRunningStore')]
            if name != 'step14_selected': pairs.append(('OCRRetrainingConfigurationFile','OCRConfigurationStableStore'))
            for child,parent in pairs:
                c=occ[str(EX[child])]; p=occ[str(EX[parent])]
                check(len(c)==len(p)==1 and p[0]['id'] in c[0]['path'], 'Missing or duplicate containment: '+child)
            for view in ('compact','extended'):
                mm=(folder/f'core_process_{view}/05_graph.mmd').read_text()
                for child in ('OCRDisagreementCounterRuntime','OCRRetrainingThresholdRuntime'):
                    oid=occ[str(EX[child])][0]['id']
                    check(any(oid+'[' in line and 'data:DataBlock' in line for line in mm.splitlines()), 'Wrong displayed type: '+child)
        for view in ('compact','extended'):
            vf=folder/f'core_process_{view}';diag=json.loads((vf/'06_process_diagnostics.json').read_text());ir=json.loads((vf/'04_process_projection.json').read_text());mmd=(vf/'05_graph.mmd').read_text()
            trace=json.loads((vf/'07_rdf_trace.json').read_text())
            refs={(o['operandIRI'],o['storedContentIRI']) for o in trace['operandReferences'] if 'storedContentIRI' in o}
            check(len(refs)==2,'Missing trace for '+name)
            count=0
            for operand,target in sorted(refs):
                check(len(occ[target])==1,'Duplicated target '+target); dest=occ[target][0]['id']
                for src in diag['storedContentReferenceOccurrences'][operand]:
                    matches=re.findall(r'^\s*'+re.escape(src)+r' -\.-> (PX_[0-9a-f]+) -\.-> '+re.escape(dest)+r'\s*$',mmd,re.M)
                    check(len(matches)==1,'Reference must reach existing occurrence '+target)
                    check(matches[0]+'(["referencesStoredContent"])' in mmd,'Missing label node')
                    count+=1
            check(count==2,'Unexpected rendered references')
    # Verify the explicit read reaches the already-existing stored content occurrence,
    # including a DataBlock in the generic example. No detached replacement nodes.
    GE=Namespace('https://example.org/ddta/data-read-example#')
    for name,step,target,parent in [('step15',EX.ReadOCRConfigurationStep,EX.OCRRetrainingConfigurationFile,EX.OCRConfigurationStableStore),('read_guide_integrated',GE.ReadSettings,GE.LimitValue,GE.SettingsFile)]:
        folder=out/name;occ=json.loads((folder/'core/04_projection.json').read_text())['occurrences']
        c,p=occ[str(target)],occ[str(parent)]
        check(len(c)==len(p)==1 and p[0]['id'] in c[0]['path'],'Read target lost containment: '+name)
        import hashlib
        source='PX_'+hashlib.sha256(str(step).encode('utf-8')).hexdigest()[:12]
        for view in ('compact','extended'):
            vf=folder/f'core_process_{view}';mmd=(vf/'05_graph.mmd').read_text()
            check_read_edge(mmd,source,c[0]['id'])
            check(any(source+'[' in x and 'data:ReadStep' in x for x in mmd.splitlines()),'ReadStep display type missing: '+name)
            trace=json.loads((vf/'07_rdf_trace.json').read_text())
            check(trace['dataAccessReferences']==[{'stepIRI':str(step),'rdfPredicate':str(DATA.readsFrom),'storedContentIRI':str(target)}],'Read edge RDF trace missing: '+name)
    folder=out/'read_guide_data';occ=json.loads((folder/'04_projection.json').read_text())['occurrences'];src=occ[str(GE.ReadSettings)][0]['id'];dst=occ[str(GE.LimitValue)][0]['id']
    check_read_edge((folder/'05_graph.mmd').read_text(),src,dst)
    print('PASS: read edges target existing contained occurrences; generic CORE+DATA and integrated examples',flush=True)
    if r3_reference:
        for view in ('compact','extended'):
            before=(r3_reference/f'PASSO15_{view}.mmd').read_text().splitlines();after=(out/'step14'/f'core_process_{view}'/'05_graph.mmd').read_text().splitlines()
            ops=[(tag,a,b,c,d) for tag,a,b,c,d in difflib.SequenceMatcher(None,before,after,autojunk=False).get_opcodes() if tag!='equal']
            check(all(tag=='insert' for tag,*_ in ops),'R3 regression: existing graphics changed')
            add=[line.strip() for tag,a,b,c,d in ops for line in after[c:d]]
            check(len(add)==10 and sum('(["referencesStoredContent"])' in x for x in add)==2 and sum(' -.-> ' in x for x in add)==2 and sum(x.startswith('style ') for x in add)==2 and sum(x.startswith('linkStyle ') for x in add)==4,'Unexpected R3 delta')
            print('R3 reference preserved:',view,'(only two new references and styles)',flush=True)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out-dir',required=True,type=Path);ap.add_argument('--r3-reference',type=Path);ap.add_argument('--check-existing',action='store_true',help='Check already generated artifacts; does not execute the pipeline');a=ap.parse_args();out=a.out_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    specs=inputs();print('PASS: module vocabulary independence, RDF progression, SPARQL, reference signatures',flush=True)
    if not a.check_existing:
        for name,(text,data,process,_) in specs.items():
            ttl=out/(name+'.ttl');ttl.write_text(text,encoding='utf-8',newline='\n');run_pipeline(ttl,out/name,data,process)
            if not process:
                run_pipeline(ttl,out/(name+'_repeat'),data,process)
                check((out/name/'05_graph.mmd').read_bytes()==(out/(name+'_repeat')/'05_graph.mmd').read_bytes(),'DATA standalone nondeterministic')
    validate_outputs(out,specs,a.r3_reference)
    print('PASS: DATA R8 checks',flush=True)
if __name__=='__main__':main()
