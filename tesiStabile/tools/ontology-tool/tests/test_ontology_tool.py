"""Regression tests: portable source discovery, strict YAML validation, dynamic modules."""
from __future__ import annotations
import contextlib
import io
import shutil
import os
import tempfile
import unittest
from pathlib import Path
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS, OWL
from rdflib.compare import isomorphic

from ddta_ontology.cli import main, make_parser
from ddta_ontology.config import load_config_file
from ddta_ontology.errors import OntologySourceError
from ddta_ontology.source import discover_sources
from ddta_ontology.workflow import validate_sources, generate_turtle, check_outputs, write_outputs

ROOT = Path(__file__).resolve().parents[1]
DOCS = Path(os.environ['DDTA_TEST_DOCS']) if os.environ.get('DDTA_TEST_DOCS') else None
SAMPLE = ROOT / 'tests' / 'fixtures' / 'NETWORK_SAMPLE.md'


def write_example(directory: Path, source: Path = SAMPLE) -> Path:
    """Copy the included test fixture into an arbitrary ontology directory."""
    directory.mkdir(parents=True, exist_ok=True)
    dest = directory / 'network.md'
    shutil.copyfile(source, dest)
    return dest


class GenericOntologyTests(unittest.TestCase):
    def test_help_without_sources(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            with self.assertRaises(SystemExit) as e:
                main(['--help'])
        self.assertEqual(e.exception.code, 0)
        self.assertIn('--source-dir', out.getvalue())
        self.assertNotIn('--repo-root', out.getvalue())

    def test_source_selection_is_explicit(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main([]), 1)

    def test_extension_requires_no_python_changes(self):
        with tempfile.TemporaryDirectory() as temp:
            path = write_example(Path(temp) / 'other' / 'nested')
            # The test only declares its namespace inside the Markdown.
            self.assertEqual(discover_sources([], [Path(temp)]), [path])
            result = validate_sources([path])
            self.assertEqual(result.modules, ('network',))
            self.assertEqual(result.counts['class'], 1)
            ttl = generate_turtle(result).turtle['network']
            g = Graph().parse(data=ttl, format='turtle')
            self.assertIn((URIRef('https://example.org/ddta/network#Router'), RDF.type, OWL.Class), g)
            self.assertIn('# Class: network:Router', ttl)

    def test_multi_file_same_module(self):
        with tempfile.TemporaryDirectory() as temp:
            dir = Path(temp)
            path1 = write_example(dir)
            content = path1.read_text(encoding='utf-8')
            start = content.index('```yaml ddta-ontology\nrecord: object-properties')
            (dir / 'properties.md').write_text(content[start:], encoding='utf-8')
            path1.write_text(content[:start], encoding='utf-8')
            result = validate_sources(discover_sources([], [dir]))
            self.assertEqual(result.modules, ('network',))
            self.assertEqual(result.counts['class'], 1)
            self.assertEqual(result.counts['object-property'], 1)
            ttl = generate_turtle(result).turtle['network']
            self.assertIn('network:connectsTo', ttl)

    def test_file_name_unrelated_to_module_name(self):
        with tempfile.TemporaryDirectory() as temp:
            source = write_example(Path(temp))
            target = source.rename(Path(temp) / 'whatever.md')
            res = validate_sources([target])
            self.assertEqual(res.modules, ('network',))

    def test_missing_namespace_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            src = write_example(Path(temp))
            s = src.read_text(encoding='utf-8')
            src.write_text(s[s.index('```yaml ddta-ontology'):], encoding='utf-8')
            with self.assertRaisesRegex(OntologySourceError, 'no namespace definition'):
                validate_sources([src])

    def test_unresolved_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            src = write_example(Path(temp))
            s = src.read_text(encoding='utf-8').replace('range: network:Router', 'range: network:Unknown')
            src.write_text(s, encoding='utf-8')
            with self.assertRaisesRegex(OntologySourceError, 'unresolved'):
                validate_sources([src])

    def test_duplicates_in_yaml_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            src = write_example(Path(temp))
            s = src.read_text(encoding='utf-8').replace('record: class', 'record: class\nrecord: class', 1)
            src.write_text(s, encoding='utf-8')
            with self.assertRaisesRegex(OntologySourceError, 'Duplicate YAML key'):
                validate_sources([src])

    def test_duplicate_iris_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            src = write_example(Path(temp))
            s = src.read_text(encoding='utf-8').replace('network:connectsTo', 'network:Router')
            src.write_text(s, encoding='utf-8')
            with self.assertRaisesRegex(OntologySourceError, 'duplicate IRI'):
                validate_sources([src])

    def test_status_nonapproved_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            src = write_example(Path(temp))
            s = src.read_text(encoding='utf-8').replace('status: approved', 'status: proposed', 1)
            src.write_text(s, encoding='utf-8')
            with self.assertRaisesRegex(OntologySourceError, 'expected approved'):
                validate_sources([src])

    def test_validation_does_not_write(self):
        with tempfile.TemporaryDirectory() as temp:
            path = write_example(Path(temp) / 'docs')
            out = Path(temp) / 'out'
            self.assertEqual(main(['--source', str(path)]), 0)
            self.assertFalse(out.exists())

    def test_cli_generation_and_check(self):
        with tempfile.TemporaryDirectory() as temp:
            path = write_example(Path(temp) / 'docs')
            out = Path(temp) / 'out'
            args = ['--source-dir', str(path.parent), '--output-dir', str(out)]
            self.assertEqual(main(args + ['--generate']), 0)
            self.assertEqual([p.name for p in out.glob('*.ttl')], ['network.ttl'])
            self.assertEqual(main(args + ['--check']), 0)
            (out / 'network.ttl').write_text('corrupt', encoding='utf-8')
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(args + ['--check']), 1)
            self.assertEqual((out / 'network.ttl').read_text(), 'corrupt')

    def test_requires_explicit_generate_flag(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as exc:
                main(['--output-dir', 'arbitrary'])
        self.assertEqual(exc.exception.code, 2)

    def test_refuse_write_in_source_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            path = write_example(Path(temp))
            valid = validate_sources([path])
            generated = generate_turtle(valid)
            with self.assertRaisesRegex(OntologySourceError, 'Refusing'):
                write_outputs(generated, path.parent, [path])

    def test_config_from_file(self):
        with tempfile.TemporaryDirectory() as temp:
            path = write_example(Path(temp))
            original = path.read_text(encoding='utf-8')
            path.write_text(original[original.index('```yaml ddta-ontology'):], encoding='utf-8')
            config = Path(temp) / 'config.yaml'
            config.write_text('modules:\n  network:\n    prefix: network\n    namespace: https://example.org/ddta/network#\n')
            result = validate_sources([path], load_config_file(config))
            self.assertEqual(result.modules, ('network',))

    def test_config_conflict_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = write_example(Path(temp))
            config = Path(temp) / 'config.yaml'
            config.write_text('modules:\n  network:\n    prefix: network\n    namespace: https://example.org/different#\n')
            with self.assertRaisesRegex(OntologySourceError, 'Conflicting'):
                validate_sources([path], load_config_file(config))

    def test_four_modules_with_cross_references(self):
        """Add a fourth ontology without registering it in a Python file."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            def minimal(module: str, prefix: str, name: str, iri: str) -> None:
                content = f"""```yaml ddta-namespace
module: {module}
prefix: {prefix}
namespace: {iri}
```
```yaml ddta-ontology
record: class
module: {module}
iri: {prefix}:{name}
status: approved
label:
  en: {name}
  it: {name}
definition:
  en: Example class in module {module}.
  it: Classe di esempio nel modulo {module}.
```
"""
                folder = root / module
                folder.mkdir()
                (folder / 'spec.MD').write_text(content, encoding='utf-8')
            minimal('core', 'ddta', 'Resource', 'https://example.org/core#')
            minimal('process', 'process', 'Process', 'https://example.org/process#')
            minimal('security', 'security', 'SecurityProperty', 'https://example.org/security#')
            path = write_example(root / 'network')
            content = path.read_text(encoding='utf-8')
            path.write_text(content.replace('status: approved\nlabel:',
                                            'status: approved\nsubClassOf: ddta:Resource\nlabel:', 1)
                            .replace('range: network:Router', 'range: ddta:Resource'),
                            encoding='utf-8')
            paths = discover_sources([], [root])
            self.assertEqual(len(paths), 4)
            validated = validate_sources(paths)
            self.assertEqual(validated.modules, ('core', 'network', 'process', 'security'))
            ttl = generate_turtle(validated).turtle
            self.assertEqual(set(ttl), {'core', 'process', 'security', 'network'})
            g = Graph().parse(data=ttl['network'], format='turtle')
            self.assertIn((URIRef('https://example.org/ddta/network#Router'),
                           RDFS.subClassOf, URIRef('https://example.org/core#Resource')), g)

    def test_non_ontology_markdown_ignored(self):
        with tempfile.TemporaryDirectory() as temp:
            path = write_example(Path(temp))
            (Path(temp) / 'readme.md').write_text('# Not an ontology\n')
            self.assertEqual(discover_sources([], [Path(temp)]), [path])

    def test_rdf_determinism(self):
        with tempfile.TemporaryDirectory() as temp:
            path = write_example(Path(temp))
            val = validate_sources([path])
            a = generate_turtle(val)
            b = generate_turtle(val)
            self.assertEqual(a.turtle, b.turtle)

    @unittest.skipUnless(DOCS is not None and DOCS.exists(), 'optional reference ontology Markdown unavailable')
    def test_reference_ontologies(self):
        files = discover_sources([], [DOCS])
        result = validate_sources(files, load_config_file(ROOT / 'ontology-tool.yaml'))
        self.assertEqual(result.modules, ('core', 'process', 'security'))
        self.assertEqual(result.counts, {'class': 31, 'datatype-property':26,
                                         'individual':12, 'object-property':53})
        output = generate_turtle(result)
        for module, ttl in output.turtle.items():
            g = Graph().parse(data=ttl, format='turtle')
            self.assertIn((URIRef(result.config.spec(module).ontology_iri), RDF.type, OWL.Ontology), g)


if __name__ == '__main__':
    unittest.main()
