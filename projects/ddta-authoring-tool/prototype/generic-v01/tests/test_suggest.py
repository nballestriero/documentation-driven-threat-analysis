"""DDTA-FR: FR-MR01-03-02; schema-driven completion smoke tests."""
import unittest
from ddta_tool.suggest import suggest

class SuggestTest(unittest.TestCase):
    def test_missing_fields_are_schema_driven(self):
        src = "---\ntype: FunctionalRequirement\n\n---\n"
        items = suggest(src,3,1)['items']
        labels={v['label'] for v in items}
        self.assertIn('parentDecision',labels)
        self.assertIn('title',labels)
        self.assertNotIn('type',labels)

    def test_unknown_type_does_not_generate_fake_fields(self):
        src="---\ntype: UnknownType\n\n---\n"
        from ddta_tool.engine import SchemaError
        with self.assertRaises(SchemaError): suggest(src,3,1)

    def test_outside_front_matter_is_empty(self):
        src="---\ntype: FunctionalRequirement\n---\n# title\n"
        self.assertEqual(suggest(src,4,1),{'items': []})
