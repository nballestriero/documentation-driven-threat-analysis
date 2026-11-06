"""Project-independent regression checks for system-node L1 projection."""
from pathlib import Path
import json
import sys
import tempfile
import unittest

from rdflib import Graph, Namespace, RDF

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import build_l1 as l1

DDTA = Namespace("https://w3id.org/ddta/core#")
EX = Namespace("https://example.test/architecture#")

FIXTURE = """
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix ex: <https://example.test/architecture#> .
ex:Alpha a ddta:System ;
  ddta:hasOperationalEnvironment ex:Env ;
  ddta:providesFunction ex:Processing, ex:Reporting .
ex:Env a ddta:Environment ; ddta:hasPart ex:NestedComponent .
ex:Setup a ddta:Function ; ddta:prepares ex:Env .
ex:Check a ddta:Function ; ddta:verifies ex:Alpha .
ex:Adjust a ddta:Function ; ddta:adapts ex:NestedComponent .
ex:Processing a ddta:Function ; ddta:hasOutput ex:Result .
ex:Reporting a ddta:Function ; ddta:hasInput ex:Result .
ex:Result a ddta:Information .
ex:Beta a ddta:System ; ddta:providesFunction ex:Independent .
ex:Independent a ddta:Function .
"""

class TestL1SystemRoles(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / 'example.ttl'
        self.source.write_text(FIXTURE, encoding='utf-8')
        self.out = self.base / 'result'

    def run_projection(self, value=FIXTURE, system=None):
        self.source.write_text(value, encoding='utf-8')
        return l1.generate([], [self.source], self.out, root=self.base, system=system)

    def test_system_is_node_not_only_subgraph(self):
        stats = self.run_projection()
        graph = (self.out/'L1_OVERVIEW.graph.md').read_text(encoding='utf-8')
        self.assertEqual(stats['systems'], 2)
        self.assertIn('Alpha (System)', graph)
        self.assertIn('Beta (System)', graph)
        self.assertIn('providesFunction', graph)
        self.assertIn('prepares (target: Env)', graph)
        self.assertIn('verifies', graph)
        self.assertIn('adapts (target: NestedComponent)', graph)

    def test_architectural_evidence_includes_full_path(self):
        self.run_projection()
        items = json.loads((self.out/'L1_SYSTEM_EVIDENCE.json').read_text(encoding='utf-8'))
        self.assertEqual(len(items), 6) # 2 provided + 3 external + 1 Beta
        self.assertTrue(all(t['sources'] == ['example.ttl']
                            for item in items for t in item['evidence']))
        adapt = next(item for item in items if item['function'] == str(EX.Adjust))
        self.assertEqual(len(adapt['evidence']), 3) # adapts + env + hasPart
        self.assertEqual(adapt['target'], str(EX.NestedComponent))

    def test_no_architectural_inference_of_execution_order(self):
        self.run_projection()
        g = (self.out/'L1_OVERVIEW.graph.md').read_text(encoding='utf-8')
        self.assertNotIn('plannedWorkflowLink:', g.split('```')[1])
        self.assertEqual(json.loads((self.out/'L1_REPORT.json').read_text(encoding='utf-8'))['derived_edge_rows'], 1)

    def test_remove_prepares_removes_edge_and_scope(self):
        stats = self.run_projection(FIXTURE.replace('ex:Setup a ddta:Function ; ddta:prepares ex:Env .', 'ex:Setup a ddta:Function .'))
        self.assertEqual(stats['functions_unscoped'], 1)
        g = (self.out/'L1_OVERVIEW.graph.md').read_text(encoding='utf-8')
        self.assertNotIn('prepares (target: Env)',g)

    def test_two_systems_are_not_cross_connected(self):
        self.run_projection()
        items = json.loads((self.out/'L1_SYSTEM_EVIDENCE.json').read_text(encoding='utf-8'))
        self.assertEqual([x['system'] for x in items if x['function']==str(EX.Independent)], [str(EX.Beta)])

    def test_system_filter_preserves_roles(self):
        stats = self.run_projection(system=str(EX.Beta))
        self.assertEqual(stats['architectural_role_rows'], 1)
        graph = (self.out/'L1_OVERVIEW.graph.md').read_text(encoding='utf-8')
        self.assertIn('Beta (System)',graph)
        self.assertNotIn('Alpha (System)',graph)

    def test_deterministic_system_evidence(self):
        self.run_projection()
        before = (self.out/'L1_SYSTEM_EVIDENCE.json').read_bytes()
        self.run_projection()
        self.assertEqual(before, (self.out/'L1_SYSTEM_EVIDENCE.json').read_bytes())

if __name__ == '__main__':
    unittest.main()
