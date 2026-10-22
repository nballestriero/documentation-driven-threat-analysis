"""C2 R3: separate freeform general guides from schema-governed BA operator sheets."""
from pathlib import Path
import shutil
import tempfile
import unittest

from ddta_tool.ba_rules import load_rules

ROOT = Path(__file__).resolve().parents[3] / 'guides'


class BASplitGuideLayoutTest(unittest.TestCase):

    def test_operator_guides_are_discovered_from_directory(self):
        """DDTA-TC: TC-FR-MR02-03-01-50
        DDTA-NC: FR-MR02-03-01/NC-1 MD5=a0c0a2418e53828f54107a142f1a234f
        DDTA-NC: FR-MR02-03-01/NC-3 MD5=28c22ed27c0e5018b2ebd53d46b01fef
        """
        guides = ROOT / 'ba'
        rules = load_rules(guides)
        filenames = {p.stem for p in (guides / 'operators').iterdir()}
        self.assertEqual(rules.recognized, filenames)
        self.assertEqual(set(rules.active) | set(rules.pending), filenames)

    def test_new_reviewed_operator_is_discovered_without_code_changes(self):
        # A temporary renamed copy is a syntactically valid additional operator.
        # This tests catalogue extensibility, not new semantic meaning.
        """DDTA-TC: TC-FR-MR02-03-03-50
        DDTA-NC: FR-MR02-03-03/NC-1 MD5=80d63f7a1b96b5dc7bd70afdce274137
        """
        with tempfile.TemporaryDirectory() as tmp:
            guides = Path(tmp) / 'ba'
            shutil.copytree(ROOT / 'ba' / 'contracts', guides / 'contracts')
            shutil.copytree(ROOT / 'ba' / 'operators', guides / 'operators')
            original = load_rules(guides)
            source = (guides / 'operators' / 'produce.md').read_text(encoding='utf-8')
            self.assertIn('semanticOperatorKey: produce', source)
            self.assertIn('id: BA2-OP-PRODUCE', source)
            candidate = source.replace('semanticOperatorKey: produce', 'semanticOperatorKey: probeOperator', 1)
            candidate = candidate.replace('id: BA2-OP-PRODUCE', 'id: BA2-OP-PROBE', 1)
            candidate = candidate.replace("title: 'Produce'", "title: 'Probe'", 1)
            candidate = candidate.replace('# BA2-OP-PRODUCE — Produce', '# BA2-OP-PROBE — Probe', 1)
            (guides / 'operators' / 'probeOperator.md').write_text(candidate, encoding='utf-8')
            expanded = load_rules(guides)
            self.assertEqual(expanded.recognized, original.recognized | {'probeOperator'})
            self.assertIn('probeOperator', expanded.active)
            self.assertEqual(set(original.active), set(expanded.active) - {'probeOperator'})



if __name__ == '__main__':
    unittest.main()
