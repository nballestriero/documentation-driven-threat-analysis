"""Consolidation checks: ontology lifecycle, START, configuration and SHACL SPARQL."""
import re,sys,tempfile,unittest
from pathlib import Path
from rdflib import Graph, RDF, Namespace, URIRef, Literal
from rdflib.plugins.sparql.parser import parseQuery

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from ddta_process import project, ProcessRenderer, stable
from process_shacl import compile_shapes
DDTA=Namespace('https://w3id.org/ddta/core#')
PR=Namespace('https://w3id.org/ddta/process#')
EX=Namespace('https://example.org/ddta/plate-gate#')
SH=Namespace('http://www.w3.org/ns/shacl#')
CORE=ROOT/'tests/fixtures/process/examples/00_PLATE_GATE_CORE_BASELINE.ttl'
PROCESS=ROOT/'tests/fixtures/process/examples/02_RECOGNIZE_PLATE_PROCESS_R6_CANDIDATA.ttl'
GUIDE=ROOT.parents[1]/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'
CORE_GUIDE=ROOT.parents[1]/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
DOC=ROOT.parents[1]/'ontologies/process/DDTA_PROCESS.md'

class Consolidamento(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g=Graph().parse(str(CORE),format='turtle')
        cls.g.parse(str(PROCESS),format='turtle')
        cls.ir=project(CORE,PROCESS,GUIDE)
        cls.shapes=compile_shapes(DOC)

    def test_approved_control_properties_and_transition_removed(self):
        doc=DOC.read_text('utf8')
        for prop in ('process:hasTrueNextStep','process:hasFalseNextStep','process:evaluatesCondition','process:hasParticipantStep'):
            self.assertRegex(doc,r'  - iri: '+re.escape(prop)+r'\n    status: approved')
        for term in ('iri: process:ProcessTransition','iri: process:hasTransition',
                     'iri: process:fromStep','iri: process:toStep','iri: process:hasGuard'):
            self.assertNotIn(term,doc)

    def test_start_marker_is_declared_and_yaml_driven(self):
        main=EX.RecognizePlateNumberProcess
        self.assertIn((main,PR.hasInitialStep,EX.ReceivePlateImageStep),self.g)
        frag,_=ProcessRenderer(self.ir,GUIDE,CORE_GUIDE,'extended').render()
        start_id=stable('start-marker:'+str(main)+':'+str(EX.ReceivePlateImageStep))
        self.assertEqual(frag.count(start_id+'(["START"])'),1)
        self.assertIn(start_id+' --> ',frag)
        self.assertNotIn((main,DDTA.hasStep,URIRef('https://example.org/ddta/plate-gate#START')),self.g)

    def test_uses_configuration_is_a_direct_resource_reference(self):
        g=Graph().parse(str(PROCESS),format='turtle')
        config=EX.OCRConfigurationExample
        g.add((EX.ExtractPlateNumberStep,PR.usesConfiguration,config))
        g.add((config,RDF.type,DDTA.Resource))
        g.add((config,Namespace('http://www.w3.org/2000/01/rdf-schema#').label,Literal('Example config (test only)')))
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'example.ttl'
            p.write_text(g.serialize(format='turtle'),encoding='utf8')
            ir=project(CORE,p,GUIDE)
            frag,_=ProcessRenderer(ir,GUIDE,CORE_GUIDE,'extended').render()
            refs=[r for r in ir['references'] if r['predicate']=='usesConfiguration']
            self.assertEqual(len(refs),1)
            self.assertEqual(refs[0]['to'],str(config))
            self.assertIn('usesConfiguration',frag)
            self.assertIn('data:image/svg+xml;base64,',frag)
            self.assertIn('Example config (test only)',frag)

    def test_subprocess_is_structural_and_noninvoking(self):
        g=Graph().parse(str(ROOT/'tests/fixtures/process/examples/03_R8_COMPOSITION_TEST.ttl'),format='turtle')
        parent=EX.ParentProcessTest;child=EX.ChildProcessTest
        self.assertIn((parent,PR.hasSubProcess,child),g)
        self.assertNotIn((parent,PR.invokesProcess,child),g)
        self.assertNotIn((child,PR.hasSubProcess,parent),g)
        self.assertEqual(list(g.transitive_objects(child,PR.hasSubProcess)),[child])
        g.add((child,PR.hasSubProcess,parent))
        self.assertIn(parent,list(g.transitive_objects(child,PR.hasSubProcess)))
        self.assertIn(child,list(g.transitive_objects(parent,PR.hasSubProcess)))

    def test_shapes_deterministic_and_all_queries_parse(self):
        a=compile_shapes(DOC)
        b=compile_shapes(DOC)
        self.assertEqual(set(a),set(b))
        ids=set()
        for rule in a.subjects(RDF.type,SH.SPARQLConstraint):
            ids.add(str(rule).split('#')[-1])
            parseQuery(str(a.value(rule,SH.select)).replace('$this','?this'))
        for rid in ('PRC-COMP-01','PRC-COMP-02','PRC-CTRL-01','PRC-CTRL-03','PRC-CTRL-04',
                    'PRC-SYNC-01','PRC-SYNC-02','PRC-SYNC-03','PRC-SYNC-05','PRC-SYNC-06','PRC-ATOM-02'):
            self.assertIn(rid,ids)
        self.assertEqual(len(list(a.subjects(RDF.type,SH.NodeShape))),4)

    def violations(self,shape_rule,graph=None):
        g=graph or self.g
        sh=next(s for s in self.shapes.subjects(RDF.type,SH.SPARQLConstraint)
                if str(s).endswith('#'+shape_rule))
        owner=next(self.shapes.subjects(SH.sparql,sh))
        targets=sorted(set(g.subjects(RDF.type,self.shapes.value(owner,SH.targetClass))),key=str)
        if not targets:return []
        q=str(self.shapes.value(sh,SH.select)).replace('$this','?this')
        q=q.replace('WHERE {','WHERE { VALUES ?this {'+ ' '.join('<'+str(x)+'>' for x in targets)+'} ',1)
        return list(g.query(q))

    def test_shacl_sparql_baseline_no_violations(self):
        for sh in self.shapes.subjects(RDF.type,SH.SPARQLConstraint):
            rid=str(sh).split('#')[-1]
            with self.subTest(rid=rid):
                self.assertEqual(self.violations(rid),[])

    def test_shacl_sp_rejects_incorrect_branches_and_sync(self):
        g=Graph()
        for t in self.g:g.add(t)
        g.remove((EX.ModelAgreementXor,PR.hasFalseNextStep,EX.ReportDiscordanceStep))
        self.assertTrue(self.violations('PRC-CTRL-03',g))
        g.add((EX.ModelAgreementXor,PR.hasFalseNextStep,EX.ReportDiscordanceStep))
        g.remove((EX.ConcurrentOCRSplit,PR.requiredCount,None))
        g.add((EX.ConcurrentOCRSplit,PR.requiredCount,Literal(3)))
        self.assertTrue(self.violations('PRC-SYNC-06',g))
        g.remove((EX.ConcurrentOCRSplit,PR.requiredCount,None))
        g.add((EX.ConcurrentOCRSplit,PR.requiredCount,Literal(2)))
        self.assertEqual(self.violations('PRC-SYNC-06',g),[])

if __name__=='__main__':unittest.main()
