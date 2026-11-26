"""Regression for R4.5 deterministic orchestrator and RDF ordering."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from rdflib import Graph, Namespace, RDF, Literal

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from ddta_process import project,ProcessRenderer,deterministic_label
from ddta_process_pipeline import sha

CORE=ROOT/'tests/fixtures/process/examples/00_PLATE_GATE_CORE_BASELINE.ttl'
PROCESS=ROOT/'tests/fixtures/process/examples/01_RECOGNIZE_PLATE_PROCESS.ttl'
GUIDE=ROOT/'tests/fixtures/process/legacy/DDTA_PROCESS_VISUALIZATION_R79.md'
COREGUIDE=ROOT.parents[1]/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
BASE=ROOT/'tests/fixtures/process/examples/CORE_BASE_GRAFO_SCELTO.mmd'
ENTRY=ROOT/'src/ddta_process_pipeline.py'


def args(out, *,core_mermaid=BASE, process_ttl=PROCESS, core_generator=None):
    cmd=[sys.executable,str(ENTRY),'--core-ttl',str(CORE),
         '--core-guide',str(COREGUIDE),'--process-ttl',str(process_ttl),
         '--process-guide',str(GUIDE),'--out-dir',str(out)]
    if core_generator:
        cmd+=['--core-generator',str(core_generator)]
    else:
        cmd+=['--core-mermaid',str(core_mermaid)]
    return cmd

class TestDeterministicPipelineR45(unittest.TestCase):
    def test_two_independent_generations_and_provenance(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out'
            run=subprocess.run(args(out),capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            m=json.loads((out/'manifest.json').read_text('utf-8'))
            self.assertEqual(m['independentRuns'],2)
            self.assertTrue(m['deterministicByteForByte'])
            self.assertTrue(m['coreOnlyByteForByte'])
            self.assertEqual(sha(out/'core_only/05_graph.mmd'),sha(BASE))
            for rel,digest in m['outputSha256'].items():
                self.assertEqual(sha(out/rel),digest,rel)
            self.assertIn('core_process_extended/05_graph.md',m['outputSha256'])
            trace=json.loads((out/'core_process_extended/07_rdf_trace.json').read_text('utf-8'))
            names={p['operandIRI'].rsplit('#',1)[-1]:p['contractElementIRI'].rsplit('#',1)[-1]
                   for p in trace['operandReferences']}
            self.assertEqual(names,{'ExtractedPlateOperand':'ExtractedPlateNumber',
                                    'VerifiedPlateOperand':'VerifiedPlateNumber'})
            self.assertTrue(all(not p['isDataTransfer'] for p in trace['operandReferences']))

    def test_rdf_turtle_statement_order_does_not_affect_mermaid(self):
        ir=project(CORE,PROCESS,GUIDE)
        original,original_diag=ProcessRenderer(ir,GUIDE,COREGUIDE,'extended').render()
        with tempfile.TemporaryDirectory() as tmp:
            nt=Graph().parse(str(PROCESS),format='turtle').serialize(format='nt').splitlines()
            altered=Path(tmp)/'permuted.ttl'
            altered.write_text('\n'.join(reversed(sorted(nt)))+'\n',encoding='utf-8')
            ir2=project(CORE,altered,GUIDE)
            second,second_diag=ProcessRenderer(ir2,GUIDE,COREGUIDE,'extended').render()
            self.assertEqual(ir,ir2)
            self.assertEqual(original,second)
            self.assertEqual(original_diag,second_diag)

    def test_live_generator_is_invoked(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp)
            fake=d/'fake_core.py'
            fake.write_text(
                'import argparse\nfrom pathlib import Path\n'
                'p=argparse.ArgumentParser();p.add_argument("--guides-md");p.add_argument("--ttl");p.add_argument("--out-dir");a=p.parse_args()\n'
                f'base=Path({str(BASE)!r})\n'
                'out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)\n'
                '(out/"05_graph.mmd").write_bytes(base.read_bytes())\n'
                '(out/"05_graph.md").write_bytes(b"```mermaid\\n"+base.read_bytes()+b"```\\n")\n',
                encoding='utf-8')
            out=d/'generated'
            run=subprocess.run(args(out,core_generator=fake),capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            self.assertEqual(json.loads((out/'manifest.json').read_text())['coreMode'],'live')

    def test_missing_core_generator_fails_not_fallback(self):
        with tempfile.TemporaryDirectory() as tmp:
            run=subprocess.run(args(Path(tmp)/'generated',core_generator=Path(tmp)/'not_found.py'),
                               capture_output=True,text=True)
            self.assertNotEqual(run.returncode,0)
            self.assertIn('core_generator',run.stderr)
            self.assertFalse((Path(tmp)/'generated/manifest.json').exists())

    def test_conflicting_labels_are_error_not_random_choice(self):
        g=Graph();subj=Namespace('https://example.test/#').Object
        g.add((subj,RDF.type,subj))
        from rdflib import RDFS
        g.add((subj,RDFS.label,Literal('A',lang='it')))
        g.add((subj,RDFS.label,Literal('B',lang='it')))
        with self.assertRaisesRegex(ValueError,'etichette RDF conflittuali'):
            deterministic_label(g,subj,'Object')

if __name__=='__main__':unittest.main()
