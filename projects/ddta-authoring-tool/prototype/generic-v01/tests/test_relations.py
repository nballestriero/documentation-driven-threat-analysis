"""MR-03 candidate regression: declared identity, typed links, fail-closed scope."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from ddta_tool.engine import render_template
from ddta_tool.relations import check_workspace


class RelationCheckTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'docs'
        self.root.mkdir()

    def doc(self, kind: str, doc_id: str, *, parent: str | None = None,
            depends: list[str] | None = None, name: str | None = None) -> Path:
        paths = {'MacroRequirement': '01-macro-requirements',
                 'Decision': '02-decisions',
                 'FunctionalRequirement': '03-functional-requirements'}
        values = {}
        if kind == 'Decision':
            values['parentMacroRequirement'] = parent if parent is not None else 'MR-A'
        if kind == 'FunctionalRequirement':
            values['parentDecision'] = parent if parent is not None else 'DEC-A'
        data = render_template(kind, doc_id, f'Test {doc_id}', values=values)
        if kind == 'MacroRequirement' and depends is not None:
            data = data.replace('dependsOn: []', 'dependsOn: [' + ', '.join(depends) + ']')
        # Fill in only the intentionally incomplete template placeholders.
        data = data.replace('<!-- Da compilare -->', 'Il servizio MUST fornire il risultato.')
        import re
        data = re.sub(r'<!-- [^\n]* -->', 'Contenuto di test.', data)
        folder = self.root / paths[kind]
        folder.mkdir(exist_ok=True)
        file = folder / (name or doc_id + '.md')
        file.write_text(data, encoding='utf-8')
        return file

    def valid_hierarchy(self):
        self.doc('MacroRequirement', 'MR-A')
        self.doc('Decision', 'DEC-A', parent='MR-A')
        self.doc('FunctionalRequirement', 'FR-A', parent='DEC-A')

    def codes(self, result):
        return {d.code for d in result.diagnostics}

    def test_clean_three_level_hierarchy(self):
        self.valid_hierarchy()
        result = check_workspace(self.root)
        self.assertTrue(result.valid, result.as_dict())
        self.assertEqual((result.documents, result.errors), (3, 0))

    def test_missing_decision_parent(self):
        self.doc('MacroRequirement', 'MR-A')
        self.doc('Decision', 'DEC-A', parent='MR-NOT-THERE')
        result = check_workspace(self.root)
        self.assertIn('REL-TARGET-MISSING', self.codes(result))
        self.assertFalse(result.valid)

    def test_fr_parent_of_wrong_type(self):
        self.doc('MacroRequirement', 'MR-A')
        self.doc('FunctionalRequirement', 'FR-A', parent='MR-A')
        result = check_workspace(self.root)
        self.assertIn('REL-TARGET-TYPE', self.codes(result))
        self.assertFalse(result.valid)

    def test_duplicate_identity_and_ambiguous_target(self):
        self.doc('MacroRequirement', 'MR-A')
        self.doc('MacroRequirement', 'MR-A', name='AnotherFilename.md')
        self.doc('Decision', 'DEC-A', parent='MR-A')
        result = check_workspace(self.root)
        self.assertIn('REL-ID-DUPLICATE', self.codes(result))
        self.assertIn('REL-TARGET-AMBIGUOUS', self.codes(result))
        self.assertFalse(result.valid)

    def test_dependencies_resolve_only_macro_requirement(self):
        self.doc('MacroRequirement', 'MR-A', depends=['MR-B'])
        self.doc('MacroRequirement', 'MR-B')
        self.assertTrue(check_workspace(self.root).valid)
        (self.root / '01-macro-requirements' / 'MR-B.md').unlink()
        self.doc('Decision', 'MR-B', parent='MR-A')
        result = check_workspace(self.root)
        self.assertIn('REL-TARGET-TYPE', self.codes(result))

    def test_duplicate_id_detected_across_types(self):
        self.doc('MacroRequirement', 'MR-A')
        self.doc('Decision', 'MR-A', parent='MR-A')
        self.assertIn('REL-ID-DUPLICATE', self.codes(check_workspace(self.root)))

    def test_uses_metadata_not_filename(self):
        self.doc('MacroRequirement', 'MR-A', name='different.md')
        self.doc('Decision', 'DEC-A', parent='MR-A', name='some-other-name.md')
        self.assertTrue(check_workspace(self.root).valid)

    def test_ignores_non_document_markdown_outside_governed_folders(self):
        self.valid_hierarchy()
        (self.root / 'README.md').write_text('# Not a DDTA document\n', encoding='utf-8')
        self.assertTrue(check_workspace(self.root).valid)

    def test_malformed_document_is_not_silently_ignored(self):
        self.valid_hierarchy()
        p = self.root / '02-decisions' / 'broken.md'
        p.write_text('# Without frontmatter\n', encoding='utf-8')
        result = check_workspace(self.root)
        self.assertFalse(result.complete)
        self.assertIn('DOC-FRONTMATTER', self.codes(result))
        self.assertFalse(result.valid)

    def test_blank_scope_is_not_pass(self):
        (self.root / '01-macro-requirements').mkdir()
        result = check_workspace(self.root)
        self.assertFalse(result.complete)
        self.assertIn('REL-SCOPE-EMPTY', self.codes(result))

    def test_unavailable_scope_is_not_pass(self):
        result = check_workspace(self.root / 'missing')
        self.assertFalse(result.complete)
        self.assertIn('REL-SCOPE-UNAVAILABLE', self.codes(result))

    def test_scope_with_unrecognized_subdirectories_is_not_pass(self):
        (self.root / 'somewhere').mkdir()
        result = check_workspace(self.root)
        self.assertFalse(result.complete)
        self.assertIn('REL-SCOPE-UNSUPPORTED', self.codes(result))

    def test_draft_does_not_hide_broken_links(self):
        self.doc('Decision', 'DEC-A', parent='MR-MISSING')
        result = check_workspace(self.root, 'draft')
        self.assertIn('REL-TARGET-MISSING', self.codes(result))
        self.assertFalse(result.valid)

    def test_repeatable_diagnostics(self):
        self.doc('Decision', 'DEC-A', parent='MR-MISSING')
        self.assertEqual(check_workspace(self.root).as_dict(),
                         check_workspace(self.root).as_dict())

    def test_cli_json_exit_code(self):
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


if __name__ == '__main__':
    unittest.main()
