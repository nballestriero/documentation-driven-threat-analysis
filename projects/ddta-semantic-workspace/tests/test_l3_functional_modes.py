"""Regressions: canonical MR-01 FunctionalMode interfaces and focus rendering."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal, XSD
from tools.graph_pipeline.compose import PipelineError, canonical_turtle, extract_graph, validate
from tools.graph_pipeline.query import execute_chain
from tools.rdf_mermaid.render import load_config, mermaid_id, project
from tools.visualize import ROOT, PRESETS, process

HERE = ROOT / 'experiments' / 'graph-l3-functional-modes'
D = Namespace('https://example.org/ddta/dermatriage#')
DDTA = Namespace('https://w3id.org/ddta/core#')
V = Namespace('urn:ddta:view#')
RETIRED = (DDTA.modeHasInput, DDTA.guaranteesOutput, DDTA.requiresPresent, DDTA.requiresAbsent)
spec = importlib.util.spec_from_file_location('ddta_l3_focus_runner', HERE / 'run_experiment.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

class GraphL3FunctionalModesTest(unittest.TestCase):
    def setUp(self):
        self.g = extract_graph(ROOT / 'dermatriage/mr/MR-01.md')
        self.schema = extract_graph(ROOT / 'ontology/core.ttl')
        self.query = HERE / '01-l3-primary-mode-focus.rq'
        self.config = load_config(ROOT / 'tools/visualization.yaml')

    def test_core_has_no_retired_properties_or_domain_which_conflates_modes(self):
        for predicate in RETIRED:
            self.assertFalse(any(self.schema.triples((predicate, None, None))))
        for property_ in (DDTA.hasInput, DDTA.hasOutput):
            self.assertIn((property_, RDF.type, OWL.ObjectProperty), self.schema)
            self.assertNotIn((property_, RDFS.domain, DDTA.Function), self.schema)
        self.assertIn((DDTA.FunctionalMode, OWL.disjointWith, DDTA.Function), self.schema)

    def test_contract_property_renamed_without_semantic_loss(self):
        self.assertIn((DDTA.constrainsInformation, RDF.type, OWL.ObjectProperty), self.schema)
        self.assertFalse(any(self.schema.triples((DDTA.specifiesInformation, None, None))))
        self.assertIn((D.LesionImageElement, DDTA.constrainsInformation, D.LesionImage), self.g)
        self.assertIn((D.GeneralCaseInformationElement, DDTA.constrainsInformation, D.GeneralCaseInformation), self.g)
        bad = Graph() + self.g
        bad.add((D.LesionImageElement, DDTA.specifiesInformation, D.LesionImage))
        with self.assertRaisesRegex(PipelineError, 'RETIRED_CONTRACT_PREDICATE'):
            validate(bad, self.schema)

    def test_canonical_mr01_reuses_interface_properties(self):
        validate(self.g, self.schema)
        self.assertIn((D.DermatologicalTriageEvaluation, DDTA.hasMode, D.WithImageMode), self.g)
        self.assertIn((D.DermatologicalTriageEvaluation, DDTA.hasMode, D.WithoutImageMode), self.g)
        for mode in (D.WithImageMode, D.WithoutImageMode):
            self.assertIn((mode, RDF.type, DDTA.FunctionalMode), self.g)
            self.assertNotIn((mode, RDF.type, DDTA.Function), self.g)
            self.assertIn((mode, DDTA.hasInput, D.GeneralCaseInformation), self.g)
            self.assertIn((mode, DDTA.hasOutput, D.TriageOutcome), self.g)
        self.assertIn((D.WithImageMode, DDTA.hasInput, D.LesionImage), self.g)
        self.assertNotIn((D.WithoutImageMode, DDTA.hasInput, D.LesionImage), self.g)
        for retired in RETIRED:
            self.assertFalse(any(self.g.triples((None, retired, None))))
            self.assertFalse(any(self.g.triples((None, DDTA.gapPredicate, retired))))

    def test_no_inferred_absence_or_specific_output_guarantee(self):
        self.assertIn((D.LesionImageElement, DDTA.minOccurs, Literal(0, datatype=XSD.nonNegativeInteger)), self.g)
        self.assertIn((D.NoImagePriorityOutputGap, DDTA.gapPredicate, DDTA.hasOutput), self.g)
        self.assertNotIn((D.WithoutImageMode, DDTA.hasOutput, D.OperationalTriagePriority), self.g)
        self.assertIn((D.WithoutImageMode, DDTA.hasOutput, D.TriageOutcome), self.g)

    def test_owl_disjointness_and_deprecated_checks(self):
        altered = Graph() + self.g
        altered.add((D.WithImageMode, RDF.type, DDTA.Function))
        with self.assertRaisesRegex(PipelineError, 'DISJOINT_CLASS'):
            validate(altered, self.schema)
        altered2 = Graph() + self.g
        altered2.add((D.WithImageMode, DDTA.modeHasInput, D.LesionImage))
        with self.assertRaisesRegex(PipelineError, 'RETIRED_MODE_PREDICATE'):
            validate(altered2, self.schema)

    def test_cardinality_and_gap_constraints_still_validate(self):
        g = Graph() + self.g
        g.remove((D.LesionImageElement, DDTA.maxOccurs, None))
        g.add((D.LesionImageElement, DDTA.maxOccurs, Literal(0, datatype=XSD.nonNegativeInteger)))
        validate(g,self.schema)
        g2 = Graph() + self.g
        g2.remove((D.GeneralCaseInformationElement, DDTA.maxOccurs, None))
        g2.add((D.GeneralCaseInformationElement, DDTA.maxOccurs, Literal(0, datatype=XSD.nonNegativeInteger)))
        with self.assertRaisesRegex(PipelineError, 'CONTRACT_CARDINALITY_INVALID'):
            validate(g2,self.schema)
        g3=Graph()+self.g
        g3.remove((D.NoImagePriorityOutputGap,RDFS.label,None))
        with self.assertRaisesRegex(PipelineError,'DOCUMENTATION_GAP_LABEL_REQUIRED'):
            validate(g3,self.schema)
        g4=Graph()+self.g
        g4.add((D.WithoutImageMode, DDTA.hasOutput, D.OperationalTriagePriority))
        with self.assertRaisesRegex(PipelineError,'RELATION_GAP_ALREADY_ASSERTED'):
            validate(g4,self.schema)

    def test_focus_renders_contract_and_gap_with_canonical_MR(self):
        selected=execute_chain(self.g,[self.query])
        self.assertIn((D.WithImageMode,DDTA.hasInput,D.LesionImage),selected)
        self.assertIn((D.WithoutImageMode,DDTA.hasOutput,D.TriageOutcome),selected)
        self.assertEqual(int(next(iter(selected.objects(D.LesionImage,V.minOccurs)))),0)
        self.assertIn((D.NoImagePriorityOutputGap,DDTA.gapPredicate,DDTA.hasOutput),selected)
        mm=project(selected,self.config)
        self.assertIn('cardinality',mm) if 'cardinality' in mm else self.assertIn('optionalInformation',mm)
        self.assertIn('WithImageMode',mm)
        self.assertIn('WithoutImageMode',mm)
        self.assertEqual(mm.count('(("?"))'),2)
        self.assertNotIn('requiresPresent',mm)
        self.assertNotIn('requiresAbsent',mm)

    def test_focus_deterministic_regeneration(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/'l3'
            a,b,m=runner.generate([ROOT/'dermatriage/mr/MR-01.md'],out)
            aa,bb,mm=runner.generate([ROOT/'dermatriage/mr/MR-01.md'],out,check=True)
            self.assertEqual(canonical_turtle(a),canonical_turtle(aa))
            self.assertEqual(canonical_turtle(b),canonical_turtle(bb))
            self.assertEqual(m,mm)

    def test_general_l1_backward_compatibility(self):
        mrdir=ROOT/'dermatriage/mr'
        _,_,mmd=process([mrdir/'MR-01.md',mrdir/'MR-02.md'],PRESETS['l1'],ROOT/'tools/visualization.yaml',ROOT/'ontology/core.ttl')
        self.assertIn('informationLink',mmd)
        self.assertIn('hasPrimaryFunction',mmd)
        self.assertNotIn('WithImageMode',mmd)

if __name__=='__main__':
    unittest.main()
