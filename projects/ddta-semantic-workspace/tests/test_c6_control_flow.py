"""DEC-C6-01 control flow and ontology modularity, experimental only."""
import importlib.util
from pathlib import Path
import unittest

from rdflib import Graph, Namespace, RDF, URIRef
from rdflib.namespace import OWL, RDFS

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "experiments" / "c6-process-control-flow"
CORE = Namespace("https://w3id.org/ddta/core#")
PROC = Namespace("https://w3id.org/ddta/process#")
DERMA = Namespace("https://example.org/ddta/dermatriage#")

module_spec = importlib.util.spec_from_file_location("c6_flow_renderer", FOLDER / "render_workflow.py")
renderer = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(renderer)

ORDER = [
    DERMA.SetupRepositoryStep,
    DERMA.SetupDependenciesStep,
    DERMA.SetupModelsStep,
    DERMA.SetupConfigurationStep,
    DERMA.SetupInitializationStep,
    DERMA.SetupStartupStep,
]


class TestC6ProcessFlow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = renderer.load_graph(ROOT)
        cls.extended = renderer.load_graph(ROOT, with_hypothetical=True)
        cls.vocab = Graph().parse(ROOT / "ontology" / "process.ttl", format="turtle")

    def test_c6_has_six_steps_and_five_transitions(self):
        parts = set(self.graph.objects(DERMA.EnvironmentSetupProcedure, CORE.hasPart))
        steps = {p for p in parts if (p, RDF.type, PROC.ProcessStep) in self.graph}
        links = {p for p in parts if (p, RDF.type, PROC.ControlFlowTransition) in self.graph}
        self.assertEqual(steps, set(ORDER))
        self.assertEqual(len(links), 5)
        self.assertEqual(len(parts), 11)

    def test_rdf_reconstructs_exact_six_step_linear_path(self):
        path, edges = renderer.describe_linear_workflow(self.graph, DERMA.EnvironmentSetupProcedure)
        self.assertEqual(path, ORDER)
        self.assertEqual(len(edges), 5)
        for a, b in zip(ORDER, ORDER[1:]):
            self.assertIn((a, b), edges)
            self.assertEqual(set(self.graph.objects(edges[a, b], PROC.fromNode)), {a})
            self.assertEqual(set(self.graph.objects(edges[a, b], PROC.toNode)), {b})

    def test_sparql_recovers_same_five_edges(self):
        q = (FOLDER / "workflow-transitions.rq").read_text(encoding="utf-8")
        rows = list(self.graph.query(q))
        self.assertEqual(len(rows), 5)
        expected = set(zip(ORDER, ORDER[1:]))
        self.assertEqual({(r['from'], r['to']) for r in rows}, expected)
        self.assertTrue(all(r.workflow == DERMA.EnvironmentSetupProcedure for r in rows))

    def test_sparql_construct_keeps_structure(self):
        q = (FOLDER / "workflow-structure.rq").read_text(encoding="utf-8")
        view = self.graph.query(q).graph
        self.assertEqual(len(set(view.objects(DERMA.EnvironmentSetupProcedure, CORE.hasPart))), 11)
        self.assertEqual(set(view.subjects(RDF.type, PROC.ControlFlowTransition)),
                         set(self.graph.subjects(RDF.type, PROC.ControlFlowTransition)))
        self.assertEqual(set(view.subjects(RDF.type, PROC.ProcessStep)), set(ORDER))
        self.assertEqual(set(view.predicates()), {
            RDF.type, CORE.hasPart, PROC.referencesProcess, PROC.fromNode, PROC.toNode,
        })

    def test_same_underlying_process_has_independent_order_per_workflow(self):
        q = (FOLDER / "workflow-transitions.rq").read_text(encoding="utf-8")
        rows = list(self.extended.query(q))
        self.assertEqual(len(rows), 6)
        self.assertEqual(len([r for r in rows if r.workflow == DERMA.EnvironmentSetupProcedure]), 5)
        other = [r for r in rows if r.workflow == DERMA.HypotheticalModelRefreshWorkflow]
        self.assertEqual(len(other), 1)
        self.assertEqual((other[0]['from'], other[0]['to']),
                         (DERMA.RefreshModelsStep, DERMA.RefreshRepositoryStep))
        self.assertEqual(other[0].fromProcess, DERMA.ModelResourceAcquisitionStage)
        self.assertEqual(other[0].toProcess, DERMA.RepositoryAcquisitionStage)
        path, _ = renderer.describe_linear_workflow(self.extended, DERMA.HypotheticalModelRefreshWorkflow)
        self.assertEqual(path, [DERMA.RefreshModelsStep, DERMA.RefreshRepositoryStep])

    def test_no_global_ordering_on_process_definitions(self):
        process_definitions = set(self.graph.subjects(RDF.type, CORE.Process))
        for process in process_definitions:
            self.assertFalse(list(self.graph.triples((process, PROC.fromNode, None))))
            self.assertFalse(list(self.graph.triples((process, PROC.toNode, None))))
        self.assertNotIn((PROC.precedes, RDF.type, OWL.ObjectProperty), self.vocab)

    def test_rdfs_entails_step_is_flow_node_but_not_execution(self):
        self.assertIn((PROC.ProcessStep, RDFS.subClassOf, PROC.FlowNode), self.vocab)
        self.assertNotIn((PROC.ProcessStep, RDFS.subClassOf, CORE.Process), self.vocab)
        self.assertNotIn((PROC.ControlFlowTransition, RDFS.subClassOf, CORE.Transfer), self.vocab)
        self.assertEqual(list(self.vocab.triples((URIRef("https://w3id.org/ddta/process"), OWL.imports, None))), [])

    def test_missing_endpoint_is_rejected(self):
        bad = Graph()
        for t in self.graph:
            bad.add(t)
        bad.remove((DERMA.RepositoryToDependencies, PROC.toNode, DERMA.SetupDependenciesStep))
        with self.assertRaisesRegex(ValueError, "exactly one"):
            renderer.describe_linear_workflow(bad, DERMA.EnvironmentSetupProcedure)

    def test_cross_workflow_endpoint_is_rejected(self):
        bad = Graph()
        for t in self.extended:
            bad.add(t)
        bad.remove((DERMA.RepositoryToDependencies, PROC.toNode, DERMA.SetupDependenciesStep))
        bad.add((DERMA.RepositoryToDependencies, PROC.toNode, DERMA.RefreshRepositoryStep))
        with self.assertRaisesRegex(ValueError, "boundary"):
            renderer.describe_linear_workflow(bad, DERMA.EnvironmentSetupProcedure)

    def test_non_linear_or_cycle_is_rejected_only_by_linear_pilot(self):
        bad = Graph()
        for t in self.graph:
            bad.add(t)
        bad.remove((DERMA.InitializationToStartup, PROC.toNode, DERMA.SetupStartupStep))
        bad.add((DERMA.InitializationToStartup, PROC.toNode, DERMA.SetupRepositoryStep))
        with self.assertRaises(ValueError):
            renderer.describe_linear_workflow(bad, DERMA.EnvironmentSetupProcedure)
        # OWL vocabulary intentionally has NO axiom banning cycles generally.
        self.assertFalse(list(self.vocab.triples((PROC.ControlFlowTransition, OWL.disjointWith, None))))

    def test_generated_diagram_is_deterministic_and_fresh(self):
        result = renderer.generate(ROOT, FOLDER / "diagrams" / "DEC-C6-01-control-flow", check=True)
        mmd = result[0][1]
        self.assertEqual(sum(" --> " in line for line in mmd.splitlines()), 5)
        self.assertIn("realizesFunction", mmd)
        self.assertEqual(mmd.count("referencesProcess"), 6)
        self.assertNotIn("if-then", mmd.lower())


if __name__ == "__main__":
    unittest.main()
