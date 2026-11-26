"""Candidate R5 concept audit: no silent promotion of proposed properties."""
import sys, unittest, re, yaml
from pathlib import Path
from rdflib import Graph, RDF, Namespace
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'src'))
from ddta_process import project, ProcessRenderer
ROOT=Path(__file__).resolve().parents[2]
DOC=ROOT.parents[1]/'ontologies/process/DDTA_PROCESS.md'
CORE=ROOT/'tests/fixtures/process/examples/00_PLATE_GATE_CORE_BASELINE.ttl'
TTL=ROOT/'tests/fixtures/process/examples/02_RECOGNIZE_PLATE_PROCESS_R5_CANDIDATA.ttl'
GUIDE=ROOT/'tests/fixtures/process/legacy/DDTA_PROCESS_VISUALIZATION_R79.md'
CORE_GUIDE=ROOT.parents[1]/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
DDTA=Namespace('https://w3id.org/ddta/core#')
PR=Namespace('https://w3id.org/ddta/process#')
EX=Namespace('https://example.org/ddta/plate-gate#')
class CandidateR5(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.g=Graph().parse(str(TTL),format='turtle')
 def test_normative_vocabulary_no_retired_terms(self):
  data=DOC.read_text('utf-8')
  specs=[yaml.safe_load(x) for x in re.findall(r'```yaml ddta-ontology\s*\n(.*?)\n```',data,re.S)]
  iris=[]
  for spec in specs:
   if spec['record']=='class':iris.append(spec['iri'])
   elif spec['record'] in ('object-properties','datatype-properties'):
    iris.extend(p['iri'] for p in spec['properties'])
  self.assertEqual(len(iris),len(set(iris)))
  for retired in ('process:Condition','process:CompositeCondition','process:hasActivationCondition','process:hasCondition','process:logicalOperator'):
   self.assertNotIn(retired,iris)
  for k in ('process:AtomicCondition','process:ControlNode','process:hasTrueNextStep','process:hasFalseNextStep','process:evaluatesCondition'):
   self.assertIn(k,iris)
 def test_turtle_no_retired_entities_and_explicit_branches(self):
  g=self.g
  for p in (PR.hasActivationCondition,PR.hasTransition,PR.hasGuard,PR.hasCondition,PR.logicalOperator):
   self.assertFalse(list(g.triples((None,p,None))))
  self.assertFalse(list(g.subjects(RDF.type,PR.CompositeCondition)))
  self.assertFalse(list(g.subjects(RDF.type,PR.Condition)))
  for s,crit,yes,no in ((EX.ModelAgreementXor,EX.ModelResultsAgree,EX.EndAgreement,EX.ReportDiscordanceStep),
                         (EX.RetrainingThresholdXor,EX.AtLeastTenDiscordances,EX.InvokeRetrainingStep,EX.EndDiscordance)):
   self.assertIn((s,PR.evaluatesCondition,crit),g)
   self.assertIn((s,PR.hasTrueNextStep,yes),g)
   self.assertIn((s,PR.hasFalseNextStep,no),g)
   self.assertNotIn((s,DDTA.hasNextStep,yes),g)
  self.assertIn((EX.ReceivePlateImageStep,DDTA.hasNextStep,EX.ConcurrentOCRSplit),g)
  self.assertIn((EX.OCRReadingsJoin,DDTA.hasNextStep,EX.ModelAgreementXor),g)
 def test_projection_recovers_complete_control_topology(self):
  ir=project(CORE,TTL,GUIDE)
  main=next(p for p in ir['processes'] if p['name']=='RecognizePlateNumberProcess')
  paths=[t for t in ir['transitions'] if t['process']==main['iri']]
  self.assertEqual(len(paths),13)
  self.assertEqual(len([t for t in paths if t['sourceRelation']=='ddta:hasNextStep']),9)
  self.assertEqual(len([t for t in paths if t['branch'] in ('TRUE','FALSE')]),4)
  self.assertTrue(all(t['iri'] is None for t in paths))
  self.assertEqual(len(ir['conditions']),2)
  self.assertEqual(ir['nodes'][str(EX.OCRReadingsJoin)]['requiredCount'],'2')
  code,meta=ProcessRenderer(ir,GUIDE,CORE_GUIDE,'extended').render()
  self.assertTrue(meta['allProcessStepsShown'])
  self.assertIn('hasNextStep',code)
  self.assertEqual(len(meta['xorConditionHeaders']),2)
  self.assertEqual(len(meta['operandProvenance']),2)
  self.assertIn('#238636',[color for _,color in meta['processLinkStylesRelative']])
  self.assertIn('#C62828',[color for _,color in meta['processLinkStylesRelative']])
 def test_fail_on_duplicate_branch_and_core_link(self):
  import tempfile
  g=Graph().parse(str(TTL),format='turtle')
  g.add((EX.ModelAgreementXor,DDTA.hasNextStep,EX.EndAgreement))
  with tempfile.TemporaryDirectory() as temp:
   p=Path(temp)/'duplicate.ttl';g.serialize(destination=p,format='turtle')
   with self.assertRaisesRegex(ValueError,'Successione duplicata'):
    project(CORE,p,GUIDE)
 def test_fail_on_incomplete_binary_control(self):
  import tempfile
  g=Graph().parse(str(TTL),format='turtle')
  g.remove((EX.ModelAgreementXor,PR.hasFalseNextStep,EX.ReportDiscordanceStep))
  with tempfile.TemporaryDirectory() as temp:
   p=Path(temp)/'missing.ttl';g.serialize(destination=p,format='turtle')
   with self.assertRaisesRegex(ValueError,'Controllo binario incompleto'):
    project(CORE,p,GUIDE)

if __name__=='__main__':unittest.main()
