"""Regression for document-to-artifact evidence, separate from FR semantic approval."""
from __future__ import annotations
from pathlib import Path
import tempfile
import unittest

from ddta_tool.implementations import check_implementation_bindings

FR_ID = 'FR-MR03-02-02'
FILE = 'prototype/generic-v01/ddta_tool/demo.py'


def make_fr(root: Path, claim='partial', bindings=None, doc_id=FR_ID):
    folder = root / 'docs/03-functional-requirements'
    folder.mkdir(parents=True, exist_ok=True)
    if bindings is None:
        bindings = [f'{FILE}::sample']
    from yaml import safe_dump
    meta = {'type':'FunctionalRequirement','schemaVersion':'0.1','id':doc_id,
            'title':'Verifica test','parentDecision':'DEC-MR03-02',
            'lifecycle':'candidate','authority':'EXPERIMENTAL_NON_CANONICAL',
            'implementationClaim':claim,'implementationBindings':bindings}
    body = (f'# {doc_id} — Verifica test\n\n## Functional obligation\n\n'
            'Controllare il binding.\n\n## Normative clauses\n\n'
            '- **NC-1:** La verifica MUST distinguere file e simbolo.\n')
    (folder / f'{doc_id}.md').write_text('---\n'+safe_dump(meta,sort_keys=False,allow_unicode=True)+'---\n\n'+body,encoding='utf-8')


def make_code(root: Path, code=None):
    dest = root / FILE
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(code or f'def sample():\n    """DDTA-FR: {FR_ID}"""\n    return True\n',encoding='utf-8')


class ImplementationEvidenceTest(unittest.TestCase):
    def setup_project(self, claim='partial', bindings=None, code=True):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        make_fr(root,claim,bindings)
        if code: make_code(root)
        return root

    def codes(self,root):
        return [d.code for d in check_implementation_bindings(root).diagnostics]

    def test_valid_partial_binding(self):
        root=self.setup_project()
        result=check_implementation_bindings(root)
        self.assertTrue(result.valid,result.as_dict())
        self.assertEqual((result.documents,result.claims,result.bindings),(1,1,1))

    def test_valid_implemented_is_only_evidence(self):
        root=self.setup_project(claim='implemented')
        self.assertTrue(check_implementation_bindings(root).valid)

    def test_unassessed_without_binding(self):
        root=self.setup_project(claim='unassessed',bindings=[])
        make_code(root,'def sample():\n    return True\n')
        self.assertTrue(check_implementation_bindings(root).valid)

    def test_no_binding_fails_partial(self):
        root=self.setup_project(bindings=[])
        self.assertIn('IMP-BINDINGS-MISSING',self.codes(root))

    def test_missing_file(self):
        root=self.setup_project(code=False)
        self.assertIn('IMP-ARTIFACT',self.codes(root))

    def test_missing_symbol(self):
        root=self.setup_project()
        make_code(root,'def other():\n    """DDTA-FR: FR-MR03-02-02"""\n    return True\n')
        self.assertIn('IMP-SYMBOL',self.codes(root))

    def test_missing_backlink(self):
        root=self.setup_project()
        make_code(root,'def sample():\n    """DDTA-FR: FR-WRONG"""\n    return True\n')
        self.assertIn('IMP-BACKLINK',self.codes(root))

    def test_traversal_path_rejected(self):
        root=self.setup_project(bindings=['prototype/../../outside.py::sample'])
        self.assertIn('IMP-BINDING-PATH',self.codes(root))

    def test_bad_binding_format(self):
        root=self.setup_project(bindings=['sample.py'])
        self.assertIn('IMP-BINDING-FORMAT',self.codes(root))

    def test_scope_unavailable(self):
        with tempfile.TemporaryDirectory() as t:
            result=check_implementation_bindings(Path(t))
            self.assertFalse(result.valid)
            self.assertFalse(result.complete)
            self.assertIn('IMP-SCOPE', [d.code for d in result.diagnostics])

    def test_unassessed_cannot_verify_claim(self):
        root=self.setup_project(claim='unassessed')
        self.assertIn('IMP-UNASSESSED-BINDINGS',self.codes(root))

    def test_unknown_fr_in_code_is_reported(self):
        root=self.setup_project()
        make_code(root, f'def sample():\n    \"\"\"DDTA-FR: {FR_ID}\n    DDTA-FR: FR-DOES-NOT-EXIST\"\"\"\n    return True\n')
        self.assertIn('IMP-FR-UNKNOWN', self.codes(root))

    def test_orphan_code_tag_is_reported(self):
        root=self.setup_project()
        make_code(root, f'def sample():\n    \"\"\"DDTA-FR: {FR_ID}\"\"\"\n    return True\n'
                  f'def extra():\n    \"\"\"DDTA-FR: {FR_ID}\"\"\"\n    return True\n')
        self.assertIn('IMP-BACKLINK-ORPHAN', self.codes(root))

    def test_malformed_code_tag_is_reported(self):
        root=self.setup_project()
        make_code(root, f'def sample():\n    \"\"\"DDTA-FR: {FR_ID}\n    DDTA-FR: !not-valid!\"\"\"\n    return True\n')
        self.assertIn('IMP-CODE-TAG-FORMAT', self.codes(root))

    def test_diagnostics_are_deterministic(self):
        root=self.setup_project(code=False)
        a=check_implementation_bindings(root).as_dict()
        b=check_implementation_bindings(root).as_dict()
        self.assertEqual(a,b)

if __name__=='__main__':
    unittest.main()
