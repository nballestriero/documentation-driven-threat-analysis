"""Reject removed PROCESS RDF vocabulary without changing legitimate Step arcs.

The approved PROCESS ontology contains no nominal ProcessTransition,
CompositeCondition, separate SynchronizationNode or activation-condition relation.
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

from rdflib import Graph, Namespace, RDF

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
from ddta_process import project
from ddta_process_pipeline import trace_projection

CORE = ROOT / 'tests/fixtures/process/examples/00_PLATE_GATE_CORE_BASELINE.ttl'
PROCESS = ROOT / 'tests/fixtures/process/examples/PLATE_GATE_PROCESS_TEST.ttl'
GUIDE = ROOT.parents[1] / 'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'
PR = Namespace('https://w3id.org/ddta/process#')
EX = Namespace('https://example.org/ddta/process-vocabulary-rejection#')

OBSOLETE_CLASSES = ('ProcessTransition', 'CompositeCondition', 'Condition', 'SynchronizationNode')
OBSOLETE_PROPERTIES = ('hasTransition', 'fromStep', 'toStep', 'hasGuard',
                       'hasCondition', 'logicalOperator', 'hasActivationCondition')

class ProcessVocabularyRejectionTests(unittest.TestCase):
    def modified(self, alter):
        graph = Graph().parse(str(PROCESS), format='turtle')
        alter(graph)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'candidate.ttl'
            graph.serialize(destination=path, format='turtle')
            return project(CORE, path, GUIDE)

    def test_removed_class_names_fail_closed(self):
        for name in OBSOLETE_CLASSES:
            with self.subTest(class_name=name):
                with self.assertRaisesRegex(ValueError, 'Vocabolario PROCESS obsoleto:.*process:' + name):
                    self.modified(lambda g, n=name: g.add((EX.Detached, RDF.type, PR[n])))

    def test_removed_property_names_fail_closed(self):
        for name in OBSOLETE_PROPERTIES:
            with self.subTest(property_name=name):
                with self.assertRaisesRegex(ValueError, 'Vocabolario PROCESS obsoleto:.*process:' + name):
                    self.modified(lambda g, n=name: g.add((EX.Detached, PR[n], EX.Other)))

    def test_legacy_iris_in_subject_or_object_cannot_be_ignored(self):
        for use in ('subject', 'object'):
            with self.subTest(use=use):
                def alter(graph):
                    graph.add((PR.ProcessTransition, RDF.type, EX.Retired)) if use=='subject' else graph.add((EX.Unknown, EX.mentions, PR.ProcessTransition))
                with self.assertRaisesRegex(ValueError,'Vocabolario PROCESS obsoleto:.*process:ProcessTransition'):
                    self.modified(alter)

    def test_current_direct_arcs_preserve_trace_provenance(self):
        ir = project(CORE, PROCESS, GUIDE)
        self.assertTrue(ir['transitions'])
        self.assertFalse(any(t['iri'] for t in ir['transitions']))
        self.assertTrue(all(t['sourceRelation'] in
            ('ddta:hasNextStep', 'hasTrueNextStep', 'hasFalseNextStep') for t in ir['transitions']))
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'project.json'
            trace = Path(temp) / 'trace.json'
            source.write_text(json.dumps(ir), encoding='utf-8')
            trace_projection(source, trace)
            result = json.loads(trace.read_text('utf-8'))
        self.assertEqual(len(result['transitions']), len(ir['transitions']))
        self.assertTrue(all(t['transitionIRI'] is None for t in result['transitions']))
        self.assertTrue(all(t['sourceRelation'] != 'process:ProcessTransition' for t in result['transitions']))

    def test_condition_requires_approved_atomic_class(self):
        graph = Graph().parse(str(PROCESS), format='turtle')
        targets = list(graph.objects(None, PR.evaluatesCondition))
        self.assertTrue(targets)
        target = targets[0]
        graph.remove((target, RDF.type, PR.AtomicCondition))
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'condition_untyped.ttl'
            graph.serialize(destination=path,format='turtle')
            with self.assertRaisesRegex(ValueError,'richiede process:AtomicCondition'):
                project(CORE, path, GUIDE)

if __name__ == '__main__':
    unittest.main()
