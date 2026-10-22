"""Test invariants for FR-MR01-02-01; ownership and clause MD5 are declared in TestSpecification."""
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
    def test_frontmatter_missing_is_not_pass(self):
        """DDTA-TC: TC-FR-MR01-02-01-01
        DDTA-NC: FR-MR01-02-01/NC-3 MD5=46aeb1b4ee2d561fee2e3809dc17e9f6
        """
        self.assertFalse(validate('# MR-X\n## Intent\nYes').complete)


if __name__ == "__main__":
    unittest.main()
