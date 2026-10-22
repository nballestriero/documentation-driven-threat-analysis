"""Test cases justified by FR-MR02-03-01 and its TestSpecification."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from ddta_tool.ba_rules import BARuleError, check_ba_text, load_rules
from _ba_rule_fixtures import BARuleFixture, ROOT, GUIDES, EXAMPLE, BAD_EXAMPLE

class BARuleLoadingTest(BARuleFixture, unittest.TestCase):

    def test_reviewed_transfer_loads_from_guide_and_passes(self):
        """DDTA-TC: TC-FR-MR02-03-01-02
        DDTA-NC: FR-MR02-03-01/NC-1 MD5=a0c0a2418e53828f54107a142f1a234f
        DDTA-NC: FR-MR02-03-01/NC-2 MD5=dc6245cc70957ffeb45860136f21c2de
        DDTA-NC: FR-MR02-03-01/NC-5 MD5=e1e17c2035c74b93a8aeca32757c3422
        """
        self.active_transfer()
        rules = load_rules(self.guides)
        self.assertEqual(rules.active['transfer'].roles['source'],(1,1))
        outcome = self.check(self.source())
        self.assertTrue(outcome.valid, outcome.as_dict())
        self.assertEqual(outcome.errors,0)
        self.assertTrue(outcome.ruleset.get('operator:transfer'))

    def test_unsupported_constraint_fails_closed(self):
        """DDTA-TC: TC-FR-MR02-03-01-03
        DDTA-NC: FR-MR02-03-01/NC-4 MD5=cbf31593f5ec18fd84c378ddb7bbdb4d
        """
        path=self.active_transfer()
        raw=path.read_text(encoding='utf-8')
        path.write_text(raw.replace('constraints: []','constraints: [unimplementedConstraint]'),encoding='utf-8')
        with self.assertRaises(BARuleError): load_rules(self.guides)
        result=self.check(self.source())
        self.assertIn('BA-RULESET-INVALID',{d.code for d in result.diagnostics})
        self.assertFalse(result.complete)

    def test_duplicate_rule_keys_fail_closed(self):
        """DDTA-TC: TC-FR-MR02-03-01-04
        DDTA-NC: FR-MR02-03-01/NC-2 MD5=dc6245cc70957ffeb45860136f21c2de
        """
        path=self.active_transfer()
        duplicate=self.guides/'operators'/'another.md'
        raw=path.read_text(encoding='utf-8')
        duplicate.write_text(raw.replace('id: BA2-OP-TRANSFER','id: BA2-OP-TRANSFER-ANOTHER')
            .replace('# BA2-OP-TRANSFER —','# BA2-OP-TRANSFER-ANOTHER —'),encoding='utf-8')
        with self.assertRaises(BARuleError):load_rules(self.guides)

    def test_invalid_rule_contract_duplicates_and_unknown_key(self):
        """DDTA-TC: TC-FR-MR02-03-01-04
        DDTA-NC: FR-MR02-03-01/NC-2 MD5=dc6245cc70957ffeb45860136f21c2de
        """
        path=self.active_transfer()
        raw=path.read_text(encoding='utf-8').replace('  source: {min: 1, max: 1}',
                 '  source: {min: 1, max: 1}\n  source: {min: 0, max: 1}')
        path.write_text(raw,encoding='utf-8')
        with self.assertRaises(BARuleError):load_rules(self.guides)

    def test_operator_catalog_consistency(self):
        """DDTA-TC: TC-FR-MR02-03-01-01
        DDTA-NC: FR-MR02-03-01/NC-1 MD5=a0c0a2418e53828f54107a142f1a234f
        DDTA-NC: FR-MR02-03-01/NC-2 MD5=dc6245cc70957ffeb45860136f21c2de
        DDTA-NC: FR-MR02-03-01/NC-3 MD5=28c22ed27c0e5018b2ebd53d46b01fef
        """
        with tempfile.TemporaryDirectory() as tmp:
            guide_root = Path(tmp) / 'ba'
            shutil.copytree(GUIDES, guide_root)
            folder = guide_root / 'operators'
            entries = list(folder.iterdir())
            self.assertTrue(all(p.is_file() and not p.is_symlink() and p.suffix == '.md' for p in entries))
            result = load_rules(guide_root)
            expected = {p.stem for p in entries}
            self.assertEqual(set(result.recognized), expected)
            self.assertEqual(set(result.active) | set(result.pending), expected)
            self.assertFalse(set(result.active) & set(result.pending))
            self.assertEqual(len(result.recognized), len(entries))
    
            # The same catalogue invariant must reject an extraneous entry.
            (folder / 'unexpected.txt').write_text('not an operator guide', encoding='utf-8')
            with self.assertRaises(BARuleError):
                load_rules(guide_root)

if __name__ == "__main__":
    unittest.main()
