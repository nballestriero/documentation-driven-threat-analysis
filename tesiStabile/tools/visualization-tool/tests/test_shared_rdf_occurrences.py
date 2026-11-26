"""Verifiche generali: identità RDF e occorrenza grafica non coincidono."""
from __future__ import annotations

import sys
import os
import tempfile
import unittest
from pathlib import Path

from rdflib import Graph, Namespace, RDF, URIRef

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))

from ddta_viz.catalog import Catalog, RuleError
from ddta_viz.compile_rules import compile_rules
from ddta_viz.extract_guides import extract_guides
from ddta_viz.project_view import project
from ddta_viz.render_mermaid import render

DDTA = Namespace('https://w3id.org/ddta/core#')
EX = Namespace('https://example.org/shared-rdf-identity#')


class SharedRdfIdentityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        out = Path(cls.temp.name)
        extracted = out / 'extracted.yaml'
        compiled = out / 'compiled.yaml'
        extract_guides([Path(os.environ.get('DDTA_VIZ_CORE_GUIDE', str(ROOT.parents[1] / 'ontologies/core/DDTA_CORE_VISUALIZATION.md')))], extracted)
        compile_rules([extracted], compiled)
        cls.catalog = Catalog([compiled])

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def graph(self, definitions, relations):
        graph = Graph()
        graph.bind('ddta', DDTA)
        graph.bind('ex', EX)
        for key, class_name in definitions:
            graph.add((EX[key], RDF.type, DDTA[class_name]))
        for src, property_name, dst in relations:
            graph.add((EX[src], DDTA[property_name], EX[dst]))
        return graph

    def check_identity(self, ir, name, copies):
        uri = str(EX[name])
        self.assertIn(uri, ir['nodes'])
        self.assertEqual(len(ir['occurrences'][uri]), copies)
        occurrence_ids = [o['id'] for o in ir['occurrences'][uri]]
        self.assertEqual(len(set(occurrence_ids)), copies)
        self.assertEqual(ir['nodes'][uri]['iri'], uri)
        self.assertEqual(ir['statistics']['rdfIndividuals'], len(ir['nodes']))
        self.assertTrue(all(d['severity'] != 'warning' for d in ir['diagnostics']))
        shared = [d for d in ir['diagnostics'] if d['code'] == 'SHARED_RDF_INDIVIDUAL']
        self.assertEqual(len(shared), 1)
        self.assertEqual(shared[0]['severity'], 'info')
        self.assertEqual(shared[0]['individuals'][uri], copies)

    def test_nested_containers_are_not_multiple_rdf_parents(self):
        g = self.graph(
            [('F', 'Function'), ('C', 'Contract'), ('E', 'ContractElement')],
            [('F', 'hasInputContract', 'C'), ('C', 'hasContractElement', 'E')],
        )
        ir = project(g, self.catalog, strict=True)
        self.assertEqual(ir['statistics']['rdfIndividuals'], 3)
        self.assertEqual(ir['statistics']['visualOccurrences'], 3)
        self.assertFalse(any(d['code'] in {'MULTIPLE_GRAPHIC_PARENTS', 'SHARED_RDF_INDIVIDUAL'}
                             for d in ir['diagnostics']))

    def test_element_reused_in_two_contracts_is_valid_in_strict(self):
        g = self.graph(
            [('A', 'Contract'), ('B', 'Contract'), ('E', 'ContractElement')],
            [('A', 'hasContractElement', 'E'), ('B', 'hasContractElement', 'E')],
        )
        ir = project(g, self.catalog, strict=True)
        self.check_identity(ir, 'E', 2)
        self.assertEqual(ir['statistics']['visualOccurrences'], 4)
        multi = [d for d in ir['diagnostics'] if d['code'] == 'MULTIPLE_GRAPHIC_PARENTS']
        self.assertEqual(len(multi), 1)
        self.assertEqual(multi[0]['severity'], 'info')
        self.assertIn('E', render(ir, self.catalog))

    def test_contract_reused_as_output_and_input(self):
        g = self.graph(
            [('Send', 'Function'), ('Receive', 'Function'), ('C', 'Contract')],
            [('Send', 'hasOutputContract', 'C'), ('Receive', 'hasInputContract', 'C')],
        )
        ir = project(g, self.catalog, strict=True)
        self.check_identity(ir, 'C', 2)
        self.assertEqual(ir['statistics']['rdfIndividuals'], 3)
        self.assertEqual(ir['statistics']['visualOccurrences'], 4)
        self.assertEqual(len([d for d in ir['diagnostics'] if d['code'] == 'MULTIPLE_GRAPHIC_PARENTS']), 1)

    def test_same_contract_input_and_output_of_same_function(self):
        g = self.graph(
            [('F', 'Function'), ('C', 'Contract')],
            [('F', 'hasInputContract', 'C'), ('F', 'hasOutputContract', 'C')],
        )
        ir = project(g, self.catalog, strict=True)
        self.check_identity(ir, 'C', 2)
        self.assertEqual(ir['statistics']['visualOccurrences'], 3)
        self.assertFalse(any(d['code'] == 'MULTIPLE_GRAPHIC_PARENTS' for d in ir['diagnostics']))
        contract_occurrences = ir['occurrences'][str(EX.C)]
        self.assertEqual({o['role'] for o in contract_occurrences}, {'INPUT', 'OUTPUT'})

    def test_focused_view_does_not_report_sharing_outside_view(self):
        g = self.graph(
            [('Send', 'Function'), ('Receive', 'Function'), ('C', 'Contract')],
            [('Send', 'hasOutputContract', 'C'), ('Receive', 'hasInputContract', 'C')],
        )
        ir = project(g, self.catalog, focus=EX.Send, strict=True)
        self.assertEqual(len(ir['occurrences'][str(EX.C)]), 1)
        self.assertFalse(any(d['code'] in {'MULTIPLE_GRAPHIC_PARENTS', 'SHARED_RDF_INDIVIDUAL'}
                             for d in ir['diagnostics']))

    def test_genuine_warning_still_blocks_strict(self):
        g = self.graph([('F', 'Function'), ('Unknown', 'UndefinedClass')], [])
        with self.assertRaisesRegex(RuleError, 'Ambiguità'):
            project(g, self.catalog, strict=True)

    def test_explicit_multiple_parents_error_is_not_disabled(self):
        # Existing rule hasSubFunction states multipleParents: error.
        g = self.graph(
            [('A', 'Function'), ('B', 'Function'), ('Child', 'Function')],
            [('A', 'hasSubFunction', 'Child'), ('B', 'hasSubFunction', 'Child')],
        )
        with self.assertRaisesRegex(RuleError, 'multipleParents:error'):
            project(g, self.catalog, strict=True)

    def test_containment_cycle_still_blocked(self):
        g = self.graph(
            [('A', 'Function'), ('B', 'Function')],
            [('A', 'hasSubFunction', 'B'), ('B', 'hasSubFunction', 'A')],
        )
        with self.assertRaisesRegex(RuleError, 'Ciclo'):
            project(g, self.catalog, focus=EX.A)


if __name__ == '__main__':
    unittest.main()
