"""C9 R3: declarative new types preserve legacy relation checks."""
import tempfile
import unittest
from pathlib import Path

from ddta_tool.snapshot import check_snapshot
from ddta_tool.engine import DEFAULT_SCHEMAS


class DeclarativeSnapshotTest(unittest.TestCase):
    def test_new_type_uses_loaded_schema_without_cross_type_claims(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / 'docs'
            folder = root / '06-declarative-probes'
            folder.mkdir(parents=True)
            document = folder / 'P.md'
            document.write_text("""---
type: C9DeclarativeProbe
schemaVersion: '0.1'
id: PROBE-C9-01
title: Declarative probe
lifecycle: candidate
reviewMode: trace
---

# PROBE-C9-01 — Declarative probe

## Purpose
A synthetic scenario.
""", encoding='utf-8')
            # The C9 schema is supplied externally by this bounded checkpoint.
            source = document.read_text(encoding='utf-8')
            result = check_snapshot(root, document, source, schemas_dir=DEFAULT_SCHEMAS)
            self.assertTrue(result['valid'], result)
            self.assertFalse(result['relationsChecked'])
            self.assertEqual(result['workspace']['documents'], 1)
            self.assertEqual(result['workspace']['diagnostics'], [])
            changed = source.replace('lifecycle: candidate\n', '')
            missing = check_snapshot(root, document, changed, schemas_dir=DEFAULT_SCHEMAS)
            self.assertIn('DOC-FIELD-MISSING', [d['code'] for d in missing['workspace']['diagnostics']])
            self.assertFalse(missing['relationsChecked'])

    def test_legacy_link_checks_remain_active(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / 'docs'
            folder = root / '03-functional-requirements'
            folder.mkdir(parents=True)
            document = folder / 'FR-X.md'
            source = """---
type: FunctionalRequirement
schemaVersion: '0.1'
id: FR-X
title: Example
parentDecision: DEC-MISSING
lifecycle: candidate
---

# FR-X — Example

## Functional obligation
Example.

## Normative clauses
- **NC-1:** Example.
"""
            document.write_text(source, encoding='utf-8')
            result = check_snapshot(root, document, source, schemas_dir=DEFAULT_SCHEMAS)
            self.assertTrue(result['relationsChecked'])
            self.assertIn('REL-TARGET-MISSING', [d['code'] for d in result['workspace']['diagnostics']])


if __name__ == '__main__':
    unittest.main()
