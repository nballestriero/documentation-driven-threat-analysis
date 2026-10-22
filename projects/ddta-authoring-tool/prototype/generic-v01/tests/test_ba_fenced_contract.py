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
        """DDTA-TC: TC-FR-MR02-01-02-50
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        self.assertEqual(next(s['kind'] for s in load_schema('BAOperatorGuide')['sections']
                              if s['name'] == 'Canonical contract'), 'fenced')
        for operator in (path.stem for path in sorted((GUIDES / 'operators').glob('*.md'))):
            with self.subTest(operator=operator):
                out = validate(self._source(operator), 'strict')
                self.assertTrue(out.valid, out.as_dict())

    def test_empty_fenced_contract_is_rejected(self):
        """DDTA-TC: TC-FR-MR02-01-02-51
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        for operator in (path.stem for path in sorted((GUIDES / 'operators').glob('*.md'))):
            with self.subTest(operator=operator):
                src = self._source(operator)
                changed, count = re.subn(r'(?ms)^```yaml ba-rule\s*\n.*?^```',
                                         '```yaml ba-rule\n```', src, count=1)
                self.assertEqual(count, 1)
                out = validate(changed, 'strict')
                self.assertIn('DOC-SECTION-EMPTY', {d.code for d in out.diagnostics})

    def test_prose_cannot_replace_fenced_contract(self):
        """DDTA-TC: TC-FR-MR02-01-02-52
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = self._source('produce')
        changed, count = re.subn(r'(?ms)^```yaml ba-rule\s*\n.*?^```',
                                 'The rule is described elsewhere.', src, count=1)
        self.assertEqual(count, 1)
        out = validate(changed, 'strict')
        self.assertIn('DOC-SECTION-EMPTY', {d.code for d in out.diagnostics})

    def test_unclosed_fence_is_rejected(self):
        """DDTA-TC: TC-FR-MR02-01-02-53
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        DDTA-NC: FR-MR02-01-02/NC-3 MD5=dc1decc96057ea96d112e923f5b11fac
        """
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
