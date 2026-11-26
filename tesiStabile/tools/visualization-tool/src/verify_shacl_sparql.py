#!/usr/bin/env python3
"""Run normative SHACL SPARQL and property-cardinality checks via RDFLib.

This is NOT a replacement for an independent pySHACL processor. It verifies
that each encoded query and property-count rule behaves on test graphs.
"""
from pathlib import Path
import sys, re
from rdflib import Graph, RDF, Namespace, Literal
from process_shacl import compile_shapes, SH
ROOT=Path(__file__).resolve().parents[1]
CORE=Namespace('https://w3id.org/ddta/core#')
PR=Namespace('https://w3id.org/ddta/process#')
EX=Namespace('https://example.org/ddta/plate-gate#')

def graph():
    g=Graph().parse(str(ROOT/'examples/00_PLATE_GATE_CORE_BASELINE.ttl'),format='turtle')
    g.parse(str(ROOT/'examples/02_RECOGNIZE_PLATE_PROCESS_R6_CANDIDATA.ttl'),format='turtle')
    return g

def violations(g,shapes):
    out=set()
    for shape in shapes.subjects(RDF.type,SH.NodeShape):
        targets=sorted(set(g.subjects(RDF.type,shapes.value(shape,SH.targetClass))),key=str)
        if not targets:continue
        for sp in shapes.objects(shape,SH.sparql):
            query=str(shapes.value(sp,SH.select)).replace('$this','?this')
            query=query.replace('WHERE {','WHERE { VALUES ?this { '+ ' '.join('<'+str(x)+'>' for x in targets)+' } ',1)
            rows=list(g.query(query))
            if rows:out.add(str(sp).rsplit('#',1)[-1])
        for prop_shape in shapes.objects(shape,SH.property):
            path=shapes.value(prop_shape,SH.path)
            lo=shapes.value(prop_shape,SH.minCount)
            hi=shapes.value(prop_shape,SH.maxCount)
            if any((lo is not None and len(set(g.objects(target,path)))<int(lo)) or
                   (hi is not None and len(set(g.objects(target,path)))>int(hi)) for target in targets):
                out.add(str(prop_shape).rsplit('#',1)[-1])
    return out

def run():
    shapes=compile_shapes(ROOT/'ontologies/process/DDTA_PROCESS.md')
    test=[]
    g=graph();test.append(('baseline',violations(g,shapes),set()))
    g=graph();g.remove((EX.ModelAgreementXor,PR.hasFalseNextStep,None))
    test.append(('missing_false_branch',violations(g,shapes),{'PRC-CTRL-03'}))
    g=graph();g.remove((EX.ConcurrentOCRSplit,PR.requiredCount,None));g.add((EX.ConcurrentOCRSplit,PR.requiredCount,Literal(3)))
    test.append(('threshold_3_of_2',violations(g,shapes),{'PRC-SYNC-06'}))
    g=graph();g.add((EX.RecognizePlateNumberProcess,PR.hasInitialStep,EX.NonMember))
    test.append(('nonmember_start',violations(g,shapes),{'PRC-COMP-02'}))
    g=graph();g.parse(str(ROOT/'examples/03_R8_COMPOSITION_TEST.ttl'),format='turtle');g.add((EX.ChildProcessTest,PR.hasSubProcess,EX.ParentProcessTest))
    test.append(('cyclic_subprocess',violations(g,shapes),{'PRC-COMP-01'}))
    g=graph();g.add((EX.InvokeRetrainingStep,PR.invokesProcess,EX.AnotherProcess))
    test.append(('too_many_invocations',violations(g,shapes),{'PRC-COMP-03_P1'}))
    g=graph();atom=sorted(g.subjects(RDF.type,PR.AtomicCondition),key=str)[0];g.remove((atom,PR.comparisonOperator,None));g.add((atom,PR.comparisonOperator,Literal('BOGUS')))
    test.append(('invalid_comparison',violations(g,shapes),{'PRC-ATOM-02'}))
    errors=[]
    for name,observed,expected in test:
        ok=observed==expected
        print(('PASS' if ok else 'FAIL'),name,'violazioni:',','.join(sorted(observed)) or 'nessuna')
        if not ok:errors.append(name)
    print('RDFLib:',len(test)-len(errors),'/',len(test),'casi; SHACL standard ancora da verificare con pySHACL')
    return bool(errors)

if __name__=='__main__':sys.exit(int(run()))
