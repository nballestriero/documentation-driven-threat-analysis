import sys, unittest, hashlib, tempfile, json, re
from pathlib import Path
from rdflib import Graph, URIRef, RDF
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from ddta_process import project,ProcessRenderer,compose,stable,count_mermaid_edges,PR

CORE=ROOT/'tests/fixtures/process/examples/00_PLATE_GATE_CORE_BASELINE.ttl'
PROCESS=ROOT/'tests/fixtures/process/examples/01_RECOGNIZE_PLATE_PROCESS.ttl'
GUIDE=ROOT/'tests/fixtures/process/legacy/DDTA_PROCESS_VISUALIZATION_R79.md'
BASE=ROOT/'tests/fixtures/process/examples/CORE_R10_1_FUNZIONI.mmd'
COREGUIDE=ROOT.parents[1]/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
EX='https://example.org/ddta/plate-gate#'


def in_subgraph(text, parent, child):
    lines=text.splitlines(); start=None; depth=0
    for i,line in enumerate(lines):
        if re.match(r'^\s*subgraph\s+'+re.escape(parent)+r'(?:\[|\s)',line):start=i;break
    if start is None:return False
    for line in lines[start:]:
        if re.match(r'^\s*subgraph\s+\w+',line):depth+=1
        elif line.strip()=='end':
            depth-=1
            if depth==0:return False
        if child in line:return True
    return False

