"""Document-level BAOperatorGuide checks only; NOT validation of BA semantics.

Candidate implementation test for FR-MR02-03-01 (partial envelope only).
"""
from pathlib import Path
import unittest

from ddta_tool.engine import load_schema, render_template, validate

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = (ROOT / '..' / '..' / 'guides' / 'ba' / 'templates' /
            'BA_OPERATOR_GUIDE_TEMPLATE.md').resolve()


class BAOperatorGuideFormatTest(unittest.TestCase):
    def test_guide_schema_is_loadable_without_engine_changes(self):
        schema = load_schema('BAOperatorGuide')
        self.assertEqual(schema['schemaVersion'], '0.1')
        self.assertEqual(schema['metadata']['reviewStatus']['enum'], ['draft', 'reviewed'])

    def test_template_is_deliberately_incomplete(self):
        source = TEMPLATE.read_text(encoding='utf-8')
        self.assertTrue(validate(source, 'draft').valid)
        self.assertGreater(validate(source, 'draft').warnings, 0)
        strict = validate(source, 'strict')
        self.assertFalse(strict.valid)
        self.assertGreater(strict.errors, 0)

    def test_synthetic_filled_guide_passes_document_format_only(self):
        schema = load_schema('BAOperatorGuide')
        lines = ['---', "type: BAOperatorGuide", "schemaVersion: '0.1'",
                 'id: BA2-OP-SYNTHETIC', "title: 'Synthetic example'",
                 'methodStatus: unresolved', 'reviewStatus: draft',
                 'sourceRefs:', '  - methodology/TEST_ONLY.md', '---', '',
                 '# BA2-OP-SYNTHETIC — Synthetic example', '']
        for section in schema['sections']:
            lines.extend([f"## {section['name']}", '',
                          'Synthetic fixture content; no BA operator is admitted.', ''])
        result = validate('\n'.join(lines), 'strict')
        self.assertTrue(result.valid, result.as_dict())

    def test_disambiguation_optional_and_empty(self):
        schema = load_schema('BAOperatorGuide')
        disambiguation = [s for s in schema['sections'] if s['name'] == 'Disambiguation']
        self.assertEqual(len(disambiguation), 1)
        self.assertFalse(disambiguation[0]['required'])

        # The original template deliberately leaves nine REQUIRED sections empty.
        # Test the optional field against an otherwise complete document, so an
        # unrelated DOC-SECTION-EMPTY does not cause a false failure.
        def filled_guide(include_disambiguation: bool) -> str:
            lines = [
                '---',
                'type: BAOperatorGuide',
                "schemaVersion: '0.1'",
                'id: BA2-OP-SYNTHETIC-DISAMBIGUATION',
                "title: 'Synthetic disambiguation fixture'",
                'methodStatus: unresolved',
                'reviewStatus: draft',
                'sourceRefs:',
                '  - methodology/TEST_ONLY.md',
                '---', '',
                '# BA2-OP-SYNTHETIC-DISAMBIGUATION — Synthetic disambiguation fixture', '',
            ]
            for section in schema['sections']:
                if section['name'] == 'Disambiguation':
                    if include_disambiguation:
                        lines.extend(['## Disambiguation', ''])  # intentionally empty
                    continue
                lines.extend([
                    f"## {section['name']}", '',
                    'Synthetic fixture content; no BA operator is admitted.', '',
                ])
            return '\n'.join(lines)

        empty_result = validate(filled_guide(include_disambiguation=True), 'strict')
        self.assertTrue(empty_result.valid, empty_result.as_dict())

        absent_result = validate(filled_guide(include_disambiguation=False), 'strict')
        self.assertTrue(absent_result.valid, absent_result.as_dict())

    def test_polarity_not_redefined_as_transfer_specific_role(self):
        review = (ROOT / '..' / '..' / 'guides' / 'ba' / 'reviews' / 'transfer-review-r3.md').resolve().read_text(encoding='utf-8')
        import re, yaml
        found = re.search(r'```yaml ba-rule\n(contractVersion: .*?)\n```', review, re.DOTALL)
        self.assertIsNotNone(found)
        contract = yaml.safe_load(found.group(1))
        self.assertEqual(contract['semanticOperatorKey'], 'transfer')
        self.assertNotIn('polarity', contract['roles'])
        self.assertIn('polarity = negative', review)

    def test_transfer_review_passes_document_schema_only(self):
        review = (ROOT / '..' / '..' / 'guides' / 'ba' / 'reviews' /
                  'transfer-review-r3.md').resolve().read_text(encoding='utf-8')
        result = validate(review, 'strict')
        self.assertTrue(result.valid, result.as_dict())
        self.assertIn('REVIEW DRAFT / NOT EXECUTABLE', review)

    def test_operator_review_guidance_is_english(self):
        review = (ROOT / '..' / '..' / 'guides' / 'ba' / 'reviews' /
                  'transfer-review-r3.md').resolve().read_text(encoding='utf-8')
        for italian in ('Un trasferimento asserisce',
                        'Solo quando la documentazione',
                        'Manca un ruolo obbligatorio',
                        'La sintassi', 'Campo facoltativo'):
            self.assertNotIn(italian, review)
        for heading in ('Meaning', 'When to use', 'When not to use',
                        'Canonical contract', 'Diagnostics', 'Source reconciliation'):
            self.assertIn('## ' + heading + '\n', review)

    def test_all_canonical_operator_headings_are_english(self):
        schema = load_schema('BAOperatorGuide')
        expected = ['Meaning', 'When to use', 'When not to use', 'Disambiguation',
                    'Canonical contract', 'Invariants', 'Diagnostics',
                    'Valid examples', 'Invalid examples', 'Source reconciliation']
        self.assertEqual([section['name'] for section in schema['sections']], expected)
        source = TEMPLATE.read_text(encoding='utf-8')
        for heading in expected:
            self.assertIn(f'## {heading}\n', source)
        self.assertNotIn('## Significato\n', source)

    def test_italian_legacy_heading_is_rejected(self):
        source = TEMPLATE.read_text(encoding='utf-8').replace('## Meaning', '## Significato')
        result = validate(source, 'strict')
        codes = {item.code for item in result.diagnostics}
        self.assertIn('DOC-SECTION-UNKNOWN', codes)
        self.assertIn('DOC-SECTION-MISSING', codes)

    def test_unknown_section_stays_rejected(self):
        source = TEMPLATE.read_text(encoding='utf-8')
        source += '\n## Invented section\n\nContent.\n'
        codes = {d.code for d in validate(source, 'strict').diagnostics}
        self.assertIn('DOC-SECTION-UNKNOWN', codes)

    def test_missing_source_refs_is_not_strict_pass(self):
        source = TEMPLATE.read_text(encoding='utf-8').replace(
            'sourceRefs:\n  - methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex\n'
            '  - methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex',
            'sourceRefs: []')
        codes = {d.code for d in validate(source, 'strict').diagnostics}
        self.assertIn('DOC-FIELD-LIST-SIZE', codes)

    def test_generator_understands_new_guide_type(self):
        source = render_template('BAOperatorGuide', 'BA2-OP-GENERATED', 'Generated draft')
        self.assertIn('type: BAOperatorGuide', source)
        self.assertIn('## Canonical contract', source)
        self.assertNotIn('semanticOperatorKey:', source)


if __name__ == '__main__':
    unittest.main()
