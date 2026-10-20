"""Behavioral tests of the same generator and validator against multiple schemas."""
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
    def test_all_three_schemas_load(self):
        for name in ('MacroRequirement', 'Decision', 'FunctionalRequirement'):
            with self.subTest(name=name):
                self.assertEqual(load_schema(name)['schemaId'], name)

    def test_all_three_examples_strict(self):
        for name in ('MR-VALID.md', 'DEC-VALID.md', 'FR-VALID.md'):
            with self.subTest(name=name):
                result = validate((EXAMPLES / name).read_text(encoding='utf-8'))
                self.assertTrue(result.valid, result.as_dict())
                self.assertEqual(result.errors, 0)

    def test_generated_drafts_valid_and_warn(self):
        for typ, doc_id, missing in (('MacroRequirement', 'MR-X', 5),
                                     ('Decision', 'DEC-X', 5),
                                     ('FunctionalRequirement', 'FR-X', 4)):
            with self.subTest(typ=typ):
                draft = render_template(typ, doc_id)
                d = validate(draft, 'draft')
                s = validate(draft, 'strict')
                self.assertTrue(d.valid, d.as_dict())
                self.assertEqual(d.warnings, missing)
                self.assertFalse(s.valid)
                self.assertEqual(s.errors, missing)

    def test_parent_metadata_in_correct_type(self):
        dec = render_template('Decision', 'DEC-X', 'Title', {'parentMacroRequirement': 'MR-X'})
        fr = render_template('FunctionalRequirement', 'FR-X', 'Title', {'parentDecision': 'DEC-X'})
        self.assertIn('parentMacroRequirement: MR-X', dec)
        self.assertIn('parentDecision: DEC-X', fr)
        self.assertNotIn('parentDecision:', dec)
        self.assertNotIn('parentMacroRequirement:', fr)

    def test_parent_decision_missing_is_strict_error(self):
        src = (EXAMPLES / 'DEC-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-FIELD-MISSING', codes(src.replace('parentMacroRequirement: MR-DEMO-01\n', '')))

    def test_parent_fr_missing_is_strict_error(self):
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-FIELD-MISSING', codes(src.replace('parentDecision: DEC-DEMO-01\n', '')))

    def test_parent_decision_wrong_type_error(self):
        src = (EXAMPLES / 'DEC-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-FIELD-TYPE', codes(src.replace('parentMacroRequirement: MR-DEMO-01', 'parentMacroRequirement: [MR-DEMO-01]')))

    def test_fr_min_one_normative_clause(self):
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-CLAUSE-MISSING', codes(src.replace('- **NC-1:** Il motore MUST produrre un risultato verificabile.', '')))

    def test_fr_duplicate_clause(self):
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8')
        needle = '- **NC-1:** Il motore MUST produrre un risultato verificabile.'
        self.assertIn('DOC-CLAUSE-DUPLICATE', codes(src.replace(needle, needle+'\n'+needle)))

    def test_fr_malformed_clause(self):
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-CLAUSE-SYNTAX', codes(src.replace('- **NC-1:**', '- NC-1:')))

    def test_fr_empty_clause_draft_warns_strict_errors(self):
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8')
        src = src.replace('Il motore MUST produrre un risultato verificabile.', '<!-- da compilare -->')
        self.assertIn('DOC-CLAUSE-MISSING', codes(src, 'draft'))
        self.assertEqual(next(d.severity for d in validate(src, 'draft').diagnostics if d.code == 'DOC-CLAUSE-MISSING'), 'warning')
        self.assertEqual(next(d.severity for d in validate(src).diagnostics if d.code == 'DOC-CLAUSE-MISSING'), 'error')

    def test_yaml_bad_is_not_pass(self):
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace('dependsOn: []','dependsOn: [')
        result = validate(src)
        self.assertFalse(result.complete)
        self.assertIn('DOC-YAML', {x.code for x in result.diagnostics})

    def test_frontmatter_missing_is_not_pass(self):
        self.assertFalse(validate('# MR-X\n## Intent\nYes').complete)

    def test_unknown_type_is_incomplete_diagnostic(self):
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace('type: MacroRequirement','type: SpecialType')
        result = validate(src)
        self.assertFalse(result.complete)
        self.assertIn('DOC-SCHEMA', {x.code for x in result.diagnostics})

    def test_wrong_schema_version_rejected(self):
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace("schemaVersion: '0.1'", "schemaVersion: '9.9'")
        self.assertIn('DOC-FIELD-CONST', codes(src))

    def test_unknown_yaml_field_suggests_correct_name(self):
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace('lifecycle:', 'lifecyle:')
        self.assertIn('DOC-FIELD-UNKNOWN', codes(src))
        self.assertIn('lifecycle', str(validate(src).diagnostics))

    def test_no_mr_parent_and_no_objective(self):
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace('lifecycle:', 'parentDecision: DEC-X\nobjective: Wrong\nlifecycle:')
        self.assertIn('DOC-FIELD-UNKNOWN', codes(src))

    def test_depends_on_self_and_duplicates(self):
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8')
        self.assertIn('DOC-FIELD-SELF', codes(src.replace('dependsOn: []', 'dependsOn: [MR-DEMO-01]')))
        self.assertIn('DOC-FIELD-DUPLICATE', codes(src.replace('dependsOn: []', 'dependsOn: [MR-2, MR-2]')))

    def test_duplicate_yaml_keys(self):
        src = (EXAMPLES / 'DEC-VALID.md').read_text(encoding='utf-8').replace('id: DEC-DEMO-01', 'id: DEC-DEMO-01\nid: DEC-X')
        self.assertIn('DOC-YAML', codes(src))

    def test_section_typo(self):
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace('## Stakeholders', '## Stakeholdrs')
        self.assertIn('DOC-SECTION-UNKNOWN', codes(src))
        self.assertIn('DOC-SECTION-MISSING', codes(src))

    def test_code_fence_does_not_create_extra_heading(self):
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8')+'\n```markdown\n# A SECOND H1\n## Context\n```\n'
        self.assertTrue(validate(src).valid)

    def test_required_section_missing(self):
        src = (EXAMPLES / 'DEC-VALID.md').read_text(encoding='utf-8').split('## Consequences')[0]
        self.assertIn('DOC-SECTION-MISSING', codes(src))

    def test_missing_title_is_warn_in_draft(self):
        src = render_template('Decision', 'DEC-X')
        self.assertEqual(next(d.severity for d in validate(src,'draft').diagnostics if d.code=='DOC-FIELD-EMPTY'), 'warning')

    def test_wrong_h1(self):
        src = (EXAMPLES / 'FR-VALID.md').read_text(encoding='utf-8').replace('# FR-DEMO-01', '# FR-WRONG-01')
        self.assertIn('DOC-H1-MISMATCH', codes(src))

    def test_cannot_overwrite_existing_output(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)/'MR-NEW.md'
            cmd = [sys.executable, '-m','ddta_tool', 'new','MacroRequirement','--id','MR-X','--output',str(path)]
            first = subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
            second = subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(first.returncode,0,first.stderr)
            self.assertEqual(second.returncode,2)

    def test_cli_json(self):
        cmd = [sys.executable, '-m','ddta_tool', 'check',str(EXAMPLES/'FR-VALID.md'),'--json']
        result = subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual((data['type'],data['valid'],data['errors']),('FunctionalRequirement',True,0))

    def test_cli_report_invalid_exit_one(self):
        cmd = [sys.executable, '-m','ddta_tool', 'check',str(EXAMPLES/'FR-INVALID.md'),'--profile','strict','--json']
        result = subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(result.returncode,1,result.stderr)
        self.assertGreater(json.loads(result.stdout)['errors'],0)

    def test_reject_unknown_constraint_in_schema_fail_closed(self):
        with tempfile.TemporaryDirectory() as td:
            for path in DEFAULT_SCHEMAS.glob('*.yaml'):
                shutil.copy2(path, td)
            path = Path(td)/'macro-requirement.yaml'
            doc = path.read_text(encoding='utf-8').replace('required: true, default: candidate', 'required: true, extraUnknown: foo, default: candidate')
            path.write_text(doc, encoding='utf-8')
            result = validate((EXAMPLES/'MR-VALID.md').read_text(encoding='utf-8'),schemas_dir=Path(td))
            self.assertFalse(result.complete)
            self.assertIn('DOC-SCHEMA', {x.code for x in result.diagnostics})

    def test_adding_fourth_schema_needs_no_python_changes(self):
        with tempfile.TemporaryDirectory() as td:
            for path in DEFAULT_SCHEMAS.glob('*.yaml'):
                shutil.copy2(path,td)
            data = {
                'schemaId':'ExampleNote','schemaVersion':'0.1',
                'metadata':{
                    'type':{'type':'string','required':True,'default':'ExampleNote','const':'ExampleNote'},
                    'schemaVersion':{'type':'string','required':True,'default':'0.1','const':'0.1'},
                    'id':{'type':'string','required':True,'default':''},
                    'title':{'type':'string','required':True,'default':''},
                    'category':{'type':'string','required':True,'default':'sample'},
                },
                'sections':[{'name':'Summary','required':True,'kind':'text','hint':'Da compilare'}]
            }
            (Path(td)/'example-note.yaml').write_text(yaml.safe_dump(data,sort_keys=False),encoding='utf-8')
            self.assertEqual(load_schema('ExampleNote',Path(td))['schemaId'],'ExampleNote')
            src = render_template('ExampleNote','NOTE-01', 'Prova',schemas_dir=Path(td))
            self.assertIn('## Summary',src)
            self.assertTrue(validate(src,'draft',Path(td)).valid)
            filled = src.replace('<!-- Da compilare -->','Questo e un esempio.')
            self.assertTrue(validate(filled,'strict',Path(td)).valid)

    def test_no_implicit_cross_file_resolution(self):
        src = (EXAMPLES/'DEC-VALID.md').read_text(encoding='utf-8').replace('MR-DEMO-01','MR-DOES-NOT-EXIST')
        self.assertTrue(validate(src).valid)  # Deliberate limit: MR-03 deferred

    def test_generic_parser_can_receive_in_memory_text(self):
        src = (EXAMPLES/'MR-VALID.md').read_text(encoding='utf-8')
        self.assertTrue(validate(src).valid)

    def test_optional_section_does_not_need_presence(self):
        src = (EXAMPLES/'MR-VALID.md').read_text(encoding='utf-8')
        self.assertTrue(validate(src).valid)
        self.assertTrue(validate(src+'\n## Assumptions / Constraints\n\nNessuna ulteriore condizione.\n').valid)

    def test_schema_bad_regex_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            for path in DEFAULT_SCHEMAS.glob('*.yaml'):
                shutil.copy2(path,td)
            path=Path(td)/'functional-requirement.yaml'
            doc=path.read_text(encoding='utf-8').replace("itemPattern: '- \\*\\*(NC-[0-9]+):\\*\\*\\s*(.*)'", "itemPattern: '['")
            path.write_text(doc, encoding='utf-8')
            result=validate((EXAMPLES/'FR-VALID.md').read_text(encoding='utf-8'),schemas_dir=Path(td))
            self.assertFalse(result.complete)
            self.assertIn('DOC-SCHEMA',{d.code for d in result.diagnostics})


if __name__=='__main__':
    unittest.main()
