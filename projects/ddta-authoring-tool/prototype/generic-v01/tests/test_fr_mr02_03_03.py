"""Test cases justified by FR-MR02-03-03 and its TestSpecification."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from ddta_tool.ba_rules import BARuleError, check_ba_text, load_rules
from _ba_rule_fixtures import BARuleFixture, ROOT, GUIDES, EXAMPLE, BAD_EXAMPLE

class BARuleCoverageTest(BARuleFixture, unittest.TestCase):

    def test_current_transfer_is_reviewed_and_active(self):
        """DDTA-TC: TC-FR-MR02-03-03-01
        DDTA-NC: FR-MR02-03-03/NC-2 MD5=dad9c7ba80f4cf4ec45f72a7dc6ba398
        DDTA-NC: FR-MR02-03-03/NC-3 MD5=007a1638fcb3ff5dcda27b3ccb868512
        """
        # DDTA-FR: FR-MR02-03-01; FR-MR02-03-03.
        rules = load_rules(GUIDES)
        self.assertIn('transfer', rules.recognized)
        self.assertIn('transfer', rules.active)
        self.assertNotIn('transfer', rules.pending)
        outcome = check_ba_text(self.source(), GUIDES)
        self.assertTrue(outcome.valid, outcome.as_dict())
        self.assertTrue(outcome.complete)
        self.assertEqual(outcome.errors, 0)

    def test_draft_guide_copy_is_not_executable(self):
        """DDTA-TC: TC-FR-MR02-03-03-01
        DDTA-NC: FR-MR02-03-03/NC-2 MD5=dad9c7ba80f4cf4ec45f72a7dc6ba398
        DDTA-NC: FR-MR02-03-03/NC-3 MD5=007a1638fcb3ff5dcda27b3ccb868512
        """
        self.draft_transfer()
        rules = load_rules(self.guides)
        self.assertIn('transfer', rules.pending)
        self.assertNotIn('transfer', rules.active)
        outcome = self.check(self.source())
        self.assertFalse(outcome.valid)
        self.assertFalse(outcome.complete)
        self.assertIn('BA-OP-UNCOVERED', {d.code for d in outcome.diagnostics})

    def test_unrecognized_operator_is_reported(self):
        """DDTA-TC: TC-FR-MR02-03-03-01
        DDTA-NC: FR-MR02-03-03/NC-2 MD5=dad9c7ba80f4cf4ec45f72a7dc6ba398
        DDTA-NC: FR-MR02-03-03/NC-3 MD5=007a1638fcb3ff5dcda27b3ccb868512
        """
        src=self.source().replace(' - transfer',' - notDeclared')
        outcome=self.check(src)
        self.assertFalse(outcome.valid)
        self.assertIn('BA-OP-UNKNOWN',{d.code for d in outcome.diagnostics})
        self.assertNotIn('BA-OP-UNCOVERED',{d.code for d in outcome.diagnostics})

    def test_deleted_guide_makes_operator_unknown(self):
        """DDTA-TC: TC-FR-MR02-03-03-01
        DDTA-NC: FR-MR02-03-03/NC-2 MD5=dad9c7ba80f4cf4ec45f72a7dc6ba398
        DDTA-NC: FR-MR02-03-03/NC-3 MD5=007a1638fcb3ff5dcda27b3ccb868512
        """
        (self.guides/'operators'/'produce.md').unlink()
        result = self.check(self.source().replace(' - transfer', ' - produce'))
        self.assertIn('BA-OP-UNKNOWN', {d.code for d in result.diagnostics})
        self.assertNotIn('BA-OP-UNCOVERED', {d.code for d in result.diagnostics})

    def test_draft_guide_stays_recognized_but_uncovered(self):
        """DDTA-TC: TC-FR-MR02-03-03-01
        DDTA-NC: FR-MR02-03-03/NC-2 MD5=dad9c7ba80f4cf4ec45f72a7dc6ba398
        DDTA-NC: FR-MR02-03-03/NC-3 MD5=007a1638fcb3ff5dcda27b3ccb868512
        """
        p = self.guides/'operators'/'produce.md'
        raw = p.read_text(encoding='utf-8')
        p.write_text(raw.replace('reviewStatus: reviewed','reviewStatus: draft'), encoding='utf-8')
        result = self.check(self.source().replace(' - transfer', ' - produce'))
        self.assertIn('BA-OP-UNCOVERED', {d.code for d in result.diagnostics})
        self.assertNotIn('BA-OP-UNKNOWN', {d.code for d in result.diagnostics})

    def test_declared_cardinality_can_change_without_python(self):
        """DDTA-TC: TC-FR-MR02-03-03-02
        DDTA-NC: FR-MR02-03-03/NC-4 MD5=f90b0da1df935eedbbe7a077bd3fe5bb
        """
        path=self.active_transfer()
        before=self.check(self.source())
        self.assertTrue(before.valid)
        original=path.read_text(encoding='utf-8')
        path.write_text(original.replace('source: {min: 1, max: 1}','source: {min: 2, max: 2}'),encoding='utf-8')
        after=self.check(self.source())
        self.assertIn('BA-ROLE-MISSING',{d.code for d in after.diagnostics})
        self.assertNotEqual(before.ruleset.get('operator:transfer'),after.ruleset.get('operator:transfer'))

    def test_new_synthetic_operator_needs_only_guide_not_python(self):
        """DDTA-TC: TC-FR-MR02-03-03-03
        DDTA-NC: FR-MR02-03-03/NC-1 MD5=80d63f7a1b96b5dc7bd70afdce274137
        """
        self.active_transfer()
        guide=self.guides/'operators'/'syntheticPart.md'
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

    def test_temporal_scope_is_recognized_but_incomplete(self):
        """DDTA-TC: TC-FR-MR02-03-03-04
        DDTA-NC: FR-MR02-03-03/NC-3 MD5=007a1638fcb3ff5dcda27b3ccb868512
        """
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

    def test_temporal_scope_does_not_suppress_polarity_error(self):
        """DDTA-TC: TC-FR-MR02-03-03-04
        DDTA-NC: FR-MR02-03-03/NC-3 MD5=007a1638fcb3ff5dcda27b3ccb868512
        """
        src = self.source().replace('  polarity    = affirmative',
                                    '  temporalScope = DuringTraining')
        out = self.check(src)
        self.assertIn('BA-POLARITY-MISSING', {d.code for d in out.diagnostics})
        self.assertIn('BA-TEMPORAL-SCOPE-UNVERIFIED', {d.code for d in out.diagnostics})

if __name__ == "__main__":
    unittest.main()
