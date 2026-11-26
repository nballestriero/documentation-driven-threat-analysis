"""Verify the YAML-driven projection of multiple entries and subprocess containment.

All examples here are synthetic; they are not facts about the plate-recognition system.
"""
from pathlib import Path
import sys, tempfile, unittest, re
from rdflib import Graph, RDF, Namespace

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from ddta_process import project, ProcessRenderer, stable
CORE=Namespace('https://w3id.org/ddta/core#')
PR=Namespace('https://w3id.org/ddta/process#')
EX=Namespace('https://example.org/ddta/plate-gate#')
CORE_FILE=ROOT/'tests/fixtures/process/examples/00_PLATE_GATE_CORE_BASELINE.ttl'
TTLF=ROOT/'tests/fixtures/process/examples/02_RECOGNIZE_PLATE_PROCESS_R6_CANDIDATA.ttl'
VIS=ROOT.parents[1]/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'
COREGUIDE=ROOT.parents[1]/'ontologies/core/DDTA_CORE_VISUALIZATION.md'

class GraphGaps(unittest.TestCase):
    def fixture(self, mutate=None, composition=False):
        g=Graph().parse(str(ROOT/'tests/fixtures/process/examples/03_R8_COMPOSITION_TEST.ttl') if composition else str(TTLF),format='turtle')
        if mutate:mutate(g)
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'test.ttl'
            p.write_text(g.serialize(format='turtle'),encoding='utf-8')
            ir=project(CORE_FILE,p,VIS)
            mermaid,_=ProcessRenderer(ir,VIS,COREGUIDE,'extended').render()
            return ir,mermaid

    def test_two_declared_entries_both_have_start_markers(self):
        def change(g):
            other=EX.SecondIndependentEntry
            p=EX.RecognizePlateNumberProcess
            g.add((other,RDF.type,CORE.ProcessStep))
            g.add((p,CORE.hasStep,other))
            g.add((p,PR.hasInitialStep,other))
        ir,graph=self.fixture(change)
        p=next(x for x in ir['processes'] if x['iri']==str(EX.RecognizePlateNumberProcess))
        self.assertEqual(p['initials'],sorted([str(EX.ReceivePlateImageStep),str(EX.SecondIndependentEntry)]))
        for entry in p['initials']:
            sid=stable('start-marker:'+p['iri']+':'+entry)
            self.assertEqual(graph.count(sid+'(["START"])'),1)
            self.assertIn(sid+' --> ',graph)
        self.assertEqual(graph.count('(["START"])'),2)  # no invented marker

    def test_second_entry_reached_from_first_does_not_duplicate_step(self):
        def change(g):
            g.add((EX.RecognizePlateNumberProcess,PR.hasInitialStep,EX.ReportDiscordanceStep))
        ir,graph=self.fixture(change)
        p=next(x for x in ir['processes'] if x['iri']==str(EX.RecognizePlateNumberProcess))
        self.assertEqual(len(p['initials']),2)
        self.assertEqual(graph.count(stable('start-marker:'+p['iri']+':'+str(EX.ReportDiscordanceStep))+'(["START"])'),1)

    def test_one_start_outside_process_rejected(self):
        def change(g):
            g.add((EX.RecognizePlateNumberProcess,PR.hasInitialStep,EX.NonMember))
        with self.assertRaisesRegex(ValueError,'fuori da hasStep'):
            self.fixture(change)

    def test_subprocess_nested_graph_without_invented_invocation(self):
        ir,graph=self.fixture(composition=True)
        parent=EX.ParentProcessTest;child=EX.ChildProcessTest
        self.assertEqual(next(p for p in ir['processes'] if p['iri']==str(parent))['subProcesses'],[str(child)])
        pid=stable(str(parent));cid=stable(str(child))
        self.assertEqual(graph.count('subgraph '+pid+'['),1)
        self.assertEqual(graph.count('subgraph '+cid+'['),1)
        self.assertLess(graph.find('subgraph '+pid+'['),graph.find('subgraph '+cid+'['))
        self.assertNotIn('invokesProcess',graph)

    def test_nested_subprocess_three_levels(self):
        def change(g):
            g.add((EX.ChildProcessTest,PR.hasSubProcess,EX.GrandchildProcessTest))
            g.add((EX.GrandchildProcessTest,RDF.type,CORE.Process))
            g.add((EX.GrandchildProcessTest,CORE.hasStep,EX.GrandchildStartTest))
            g.add((EX.GrandchildProcessTest,PR.hasInitialStep,EX.GrandchildStartTest))
            g.add((EX.GrandchildStartTest,RDF.type,CORE.ProcessStep))
        ir,graph=self.fixture(change,composition=True)
        locs=[graph.find('subgraph '+stable(str(x))+'[') for x in (EX.ParentProcessTest,EX.ChildProcessTest,EX.GrandchildProcessTest)]
        self.assertEqual(locs,sorted(locs))
        self.assertTrue(all(p>=0 for p in locs))

    def test_composition_cycle_rejected(self):
        def change(g):g.add((EX.ChildProcessTest,PR.hasSubProcess,EX.ParentProcessTest))
        with self.assertRaisesRegex(ValueError,'ciclico'):
            self.fixture(change,composition=True)

    def test_multiple_parents_rejected_not_duplicated(self):
        def change(g):
            g.add((EX.OtherParentTest,RDF.type,CORE.Process))
            g.add((EX.OtherParentTest,PR.hasSubProcess,EX.ChildProcessTest))
        with self.assertRaisesRegex(ValueError,'piu contenitori visibili'):
            self.fixture(change,composition=True)

    def test_missing_subprocess_type_rejected(self):
        def change(g):g.add((EX.ParentProcessTest,PR.hasSubProcess,EX.UntypedProcessTest))
        with self.assertRaisesRegex(ValueError,'Process non dichiarato'):
            self.fixture(change,composition=True)

if __name__=='__main__':unittest.main()