class TestProcessPlugin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ir=project(CORE,PROCESS,GUIDE)
        cls.fragment,cls.diag=ProcessRenderer(cls.ir,GUIDE,COREGUIDE).render()
        cls.unified=compose(BASE,cls.fragment,cls.ir,cls.diag)
        cls.byname={n['name']:n for n in cls.ir['nodes'].values()}
    def test_process_and_core_immutable(self):
        self.assertEqual(self.ir['coreBaselineTripleCount'],23)
        self.assertTrue(set(Graph().parse(str(CORE),format='turtle')).issubset(set(Graph().parse(str(CORE),format='turtle'))|set(Graph().parse(str(PROCESS),format='turtle'))))
        self.assertIn(BASE.read_text('utf8').strip(),self.unified)
    def test_steps_and_transitions(self):
        pr=next(p for p in self.ir['processes'] if p['name']=='RecognizePlateNumberProcess')
        self.assertEqual(len(pr['steps']),13)
        self.assertEqual(len(pr['transitions']),13)
        self.assertEqual(len(self.ir['processes']),2)
    def test_concurrent_two_independent_ocr(self):
        src=EX+'ConcurrentOCRSplit';dest={t['to'] for t in self.ir['transitions'] if t['from']==src}
        self.assertEqual(dest,{EX+'ExtractPlateNumberStep',EX+'VerifyPlateNumberStep'})
        self.assertIn('2/2',self.fragment)
        self.assertIn('cct-s-v2-global-model',self.fragment)
        self.assertIn('latin_PP-OCRv5_mobile_rec',self.fragment)
        join=EX+'OCRReadingsJoin'
        self.assertTrue(in_subgraph(self.fragment,stable('control-region:'+src),stable(join)))
    def test_implemented_by_local_group(self):
        for label in ('ExtractPlateNumberStep','VerifyPlateNumberStep'):
            iri=EX+label
            group=stable('implementation-group:'+iri)
            self.assertTrue(in_subgraph(self.fragment,group,stable(iri)))
            self.assertIn(iri,self.diag['implementationGroups'])
        self.assertEqual(len([r for r in self.ir['references'] if r['predicate']=='implementedBy']),2)
    def test_below_ten_xor_retains_not_rdf_without_second_yellow_box(self):
        threshold=EX+'RetrainingThresholdXor'
        positive=EX+'AtLeastTenDiscordances'
        negative=EX+'BelowTenDiscordances'
        wrapper=stable('condition:'+threshold+':'+positive)
        region=stable('control-region:'+threshold)
        self.assertTrue(in_subgraph(self.fragment,region,wrapper))
        self.assertNotIn('subgraph '+stable('condition:'+threshold+':'+negative),self.fragment)
        self.assertEqual(self.ir['conditions'][negative]['operator'],'NOT')
        self.assertEqual(self.ir['conditions'][negative]['members'],[positive])
        self.assertIn(wrapper+' --> '+stable(EX+'EndDiscordance'),self.fragment)
        self.assertIn(wrapper+' --> '+stable(EX+'InvokeRetrainingStep'),self.fragment)
        self.assertIn('END_PROCESS',self.fragment)
    def test_conditions_only_declared_rdf(self):
        self.assertEqual(len(self.diag['conditionPlacements']),2)
        for entry in self.diag['conditionPlacements']:
            self.assertIn(entry['guard'],self.ir['conditions'])
            self.assertEqual(entry['guard'],next(x['visibleGuard'] for x in self.diag['xorConditionHeaders'] if x['control']==entry['control']))
        self.assertEqual({x['control'].split('#')[-1] for x in self.diag['xorConditionHeaders']},
            {'ModelAgreementXor','RetrainingThresholdXor'})
    def test_core_only_bitwise_identical(self):
        # Exercise the CLI, not merely a read_text() roundtrip of the baseline.
        # Test both LF and CRLF to catch platform-dependent newline conversion.
        import subprocess
        base=BASE.read_bytes().replace(b'\r\n',b'\n')
        with tempfile.TemporaryDirectory() as tmp:
            for tag,ending in (('LF',b'\n'),('CRLF',b'\r\n')):
                with self.subTest(newline=tag):
                    src=Path(tmp)/('core_'+tag+'.mmd')
                    src.write_bytes(base.replace(b'\n',ending))
                    dest=Path(tmp)/('out_'+tag)
                    subprocess.run([
                        sys.executable,str(ROOT/'src/ddta_process.py'),
                        '--core-ttl',str(CORE),'--process-ttl',str(PROCESS),
                        '--process-guide',str(GUIDE),'--core-guide',str(COREGUIDE),'--core-mermaid',str(src),
                        '--modules','core','--out-dir',str(dest),
                    ],check=True,capture_output=True,text=True)
                    self.assertEqual(src.read_bytes(),(dest/'05_graph.mmd').read_bytes())
    def test_deterministic(self):
        ir=project(CORE,PROCESS,GUIDE)
        frag,diag=ProcessRenderer(ir,GUIDE,COREGUIDE).render()
        self.assertEqual(self.fragment,frag)
        self.assertEqual(json.dumps(self.ir,sort_keys=True),json.dumps(ir,sort_keys=True))
        self.assertEqual(self.unified,compose(BASE,frag,ir,diag))
    def test_link_style_has_valid_indices(self):
        n=count_mermaid_edges(self.unified)
        ix=[int(k) for k in re.findall(r'linkStyle\s+(\d+)\s+stroke:',self.unified)]
        self.assertTrue(all(0<=i<n for i in ix))
        self.assertEqual(len(ix),len(set(ix)))
        self.assertTrue(any('stroke:#C62828' in line for line in self.unified.splitlines() if 'linkStyle' in line))
        self.assertTrue(any('stroke:#79B991' in line for line in self.unified.splitlines() if 'linkStyle' in line))
    def test_xor_single_header_and_concurrent_circle(self):
        for control,condition in [('ModelAgreementXor','ModelResultsAgree'),('RetrainingThresholdXor','AtLeastTenDiscordances')]:
            control_id=EX+control
            wrapper=stable('condition:'+control_id+':'+EX+condition)
            self.assertTrue(in_subgraph(self.fragment,stable('control-region:'+control_id),wrapper))
            self.assertNotIn(stable(control_id)+'(['+json.dumps('XOR · 1 ramo',ensure_ascii=False)+'])', self.fragment)
            self.assertIn(wrapper+' --> ',self.fragment)
        circle=stable(EX+'ConcurrentOCRSplit')
        self.assertIn(circle+'(('+json.dumps('∥',ensure_ascii=False)+'))',self.fragment)
    def test_semantic_guards_and_colored_edges(self):
        for control,yes,no,yes_target,no_target in [
            ('ModelAgreementXor','ModelResultsAgree','ModelResultsDisagree','EndAgreement','ReportDiscordanceStep'),
            ('RetrainingThresholdXor','AtLeastTenDiscordances','BelowTenDiscordances','InvokeRetrainingStep','EndDiscordance'),
        ]:
            wrapper=stable('condition:'+EX+control+':'+EX+yes)
            self.assertIn(wrapper+' --> '+stable(EX+yes_target),self.fragment)
            self.assertIn(wrapper+' --> '+stable(EX+no_target),self.fragment)
            self.assertEqual(self.ir['conditions'][EX+no]['operator'],'NOT')
            self.assertEqual(self.ir['conditions'][EX+no]['members'],[EX+yes])
        colors=[color for _,color in self.diag['processLinkStylesRelative'] if color in ('#238636','#C62828')]
        self.assertEqual(sorted(colors),sorted(['#238636','#C62828']*2))
    def test_atomic_condition_has_two_operands_inside_yellow_wrapper(self):
        control=EX+'ModelAgreementXor'
        guard=EX+'ModelResultsAgree'
        wrapper=stable('condition:'+control+':'+guard)
        for name in ('operand-left:','operand-right:'):
            operand_id=stable(name+control+':'+guard)
            self.assertTrue(in_subgraph(self.fragment,wrapper,operand_id))
        self.assertIn('ExtractedPlateOperand',self.fragment)
        self.assertIn('VerifiedPlateOperand',self.fragment)

    def test_guide_selects_split_marker_per_control_kind(self):
        from ddta_process import guide_rules
        x=guide_rules(GUIDE)[('class-style','process:ControlNode')]['projection']['splitMarker']['byKind']
        self.assertEqual(x['XOR_SPLIT']['shape'],'rounded-rectangle')
        self.assertEqual(x['CONCURRENT_SPLIT']['shape'],'circle')
        rules=guide_rules(GUIDE)
        self.assertEqual(rules[('projection-rule-id','conditional-xor-single-atomic-header')]['selection']['negativeOperatorValue'],'NOT')

    def test_internal_contracts_are_rdf_not_value_locator(self):
        self.assertEqual(len(self.ir['contracts']),2)
        pairs=[('ExtractPlateNumberStep','ExtractedPlateContract','ExtractedPlateNumber','ExtractedPlateOperand'),
               ('VerifyPlateNumberStep','VerifiedPlateContract','VerifiedPlateNumber','VerifiedPlateOperand')]
        for step,contract,element,operand in pairs:
            self.assertEqual(self.ir['nodes'][EX+step]['outputContracts'],[EX+contract])
            self.assertEqual(self.ir['contracts'][EX+contract]['elements'][0]['iri'],EX+element)
            self.assertEqual(self.ir['operands'][EX+operand]['contractElement'],EX+element)
            contract_id=stable('step-contract:'+EX+step+':OUTPUT:'+EX+contract)
            step_id=stable(EX+step)
            element_id=stable('step-contract-element:'+EX+step+':OUTPUT:'+EX+element)
            self.assertTrue(in_subgraph(self.fragment,step_id,contract_id))
            self.assertTrue(in_subgraph(self.fragment,contract_id,element_id))
            self.assertNotIn('declaresOutputContract',self.fragment)
            self.assertNotIn('hasContractElement',self.fragment)
            self.assertIn('ddta:Contract',self.fragment)
        self.assertEqual({r['declaredOutputStep'] for r in self.ir['operandProvenance']},
            {EX+'ExtractPlateNumberStep', EX+'VerifyPlateNumberStep'})
        self.assertNotIn('valueLocator',self.fragment)
        self.assertNotIn('EvaluateModelAgreementStep',self.fragment)
        self.assertNotIn('PublishPlateNumberStep',self.fragment)
    def test_optional_input_contract_supported_without_duplicating_function_contract(self):
        from rdflib import Namespace
        g=Graph().parse(str(PROCESS),format='turtle')
        ex=Namespace(EX)
        g.add((ex.ReportDiscordanceStep,PR.declaresInputContract,ex.ExtractedPlateContract))
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'with_input.ttl';g.serialize(path,format='turtle')
            ir=project(CORE,path,GUIDE)
            self.assertEqual(ir['nodes'][EX+'ReportDiscordanceStep']['inputContracts'],[EX+'ExtractedPlateContract'])
            rendered,_=ProcessRenderer(ir,GUIDE,COREGUIDE).render()
            step_id=stable(EX+'ReportDiscordanceStep')
            contract_id=stable('step-contract:'+EX+'ReportDiscordanceStep'+':INPUT:'+EX+'ExtractedPlateContract')
            self.assertTrue(in_subgraph(rendered,step_id,contract_id))
            self.assertNotIn('declaresInputContract',rendered)
    def test_shared_element_does_not_invent_unique_producer(self):
        from rdflib import Namespace
        g=Graph().parse(str(PROCESS),format='turtle');ex=Namespace(EX)
        g.add((ex.VerifiedPlateContract,URIRef('https://w3id.org/ddta/core#hasContractElement'),ex.ExtractedPlateNumber))
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'shared.ttl';g.serialize(path,format='turtle')
            ir=project(CORE,path,GUIDE)
        matches=[p for p in ir['operandProvenance'] if p['contractElement']==EX+'ExtractedPlateNumber']
        self.assertEqual(len(matches),1)
        self.assertIsNone(matches[0]['declaredOutputStep'])
        self.assertEqual(set(matches[0]['candidateOutputSteps']),
            {EX+'ExtractPlateNumberStep',EX+'VerifyPlateNumberStep'})
    def test_fallback_xor_without_complement_does_not_invent_header(self):
        from rdflib import Namespace
        g=Graph().parse(str(PROCESS),format='turtle');ex=Namespace(EX)
        g.remove((ex.T_ModelAgreementXor_to_ReportDiscordanceStep,PR.hasGuard,ex.ModelResultsDisagree))
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'no_not_guard.ttl';g.serialize(path,format='turtle')
            ir=project(CORE,path,GUIDE);fragment,diag=ProcessRenderer(ir,GUIDE,COREGUIDE).render()
            self.assertFalse(any(x['control']==EX+'ModelAgreementXor' for x in diag['xorConditionHeaders']))
            self.assertIn(stable(EX+'ModelAgreementXor')+'(['+json.dumps('XOR · 1 ramo',ensure_ascii=False)+'])',fragment)
    def test_reference_invocation(self):
        self.assertIn('invokesProcess',self.fragment)
        self.assertIn('PlateRetrainingProcess',self.fragment)
        self.assertIn('RetrainPlateOCRModels',self.unified)

    def test_core_style_is_read_from_core_guide(self):
        from ddta_process import core_contract_rules, mermaid_style
        rules=core_contract_rules(COREGUIDE)
        self.assertIn('classDef PROC_coreContract '+mermaid_style(rules['classes']['ddta:Contract']['style']),self.fragment)
        self.assertIn('classDef PROC_coreContractElement '+mermaid_style(rules['classes']['ddta:ContractElement']['style']),self.fragment)
        self.assertIn("data:image/svg+xml;base64,",self.fragment)
    def test_contract_views_compact_extended(self):
        comp,cdiag=ProcessRenderer(self.ir,GUIDE,COREGUIDE,'compact').render()
        ext,ediag=ProcessRenderer(self.ir,GUIDE,COREGUIDE,'extended').render()
        self.assertEqual(cdiag['contractView'],'compact')
        self.assertEqual(ediag['contractView'],'extended')
        self.assertIn('ExtractedPlateOperand → ExtractedPlateNumber',comp)
        self.assertIn('VerifiedPlateOperand → VerifiedPlateNumber',comp)
        self.assertNotIn('referencesContractElement',comp)
        self.assertEqual(ext.count('(["referencesContractElement"])'),2)
        self.assertNotIn('|"referencesContractElement"|',ext)
        label_style=next(line for line in ext.splitlines()
                         if line.strip().startswith('classDef PROC_referenceLabel '))
        self.assertIn('fill:#F3F4F6',label_style)
        self.assertIn('stroke-dasharray:5 4',label_style)
        for operand_label,element_name,side in (
            ('ExtractedPlateOperand','ExtractedPlateNumber','left'),
            ('VerifiedPlateOperand','VerifiedPlateNumber','right')):
            operand=EX+operand_label
            element=EX+element_name
            occurrence=stable('operand-'+side+':'+EX+'ModelAgreementXor'+':'+EX+'ModelResultsAgree')
            group=stable('operand-reference-layout:'+occurrence)
            label=stable('operand-contract-reference-label:'+occurrence+':'+element)
            target=stable('step-contract-element:'+EX+('ExtractPlateNumberStep' if side=='left' else 'VerifyPlateNumberStep')+':OUTPUT:'+element)
            self.assertTrue(in_subgraph(ext,group,occurrence))
            self.assertTrue(in_subgraph(ext,group,label))
            self.assertTrue(in_subgraph(ext,stable('condition:'+EX+'ModelAgreementXor'+':'+EX+'ModelResultsAgree'),group))
            self.assertIn(occurrence+' -.-> '+label,ext)
            self.assertIn(label+' -.-> '+target,ext)
        self.assertNotRegex(ext,r'PX_\w+ --- PX_\w+ -\.-> PX_\w+')
        self.assertNotIn('ExtractedPlateOperand → ExtractedPlateNumber',ext)
        self.assertIn(stable('step-contract-element:'+EX+'ExtractPlateNumberStep'+':OUTPUT:'+EX+'ExtractedPlateNumber'),ext)
        # Two RDF references, each rendered as two graphical segments.
        self.assertEqual(ediag['processEdgeCount']-cdiag['processEdgeCount'],4)
        complete=compose(BASE,ext,self.ir,ediag)
        n=count_mermaid_edges(complete)
        indexes=[int(x) for x in re.findall(r'linkStyle\s+(\d+)\s+stroke:',complete)]
        self.assertTrue(all(0<=x<n for x in indexes))
    def test_extended_reference_grouping_is_declared_in_yaml(self):
        import tempfile
        source=GUIDE.read_text(encoding='utf8')
        self.assertIn('type: layout-only-subgraph',source)
        self.assertIn('sourceSegment: "-.->"',source)
        with tempfile.TemporaryDirectory() as folder:
            guide=Path(folder)/'invalid.md'
            guide.write_text(source.replace('scope: containing-atomic-condition',
                                            'scope: outside-the-condition',1),encoding='utf8')
            with self.assertRaisesRegex(ValueError,'raggruppamento'):
                ProcessRenderer(self.ir,guide,COREGUIDE,'extended').render()

    def test_reference_label_style_is_driven_by_process_yaml(self):
        import tempfile
        guide_text=GUIDE.read_text(encoding='utf-8')
        self.assertIn('fill: "#F3F4F6"',guide_text)
        with tempfile.TemporaryDirectory() as directory:
            alt=Path(directory)/'process-guide.md'
            alt.write_text(guide_text.replace('fill: "#F3F4F6"',
                                'fill: "#E5E7EB"',1),encoding='utf-8')
            ext,_=ProcessRenderer(self.ir,alt,COREGUIDE,'extended').render()
            self.assertIn('classDef PROC_referenceLabel fill:#E5E7EB',ext)
            self.assertNotIn('classDef PROC_referenceLabel fill:#F3F4F6',ext)

    def test_extended_fails_for_non_resolvable_producer(self):
        from rdflib import Namespace
        g=Graph().parse(str(PROCESS),format='turtle');ex=Namespace(EX)
        g.remove((ex.ExtractPlateNumberStep,PR.declaresOutputContract,ex.ExtractedPlateContract))
        with tempfile.TemporaryDirectory() as temp:
            ttl=Path(temp)/'out.ttl';g.serialize(ttl,format='turtle')
            ir=project(CORE,ttl,GUIDE)
            with self.assertRaisesRegex(ValueError,'Provenienza RDF non risolta'):
                ProcessRenderer(ir,GUIDE,COREGUIDE,'extended').render()
    def test_renderer_uses_no_process_colors_for_core_contract(self):
        import yaml
        from ddta_process import guide_rules
        rule=guide_rules(GUIDE)[('projection-rule-id','process-step-internal-contracts')]
        self.assertNotIn('contractStyle',rule['projection'])
        self.assertNotIn('elementStyle',rule['projection'])
        self.assertEqual(rule['projection']['reuseCoreRelationRule'],'ddta:hasContractElement')
    def test_core_input_and_ontology_hash_are_never_modified(self):
        before={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in (CORE,PROCESS,BASE,COREGUIDE)}
        ProcessRenderer(self.ir,GUIDE,COREGUIDE,'compact').render()
        ProcessRenderer(self.ir,GUIDE,COREGUIDE,'extended').render()
        after={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in before}
        self.assertEqual(before,after)

if __name__=='__main__':unittest.main()
