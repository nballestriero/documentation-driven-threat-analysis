"""R7 graphical contract is driven by TTL+YAML, not handwritten Mermaid."""
import copy
import json
import re
import sys
import unittest
from pathlib import Path
from rdflib import Graph, Namespace

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from ddta_process import project,ProcessRenderer,guide_rules,core_contract_rules,stable,count_mermaid_edges,compose

GUIDE=ROOT.parents[1]/'ontologies/process/DDTA_PROCESS_VISUALIZATION.md'
CORE_GUIDE=ROOT.parents[1]/'ontologies/core/DDTA_CORE_VISUALIZATION.md'
CORE=ROOT/'tests/fixtures/process/examples/00_PLATE_GATE_CORE_BASELINE.ttl'
PROCESS=ROOT/'tests/fixtures/process/examples/02_RECOGNIZE_PLATE_PROCESS_R6_CANDIDATA.ttl'
BASE=ROOT/'tests/fixtures/process/examples/CORE_BASE_GRAFO_SCELTO.mmd'
EX='https://example.org/ddta/plate-gate#'


def in_subgraph(src,parent,child):
    lines=src.splitlines();started=False;depth=0
    for line in lines:
        if not started:
            if re.match(r'^\s*subgraph\s+'+re.escape(parent)+r'\[',line):started=True
            else:continue
        if re.match(r'^\s*subgraph\s+\w+',line):depth+=1
        elif line.strip()=='end':
            depth-=1
            if depth==0:return False
        if child in line:return True
    return False

