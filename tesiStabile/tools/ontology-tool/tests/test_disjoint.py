import tempfile
import unittest
from pathlib import Path
from rdflib import Graph, URIRef
from rdflib.namespace import OWL
from ddta_ontology.workflow import validate_sources, generate_turtle
from ddta_ontology.errors import OntologySourceError

class DisjointTests(unittest.TestCase):
    def run_case(self, target):
        sample = (Path(__file__).parent / 'fixtures/NETWORK_SAMPLE.md').read_text(encoding='utf-8')
        cls = sample[sample.index('```yaml ddta-ontology'):sample.index('```yaml ddta-ontology\nrecord: object-properties')]
        second = cls.replace('network:Router', 'network:Switch')
        sample = sample.replace('iri: network:Router\n', 'iri: network:Router\ndisjointWith: ' + target + '\n', 1) + '\n' + second
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/'test.md'; p.write_text(sample, encoding='utf-8')
            result = validate_sources([p])
            a = generate_turtle(result).turtle['network']
            self.assertEqual(a, generate_turtle(result).turtle['network'])
            return Graph().parse(data=a, format='turtle')
    def test_valid(self):
        g = self.run_case('network:Switch')
        self.assertIn((URIRef('https://example.org/ddta/network#Router'), OWL.disjointWith, URIRef('https://example.org/ddta/network#Switch')), g)
    def test_invalid(self):
        for target in ('network:Missing', 'network:connectsTo', 'network:Router', '[network:Switch]', 'other:Switch'):
            with self.subTest(target=target), self.assertRaises(OntologySourceError):
                self.run_case(target)
