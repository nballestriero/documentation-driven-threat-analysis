"""Pilot regression for TestSpecification ↔ Python test reciprocal links."""
from pathlib import Path
import shutil
import tempfile
import unittest

from ddta_tool.test_trace import check_test_specifications

PROJECT = Path(__file__).resolve().parents[3]


class TestTraceabilityTest(unittest.TestCase):
    def test_bidirectional_links(self):
        """DDTA-TC: TC-FR-MR03-06-02-01
        DDTA-NC: FR-MR03-06-02/NC-1 MD5=502c0fa19d4338c953ecaa4b4642072b
        DDTA-NC: FR-MR03-06-02/NC-2 MD5=0fe47a5fd24cad161b1c0f84f8b81fa0
        DDTA-NC: FR-MR03-06-02/NC-3 MD5=97a8b07d1ae323ebab85feb2986bb517
        DDTA-NC: FR-MR03-06-02/NC-4 MD5=762814ea135b405ed000987b380d24bc
        DDTA-NC: FR-MR03-06-02/NC-6 MD5=6a9bba656c810a9c6fd09eb800f225d0
        DDTA-NC: FR-MR03-06-02/NC-7 MD5=0473234dc5ae5868ff5f84e837e3a7b9
        DDTA-NC: FR-MR03-06-02/NC-8 MD5=fae02eb0b16eb9178e4b569289ebc3a2
        """
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
            # Restore the case ID, then make the code claim a stale NC fingerprint.
            edited.write_text(original, encoding='utf-8')
            other_test = root / 'prototype/generic-v01/tests/test_test_trace.py'
            other_source = other_test.read_text(encoding='utf-8')
            other_test.write_text(other_source.replace('MD5=502c0fa19d4338c953ecaa4b4642072b',
                                                      'MD5=00000000000000000000000000000000'),
                                  encoding='utf-8')
            stale_code = check_test_specifications(root, 'pilot')
            self.assertIn('TC-BACKLINK-NC', {d.code for d in stale_code.diagnostics})
            # Restore the code, change the FR without changing any expected MD5.
            other_test.write_text(other_source, encoding='utf-8')
            fr = root / 'docs/03-functional-requirements/FR-MR03-06-02.md'
            src = fr.read_text(encoding='utf-8')
            fr.write_text(src.replace('MUST risolvere il `parentFunctionalRequirement`',
                                      'MUST individuare e risolvere il `parentFunctionalRequirement`'),
                          encoding='utf-8')
            changed_fr = check_test_specifications(root, 'pilot')
            self.assertIn('TC-CLAUSE-MD5', {d.code for d in changed_fr.diagnostics})


if __name__ == '__main__':
    unittest.main()