class R7GraphicalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ir=project(CORE,PROCESS,GUIDE)
        cls.frag,cls.diag=ProcessRenderer(cls.ir,GUIDE,CORE_GUIDE,'extended').render()
        cls.full=compose(BASE,cls.frag,cls.ir,cls.diag)
        cls.rules=guide_rules(GUIDE)

    def test_core_must_precede_visual_palette_reused(self):
        core_txt=CORE_GUIDE.read_text('utf8')
        idx=core_txt.index('target: ddta:mustPrecede')
        snippet=core_txt[idx:idx+580]
        r=self.rules[('relation-style','ddta:hasNextStep')]
        self.assertIn('stroke: "#374151"',snippet)
        self.assertEqual(r['representation']['stroke'],'#374151')
        self.assertEqual(r['representation']['layoutPlacement'],'selected-branch-else-owning-process')
        self.assertEqual(r['representation']['strokePattern'],'dashed')
        self.assertEqual(r['representation']['dashArray'],'6 4')
        self.assertEqual(r['label']['representation'],'rounded-inline-node')
        self.assertEqual((r['label']['fill'],r['label']['stroke'],r['label']['color'],r['label']['cornerRadius']),
                         ('#F3F4F6','#374151','#374151',12))

    def test_participant_blue_dashed_label(self):
        r=self.rules[('relation-style','process:hasParticipantStep')]
        self.assertEqual(r['representation']['stroke'],'#2563EB')
        self.assertEqual(r['representation']['strokePattern'],'dashed')
        self.assertEqual(r['label']['strokePattern'],'dashed')
        self.assertEqual(r['label']['color'],'#2563EB')
        self.assertEqual(r['label']['representation'],'rounded-inline-node')

    def test_real_declarations_have_exact_graphical_labels(self):
        flows=[t for t in self.ir['transitions'] if t.get('sourceRelation')=='ddta:hasNextStep']
        self.assertEqual(self.frag.count('(["hasNextStep"])'),len(flows))
        participants=sum(len(n.get('participantSteps',[])) for n in self.ir['nodes'].values())
        self.assertEqual(self.frag.count('(["hasParticipantStep"])'),participants)
        self.assertNotIn('-->|hasNextStep|',self.frag)
        self.assertNotIn('|hasParticipantStep|',self.frag)
        self.assertTrue(any('stroke-dasharray:6 4' in x[2] and x[1]=='#374151'
                            for x in self.diag['processLinkStylesRelative'] if len(x)>2))
        self.assertTrue(any('stroke-dasharray:6 4' in x[2] and x[1]=='#2563EB'
                            for x in self.diag['processLinkStylesRelative'] if len(x)>2))

    def test_labels_inside_semantic_containers(self):
        for t in self.ir['transitions']:
            if t['sourceRelation']!='ddta:hasNextStep':continue
            source=stable(t['from']);target=stable(t['to'])
            # For XOR targets the visible diagram connects to condition wrapper.
            renderer=ProcessRenderer(self.ir,GUIDE,CORE_GUIDE,'extended')
            source=renderer.next_step_attachment_id(t['from'])
            target=renderer.next_step_attachment_id(t['to'])
            label=stable('rdf-relation-label:ddta:hasNextStep:'+source+':'+target)
            self.assertTrue(in_subgraph(self.frag,stable(t['process']),label))
        ctrl=EX+'ConcurrentOCRSplit'
        for part in self.ir['nodes'][ctrl]['participantSteps']:
            label=stable('rdf-relation-label:process:hasParticipantStep:'+stable(ctrl)+':'+stable(part))
            self.assertTrue(in_subgraph(self.frag,stable('control-region:'+ctrl),label))

    def test_operand_contains_existing_input_contract_not_separate_arrow(self):
        ctrl=EX+'ModelAgreementXor';guard=EX+'ModelResultsAgree'
        pairs=[('ExtractedPlateOperand','PlateNumberContract'),('VerifiedPlateOperand','PlateNumberContract')]
        for name,contract_name in pairs:
            actual=EX+name
            branch='left' if name.startswith('Extracted') else 'right'
            operand=stable('operand-'+branch+':'+ctrl+':'+guard)
            contract=stable('operand-input-contract:'+operand+':'+EX+contract_name)
            self.assertTrue(in_subgraph(self.frag,operand,contract))
            self.assertIn(contract_name,self.frag)
            self.assertIn('INPUT',self.frag)
        self.assertNotIn('(["referencesContractElement"])',self.frag)
        self.assertNotIn('"referencesContractElement"',self.frag)
        g=Graph().parse(str(PROCESS),format='turtle')
        PR=Namespace('https://w3id.org/ddta/process#')
        self.assertEqual(len(list(g.triples((None,PR.referencesContractElement,None)))),2)
        self.assertEqual(len(self.ir['operandProvenance']),2)

    def test_control_contracts_not_repeated_outside_operand(self):
        """R7 R2: the two declared inputs must have just one visible occurrence per control."""
        ctrl=EX+'ModelAgreementXor'
        for view in ('compact','extended'):
            frag,_=ProcessRenderer(self.ir,GUIDE,CORE_GUIDE,view).render()
            # One shared RDF contract: two OUTPUT presentations at OCR Steps,
            # two INPUT presentations within distinct Operands of the XOR.
            name='PlateNumberContract'
            self.assertEqual(frag.count('>'+name+'</span>'),4,(view,name))
            self.assertNotIn('subgraph '+stable('control-contract:'+ctrl+':INPUT:'+EX+name),frag)
            self.assertNotIn('subgraph '+stable('control-contracts-group:'+ctrl),frag)
        self.assertEqual(self.ir['nodes'][ctrl]['inputContracts'],[EX+'PlateNumberContract'])

    def test_unreferenced_control_input_and_output_remain_visible(self):
        altered=copy.deepcopy(self.ir)
        ctrl=EX+'ModelAgreementXor'
        extra=EX+'PlateImageContract'
        self.assertIn(extra,altered['contracts'])
        altered['nodes'][ctrl]['inputContracts'].append(extra)
        altered['nodes'][ctrl]['outputContracts'].append(extra)
        frag,_=ProcessRenderer(altered,GUIDE,CORE_GUIDE,'extended').render()
        self.assertIn('subgraph '+stable('control-contract:'+ctrl+':INPUT:'+extra),frag)
        self.assertIn('subgraph '+stable('control-contract:'+ctrl+':OUTPUT:'+extra),frag)
        self.assertNotIn('subgraph '+stable('control-contract:'+ctrl+':INPUT:'+EX+'PlateNumberContract'),frag)

    def test_duplicate_rule_is_read_from_yaml(self):
        self.assertEqual(self.rules[('projection-rule-id','process-operand-contract-reference')]['projection']
                         ['duplicateControlContractPresentation']['action'],
                         'suppress-control-contract-copy')
        altered=copy.deepcopy(self.ir)
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            txt=GUIDE.read_text('utf-8')
            p=Path(folder)/'guide.md'
            p.write_text(txt.replace('    action: suppress-control-contract-copy',
                                     '    action: render-control-contract-copy'),encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'anti-duplicazione'):
                ProcessRenderer(altered,p,CORE_GUIDE,'extended').render()

    def test_missing_contract_raises_instead_of_guessing(self):
        altered=copy.deepcopy(self.ir)
        altered['nodes'][EX+'ModelAgreementXor']['inputContracts']=[]
        with self.assertRaisesRegex(ValueError,'Contratto INPUT Operand non univoco'):
            ProcessRenderer(altered,GUIDE,CORE_GUIDE,'extended').render()

    def test_false_branch_has_next_step_is_drawn_inside_control(self):
        """A declared internal link must not escape its containing XOR branch."""
        ctrl=EX+'ModelAgreementXor'
        report=EX+'ReportDiscordanceStep'
        count=EX+'IncrementDiscordanceCountStep'
        branch=stable('branch:'+ctrl+':hasFalseNextStep:'+report)
        region=stable('control-region:'+ctrl)
        src=stable(report);dst=stable(count)
        label=stable('rdf-relation-label:ddta:hasNextStep:'+src+':'+dst)
        edge=f'{src} --- {label} --> {dst}'
        self.assertTrue(in_subgraph(self.frag,region,label))
        self.assertTrue(in_subgraph(self.frag,branch,label))
        self.assertTrue(in_subgraph(self.frag,branch,edge))
        self.assertEqual(self.frag.count(edge),1)
        self.assertEqual(self.frag.count('\n'+8*' '+label+'(["hasNextStep"])'),0)
        g=Graph().parse(str(PROCESS),format='turtle')
        core=Namespace('https://w3id.org/ddta/core#')
        self.assertIn((Namespace(EX).ReportDiscordanceStep,core.hasNextStep,
                       Namespace(EX).IncrementDiscordanceCountStep),g)
        # Nesting is a presentation choice. No RDF substep assertion is added.
        self.assertFalse(any('hasSubStep' in str(predicate) for _,predicate,_ in g))

    def test_branch_inner_links_remain_unique_in_both_views(self):
        ctrl=EX+'ModelAgreementXor'
        src=stable(EX+'ReportDiscordanceStep')
        dst=stable(EX+'IncrementDiscordanceCountStep')
        label=stable('rdf-relation-label:ddta:hasNextStep:'+src+':'+dst)
        for mode in ('compact','extended'):
            frag,diag=ProcessRenderer(self.ir,GUIDE,CORE_GUIDE,mode).render()
            self.assertTrue(in_subgraph(frag,stable('control-region:'+ctrl),
                                        f'{src} --- {label} --> {dst}'))
            self.assertEqual(frag.count(f'{src} --- {label} --> {dst}'),1)
            self.assertEqual(frag.count('(["hasNextStep"])'),5)
            self.assertTrue(all(0<=x[0]<diag['processEdgeCount']
                                for x in diag['processLinkStylesRelative']))

    def test_entire_false_branch_sequence_is_locally_connected(self):
        """Both consecutive hasNextStep links stay inside the same RDF-selected branch.

        This covers the nested RetrainingThresholdXor, not only the initial
        ReportDiscordanceStep -> IncrementDiscordanceCountStep link.
        """
        control=EX+'ModelAgreementXor'
        report=EX+'ReportDiscordanceStep'
        count=EX+'IncrementDiscordanceCountStep'
        nested=EX+'RetrainingThresholdXor'
        branch=stable('branch:'+control+':hasFalseNextStep:'+report)
        region=stable('control-region:'+control)
        for frm,to in ((report,count),(count,nested)):
            source=stable(frm)
            # A declared next-step arrives at the outer ControlNode region.
            target=ProcessRenderer(self.ir,GUIDE,CORE_GUIDE,'extended').next_step_attachment_id(to)
            label=stable('rdf-relation-label:ddta:hasNextStep:'+source+':'+target)
            link=f'{source} --- {label} --> {target}'
            for view in ('compact','extended'):
                fragment,_=ProcessRenderer(self.ir,GUIDE,CORE_GUIDE,view).render()
                self.assertTrue(in_subgraph(fragment,region,link),(view,frm,to))
                self.assertTrue(in_subgraph(fragment,branch,link),(view,frm,to))
                self.assertEqual(fragment.count(link),1,(view,frm,to))
            rdf=Graph().parse(str(PROCESS),format='turtle')
            ddta=Namespace('https://w3id.org/ddta/core#')
            self.assertIn((Namespace(EX)[frm.rsplit('#',1)[1]],ddta.hasNextStep,
                           Namespace(EX)[to.rsplit('#',1)[1]]),rdf)

    def test_other_step_links_remain_outside_false_branch(self):
        """A branch-local placement does not pull unrelated transitions inside."""
        control=EX+'ModelAgreementXor'
        report=EX+'ReportDiscordanceStep'
        branch=stable('branch:'+control+':hasFalseNextStep:'+report)
        prefix=EX+'ReceivePlateImageStep'
        concurrent=EX+'ConcurrentOCRSplit'
        src=stable(prefix)
        dst=stable('control-region:'+concurrent)
        label=stable('rdf-relation-label:ddta:hasNextStep:'+src+':'+dst)
        link=f'{src} --- {label} --> {dst}'
        self.assertEqual(self.frag.count(link),1)
        self.assertFalse(in_subgraph(self.frag,branch,link))

    def test_nested_branch_yaml_semantics_are_enforced(self):
        rules=self.rules[('projection-rule-id','conditional-xor-single-atomic-header')]
        spec=rules['projection']['nestedBranchFlow']
        self.assertEqual(spec['placement'],'within-selected-branch')
        self.assertEqual(spec['relation'],'ddta:hasNextStep')
        self.assertTrue(spec['groupDoesNotAssertStepComposition'])
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            changed=GUIDE.read_text('utf8').replace('placement: within-selected-branch',
                                                   'placement: outside-control')
            p=Path(folder)/'guide.md'
            p.write_text(changed,encoding='utf8')
            with self.assertRaisesRegex(ValueError,'ramo XOR hasNextStep'):
                ProcessRenderer(self.ir,p,CORE_GUIDE,'extended')

    def test_external_control_flow_attaches_at_both_outer_boundaries(self):
        """Direct control-to-control hasNextStep never uses inner `||`/EQ IDs."""
        src=EX+'ConcurrentOCRSplit'; dst=EX+'ModelAgreementXor'
        region_src=stable('control-region:'+src)
        region_dst=stable('control-region:'+dst)
        label=stable('rdf-relation-label:ddta:hasNextStep:'+region_src+':'+region_dst)
        expected=f'{region_src} --- {label} --> {region_dst}'
        g=Graph().parse(str(PROCESS),format='turtle')
        core=Namespace('https://w3id.org/ddta/core#')
        self.assertIn((Namespace(EX).ConcurrentOCRSplit,core.hasNextStep,
                       Namespace(EX).ModelAgreementXor),g)
        for mode in ('compact','extended'):
            fragment,diagnostics=ProcessRenderer(self.ir,GUIDE,CORE_GUIDE,mode).render()
            self.assertEqual(fragment.count(expected),1,mode)
            self.assertTrue(in_subgraph(fragment,stable(EX+'RecognizePlateNumberProcess'),expected))
            old_from=stable(src)
            old_to=stable('condition:'+dst+':'+EX+'ModelResultsAgree')
            self.assertNotIn(f'{old_from} --- {label} --> {old_to}',fragment)
            self.assertNotIn(f'{old_from} --- {label}',fragment)
        self.assertEqual(self.rules[('class-style','process:ControlNode')]['projection']
                         ['externalFlowAttachment']['type'],'mermaid-subgraph-border')
        self.assertEqual(self.rules[('projection-rule-id','conditional-xor-single-atomic-header')]
                         ['projection']['incomingToControlVisualization'],
                         'control-region-border-for-hasNextStep')

    def test_external_flow_to_compound_control_border_and_nested_xor_border(self):
        renderer=ProcessRenderer(self.ir,GUIDE,CORE_GUIDE,'extended')
        pairs=[(EX+'ReceivePlateImageStep',EX+'ConcurrentOCRSplit'),
               (EX+'IncrementDiscordanceCountStep',EX+'RetrainingThresholdXor')]
        for frm,to in pairs:
            src=renderer.next_step_attachment_id(frm)
            dst=stable('control-region:'+to)
            label=stable('rdf-relation-label:ddta:hasNextStep:'+src+':'+dst)
            edge=f'{src} --- {label} --> {dst}'
            self.assertEqual(self.frag.count(edge),1,(frm,to))
        branch=stable('branch:'+EX+'ModelAgreementXor'+':hasFalseNextStep:'+EX+'ReportDiscordanceStep')
        self.assertTrue(in_subgraph(self.frag,branch,edge))

    def test_external_boundary_policy_change_is_rejected(self):
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            changed=GUIDE.read_text('utf8').replace('type: mermaid-subgraph-border',
                                                    'type: internal-control-marker')
            p=Path(folder)/'guide.md'
            p.write_text(changed,encoding='utf8')
            with self.assertRaisesRegex(ValueError,'externalFlowAttachment'):
                ProcessRenderer(self.ir,p,CORE_GUIDE,'extended').render()

    def test_relative_mermaid_edge_indices_unique_and_valid(self):
        # New visual labels split one RDF edge into two Mermaid segments.
        rel=[x[0] for x in self.diag['processLinkStylesRelative']]
        self.assertEqual(len(rel),len(set(rel)))
        self.assertTrue(all(0<=index<self.diag['processEdgeCount'] for index in rel))
        self.assertEqual(self.frag.count('(["hasNextStep"])'),5)

if __name__=='__main__':unittest.main()
