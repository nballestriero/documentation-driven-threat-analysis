"""MR-C7 L1 integration: stable system/environment targets, not a workflow.

Run from projects/ddta-semantic-workspace:
  python -m unittest discover -s tests -p test_mr_c7.py -v
"""
from __future__ import annotations

import json
import re
import tempfile
import unittest
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal

ROOT = Path(__file__).resolve().parents[1]
MR = ROOT / 'dermatriage' / 'mr'
DDTA = Namespace('https://w3id.org/ddta/core#')
DERMA = Namespace('https://example.org/ddta/dermatriage#')


def turtle_block(text: str) -> str:
    blocks = re.findall(r'^```(?:ttl|turtle)\r?\n(.*?)^```[ \t]*$', text,
                        flags=re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if len(blocks) != 1:
        raise AssertionError(f'Expected exactly one Turtle block, got {len(blocks)}')
    return blocks[0]


def all_mr_sources():
    return sorted(MR.glob('MR-*.md'))


def load_sources(paths):
    g = Graph()
    for p in paths:
        g.parse(data=turtle_block(p.read_text(encoding='utf-8')), format='turtle')
    return g


class TestMRC7L1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.md = (MR / 'MR-C7.md').read_text(encoding='utf-8')
        cls.ttl = turtle_block(cls.md)
        cls.g = Graph().parse(data=cls.ttl, format='turtle')
        cls.c6 = Graph().parse(MR / 'MR-C6.ttl', format='turtle')
        cls.core = Graph().parse(ROOT / 'ontology' / 'core.ttl', format='turtle')

    def test_metadata_and_text_remain_as_accepted(self):
        for token in ('type: MacroRequirement', 'id: MR-C7', 'lifecycle: candidate',
                      'authority: EXPERIMENTAL_NON_CANONICAL', 'dependsOn: []',
                      '## Intent', '## Context', '## Turtle',
                      'La verifica è una responsabilità autonoma'):
            self.assertIn(token, self.md)

    def test_embedded_and_standalone_turtle_match(self):
        self.assertEqual(self.ttl, (MR / 'MR-C7.ttl').read_text(encoding='utf-8'))

    def test_only_seven_expected_c7_triples(self):
        self.assertEqual(set(self.g), {
            (DERMA.DermaTriage, RDF.type, DDTA.System),
            (DERMA.DermaTriageVerification, RDF.type, DDTA.Function),
            (DERMA.DermaTriageVerification, RDFS.label, Literal('Verifica sistema', lang='it')),
            (DERMA.DermaTriageVerification, DDTA.verifies, DERMA.DermaTriage),
            (DERMA.DermaTriageVerification, DDTA.verifies, DERMA.DermaTriageEnvironment),
            (DERMA.DermaTriageVerification, DDTA.hasOutput, DERMA.VerificationResults),
            (DERMA.VerificationResults, RDF.type, DDTA.Information),
        })

    def test_all_properties_belong_to_approved_core(self):
        for _, predicate, obj in self.g:
            if predicate == RDF.type:
                self.assertIn((obj, RDF.type, OWL.Class), self.core)
            elif predicate != RDFS.label:
                self.assertIn((predicate, RDF.type, OWL.ObjectProperty), self.core)
        self.assertIn((DDTA.verifies, RDF.type, OWL.ObjectProperty), self.core)

    def test_c6_identity_and_five_parts_are_preserved(self):
        parts = {DERMA.ComputeResources, DERMA.SoftwareComponents,
                 DERMA.ModelResources, DERMA.DataResources,
                 DERMA.EnvironmentConfiguration}
        self.assertEqual(set(self.c6.objects(DERMA.DermaTriageEnvironment,
                                              DDTA.hasPart)), parts)
        self.assertIn((DERMA.EnvironmentPreparation, DDTA.prepares,
                       DERMA.DermaTriageEnvironment), self.c6)
        self.assertIn((DERMA.DermaTriage, DDTA.hasOperationalEnvironment,
                       DERMA.DermaTriageEnvironment), self.c6)

    def test_aggregation_reuses_system_identity_without_duplication(self):
        sources = all_mr_sources()
        self.assertEqual({p.name for p in sources},
                         {'MR-01.md', 'MR-02.md', 'MR-03.md', 'MR-04.md',
                          'MR-C6.md', 'MR-C7.md'})
        before = load_sources(p for p in sources if p.name != 'MR-C7.md')
        after = load_sources(sources)
        shared = set(before) & set(self.g)
        self.assertEqual(shared, {(DERMA.DermaTriage, RDF.type, DDTA.System)})
        self.assertEqual(set(after), set(before) | set(self.g))
        self.assertEqual(set(after) - set(before), set(self.g) - shared)

    def test_no_execution_order_or_input_invented(self):
        self.assertFalse(list(self.g.triples((None, DDTA.hasInput, None))))
        self.assertFalse(list(self.g.triples((None, DDTA.hasPart, None))))
        self.assertFalse(list(self.g.triples((None, DDTA.realizesFunction, None))))
        self.assertFalse(any('process#' in str(p) for _, p, _ in self.g))
        self.assertNotIn((DERMA.DermaTriage, DDTA.providesFunction,
                          DERMA.DermaTriageVerification), self.g)

    def test_generic_l1_recognizes_six_functions(self):
        from tools.build_l1 import generate
        with tempfile.TemporaryDirectory() as td:
            stats = generate([MR], [], Path(td), root=ROOT)
            self.assertEqual(stats['systems'], 1)
            self.assertEqual(stats['functions_in_scope'], 6)
            self.assertEqual(stats['functions_unscoped'], 0)
            self.assertEqual(stats['derived_edge_rows'], 3)
            self.assertEqual(stats['architectural_role_rows'], 7)
            graph = (Path(td) / 'L1_OVERVIEW.graph.md').read_text(encoding='utf-8')
            self.assertIn('Verifica sistema [MR-C7]', graph)
            self.assertIn('verifies (target: DermaTriageEnvironment)', graph)
            self.assertIn('informationCompositionLink: ClinicalReviewRecord', graph)
            self.assertNotIn('plannedWorkflowLink:', graph.split('```mermaid')[1].split('```')[0])
            evidence = json.loads((Path(td) / 'L1_SYSTEM_EVIDENCE.json').read_text(encoding='utf-8'))
            checks = [x for x in evidence if x['function'] == str(DERMA.DermaTriageVerification)]
            self.assertEqual({x['target'] for x in checks},
                             {str(DERMA.DermaTriage), str(DERMA.DermaTriageEnvironment)})
            self.assertTrue(all(x['evidence'] for x in checks))

    def test_cross_mr_information_identities_survive(self):
        combined = load_sources(all_mr_sources())
        self.assertIn((DERMA.DermatologicalTriageEvaluation, DDTA.hasOutput,
                       DERMA.TriageOutcome), combined)
        self.assertIn((DERMA.SpecialistDestinationDetermination, DDTA.hasInput,
                       DERMA.TriageOutcome), combined)
        self.assertIn((DERMA.AccumulatedClinicalReviewRecords, DDTA.hasPart,
                       DERMA.ClinicalReviewRecord), combined)


if __name__ == '__main__':
    unittest.main()
