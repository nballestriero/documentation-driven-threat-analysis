"""Generic Graph L3: all six MR, no invented facts, no default gap display.

Run from the semantic workspace root:
    python -m unittest tests.test_l3_general -v
"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS, URIRef

from tools.graph_pipeline.compose import compose, load_schema, validate, PipelineError
from tools.graph_pipeline.query import execute_chain
from tools.rdf_mermaid.render import load_config, project
from tools.visualize import process, ROOT, PRESETS


CORE = Namespace('https://w3id.org/ddta/core#')
DERMA = Namespace('https://example.org/ddta/dermatriage#')
VIEW = Namespace('urn:ddta:view#')


class GraphL3GeneralTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = [ROOT / 'dermatriage' / 'mr' / (name + '.md')
                       for name in ('MR-01','MR-02','MR-03','MR-04','MR-C6','MR-C7')]
        cls.schema = ROOT / 'ontology' / 'core.ttl'
        cls.config = ROOT / 'tools' / 'visualization.yaml'
        cls.query = ROOT / 'views' / 'pipeline' / '03-l3-general.rq'
        cls.merged, cls.selected, cls.mermaid = process(cls.sources, PRESETS['l3'], cls.config, cls.schema)

    def test_all_six_source_graph_validated(self):
        self.assertEqual(len(self.sources), 6)
        self.assertGreaterEqual(len(self.merged), 100)
        validate(self.merged, load_schema(self.schema))

    def test_query_has_no_system_specific_iri(self):
        txt = self.query.read_text(encoding='utf8')
        self.assertNotIn('derma:', txt)
        self.assertNotIn('example.org', txt)
        self.assertNotIn('MR-01', txt)

    def test_shared_referents_are_one_identity(self):
        m = self.merged
        self.assertIn((DERMA.DermatologicalTriageEvaluation, CORE.hasOutput, DERMA.TriageOutcome), m)
        self.assertIn((DERMA.SpecialistDestinationDetermination, CORE.hasInput, DERMA.TriageOutcome), m)
        self.assertIn((DERMA.ClinicalReviewManagement, CORE.hasInput, DERMA.TriageOutcome), m)
        self.assertIn((DERMA.ClinicalReviewRecord, CORE.hasPart, DERMA.TriageOutcome), m)
        self.assertIn((DERMA.AccumulatedClinicalReviewRecords, CORE.hasPart, DERMA.ClinicalReviewRecord), m)

    def test_function_modes_and_subfunctions_are_distinct(self):
        s = self.selected
        self.assertIn((DERMA.DermatologicalTriageEvaluation, CORE.hasMode, DERMA.WithImageMode), s)
        self.assertIn((DERMA.DermatologicalTriageEvaluation, CORE.hasMode, DERMA.WithoutImageMode), s)
        for part in (DERMA.ImageClassificationModelAdaptation, DERMA.GenerativePromptAdaptation):
            self.assertIn((DERMA.ControlledAdaptation, CORE.hasPart, part), s)
            self.assertIn((part, RDF.type, CORE.Function), s)
            self.assertNotIn((DERMA.ControlledAdaptation, CORE.hasMode, part), s)
        self.assertIn((DERMA.WithoutImageMode, CORE.hasOutput, DERMA.TriageOutcome), s)
        self.assertIn((DERMA.WithImageMode, CORE.hasInput, DERMA.LesionImage), s)
        self.assertIn((DERMA.WithoutImageMode, CORE.hasInput, DERMA.GeneralCaseInformation), s)
        for predicate in (CORE.modeHasInput, CORE.guaranteesOutput, CORE.requiresPresent, CORE.requiresAbsent):
            self.assertFalse(any(self.merged.triples((None, predicate, None))))
            self.assertFalse(any(s.triples((None, predicate, None))))

    def test_c6_system_environment_and_c7_is_independent(self):
        s = self.selected
        self.assertIn((DERMA.DermaTriage, CORE.hasOperationalEnvironment, DERMA.DermaTriageEnvironment), s)
        self.assertIn((DERMA.EnvironmentPreparation, CORE.prepares, DERMA.DermaTriageEnvironment), s)
        self.assertNotIn((DERMA.EnvironmentPreparation, CORE.hasOutput, DERMA.DermaTriageEnvironment), s)
        self.assertIn((DERMA.DermaTriageVerification, CORE.verifies, DERMA.DermaTriage), s)
        self.assertIn((DERMA.DermaTriageVerification, CORE.verifies, DERMA.DermaTriageEnvironment), s)
        self.assertNotIn((DERMA.DermaTriage, CORE.providesFunction, DERMA.DermaTriageVerification), s)

    def test_cardinality_is_view_only_and_contract_aware(self):
        s = self.selected
        m = self.merged
        self.assertIn((DERMA.LesionImage, VIEW.cardinality, None), [(a,b,None) for a,b,c in s if a==DERMA.LesionImage and b == VIEW.cardinality])
        self.assertTrue(any(str(value) == '0..1' for value in s.objects(DERMA.LesionImage, VIEW.cardinality)))
        self.assertTrue(any(str(value) == '1..1' for value in s.objects(DERMA.GeneralCaseInformation, VIEW.cardinality)))
        self.assertFalse(any(m.triples((None, VIEW.cardinality, None))))
        self.assertIn((DERMA.LesionImageElement, CORE.constrainsInformation, DERMA.LesionImage), m)
        self.assertNotIn((DERMA.LesionImageElement, CORE.constrainsInformation, DERMA.LesionImage), s)
        self.assertNotIn((DERMA.CaseInformation, CORE.constrainedBy, DERMA.CaseInformationContract), s)
        for entity in (DERMA.CaseInformationContract, DERMA.GeneralCaseInformationElement, DERMA.LesionImageElement):
            self.assertFalse(any(s.triples((entity, None, None))))
            self.assertFalse(any(s.triples((None, None, entity))))
        self.assertFalse(any(s.triples((DERMA.LesionImageElement, CORE.maxOccurs, None))))
        self.assertNotIn('maxOccurs = 1', self.mermaid)
        self.assertNotIn('CaseInformationContract', self.mermaid)
        self.assertNotIn('LesionImageElement', self.mermaid)
        self.assertNotIn('constrainsInformation', self.mermaid)
        self.assertIn('cardinality = 0..1', self.mermaid)

    def test_gap_validated_but_hidden_by_default(self):
        for gap in (DERMA.NoImagePriorityOutputGap,
                    DERMA.GeneralCaseInformationContentGap,
                    DERMA.ClinicalReviewOriginGap):
            self.assertTrue(any(self.merged.triples((gap, RDF.type, None))))
            self.assertFalse(any(self.selected.triples((gap, None, None))))
            self.assertFalse(any(self.selected.triples((None, None, gap))))
            self.assertNotIn(str(gap).split('#')[-1], self.mermaid)
        self.assertNotIn('DocumentationGap', self.mermaid)

    def test_missing_gap_label_fails_even_when_hidden(self):
        g=Graph()
        g += self.merged
        g.remove((DERMA.ClinicalReviewOriginGap, RDFS.label, None))
        with self.assertRaisesRegex(PipelineError, 'DOCUMENTATION_GAP_LABEL_REQUIRED'):
            validate(g, load_schema(self.schema))

    def test_no_synthetic_link_or_non_source_relation_assertions(self):
        s=self.selected
        for source, predicate, target in s:
            if predicate in (VIEW.cardinality, VIEW.minOccurs, RDF.type, RDFS.label):
                continue
            self.assertIn((source,predicate,target), self.merged)
        self.assertFalse(any(s.triples((None, VIEW.informationLink, None))))
        self.assertFalse(any(s.triples((None, VIEW.informationCompositionLink, None))))

    def test_renderer_subgraphs_not_corrupted_by_yaml_metadata(self):
        self.assertIn('DermaTriageEnvironment · Environment', self.mermaid)
        self.assertIn('ControlledAdaptation · Function', self.mermaid)
        self.assertIn('AdaptationCandidate<br/>Artifact', self.mermaid)
        self.assertNotIn('emitWhenUsed:', self.mermaid)
        self.assertNotIn('providesFunction', self.mermaid)
        self.assertNotIn('requiresPresent', self.mermaid)
        self.assertNotIn('requiresAbsent', self.mermaid)

    def test_deterministic_source_order_and_no_regression(self):
        original = self.mermaid
        graph, selected, text = process(list(reversed(self.sources)), PRESETS['l3'], self.config, self.schema)
        self.assertEqual(original, text)
        self.assertEqual(set(self.selected), set(selected))
        for queries in (PRESETS['l1'], [ROOT/'views/pipeline/01-information-links.rq',
                                      ROOT/'views/pipeline/02-l2-primary-interface.rq']):
            g1, s1, text1 = process(self.sources, queries, self.config, self.schema)
            g2, s2, text2 = process(list(reversed(self.sources)), queries, self.config, self.schema)
            self.assertEqual(text1, text2)


if __name__ == '__main__':
    unittest.main()
