"""Project-neutral contract tests for the proposed primary-function relation."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from rdflib import Graph, Namespace, RDF, RDFS, OWL

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("primary_pilot", HERE / "run_pilot.py")
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)
DDTA = Namespace("https://w3id.org/ddta/core#")
DERMA = Namespace("https://example.org/ddta/dermatriage#")
SHOP = Namespace("https://example.org/independent-commerce#")
DEMO = Namespace("https://example.org/independent-monitoring#")


class TestPrimaryFunctionPilot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph, cls.provenance = pilot.read_sources()
        cls.report = pilot.analyze(cls.graph, cls.provenance)

    def test_candidate_is_subproperty_of_provides_function(self):
        self.assertIn((DDTA.hasPrimaryFunction, RDFS.subPropertyOf, DDTA.providesFunction), self.graph)
        self.assertIn((DDTA.hasPrimaryFunction, RDFS.domain, DDTA.System), self.graph)
        self.assertIn((DDTA.hasPrimaryFunction, RDFS.range, DDTA.Function), self.graph)

    def test_candidate_does_not_assert_one_primary(self):
        self.assertNotIn((DDTA.hasPrimaryFunction, RDF.type, OWL.FunctionalProperty), self.graph)
        self.assertEqual(set(self.graph.objects(SHOP.CommercePlatform, DDTA.hasPrimaryFunction)),
                         {SHOP.OrderManagement, SHOP.ReturnManagement})

    def test_dermatriage_primary_is_explicitly_only_triage(self):
        primary = {row['function'] for row in self.report['evidence']
                   if row['system'] == str(DERMA.DermaTriage) and row['role'] == 'primary'}
        self.assertEqual(primary, {str(DERMA.DermatologicalTriageEvaluation)})

    def test_specialist_is_not_automatically_primary(self):
        result = {row['function']: row['role'] for row in self.report['evidence']
                  if row['system'] == str(DERMA.DermaTriage)}
        self.assertEqual(result[str(DERMA.SpecialistDestinationDetermination)], 'provided_other')
        self.assertEqual(result[str(DERMA.ControlledAdaptation)], 'provided_other')

    def test_second_system_has_two_primary_functions(self):
        primary = {row['function'] for row in self.report['evidence']
                   if row['system'] == str(SHOP.CommercePlatform) and row['role'] == 'primary'}
        self.assertEqual(primary, {str(SHOP.OrderManagement), str(SHOP.ReturnManagement)})

    def test_missing_primary_is_reported_not_guessed(self):
        self.assertEqual(self.report['systems_without_declared_primary'], [str(DEMO.MonitoringSystem)])
        self.assertFalse(any(row['role'] == 'primary' and row['system'] == str(DEMO.MonitoringSystem)
                             for row in self.report['evidence']))

    def test_external_preparation_not_promoted_to_primary_or_provided(self):
        self.assertNotIn(str(SHOP.EnvironmentSetup),
                         {row['function'] for row in self.report['evidence']})

    def test_every_role_is_backed_by_exact_assertion(self):
        for record in self.report['evidence']:
            witness = record['witness']
            self.assertTrue(witness['files'])
            pred = DDTA.hasPrimaryFunction if record['role'] == 'primary' else DDTA.providesFunction
            self.assertEqual(witness['p'], str(pred))

    def test_no_cross_system_function_leakage(self):
        rows = self.report['evidence']
        self.assertFalse(any(row['system'] == str(SHOP.CommercePlatform)
                             and row['function'].startswith(str(DERMA)) for row in rows))

    def test_query_is_project_independent(self):
        for queryfile in (HERE / 'queries').glob('*.rq'):
            text = queryfile.read_text(encoding='utf-8')
            self.assertNotIn('derma:', text)
            self.assertNotIn('shop:', text)
            self.assertNotIn('example.org', text)

    def test_deterministic_output(self):
        g2, prov2 = pilot.read_sources()
        self.assertEqual(self.report, pilot.analyze(g2, prov2))
        self.assertEqual(pilot.render(self.graph, self.report), pilot.render(g2, pilot.analyze(g2, prov2)))

    def test_mermaid_edge_labels_with_parentheses_are_quoted(self):
        rendered = pilot.render(self.graph, self.report)
        self.assertIn('-.->|"provided (role not specified)"|', rendered)
        self.assertIn('==>|"primary capability"|', rendered)
        self.assertNotIn('|provided (role not specified)|', rendered)
        self.assertNotIn('|primary capability|', rendered)

    def test_mermaid_edge_escape_handles_quotes_and_pipe(self):
        label = pilot.mermaid_edge_label('type (role) | "note"')
        self.assertEqual(label, '-.->|"type (role) &#124; &quot;note&quot;"|')

    def test_run_writes_outside_sources_only(self):
        source_data = [(p, p.read_bytes()) for p in pilot.SOURCES]
        with tempfile.TemporaryDirectory() as tempdir:
            out = Path(tempdir)
            proc = subprocess.run([sys.executable, str(HERE / 'run_pilot.py'), '--output-dir', str(out)],
                                  capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertTrue((out / 'L1_PRIMARY_REPORT.json').is_file())
            self.assertTrue((out / 'L1_PRIMARY_PILOT.graph.md').is_file())
        self.assertEqual(source_data, [(p, p.read_bytes()) for p in pilot.SOURCES])


if __name__ == '__main__':
    unittest.main()
