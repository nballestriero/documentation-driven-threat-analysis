"""Test invariants for FR-MR02-01-02; ownership and clause MD5 are declared in TestSpecification."""
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
    def test_all_three_examples_strict(self):
        """DDTA-TC: TC-FR-MR02-01-02-01
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        DDTA-NC: FR-MR02-01-02/NC-2 MD5=0c792d0900914203dfcd02b022dc6961
        """
        for name in ('MR-VALID.md', 'DEC-VALID.md', 'FR-VALID.md'):
            with self.subTest(name=name):
                result = validate((EXAMPLES / name).read_text(encoding='utf-8'))
                self.assertTrue(result.valid, result.as_dict())
                self.assertEqual(result.errors, 0)

    def test_parent_decision_missing_is_strict_error(self):
        """DDTA-TC: TC-FR-MR02-01-02-02
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'DEC-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-FIELD-MISSING', codes(src.replace('parentMacroRequirement: MR-DEMO-01\n', '')))

    def test_parent_fr_missing_is_strict_error(self):
        """DDTA-TC: TC-FR-MR02-01-02-02
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-FIELD-MISSING', codes(src.replace('parentDecision: DEC-DEMO-01\n', '')))

    def test_parent_decision_wrong_type_error(self):
        """DDTA-TC: TC-FR-MR02-01-02-02
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'DEC-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-FIELD-TYPE', codes(src.replace('parentMacroRequirement: MR-DEMO-01', 'parentMacroRequirement: [MR-DEMO-01]')))

    def test_fr_min_one_normative_clause(self):
        """DDTA-TC: TC-FR-MR02-01-02-03
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-CLAUSE-MISSING', codes(src.replace('- **NC-1:** Il motore MUST produrre un risultato verificabile.', '')))

    def test_fr_duplicate_clause(self):
        """DDTA-TC: TC-FR-MR02-01-02-03
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8')
        needle = '- **NC-1:** Il motore MUST produrre un risultato verificabile.'
        self.assertIn('DOC-CLAUSE-DUPLICATE', codes(src.replace(needle, needle+'\n'+needle)))

    def test_fr_malformed_clause(self):
        """DDTA-TC: TC-FR-MR02-01-02-03
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-CLAUSE-SYNTAX', codes(src.replace('- **NC-1:**', '- NC-1:')))

    def test_yaml_bad_is_not_pass(self):
        """DDTA-TC: TC-FR-MR02-01-02-04
        DDTA-NC: FR-MR02-01-02/NC-3 MD5=dc1decc96057ea96d112e923f5b11fac
        """
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace('dependsOn: []','dependsOn: [')
        result = validate(src)
        self.assertFalse(result.complete)
        self.assertIn('DOC-YAML', {x.code for x in result.diagnostics})

    def test_unknown_yaml_field_suggests_correct_name(self):
        """DDTA-TC: TC-FR-MR02-01-02-02
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace('lifecycle:', 'lifecyle:')
        self.assertIn('DOC-FIELD-UNKNOWN', codes(src))
        self.assertIn('lifecycle', str(validate(src).diagnostics))

    def test_no_mr_parent_and_no_objective(self):
        """DDTA-TC: TC-FR-MR02-01-02-02
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace('lifecycle:', 'parentDecision: DEC-X\nobjective: Wrong\nlifecycle:')
        self.assertIn('DOC-FIELD-UNKNOWN', codes(src))

    def test_depends_on_self_and_duplicates(self):
        """DDTA-TC: TC-FR-MR02-01-02-02
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-FIELD-SELF', codes(src.replace('dependsOn: []', 'dependsOn: [MR-DEMO-01]')))
        self.assertIn('DOC-FIELD-DUPLICATE', codes(src.replace('dependsOn: []', 'dependsOn: [MR-2, MR-2]')))

    def test_duplicate_yaml_keys(self):
        """DDTA-TC: TC-FR-MR02-01-02-04
        DDTA-NC: FR-MR02-01-02/NC-3 MD5=dc1decc96057ea96d112e923f5b11fac
        """
        src = (EXAMPLES / 'DEC-VALID.md').read_text(encoding='utf-8').replace('id: DEC-DEMO-01', 'id: DEC-DEMO-01\nid: DEC-X')
        self.assertIn('DOC-YAML', codes(src))

    def test_section_typo(self):
        """DDTA-TC: TC-FR-MR02-01-02-05
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace('## Stakeholders', '## Stakeholdrs')
        self.assertIn('DOC-SECTION-UNKNOWN', codes(src))
        self.assertIn('DOC-SECTION-MISSING', codes(src))

    def test_code_fence_does_not_create_extra_heading(self):
        """DDTA-TC: TC-FR-MR02-01-02-05
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8')+'\n```markdown\n# A SECOND H1\n## Context\n```\n'
        self.assertTrue(validate(src).valid)

    def test_required_section_missing(self):
        """DDTA-TC: TC-FR-MR02-01-02-05
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'DEC-VALID.md').read_text(encoding='utf-8').split('## Consequences')[0]
        self.assertIn('DOC-SECTION-MISSING', codes(src))

    def test_wrong_h1(self):
        """DDTA-TC: TC-FR-MR02-01-02-05
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8').replace('# FR-DEMO-01', '# FR-WRONG-01')
        self.assertIn('DOC-H1-MISMATCH', codes(src))

    def test_optional_section_does_not_need_presence(self):
        """DDTA-TC: TC-FR-MR02-01-02-06
        DDTA-NC: FR-MR02-01-02/NC-1 MD5=b945f945cb37a6f4abf9701149c67ee5
        """
        src = (EXAMPLES/'MR-VALID.md').read_text(encoding='utf-8')
        self.assertTrue(validate(src).valid)
        self.assertTrue(validate(src+'\n## Assumptions / Constraints\n\nNessuna ulteriore condizione.\n').valid)


if __name__ == "__main__":
    unittest.main()
