"""Review-only tests for DEC-C6-01 Core-only process composition pilot."""
from pathlib import Path
import unittest

from rdflib import Graph, Namespace, RDF, URIRef

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "experiments" / "c6-process-composition"
DDTA = Namespace("https://w3id.org/ddta/core#")
DERMA = Namespace("https://example.org/ddta/dermatriage#")
PROC = Namespace("https://w3id.org/ddta/process#")
EXPECTED = {
    DERMA.RepositoryAcquisitionStage,
    DERMA.SoftwareDependencyInstallationStage,
    DERMA.ModelResourceAcquisitionStage,
    DERMA.EnvironmentConfigurationStage,
    DERMA.LocalResourceInitializationStage,
    DERMA.ServiceStartupStage,
}


class TestC6CoreOnlyProcessComposition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g = Graph().parse(PILOT / "DEC-C6-01-process-composition.ttl", format="turtle")
        cls.core = Graph().parse(ROOT / "ontology" / "core.ttl", format="turtle")

    def test_only_existing_core_vocabulary_is_used(self):
        predicates = {predicate for _, predicate, _ in self.g}
        self.assertEqual(predicates, {RDF.type, DDTA.hasPart, DDTA.realizesFunction})
        self.assertIn((DDTA.Process, RDF.type, URIRef("http://www.w3.org/2002/07/owl#Class")), self.core)
        self.assertIn((DDTA.hasPart, RDF.type, URIRef("http://www.w3.org/2002/07/owl#ObjectProperty")), self.core)
        self.assertIn((DDTA.realizesFunction, RDF.type, URIRef("http://www.w3.org/2002/07/owl#ObjectProperty")), self.core)

    def test_workflow_realizes_preparation_function(self):
        self.assertIn((DERMA.EnvironmentSetupProcedure, RDF.type, DDTA.Process), self.g)
        self.assertIn((DERMA.EnvironmentPreparation, RDF.type, DDTA.Function), self.g)
        self.assertIn((DERMA.EnvironmentSetupProcedure, DDTA.realizesFunction,
                       DERMA.EnvironmentPreparation), self.g)

    def test_six_independently_identified_subprocesses(self):
        parts = set(self.g.objects(DERMA.EnvironmentSetupProcedure, DDTA.hasPart))
        self.assertEqual(parts, EXPECTED)
        for part in parts:
            self.assertIn((part, RDF.type, DDTA.Process), self.g)
            self.assertNotIn((part, RDF.type, DDTA.Function), self.g)
            self.assertNotEqual(part, DERMA.EnvironmentSetupProcedure)

    def test_sparql_recovers_six_parts_without_stage_order(self):
        q = (PILOT / "processes.rq").read_text(encoding="utf-8")
        results = [row.part for row in self.g.query(q)]
        self.assertEqual(set(results), EXPECTED)
        self.assertEqual(len(results), 6)
        # The SELECT result is alphabetic by IRI, not the source's stage order.
        # RDF membership does not encode source order or any scheduling rule.
        self.assertEqual(results, sorted(results, key=str))

    def test_construct_view_preserves_only_structure(self):
        q = (PILOT / "composition-view.rq").read_text(encoding="utf-8")
        g = self.g.query(q).graph
        self.assertEqual(set(g.objects(DERMA.EnvironmentSetupProcedure, DDTA.hasPart)), EXPECTED)
        self.assertIn((DERMA.EnvironmentSetupProcedure, DDTA.realizesFunction,
                       DERMA.EnvironmentPreparation), g)
        self.assertEqual({pred for _, pred, _ in g},
                         {RDF.type, DDTA.hasPart, DDTA.realizesFunction})

    def test_no_process_extension_is_sneaked_in(self):
        for s, p, o in self.g:
            for term in (s, p, o):
                self.assertFalse(str(term).startswith(str(PROC)))
        # No workflow execution, transfer, condition or ordering is claimed.
        self.assertEqual(set(self.g.predicates()),
                         {RDF.type, DDTA.hasPart, DDTA.realizesFunction})


if __name__ == "__main__":
    unittest.main()
