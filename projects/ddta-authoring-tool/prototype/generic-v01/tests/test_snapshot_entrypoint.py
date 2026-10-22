"""C9 R1A: same engine for persisted scope and unsaved editor snapshots."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

from ddta_tool.snapshot import check_snapshot


ROOT = Path(__file__).resolve().parents[3]
EXAMPLES = ROOT / 'pilots' / 'c9-independent-project' / 'docs'
FR_REL = '03-functional-requirements/FR-DEMO-01.md'


class SnapshotEntrypointTest(unittest.TestCase):
    def test_snapshot_cli_api_equivalence_and_no_write(self):
        source_path = EXAMPLES / FR_REL
        original = source_path.read_bytes()
        unsaved = original.decode('utf-8').replace('parentDecision: DEC-DEMO-01',
                                                    'parentDecision: DEC-UNKNOWN')
        self.assertNotEqual(unsaved.encode('utf-8'), original)
        api = check_snapshot(EXAMPLES, FR_REL, unsaved, profile='strict')
        command = [sys.executable, '-m', 'ddta_tool', 'check-snapshot',
                   str(EXAMPLES), FR_REL, '--profile', 'strict', '--json']
        output = subprocess.run(command, input=unsaved.encode('utf-8'),
                                capture_output=True, check=False)
        stdout = output.stdout.decode('utf-8')
        stderr = output.stderr.decode('utf-8', errors='replace')
        self.assertEqual(output.returncode, 1, stderr)
        self.assertEqual(json.loads(stdout), api)
        self.assertIn('REL-TARGET-MISSING',
                      {d['code'] for d in api['workspace']['diagnostics']})
        self.assertEqual(source_path.read_bytes(), original)

    def test_snapshot_rejects_foreign_file(self):
        with self.assertRaises(ValueError):
            check_snapshot(EXAMPLES, '../../outside.md', 'text')

    def test_pilot_workspace_is_valid(self):
        from ddta_tool.relations import check_workspace
        result = check_workspace(EXAMPLES)
        self.assertTrue(result.valid, result.as_dict())
        self.assertEqual(result.documents, 3)
