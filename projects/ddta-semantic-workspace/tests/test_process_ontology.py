"""Focused vocabulary tests for experimental DDTA Process R1."""

from pathlib import Path
import unittest

from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, RDFS

PROC = "https://w3id.org/ddta/process#"
CORE = "https://w3id.org/ddta/core#"
ONTOLOGY = URIRef("https://w3id.org/ddta/process")
SOURCE = Path(__file__).resolve().parents[1] / "ontology" / "process.ttl"


class TestProcessOntologyBootstrap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = Graph().parse(SOURCE, format="turtle")

    def test_ontology_identity(self):
        self.assertIn((ONTOLOGY, RDF.type, OWL.Ontology), self.graph)

    def test_no_unreviewed_imports(self):
        self.assertEqual(list(self.graph.triples((ONTOLOGY, OWL.imports, None))), [])

    def test_approved_process_vocabulary_only(self):
        classes = set(self.graph.subjects(RDF.type, OWL.Class))
        props = set(self.graph.subjects(RDF.type, OWL.ObjectProperty))
        self.assertEqual(classes, {URIRef(PROC + x) for x in ("ProcessStep", "FlowNode", "ControlFlowTransition")})
        self.assertEqual(props, {URIRef(PROC + x) for x in ("referencesProcess", "fromNode", "toNode")})
        self.assertEqual(list(self.graph.subjects(RDF.type, OWL.DatatypeProperty)), [])

    def test_references_process_has_expected_domain_and_range(self):
        prop = URIRef(PROC + "referencesProcess")
        self.assertIn((prop, RDFS.domain, URIRef(PROC + "ProcessStep")), self.graph)
        self.assertIn((prop, RDFS.range, URIRef(CORE + "Process")), self.graph)

    def test_flow_node_taxonomy(self):
        self.assertIn((URIRef(PROC + "ProcessStep"), RDFS.subClassOf, URIRef(PROC + "FlowNode")), self.graph)
        self.assertNotIn((URIRef(PROC + "ControlFlowTransition"), RDFS.subClassOf, URIRef(PROC + "FlowNode")), self.graph)

    def test_transition_endpoint_properties(self):
        for prop in ("fromNode", "toNode"):
            self.assertIn((URIRef(PROC + prop), RDFS.domain, URIRef(PROC + "ControlFlowTransition")), self.graph)
            self.assertIn((URIRef(PROC + prop), RDFS.range, URIRef(PROC + "FlowNode")), self.graph)

    def test_no_binary_precedes_or_runtime_conditions(self):
        for forbidden in ("precedes", "Condition", "Branch", "Workflow", "ProcessExecution", "ParallelSplit"):
            self.assertFalse(list(self.graph.triples((URIRef(PROC + forbidden), None, None))))

    def test_step_is_not_declared_a_process_subclass(self):
        self.assertNotIn((URIRef(PROC + "ProcessStep"), RDFS.subClassOf, URIRef(CORE + "Process")), self.graph)


if __name__ == "__main__":
    unittest.main()
