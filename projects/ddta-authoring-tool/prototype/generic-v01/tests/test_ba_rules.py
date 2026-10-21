"""C4 prototype structural BA checks. No semantic source-evidence approval.

DDTA-FR: FR-MR02-03-01
DDTA-FR: FR-MR02-03-02
DDTA-FR: FR-MR02-03-03
DDTA-FR: FR-MR02-02-03
"""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

from ddta_tool.ba_rules import BARuleError, check_ba_text, load_rules

ROOT = Path(__file__).resolve().parents[1]
GUIDES = (ROOT / '..' / '..' / 'guides' / 'ba').resolve()
EXAMPLE = (ROOT / 'examples' / 'BA-C4-TRANSFER-VALID.md')
BAD_EXAMPLE = (ROOT / 'examples' / 'BA-C4-TRANSFER-INVALID.md')


class BARulePrototypeTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.guides = Path(self.temp.name) / 'ba'
        shutil.copytree(GUIDES, self.guides)

    def active_transfer(self):
        file = self.guides / 'operators' / 'transfer.md'
        src = file.read_text(encoding='utf-8')
        self.assertIn('reviewStatus: draft', src)
        file.write_text(src.replace('reviewStatus: draft','reviewStatus: reviewed'), encoding='utf-8')
        return file

    def source(self):
        return EXAMPLE.read_text(encoding='utf-8')

    def check(self, text):
        return check_ba_text(text, self.guides)

    def test_current_transfer_remains_disabled_without_approval(self):
        rules = load_rules(self.guides)
        self.assertIn('transfer', rules.recognized)
        self.assertIn('transfer', rules.pending)
        self.assertNotIn('transfer', rules.active)
        outcome = self.check(self.source())
        self.assertFalse(outcome.valid)
        self.assertFalse(outcome.complete)
        self.assertIn('BA-OP-UNCOVERED', {d.code for d in outcome.diagnostics})

    def test_reviewed_transfer_loads_from_guide_and_passes(self):
        self.active_transfer()
        rules = load_rules(self.guides)
        self.assertEqual(rules.active['transfer'].roles['source'],(1,1))
        outcome = self.check(self.source())
        self.assertTrue(outcome.valid, outcome.as_dict())
        self.assertEqual(outcome.errors,0)
        self.assertTrue(outcome.ruleset.get('operator:transfer'))

    def test_missing_polarity_is_error_even_with_draft_operator(self):
        outcome = self.check(BAD_EXAMPLE.read_text(encoding='utf-8'))
        self.assertIn('BA-POLARITY-MISSING', {d.code for d in outcome.diagnostics})
        self.assertGreater(outcome.errors,0)
        self.assertFalse(outcome.valid)

    def test_missing_polarity_is_error_with_active_rule(self):
        self.active_transfer()
        result = self.check(self.source().replace('  polarity    = affirmative\n',''))
        self.assertIn('BA-POLARITY-MISSING', {d.code for d in result.diagnostics})
        self.assertFalse(result.valid)

    def test_negative_polarity_is_valid_when_explicit(self):
        self.active_transfer()
        result = self.check(self.source().replace('polarity    = affirmative','polarity    = negative'))
        self.assertTrue(result.valid, result.as_dict())

    def test_invalid_polarity_is_error(self):
        self.active_transfer()
        result = self.check(self.source().replace('affirmative','unknown'))
        self.assertIn('BA-POLARITY-INVALID',{d.code for d in result.diagnostics})

    def test_duplicate_polarity_is_error(self):
        self.active_transfer()
        result = self.check(self.source().replace('  polarity    = affirmative','  polarity    = affirmative\n  polarity    = negative'))
        self.assertIn('BA-POLARITY-DUPLICATE',{d.code for d in result.diagnostics})

    def test_missing_content_reads_guide_diagnostic(self):
        self.active_transfer()
        result = self.check(self.source().replace('  content     -> DataX    # BAR-EX-C4-X\n',''))
        d = next(d for d in result.diagnostics if d.code == 'BA-ROLE-MISSING')
        self.assertIn('content', d.message)
        self.assertIn('Canonical contract',d.guideSection)
        self.assertIn('Do not invent BAReferents',d.llmInstruction)
        self.assertIn('operators/transfer.md',d.guideRef)

    def test_two_sources_violate_cardinality(self):
        self.active_transfer()
        result = self.check(self.source().replace('  source      -> SystemA  # BAR-EX-C4-A',
                    '  source      -> SystemA  # BAR-EX-C4-A\n  source      -> SystemC  # BAR-EX-C4-C'))
        self.assertIn('BA-ROLE-CARDINALITY',{d.code for d in result.diagnostics})

    def test_unknown_role_is_rejected(self):
        self.active_transfer()
        result = self.check(self.source().replace('  polarity    = affirmative','  protocol -> HTTP\n  polarity    = affirmative'))
        self.assertIn('BA-ROLE-UNKNOWN',{d.code for d in result.diagnostics})

    def test_declared_cardinality_can_change_without_python(self):
        path=self.active_transfer()
        before=self.check(self.source())
        self.assertTrue(before.valid)
        original=path.read_text(encoding='utf-8')
        path.write_text(original.replace('source: {min: 1, max: 1}','source: {min: 2, max: 2}'),encoding='utf-8')
        after=self.check(self.source())
        self.assertIn('BA-ROLE-MISSING',{d.code for d in after.diagnostics})
        self.assertNotEqual(before.ruleset.get('operator:transfer'),after.ruleset.get('operator:transfer'))

    def test_duplicate_proposition_id_is_local_error(self):
        self.active_transfer()
        src=self.source()
        start=src.index('BAP-EX-MR-BA-C4-VALID-01 - transfer')
        block=src[start:src.index('```',start)]
        src=src.replace(block,block+'\n'+block)
        result=self.check(src)
        self.assertIn('BA-ID-DUPLICATE',{d.code for d in result.diagnostics})

    def test_known_uncovered_produce_is_incomplete(self):
        src=self.source().replace(' - transfer',' - produce')
        outcome=self.check(src)
        self.assertFalse(outcome.complete)
        self.assertIn('BA-OP-UNCOVERED',{d.code for d in outcome.diagnostics})
        self.assertNotIn('BA-OP-UNKNOWN',{d.code for d in outcome.diagnostics})

    def test_unknown_operator_is_error(self):
        src=self.source().replace(' - transfer',' - invention')
        outcome=self.check(src)
        self.assertIn('BA-OP-UNKNOWN',{d.code for d in outcome.diagnostics})

    def test_unsupported_constraint_fails_closed(self):
        path=self.active_transfer()
        raw=path.read_text(encoding='utf-8')
        path.write_text(raw.replace('constraints: []','constraints: [unimplementedConstraint]'),encoding='utf-8')
        with self.assertRaises(BARuleError): load_rules(self.guides)
        result=self.check(self.source())
        self.assertIn('BA-RULESET-INVALID',{d.code for d in result.diagnostics})
        self.assertFalse(result.complete)

    def test_duplicate_rule_keys_fail_closed(self):
        path=self.active_transfer()
        duplicate=self.guides/'operators'/'another.md'
        raw=path.read_text(encoding='utf-8')
        duplicate.write_text(raw.replace('id: BA2-OP-TRANSFER','id: BA2-OP-TRANSFER-ANOTHER')
            .replace('# BA2-OP-TRANSFER —','# BA2-OP-TRANSFER-ANOTHER —'),encoding='utf-8')
        with self.assertRaises(BARuleError):load_rules(self.guides)

    def test_new_synthetic_operator_needs_only_guide_not_python(self):
        self.active_transfer()
        registry=self.guides/'operator-registry.yaml'
        registry.write_text(registry.read_text(encoding='utf-8')+'  - syntheticPart\n',encoding='utf-8')
        guide=self.guides/'operators'/'synthetic-part.md'
        raw=(self.guides/'operators'/'transfer.md').read_text(encoding='utf-8')
        raw=raw.replace('BA2-OP-TRANSFER','BA2-OP-SYNTHETICPART')
        raw=raw.replace('semanticOperatorKey: transfer','semanticOperatorKey: syntheticPart')
        raw=raw.replace('  behavior: {min: 0, max: 1}\n  source: {min: 1, max: 1}\n  destination: {min: 1, max: unbounded}\n  content: {min: 1, max: unbounded}',
            '  parent: {min: 1, max: 1}\n  part: {min: 1, max: unbounded}')
        guide.write_text(raw,encoding='utf-8')
        doc=self.source().replace(' - transfer',' - syntheticPart')
        doc=re.sub(r'  source\s+->[^\n]+\n  destination\s+->[^\n]+\n  content\s+->[^\n]+',
                   '  parent -> SystemA\n  part -> SystemB',doc)
        result=self.check(doc)
        self.assertTrue(result.valid,result.as_dict())
        self.assertIn('operator:syntheticPart',result.ruleset)

    def test_unwritten_ba_is_incomplete(self):
        src=self.source().split('## Base Analysis')[0]
        result=self.check(src)
        self.assertFalse(result.complete)
        self.assertIn('BA-NOT-AUTHORED',{d.code for d in result.diagnostics})

    def test_invalid_rule_contract_duplicates_and_unknown_key(self):
        path=self.active_transfer()
        raw=path.read_text(encoding='utf-8').replace('  source: {min: 1, max: 1}',
                 '  source: {min: 1, max: 1}\n  source: {min: 0, max: 1}')
        path.write_text(raw,encoding='utf-8')
        with self.assertRaises(BARuleError):load_rules(self.guides)

    def test_optional_temporal_scope_absent_has_no_extra_diagnostic(self):
        self.active_transfer()
        out = self.check(self.source())
        self.assertTrue(out.valid, out.as_dict())
        self.assertNotIn('BA-TEMPORAL-SCOPE-UNVERIFIED', {d.code for d in out.diagnostics})

    def test_temporal_scope_is_recognized_but_incomplete(self):
        self.active_transfer()
        src = self.source().replace('  polarity    = affirmative',
                                    '  temporalScope = DuringTraining\n  polarity    = affirmative')
        out = self.check(src)
        codes = {d.code for d in out.diagnostics}
        self.assertIn('BA-TEMPORAL-SCOPE-UNVERIFIED', codes)
        self.assertNotIn('BA-ROLE-UNKNOWN', codes)
        self.assertNotIn('BA-PARSE', codes)
        self.assertFalse(out.complete)
        self.assertFalse(out.valid)
        warning = next(d for d in out.diagnostics if d.code == 'BA-TEMPORAL-SCOPE-UNVERIFIED')
        self.assertEqual(warning.guideSection, 'temporalScope')
        self.assertIn('temporal qualification', warning.llmInstruction)

    def test_temporal_scope_missing_value_is_error(self):
        self.active_transfer()
        src = self.source().replace('  polarity    = affirmative',
                                    '  temporalScope =\n  polarity    = affirmative')
        out = self.check(src)
        self.assertIn('BA-TEMPORAL-SCOPE-EMPTY', {d.code for d in out.diagnostics})
        self.assertGreater(out.errors, 0)

    def test_temporal_scope_duplicate_is_error(self):
        self.active_transfer()
        src = self.source().replace('  polarity    = affirmative',
                                    '  temporalScope = BeforeEvent\n  temporalScope = AfterEvent\n  polarity    = affirmative')
        out = self.check(src)
        self.assertIn('BA-TEMPORAL-SCOPE-DUPLICATE', {d.code for d in out.diagnostics})
        self.assertFalse(out.valid)

    def test_temporal_scope_does_not_suppress_polarity_error(self):
        src = self.source().replace('  polarity    = affirmative',
                                    '  temporalScope = DuringTraining')
        out = self.check(src)
        self.assertIn('BA-POLARITY-MISSING', {d.code for d in out.diagnostics})
        self.assertIn('BA-TEMPORAL-SCOPE-UNVERIFIED', {d.code for d in out.diagnostics})

    def test_current_operator_source_is_r7_not_r3(self):
        from ddta_tool.ba_rules import DEFAULT_GUIDES
        root = DEFAULT_GUIDES
        self.assertNotIn('OPERATIONAL_GUIDE_R3', (root/'operator-registry.yaml').read_text(encoding='utf-8'))
        self.assertNotIn('OPERATIONAL_GUIDE_R3', (root/'operators'/'transfer.md').read_text(encoding='utf-8'))
        self.assertIn('REBUILD_R7', (root/'operator-registry.yaml').read_text(encoding='utf-8'))

    def test_cli_json_exit_one_for_missing_polarity(self):
        command=[sys.executable,'-m','ddta_tool','check-ba',str(BAD_EXAMPLE),
                 '--guides-root',str(self.guides),'--json']
        proc=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
        self.assertEqual(proc.returncode,1,proc.stderr)
        self.assertIn('BA-POLARITY-MISSING',proc.stdout)


if __name__ == '__main__':
    unittest.main()
