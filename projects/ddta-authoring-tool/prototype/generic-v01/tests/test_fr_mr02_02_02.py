"""Test invariants for FR-MR02-02-02; ownership and clause MD5 are declared in TestSpecification."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml
from ddta_tool.engine import DEFAULT_SCHEMAS, SchemaError, load_schema, render_template, validate

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / 'examples'


def codes(source: str, profile: str = 'strict', schemas_dir: Path = DEFAULT_SCHEMAS) -> set[str]:
    return {d.code for d in validate(source, profile, schemas_dir).diagnostics}



class GenericEngineTest(unittest.TestCase):
    def test_generated_drafts_valid_and_warn(self):
        """DDTA-TC: TC-FR-MR02-02-02-01
        DDTA-NC: FR-MR02-02-02/NC-1 MD5=4b1cc02cb12f9c7dec4cccacfa06c2d9
        DDTA-NC: FR-MR02-02-02/NC-2 MD5=833a75add75f7c8b668a9528f4237a7b
        DDTA-NC: FR-MR02-02-02/NC-3 MD5=58652ed147e0c948febac4bbb0296035
        """
        for typ, doc_id in (('MacroRequirement', 'MR-X'),
                                     ('Decision', 'DEC-X'),
                                     ('FunctionalRequirement', 'FR-X')):
            with self.subTest(typ=typ):
                draft = render_template(typ, doc_id)
                d = validate(draft, 'draft')
                s = validate(draft, 'strict')
                self.assertTrue(d.valid, d.as_dict())
                self.assertGreater(d.warnings, 0)
                self.assertFalse(s.valid)
                self.assertEqual(s.errors, d.warnings)

    def test_fr_empty_clause_draft_warns_strict_errors(self):
        """DDTA-TC: TC-FR-MR02-02-02-02
        DDTA-NC: FR-MR02-02-02/NC-1 MD5=4b1cc02cb12f9c7dec4cccacfa06c2d9
        DDTA-NC: FR-MR02-02-02/NC-2 MD5=833a75add75f7c8b668a9528f4237a7b
        DDTA-NC: FR-MR02-02-02/NC-3 MD5=58652ed147e0c948febac4bbb0296035
        """
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8')
        src = src.replace('Il motore MUST produrre un risultato verificabile.', '<!-- da compilare -->')
        self.assertIn('DOC-CLAUSE-MISSING', codes(src, 'draft'))
        self.assertEqual(next(d.severity for d in validate(src, 'draft').diagnostics if d.code == 'DOC-CLAUSE-MISSING'), 'warning')
        self.assertEqual(next(d.severity for d in validate(src).diagnostics if d.code == 'DOC-CLAUSE-MISSING'), 'error')

    def test_missing_title_is_warn_in_draft(self):
        """DDTA-TC: TC-FR-MR02-02-02-03
        DDTA-NC: FR-MR02-02-02/NC-1 MD5=4b1cc02cb12f9c7dec4cccacfa06c2d9
        DDTA-NC: FR-MR02-02-02/NC-2 MD5=833a75add75f7c8b668a9528f4237a7b
        DDTA-NC: FR-MR02-02-02/NC-3 MD5=58652ed147e0c948febac4bbb0296035
        """
        src = render_template('Decision', 'DEC-X')
        self.assertEqual(next(d.severity for d in validate(src,'draft').diagnostics if d.code=='DOC-FIELD-EMPTY'), 'warning')


if __name__ == "__main__":
    unittest.main()
