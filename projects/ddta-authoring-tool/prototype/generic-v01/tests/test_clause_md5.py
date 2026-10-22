"""Deterministic clause fingerprint contract, linked to FR-MR03-06-04."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from ddta_tool.clause_md5 import ClauseFingerprintError, fingerprint_clauses, md5_clause

ROOT = Path(__file__).resolve().parents[1]


class ClauseMD5Test(unittest.TestCase):
    def test_clause_fingerprint_contract(self):
        """DDTA-TC: TC-FR-MR03-06-04-01
        DDTA-NC: FR-MR03-06-04/NC-1 MD5=4fd97934427105321546ed15aea0bf33
        DDTA-NC: FR-MR03-06-04/NC-2 MD5=c625108a01d2968c652822037fbc5f7d
        DDTA-NC: FR-MR03-06-04/NC-3 MD5=f35aebb112b245f0c9a535557313a238
        DDTA-NC: FR-MR03-06-04/NC-4 MD5=15333c36dd5d2404593ef449aad2f377
        """
        original = ('# FR-EX — Esempio\n\n## Normative clauses\n\n'
                    '- **NC-1:** Deve riconoscere café senza differenze di spazi.\n'
                    '- **NC-2:** Deve rifiutare una clausola duplicata.\n\n'
                    '## Riferimenti SPO e BA\nNessuno.\n')
        wrapped = ('# FR-EX — Esempio\r\n\r\n## Normative clauses\r\n\r\n'
                   '- **NC-1:** Deve riconoscere cafe\u0301\r\n'
                   '  senza differenze di   spazi.\r\n'
                   '- **NC-2:** Deve rifiutare una clausola duplicata.\r\n\r\n'
                   '## Riferimenti SPO e BA\r\nNessuno.\r\n')
        expected = fingerprint_clauses(original)
        self.assertEqual(expected, fingerprint_clauses(wrapped))
        self.assertEqual(expected['NC-1'], md5_clause('Deve riconoscere café senza differenze di spazi.'))
        changed = original.replace('senza differenze', 'con differenze')
        self.assertNotEqual(expected['NC-1'], fingerprint_clauses(changed)['NC-1'])
        self.assertEqual(expected['NC-2'], fingerprint_clauses(changed)['NC-2'])
        with self.assertRaises(ClauseFingerprintError):
            fingerprint_clauses(original.replace('## Riferimenti SPO e BA',
                                                  '- **NC-1:** Duplicata.\n\n## Riferimenti SPO e BA'))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'FR-EX.md'
            path.write_text(original, encoding='utf-8', newline='\n')
            cmd = [sys.executable, '-m', 'ddta_tool.clause_md5', str(path), '--clause', 'NC-1', '--json']
            result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)['clauses'], {'NC-1': expected['NC-1']})
            missing = subprocess.run(cmd[:-2] + ['NC-999'], cwd=ROOT,
                                     capture_output=True, text=True, encoding='utf-8')
            self.assertNotEqual(missing.returncode, 0)


if __name__ == '__main__':
    unittest.main()
