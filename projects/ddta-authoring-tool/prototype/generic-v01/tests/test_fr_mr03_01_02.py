"""FR-owned regression scenarios; normative trace in TestSpecification."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest

from ddta_tool.relations import check_workspace
from _relation_fixtures import RelationFixtureMixin


class DocumentRelationTest(RelationFixtureMixin, unittest.TestCase):
    def test_clean_three_level_hierarchy(self):
        """DDTA-TC: TC-FR-MR03-01-02-01
        DDTA-NC: FR-MR03-01-02/NC-1 MD5=edbffb61f39a0acddb28fb1b5352135c
        """
        self.valid_hierarchy()
        result = check_workspace(self.root)
        self.assertTrue(result.valid, result.as_dict())
        self.assertEqual((result.documents, result.errors), (3, 0))

    def test_missing_decision_parent(self):
        """DDTA-TC: TC-FR-MR03-01-02-02
        DDTA-NC: FR-MR03-01-02/NC-1 MD5=edbffb61f39a0acddb28fb1b5352135c
        DDTA-NC: FR-MR03-01-02/NC-3 MD5=187e2d64779fe02c19b614a51a2d4ef1
        """
        self.doc('MacroRequirement', 'MR-A')
        self.doc('Decision', 'DEC-A', parent='MR-NOT-THERE')
        result = check_workspace(self.root)
        self.assertIn('REL-TARGET-MISSING', self.codes(result))
        self.assertFalse(result.valid)

    def test_fr_parent_of_wrong_type(self):
        """DDTA-TC: TC-FR-MR03-01-02-03
        DDTA-NC: FR-MR03-01-02/NC-1 MD5=edbffb61f39a0acddb28fb1b5352135c
        DDTA-NC: FR-MR03-01-02/NC-3 MD5=187e2d64779fe02c19b614a51a2d4ef1
        """
        self.doc('MacroRequirement', 'MR-A')
        self.doc('FunctionalRequirement', 'FR-A', parent='MR-A')
        result = check_workspace(self.root)
        self.assertIn('REL-TARGET-TYPE', self.codes(result))
        self.assertFalse(result.valid)

    def test_ambiguous_parent_target(self):
        """DDTA-TC: TC-FR-MR03-01-02-04
        DDTA-NC: FR-MR03-01-02/NC-1 MD5=edbffb61f39a0acddb28fb1b5352135c
        DDTA-NC: FR-MR03-01-02/NC-3 MD5=187e2d64779fe02c19b614a51a2d4ef1
        """
        self.doc('MacroRequirement', 'MR-A')
        self.doc('MacroRequirement', 'MR-A', name='AnotherFilename.md')
        self.doc('Decision', 'DEC-A', parent='MR-A')
        result = check_workspace(self.root)
        self.assertIn('REL-TARGET-AMBIGUOUS', self.codes(result))
        self.assertFalse(result.valid)

    def test_dependencies_resolve_only_macro_requirement(self):
        """DDTA-TC: TC-FR-MR03-01-02-05
        DDTA-NC: FR-MR03-01-02/NC-2 MD5=99cd4f3905568966cdb1dc6f87ca310e
        DDTA-NC: FR-MR03-01-02/NC-3 MD5=187e2d64779fe02c19b614a51a2d4ef1
        """
        self.doc('MacroRequirement', 'MR-A', depends=['MR-B'])
        self.doc('MacroRequirement', 'MR-B')
        self.assertTrue(check_workspace(self.root).valid)
        (self.root / '01-macro-requirements' / 'MR-B.md').unlink()
        self.doc('Decision', 'MR-B', parent='MR-A')
        result = check_workspace(self.root)
        self.assertIn('REL-TARGET-TYPE', self.codes(result))

    def test_draft_does_not_hide_broken_links(self):
        """DDTA-TC: TC-FR-MR03-01-02-06
        DDTA-NC: FR-MR03-01-02/NC-3 MD5=187e2d64779fe02c19b614a51a2d4ef1
        DDTA-NC: FR-MR03-01-02/NC-4 MD5=9f5ca39dbb893c367e316f735bd1c70e
        """
        self.doc('Decision', 'DEC-A', parent='MR-MISSING')
        result = check_workspace(self.root, 'draft')
        self.assertIn('REL-TARGET-MISSING', self.codes(result))
        self.assertFalse(result.valid)

    def test_cli_json_exit_code(self):
        """DDTA-TC: TC-FR-MR03-01-02-07
        DDTA-NC: FR-MR03-01-02/NC-5 MD5=33bae312d6818d114b5360593eb01b54
        """
        self.valid_hierarchy()
        wd = Path(__file__).resolve().parents[1]
        command = [sys.executable, '-m', 'ddta_tool', 'check-workspace',
                   str(self.root), '--profile', 'strict', '--json']
        run = subprocess.run(command, cwd=wd, capture_output=True,
                             text=True, encoding='utf-8')
        self.assertEqual(run.returncode, 0, run.stderr + run.stdout)
        data = json.loads(run.stdout)
        self.assertEqual((data['documents'], data['valid']), (3, True))
        (self.root / '01-macro-requirements' / 'MR-A.md').unlink()
        run = subprocess.run(command, cwd=wd, capture_output=True,
                             text=True, encoding='utf-8')
        self.assertEqual(run.returncode, 1)
        self.assertIn('REL-TARGET-MISSING',
                      {d['code'] for d in json.loads(run.stdout)['diagnostics']})

