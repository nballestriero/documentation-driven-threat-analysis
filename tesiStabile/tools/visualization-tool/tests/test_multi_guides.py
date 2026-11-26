"""Una sola pipeline può leggere regole e individui di due moduli distinti."""
from pathlib import Path
import sys, tempfile, unittest, json
from rdflib import Graph, URIRef, RDF

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from ddta_viz.pipeline import main
from ddta_viz.catalog import Catalog

class MultiGuideTests(unittest.TestCase):
    def test_core_and_extension_are_combined(self):
        guide = ROOT.parents[1] / "ontologies/core/DDTA_CORE_VISUALIZATION.md"
        extguide = ROOT / "examples/extension/DEMO_VISUALIZATION.md"
        ttl = ROOT / "tests/fixtures/credential_exchange.ttl"
        extttl = ROOT / "examples/extension/demo.ttl"
        self.assertTrue(guide.is_file(), "La guida CORE deve essere nella cartella ontologies/core del repository")
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            code = main(["--guides-md",str(guide),str(extguide),"--ttl",str(ttl),str(extttl),"--strict","--out-dir",str(output)])
            self.assertEqual(code,0)
            report = json.loads((output / '06_diagnostics.json').read_text(encoding='utf-8'))
            self.assertEqual(report['regole'], 33)
            self.assertEqual(report['triple'], 96)
            self.assertEqual(len([d for d in report['diagnostici'] if d['severity']=='warning']),0)
            diagram = (output / '05_graph.mmd').read_text(encoding='utf-8')
            self.assertIn('demo:Processor', diagram)
            self.assertIn('ddta:Function', diagram)
