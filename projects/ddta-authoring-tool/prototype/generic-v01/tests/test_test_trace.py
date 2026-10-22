"""Pilot regression for TestSpecification ↔ Python test reciprocal links."""
from pathlib import Path
import shutil
import tempfile
import unittest

from ddta_tool.test_trace import check_test_specifications

PROJECT = Path(__file__).resolve().parents[3]


class TestTraceabilityTest(unittest.TestCase):
    def test_bidirectional_links(self):
        """DDTA-TC: TC-FR-MR03-06-02-01"""
        paths = [
            'docs/03-functional-requirements/FR-MR02-03-01.md',
            'docs/03-functional-requirements/FR-MR03-06-02.md',
            'docs/05-test-specifications/TS-FR-MR02-03-01.md',
            'docs/05-test-specifications/TS-FR-MR03-06-02.md',
            'prototype/generic-v01/tests/test_ba_catalog.py',
            'prototype/generic-v01/tests/test_test_trace.py',
        ]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in paths:
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(PROJECT / name, target)
            valid = check_test_specifications(root, 'pilot')
            self.assertTrue(valid.valid, valid.as_dict())
            self.assertEqual(valid.cases, 2)
            self.assertEqual(valid.mapped_tests, 2)
            self.assertEqual(valid.unmapped_tests, 0)
            edited = root / 'prototype/generic-v01/tests/test_ba_catalog.py'
            original = edited.read_text(encoding='utf-8')
            edited.write_text(original.replace('DDTA-TC: TC-FR-MR02-03-01-01',
                                               'DDTA-TC: TC-FR-MR02-03-01-99'), encoding='utf-8')
            invalid = check_test_specifications(root, 'pilot')
            self.assertFalse(invalid.valid)
            self.assertIn('TC-BACKLINK', {d.code for d in invalid.diagnostics})


if __name__ == '__main__':
    unittest.main()
