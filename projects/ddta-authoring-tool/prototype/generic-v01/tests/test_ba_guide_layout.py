"""C2 R3: separate freeform general guides from schema-governed BA operator sheets."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3] / 'guides'


class BASplitGuideLayoutTest(unittest.TestCase):
    def test_general_ba_guide_is_plain_markdown_without_operator_schema(self):
        data = (ROOT / 'ba' / 'GUIDE.md').read_text(encoding='utf-8')
        self.assertTrue(data.startswith('# Base Analysis — General Guide'))
        self.assertNotIn('type: BAOperatorGuide', data)
        self.assertFalse(data.startswith('---\n'))

    def test_only_canonical_operator_guides_are_catalogued(self):
        operators = ROOT / 'ba' / 'operators'
        self.assertEqual({p.stem for p in operators.glob('*.md')},{'transfer','produce'})
        self.assertFalse((ROOT/'ba'/'operator-registry.yaml').exists())
        self.assertFalse((ROOT/'ba'/'reviews'/'transfer-review-r3.md').exists())

    def test_mermaid_general_guide_is_a_placeholder(self):
        data = (ROOT / 'mermaid' / 'GUIDE.md').read_text(encoding='utf-8')
        self.assertIn('PLACEHOLDER', data)
        self.assertNotIn('type: BAOperatorGuide', data)


if __name__ == '__main__':
    unittest.main()
