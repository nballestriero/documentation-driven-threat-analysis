"""C8 catalog invariance: one operator per valid guide, no extraneous entries."""
from pathlib import Path
import shutil
import tempfile
import unittest
from ddta_tool.ba_rules import BARuleError, load_rules

ROOT = Path(__file__).resolve().parents[1]
GUIDES = (ROOT / '..' / '..' / 'guides' / 'ba').resolve()


class BACatalogTest(unittest.TestCase):
    def test_operator_catalog_consistency(self):
        """DDTA-TC: TC-FR-MR02-03-01-01"""
        with tempfile.TemporaryDirectory() as tmp:
            guide_root = Path(tmp) / 'ba'
            shutil.copytree(GUIDES, guide_root)
            folder = guide_root / 'operators'
            entries = list(folder.iterdir())
            self.assertTrue(all(p.is_file() and not p.is_symlink() and p.suffix == '.md' for p in entries))
            result = load_rules(guide_root)
            expected = {p.stem for p in entries}
            self.assertEqual(set(result.recognized), expected)
            self.assertEqual(set(result.active) | set(result.pending), expected)
            self.assertFalse(set(result.active) & set(result.pending))
            self.assertEqual(len(result.recognized), len(entries))

            # The same catalogue invariant must reject an extraneous entry.
            (folder / 'unexpected.txt').write_text('not an operator guide', encoding='utf-8')
            with self.assertRaises(BARuleError):
                load_rules(guide_root)


if __name__ == '__main__':
    unittest.main()
