"""Regression: fenced-only Canonical contract sections are valid content.

DDTA-FR: FR-MR02-01-02
"""
from pathlib import Path
import re
import unittest
from ddta_tool.engine import validate, load_schema

ROOT = Path(__file__).resolve().parents[1]
GUIDES = (ROOT / '..' / '..' / 'guides' / 'ba').resolve()

class BAContractFenceTest(unittest.TestCase):
    def _source(self, operator):
        return (GUIDES / 'operators' / f'{operator}.md').read_text(encoding='utf-8')

    def test_fenced_yaml_only_is_nonempty(self):
        self.assertEqual(next(s['kind'] for s in load_schema('BAOperatorGuide')['sections']
                              if s['name'] == 'Canonical contract'), 'fenced')
        for operator in ('produce', 'transfer'):
            with self.subTest(operator=operator):
                out = validate(self._source(operator), 'strict')
                self.assertTrue(out.valid, out.as_dict())

    def test_empty_fenced_contract_is_rejected(self):
        for operator in ('produce', 'transfer'):
            with self.subTest(operator=operator):
                src = self._source(operator)
                changed, count = re.subn(r'(?ms)^```yaml ba-rule\s*\n.*?^```',
                                         '```yaml ba-rule\n```', src, count=1)
                self.assertEqual(count, 1)
                out = validate(changed, 'strict')
                self.assertIn('DOC-SECTION-EMPTY', {d.code for d in out.diagnostics})

    def test_prose_cannot_replace_fenced_contract(self):
        src = self._source('produce')
        changed, count = re.subn(r'(?ms)^```yaml ba-rule\s*\n.*?^```',
                                 'The rule is described elsewhere.', src, count=1)
        self.assertEqual(count, 1)
        out = validate(changed, 'strict')
        self.assertIn('DOC-SECTION-EMPTY', {d.code for d in out.diagnostics})

    def test_unclosed_fence_is_rejected(self):
        src = self._source('produce')
        changed, count = re.subn(r'(?m)^```\s*$', '', src, count=1)
        self.assertEqual(count, 1)
        out = validate(changed, 'strict')
        # An unclosed fence hides subsequent section headings from the parser.
        # The document must fail validation, regardless of the fence payload.
        self.assertFalse(out.valid, out.as_dict())
        self.assertIn('DOC-SECTION-MISSING', {d.code for d in out.diagnostics})

if __name__ == '__main__':
    unittest.main()
