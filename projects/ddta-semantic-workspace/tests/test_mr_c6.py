"""MR-C6 candidate: keep the text and Turtle synchronized and Core-only.

Run from projects/ddta-semantic-workspace:
    python -m unittest discover -s tests -p test_mr_c6.py -v
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, URIRef

ROOT = Path(__file__).resolve().parents[1]
MR = ROOT / 'dermatriage' / 'mr'
CORE = ROOT / 'ontology' / 'core.ttl'
DDTA = Namespace('https://w3id.org/ddta/core#')
DERMA = Namespace('https://example.org/ddta/dermatriage#')
EXPECTED_PARTS = {
    DERMA.ComputeResources,
    DERMA.SoftwareComponents,
    DERMA.ModelResources,
    DERMA.DataResources,
    DERMA.EnvironmentConfiguration,
}


def embedded_turtle(text: str) -> str:
    blocks = re.findall(r'^```(?:turtle|ttl)\r?\n(.*?)^```[ \t]*$', text,
                        flags=re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if len(blocks) != 1:
        raise AssertionError(f'Expected exactly one Turtle block, got {len(blocks)}')
    return blocks[0]


class TestMRC6Closure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (MR / 'MR-C6.md').read_text(encoding='utf-8')
        cls.turtle = embedded_turtle(cls.text)
        cls.graph = Graph().parse(data=cls.turtle, format='turtle')
        cls.core = Graph().parse(CORE, format='turtle')

    def test_metadata_matches_candidate_conventions(self):
        for token in ('type: MacroRequirement', "id: MR-C6",
                      'lifecycle: candidate', 'authority: EXPERIMENTAL_NON_CANONICAL',
                      'dependsOn: []', '## Intent', '## Context', '## Turtle'):
            self.assertIn(token, self.text)

    def test_embedded_and_separate_turtle_are_equal(self):
        self.assertEqual(self.turtle,
                         (MR / 'MR-C6.ttl').read_text(encoding='utf-8'))

    def test_function_outputs_environment(self):
        self.assertIn((DERMA.EnvironmentPreparation, RDF.type, DDTA.Function), self.graph)
        self.assertIn((DERMA.EnvironmentPreparation, DDTA.hasOutput,
                       DERMA.DermaTriageEnvironment), self.graph)
        self.assertIn((DERMA.DermaTriageEnvironment, RDF.type, DDTA.Environment), self.graph)

    def test_exactly_five_stable_logical_parts(self):
        self.assertEqual(set(self.graph.objects(DERMA.DermaTriageEnvironment,
                                                DDTA.hasPart)), EXPECTED_PARTS)
        # The five stable constituents remain exactly the same at MR level.
        # The L1 architectural context adds permitted relations without
        # changing the environment's logical composition.
        self.assertEqual(len(self.graph), 12, 'Unexpected change to the C6 MR claims')

    def test_existing_core_vocabulary_only(self):
        allowed_props = {DDTA.hasPart, DDTA.hasOutput, DDTA.prepares,
                         DDTA.hasOperationalEnvironment, RDF.type, RDFS.label}
        for subject, predicate, obj in self.graph:
            self.assertIn(predicate, allowed_props)
            if predicate == RDFS.label:
                self.assertEqual(subject, DERMA.EnvironmentPreparation)
                self.assertEqual(obj.language, 'it')
            elif predicate == RDF.type:
                self.assertIn((obj, RDF.type, URIRef('http://www.w3.org/2002/07/owl#Class')),
                              self.core)
            elif predicate != RDF.type:
                self.assertIn((predicate, RDF.type, URIRef('http://www.w3.org/2002/07/owl#ObjectProperty')),
                              self.core)

    def test_no_premature_system_or_implementation_relations(self):
        # MR-C6 now explicitly describes which system uses the prepared
        # environment. This does not mean that the system itself performs setup.
        self.assertIn((DERMA.DermaTriage, RDF.type, DDTA.System), self.graph)
        self.assertIn((DERMA.DermaTriage, DDTA.hasOperationalEnvironment,
                       DERMA.DermaTriageEnvironment), self.graph)
        self.assertIn((DERMA.EnvironmentPreparation, DDTA.prepares,
                       DERMA.DermaTriageEnvironment), self.graph)
        self.assertNotIn((DERMA.DermaTriage, DDTA.providesFunction,
                          DERMA.EnvironmentPreparation), self.graph)
        self.assertFalse(list(self.graph.triples((None, DDTA.providesFunction, None))))
        self.assertFalse(list(self.graph.triples((None, DDTA.realizesFunction, None))))
        self.assertFalse(list(self.graph.triples((None, DDTA.constrainedBy, None))))

    def test_aggregation_preserves_existing_mr_graph(self):
        existing = Graph()
        for i in range(1,5):
            text = (MR / f'MR-0{i}.md').read_text(encoding='utf-8')
            existing.parse(data=embedded_turtle(text), format='turtle')
        combined = Graph()
        combined += existing
        combined += self.graph
        # Shared identities are expected: MR-01..04 already identify the same
        # System. RDF Graph is a SET of triples, so identical assertions merge.
        shared = set(existing) & set(self.graph)
        self.assertEqual(shared, {(DERMA.DermaTriage, RDF.type, DDTA.System)})
        self.assertEqual(set(combined), set(existing) | set(self.graph))
        self.assertEqual(len(combined), len(existing) + len(self.graph) - len(shared))
        self.assertIn((DERMA.DermatologicalTriageEvaluation, RDF.type, DDTA.Function), combined)
        self.assertIn((DERMA.ControlledAdaptation, RDF.type, DDTA.Function), combined)
        self.assertEqual(set(combined.objects(DERMA.DermaTriageEnvironment,
                                              DDTA.hasPart)), EXPECTED_PARTS)


if __name__ == '__main__':
    unittest.main()
