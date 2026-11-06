"""DDTA L1 generic projection regression tests (no project-specific fixtures)."""
from pathlib import Path
import json
import sys
import tempfile
import unittest

from rdflib import Graph, Namespace, RDF

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import build_l1 as l1  # noqa: E402

DDTA = Namespace("https://w3id.org/ddta/core#")
L1 = Namespace("urn:ddta:l1-view#")
EX = Namespace("https://example.test/generic#")

FIXTURE = '''
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix proc: <https://w3id.org/ddta/process#> .
@prefix ex: <https://example.test/generic#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
ex:SystemA a ddta:System ; rdfs:label "Sistema principale"@it ;
 ddta:hasOperationalEnvironment ex:EnvironmentA ;
 ddta:providesFunction ex:DataFunction, ex:ReportFunction .
ex:EnvironmentA a ddta:Environment .
ex:SetupFunction a ddta:Function ; ddta:prepares ex:EnvironmentA ;
 rdfs:label "Preparazione"@it .
ex:VerificationFunction a ddta:Function ; ddta:verifies ex:SystemA .
ex:AdaptationFunction a ddta:Function ; ddta:adapts ex:SystemA .
ex:DataFunction a ddta:Function ; ddta:hasOutput ex:DataAlpha, ex:DataGamma .
ex:ReportFunction a ddta:Function ; ddta:hasInput ex:DataAlpha, ex:DataGamma ;
 rdfs:label "Report operativo"@it .
ex:DataAlpha a ddta:Information ; rdfs:label "Dati di ingresso"@it .
ex:DataGamma a ddta:Information ; rdfs:label "Risultato gamma"@it .
ex:WorkflowOne a ddta:Process ;
 ddta:hasPart ex:SetupStep, ex:VerifyStep, ex:TransitionOne .
ex:SetupProcess a ddta:Process ; ddta:realizesFunction ex:SetupFunction .
ex:VerifyProcess a ddta:Process ; ddta:realizesFunction ex:VerificationFunction .
ex:SetupStep a proc:ProcessStep ; proc:referencesProcess ex:SetupProcess .
ex:VerifyStep a proc:ProcessStep ; proc:referencesProcess ex:VerifyProcess .
ex:TransitionOne a proc:ControlFlowTransition ;
 proc:fromNode ex:SetupStep ; proc:toNode ex:VerifyStep .
ex:SystemB a ddta:System ; ddta:providesFunction ex:OtherFunction .
ex:OtherFunction a ddta:Function ; ddta:hasInput ex:DataAlpha .
ex:UnscopedFunction a ddta:Function .
'''


def md(mrid, function, data, input_or_output, label):
    return f'''---
type: MacroRequirement
id: {mrid}
---
# {mrid}

## Turtle
```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix ex: <https://example.test/markdown#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
ex:Tool a ddta:System ; ddta:providesFunction ex:{function} .
ex:{function} a ddta:Function ; rdfs:label "{label}"@it ;
 ddta:{input_or_output} ex:{data} .
ex:{data} a ddta:Information .
```
'''


