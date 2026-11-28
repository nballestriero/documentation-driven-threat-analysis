"""ContentType: projection only, no inferred security or new RDF identity."""
import sys, tempfile, unittest
from pathlib import Path
from rdflib import Graph, Namespace, RDF
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from ddta_viz.catalog import Catalog, RuleError
from ddta_viz.extract_guides import extract_guides
from ddta_viz.compile_rules import compile_rules
from ddta_viz.project_view import project
from ddta_viz.render_mermaid import render
from ddta_viz.render_data import extend_catalog
D=Namespace('https://w3id.org/ddta/core#')
E=Namespace('https://example.org/content#')
X=Namespace('https://example.org/types#')
DATA=Namespace('https://w3id.org/ddta/data#')
class ContentTypeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory(); p=Path(cls.tmp.name)
        core=ROOT.parents[1]/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
        data=ROOT.parents[1]/'ontologies/data/DDTA_DATA_VISUALIZATION.md'
        extract_guides([core],p/'e.yaml');compile_rules([p/'e.yaml'],p/'c.yaml');cls.catalog=Catalog([p/'c.yaml'])
        cls.data_guide=data; cls.compiled=p/'c.yaml'; cls.folder=p
    @classmethod
    def tearDownClass(cls): cls.tmp.cleanup()
    def graph(self):
        g=Graph();g.bind('ddta',D);g.bind('ex',E);g.bind('tech',X);g.bind('data',DATA)
        for s,t in [(E.A,D.ContractElement),(E.B,D.StoredContent),(X.Z,D.ContentType),(X.A,D.ContentType)]:g.add((s,RDF.type,t))
        return g
    def test_multiple_shared_and_order(self):
        g=self.graph()
        for s,o in [(E.A,X.Z),(E.A,X.A),(E.B,X.A)]:g.add((s,D.hasContentType,o))
        original=set(g);ir=project(g,self.catalog,strict=True);m=render(ir,self.catalog)
        self.assertEqual(original,set(g));self.assertEqual(len(ir['nodes']),4);self.assertEqual(len(ir['roots']),2);self.assertFalse(ir['edges'])
        refs=ir['roots'][0]['inlineReferences'];self.assertEqual([x['iri'] for x in refs],[str(X.A),str(X.Z)])
        self.assertEqual(m.count('tech:A</span>'),2);self.assertIn('border-radius:4px',m)
        self.assertEqual(m,render(project(g,self.catalog,strict=True),self.catalog))
        self.assertNotIn('Guaranteed',m)
    def test_nested_and_focus(self):
        g=self.graph();g.add((E.C,RDF.type,D.ContractElement));g.add((E.A,D.hasSubContractElement,E.C));g.add((E.A,D.hasContentType,X.A));g.add((E.C,D.hasContentType,X.Z))
        ir=project(g,self.catalog,focus=E.A,strict=True);self.assertEqual(len(ir['roots']),1)
        root=ir['roots'][0];self.assertEqual(root['inlineReferences'][0]['iri'],str(X.A));self.assertEqual(root['children'][0]['inlineReferences'][0]['iri'],str(X.Z))
        m=render(ir,self.catalog);self.assertIn('subgraph',m);self.assertIn('tech:A',m);self.assertIn('tech:Z',m)
    def test_untyped_and_invalid_domain(self):
        g=self.graph();g.add((E.F,RDF.type,D.Function));g.add((E.F,D.hasContentType,X.A));g.add((E.A,D.hasContentType,X.Missing))
        ir=project(g,self.catalog);self.assertEqual(sum(d['code']=='INVALID_INLINE_REFERENCE' for d in ir['diagnostics']),2)
        with self.assertRaises(RuleError):project(g,self.catalog,strict=True)
    def test_data_block(self):
        g=self.graph();g.add((E.Block,RDF.type,DATA.DataBlock));g.add((E.Block,D.hasContentType,X.A));g.add((E.B,DATA.hasDataBlock,E.Block))
        combined=Catalog([self.compiled]);extend_catalog(combined,g,self.data_guide,self.folder/'data.yaml')
        ir=project(g,combined,strict=True);m=render(ir,combined);self.assertIn('tech:A',m);self.assertIn('data:DataBlock',m)
    def test_no_inference_from_name_and_no_annotation_without_relation(self):
        g=Graph();g.bind('ddta',D);g.bind('ex',E);g.add((E.Ciphertext,RDF.type,D.ContractElement))
        m=render(project(g,self.catalog,strict=True),self.catalog);self.assertNotIn('hasContentType',m)
    def test_full_iri_without_prefix(self):
        g=Graph();g.bind('ddta',D);g.bind('ex',E);g.add((E.A,RDF.type,D.ContractElement));g.add((X.Z,RDF.type,D.ContentType));g.add((E.A,D.hasContentType,X.Z))
        ir=project(g,self.catalog,strict=True);self.assertEqual(ir['roots'][0]['inlineReferences'][0]['display'],str(X.Z))
