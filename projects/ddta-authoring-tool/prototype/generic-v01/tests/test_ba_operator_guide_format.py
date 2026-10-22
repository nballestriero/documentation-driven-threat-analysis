"""Canonical operator guide format, without historical source references."""
from pathlib import Path
import unittest
from ddta_tool.engine import load_schema, render_template, validate

ROOT = Path(__file__).resolve().parents[1]
GUIDES = (ROOT/'..'/'..'/'guides'/'ba').resolve()
TEMPLATE = GUIDES/'templates'/'BA_OPERATOR_GUIDE_TEMPLATE.md'

class BAOperatorGuideFormatTest(unittest.TestCase):
    def test_schema_is_loadable(self):
        s=load_schema('BAOperatorGuide')
        self.assertEqual(s['schemaVersion'],'0.1')
        self.assertEqual(s['metadata']['reviewStatus']['enum'],['draft','reviewed'])
        self.assertNotIn('sourceRefs',s['metadata'])
        self.assertNotIn('methodStatus',s['metadata'])

    def test_template_is_draft_and_incomplete(self):
        text=TEMPLATE.read_text(encoding='utf-8')
        self.assertTrue(validate(text,'draft').valid)
        self.assertFalse(validate(text,'strict').valid)

    def test_both_operator_guides_are_strict_valid(self):
        for name in ['transfer','produce']:
            with self.subTest(name=name):
                text=(GUIDES/'operators'/f'{name}.md').read_text(encoding='utf-8')
                self.assertTrue(validate(text,'strict').valid)

    def test_minimal_sections_and_optional_invariants(self):
        s=load_schema('BAOperatorGuide')
        sections=[x['name'] for x in s['sections']]
        self.assertEqual(sections,['Meaning','When to use','When not to use',
            'Disambiguation','Canonical contract','Invariants','Valid examples','Invalid examples'])
        self.assertFalse(next(x for x in s['sections'] if x['name']=='Invariants')['required'])
        self.assertFalse(next(x for x in s['sections'] if x['name']=='Disambiguation')['required'])
        for removed in ('Diagnostics','Source reconciliation'):
            self.assertNotIn(removed,sections)

    def test_empty_disambiguation_comment_is_accepted(self):
        txt=(GUIDES/'operators'/'produce.md').read_text(encoding='utf-8')
        self.assertIn('## Disambiguation\n\n<!-- -->',txt)
        self.assertTrue(validate(txt,'strict').valid)

    def test_schema_rejects_historical_fields(self):
        txt=(GUIDES/'operators'/'produce.md').read_text(encoding='utf-8')
        bad=txt.replace('reviewStatus: reviewed','sourceRefs: []\nreviewStatus: reviewed')
        self.assertIn('DOC-FIELD-UNKNOWN',{d.code for d in validate(bad,'strict').diagnostics})

    def test_generated_guide_draft(self):
        txt=render_template('BAOperatorGuide','BA2-OP-GENERATED','Generated draft')
        self.assertIn('## Canonical contract',txt)
        self.assertNotIn('sourceRefs:',txt)

    def test_unknown_section_is_rejected(self):
        txt=TEMPLATE.read_text(encoding='utf-8')+'\n## Source reconciliation\n\nObsolete.\n'
        self.assertIn('DOC-SECTION-UNKNOWN',{d.code for d in validate(txt,'strict').diagnostics})

if __name__=='__main__': unittest.main()
