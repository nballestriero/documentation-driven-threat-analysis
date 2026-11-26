"""Regression: immutable CORE prefix and normative PROCESS R6 projection.

The older R79 fixture is retained as historical test data elsewhere. This
snapshot intentionally uses the current PROCESS visualization guide.
"""
import hashlib
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
sys.path.insert(0, str(ROOT / 'src'))

from ddta_process import project, ProcessRenderer, compose


class TestSelectedCoreGraph(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixtures = ROOT / 'tests/fixtures/process/examples'
        graph = fixtures / 'CORE_BASE_GRAFO_SCELTO.mmd'
        guide = REPO / 'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'
        core_guide = REPO / 'ontologies/core/DDTA_CORE_VISUALIZATION.md'
        ir = project(
            fixtures / '00_PLATE_GATE_CORE_BASELINE.ttl',
            fixtures / '02_RECOGNIZE_PLATE_PROCESS_R6_CANDIDATA.ttl',
            guide,
        )
        fragment, diagnostics = ProcessRenderer(ir, guide, core_guide, 'compact').render()
        cls.composed = compose(graph, fragment, ir, diagnostics)
        cls.core_source = graph.read_text(encoding='utf-8').rstrip('\n')

    def test_01_core_text_is_preserved_in_composition(self):
        marker = '    %% DDTA PROCESS: modular RDF projection'
        self.assertIn(marker, self.composed)
        prefix = self.composed.split(marker, 1)[0].rstrip('\n')
        self.assertEqual(prefix, self.core_source)

    def test_02_normative_rdf_projection_labels(self):
        self.assertEqual(self.composed.count('(["START"])'), 1)
        self.assertEqual(self.composed.count('(["hasNextStep"])'), 5)
        self.assertEqual(self.composed.count('(["hasParticipantStep"])'), 2)
        self.assertIn('ModelResultsAgree', self.composed)
        self.assertIn('AtLeastTenDiscordances', self.composed)
        self.assertIn('PlateImageContract', self.composed)
        self.assertIn('PlateNumberContract', self.composed)
        self.assertIn('invokesProcess', self.composed)
        self.assertIn('stroke:#238636', self.composed)
        self.assertIn('stroke:#C62828', self.composed)

    def test_03_current_guide_snapshot_sha256(self):
        self.assertEqual(
            hashlib.sha256(self.composed.encode('utf-8')).hexdigest(),
            '9fc46c08e602869abbc241dc8a9dfe514cf22a24e317d95d720542619afc147b',
        )


if __name__ == '__main__':
    unittest.main()
