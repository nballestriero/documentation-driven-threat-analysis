"""Common BA rule test setup; no test scenarios or normative rule definitions."""
from pathlib import Path
import shutil
import tempfile
from ddta_tool.ba_rules import check_ba_text

ROOT = Path(__file__).resolve().parents[1]
GUIDES = (ROOT / '..' / '..' / 'guides' / 'ba').resolve()
EXAMPLE = ROOT / 'examples' / 'BA-C4-TRANSFER-VALID.md'
BAD_EXAMPLE = ROOT / 'examples' / 'BA-C4-TRANSFER-INVALID.md'

class BARuleFixture:

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.guides = Path(self.temp.name) / 'ba'
        shutil.copytree(GUIDES, self.guides)

    def active_transfer(self):
        # DDTA-FR: FR-MR02-03-01 — the checked-in guide declares its execution status.
        file = self.guides / 'operators' / 'transfer.md'
        src = file.read_text(encoding='utf-8')
        self.assertIn('reviewStatus: reviewed', src)
        return file

    def draft_transfer(self):
        # Test the review gate by demoting an isolated copy, never the repository.
        file = self.active_transfer()
        src = file.read_text(encoding='utf-8')
        file.write_text(src.replace('reviewStatus: reviewed','reviewStatus: draft'), encoding='utf-8')
        return file

    def source(self):
        return EXAMPLE.read_text(encoding='utf-8')

    def check(self, text):
        return check_ba_text(text, self.guides)
