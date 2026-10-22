"""Test invariants for FR-MR01-01-04; ownership and clause MD5 are declared in TestSpecification."""
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
    def test_cli_json(self):
        """DDTA-TC: TC-FR-MR01-01-04-01
        DDTA-NC: FR-MR01-01-04/NC-1 MD5=28cbf70282a967317aeb2d3134b6870b
        """
        cmd = [sys.executable, '-m','ddta_tool', 'check',str(EXAMPLES/'FR-VALID.md'),'--json']
        result = subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual((data['type'],data['valid'],data['errors']),('FunctionalRequirement',True,0))

    def test_cli_report_invalid_exit_one(self):
        """DDTA-TC: TC-FR-MR01-01-04-01
        DDTA-NC: FR-MR01-01-04/NC-1 MD5=28cbf70282a967317aeb2d3134b6870b
        """
        cmd = [sys.executable, '-m','ddta_tool', 'check',str(EXAMPLES/'FR-INVALID.md'),'--profile','strict','--json']
        result = subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(result.returncode,1,result.stderr)
        self.assertGreater(json.loads(result.stdout)['errors'],0)


if __name__ == "__main__":
    unittest.main()
