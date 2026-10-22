"""Test cases justified by FR-MR02-03-02 and its TestSpecification."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from ddta_tool.ba_rules import BARuleError, check_ba_text, load_rules
from _ba_rule_fixtures import BARuleFixture, ProduceFixture, ROOT, GUIDES, EXAMPLE, BAD_EXAMPLE

class BAPropositionTest(BARuleFixture, unittest.TestCase):

    def test_missing_polarity_is_error_even_with_draft_operator(self):
        """DDTA-TC: TC-FR-MR02-03-02-01
        DDTA-NC: FR-MR02-03-02/NC-1 MD5=548eb8ef3b147a68c0791a94563b045b
        """
        self.draft_transfer()
        outcome = self.check(BAD_EXAMPLE.read_text(encoding='utf-8'))
        self.assertIn('BA-POLARITY-MISSING', {d.code for d in outcome.diagnostics})
        self.assertGreater(outcome.errors,0)
        self.assertFalse(outcome.valid)

    def test_missing_polarity_is_error_with_active_rule(self):
        """DDTA-TC: TC-FR-MR02-03-02-01
        DDTA-NC: FR-MR02-03-02/NC-1 MD5=548eb8ef3b147a68c0791a94563b045b
        """
        self.active_transfer()
        result = self.check(self.source().replace('  polarity    = affirmative\n',''))
        self.assertIn('BA-POLARITY-MISSING', {d.code for d in result.diagnostics})
        self.assertFalse(result.valid)

    def test_negative_polarity_is_valid_when_explicit(self):
        """DDTA-TC: TC-FR-MR02-03-02-08
        DDTA-NC: FR-MR02-03-02/NC-1 MD5=548eb8ef3b147a68c0791a94563b045b
        """
        self.active_transfer()
        result = self.check(self.source().replace('polarity    = affirmative','polarity    = negative'))
        self.assertTrue(result.valid, result.as_dict())

    def test_invalid_polarity_is_error(self):
        """DDTA-TC: TC-FR-MR02-03-02-09
        DDTA-NC: FR-MR02-03-02/NC-1 MD5=548eb8ef3b147a68c0791a94563b045b
        """
        self.active_transfer()
        result = self.check(self.source().replace('affirmative','unknown'))
        self.assertIn('BA-POLARITY-INVALID',{d.code for d in result.diagnostics})

    def test_duplicate_polarity_is_error(self):
        """DDTA-TC: TC-FR-MR02-03-02-10
        DDTA-NC: FR-MR02-03-02/NC-1 MD5=548eb8ef3b147a68c0791a94563b045b
        """
        self.active_transfer()
        result = self.check(self.source().replace('  polarity    = affirmative','  polarity    = affirmative\n  polarity    = negative'))
        self.assertIn('BA-POLARITY-DUPLICATE',{d.code for d in result.diagnostics})

    def test_two_sources_violate_cardinality(self):
        """DDTA-TC: TC-FR-MR02-03-02-02
        DDTA-NC: FR-MR02-03-02/NC-2 MD5=8a8437e527896e2f851c0b6091c96c7d
        """
        self.active_transfer()
        result = self.check(self.source().replace('  source      -> SystemA  # BAR-EX-C4-A',
                    '  source      -> SystemA  # BAR-EX-C4-A\n  source      -> SystemC  # BAR-EX-C4-C'))
        self.assertIn('BA-ROLE-CARDINALITY',{d.code for d in result.diagnostics})

    def test_unknown_role_is_rejected(self):
        """DDTA-TC: TC-FR-MR02-03-02-11
        DDTA-NC: FR-MR02-03-02/NC-2 MD5=8a8437e527896e2f851c0b6091c96c7d
        """
        self.active_transfer()
        result = self.check(self.source().replace('  polarity    = affirmative','  protocol -> HTTP\n  polarity    = affirmative'))
        self.assertIn('BA-ROLE-UNKNOWN',{d.code for d in result.diagnostics})

    def test_duplicate_proposition_id_is_local_error(self):
        """DDTA-TC: TC-FR-MR02-03-02-03
        DDTA-NC: FR-MR02-03-02/NC-1 MD5=548eb8ef3b147a68c0791a94563b045b
        """
        self.active_transfer()
        src=self.source()
        start=src.index('BAP-EX-MR-BA-C4-VALID-01 - transfer')
        block=src[start:src.index('```',start)]
        src=src.replace(block,block+'\n'+block)
        result=self.check(src)
        self.assertIn('BA-ID-DUPLICATE',{d.code for d in result.diagnostics})

    def test_optional_temporal_scope_absent_has_no_extra_diagnostic(self):
        """DDTA-TC: TC-FR-MR02-03-02-05
        DDTA-NC: FR-MR02-03-02/NC-1 MD5=548eb8ef3b147a68c0791a94563b045b
        """
        self.active_transfer()
        out = self.check(self.source())
        self.assertTrue(out.valid, out.as_dict())
        self.assertNotIn('BA-TEMPORAL-SCOPE-UNVERIFIED', {d.code for d in out.diagnostics})

    def test_temporal_scope_missing_value_is_error(self):
        """DDTA-TC: TC-FR-MR02-03-02-12
        DDTA-NC: FR-MR02-03-02/NC-1 MD5=548eb8ef3b147a68c0791a94563b045b
        """
        self.active_transfer()
        src = self.source().replace('  polarity    = affirmative',
                                    '  temporalScope =\n  polarity    = affirmative')
        out = self.check(src)
        self.assertIn('BA-TEMPORAL-SCOPE-EMPTY', {d.code for d in out.diagnostics})
        self.assertGreater(out.errors, 0)

    def test_temporal_scope_duplicate_is_error(self):
        """DDTA-TC: TC-FR-MR02-03-02-13
        DDTA-NC: FR-MR02-03-02/NC-1 MD5=548eb8ef3b147a68c0791a94563b045b
        """
        self.active_transfer()
        src = self.source().replace('  polarity    = affirmative',
                                    '  temporalScope = BeforeEvent\n  temporalScope = AfterEvent\n  polarity    = affirmative')
        out = self.check(src)
        self.assertIn('BA-TEMPORAL-SCOPE-DUPLICATE', {d.code for d in out.diagnostics})
        self.assertFalse(out.valid)

    def test_cli_real_guides_valid_transfer_passes(self):
        """DDTA-TC: TC-FR-MR02-03-02-04
        DDTA-NC: FR-MR02-03-02/NC-1 MD5=548eb8ef3b147a68c0791a94563b045b
        """
        # DDTA-FR: FR-MR02-03-02 — real configured rule, not a temporary toggle.
        command = [sys.executable, '-m', 'ddta_tool', 'check-ba', str(EXAMPLE), '--json']
        proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        import json
        result = json.loads(proc.stdout)
        self.assertTrue(result['valid'])
        self.assertTrue(result['complete'])
        self.assertEqual(result['errors'], 0)
        self.assertIn('operator:transfer', result['ruleset'])

    def test_cli_real_guides_missing_polarity_is_error(self):
        """DDTA-TC: TC-FR-MR02-03-02-14
        DDTA-NC: FR-MR02-03-02/NC-1 MD5=548eb8ef3b147a68c0791a94563b045b
        """
        command = [sys.executable, '-m', 'ddta_tool', 'check-ba', str(BAD_EXAMPLE), '--json']
        proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(proc.returncode, 1, proc.stderr + proc.stdout)
        import json
        result = json.loads(proc.stdout)
        self.assertIn('BA-POLARITY-MISSING', {d['code'] for d in result['diagnostics']})
        self.assertNotIn('BA-OP-UNCOVERED', {d['code'] for d in result['diagnostics']})



class ProduceRoleContractTest(ProduceFixture, unittest.TestCase):
    def test_produce_valid_actor_and_result(self):
        """DDTA-TC: TC-FR-MR02-03-02-06
        DDTA-NC: FR-MR02-03-02/NC-2 MD5=8a8437e527896e2f851c0b6091c96c7d
        """
        outcome=self.check_produce()
        self.assertTrue(outcome.valid, outcome.as_dict())
        self.assertTrue(outcome.complete)
        self.assertEqual(outcome.errors, 0)
        self.assertIn('operator:produce', outcome.ruleset)

    def test_produce_multiple_results_and_optional_input(self):
        """DDTA-TC: TC-FR-MR02-03-02-15
        DDTA-NC: FR-MR02-03-02/NC-2 MD5=8a8437e527896e2f851c0b6091c96c7d
        """
        src=self.produce_source().replace('  polarity = affirmative',
            '  result   -> ReportSummary # BAR-EX-C5-SUMMARY\n  polarity = affirmative')
        result=self.check_produce(src)
        self.assertTrue(result.valid, result.as_dict())
        self.assertTrue(result.complete)

    def test_produce_requires_result(self):
        """DDTA-TC: TC-FR-MR02-03-02-07
        DDTA-NC: FR-MR02-03-02/NC-2 MD5=8a8437e527896e2f851c0b6091c96c7d
        """
        src='\n'.join(line for line in self.produce_source().splitlines()
                      if not line.strip().startswith('result   ->'))
        result=self.check_produce(src)
        self.assertIn('BA-ROLE-MISSING', {d.code for d in result.diagnostics})
        self.assertTrue(any('result' in d.message for d in result.diagnostics))

    def test_produce_rejects_two_actors(self):
        """DDTA-TC: TC-FR-MR02-03-02-16
        DDTA-NC: FR-MR02-03-02/NC-2 MD5=8a8437e527896e2f851c0b6091c96c7d
        """
        src=self.produce_source().replace('  result   ->',
            '  actor    -> SecondProducer # BAR-EX-C5-SECOND\n  result   ->')
        out=self.check_produce(src)
        self.assertIn('BA-ROLE-CARDINALITY', {d.code for d in out.diagnostics})

if __name__ == "__main__":
    unittest.main()
