"""Regression tests for optional embedded BA in DDTA MR and Decision documents.

These checks test the *section contract*, not BA proposition semantics.
"""
from pathlib import Path
import unittest

from ddta_tool.engine import load_schema, validate

EXAMPLES = Path(__file__).resolve().parents[1] / 'examples'
BA = """
## Base Analysis

### BAReferent

| BAReferent | ID | Significato |
|---|---|---|
| `ExampleFunction` | `BAR-EX-01` | Funzione di esempio. |
| `ExampleDocument` | `BAR-EX-02` | Documento di esempio. |

### BAProposition

```text
BAP-EX-01 - produce
  actor  -> ExampleFunction  # BAR-EX-01
  result -> ExampleDocument  # BAR-EX-02
```
"""


class BaseAnalysisSectionSchemaTest(unittest.TestCase):
    def test_ba_section_optional_in_mr_and_decision(self):
        for name, dtype in (("MR-VALID.md", "MacroRequirement"),
                            ("DEC-VALID.md", "Decision")):
            with self.subTest(document_type=dtype):
                schema = load_schema(dtype)
                ba = [s for s in schema['sections'] if s['name'] == 'Base Analysis']
                self.assertEqual(len(ba), 1)
                self.assertFalse(ba[0]['required'])
                source = (EXAMPLES / name).read_text(encoding='utf-8')
                result = validate(source, 'strict')
                self.assertTrue(result.valid, result.as_dict())

    def test_embedded_ba_accepted_in_mr_and_decision(self):
        for name in ('MR-VALID.md', 'DEC-VALID.md'):
            with self.subTest(name=name):
                source = (EXAMPLES / name).read_text(encoding='utf-8')
                result = validate(source + BA, 'strict')
                self.assertTrue(result.valid, result.as_dict())

    def test_unknown_section_still_rejected(self):
        source = (EXAMPLES / 'MR-VALID.md').read_text(encoding='utf-8')
        result = validate(source + "\n## NotAnAllowedSection\n\nContenuto.\n", 'strict')
        codes = {d.code for d in result.diagnostics}
        self.assertIn('DOC-SECTION-UNKNOWN', codes)


if __name__ == '__main__':
    unittest.main()
