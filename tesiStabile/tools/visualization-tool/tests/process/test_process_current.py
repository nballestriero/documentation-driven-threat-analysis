"""Regression tests of the approved PROCESS vocabulary and graphical guide.

The fixture is a test graph, not the canonical plate-gate example document.
All checks are based on the currently approved docs and source RDF.
"""
import hashlib
import tempfile
import unittest
from pathlib import Path
from rdflib import Graph, Namespace, RDF
import sys

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from ddta_process import project, ProcessRenderer, compose, count_mermaid_edges

CORE=ROOT/'tests/fixtures/process/examples/00_PLATE_GATE_CORE_BASELINE.ttl'
PROCESS=ROOT/'tests/fixtures/process/examples/PLATE_GATE_PROCESS_TEST.ttl'
GUIDE=ROOT.parents[1]/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'
COREGUIDE=ROOT.parents[1]/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
DOC=ROOT.parents[1]/'ontologies/process/DDTA_PROCESS.md'
BASE=ROOT/'tests/fixtures/process/examples/CORE_BASE_GRAFO_SCELTO.mmd'
EX=Namespace('https://example.org/ddta/plate-gate#')
PR=Namespace('https://w3id.org/ddta/process#')
CORENS=Namespace('https://w3id.org/ddta/core#')

class CurrentProcessRendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ir=project(CORE,PROCESS,GUIDE)
        cls.compact,cls.comp_diag=ProcessRenderer(cls.ir,GUIDE,COREGUIDE,'compact').render()
        cls.extended,cls.ext_diag=ProcessRenderer(cls.ir,GUIDE,COREGUIDE,'extended').render()

    def test_approved_turtle_uses_direct_successors_not_named_transitions(self):
        g=Graph().parse(str(PROCESS),format='turtle')
        self.assertEqual(len(list(g.triples((None,PR.hasTrueNextStep,None)))),2)
        self.assertEqual(len(list(g.triples((None,PR.hasFalseNextStep,None)))),2)
        for predicate in (PR.hasTransition,PR.fromStep,PR.toStep,PR.hasGuard):
            self.assertFalse(any(g.triples((None,predicate,None))))
        self.assertFalse(any(g.triples((None,RDF.type,PR.ProcessTransition))))

    def test_reject_duplicate_direct_and_conditional_successor(self):
        from rdflib import Graph
        g=Graph().parse(str(PROCESS),format='turtle')
        g.add((EX.ModelAgreementXor,CORENS.hasNextStep,EX.EndAgreement))
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'invalid.ttl'
            g.serialize(destination=path,format='turtle')
            with self.assertRaisesRegex(ValueError,'Successione duplicata'):
                project(CORE,path,GUIDE)

    def test_reject_incomplete_xor_branch(self):
        g=Graph().parse(str(PROCESS),format='turtle')
        g.remove((EX.ModelAgreementXor,PR.hasFalseNextStep,EX.ReportDiscordanceStep))
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'invalid.ttl'
            g.serialize(destination=path,format='turtle')
            with self.assertRaisesRegex(ValueError,'Controllo binario incompleto'):
                project(CORE,path,GUIDE)

    def test_renderer_shows_current_semantic_properties(self):
        self.assertIn('hasNextStep',self.compact)
        self.assertIn('hasParticipantStep',self.compact)
        self.assertIn('invokesProcess',self.compact)
        self.assertIn('PlateNumberContract',self.compact)
        self.assertNotIn('ProcessTransition',self.compact)
        self.assertEqual(self.comp_diag['contractView'],'compact')
        self.assertEqual(self.ext_diag['contractView'],'extended')

    def test_shared_contract_element_does_not_invent_unique_producer(self):
        refs=self.ir['operandProvenance']
        self.assertEqual(len(refs),2)
        self.assertEqual({x['contractElement'] for x in refs},{str(EX.PlateNumber)})
        self.assertTrue(all(x['declaredOutputStep'] is None for x in refs))
        targets={str(EX.ExtractPlateNumberStep),str(EX.VerifyPlateNumberStep)}
        self.assertTrue(all(set(x['candidateOutputSteps'])==targets for x in refs))

    def test_render_immutable_inputs(self):
        targets=[CORE,PROCESS,GUIDE,COREGUIDE,BASE,DOC]
        before={str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in targets}
        ProcessRenderer(self.ir,GUIDE,COREGUIDE,'compact').render()
        ProcessRenderer(self.ir,GUIDE,COREGUIDE,'extended').render()
        after={str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in targets}
        self.assertEqual(before,after)

    def test_composition_deterministic_and_mermaid_indices_valid(self):
        ir=project(CORE,PROCESS,GUIDE)
        frag,diag=ProcessRenderer(ir,GUIDE,COREGUIDE,'extended').render()
        self.assertEqual(frag,self.extended)
        composed=compose(BASE,frag,ir,diag)
        import re
        count=count_mermaid_edges(composed)
        indexes=[int(x) for x in re.findall(r'linkStyle\s+(\d+)\s+stroke:',composed)]
        self.assertTrue(all(0<=x<count for x in indexes))
        self.assertEqual(len(indexes),len(set(indexes)))

if __name__=='__main__':unittest.main()
