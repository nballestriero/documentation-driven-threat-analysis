"""Test invariants for FR-MR01-02-02; ownership and clause MD5 are declared in TestSpecification."""
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
    def test_parent_metadata_in_correct_type(self):
        """DDTA-TC: TC-FR-MR01-02-02-01
        DDTA-NC: FR-MR01-02-02/NC-1 MD5=c2227ce17220708f3267c77ba2cada42
        DDTA-NC: FR-MR01-02-02/NC-2 MD5=9118cdaae8632ddf35490a1012186b1a
        """
        dec = render_template('Decision', 'DEC-X', 'Title', {'parentMacroRequirement': 'MR-X'})
        fr = render_template('FunctionalRequirement', 'FR-X', 'Title', {'parentDecision': 'DEC-X'})
        self.assertIn('parentMacroRequirement: MR-X', dec)
        self.assertIn('parentDecision: DEC-X', fr)
        self.assertNotIn('parentDecision:', dec)
        self.assertNotIn('parentMacroRequirement:', fr)

    def test_adding_fourth_schema_needs_no_python_changes(self):
        """DDTA-TC: TC-FR-MR01-02-02-02
        DDTA-NC: FR-MR01-02-02/NC-1 MD5=c2227ce17220708f3267c77ba2cada42
        DDTA-NC: FR-MR01-02-02/NC-5 MD5=c7da450bb3a208d434a1826a9b58458e
        """
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


if __name__ == "__main__":
    unittest.main()
