"""MR-03 composition and on-demand cross-MR RDF views: no new Core vocabulary."""
import hashlib
import unittest
from pathlib import Path

from rdflib import URIRef, RDF
from tools.rdf_mermaid.render import (
    render, read_many_rdf, apply_sparql_view, load_config, project, mermaid_id,
)

ROOT = Path(__file__).resolve().parents[1]
MR = [ROOT / f'dermatriage/mr/MR-0{i}.md' for i in (1, 2, 3)]
CONF = ROOT / 'tools/visualization.yaml'
VIEWS = ROOT / 'dermatriage/views'
CORE = 'https://w3id.org/ddta/core#'
DERMA = 'https://example.org/ddta/dermatriage#'

class MR03CompositionTests(unittest.TestCase):
    def test_mr03_has_two_inputs_output_and_composition(self):
        g = read_many_rdf([MR[2]])
        fn, out = (URIRef(DERMA + name) for name in ('ClinicalReviewManagement','ClinicalReviewRecord'))
        a, b = (URIRef(DERMA + name) for name in ('TriageOutcome','ClinicalReview'))
        for inp in (a, b):
            self.assertIn((fn,URIRef(CORE+'hasInput'),inp),g)
            self.assertIn((out,URIRef(CORE+'hasPart'),inp),g)
        self.assertIn((fn,URIRef(CORE+'hasOutput'),out),g)

    def test_global_iri_is_shared_and_no_extra_core_terms(self):
        g = read_many_rdf(MR)
        t = URIRef(DERMA+'TriageOutcome')
        self.assertIn((URIRef(DERMA+'DermatologicalTriageEvaluation'),URIRef(CORE+'hasOutput'),t),g)
        self.assertIn((URIRef(DERMA+'SpecialistDestinationDetermination'),URIRef(CORE+'hasInput'),t),g)
        self.assertIn((URIRef(DERMA+'ClinicalReviewManagement'),URIRef(CORE+'hasInput'),t),g)
        self.assertEqual(len(list(g.triples((t,RDF.type,None)))),1)
        core = read_many_rdf([ROOT/'ontology/core.ttl'])
        vocabulary = set(core.subjects())
        for s,p,o in g:
            if str(p).startswith(CORE):
                self.assertIn(p,vocabulary)
            if p == RDF.type and isinstance(o,URIRef) and str(o).startswith(CORE):
                self.assertIn(o,vocabulary)

    def test_projection_keeps_single_nodes_and_uses_containment(self):
        for sources in ([MR[2]],MR):
            txt = render(sources,CONF,VIEWS/'mr-functions-structure.rq')
            self.assertIn('ClinicalReviewRecord · Information',txt)
            self.assertIn('subgraph',txt)
            self.assertEqual(txt.count('TriageOutcome · Information') + txt.count('TriageOutcome<br/>Information'),1)
            self.assertEqual(txt.count('ClinicalReview<br/>Information'),1)
            agg = mermaid_id(URIRef(DERMA+'ClinicalReviewRecord'),'sg')
            self.assertIn(' --> '+agg,txt)
            self.assertIn(' --> '+mermaid_id(URIRef(DERMA+'ClinicalReviewManagement')),txt)

    def test_dynamic_query_includes_all_function_roots(self):
        txt = render(MR,CONF,VIEWS/'mr-functions-overview.rq')
        for name in ('DermatologicalTriageEvaluation','SpecialistDestinationDetermination','ClinicalReviewManagement'):
            self.assertIn(name,txt)
        self.assertNotIn('ClinicalReviewRecord · Information',txt)
        self.assertIn('ClinicalReviewRecord<br/>Information',txt)

    def test_determinism_and_source_order_independent(self):
        for view in ('mr-functions-overview.rq','mr-functions-structure.rq'):
            forward = render(MR, CONF, VIEWS/view)
            backward = render(list(reversed(MR)), CONF, VIEWS/view)
            self.assertEqual(forward,backward)
            self.assertEqual(forward,render(MR,CONF,VIEWS/view))

    def test_render_does_not_change_source_files(self):
        inputs = MR + [CONF,ROOT/'ontology/core.ttl']
        before = [hashlib.sha256(p.read_bytes()).digest() for p in inputs]
        render(MR, CONF, VIEWS/'mr-functions-structure.rq')
        after = [hashlib.sha256(p.read_bytes()).digest() for p in inputs]
        self.assertEqual(before,after)

if __name__=='__main__':
    unittest.main()
