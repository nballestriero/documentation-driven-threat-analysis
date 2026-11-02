"""MR-04: composable abstract clinical review collection and adaptation outputs."""
import hashlib
import unittest
from pathlib import Path

from rdflib import RDF, URIRef
from tools.rdf_mermaid.render import (
    load_config, mermaid_id, read_many_rdf, render,
)

ROOT = Path(__file__).resolve().parents[1]
MR = [ROOT / f'dermatriage/mr/MR-0{i}.md' for i in (1, 2, 3, 4)]
CONFIG = ROOT / 'tools/visualization.yaml'
CORE = ROOT / 'ontology/core.ttl'
VIEWS = ROOT / 'dermatriage/views'
DDTA = 'https://w3id.org/ddta/core#'
DERMA = 'https://example.org/ddta/dermatriage#'


def d(name):
    return URIRef(DERMA + name)


def p(name):
    return URIRef(DDTA + name)


class MR04AdaptationTests(unittest.TestCase):
    def test_approved_mr04_text_and_document_dependency(self):
        source = MR[3].read_text(encoding='utf-8')
        self.assertIn('dependsOn:\n  - MR-03', source)
        self.assertIn('senza modificare l\'identità delle funzioni', source)
        self.assertIn('non ne comporta automaticamente l\'adozione', source)

    def test_mr04_collection_and_outputs(self):
        graph = read_many_rdf([MR[3]])
        self.assertIn((d('AccumulatedClinicalReviewRecords'), p('hasPart'), d('ClinicalReviewRecord')), graph)
        self.assertIn((d('ClinicalReviewRecord'), RDF.type, p('Information')), graph)
        self.assertIn((d('ControlledAdaptation'), RDF.type, p('Function')), graph)
        self.assertIn((d('ControlledAdaptation'), p('hasInput'), d('AccumulatedClinicalReviewRecords')), graph)
        self.assertIn((d('ControlledAdaptation'), p('hasOutput'), d('AdaptationCandidate')), graph)
        self.assertIn((d('ControlledAdaptation'), p('hasOutput'), d('AdaptationQualificationResult')), graph)
        self.assertIn((d('AdaptationCandidate'), RDF.type, p('Artifact')), graph)
        self.assertIn((d('AdaptationQualificationResult'), RDF.type, p('Information')), graph)
        self.assertNotIn((d('ControlledAdaptation'), p('hasOutput'), d('ClinicalReviewRecord')), graph)
        self.assertFalse(any('Adopt' in str(s) or 'Deploy' in str(s) for s in graph.subjects()))

    def test_reuses_mr03_record_identity_and_mr01_outcome(self):
        graph = read_many_rdf(MR)
        self.assertIn((d('ClinicalReviewManagement'), p('hasOutput'), d('ClinicalReviewRecord')), graph)
        self.assertIn((d('AccumulatedClinicalReviewRecords'), p('hasPart'), d('ClinicalReviewRecord')), graph)
        self.assertIn((d('ClinicalReviewRecord'), p('hasPart'), d('TriageOutcome')), graph)
        self.assertIn((d('DermatologicalTriageEvaluation'), p('hasOutput'), d('TriageOutcome')), graph)
        self.assertEqual(len(list(graph.triples((d('ClinicalReviewRecord'), RDF.type, None)))), 1)
        self.assertEqual(len(list(graph.triples((d('TriageOutcome'), RDF.type, None)))), 1)

    def test_no_new_core_terms_or_core_changes(self):
        source = read_many_rdf([MR[3]])
        core = read_many_rdf([CORE])
        subjects = set(core.subjects())
        for s, pred, obj in source:
            if str(pred).startswith(DDTA):
                self.assertIn(pred, subjects)
            if pred == RDF.type and str(obj).startswith(DDTA):
                self.assertIn(obj, subjects)
        # The Core hasOutput predicate deliberately has no rdf range restricting Artifact.
        self.assertFalse(list(core.objects(p('hasOutput'), URIRef('http://www.w3.org/2000/01/rdf-schema#range'))))

    def test_single_iri_per_node_containment_all_four_mrs(self):
        graph = render(MR, CONFIG, VIEWS / 'mr-functions-structure.rq')
        self.assertIn('AccumulatedClinicalReviewRecords · Information', graph)
        self.assertIn('ClinicalReviewRecord · Information', graph)
        self.assertIn('TriageOutcome · Information', graph)
        self.assertIn('AdaptationCandidate<br/>Artifact', graph)
        self.assertIn('AdaptationQualificationResult<br/>Information', graph)
        self.assertEqual(graph.count('ClinicalReviewRecord · Information'), 1)
        self.assertEqual(graph.count('TriageOutcome · Information'), 1)
        collection = mermaid_id(d('AccumulatedClinicalReviewRecords'), 'sg')
        record = mermaid_id(d('ClinicalReviewRecord'), 'sg')
        self.assertIn(collection + ' --> ' + mermaid_id(d('ControlledAdaptation')), graph)
        self.assertIn(mermaid_id(d('ClinicalReviewManagement')) + ' --> ' + record, graph)

    def test_isolated_and_all_mrs_deterministic(self):
        for sources in ([MR[3]], MR):
            for view in ('mr-functions-overview.rq', 'mr-functions-structure.rq'):
                forward = render(sources, CONFIG, VIEWS / view)
                backward = render(list(reversed(sources)), CONFIG, VIEWS / view)
                self.assertEqual(forward, backward)

    def test_no_mutation_on_render(self):
        inputs = MR + [CORE, CONFIG] + [VIEWS / 'mr-functions-structure.rq']
        before = [hashlib.sha256(f.read_bytes()).digest() for f in inputs]
        render(MR, CONFIG, VIEWS / 'mr-functions-structure.rq')
        self.assertEqual(before, [hashlib.sha256(f.read_bytes()).digest() for f in inputs])


if __name__ == '__main__':
    unittest.main()
