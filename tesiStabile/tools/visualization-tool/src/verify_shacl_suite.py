#!/usr/bin/env python3
"""Independent pySHACL positive/negative test suite. Requires requirements-shacl.txt.

The graph is synthetic whenever a negative mutation is applied. No baseline or
repository files are changed. Shapes are compiled directly from normative YAML.
"""
from pathlib import Path
import sys
from rdflib import Graph, RDF, Namespace, Literal
from process_shacl import compile_shapes

ROOT=Path(__file__).resolve().parents[1]
CORE=Namespace('https://w3id.org/ddta/core#')
PR=Namespace('https://w3id.org/ddta/process#')
EX=Namespace('https://example.org/ddta/plate-gate#')

def base_graph():
    graph=Graph().parse(str(ROOT/'examples/00_PLATE_GATE_CORE_BASELINE.ttl'),format='turtle')
    graph.parse(str(ROOT/'examples/02_RECOGNIZE_PLATE_PROCESS_R6_CANDIDATA.ttl'),format='turtle')
    return graph

def all_cases():
    yield 'baseline',lambda g:None,True,''
    def missing_branch(g):g.remove((EX.ModelAgreementXor,PR.hasFalseNextStep,None))
    yield 'missing_false_branch',missing_branch,False,'PRC-CTRL-03'
    def invalid_threshold(g):
        g.remove((EX.ConcurrentOCRSplit,PR.requiredCount,None))
        g.add((EX.ConcurrentOCRSplit,PR.requiredCount,Literal(3)))
    yield 'threshold_3_of_2',invalid_threshold,False,'PRC-SYNC-06'
    def foreign_initial(g):
        g.add((EX.RecognizePlateNumberProcess,PR.hasInitialStep,EX.UnknownExternalStep))
    yield 'start_outside_process',foreign_initial,False,'PRC-COMP-02'
    def subprocess_cycle(g):
        g.parse(str(ROOT/'examples/03_R8_COMPOSITION_TEST.ttl'),format='turtle')
        g.add((EX.ChildProcessTest,PR.hasSubProcess,EX.ParentProcessTest))
    yield 'subprocess_cycle',subprocess_cycle,False,'PRC-COMP-01'
    def invalid_operator(g):
        targets=sorted(g.subjects(RDF.type,PR.AtomicCondition),key=str)
        if not targets:raise ValueError('No AtomicCondition found in baseline')
        x=targets[0];g.remove((x,PR.comparisonOperator,None));g.add((x,PR.comparisonOperator,Literal('INVALID')))
    yield 'invalid_atomic_operator',invalid_operator,False,'PRC-ATOM-02'

def main():
    try:
        from pyshacl import validate
    except ImportError:
        print('NON ESEGUITO: pySHACL assente. Eseguire `python -m pip install -r requirements-shacl.txt`.',file=sys.stderr)
        return 2
    shapes=compile_shapes(ROOT/'ontologies/process/DDTA_PROCESS.md')
    errors=[]
    for name,mutator,expected,rule_id in all_cases():
        g=base_graph();mutator(g)
        conforms,report,_=validate(g,shacl_graph=shapes,inference='none',abort_on_first=False)
        report_text=report.serialize(format='turtle')
        if bool(conforms)!=expected or (rule_id and rule_id not in report_text):
            errors.append(name)
            print('FAIL:',name,'conforms=',conforms,'expected=',expected,'rule=',rule_id)
            print(report_text[:2000])
        else:
            print('PASS:',name,'conforms=',conforms,'rule=',rule_id or 'none')
    print('RIEPILOGO:',len(tuple(all_cases()))-len(errors),'/',len(tuple(all_cases())),'casi SHACL indipendenti')
    return 1 if errors else 0

if __name__=='__main__':sys.exit(main())
