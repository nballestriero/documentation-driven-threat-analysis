from pathlib import Path
import sys
import unittest
from rdflib import Graph, Namespace, RDF, RDFS, Literal
from rdflib.namespace import XSD
from verify_and_render_r5 import D, V, check, elem, contracts, contract_detail

HERE=Path(__file__).resolve().parent
DH=Namespace('https://example.org/ddta/dh-deterministic-r4#')
P=Namespace('https://w3id.org/ddta/process#')

class ContractTests(unittest.TestCase):
    def setUp(self):
        self.g=Graph().parse(HERE/'dh_r5.ttl',format='turtle')
    def altered(self):
        g=Graph()
        for x in self.g:g.add(x)
        return g
    def test_all_functions_complete(self):
        errors,funs,conts,ex=check(self.g)
        self.assertEqual(errors,[])
        self.assertEqual(len(funs),15)
        self.assertEqual(len(conts),28)
        self.assertEqual(len(ex),2)
    def test_preserves_non_contract_model(self):
        original=Graph().parse(HERE/'dh_r4_baseline.ttl',format='turtle')
        c0=set(original.subjects(RDF.type,D.Contract))
        c1=set(self.g.subjects(RDF.type,D.Contract))
        e0=set(original.subjects(RDF.type,D.ContractElement))
        e1=set(self.g.subjects(RDF.type,D.ContractElement))
        # Ignore only the contract layer; all Process, Function, System,
        # Environment, Boundary and Channel triples must be preserved.
        def keep(g):
            return {(s,p,o) for s,p,o in g if p not in (D.hasInputContract,D.hasOutputContract)
                    and s not in (c0|c1|e0|e1)}
        self.assertEqual(keep(original),keep(self.g))
    def test_all_contracts_queryable_sparql(self):
        query='''PREFIX ddta:<https://w3id.org/ddta/core#>
             SELECT ?f ?e WHERE { ?f ddta:hasInputContract ?c . ?c ddta:hasContractElement ?e . }'''
        rows=list(self.g.query(query))
        self.assertGreater(len(rows),40)
        self.assertIn((DH.PCDeriveSecret,DH.ModulusP),rows)
        self.assertIn((DH.PCDeriveSecret,DH.AcceptedBRequired),rows)
        self.assertIn((DH.PCGeneratePrivate,DH.EntropyPC),rows)
    def test_received_raw_vs_validated_separate(self):
        self.assertNotEqual(DH.ReceivedB,DH.AcceptedBRequired)
        self.assertIn(DH.ReceivedB,elem(self.g,contracts(self.g,DH.PCValidatePublic,'input')[0]))
        self.assertIn(DH.AcceptedBOptional,elem(self.g,contracts(self.g,DH.PCValidatePublic,'output')[0]))
        self.assertIn(DH.AcceptedBRequired,elem(self.g,contracts(self.g,DH.PCDeriveSecret,'input')[0]))
        self.assertEqual(int(next(self.g.objects(DH.AcceptedBOptional,D.minOccurs))),0)
        self.assertEqual(int(next(self.g.objects(DH.AcceptedBRequired,D.minOccurs))),1)
    def test_missing_contract_is_rejected(self):
        g=self.altered()
        for c in list(g.objects(DH.PCCalculatePublic,D.hasInputContract)):
            g.remove((DH.PCCalculatePublic,D.hasInputContract,c))
        self.assertTrue(any('PCCalculatePublic' in e for e in check(g)[0]))
    def test_private_value_on_channel_rejected(self):
        g=self.altered();g.add((DH.PublicAOverChannel,D.hasContractElement,DH.PrivateA))
        self.assertTrue(any('SECURITY' in e for e in check(g)[0]))
    def test_invalid_cardinality_rejected(self):
        g=self.altered();g.remove((DH.AcceptedAOptional,D.minOccurs,None))
        g.add((DH.AcceptedAOptional,D.minOccurs,Literal(2,datatype=XSD.nonNegativeInteger)))
        self.assertTrue(any('AcceptedAOptional' in e for e in check(g)[0]))
    def test_contract_channel_mismatch_rejected(self):
        g=self.altered()
        g.remove((DH.UserReceivePublic,D.usesChannel,DH.PCToUserChannel))
        g.add((DH.UserReceivePublic,D.usesChannel,DH.UserToPCChannel))
        self.assertTrue(any('channel mismatch' in e for e in check(g)[0]))
    def test_ambiguous_receiver_rejected(self):
        g=self.altered()
        g.add((DH.PCReceivePublic,D.hasInputContract,DH.PublicAOverChannel))
        self.assertTrue(any('ambiguous receiver' in e for e in check(g)[0]))
    def test_output_changes_when_only_rdf_changes(self):
        old=contract_detail(self.g,DH.PCCalculatePublic)
        g=self.altered()
        new=DH.ExperimentalExtraElement
        g.add((new,RDF.type,D.ContractElement))
        g.add((new,RDFS.label,Literal('Extra test field')))
        c=contracts(g,DH.PCCalculatePublic,'output')[0]
        g.add((c,D.hasContractElement,new))
        modified=contract_detail(g,DH.PCCalculatePublic)
        self.assertNotEqual(old,modified)
        self.assertIn('Extra test field',modified)

if __name__=='__main__':unittest.main(verbosity=2)
