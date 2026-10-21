"""C5 R1: candidate produce operator review, without enabling it.

DDTA-FR: FR-MR02-03-01  # guide and machine-rule loading
DDTA-FR: FR-MR02-03-02  # shared BAProposition checks
DDTA-FR: FR-MR02-03-03  # uncovered vs executable operator
DDTA-FR: FR-MR02-02-03  # guide-linked human and LLM diagnostics

These tests do not assert semantic approval or full FR implementation.
"""
from pathlib import Path
import shutil
import tempfile
import unittest

from ddta_tool.ba_rules import check_ba_text, load_rules
from ddta_tool.engine import validate

ROOT = Path(__file__).resolve().parents[1]
GUIDES = (ROOT / '..' / '..' / 'guides' / 'ba').resolve()
EXAMPLES = ROOT / 'examples'
PRODUCE_GUIDE = GUIDES / 'operators' / 'produce.md'


class ProduceCandidateTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.guides = Path(tmp.name) / 'ba'
        shutil.copytree(GUIDES, self.guides)

    def source(self, name='BA-C5-PRODUCE-VALID.md'):
        return (EXAMPLES / name).read_text(encoding='utf-8')

    def reviewed_in_temporary_copy(self):
        path = self.guides / 'operators' / 'produce.md'
        raw = path.read_text(encoding='utf-8')
        self.assertIn('reviewStatus: draft', raw)
        path.write_text(raw.replace('reviewStatus: draft', 'reviewStatus: reviewed'), encoding='utf-8')

    def check(self, name='BA-C5-PRODUCE-VALID.md'):
        return check_ba_text(self.source(name), self.guides)

    def test_draft_produce_document_format_is_valid(self):
        result = validate(PRODUCE_GUIDE.read_text(encoding='utf-8'), 'strict')
        self.assertTrue(result.valid)

    def test_produce_is_recognized_but_pending_and_transfer_remains_active(self):
        rules = load_rules(GUIDES)
        self.assertIn('produce', rules.recognized)
        self.assertIn('produce', rules.pending)
        self.assertNotIn('produce', rules.active)
        self.assertIn('transfer', rules.active)

    def test_r7_only_as_current_source(self):
        text = PRODUCE_GUIDE.read_text(encoding='utf-8')
        self.assertIn('DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex', text)
        self.assertNotIn('OPERATIONAL_GUIDE_R3', text)
        self.assertIn('methodStatus: candidate', text)
        self.assertIn('reviewStatus: draft', text)

    def test_unapproved_produce_is_not_false_pass(self):
        out = self.check()
        self.assertFalse(out.valid)
        self.assertFalse(out.complete)
        self.assertEqual(out.errors, 0)
        self.assertIn('BA-OP-UNCOVERED', {d.code for d in out.diagnostics})

    def test_temporary_reviewed_guide_enables_produce_without_python_changes(self):
        self.reviewed_in_temporary_copy()
        rules = load_rules(self.guides)
        self.assertEqual(rules.active['produce'].roles['actor'], (1, 1))
        self.assertEqual(rules.active['produce'].roles['input'], (0, None))
        self.assertEqual(rules.active['produce'].roles['result'], (1, None))
        out = self.check()
        self.assertTrue(out.valid, out.as_dict())
        self.assertTrue(out.complete)
        self.assertEqual(out.errors, 0)
        self.assertIn('operator:produce', out.ruleset)

    def test_missing_actor_with_temporary_approval_reads_guide_diagnostic(self):
        self.reviewed_in_temporary_copy()
        out = self.check('BA-C5-PRODUCE-MISSING-ACTOR.md')
        d = next(d for d in out.diagnostics if d.code == 'BA-ROLE-MISSING')
        self.assertIn('actor', d.message)
        self.assertEqual(d.guideSection, 'Canonical contract')
        self.assertIn('operators/produce.md', d.guideRef)
        self.assertIn('Never invent', d.llmInstruction)

    def test_missing_result_is_error_when_reviewed(self):
        self.reviewed_in_temporary_copy()
        s = self.source()
        s = '\n'.join(line for line in s.splitlines() if not line.strip().startswith('result   ->'))
        out = check_ba_text(s, self.guides)
        self.assertIn('BA-ROLE-MISSING', {d.code for d in out.diagnostics})
        self.assertTrue(any('result' in d.message for d in out.diagnostics))

    def test_two_actors_break_declared_cardinality(self):
        self.reviewed_in_temporary_copy()
        s = self.source().replace('  result   ->',
            '  actor    -> SecondProducer # BAR-EX-C5-SECOND\n  result   ->')
        out = check_ba_text(s, self.guides)
        self.assertIn('BA-ROLE-CARDINALITY', {d.code for d in out.diagnostics})

    def test_multiple_results_are_allowed_and_input_remains_optional(self):
        self.reviewed_in_temporary_copy()
        s = self.source().replace('  polarity = affirmative',
            '  result   -> ReportSummary # BAR-EX-C5-SUMMARY\n  polarity = affirmative')
        out = check_ba_text(s, self.guides)
        self.assertTrue(out.valid, out.as_dict())

    def test_shared_polarity_error_survives_draft_and_review(self):
        name = 'BA-C5-PRODUCE-MISSING-POLARITY.md'
        before = self.check(name)
        self.assertIn('BA-POLARITY-MISSING', {d.code for d in before.diagnostics})
        self.reviewed_in_temporary_copy()
        after = self.check(name)
        self.assertIn('BA-POLARITY-MISSING', {d.code for d in after.diagnostics})
        self.assertGreater(after.errors, 0)

    def test_optional_temporal_scope_remains_incomplete_even_when_reviewed(self):
        self.reviewed_in_temporary_copy()
        s = self.source().replace('  polarity = affirmative',
            '  temporalScope = DuringTraining\n  polarity = affirmative')
        out = check_ba_text(s, self.guides)
        self.assertIn('BA-TEMPORAL-SCOPE-UNVERIFIED', {d.code for d in out.diagnostics})
        self.assertFalse(out.complete)
        self.assertFalse(out.valid)

    def test_transfer_still_passes_with_candidate_produce_present(self):
        source = (EXAMPLES / 'BA-C4-TRANSFER-VALID.md').read_text(encoding='utf-8')
        out = check_ba_text(source, self.guides)
        self.assertTrue(out.valid, out.as_dict())
        self.assertIn('operator:transfer', out.ruleset)


if __name__ == '__main__':
    unittest.main()
