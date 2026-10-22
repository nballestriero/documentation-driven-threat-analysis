"""Canonical operator guide format, without historical source references."""
from pathlib import Path
import unittest
from ddta_tool.engine import load_schema, render_template, validate

ROOT = Path(__file__).resolve().parents[1]
GUIDES = (ROOT/'..'/'..'/'guides'/'ba').resolve()
TEMPLATE = GUIDES/'templates'/'BA_OPERATOR_GUIDE_TEMPLATE.md'

class BAOperatorGuideFormatTest(unittest.TestCase):
    def test_schema_is_loadable(self):
        """DDTA-TC: TC-FR-MR02-03-01-51
        DDTA-NC: FR-MR02-03-01/NC-2 MD5=dc6245cc70957ffeb45860136f21c2de
        """
        s=load_schema('BAOperatorGuide')
        self.assertEqual(s['schemaVersion'],'0.1')
        self.assertEqual(s['metadata']['reviewStatus']['enum'],['draft','reviewed'])

    def test_template_is_draft_and_incomplete(self):
        """DDTA-TC: TC-FR-MR02-01-02-54
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        DDTA-NC: FR-MR02-01-02/NC-3 MD5=dc1decc96057ea96d112e923f5b11fac
        """
        text=TEMPLATE.read_text(encoding='utf-8')
        self.assertTrue(validate(text,'draft').valid)
        self.assertFalse(validate(text,'strict').valid)

    def test_all_declared_operator_guides_are_strict_valid(self):
        """DDTA-TC: TC-FR-MR02-03-01-52
        DDTA-NC: FR-MR02-03-01/NC-1 MD5=a0c0a2418e53828f54107a142f1a234f
        DDTA-NC: FR-MR02-03-01/NC-2 MD5=dc6245cc70957ffeb45860136f21c2de
        """
        operator_paths = sorted((GUIDES / 'operators').glob('*.md'))
        self.assertTrue(operator_paths, 'An empty set cannot prove guide validity')
        for path in operator_paths:
            with self.subTest(operator=path.stem):
                self.assertTrue(validate(path.read_text(encoding='utf-8'),'strict').valid)

    def test_minimal_sections_and_optional_invariants(self):
        """DDTA-TC: TC-FR-MR02-03-01-53
        DDTA-NC: FR-MR02-03-01/NC-2 MD5=dc6245cc70957ffeb45860136f21c2de
        """
        s=load_schema('BAOperatorGuide')
        sections=[x['name'] for x in s['sections']]
        self.assertEqual(sections,['Meaning','When to use','When not to use',
            'Disambiguation','Canonical contract','Invariants','Valid examples','Invalid examples'])
        self.assertFalse(next(x for x in s['sections'] if x['name']=='Invariants')['required'])
        self.assertFalse(next(x for x in s['sections'] if x['name']=='Disambiguation')['required'])
        for removed in ('Diagnostics','Source reconciliation'):
            self.assertNotIn(removed,sections)

    def test_empty_disambiguation_comment_is_accepted(self):
        """DDTA-TC: TC-FR-MR02-01-02-55
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        txt=(GUIDES/'operators'/'produce.md').read_text(encoding='utf-8')
        self.assertIn('## Disambiguation\n\n<!-- -->',txt)
        self.assertTrue(validate(txt,'strict').valid)

    def test_schema_rejects_undeclared_fields(self):
        """DDTA-TC: TC-FR-MR02-01-02-56
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        txt=(GUIDES/'operators'/'produce.md').read_text(encoding='utf-8')
        bad=txt.replace('reviewStatus: reviewed','unexpectedAttribute: true\nreviewStatus: reviewed')
        self.assertIn('DOC-FIELD-UNKNOWN',{d.code for d in validate(bad,'strict').diagnostics})

    def test_generated_guide_draft(self):
        """DDTA-TC: TC-FR-MR02-01-02-57
        DDTA-NC: FR-MR02-01-02/NC-2 MD5=0c792d0900914203dfcd02b022dc6961
        """
        txt=render_template('BAOperatorGuide','BA2-OP-GENERATED','Generated draft')
        self.assertIn('## Canonical contract',txt)

    def test_unknown_section_is_rejected(self):
        """DDTA-TC: TC-FR-MR02-01-02-58
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        txt=TEMPLATE.read_text(encoding='utf-8')+'\n## Source reconciliation\n\nObsolete.\n'
        self.assertIn('DOC-SECTION-UNKNOWN',{d.code for d in validate(txt,'strict').diagnostics})

if __name__=='__main__': unittest.main()
