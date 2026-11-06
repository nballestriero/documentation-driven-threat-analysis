"""DEC-C6-01 context/reuse pilot; deliberately leaves ordering unspecified."""

from pathlib import Path
import unittest
from rdflib import Graph, URIRef
from rdflib.namespace import RDF

BASE = Path(__file__).resolve().parents[1]
EXPERIMENT = BASE / "experiments" / "c6-process-context"
CORE = "https://w3id.org/ddta/core#"
PROC = "https://w3id.org/ddta/process#"
DERMA = "https://example.org/ddta/dermatriage#"


class TestC6ProcessContext(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = Graph()
        cls.graph.parse(EXPERIMENT / "DEC-C6-01-workflow-steps.ttl", format="turtle")
        cls.graph.parse(EXPERIMENT / "hypothetical-refresh.ttl", format="turtle")
        cls.query = (EXPERIMENT / "step-placements.rq").read_text(encoding="utf-8")

    def test_all_six_c6_steps_refer_to_existing_process_identities(self):
        workflow = URIRef(DERMA + "EnvironmentSetupProcedure")
        parts = set(self.graph.objects(workflow, URIRef(CORE + "hasPart")))
        self.assertEqual(len(parts), 6)
        self.assertTrue(all((s, RDF.type, URIRef(PROC + "ProcessStep")) in self.graph for s in parts))
        refs = {next(iter(self.graph.objects(s, URIRef(PROC + "referencesProcess")))) for s in parts}
        names = {str(x).split("#")[-1] for x in refs}
        self.assertEqual(names, {
            "RepositoryAcquisitionStage", "SoftwareDependencyInstallationStage",
            "ModelResourceAcquisitionStage", "EnvironmentConfigurationStage",
            "LocalResourceInitializationStage", "ServiceStartupStage",
        })

    def test_same_process_reused_in_distinct_workflow_steps(self):
        model = URIRef(DERMA + "ModelResourceAcquisitionStage")
        steps = set(self.graph.subjects(URIRef(PROC + "referencesProcess"), model))
        self.assertEqual(steps, {URIRef(DERMA + "SetupModelsStep"), URIRef(DERMA + "RefreshModelsStep")})
        parents = {p for s in steps for p in self.graph.subjects(URIRef(CORE + "hasPart"), s)}
        self.assertEqual(parents, {
            URIRef(DERMA + "EnvironmentSetupProcedure"),
            URIRef(DERMA + "HypotheticalModelRefreshWorkflow"),
        })

    def test_sparql_finds_all_eight_placements_without_ordering(self):
        rows = list(self.graph.query(self.query))
        self.assertEqual(len(rows), 8)
        self.assertEqual(len([r for r in rows if str(r.workflow).endswith("EnvironmentSetupProcedure")]), 6)
        self.assertEqual(len([r for r in rows if str(r.workflow).endswith("HypotheticalModelRefreshWorkflow")]), 2)
        self.assertEqual(len({str(r.process) for r in rows}), 6)

    def test_no_step_is_the_process_it_references(self):
        for step, process in self.graph.subject_objects(URIRef(PROC + "referencesProcess")):
            self.assertNotEqual(step, process)
            self.assertNotIn((step, RDF.type, URIRef(CORE + "Process")), self.graph)

    def test_no_precedence_branch_or_runtime_execution(self):
        used = {str(pred) for _, pred, _ in self.graph}
        self.assertEqual({p for p in used if p.startswith(PROC)}, {PROC + "referencesProcess"})
        self.assertEqual({p for p in used if p.startswith(CORE)}, {
            CORE + "hasPart", CORE + "realizesFunction",
        })

    def test_workflow_realizes_existing_function(self):
        self.assertIn((
            URIRef(DERMA + "EnvironmentSetupProcedure"),
            URIRef(CORE + "realizesFunction"),
            URIRef(DERMA + "EnvironmentPreparation"),
        ), self.graph)


if __name__ == "__main__":
    unittest.main()
