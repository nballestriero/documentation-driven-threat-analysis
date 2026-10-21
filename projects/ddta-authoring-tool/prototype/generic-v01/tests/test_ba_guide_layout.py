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

    def test_transfer_review_is_not_an_activated_operator(self):
        review = ROOT / 'ba' / 'reviews' / 'transfer-review-r3.md'
        self.assertTrue(review.is_file())
        self.assertNotEqual(review.parent.name, 'operators')
        content = review.read_text(encoding='utf-8')
        self.assertTrue(content.startswith('---\n'))
        self.assertIn('## Canonical contract', content)
        self.assertIn('# BA2-OP-TRANSFER — Transfer — operator review draft R3', content)
        self.assertIn('NOT EXECUTABLE', content)


    def test_transfer_review_has_no_mermaid_projection_rules(self):
        text = (ROOT / 'ba' / 'reviews' / 'transfer-review-r3.md').read_text(encoding='utf-8')
        self.assertNotIn('Mermaid', text)

    def test_mermaid_general_guide_is_a_placeholder(self):
        data = (ROOT / 'mermaid' / 'GUIDE.md').read_text(encoding='utf-8')
        self.assertIn('PLACEHOLDER', data)
        self.assertNotIn('type: BAOperatorGuide', data)


if __name__ == '__main__':
    unittest.main()
