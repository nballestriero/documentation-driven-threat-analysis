import importlib.util, pathlib, tempfile, unittest
p=pathlib.Path(__file__).parent/'ont_ollama.py'
spec=importlib.util.spec_from_file_location('ont_ollama',p)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
SOURCE='Una piattaforma permette ai clienti di acquistare prodotti.'
class TestOntology(unittest.TestCase):
    def test_rotation(self):
        names=['a','b']; rounds=m.rotation(names,1)
        self.assertEqual(rounds,[{'cycle':1,'target':'a','partner':'b'},
                                 {'cycle':1,'target':'b','partner':'a'}])
        with self.assertRaises(ValueError):m.rotation(names,2)
    def test_valid(self):
        doc={'testId':'ONT-T01','objects':[{'id':'O-001','name':'Piattaforma','candidateCategory':'sistema','evidence':'Una piattaforma','uncertainty':None}], 'relations':[],'actions':[], 'ambiguities':[]}
        self.assertEqual(m.validate(doc,SOURCE,'ONT-T01'),[])
        doc['actions']=[{'id':'A-001','verb':'permette','actorId':'O-999','participants':[],'resultIds':[],'condition':None,'evidence':'permette ai clienti','uncertainty':None}]
        self.assertTrue(any('unknown actor' in x for x in m.validate(doc,SOURCE,'ONT-T01')))
    def test_evidence(self):
        doc={'testId':'ONT-T01','objects':[{'id':'O-001','name':'Piattaforma','candidateCategory':'sistema','evidence':'inventato','uncertainty':None}], 'relations':[],'actions':[], 'ambiguities':[]}
        self.assertTrue(any('literal' in x for x in m.validate(doc,SOURCE,'ONT-T01')))
if __name__=='__main__':unittest.main()
