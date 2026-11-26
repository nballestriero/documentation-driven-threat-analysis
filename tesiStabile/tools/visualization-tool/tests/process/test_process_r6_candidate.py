"""Regression tests for R6 compound ControlNode and intermediate contracts."""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from rdflib import Graph, Namespace, RDF, URIRef, Literal

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from ddta_process import project, ProcessRenderer, stable

CORE=ROOT/'tests/fixtures/process/examples/00_PLATE_GATE_CORE_BASELINE.ttl'
PROCESS=ROOT/'tests/fixtures/process/examples/02_RECOGNIZE_PLATE_PROCESS_R6_CANDIDATA.ttl'
GUIDE=ROOT.parents[1]/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'
CORE_GUIDE=ROOT.parents[1]/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
ONTOLOGY=ROOT.parents[1]/'ontologies/process/DDTA_PROCESS.md'
EX=Namespace('https://example.org/ddta/plate-gate#')
PR=Namespace('https://w3id.org/ddta/process#')
DDTA=Namespace('https://w3id.org/ddta/core#')

class TestR6CompoundControl(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g=Graph().parse(str(CORE),format='turtle')
        cls.g.parse(str(PROCESS),format='turtle')
        cls.ir=project(CORE,PROCESS,GUIDE)
        cls.fragment,cls.diag=ProcessRenderer(cls.ir,GUIDE,CORE_GUIDE,'extended').render()

    def test_no_synchronization_node_or_join_and_new_vocab(self):
        self.assertNotIn('iri: process:SynchronizationNode',ONTOLOGY.read_text('utf-8'))
        self.assertEqual(list(self.g.subjects(RDF.type,PR.SynchronizationNode)),[])
        self.assertNotIn((EX.RecognizePlateNumberProcess, DDTA.hasStep,EX.OCRReadingsJoin),self.g)
        self.assertEqual(len(list(self.g.objects(EX.ConcurrentOCRSplit,PR.hasParticipantStep))),2)
        self.assertEqual(len(list(self.g.objects(EX.ConcurrentOCRSplit,DDTA.hasNextStep))),1)

    def test_explicit_two_of_two_success(self):
        n=self.ir['nodes'][str(EX.ConcurrentOCRSplit)]
        self.assertEqual(n['controlKind'],'CONCURRENT_SPLIT')
        self.assertEqual(set(n['participantSteps']),{str(EX.ExtractPlateNumberStep),str(EX.VerifyPlateNumberStep)})
        self.assertEqual((n['joinPolicy'],n['requiredCount'],n['completionCriterion']),('N_OF_M','2','SUCCESS'))
        self.assertIn('2/2 · SUCCESS',self.fragment)
        self.assertEqual(self.fragment.count('([\"hasParticipantStep\"])'),2)
        self.assertIn(stable('control-region:'+str(EX.ConcurrentOCRSplit)),self.fragment)
        self.assertNotIn('OCRReadingsJoin',self.fragment)

    def test_control_flow_is_declared_not_derived(self):
        t=[t for t in self.ir['transitions'] if t['process']==str(EX.RecognizePlateNumberProcess)]
        self.assertEqual(len(t),9)
        self.assertEqual(len([x for x in t if x['sourceRelation']=='ddta:hasNextStep']),5)
        self.assertEqual(len([x for x in t if x.get('branch')]),4)
        self.assertEqual([x['to'] for x in t if x['from']==str(EX.ConcurrentOCRSplit)],[str(EX.ModelAgreementXor)])
        self.assertFalse(any(x['to'] in (str(EX.ExtractPlateNumberStep),str(EX.VerifyPlateNumberStep)) for x in t))

    def test_declared_input_and_output_contracts_reuse_core_identity(self):
        for ocr in (EX.ExtractPlateNumberStep,EX.VerifyPlateNumberStep):
            self.assertIn((ocr,PR.declaresInputContract,EX.PlateImageContract),self.g)
        self.assertIn((EX.ModelAgreementXor,PR.declaresInputContract,EX.PlateNumberContract),self.g)
        self.assertEqual(set(self.g.objects(EX.ModelAgreementXor,PR.declaresInputContract)),{EX.PlateNumberContract})
        self.assertEqual(len(self.ir['operandProvenance']),2)
        self.assertEqual({x['contractElement'] for x in self.ir['operandProvenance']}, {str(EX.PlateNumber)})
        expected={str(EX.ExtractPlateNumberStep),str(EX.VerifyPlateNumberStep)}
        for x in self.ir['operandProvenance']:
            self.assertIsNone(x['declaredOutputStep'])
            self.assertEqual(set(x['candidateOutputSteps']),expected)
        self.assertIn('PlateImageContract',self.fragment)
        self.assertIn('PlateNumberContract',self.fragment)
        self.assertNotIn('ExtractedPlateContract',self.fragment)
        self.assertNotIn('VerifiedPlateContract',self.fragment)

    def test_nominal_true_false_and_resources(self):
        self.assertEqual(len(self.diag['xorConditionHeaders']),2)
        self.assertIn('fast-plate-ocr',self.fragment)
        self.assertIn('PaddleOCR',self.fragment)
        self.assertTrue(any(x[1]=='#238636' for x in self.diag['processLinkStylesRelative']))
        self.assertTrue(any(x[1]=='#C62828' for x in self.diag['processLinkStylesRelative']))
        self.assertTrue(all(x['visibleGuard']==x['negativeGuard'] for x in self.diag['xorConditionHeaders']))

    def altered(self,func):
        g=Graph().parse(str(PROCESS),format='turtle')
        func(g)
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'modified.ttl'
            g.serialize(destination=p,format='turtle')
            return project(CORE,p,GUIDE)

    def test_invalid_four_of_three_rejected(self):
        with self.assertRaisesRegex(ValueError,'N_OF_M incoerente'):
            self.altered(lambda g: (g.remove((EX.ConcurrentOCRSplit,PR.requiredCount,None)), g.add((EX.ConcurrentOCRSplit,PR.requiredCount,Literal(4)))))

    def test_undeclared_member_must_fail_not_guess(self):
        with self.assertRaisesRegex(ValueError,'Partecipanti RDF non validi'):
            self.altered(lambda g: (g.remove((EX.ConcurrentOCRSplit,PR.hasParticipantStep,EX.VerifyPlateNumberStep)),g.add((EX.ConcurrentOCRSplit,PR.hasParticipantStep,EX.UnknownOCR))))

    def test_participant_dataflow_not_inferred(self):
        with self.assertRaisesRegex(ValueError,'Controllo composto richiede unico hasNextStep'):
            self.altered(lambda g: g.add((EX.ConcurrentOCRSplit,DDTA.hasNextStep,EX.ExtractPlateNumberStep)))

    def test_all_any_and_two_of_three_are_structurally_valid(self):
        for policy,count,third in [('ALL',None,False),('ANY',None,False),('N_OF_M',2,True)]:
            with self.subTest(policy=policy,third=third):
                def modify(g):
                    g.remove((EX.ConcurrentOCRSplit,PR.joinPolicy,None))
                    g.remove((EX.ConcurrentOCRSplit,PR.requiredCount,None))
                    g.add((EX.ConcurrentOCRSplit,PR.joinPolicy,Literal(policy)))
                    if count is not None:g.add((EX.ConcurrentOCRSplit,PR.requiredCount,Literal(count)))
                    if third:
                        g.add((EX.RecognizePlateNumberProcess,DDTA.hasStep,EX.OCR_C))
                        g.add((EX.OCR_C,RDF.type,DDTA.ProcessStep))
                        g.add((EX.ConcurrentOCRSplit,PR.hasParticipantStep,EX.OCR_C))
                ir=self.altered(modify)
                n=ir['nodes'][str(EX.ConcurrentOCRSplit)]
                self.assertEqual(n['joinPolicy'],policy)

    def test_rdf_order_independence(self):
        g=Graph().parse(str(PROCESS),format='turtle')
        triples=sorted(g.serialize(format='nt').splitlines())
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'reordered.nt'
            p.write_text('\n'.join(reversed(triples))+'\n','utf-8')
            # rdflib project reads turtle; N-triples is a turtle subset.
            ir=project(CORE,p,GUIDE)
            fragment,_=ProcessRenderer(ir,GUIDE,CORE_GUIDE,'extended').render()
            self.assertEqual(fragment,self.fragment)

if __name__=='__main__':unittest.main()
