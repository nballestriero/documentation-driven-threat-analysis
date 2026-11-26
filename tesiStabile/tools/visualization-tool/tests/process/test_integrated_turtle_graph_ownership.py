"""Regression for a single integrated CORE+PROCESS Turtle visual partition.

The source RDF must be unchanged. Only redundant graphical ownership is
separated before CORE and PROCESS renderers are composed.
"""
from __future__ import annotations
import hashlib
import re
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from rdflib import Graph, RDF, Namespace

TOOL=Path(__file__).resolve().parents[2]
REPO=TOOL.parents[1]
sys.path.insert(0,str(TOOL/'src'))
from ddta_integrated_projection import build_core_visual_projection

CORE=Namespace('https://w3id.org/ddta/core#')
PROCESS=Namespace('https://w3id.org/ddta/process#')
EX=Namespace('https://example.org/ddta/plate-gate#')
DOC=REPO/'examples/plate-gate/DDTA_TARGA_COSTRUZIONE_PROGRESSIVA.md'


def step_turtle(number):
    md=DOC.read_text(encoding='utf-8')
    heading={13:'### 13.2',14:'### 14.3'}[number]
    beginning=md.index(heading)
    return re.search(r'```turtle\s*\n(.*?)\n```',md[beginning:],re.S).group(1)+'\n'


class IntegratedTurtleVisualOwnershipTest(unittest.TestCase):
    def test_source_unchanged_and_process_members_are_not_duplicated(self):
        for step in (13,14):
            with self.subTest(step=step), TemporaryDirectory() as temp:
                source=Path(temp)/'full.ttl';core=Path(temp)/'view.ttl'
                source.write_text(step_turtle(step),encoding='utf-8')
                before=hashlib.sha256(source.read_bytes()).hexdigest()
                report=build_core_visual_projection(source,core)
                actual=Graph().parse(str(core),format='turtle')
                self.assertEqual(before,hashlib.sha256(source.read_bytes()).hexdigest())
                self.assertLess(len(actual),report['sourceTriples'])
                self.assertIn((EX.RecognizePlateNumberProcess,RDF.type,CORE.Process),actual)
                self.assertNotIn((EX.OCR_CNN_AttentionLSTMStep,RDF.type,CORE.ProcessStep),actual)
                self.assertNotIn((EX.CNN_OCRResultContract,RDF.type,CORE.Contract),actual)
                self.assertNotIn((EX.Transformer_OCRResultContract,RDF.type,CORE.Contract),actual)
                self.assertNotIn((EX.CNN_AttentionLSTM_OCR,RDF.type,CORE.Resource),actual)
                self.assertNotIn((EX.MobileNetV3_Transformer_OCR,RDF.type,CORE.Resource),actual)
                self.assertIn((EX.PlateRecognitionSystem,CORE.hasPrimaryFunction,EX.RecognizePlateNumber),actual)
                self.assertIn((EX.PlateRecognitionSystem,CORE.hasSupportFunction,EX.SendPlateNumber),actual)
                self.assertIn((EX.ProcessingToHumanReviewChannel,RDF.type,CORE.CommunicationChannel),actual)
                if step>=14:
                    self.assertIn((EX.PlateRecognitionSystem,CORE.hasSupportFunction,EX.AutomaticOCRRetraining),actual)
                    self.assertIn((EX.ProcessingEnvironment,CORE.makesAvailable,EX.OCRRetrainingConfigurationRuntime),actual)
                other=Path(temp)/'again.ttl'
                build_core_visual_projection(source,other)
                self.assertEqual(core.read_bytes(),other.read_bytes())

    def test_shared_resource_and_contract_keep_core_occurrence(self):
        # An implementation resource can also be a legitimate CORE resource.
        with TemporaryDirectory() as temp:
            src=Path(temp)/'test.ttl';dst=Path(temp)/'core.ttl'
            src.write_text('''@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix process: <https://w3id.org/ddta/process#> .
@prefix ex: <https://example.org/ddta/plate-gate#> .
ex:S a ddta:System ; ddta:hasPrimaryFunction ex:F .
ex:F a ddta:Function ; ddta:hasOutputContract ex:C .
ex:C a ddta:Contract ; ddta:hasContractElement ex:E .
ex:E a ddta:ContractElement .
ex:P a ddta:Process ; ddta:realizesFunction ex:F ; ddta:hasStep ex:Step .
ex:Step a ddta:ProcessStep ; process:declaresOutputContract ex:C ; process:implementedBy ex:R .
ex:R a ddta:Resource .
ex:Env a ddta:Environment ; ddta:makesAvailable ex:R .
''',encoding='utf-8')
            build_core_visual_projection(src,dst)
            g=Graph().parse(str(dst),format='turtle')
            self.assertIn((EX.F,CORE.hasOutputContract,EX.C),g)
            self.assertIn((EX.C,CORE.hasContractElement,EX.E),g)
            self.assertIn((EX.Env,CORE.makesAvailable,EX.R),g)
            self.assertNotIn((EX.Step,RDF.type,CORE.ProcessStep),g)


if __name__=='__main__':unittest.main()