class TestGenericL1(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.fixture = self.base / "generic.ttl"
        self.fixture.write_text(FIXTURE, encoding="utf-8")
        self.out = self.base / "results"

    def run_fixture(self, content=None):
        if content is not None:
            self.fixture.write_text(content, encoding="utf-8")
        return l1.generate([], [self.fixture], self.out, root=self.base)

    def test_two_systems_and_valid_independent_functions(self):
        stats = self.run_fixture()
        self.assertEqual(stats["systems"], 2)
        self.assertEqual(stats["functions_in_scope"], 6)
        self.assertEqual(stats["functions_unscoped"], 1)
        graph = (self.out / "L1_OVERVIEW.graph.md").read_text(encoding="utf-8")
        self.assertIn("Sistema principale", graph)
        self.assertIn("Preparazione", graph)
        self.assertIn("Report operativo", graph)
        self.assertIn("OtherFunction", graph)
        self.assertNotIn("UnscopedFunction", graph)

    def test_labels_come_from_witness_not_hardcoded(self):
        self.run_fixture()
        graph = (self.out / "L1_OVERVIEW.graph.md").read_text(encoding="utf-8")
        self.assertIn("informationLink: Dati di ingresso, Risultato gamma", graph)
        self.assertNotIn("TriageOutcome", graph)
        self.assertIn("plannedWorkflowLink: TransitionOne", graph)

    def test_multiple_information_witnesses_preserved(self):
        stats = self.run_fixture()
        self.assertEqual(stats["derived_edge_rows"], 3)
        evidence = json.loads((self.out / "L1_EVIDENCE.json").read_text(encoding="utf-8"))
        infos = [r for r in evidence if r["relation"] == str(L1.informationLink)]
        self.assertEqual({r["witness"] for r in infos}, {str(EX.DataAlpha), str(EX.DataGamma)})

    def test_no_links_across_systems(self):
        self.run_fixture()
        evidence = json.loads((self.out / "L1_EVIDENCE.json").read_text(encoding="utf-8"))
        self.assertTrue(evidence)
        self.assertTrue(all(r["system"] == str(EX.SystemA) for r in evidence))
        self.assertTrue(all(r["to"] != str(EX.OtherFunction) for r in evidence))

    def test_no_inferred_execution_order(self):
        without_workflow = FIXTURE.replace("ex:TransitionOne a proc:ControlFlowTransition ;\n proc:fromNode ex:SetupStep ; proc:toNode ex:VerifyStep .", "")
        stats = self.run_fixture(without_workflow)
        self.assertEqual(stats["derived_edge_rows"], 2)
        graph = (self.out / "L1_OVERVIEW.graph.md").read_text(encoding="utf-8")
        self.assertNotIn("-.->|\"plannedWorkflowLink:", graph)
        self.assertIn("informationLink", graph)

    def test_input_deleted_removes_information_edge(self):
        without_input = FIXTURE.replace("ddta:hasInput ex:DataAlpha, ex:DataGamma ;", "ddta:hasInput ex:UnusedData ;")
        stats = self.run_fixture(without_input)
        self.assertEqual(stats["derived_edge_rows"], 1)
        self.assertNotIn("-->|\"informationLink:", (self.out / "L1_OVERVIEW.graph.md").read_text(encoding="utf-8"))

    def test_every_edge_has_source_rdf_provenance(self):
        self.run_fixture()
        records = json.loads((self.out / "L1_EVIDENCE.json").read_text(encoding="utf-8"))
        self.assertEqual(len(records), 3)
        for rec in records:
            self.assertTrue(rec["evidence"])
            self.assertTrue(all(triple["sources"] == ["generic.ttl"] for triple in rec["evidence"]))
            self.assertTrue(all(triple["s"] and triple["p"] and triple["o"] for triple in rec["evidence"]))
        self.assertEqual(sum(len(r["evidence"]) for r in records), 19)

    def test_deterministic_outputs(self):
        self.run_fixture()
        names = ("L1_OVERVIEW.graph.md", "L1_SCOPE.ttl", "L1_LINKS.ttl", "L1_EVIDENCE.tsv", "L1_EVIDENCE.json")
        before = {name: (self.out / name).read_bytes() for name in names}
        self.run_fixture()
        after = {name: (self.out / name).read_bytes() for name in names}
        self.assertEqual(before, after)

    def test_markdown_mr_directory_is_discovered_generically(self):
        mrdir = self.base / "project" / "mr"
        mrdir.mkdir(parents=True)
        (mrdir / "MR-01.md").write_text(md("MR-01", "Calculate", "SharedPayload", "hasOutput", "Calcolo"), encoding="utf-8")
        (mrdir / "MR-02.md").write_text(md("MR-02", "Display", "SharedPayload", "hasInput", "Visualizzazione"), encoding="utf-8")
        stats = l1.generate([mrdir], [], self.out, root=self.base)
        self.assertEqual(stats["functions_in_scope"], 2)
        self.assertEqual(stats["derived_edge_rows"], 1)
        graph = (self.out / "L1_OVERVIEW.graph.md").read_text(encoding="utf-8")
        self.assertIn("Calcolo [MR-01]", graph)
        self.assertIn("Visualizzazione [MR-02]", graph)
        self.assertIn("informationLink: SharedPayload", graph)
        evidence = json.loads((self.out / "L1_EVIDENCE.json").read_text(encoding="utf-8"))
        self.assertEqual({s for t in evidence[0]["evidence"] for s in t["sources"]},
                         {"project/mr/MR-01.md", "project/mr/MR-02.md"})

    def test_system_filter_is_explicit(self):
        stats = l1.generate([], [self.fixture], self.out, root=self.base, system=str(EX.SystemB))
        self.assertEqual(stats["systems"], 1)
        self.assertEqual(stats["functions_in_scope"], 1)
        self.assertEqual(stats["derived_edge_rows"], 0)
        self.assertEqual(stats["functions_unscoped"], 1)
        graph = (self.out / "L1_OVERVIEW.graph.md").read_text(encoding="utf-8")
        self.assertIn("OtherFunction", graph)
        self.assertNotIn("Sistema principale", graph)

    def test_invalid_turtle_reports_source(self):
        self.fixture.write_text("INVALID turtle NOT valid", encoding="utf-8")
        with self.assertRaises(Exception):
            l1.generate([], [self.fixture], self.out, root=self.base)


    def test_artifact_is_not_mislabeled_information(self):
        variant = FIXTURE.replace('ex:DataAlpha a ddta:Information ;', 'ex:DataAlpha a ddta:Artifact ;')
        stats = self.run_fixture(variant)
        self.assertEqual(stats["derived_edge_rows"], 2)
        records = json.loads((self.out / "L1_EVIDENCE.json").read_text(encoding="utf-8"))
        infos = [r for r in records if r["relation"] == str(L1.informationLink)]
        self.assertEqual([r["witness"] for r in infos], [str(EX.DataGamma)])

    def test_composition_link_from_information_collection(self):
        variant = FIXTURE + """
ex:ReviewFunction a ddta:Function ; ddta:hasOutput ex:ReviewRecord .
ex:ReviewRecord a ddta:Information ; rdfs:label "Singola revisione"@it .
ex:ReviewCollection a ddta:Information ; ddta:hasPart ex:ReviewRecord ;
 rdfs:label "Revisioni accumulate"@it .
ex:AdaptFunction a ddta:Function ; ddta:hasInput ex:ReviewCollection .
ex:SystemA ddta:providesFunction ex:ReviewFunction, ex:AdaptFunction .
"""
        stats = self.run_fixture(variant)
        self.assertEqual(stats["derived_edge_rows"], 4)
        graph = (self.out / "L1_OVERVIEW.graph.md").read_text(encoding="utf-8")
        self.assertIn("informationCompositionLink: Singola revisione in Revisioni accumulate", graph)
        rows = json.loads((self.out / "L1_EVIDENCE.json").read_text(encoding="utf-8"))
        comps = [r for r in rows if r["relation"] == str(L1.informationCompositionLink)]
        self.assertEqual(len(comps), 1)
        self.assertEqual(comps[0]["collection"], str(EX.ReviewCollection))
        self.assertEqual(len(comps[0]["evidence"]), 5)
        self.assertTrue(all(tr["sources"] == ["generic.ttl"] for tr in comps[0]["evidence"]))

    def test_composition_removal_removes_derived_edge(self):
        extra = """
ex:OutputFunction a ddta:Function ; ddta:hasOutput ex:Element .
ex:Element a ddta:Information .
ex:Collection a ddta:Information ; ddta:hasPart ex:Element .
ex:InputFunction a ddta:Function ; ddta:hasInput ex:Collection .
ex:SystemA ddta:providesFunction ex:OutputFunction, ex:InputFunction .
"""
        self.assertEqual(self.run_fixture(FIXTURE + extra)["derived_edge_rows"], 4)
        without_part = extra.replace(" ; ddta:hasPart ex:Element", "")
        self.assertEqual(self.run_fixture(FIXTURE + without_part)["derived_edge_rows"], 3)
        without_type = extra.replace("ex:Collection a ddta:Information", "ex:Collection a ddta:Artifact")
        self.assertEqual(self.run_fixture(FIXTURE + without_type)["derived_edge_rows"], 3)

    def test_composition_requires_same_system_scope(self):
        variant = FIXTURE + """
ex:OutputFunction a ddta:Function ; ddta:hasOutput ex:Element .
ex:Element a ddta:Information .
ex:Collection a ddta:Information ; ddta:hasPart ex:Element .
ex:InputFunction a ddta:Function ; ddta:hasInput ex:Collection .
ex:SystemA ddta:providesFunction ex:OutputFunction .
ex:SystemB ddta:providesFunction ex:InputFunction .
"""
        stats = self.run_fixture(variant)
        self.assertEqual(stats["derived_edge_rows"], 3)
        records = json.loads((self.out / "L1_EVIDENCE.json").read_text(encoding="utf-8"))
        self.assertFalse(any(r["relation"] == str(L1.informationCompositionLink) for r in records))

    def test_composition_not_confused_with_direct_link(self):
        variant = FIXTURE + """
ex:OutFunction a ddta:Function ; ddta:hasOutput ex:Element .
ex:Element a ddta:Information .
ex:Collection a ddta:Information ; ddta:hasPart ex:Element .
ex:InFunction a ddta:Function ; ddta:hasInput ex:Element, ex:Collection .
ex:SystemA ddta:providesFunction ex:OutFunction, ex:InFunction .
"""
        stats = self.run_fixture(variant)
        self.assertEqual(stats["derived_edge_rows"], 5)
        records = json.loads((self.out / "L1_EVIDENCE.json").read_text(encoding="utf-8"))
        related = [r for r in records if r["from"] == str(EX.OutFunction)]
        self.assertEqual({r["relation"] for r in related},
                         {str(L1.informationLink), str(L1.informationCompositionLink)})

    def test_no_project_specific_query_text(self):
        for p in (ROOT / "views" / "l1").glob("*.rq"):
            txt = p.read_text(encoding="utf-8")
            for specific in ("DermaTriage", "TriageOutcome", "MR-01", "MR-02"):
                self.assertNotIn(specific, txt, p.name)


if __name__ == "__main__":
    unittest.main()
