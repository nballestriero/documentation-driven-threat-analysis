"""Bootstrap checks for the candidate DDTA Process ontology.

These tests verify only the module shell. Every future vocabulary addition
must bring its own precise semantic tests and examples.
"""

from pathlib import Path
import unittest

from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF


ONTOLOGY_IRI = URIRef("https://w3id.org/ddta/process")
SOURCE = Path(__file__).resolve().parents[1] / "ontology" / "process.ttl"


class TestProcessOntologyBootstrap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = Graph().parse(SOURCE, format="turtle")

    def test_ontology_identity(self):
        self.assertIn((ONTOLOGY_IRI, RDF.type, OWL.Ontology), self.graph)

    def test_no_unreviewed_imports(self):
        self.assertEqual(list(self.graph.triples((ONTOLOGY_IRI, OWL.imports, None))), [])

    def test_bootstrap_declares_no_process_vocabulary_yet(self):
        # Replace this test with focused semantic tests as the first
        # process term is explicitly approved and implemented.
        types = (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty)
        declared = [(s, t) for t in types for s in self.graph.subjects(RDF.type, t)]
        self.assertEqual(declared, [])


if __name__ == "__main__":
    unittest.main()
