"""Regression tests for the generic compose/query/render path."""
from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path

from rdflib import Graph, Literal, Namespace, OWL, RDF, URIRef

from tools.graph_pipeline.compose import (PipelineError, canonical_turtle, compose,
                                          extract_graph, resolve_sources, validate)
from tools.graph_pipeline.query import execute_chain
from tools.rdf_mermaid.render import mermaid_id
from tools.visualize import ROOT, PRESETS, process, main

MRDIR = ROOT / 'dermatriage' / 'mr'
SCHEMA = ROOT / 'ontology' / 'core.ttl'
CONFIG = ROOT / 'tools' / 'visualization.yaml'
D = Namespace('https://example.org/ddta/dermatriage#')
DDTA = Namespace('https://w3id.org/ddta/core#')


class GenericGraphPipelineTest(unittest.TestCase):
    def sources(self, names):
        return resolve_sources([], ','.join(names), MRDIR)

    def run_view(self, names, view='l1'):
        return process(self.sources(names), PRESETS[view], CONFIG, SCHEMA)

    def test_read_mr_turtle_not_frontmatter(self):
        g = extract_graph(MRDIR / 'MR-01.md')
        self.assertIn((D.DermaTriage, DDTA.hasPrimaryFunction, D.DermatologicalTriageEvaluation), g)
        self.assertFalse(any('schemaVersion' in str(p) for _, p, _ in g))

    def test_same_iri_merges_and_exact_triples_dedup(self):
        a = extract_graph(MRDIR / 'MR-01.md')
        b = extract_graph(MRDIR / 'MR-02.md')
        g = compose(self.sources(['MR-01','MR-02']))
        self.assertEqual(len(g), len(set(a) | set(b)))
        self.assertIn((D.DermaTriage, DDTA.providesFunction, D.SpecialistDestinationDetermination), g)

    def test_source_order_does_not_affect_merged_serialization(self):
        a = compose(self.sources(['MR-01','MR-02']))
        b = compose(list(reversed(self.sources(['MR-01','MR-02']))))
        self.assertEqual(canonical_turtle(a), canonical_turtle(b))

    def test_two_sources_l1_uses_same_queries_yaml(self):
        merged, g, mmd = self.run_view(['MR-01','MR-02'])
        self.assertIn((D.DermaTriage, DDTA.hasPrimaryFunction, D.DermatologicalTriageEvaluation), g)
        self.assertIn('informationLink', mmd)
        self.assertNotIn('providesFunction', mmd)
        self.assertNotIn('DermaTriageVerification', mmd)
        self.assertGreater(len(merged), len(g))

    def test_all_six_l1_has_true_system_environment_endpoints(self):
        _, g, mmd = self.run_view(['MR-01','MR-02','MR-03','MR-04','MR-C6','MR-C7'])
        self.assertIn((D.DermaTriage, DDTA.hasOperationalEnvironment, D.DermaTriageEnvironment), g)
        self.assertIn((D.EnvironmentPreparation, DDTA.prepares, D.DermaTriageEnvironment), g)
        self.assertIn((D.DermaTriageVerification, DDTA.verifies, D.DermaTriage), g)
        self.assertIn((D.DermaTriageVerification, DDTA.verifies, D.DermaTriageEnvironment), g)
        self.assertIn('informationCompositionLink', mmd)
        self.assertNotIn('providesFunction', mmd)
        self.assertIn('DermaTriageEnvironment', mmd)
        e, s = mermaid_id(D.DermaTriageEnvironment), mermaid_id(D.DermaTriage)
        prep, verify = mermaid_id(D.EnvironmentPreparation), mermaid_id(D.DermaTriageVerification)
        self.assertIn(f'{prep} -.->|"prepares"| {e}', mmd)
        self.assertIn(f'{verify} -.->|"verifies"| {e}', mmd)
        self.assertIn(f'{verify} -.->|"verifies"| {s}', mmd)
        self.assertIn(f'{s} -->|"hasOperationalEnvironment"| {e}', mmd)

    def test_non_l1_query_uses_same_renderer_and_yaml(self):
        _, _, mmd = self.run_view(['MR-01','MR-02'], view='explicit')
        self.assertIn('subgraph', mmd)
        self.assertIn('CaseInformationContract', mmd)
        self.assertNotIn('hasPrimaryFunction', mmd)

    def test_deterministic_mermaid_and_rdf(self):
        names = ['MR-01','MR-02','MR-03','MR-04','MR-C6','MR-C7']
        a, b, m = self.run_view(names)
        for _ in range(3):
            aa, bb, mm = self.run_view(list(reversed(names)))
            self.assertEqual(canonical_turtle(a), canonical_turtle(aa))
            self.assertEqual(canonical_turtle(b), canonical_turtle(bb))
            self.assertEqual(m, mm)

    def test_error_invalid_turtle_creates_no_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            invalid = p/'MR-X.md'
            invalid.write_text('---\nid: MR-X\n---\n\n```turtle\n<bad> <p> .\n```\n', encoding='utf8')
            out = p/'view'
            code = main(['--source',str(invalid),'--view','l1','--out',str(out)])
            self.assertEqual(code, 2)
            self.assertFalse((p/'view.mmd').exists())
            self.assertFalse((p/'view.graph.md').exists())

    def test_conflict_explicit_disjoint_aborts_and_preserves_old_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            source = p/'conflict.md'
            source.write_text('''---\ntype: MacroRequirement\n---\n```turtle
@prefix : <https://example.org/test#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
:a a owl:Class ; owl:disjointWith :b .
:b a owl:Class .
:entity a :a, :b .
```\n''', encoding='utf8')
            out = p/'view'
            old = p/'view.mmd'
            old.write_bytes(b'PRESERVE EXACT BYTES\n')
            self.assertEqual(main(['--source',str(source),'--view','l1','--out',str(out),'--emit-merged']),2)
            self.assertEqual(old.read_bytes(), b'PRESERVE EXACT BYTES\n')
            self.assertFalse((p/'view.graph.md').exists())
            self.assertFalse((p/'view.merged.ttl').exists())

    def test_conflict_functional_property_aborts(self):
        g = Graph()
        x=Namespace('urn:example:')
        g.add((x.p,RDF.type,OWL.FunctionalProperty))
        g.add((x.s,x.p,x.o1));g.add((x.s,x.p,x.o2))
        with self.assertRaisesRegex(PipelineError,'FUNCTIONAL_PROPERTY'):
            validate(g)

    def test_compatible_multiple_classes_not_error_without_disjointness(self):
        g=Graph(); x=Namespace('urn:example:')
        g.add((x.s,RDF.type,x.A));g.add((x.s,RDF.type,x.B))
        validate(g)

    def test_different_iris_do_not_merge_by_label(self):
        g=Graph(); x=Namespace('urn:example:'); from rdflib.namespace import RDFS
        g.add((x.a,RDFS.label,Literal('Same name')))
        g.add((x.b,RDFS.label,Literal('Same name')))
        self.assertEqual(len(set(g.subjects(RDFS.label,None))), 2)

    def test_invalid_query_preserves_existing_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp); out=p/'diagram'; old=p/'diagram.mmd';old.write_text('OLD',encoding='utf8')
            bad=p/'bad.rq';bad.write_text('SELECT * WHERE { ?s ?p ?o }',encoding='utf8')
            args=['--mr','MR-01,MR-02','--mr-dir',str(MRDIR),'--query',str(bad),'--out',str(out)]
            self.assertEqual(main(args), 2)
            self.assertEqual(old.read_text(), 'OLD')
            self.assertFalse((p/'diagram.graph.md').exists())

    def test_check_mode_does_not_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'view'
            common=['--mr','MR-01,MR-02','--mr-dir',str(MRDIR),'--view','l1','--out',str(out)]
            self.assertEqual(main(common), 0)
            before=(out.with_suffix('.mmd')).read_bytes()
            self.assertEqual(main(common+['--check']),0)
            self.assertEqual(before,(out.with_suffix('.mmd')).read_bytes())
            (out.with_suffix('.mmd')).write_text('ALTERED',encoding='utf8')
            self.assertEqual(main(common+['--check']),2)
            self.assertEqual((out.with_suffix('.mmd')).read_text(),'ALTERED')

    def test_python_preserves_source_bytes(self):
        files=self.sources(['MR-01','MR-02','MR-03','MR-04','MR-C6','MR-C7'])
        before={p:hashlib.sha256(p.read_bytes()).digest() for p in files}
        self.run_view(['MR-01','MR-02','MR-03','MR-04','MR-C6','MR-C7'])
        self.assertEqual(before,{p:hashlib.sha256(p.read_bytes()).digest() for p in files})

    def test_compose_allows_multiple_turtle_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'DEC.md'
            p.write_text('''---\nid: DEC-1\n---\n\n## Intent\nA\n\n```turtle\n<urn:a> <urn:p> <urn:b> .\n```\n\n```ttl\n<urn:b> <urn:q> <urn:c> .\n```\n''',encoding='utf8')
            self.assertEqual(len(extract_graph(p)),2)

if __name__=='__main__':
    unittest.main()
