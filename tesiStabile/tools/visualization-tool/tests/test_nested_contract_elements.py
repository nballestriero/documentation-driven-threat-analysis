"""CORE containment tests; no TLS-specific renderer logic."""
import os, sys, tempfile, unittest
from pathlib import Path
from rdflib import Graph, Namespace, RDF, Literal
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from ddta_viz.catalog import Catalog, RuleError
from ddta_viz.extract_guides import extract_guides
from ddta_viz.compile_rules import compile_rules
from ddta_viz.project_view import project
from ddta_viz.render_mermaid import render
D=Namespace('https://w3id.org/ddta/core#'); E=Namespace('https://example.org/nested#')
class NestedContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory(); p=Path(cls.tmp.name)
        extract_guides([Path(os.environ.get('DDTA_VIZ_CORE_GUIDE',str(ROOT.parents[1]/'ontologies/core/DDTA_CORE_VISUALIZATION.md')))],p/'e.yaml')
        compile_rules([p/'e.yaml'],p/'c.yaml'); cls.catalog=Catalog([p/'c.yaml'])
    @classmethod
    def tearDownClass(cls): cls.tmp.cleanup()
    def graph(self):
        g=Graph();g.bind('ddta',D);g.bind('ex',E)
        for name,typ in [('C','Contract'),('D','Contract'),('A','ContractElement'),('B','ContractElement'),('Leaf','ContractElement')]:g.add((E[name],RDF.type,D[typ]))
        for triple in [(E.C,D.hasContractElement,E.A),(E.D,D.hasContractElement,E.A),(E.A,D.hasSubContractElement,E.B),(E.B,D.hasSubContractElement,E.Leaf),(E.B,D.minOccurs,Literal(0)),(E.B,D.maxOccurs,Literal(1))]:g.add(triple)
        return g
    def test_recursive_shared_identity_and_style(self):
        g=self.graph(); initial=set(g);ir=project(g,self.catalog,strict=True);mmd=render(ir,self.catalog)
        self.assertEqual(initial,set(g));self.assertEqual(ir['edges'],[]);self.assertEqual(len(ir['occurrences'][str(E.Leaf)]),2)
        for root in ir['roots']:
            self.assertEqual(root['children'][0]['children'][0]['children'][0]['iri'],str(E.Leaf))
        self.assertIn('0..1',mmd);self.assertIn('stroke-dasharray:5 4',mmd);self.assertEqual(mmd,render(project(g,self.catalog,strict=True),self.catalog))
    def test_disconnected_cycle(self):
        g=self.graph()
        for x in [E.X,E.Y]:g.add((x,RDF.type,D.ContractElement))
        g.add((E.X,D.hasSubContractElement,E.Y));g.add((E.Y,D.hasSubContractElement,E.X))
        with self.assertRaisesRegex(RuleError,'hasSubContractElement.*Ciclo'):project(g,self.catalog,focus=E.C)
    def test_self_cycle(self):
        g=self.graph();g.add((E.B,D.hasSubContractElement,E.B))
        with self.assertRaisesRegex(RuleError,'hasSubContractElement.*Ciclo'):project(g,self.catalog)
