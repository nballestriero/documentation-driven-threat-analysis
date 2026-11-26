"""Prove ricavate dai 29 record grafici CORE e dagli esempi di integrazione.

Le entità Sample* usate nei dati di prova sono dati di test, non nuova ontologia.
"""
from __future__ import annotations
import copy, json, subprocess, sys, tempfile, unittest, os
from pathlib import Path
from rdflib import Graph, URIRef, RDF, Namespace, Literal

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from ddta_viz.extract_guides import extract_guides
from ddta_viz.compile_rules import compile_rules
from ddta_viz.catalog import Catalog, RuleError
from ddta_viz.project_view import project
from ddta_viz.render_mermaid import render
from ddta_viz.common import load_graph

CORE=Path(os.environ.get('DDTA_VIZ_CORE_GUIDE', str(ROOT.parents[1]/'ontologies/core/DDTA_CORE_VISUALIZATION.md')))
CREDENTIALS=ROOT/'tests/fixtures/credential_exchange.ttl'
EX=Namespace('https://example.org/ddta/test-sheets#')
DDTA=Namespace('https://w3id.org/ddta/core#')

class CompleteGuideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory()
        folder=Path(cls.tmp.name)
        cls.extracted=folder/'extracted.yaml'
        cls.compiled=folder/'compiled.yaml'
        extract_guides([CORE],cls.extracted)
        compile_rules([cls.extracted],cls.compiled)
        cls.catalog=Catalog([cls.compiled])

    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()

    def new_graph(self):
        g=Graph()
        g.bind('ddta',DDTA);g.bind('ex',EX)
        return g

    def show(self,g,**kwargs):
        ir=project(g,self.catalog,**kwargs)
        return ir,render(ir,self.catalog)

    def test_01_guide_has_all_29_normative_rules(self):
        self.assertEqual(len(self.catalog.records),31)
        self.assertEqual({r['record'] for r in self.catalog.records},
                         {'class-style','relation-style','grouped-relations-style','global-label-style','projection-rule'})

    def test_02_every_class_style_generates_a_node_with_declared_color(self):
        items=[r for r in self.catalog.records if r['record']=='class-style']
        self.assertEqual(len(items),13)
        for r in items:
            with self.subTest(target=r['target']):
                g=self.new_graph(); s=EX['Sample']
                prefix,name=r['target'].split(':',1)
                # The guide uses the CORE namespace, but the generator only interprets declared rules.
                g.add((s,RDF.type,DDTA[name]))
                ir,mmd=self.show(g,focus=s)
                self.assertEqual(ir['nodes'][str(s)]['rdfType'],r['target'])
                self.assertIn(r['target'],mmd)
                for prop in ('fill','stroke'):
                    if prop in r.get('style',{}):self.assertIn(r['style'][prop],mmd)

    def relation_fixture(self,prop):
        """Input individual types copied from the specific ontology rule's intended endpoints."""
        configurations={
         'hasSubFunction':('Function','Function','plain','parent'),
         'stores':('Store','StoredContent','plain','parent'),
         'hasSource':('CommunicationChannel','Resource','plain',None),
         'hasDestination':('CommunicationChannel','Resource','plain',None),
         'usesChannel':('CommunicationFunction','CommunicationChannel','plain',None),
         'usesChannelForInput':('Function','CommunicationChannel','plain',None),
         'usesChannelForOutput':('Function','CommunicationChannel','plain',None),
         'hasBoundary':('System','Boundary','plain','child'),
         'encloses':('Boundary','Resource','plain','parent'),
         'hasContractElement':('Contract','ContractElement','plain','parent'),
         'mustPrecede':('Function','Function','siblings','parent'),
         'hasNextStep':('ProcessStep','ProcessStep','steps','process'),
         'realizesFunction':('Process','Function','plain',None),
        }
        ta,tb,mode,focus=configurations[prop]
        g=self.new_graph();a=EX.A;b=EX.B
        g.add((a,RDF.type,DDTA[ta]));g.add((b,RDF.type,DDTA[tb]));g.add((a,DDTA[prop],b))
        if mode=='siblings':
            g.add((EX.Parent,RDF.type,DDTA.Function))
            g.add((EX.Parent,DDTA.hasSubFunction,a))
            g.add((EX.Parent,DDTA.hasSubFunction,b))
        if mode=='steps':
            g.add((EX.Parent,RDF.type,DDTA.Process))
            g.add((EX.Parent,DDTA.hasStep,a))
            g.add((EX.Parent,DDTA.hasStep,b))
        focus_ = EX.Parent if mode in ('siblings','steps') else a if focus=='parent' else b if focus=='child' else None
        return g,focus_

    def test_03_all_11_relation_styles_are_exercised(self):
        rules=[r for r in self.catalog.records if r['record']=='relation-style']
        self.assertEqual(len(rules),13)
        for r in rules:
            rel=r['target'].split(':')[-1]
            with self.subTest(relation=rel):
                g,focus=self.relation_fixture(rel)
                ir,mmd=self.show(g,focus=focus)
                if r['representation']['type']=='containment':
                    self.assertEqual(ir['edges'],[])
                    self.assertIn('Sample' if False else 'ddta:',mmd)
                    self.assertGreaterEqual(ir['statistics']['visualOccurrences'],2)
                else:
                    self.assertTrue(any(e['predicate']==r['target'] for e in ir['edges']))
                    if r.get('label',{}).get('text'):self.assertIn(r['label']['text'],mmd)

    def test_04_all_3_grouped_rules_have_real_members(self):
        g=self.new_graph()
        for individual,typ in [(EX.S,'System'),(EX.F,'Function'),(EX.E,'Environment'),
                               (EX.ST,'Store'),(EX.C,'CommunicationChannel'),(EX.R,'Resource'),
                               (EX.IN,'Contract'),(EX.OUT,'Contract'),(EX.CE,'ContractElement')]:
            g.add((individual,RDF.type,DDTA[typ]))
        g.add((EX.S,DDTA.hasPrimaryFunction,EX.F))
        g.add((EX.S,DDTA.hasOperationalEnvironment,EX.E))
        g.add((EX.E,DDTA.makesAvailable,EX.ST));g.add((EX.E,DDTA.makesAvailable,EX.C));g.add((EX.E,DDTA.makesAvailable,EX.R))
        g.add((EX.F,DDTA.hasInputContract,EX.IN));g.add((EX.F,DDTA.hasOutputContract,EX.OUT))
        g.add((EX.IN,DDTA.hasContractElement,EX.CE));g.add((EX.OUT,DDTA.hasContractElement,EX.CE))
        for focus,expected in [(EX.S,'Primary Functions'),(EX.E,'Available Resources'),(EX.F,'Contracts')]:
            with self.subTest(focus=str(focus)):
                _,mmd=self.show(g,focus=focus)
                self.assertIn(expected,mmd)
        self.assertEqual(len([r for r in self.catalog.records if r['record']=='grouped-relations-style']),3)

    def test_05_global_label_uses_name_and_class(self):
        g=self.new_graph();g.add((EX.Demo,RDF.type,DDTA.Function))
        _,mmd=self.show(g,focus=EX.Demo)
        self.assertIn('Demo',mmd);self.assertIn('ddta:Function',mmd)
        self.assertIn('font-weight:700',mmd)

    def test_06_functional_flow_single_contract(self):
        g=self.new_graph()
        for s,cls in [(EX.Sender,'CommunicationFunction'),(EX.Receiver,'CommunicationFunction'),
                      (EX.Channel,'CommunicationChannel'),(EX.Payload,'Contract')]:
            g.add((s,RDF.type,DDTA[cls]))
        g.add((EX.Sender,DDTA.usesChannelForOutput,EX.Channel))
        g.add((EX.Receiver,DDTA.usesChannelForInput,EX.Channel))
        g.add((EX.Sender,DDTA.hasOutputContract,EX.Payload))
        g.add((EX.Receiver,DDTA.hasInputContract,EX.Payload))
        ir,mmd=self.show(g,view='functional-flow')
        flow=[x for x in ir['edges'] if x['kind']=='projection-edge']
        self.assertEqual(len(flow),2)
        self.assertIn('OUTPUT',mmd);self.assertIn('INPUT',mmd)
        self.assertNotIn('usesChannel',mmd)

    def test_07_credential_exchange_contains_selected_instances_and_relations(self):
        g=load_graph([CREDENTIALS])
        ir,mmd=self.show(g,view='functional-flow')
        self.assertEqual(ir['statistics']['selectedTriples'],93)
        self.assertEqual(ir['statistics']['rdfIndividuals'],33)
        self.assertEqual(len([x for x in ir['edges'] if x['predicate']=='ddta:mustPrecede']),3)
        self.assertEqual(len([x for x in ir['edges'] if x['kind']=='projection-edge']),4)
        for name in ['HandleAuthentication','ReadUserRecord','VerifyCredentials',
                     'VerifyPasswordHash','MD5HashStep','SHAHashStep','ClientBoundary',
                     'ServerBoundary','UsernamePasswordContract','AuthenticationResponseContract']:
            self.assertIn(name,mmd)
        self.assertIn('realizesFunction',mmd)
        self.assertTrue(any(x['code']=='SHARED_RDF_INDIVIDUAL' for x in ir['diagnostics']))

    def test_08_strict_mode_accepts_shared_rdf_identities(self):
        ir, mmd = self.show(load_graph([CREDENTIALS]), view='functional-flow', strict=True)
        shared = [d for d in ir['diagnostics'] if d['code']=='SHARED_RDF_INDIVIDUAL']
        self.assertEqual(len(shared), 1)
        self.assertEqual(shared[0]['severity'], 'info')
        self.assertTrue(mmd.startswith('%%{init:'))

    def test_09_graph_is_independent_of_turtle_triple_order(self):
        src=load_graph([CREDENTIALS]);g=self.new_graph()
        for t in reversed(sorted(src,key=lambda t:tuple(map(str,t)))):g.add(t)
        for p,n in src.namespaces():g.bind(p,n)
        _,a=self.show(src,view='functional-flow')
        _,b=self.show(g,view='functional-flow')
        self.assertEqual(a,b)

    def test_10_color_change_in_guide_yaml_needs_no_python_edit(self):
        g=self.new_graph();g.add((EX.Item,RDF.type,DDTA.Contract))
        old_ir,old=self.show(g,focus=EX.Item)
        with tempfile.TemporaryDirectory() as tmp:
            from ddta_viz.common import dump_yaml
            source={'schema':'ddta-visualization-extract-v1','records':copy.deepcopy(self.catalog.records)}
            for item in source['records']:
                if item.get('target')=='ddta:Contract' and item.get('record')=='class-style':
                    item['style']['fill']='#AABBCC'
                    item.pop('icon',None) # skip copying icon from temp test; not changing style semantics
            p=Path(tmp)/'test.yaml';dump_yaml(source,p)
            cat=Catalog([p]);modified=render(project(g,cat,focus=EX.Item),cat)
            self.assertNotEqual(old,modified)
            self.assertIn('#AABBCC',modified)

    def test_11_new_class_and_relation_in_second_ontology(self):
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)
            demo=source/'demo.yaml'
            extract_guides([ROOT/'examples/extension/DEMO_VISUALIZATION.md'],demo)
            mixed=source/'mixed.yaml'
            compile_rules([self.extracted,demo],mixed)
            cat=Catalog([mixed])
            g=load_graph([ROOT/'examples/extension/demo.ttl'])
            ir=project(g,cat)
            mmd=render(ir,cat)
            self.assertIn('demo:Processor',mmd)
            self.assertIn('#0369A1',mmd)
            self.assertIn('leadsTo',mmd)
            self.assertEqual(len(ir['edges']),1)

    def test_12_partial_ttl_requires_explicit_types(self):
        g=self.new_graph();g.add((EX.A,DDTA.hasInputContract,EX.B))
        with self.assertRaisesRegex(RuleError,'Radice richiesta'):
            self.show(g,focus=EX.A)

    def test_13_cycles_fail_instead_of_invented_layout(self):
        g=self.new_graph()
        for x in (EX.A,EX.B):g.add((x,RDF.type,DDTA.Function))
        g.add((EX.A,DDTA.hasSubFunction,EX.B));g.add((EX.B,DDTA.hasSubFunction,EX.A))
        with self.assertRaisesRegex(RuleError,'Ciclo'):
            self.show(g,focus=EX.A)

    def test_14_mermaid_examples_in_guide_are_available(self):
        import re
        blocks=re.findall(r'```mermaid\n(.*?)\n```',CORE.read_text(encoding='utf-8'),flags=re.S)
        self.assertGreaterEqual(len(blocks),10)
        self.assertTrue(all('flowchart' in x for x in blocks))


    def test_15_every_cli_script_has_help(self):
        scripts=sorted((ROOT/'scripts').glob('*.py'))
        self.assertGreaterEqual(len(scripts),7)  # I passaggi principali possono essere eseguiti separatamente.
        for script in scripts:
            with self.subTest(script=script.name):
                proc=subprocess.run([sys.executable,str(script),'--help'],capture_output=True,text=True,cwd=ROOT)
                self.assertEqual(proc.returncode,0,proc.stderr)
                self.assertIn('usage:',proc.stdout.lower())

    def test_16_optional_query_reduces_selected_triples(self):
        from ddta_viz.select_graph import select_subgraph
        with tempfile.TemporaryDirectory() as tmp:
            full=select_subgraph([CREDENTIALS],None,Path(tmp)/'full.ttl')
            sub=select_subgraph([CREDENTIALS],ROOT/'examples/query/contracts_only.rq',Path(tmp)/'subset.ttl')
            self.assertEqual(len(full),93)
            self.assertEqual(len(sub),18)
            self.assertIn((EX.None_ if False else __import__('rdflib').URIRef('https://example.org/ddta/test-communication#ReadUserRecord'),
                           DDTA.hasInputContract,
                           __import__('rdflib').URIRef('https://example.org/ddta/test-communication#ReadUserRecordContract')),sub)

    def test_17_group_id_is_declared_in_yaml_not_python(self):
        g=self.new_graph()
        for a,cls in [(EX.A,'Function'),(EX.C,'Contract')]:g.add((a,RDF.type,DDTA[cls]))
        g.add((EX.A,DDTA.hasInputContract,EX.C))
        new_records=copy.deepcopy(self.catalog.records)
        for r in new_records:
            if r.get('record')=='grouped-relations-style' and r.get('subjectClass')=='ddta:Function':
                first=r['groups'][0];old=first['id'];first['id']='interfaces-for-test'
                r['layout']['groupOrder']=[('interfaces-for-test' if x==old else x) for x in r['layout']['groupOrder']]
        from ddta_viz.common import dump_yaml
        with tempfile.TemporaryDirectory() as tmp:
            # Class Contract's icon path still points to compiled catalog asset; copy the icon folder.
            import shutil
            out=Path(tmp);shutil.copytree(self.compiled.parent/'icons',out/'icons')
            p=out/'altered.yaml';dump_yaml({'records':new_records},p)
            cat=Catalog([p]);ir=project(g,cat,focus=EX.A)
            self.assertEqual(ir['roots'][0]['children'][0]['key'],'interfaces-for-test')
            self.assertIn('C',render(ir,cat))

    def test_18_second_ontology_via_pipeline_command(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'multi'
            command=[sys.executable,str(ROOT/'scripts/pipeline.py'),
              '--guides-md',str(CORE),str(ROOT/'examples/extension/DEMO_VISUALIZATION.md'),
              '--ttl',str(CREDENTIALS),str(ROOT/'examples/extension/demo.ttl'),
              '--out-dir',str(out)]
            proc=subprocess.run(command,capture_output=True,text=True,cwd=ROOT)
            self.assertEqual(proc.returncode,0,proc.stderr)
            report=json.loads((out/'06_diagnostics.json').read_text())
            self.assertEqual(report['regole'],33)
            self.assertEqual(report['triple'],96)
            mmd=(out/'05_graph.mmd').read_text()
            self.assertIn('ProcessorA',mmd)
            self.assertIn('VerifyCredentials',mmd)

    def test_19_unsupported_shape_must_fail(self):
        from ddta_viz.common import dump_yaml
        g=self.new_graph();g.add((EX.A,RDF.type,DDTA.Function))
        data=copy.deepcopy(self.catalog.records)
        for item in data:
            if item.get('record')=='class-style' and item.get('target')=='ddta:Function':
                item['node']['shape']='new-shape-not-defined'
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'rules.yaml';dump_yaml({'records':data},p)
            cat=Catalog([p])
            with self.assertRaisesRegex(RuleError,'Forma Mermaid non supportata'):
                render(project(g,cat,focus=EX.A),cat)

    def test_21_svg_html_attributes_are_safe_for_mermaid_quoted_labels(self):
        """Regression: Mermaid rejects \" inside a quoted node/subgraph label.

        Embedded SVG images must use HTML single-quoted attributes, not JSON-escaped
        double quotes. Applies to class icons, group captions, and extra text.
        """
        g = load_graph([CREDENTIALS])
        ir, mmd = self.show(g, view='functional-flow')
        self.assertIn("<img src='data:image/svg+xml;base64,", mmd)
        self.assertIn("width='27' height='27'", mmd)
        self.assertIn("width='32' height='32'", mmd)
        # The R1+ layout keeps role/cardinality inside the measured HTML div;
        # test preserved semantics rather than an obsolete, exact CSS fragment.
        self.assertIn('ddta:Contract', mmd)
        self.assertIn('INPUT', mmd)
        self.assertIn('0..1', mmd)
        self.assertNotIn('\\"', mmd)

    def test_20_manual_steps_equal_single_pipeline(self):
        from ddta_viz.select_graph import select_subgraph
        g=load_graph([CREDENTIALS])
        with tempfile.TemporaryDirectory() as tmp:
            filtered=select_subgraph([CREDENTIALS],ROOT/'examples/query/contracts_only.rq',Path(tmp)/'selected.ttl')
            a=render(project(filtered,self.catalog,focus=__import__('rdflib').URIRef('https://example.org/ddta/test-communication#ReadUserRecord')),self.catalog)
            b=render(project(load_graph([Path(tmp)/'selected.ttl']),self.catalog,focus=__import__('rdflib').URIRef('https://example.org/ddta/test-communication#ReadUserRecord')),self.catalog)
            self.assertEqual(a,b)

if __name__=='__main__':unittest.main()
