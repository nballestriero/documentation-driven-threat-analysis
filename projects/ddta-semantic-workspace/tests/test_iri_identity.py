"""Core IRI migration: definition/reference consistency and shared-identity semantics."""
import unittest
from pathlib import Path
from rdflib import Graph, RDF, OWL, URIRef
from tools.rdf_mermaid.render import read_rdf, apply_sparql_view, load_config, project

ROOT = Path(__file__).resolve().parents[1]
CORE = "https://w3id.org/ddta/core#"
ONTOLOGY = "https://w3id.org/ddta/core"
OLD = "http://www.semanticweb.org/user/ontologies/2026/10/untitled-ontology-16"

class IdentityMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.core = Graph().parse(ROOT / "ontology/core.ttl", format="turtle")
        cls.mr = read_rdf(ROOT / "dermatriage/mr/MR-01.md")
        cls.config = load_config(ROOT / "tools/visualization.yaml")

    def test_ontology_and_term_iris(self):
        self.assertIn((URIRef(ONTOLOGY), RDF.type, OWL.Ontology), self.core)
        self.assertEqual(self.config["coreNamespace"], CORE)
        self.assertIn((URIRef(CORE + "Function"), RDF.type, OWL.Class), self.core)
        self.assertIn((URIRef(CORE + "hasInput"), RDF.type, OWL.ObjectProperty), self.core)
        self.assertIn((URIRef(CORE + "minOccurs"), RDF.type, OWL.DatatypeProperty), self.core)

    def test_no_legacy_iri_in_active_rdf(self):
        for graph in (self.core, self.mr):
            for triple in graph:
                self.assertFalse(any(isinstance(term, URIRef) and str(term).startswith(OLD)
                                     for term in triple), f"Legacy IRI: {triple}")

    def test_shared_term_identity_with_other_document(self):
        # Synthetic second MR: an entity mentioned twice is one RDF term.
        second = Graph().parse(data='''@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix derma: <https://example.org/ddta/dermatriage#> .
derma:SpecialistDestinationDetermination a ddta:Function ; ddta:hasInput derma:TriageOutcome .
''', format="turtle")
        merged = self.mr + second
        shared = URIRef("https://example.org/ddta/dermatriage#TriageOutcome")
        self.assertEqual(len(set(merged.subjects(URIRef(CORE+"hasInput"), shared))),1)
        self.assertEqual(len(set(merged.subjects(URIRef(CORE+"hasOutput"), shared))),1)

    def test_all_views_resolve_new_namespace(self):
        for view in ("mr-01-overview.rq", "mr-01-structure.rq"):
            query_path = ROOT / "dermatriage/views" / view
            self.assertNotIn(OLD, query_path.read_text(encoding="utf-8"))
            projection = apply_sparql_view(self.mr, query_path)
            result = project(projection, self.config)
            self.assertIn("TriageOutcome", result)

if __name__ == "__main__":
    unittest.main()
