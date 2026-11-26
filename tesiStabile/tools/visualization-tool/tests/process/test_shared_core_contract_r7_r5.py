"""R7 R5: shared CORE contract is a specification, not an execution value."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

from rdflib import Graph, Namespace, RDF

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
from ddta_process import ProcessRenderer, project, stable
from ddta_process_pipeline import trace_projection

EX = Namespace('https://example.org/ddta/plate-gate#')
DDTA = Namespace('https://w3id.org/ddta/core#')
PR = Namespace('https://w3id.org/ddta/process#')
CORE = ROOT / 'tests/fixtures/process/examples/00_PLATE_GATE_CORE_BASELINE.ttl'
PROCESS = ROOT / 'tests/fixtures/process/examples/02_RECOGNIZE_PLATE_PROCESS_R6_CANDIDATA.ttl'
GUIDE = ROOT.parents[1] / 'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'
CORE_GUIDE = ROOT.parents[1] / 'ontologies/core/DDTA_CORE_VISUALIZATION.md'


class SharedCoreContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.core = Graph().parse(str(CORE), format='turtle')
        cls.process = Graph().parse(str(PROCESS), format='turtle')
        cls.ir = project(CORE, PROCESS, GUIDE)

    def test_reuses_existing_core_contract_without_redeclaring_it(self):
        self.assertIn((EX.PlateNumberContract, RDF.type, DDTA.Contract), self.core)
        self.assertIn((EX.PlateNumberContract, DDTA.hasContractElement, EX.PlateNumber), self.core)
        self.assertNotIn((EX.PlateNumberContract, RDF.type, DDTA.Contract), self.process)
        self.assertNotIn((EX.PlateNumberContract, DDTA.hasContractElement, EX.PlateNumber), self.process)
        self.assertFalse(list(self.process.triples((EX.PlateNumber, None, None))))
        for step in (EX.ExtractPlateNumberStep, EX.VerifyPlateNumberStep):
            self.assertEqual(set(self.process.objects(step, PR.declaresOutputContract)), {EX.PlateNumberContract})
        self.assertEqual(set(self.process.objects(EX.ModelAgreementXor, PR.declaresInputContract)), {EX.PlateNumberContract})
        for operand in (EX.ExtractedPlateOperand, EX.VerifiedPlateOperand):
            self.assertEqual(set(self.process.objects(operand, PR.referencesContractElement)), {EX.PlateNumber})
        self.assertEqual(set(self.ir['contracts']), {str(EX.PlateImageContract), str(EX.PlateNumberContract)})
        self.assertEqual(self.ir['contracts'][str(EX.PlateNumberContract)]['elements'][0]['iri'], str(EX.PlateNumber))

    def test_operand_candidates_are_recorded_without_fabricating_provenance(self):
        expected = [str(EX.ExtractPlateNumberStep), str(EX.VerifyPlateNumberStep)]
        self.assertEqual(len(self.ir['operandProvenance']), 2)
        for record in self.ir['operandProvenance']:
            self.assertEqual(record['contractElement'], str(EX.PlateNumber))
            self.assertEqual(record['candidateOutputSteps'], expected)
            self.assertIsNone(record['declaredOutputStep'])

    def test_both_views_show_same_contract_in_distinct_declared_roles(self):
        for view in ('compact', 'extended'):
            fragment, diagnostics = ProcessRenderer(self.ir, GUIDE, CORE_GUIDE, view).render()
            self.assertEqual(fragment.count('>PlateNumberContract</span>'), 4, view)
            self.assertNotIn('ExtractedPlateContract', fragment)
            self.assertNotIn('VerifiedPlateContract', fragment)
            control = str(EX.ModelAgreementXor)
            self.assertNotIn('subgraph ' + stable('control-contract:' + control + ':INPUT:' + str(EX.PlateNumberContract)), fragment)
            for branch in ('left', 'right'):
                operand = stable('operand-' + branch + ':' + control + ':' + str(EX.ModelResultsAgree))
                contract = stable('operand-input-contract:' + operand + ':' + str(EX.PlateNumberContract))
                self.assertIn('subgraph ' + operand + '[', fragment)
                self.assertIn(contract + '[', fragment)
            self.assertNotIn('(["referencesContractElement"])', fragment)
            self.assertEqual(len(diagnostics['operandProvenance']), 2)

    def test_rdf_trace_keeps_all_possible_producers_not_an_invented_single_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            ir_path = Path(tmp) / 'ir.json'
            result_path = Path(tmp) / 'trace.json'
            ir_path.write_text(json.dumps(self.ir, ensure_ascii=False), encoding='utf8')
            trace_projection(ir_path, result_path)
            trace = json.loads(result_path.read_text('utf8'))
            self.assertEqual(len(trace['operandReferences']), 2)
            for ref in trace['operandReferences']:
                self.assertIsNone(ref['producerStepIRI'])
                self.assertEqual(ref['candidateProducerStepIRIs'], [
                    str(EX.ExtractPlateNumberStep), str(EX.VerifyPlateNumberStep)])
                self.assertFalse(ref['isDataTransfer'])

    def test_multiple_producers_remain_valid_and_order_independent(self):
        g = Graph().parse(str(PROCESS), format='turtle')
        g.add((EX.ReportDiscordanceStep, PR.declaresOutputContract, EX.PlateNumberContract))
        with tempfile.TemporaryDirectory() as temp:
            a = Path(temp) / 'normal.ttl'
            b = Path(temp) / 'reordered.nt'
            g.serialize(destination=a, format='turtle')
            b.write_text('\n'.join(reversed(sorted(g.serialize(format='nt').splitlines()))) + '\n', encoding='utf8')
            expected = sorted([str(EX.ExtractPlateNumberStep), str(EX.VerifyPlateNumberStep), str(EX.ReportDiscordanceStep)])
            results = [project(CORE, path, GUIDE) for path in (a, b)]
            for ir in results:
                for p in ir['operandProvenance']:
                    self.assertIsNone(p['declaredOutputStep'])
                    self.assertEqual(p['candidateOutputSteps'], expected)
            for view in ('compact', 'extended'):
                first, _ = ProcessRenderer(results[0], GUIDE, CORE_GUIDE, view).render()
                second, _ = ProcessRenderer(results[1], GUIDE, CORE_GUIDE, view).render()
                self.assertEqual(first, second)


if __name__ == '__main__':
    unittest.main()
