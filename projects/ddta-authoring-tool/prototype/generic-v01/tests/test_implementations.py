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
        """DDTA-TC: TC-FR-MR03-02-01-01
        DDTA-NC: FR-MR03-02-01/NC-1 MD5=040432d67cf3d4e64f87e88a5d997c2e
        DDTA-NC: FR-MR03-02-01/NC-2 MD5=92996b5b935dfcf97df37e1e47384f79
        """
        root=self.setup_project()
        result=check_implementation_bindings(root)
        self.assertTrue(result.valid,result.as_dict())
        self.assertEqual((result.documents,result.claims,result.bindings),(1,1,1))

    def test_valid_implemented_is_only_evidence(self):
        """DDTA-TC: TC-FR-MR03-02-01-02
        DDTA-NC: FR-MR03-02-01/NC-1 MD5=040432d67cf3d4e64f87e88a5d997c2e
        DDTA-NC: FR-MR03-02-01/NC-3 MD5=f320389fd7c6ceec02eb89010073bf28
        """
        root=self.setup_project(claim='implemented')
        self.assertTrue(check_implementation_bindings(root).valid)

    def test_unassessed_without_binding(self):
        """DDTA-TC: TC-FR-MR03-02-01-03
        DDTA-NC: FR-MR03-02-01/NC-2 MD5=92996b5b935dfcf97df37e1e47384f79
        """
        root=self.setup_project(claim='unassessed',bindings=[])
        make_code(root,'def sample():\n    return True\n')
        self.assertTrue(check_implementation_bindings(root).valid)

    def test_no_binding_fails_partial(self):
        """DDTA-TC: TC-FR-MR03-02-01-04
        DDTA-NC: FR-MR03-02-01/NC-2 MD5=92996b5b935dfcf97df37e1e47384f79
        """
        root=self.setup_project(bindings=[])
        self.assertIn('IMP-BINDINGS-MISSING',self.codes(root))

    def test_missing_file(self):
        """DDTA-TC: TC-FR-MR03-02-02-01
        DDTA-NC: FR-MR03-02-02/NC-1 MD5=2ac7ee10732f8cf8ac37e04ac06a713f
        DDTA-NC: FR-MR03-02-02/NC-2 MD5=ddc8abd884aff2835fbf82732ce9f201
        """
        root=self.setup_project(code=False)
        self.assertIn('IMP-ARTIFACT',self.codes(root))

    def test_missing_symbol(self):
        """DDTA-TC: TC-FR-MR03-02-02-02
        DDTA-NC: FR-MR03-02-02/NC-1 MD5=2ac7ee10732f8cf8ac37e04ac06a713f
        DDTA-NC: FR-MR03-02-02/NC-2 MD5=ddc8abd884aff2835fbf82732ce9f201
        """
        root=self.setup_project()
        make_code(root,'def other():\n    """DDTA-FR: FR-MR03-02-02"""\n    return True\n')
        self.assertIn('IMP-SYMBOL',self.codes(root))

    def test_missing_backlink(self):
        """DDTA-TC: TC-FR-MR03-02-02-03
        DDTA-NC: FR-MR03-02-02/NC-1 MD5=2ac7ee10732f8cf8ac37e04ac06a713f
        DDTA-NC: FR-MR03-02-02/NC-2 MD5=ddc8abd884aff2835fbf82732ce9f201
        """
        root=self.setup_project()
        make_code(root,'def sample():\n    """DDTA-FR: FR-WRONG"""\n    return True\n')
        self.assertIn('IMP-BACKLINK',self.codes(root))

    def test_traversal_path_rejected(self):
        """DDTA-TC: TC-FR-MR03-02-02-04
        DDTA-NC: FR-MR03-02-02/NC-2 MD5=ddc8abd884aff2835fbf82732ce9f201
        """
        root=self.setup_project(bindings=['prototype/../../outside.py::sample'])
        self.assertIn('IMP-BINDING-PATH',self.codes(root))

    def test_bad_binding_format(self):
        """DDTA-TC: TC-FR-MR03-02-02-05
        DDTA-NC: FR-MR03-02-02/NC-2 MD5=ddc8abd884aff2835fbf82732ce9f201
        """
        root=self.setup_project(bindings=['sample.py'])
        self.assertIn('IMP-BINDING-FORMAT',self.codes(root))

    def test_scope_unavailable(self):
        """DDTA-TC: TC-FR-MR03-02-02-06
        DDTA-NC: FR-MR03-02-02/NC-3 MD5=03a3b004a0fcd197e38c240c2d9178cc
        """
        with tempfile.TemporaryDirectory() as t:
            result=check_implementation_bindings(Path(t))
            self.assertFalse(result.valid)
            self.assertFalse(result.complete)
            self.assertIn('IMP-SCOPE', [d.code for d in result.diagnostics])

    def test_unassessed_with_known_binding_is_allowed(self):
        """DDTA-TC: TC-FR-MR03-02-01-05
        DDTA-NC: FR-MR03-02-01/NC-1 MD5=040432d67cf3d4e64f87e88a5d997c2e
        DDTA-NC: FR-MR03-02-01/NC-2 MD5=92996b5b935dfcf97df37e1e47384f79
        """
        root=self.setup_project(claim='unassessed')
        result=check_implementation_bindings(root)
        self.assertTrue(result.valid,result.as_dict())
        self.assertEqual((result.documents,result.claims,result.bindings),(1,0,1))

    def test_unassessed_with_missing_artifact_is_diagnosed(self):
        """DDTA-TC: TC-FR-MR03-02-01-06
        DDTA-NC: FR-MR03-02-01/NC-2 MD5=92996b5b935dfcf97df37e1e47384f79
        """
        root=self.setup_project(claim='unassessed',code=False)
        result=check_implementation_bindings(root)
        self.assertFalse(result.valid)
        self.assertIn('IMP-ARTIFACT',[d.code for d in result.diagnostics])
        self.assertNotIn('IMP-UNASSESSED-BINDINGS',[d.code for d in result.diagnostics])

    def test_unknown_fr_in_code_is_reported(self):
        """DDTA-TC: TC-FR-MR03-02-02-07
        DDTA-NC: FR-MR03-02-02/NC-5 MD5=d734ae8b1dc7199dd287cd184b1338d5
        """
        root=self.setup_project()
        make_code(root, f'def sample():\n    \"\"\"DDTA-FR: {FR_ID}\n    DDTA-FR: FR-DOES-NOT-EXIST\"\"\"\n    return True\n')
        self.assertIn('IMP-FR-UNKNOWN', self.codes(root))

    def test_orphan_code_tag_is_reported(self):
        """DDTA-TC: TC-FR-MR03-02-02-08
        DDTA-NC: FR-MR03-02-02/NC-5 MD5=d734ae8b1dc7199dd287cd184b1338d5
        """
        root=self.setup_project()
        make_code(root, f'def sample():\n    \"\"\"DDTA-FR: {FR_ID}\"\"\"\n    return True\n'
                  f'def extra():\n    \"\"\"DDTA-FR: {FR_ID}\"\"\"\n    return True\n')
        self.assertIn('IMP-BACKLINK-ORPHAN', self.codes(root))

    def test_malformed_code_tag_is_reported(self):
        """DDTA-TC: TC-FR-MR03-02-02-09
        DDTA-NC: FR-MR03-02-02/NC-5 MD5=d734ae8b1dc7199dd287cd184b1338d5
        """
        root=self.setup_project()
        make_code(root, f'def sample():\n    \"\"\"DDTA-FR: {FR_ID}\n    DDTA-FR: !not-valid!\"\"\"\n    return True\n')
        self.assertIn('IMP-CODE-TAG-FORMAT', self.codes(root))

    def test_diagnostics_are_deterministic(self):
        """DDTA-TC: TC-FR-MR02-02-01-01
        DDTA-NC: FR-MR02-02-01/NC-3 MD5=2a532695c50ec7e3dc9006eff88bda91
        """
        root=self.setup_project(code=False)
        a=check_implementation_bindings(root).as_dict()
        b=check_implementation_bindings(root).as_dict()
        self.assertEqual(a,b)

if __name__=='__main__':
    unittest.main()
