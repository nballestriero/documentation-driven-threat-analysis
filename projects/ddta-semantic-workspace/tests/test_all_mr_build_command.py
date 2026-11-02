"""Regression checks for the on-demand all-MR PowerShell view entrypoint."""
import unittest
from pathlib import Path

from tools.rdf_mermaid.render import render

ROOT = Path(__file__).resolve().parents[1]


class AllMRCommandTests(unittest.TestCase):
    def test_command_enumerates_all_mr_sources_and_writes_to_temp(self):
        source = (ROOT / 'tools/build_views.ps1').read_text(encoding='utf-8')
        self.assertIn('[switch]$AllMR', source)
        self.assertIn("-Filter 'MR-*.md'", source)
        self.assertIn('Sort-Object Name', source)
        self.assertIn("$CliArgs += @('--source', $Source.FullName)", source)
        self.assertIn('Join-Path $env:TEMP "DDTA-All-MR-$View"', source)
        self.assertIn('mr-functions-$View.rq', source)
        self.assertIn('if (-not $NoOpen)', source)

    def test_four_mr_structure_view_contains_mr04_and_record_composition(self):
        sources = sorted((ROOT / 'dermatriage/mr').glob('MR-*.md'))
        self.assertEqual([p.name for p in sources], ['MR-01.md', 'MR-02.md', 'MR-03.md', 'MR-04.md'])
        content = render(sources, ROOT / 'tools/visualization.yaml',
                         ROOT / 'dermatriage/views/mr-functions-structure.rq')
        self.assertIn('ControlledAdaptation<br/>Function', content)
        self.assertIn('AccumulatedClinicalReviewRecords · Information', content)
        self.assertIn('ClinicalReviewRecord · Information', content)
        self.assertIn('AdaptationCandidate<br/>Artifact', content)
        self.assertIn('AdaptationQualificationResult<br/>Information', content)
        self.assertEqual(content.count('ClinicalReviewRecord · Information'), 1)


if __name__ == '__main__':
    unittest.main()
