"""FR-owned regression scenarios; normative trace in TestSpecification."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest

from ddta_tool.relations import check_workspace
from _relation_fixtures import RelationFixtureMixin


class DocumentIdentityTest(RelationFixtureMixin, unittest.TestCase):
    def test_uses_metadata_not_filename(self):
        """DDTA-TC: TC-FR-MR03-01-01-01
        DDTA-NC: FR-MR03-01-01/NC-1 MD5=e2afd96c0fd1d7e6a160040f2d0de5f9
        DDTA-NC: FR-MR03-01-01/NC-5 MD5=33ea6995facdb7139b926f4a83785eb4
        """
        self.doc('MacroRequirement', 'MR-A', name='different.md')
        self.doc('Decision', 'DEC-A', parent='MR-A', name='some-other-name.md')
        self.assertTrue(check_workspace(self.root).valid)

    def test_duplicate_id_detected_across_types(self):
        """DDTA-TC: TC-FR-MR03-01-01-02
        DDTA-NC: FR-MR03-01-01/NC-2 MD5=f93df5058c0e235b904e619a372c498c
        DDTA-NC: FR-MR03-01-01/NC-3 MD5=5c308fd0dc42ca358d901a9a152e0ff8
        """
        self.doc('MacroRequirement', 'MR-A')
        self.doc('Decision', 'MR-A', parent='MR-A')
        self.assertIn('REL-ID-DUPLICATE', self.codes(check_workspace(self.root)))

    def test_duplicate_identity_in_two_files(self):
        """DDTA-TC: TC-FR-MR03-01-01-03
        DDTA-NC: FR-MR03-01-01/NC-3 MD5=5c308fd0dc42ca358d901a9a152e0ff8
        """
        self.doc('MacroRequirement', 'MR-A')
        self.doc('MacroRequirement', 'MR-A', name='AnotherFilename.md')
        self.doc('Decision', 'DEC-A', parent='MR-A')
        result = check_workspace(self.root)
        self.assertIn('REL-ID-DUPLICATE', self.codes(result))
        self.assertFalse(result.valid)

    def test_ignores_non_document_markdown_outside_governed_folders(self):
        """DDTA-TC: TC-FR-MR03-01-01-04
        DDTA-NC: FR-MR03-01-01/NC-1 MD5=e2afd96c0fd1d7e6a160040f2d0de5f9
        """
        self.valid_hierarchy()
        (self.root / 'README.md').write_text('# Not a DDTA document\n', encoding='utf-8')
        self.assertTrue(check_workspace(self.root).valid)

    def test_malformed_document_is_not_silently_ignored(self):
        """DDTA-TC: TC-FR-MR03-01-01-05
        DDTA-NC: FR-MR03-01-01/NC-4 MD5=9422271e1c2388db245948f20f730dec
        """
        self.valid_hierarchy()
        p = self.root / '02-decisions' / 'broken.md'
        p.write_text('# Without frontmatter\n', encoding='utf-8')
        result = check_workspace(self.root)
        self.assertFalse(result.complete)
        self.assertIn('DOC-FRONTMATTER', self.codes(result))
        self.assertFalse(result.valid)

    def test_blank_scope_is_not_pass(self):
        """DDTA-TC: TC-FR-MR03-01-01-06
        DDTA-NC: FR-MR03-01-01/NC-4 MD5=9422271e1c2388db245948f20f730dec
        """
        (self.root / '01-macro-requirements').mkdir()
        result = check_workspace(self.root)
        self.assertFalse(result.complete)
        self.assertIn('REL-SCOPE-EMPTY', self.codes(result))

    def test_unavailable_scope_is_not_pass(self):
        """DDTA-TC: TC-FR-MR03-01-01-07
        DDTA-NC: FR-MR03-01-01/NC-4 MD5=9422271e1c2388db245948f20f730dec
        """
        result = check_workspace(self.root / 'missing')
        self.assertFalse(result.complete)
        self.assertIn('REL-SCOPE-UNAVAILABLE', self.codes(result))

    def test_scope_with_unrecognized_subdirectories_is_not_pass(self):
        """DDTA-TC: TC-FR-MR03-01-01-08
        DDTA-NC: FR-MR03-01-01/NC-4 MD5=9422271e1c2388db245948f20f730dec
        """
        (self.root / 'somewhere').mkdir()
        result = check_workspace(self.root)
        self.assertFalse(result.complete)
        self.assertIn('REL-SCOPE-UNSUPPORTED', self.codes(result))

    def test_repeatable_diagnostics(self):
        """DDTA-TC: TC-FR-MR03-01-01-09
        DDTA-NC: FR-MR03-01-01/NC-1 MD5=e2afd96c0fd1d7e6a160040f2d0de5f9
        """
        self.doc('Decision', 'DEC-A', parent='MR-MISSING')
        self.assertEqual(check_workspace(self.root).as_dict(),
                         check_workspace(self.root).as_dict())

