"""Test cases justified by FR-MR02-02-03 and its TestSpecification."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from ddta_tool.ba_rules import BARuleError, check_ba_text, load_rules
from _ba_rule_fixtures import BARuleFixture, ROOT, GUIDES, EXAMPLE, BAD_EXAMPLE

class BAGuideDiagnosticsTest(BARuleFixture, unittest.TestCase):

    def test_missing_content_reads_guide_diagnostic(self):
        """DDTA-TC: TC-FR-MR02-02-03-01
        DDTA-NC: FR-MR02-02-03/NC-1 MD5=fd9f206be8404f51925d325c0c52764e
        DDTA-NC: FR-MR02-02-03/NC-2 MD5=1755882b68fc682d99b4083434d0e3a8
        DDTA-NC: FR-MR02-02-03/NC-5 MD5=30d5f78f5673be63db47fa6a965f2f78
        """
        self.active_transfer()
        result = self.check(self.source().replace('  content     -> DataX    # BAR-EX-C4-X\n',''))
        d = next(d for d in result.diagnostics if d.code == 'BA-ROLE-MISSING')
        self.assertIn('content', d.message)
        self.assertIn('Canonical contract',d.guideSection)
        self.assertIn('never invent',d.llmInstruction)
        self.assertIn('operators/transfer.md',d.guideRef)

if __name__ == "__main__":
    unittest.main()
