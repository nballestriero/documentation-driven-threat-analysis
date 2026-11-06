"""DDTA L1: declared primaries, minimal System arrows, complete RDF provenance."""
from pathlib import Path
import json
import re
import sys
import tempfile
import unittest

from rdflib import Graph, Namespace, RDF, RDFS, OWL

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import build_l1 as l1

DDTA = Namespace('https://w3id.org/ddta/core#')
DERMA = Namespace('https://example.org/ddta/dermatriage#')
EX = Namespace('https://example.test/primary-view#')

FIXTURE = '''
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix ex: <https://example.test/primary-view#> .
ex:Alpha a ddta:System ;
  ddta:hasPrimaryFunction ex:Order, ex:Return ;
  ddta:providesFunction ex:Order, ex:Return, ex:Fraud, ex:Isolated .
ex:Order a ddta:Function ; ddta:hasOutput ex:Result .
ex:Return a ddta:Function .
ex:Fraud a ddta:Function ; ddta:hasInput ex:Result .
ex:Isolated a ddta:Function .
ex:Result a ddta:Information .
ex:Beta a ddta:System ;
  ddta:hasPrimaryFunction ex:BetaOp ;
  ddta:providesFunction ex:BetaOp .
ex:BetaOp a ddta:Function .
'''


class TestL1PrimaryProjection(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        self.source = self.dir / 'data.ttl'
        self.out = self.dir / 'output'

    def run_case(self, text=FIXTURE, system=None):
        self.source.write_text(text, encoding='utf-8')
        stats = l1.generate([], [self.source], self.out, root=self.dir, system=system)
        graph = (self.out / 'L1_OVERVIEW.graph.md').read_text(encoding='utf-8')
        roles = json.loads((self.out / 'L1_SYSTEM_EVIDENCE.json').read_text(encoding='utf-8'))
        return stats, graph, roles

    def test_core_semantics_subproperty_not_functional(self):
        core = Graph().parse(ROOT / 'ontology' / 'core.ttl', format='turtle')
        self.assertIn((DDTA.hasPrimaryFunction, RDF.type, OWL.ObjectProperty), core)
        self.assertIn((DDTA.hasPrimaryFunction, RDFS.subPropertyOf, DDTA.providesFunction), core)
        self.assertNotIn((DDTA.hasPrimaryFunction, RDF.type, OWL.FunctionalProperty), core)
        self.assertNotIn((DDTA.contributesToFunction, RDF.type, OWL.ObjectProperty), core)

    def test_mr01_is_only_primary_declaration_for_dermatriage(self):
        folder = ROOT / 'dermatriage' / 'mr'
        md = (folder / 'MR-01.md').read_text(encoding='utf-8')
        turtle = re.findall(r'^```turtle\s*\n(.*?)^```\s*$', md, re.I | re.M | re.S)
        self.assertEqual(len(turtle), 1)
        self.assertEqual(turtle[0], (folder / 'MR-01.ttl').read_text(encoding='utf-8'))
        rdf = Graph()
        for p in sorted(folder.glob('MR-*.md')):
            rdf.parse(data=l1.FENCE_RE.findall(p.read_text(encoding='utf-8'))[0], format='turtle')
        self.assertEqual(set(rdf.objects(DERMA.DermaTriage, DDTA.hasPrimaryFunction)),
                         {DERMA.DermatologicalTriageEvaluation})
        self.assertIn((DERMA.DermaTriage, DDTA.providesFunction,
                       DERMA.DermatologicalTriageEvaluation), rdf)

    def test_dermatriage_graph_hides_only_redundant_provided_arcs(self):
        stats = l1.generate([ROOT / 'dermatriage' / 'mr'], [], self.out, root=ROOT)
        graph = (self.out / 'L1_OVERVIEW.graph.md').read_text(encoding='utf-8')
        self.assertEqual((stats['systems'], stats['functions_in_scope'],
                          stats['derived_edge_rows'], stats['architectural_role_rows']),
                         (1, 6, 3, 7))
        self.assertEqual(graph.count('hasPrimaryFunction"'), 1)
        self.assertEqual(graph.count('providesFunction"'), 0)
        for text in ('Gestione revisione clinica', 'Adattamento controllato',
                     'Indirizzamento specialistico', 'Verifica sistema',
                     'Preparazione ambiente', 'Valutazione triage'):
            self.assertIn(text, graph)
        self.assertEqual(graph.count('informationLink:'), 2)
        self.assertEqual(graph.count('informationCompositionLink:'), 1)
        self.assertIn('verifies (target: DermaTriageEnvironment)', graph)
        self.assertIn('prepares (target: DermaTriageEnvironment)', graph)
        roles = json.loads((self.out / 'L1_SYSTEM_EVIDENCE.json').read_text(encoding='utf-8'))
        self.assertEqual(len(roles), 7)  # Rendering suppresses no RDF evidence.
        self.assertEqual(len([r for r in roles if r['role'] == str(l1.L1.providedFunction)]), 4)
        self.assertTrue(any(e['p'] == str(DDTA.hasPrimaryFunction)
                            for r in roles for e in r['evidence']))

    def test_two_primaries_not_collapsed_and_shared_link_preserved(self):
        _, graph, _ = self.run_case()
        self.assertEqual(graph.count('hasPrimaryFunction"'), 3)
        self.assertEqual(graph.count('providesFunction"'), 1)  # Isolated only
        self.assertIn('informationLink: Result', graph)
        self.assertIn('Beta (System)', graph)

    def test_no_primary_declared_keeps_legacy_arcs(self):
        case = FIXTURE.replace('ddta:hasPrimaryFunction ex:Order, ex:Return ;', '')\
                      .replace('ddta:hasPrimaryFunction ex:BetaOp ;', '')
        _, graph, _ = self.run_case(case)
        self.assertNotIn('hasPrimaryFunction"', graph)
        self.assertEqual(graph.count('providesFunction"'), 5)

    def test_declared_primary_without_explicit_provides_is_supported(self):
        case = FIXTURE.replace('ddta:providesFunction ex:BetaOp .', '.').replace(' ;\n  .', ' .')
        _, graph, roles = self.run_case(case)
        self.assertIn('Beta (System)', graph)
        self.assertEqual(graph.count('hasPrimaryFunction"'), 3)
        found = [r for r in roles if r['system'] == str(EX.Beta)]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]['evidence'][0]['p'], str(DDTA.hasPrimaryFunction))

    def test_system_filter_never_imports_another_systems_primary(self):
        _, graph, records = self.run_case(system=str(EX.Beta))
        self.assertIn('Beta (System)', graph)
        self.assertNotIn('Alpha (System)', graph)
        self.assertEqual(graph.count('hasPrimaryFunction"'), 1)
        self.assertEqual({r['system'] for r in records}, {str(EX.Beta)})

    def test_determinism_of_graph_and_evidence(self):
        self.run_case()
        files = ['L1_OVERVIEW.graph.md', 'L1_SYSTEM_EVIDENCE.json', 'L1_EVIDENCE.json']
        before = [(self.out / x).read_bytes() for x in files]
        self.run_case()
        self.assertEqual(before, [(self.out / x).read_bytes() for x in files])


if __name__ == '__main__':
    unittest.main()
