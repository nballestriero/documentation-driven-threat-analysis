"""MR-01 + MR-02 are one shared-identity graph, not independent pictures."""
import hashlib
import unittest
from pathlib import Path

from rdflib import RDF, URIRef
from tools.rdf_mermaid.render import read_many_rdf, render, mermaid_id, main, apply_sparql_view, load_config, project

ROOT = Path(__file__).resolve().parents[1]
MR1 = ROOT / 'dermatriage/mr/MR-01.md'
MR2 = ROOT / 'dermatriage/mr/MR-02.md'
CONF = ROOT / 'tools/visualization.yaml'
VIEWS = ROOT / 'dermatriage/views'
OUT = ROOT / 'dermatriage/diagrams'
DERMA = 'https://example.org/ddta/dermatriage#'
CORE = 'https://w3id.org/ddta/core#'

class AggregationTests(unittest.TestCase):
    def test_shared_iri_is_single_resource(self):
        graph = read_many_rdf([MR1, MR2])
        outcome = URIRef(DERMA+'TriageOutcome')
        f1 = URIRef(DERMA+'DermatologicalTriageEvaluation')
        f2 = URIRef(DERMA+'SpecialistDestinationDetermination')
        self.assertIn((f1,URIRef(CORE+'hasOutput'),outcome), graph)
        self.assertIn((f2,URIRef(CORE+'hasInput'),outcome), graph)
        self.assertEqual(len(list(graph.triples((outcome,RDF.type,None)))),1)

    def test_union_is_order_independent(self):
        a = read_many_rdf([MR1, MR2])
        b = read_many_rdf([MR2, MR1])
        self.assertEqual(set(a),set(b))
        for view in ('overview','structure'):
            path = VIEWS/('mr-aggregate-'+view+'.rq')
            self.assertEqual(render([MR1,MR2],CONF,path),render([MR2,MR1],CONF,path))

    def test_composed_arrows_and_no_duplicate_outcome(self):
        text = render([MR1, MR2], CONF, VIEWS/'mr-aggregate-overview.rq')
        outcome = mermaid_id(URIRef(DERMA+'TriageOutcome'))
        self.assertEqual(text.count('TriageOutcome<br/>Information'),1)
        f1 = mermaid_id(URIRef(DERMA+'DermatologicalTriageEvaluation'))
        f2 = mermaid_id(URIRef(DERMA+'SpecialistDestinationDetermination'))
        self.assertIn(f'{f1} --> {outcome}',text)
        self.assertIn(f'{outcome} --> {f2}',text)

    def test_detailed_graph_has_containment(self):
        text = render([MR1,MR2], CONF, VIEWS/'mr-aggregate-structure.rq')
        self.assertIn('CaseInformationContract', text)
        self.assertIn('minOccurs = 0', text)
        self.assertIn('subgraph', text)

    def test_saved_aggregate_graphs_current(self):
        for view in ('overview','structure'):
            args=[]
            for source in (MR1,MR2): args += ['--source',str(source)]
            args += ['--config',str(CONF),'--view',str(VIEWS/('mr-aggregate-'+view+'.rq')),
                     '--out',str(OUT/('MR-01-02-'+view)),'--check']
            self.assertEqual(main(args), 0)

    def test_sources_unchanged(self):
        files=(MR1,MR2,ROOT/'ontology/core.ttl')
        before={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
        render([MR1,MR2],CONF,VIEWS/'mr-aggregate-structure.rq')
        self.assertEqual(before,{str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in files})

if __name__=='__main__':
    unittest.main()
