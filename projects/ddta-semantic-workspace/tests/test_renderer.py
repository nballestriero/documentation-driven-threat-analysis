"""Regression tests: graph projection must not silently change RDF semantics."""
import copy
import re
import tempfile
import unittest
from pathlib import Path

from rdflib import Graph

from tools.rdf_mermaid.render import (
    ProjectionError,
    apply_sparql_view,
    load_config,
    mermaid_id,
    project,
    read_rdf,
    render,
)

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / "dermatriage" / "mr" / "MR-01.md"
CONFIG = BASE / "tools" / "visualization.yaml"
STRUCTURE = BASE / "dermatriage" / "views" / "mr-01-structure.rq"
OVERVIEW = BASE / "dermatriage" / "views" / "mr-01-overview.rq"


class RendererTests(unittest.TestCase):
    def setUp(self):
        self.graph = read_rdf(SOURCE)
        self.cfg = load_config(CONFIG)
        self.ns = "https://example.org/ddta/dermatriage#"

    def ref(self, fragment):
        from rdflib import URIRef
        return URIRef(self.ns + fragment)

    def test_markdown_turtle_extract(self):
        self.assertGreater(len(self.graph), 10)

    def test_sparql_restricts_view(self):
        full = apply_sparql_view(self.graph, STRUCTURE)
        compact = apply_sparql_view(self.graph, OVERVIEW)
        self.assertGreater(len(full), len(compact))
        diagram = project(compact, self.cfg)
        self.assertIn("CaseInformation", diagram)
        self.assertIn("TriageOutcome", diagram)
        self.assertNotIn("CaseInformationContract", diagram)

    def test_has_input_is_reverse_arrow_and_output_forward(self):
        diagram = render(SOURCE, CONFIG, STRUCTURE)
        i = mermaid_id(self.ref("CaseInformation"))
        f = mermaid_id(self.ref("DermatologicalTriageEvaluation"))
        output = mermaid_id(self.ref("TriageOutcome"), "sg")
        self.assertIn(f"{i} --> {f}", diagram)
        self.assertNotIn(f"{f} --> {i}", diagram)
        self.assertIn(f"{f} --> {output}", diagram)

    def test_haspart_renders_containment_without_arrows(self):
        diagram = render(SOURCE, CONFIG, STRUCTURE)
        contract = mermaid_id(self.ref("CaseInformationContract"), "sg")
        part = mermaid_id(self.ref("LesionImageElement"))
        output = mermaid_id(self.ref("TriageOutcome"), "sg")
        urgency = mermaid_id(self.ref("CaseUrgency"))
        self.assertIn(f'subgraph {contract}', diagram)
        self.assertIn(f'    {part}["', diagram)
        self.assertIn(f'subgraph {output}', diagram)
        self.assertIn(f'    {urgency}["', diagram)
        self.assertNotRegex(diagram, re.escape(contract) + r"\s+-->")
        self.assertNotIn(f"{output} --> {urgency}", diagram)
        self.assertIn("minOccurs = 0", diagram)

    def test_constrained_by_dashed_no_arrow(self):
        diagram = render(SOURCE, CONFIG, STRUCTURE)
        i = mermaid_id(self.ref("CaseInformation"))
        c = mermaid_id(self.ref("CaseInformationContract"), "sg")
        self.assertIn(f"{i} -.- {c}", diagram)
        self.assertNotIn(f"{i} -.-> {c}", diagram)

    def test_deterministic(self):
        first = render(SOURCE, CONFIG, STRUCTURE)
        for _ in range(4):
            self.assertEqual(first, render(SOURCE, CONFIG, STRUCTURE))

    def test_cannot_silently_draw_multi_parent_composition(self):
        from rdflib import URIRef
        invalid = Graph()
        invalid += self.graph
        invalid.add((self.ref("TriageOutcome"), URIRef(self.cfg["coreNamespace"] + "hasPart"),
                     self.ref("LesionImageElement")))
        with self.assertRaisesRegex(ProjectionError, "Multiple hasPart parents"):
            project(invalid, self.cfg)

    def test_cannot_draw_containment_cycles(self):
        from rdflib import URIRef
        invalid = Graph()
        invalid += self.graph
        invalid.add((self.ref("CaseUrgency"), URIRef(self.cfg["coreNamespace"] + "hasPart"),
                     self.ref("TriageOutcome")))
        with self.assertRaisesRegex(ProjectionError, "cycle"):
            project(invalid, self.cfg)

    def test_rules_can_change_graph_without_changing_rdf(self):
        result = project(self.graph, self.cfg)
        changed = copy.deepcopy(self.cfg)
        changed["relations"]["hasInput"]["direction"] = "subject-to-object"
        result2 = project(self.graph, changed)
        self.assertNotEqual(result, result2)
        self.assertEqual(len(self.graph), len(read_rdf(SOURCE)))

    def test_one_turtle_block_required(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "invalid.md"
            path.write_text("# No Turtle here\n", encoding="utf-8")
            with self.assertRaisesRegex(ProjectionError, "exactly one"):
                read_rdf(path)

    def test_generated_files_are_current(self):
        from tools.rdf_mermaid.render import main
        for name, view in [("MR-01-overview", OVERVIEW), ("MR-01-structure", STRUCTURE)]:
            out = BASE / "dermatriage" / "diagrams" / name
            self.assertEqual(main(["--source", str(SOURCE), "--config", str(CONFIG),
                                   "--view", str(view), "--out", str(out), "--check"]), 0)

    def test_core_matches_graph_namespace_and_vocabulary(self):
        from rdflib import RDF, OWL, URIRef
        ontology_path = BASE / "ontology" / "core.ttl"
        core = Graph().parse(ontology_path, format="turtle")
        ns = self.cfg["coreNamespace"]
        for cls in ("Function", "Information", "Contract", "ContractElement"):
            self.assertIn((URIRef(ns + cls), RDF.type, OWL.Class), core)
        for prop in ("hasInput", "hasOutput", "hasPart", "constrainedBy"):
            self.assertIn((URIRef(ns + prop), RDF.type, OWL.ObjectProperty), core)
        self.assertIn((URIRef(ns + "minOccurs"), RDF.type, OWL.DatatypeProperty), core)

    def test_workspace_source_is_not_modified_during_render(self):
        import hashlib
        def digest(p):
            return hashlib.sha256(p.read_bytes()).hexdigest()
        core = BASE / "ontology" / "core.ttl"
        before = (digest(SOURCE), digest(core))
        render(SOURCE, CONFIG, STRUCTURE)
        self.assertEqual(before, (digest(SOURCE), digest(core)))


if __name__ == "__main__":
    unittest.main()
