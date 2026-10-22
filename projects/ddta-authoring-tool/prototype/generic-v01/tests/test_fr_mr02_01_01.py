"""Test invariants for FR-MR02-01-01; ownership and clause MD5 are declared in TestSpecification."""
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
        """DDTA-TC: TC-FR-MR02-01-01-01
        DDTA-NC: FR-MR02-01-01/NC-1 MD5=91e31cab69ec7808675f8ade9a3d254f
        DDTA-NC: FR-MR02-01-01/NC-4 MD5=9ca2799c7344e056f97b63aaeef09b91
        """
        for schema_file in sorted(DEFAULT_SCHEMAS.glob('*.yaml')):
            declared = yaml.safe_load(schema_file.read_text(encoding='utf-8'))
            with self.subTest(schema=schema_file.name):
                self.assertEqual(load_schema(declared['schemaId'])['schemaId'], declared['schemaId'])

    def test_unknown_type_is_incomplete_diagnostic(self):
        """DDTA-TC: TC-FR-MR02-01-01-02
        DDTA-NC: FR-MR02-01-01/NC-3 MD5=0ea8f8ddff6bcd9528cff93a7fcbf6b3
        """
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace('type: MacroRequirement','type: SpecialType')
        result = validate(src)
        self.assertFalse(result.complete)
        self.assertIn('DOC-SCHEMA', {x.code for x in result.diagnostics})

    def test_wrong_schema_version_rejected(self):
        """DDTA-TC: TC-FR-MR02-01-01-04
        DDTA-NC: FR-MR02-01-01/NC-3 MD5=0ea8f8ddff6bcd9528cff93a7fcbf6b3
        """
        src = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8').replace("schemaVersion: '0.1'", "schemaVersion: '9.9'")
        self.assertIn('DOC-FIELD-CONST', codes(src))

    def test_reject_unknown_constraint_in_schema_fail_closed(self):
        """DDTA-TC: TC-FR-MR02-01-01-03
        DDTA-NC: FR-MR02-01-01/NC-3 MD5=0ea8f8ddff6bcd9528cff93a7fcbf6b3
        """
        with tempfile.TemporaryDirectory() as td:
            for path in DEFAULT_SCHEMAS.glob('*.yaml'):
                shutil.copy2(path, td)
            path = Path(td)/'macro-requirement.yaml'
            doc = path.read_text(encoding='utf-8').replace('required: true, default: candidate', 'required: true, extraUnknown: foo, default: candidate')
            path.write_text(doc, encoding='utf-8')
            result = validate((EXAMPLES/'MR-VALID.md').read_text(encoding='utf-8'),schemas_dir=Path(td))
            self.assertFalse(result.complete)
            self.assertIn('DOC-SCHEMA', {x.code for x in result.diagnostics})

    def test_schema_bad_regex_rejected(self):
        """DDTA-TC: TC-FR-MR02-01-01-05
        DDTA-NC: FR-MR02-01-01/NC-3 MD5=0ea8f8ddff6bcd9528cff93a7fcbf6b3
        """
        with tempfile.TemporaryDirectory() as td:
            for path in DEFAULT_SCHEMAS.glob('*.yaml'):
                shutil.copy2(path,td)
            path=Path(td)/'functional-requirement.yaml'
            doc=path.read_text(encoding='utf-8').replace("itemPattern: '- \\*\\*(NC-[0-9]+):\\*\\*\\s*(.*)'", "itemPattern: '['")
            path.write_text(doc, encoding='utf-8')
            result=validate((EXAMPLES/'FR-VALID.md').read_text(encoding='utf-8'),schemas_dir=Path(td))
            self.assertFalse(result.complete)
            self.assertIn('DOC-SCHEMA',{d.code for d in result.diagnostics})


if __name__ == "__main__":
    unittest.main()
