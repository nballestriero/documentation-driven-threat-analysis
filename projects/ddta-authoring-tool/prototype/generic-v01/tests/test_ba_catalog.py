"""Directory-based BA operator discovery and activation gates."""
from pathlib import Path
import tempfile,shutil,unittest
from ddta_tool.ba_rules import BARuleError,check_ba_text,load_rules
ROOT=Path(__file__).resolve().parents[1]
GUIDES=(ROOT/'..'/'..'/'guides'/'ba').resolve()
SOURCE=(ROOT/'examples'/'BA-C5-PRODUCE-VALID.md').read_text(encoding='utf-8')

class BACatalogTest(unittest.TestCase):
    def setUp(self):
        tmp=tempfile.TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        self.g=Path(tmp.name)/'ba';shutil.copytree(GUIDES,self.g)

    def test_no_registry_is_required(self):
        self.assertFalse((self.g/'operator-registry.yaml').exists())
        rules=load_rules(self.g)
        self.assertEqual(rules.recognized, frozenset({'produce','transfer'}))
        self.assertEqual(set(rules.active), {'produce','transfer'})
        self.assertNotIn('registry',rules.fingerprints)

    def test_unlisted_operator_is_unknown(self):
        out=check_ba_text(SOURCE.replace(' - produce',' - observe'),self.g)
        self.assertIn('BA-OP-UNKNOWN',{d.code for d in out.diagnostics})

    def test_draft_operator_is_incomplete(self):
        p=self.g/'operators'/'produce.md'
        p.write_text(p.read_text(encoding='utf-8').replace('reviewStatus: reviewed','reviewStatus: draft'),encoding='utf-8')
        out=check_ba_text(SOURCE,self.g)
        self.assertIn('BA-OP-UNCOVERED',{d.code for d in out.diagnostics})

    def test_mismatched_operator_filename_fails_closed(self):
        p=self.g/'operators'/'produce.md';p.rename(self.g/'operators'/'renamed.md')
        with self.assertRaises(BARuleError):load_rules(self.g)

    def test_valid_produce_and_transfer_remain_active(self):
        out=check_ba_text(SOURCE,self.g)
        self.assertTrue(out.valid,out.as_dict())

if __name__=='__main__':unittest.main()
