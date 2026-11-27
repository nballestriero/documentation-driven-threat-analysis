#!/usr/bin/env python3
"""DDTA PROCESS extension: RDF -> Process IR -> Mermaid fragment.

CORE generator is never imported, patched, or called here. The last composition
stage consumes an immutable R10.1 CORE Mermaid file and the Process fragment.
Supported: Step containment, direct Step successors, AtomicCondition XOR,
concurrent control, implementedBy and invokesProcess.
Unsupported PROCESS declarations are reported (not silently invented).
"""
from __future__ import annotations
import argparse, base64, collections, hashlib, html, json, re
from pathlib import Path
from rdflib import Graph, RDF, RDFS, Namespace, Literal, URIRef
import yaml

CORE=Namespace('https://w3id.org/ddta/core#')
PR=Namespace('https://w3id.org/ddta/process#')
DATA=Namespace('https://w3id.org/ddta/data#')

# These RDF names were removed from the approved PROCESS ontology. Retain the
# names here *only* to reject stale input, never to project or render them.
_DEPRECATED_PROCESS_NAMES = (
    'ProcessTransition', 'hasTransition', 'fromStep', 'toStep', 'hasGuard',
    'CompositeCondition', 'Condition', 'hasCondition', 'logicalOperator',
    'SynchronizationNode', 'hasActivationCondition',
)

def reject_deprecated_process_vocabulary(graph):
    """Fail closed even when obsolete triples are disconnected from a Process."""
    found=[]
    for name in _DEPRECATED_PROCESS_NAMES:
        iri=PR[name]
        if (any(graph.triples((iri,None,None))) or
            any(graph.triples((None,iri,None))) or
            any(graph.triples((None,None,iri)))):
            found.append(name)
    if found:
        raise ValueError('Vocabolario PROCESS obsoleto: '+', '.join('process:'+name for name in found))

def local(iri): return str(iri).rsplit('#',1)[-1]
def stable(key, prefix='PX'): return prefix+'_'+hashlib.sha256(str(key).encode('utf-8')).hexdigest()[:12]
def quote(text): return json.dumps(str(text),ensure_ascii=False)
def exactly(g,s,p,required=True):
    xs=sorted(set(g.objects(s,p)),key=str)
    if len(xs)!=(1 if required else 0):
        if not required and len(xs)==1:return xs[0]
        if not required and not xs:return None
        raise ValueError(f'{local(s)}: {local(p)} cardinalita attesa {"1" if required else "0..1"}, trovati {len(xs)}')
    return xs[0] if xs else None

def optional_single(g, subject, predicate, default=None):
    """Deterministic 0..1 cardinality for single-valued RDF attributes."""
    values=sorted(set(g.objects(subject,predicate)), key=lambda value:(str(value),str(getattr(value,'language',''))))
    if len(values)>1:
        raise ValueError(f'{local(subject)}: piu valori per {local(predicate)}; la vista non puo scegliere arbitrariamente')
    return values[0] if values else default


def deterministic_label(g, subject, default):
    """Stable preference for Italian, untagged then English RDFS labels.

    Multiple different labels in the same language are invalid: selecting one
    would make the view dependent on graph iteration order.
    """
    labels=list(set(g.objects(subject, RDFS.label)))
    if not labels:
        return default
    grouped=collections.defaultdict(set)
    for value in labels:
        grouped[(value.language or '').lower()].add(str(value))
    if any(len(vals)>1 for vals in grouped.values()):
        raise ValueError(f'{local(subject)}: etichette RDF conflittuali nella stessa lingua')
    for lang in ('it','', 'en'):
        if lang in grouped:return sorted(grouped[lang])[0]
    return sorted((lang,sorted(vals)[0]) for lang,vals in grouped.items())[0][1]


def guide_rules(path):
    content=Path(path).read_text(encoding='utf-8')
    raw=re.findall(r'```yaml ddta-visualization\s*\n(.*?)\n```',content,re.S)
    rules=[yaml.safe_load(x) for x in raw]
    d={(r.get('record'),r.get('target')):r for r in rules if isinstance(r,dict) and r.get('target')}
    # Multiple projection rules may share one RDF target: index by rule ID.
    d.update({('projection-rule-id',r.get('id')):r for r in rules if isinstance(r,dict) and r.get('record')=='projection-rule' and r.get('id')})
    for k in [('relation-style','process:referencesContractElement'),('projection-rule-id','process-operand-contract-reference'),('class-style','process:ControlNode'),('class-style','process:AtomicCondition'),('relation-style','process:implementedBy'),('projection-rule-id','conditional-xor-single-atomic-header'),('projection-rule-id','process-step-internal-contracts')]:
        if k not in d:raise ValueError('Regola grafica PROCESS mancante: '+str(k))
    return d



def data_step_graphic_rules(path):
    """DATA graphic declarations used by the integrated Step owner.

    All display names, relation labels and styles originate in the guide.
    No example individuals or placement inferred from their labels.
    """
    if path is None:return {},{}
    raw=re.findall(r'```yaml ddta-visualization\s*\n(.*?)\n```',Path(path).read_text(encoding='utf-8'),re.S)
    classes={}; relations={}
    for block in raw:
        rule=yaml.safe_load(block)
        if rule.get('module')!='data':raise ValueError('Non-DATA rule in DATA guide')
        target=rule.get('target','')
        if not target.startswith('data:'):continue
        iri=str(DATA[target.split(':',1)[1]])
        if rule.get('record')=='class-style' and rule.get('inheritsVisualFormFrom')=='ddta:ProcessStep':
            if iri in classes or rule.get('displayType')!=target:raise ValueError('Invalid DATA Step graphic rule: '+target)
            classes[iri]=rule
        if rule.get('record')=='relation-style' and rule.get('representation',{}).get('targetOccurrence')=='existing-core-occurrence':
            if iri in relations:raise ValueError('Duplicate DATA Step relation graphic rule: '+target)
            relations[iri]=rule
    return classes,relations


def core_contract_rules(path):
    """Read-only CORE visual semantics. No CORE generator code is imported."""
    content=Path(path).read_text(encoding='utf-8')
    raw=re.findall(r'```yaml ddta-visualization\s*\n(.*?)\n```', content, re.S)
    rules=[yaml.safe_load(x) for x in raw]
    classes={r.get('target'):r for r in rules if isinstance(r,dict) and r.get('record')=='class-style'}
    relation=next((r for r in rules if isinstance(r,dict) and r.get('record')=='relation-style' and r.get('target')=='ddta:hasContractElement'),None)
    group=next((r for r in rules if isinstance(r,dict) and r.get('record')=='grouped-relations-style' and r.get('subjectClass')=='ddta:Function'),None)
    for k in ('ddta:Contract','ddta:ContractElement','ddta:ProcessStep'):
        if k not in classes: raise ValueError('CORE class-style non disponibile: '+k)
    if not relation or relation.get('representation',{}).get('type')!='containment' or relation['representation'].get('drawEdge') is not False:
        raise ValueError('CORE hasContractElement deve usare containment senza arco')
    if not group: raise ValueError('CORE grouped-relations-style per Function non disponibile')
    contracts=next((g for g in group['groups'] if g.get('id')=='contracts'),None)
    if not contracts or contracts.get('representation')!='containment-group' or contracts.get('drawEdges') is not False:
        raise ValueError('CORE Contracts group incompatibile')
    return {'classes':classes,'containment':relation,'group':contracts,'guidePath':str(Path(path))}

def mermaid_style(style):
    parts=[]
    for k in ('fill','stroke','color'):
        if k in style:parts.append(k+':'+str(style[k]))
    if style.get('strokeWidth') is not None:parts.append('stroke-width:'+str(style['strokeWidth'])+'px')
    if style.get('strokePattern')=='dashed':parts.append('stroke-dasharray:'+str(style.get('dashArray','5 4')))
    if style.get('cornerRadius') is not None:
        parts += ['rx:'+str(style['cornerRadius'])+'px','ry:'+str(style['cornerRadius'])+'px']
    return ','.join(parts)

def contract_role_label(name, role, rule, core_guide):
    """Resolve CORE icon and title presentation from CORE class-style YAML."""
    color=rule['style']['color']
    title=(f"<div style='display:inline-block;text-align:center;line-height:1.4;padding:6px 10px;color:{color}'>"
           f"<span style='display:block;font-size:11px;color:{color}'>{html.escape(role)}</span>"
           f"<span style='display:block;font-size:16px;font-weight:700;color:{color}'>{html.escape(name)}</span>"
           f"<span style='display:block;font-size:11px;color:{color}'>ddta:Contract</span></div>")
    icon=rule.get('icon',{})
    if icon.get('source'):
        file=Path(core_guide).parent / icon['source']
        if not file.is_file():raise ValueError('Icona CORE Contract mancante: '+str(file))
        source='data:image/svg+xml;base64,'+base64.b64encode(file.read_bytes()).decode('ascii')
        title=f"<img src='{source}' width='{icon.get('mermaid',{}).get('height',27)}' height='{icon.get('mermaid',{}).get('height',27)}'/>"+title
    return quote(title)

def contract_element_style(rule, element):
    """CORE conditional style is evaluated from declared RDF cardinality only."""
    st=dict(rule['style'])
    value=element.get('minOccurs')
    for spec in rule.get('conditionalStyles',[]):
        when=spec.get('when',{})
        if when.get('property')!='ddta:minOccurs' or value is None:continue
        if (when.get('operator')=='equals' and value==when.get('value') or
            when.get('operator')=='greater-than' and value>when.get('value')):
            st.update({k:v for k,v in spec.items() if k!='when'})
    return st

def project(core_ttl,process_ttl,guide,data_guide=None):
    guide_rules(guide)
    data_classes,data_relations=data_step_graphic_rules(data_guide)
    g=Graph().parse(str(core_ttl),format='turtle'); baseline=set(g)
    g.parse(str(process_ttl),format='turtle')
    reject_deprecated_process_vocabulary(g)
    if not baseline.issubset(set(g)):raise AssertionError('CORE modificato nella composizione')
    processes=sorted(g.subjects(RDF.type,CORE.Process),key=lambda p:(-len(set(g.objects(p,CORE.hasStep))),str(p)))
    typemap={}
    for s in sorted(g.subjects(RDF.type,None),key=str):
        typemap[str(s)]=sorted(str(t) for t in g.objects(s,RDF.type))
    result={'schema':'ddta-process-ir-v1','coreBaselineTripleCount':len(baseline),'rdfTripleCount':len(g),
            'processes':[],'nodes':{},'conditions':{},'transitions':[],
            'references':[],'realizations':[],'diagnostics':[],'contracts':{},'operands':{},'operandProvenance':[]}
    nodes=result['nodes'];conditions=result['conditions'];trans=result['transitions'];references=result['references']
    if list(g.triples((None,DATA.readsFrom,None))) and str(DATA.readsFrom) not in data_relations:
        raise ValueError('DATA readsFrom requires its graphical relation rule in --data-guide')
    if list(g.subjects(RDF.type,DATA.ReadStep)) and str(DATA.ReadStep) not in data_classes:
        raise ValueError('DATA ReadStep requires its graphical class rule in --data-guide')
    if list(g.triples((None,DATA.writesTo,None))) and str(DATA.writesTo) not in data_relations:
        raise ValueError('DATA writesTo requires its graphical relation rule in --data-guide')
    if list(g.subjects(RDF.type,DATA.WriteStep)) and str(DATA.WriteStep) not in data_classes:
        raise ValueError('DATA WriteStep requires its graphical class rule in --data-guide')
    def add_node(s):
        if str(s) not in nodes:
            nodes[str(s)]={'iri':str(s),'name':local(s),'label':deterministic_label(g,s,local(s)),
              'rdfTypes':typemap.get(str(s),[]),'controlKind':str(optional_single(g,s,PR.controlKind,'')),
              'isStep':(s,RDF.type,CORE.ProcessStep) in g or (s,RDF.type,PR.ControlNode) in g,
              'joinPolicy':str(optional_single(g,s,PR.joinPolicy,'')),
              'requiredCount':str(optional_single(g,s,PR.requiredCount,'')),
              'completionCriterion':str(optional_single(g,s,PR.completionCriterion,'')),
              'participantSteps':[str(x) for x in sorted(set(g.objects(s,PR.hasParticipantStep)),key=str)],
              'evaluatesCondition':str(optional_single(g,s,PR.evaluatesCondition,''))}
        if (s,RDF.type,PR.CodeReference) in g:
            fields=('repositoryLocator','sourcePath','symbolIdentifier','codeElementKind','sourceRevision')
            nodes[str(s)]['codeReferenceFields']={key:str(value) for key in fields
                if (value:=optional_single(g,s,PR[key])) is not None}
        return nodes[str(s)]
    def add_condition(c):
        if str(c) in conditions:return
        if (c,RDF.type,PR.AtomicCondition) not in g:
            raise ValueError('evaluatesCondition richiede process:AtomicCondition: '+local(c))
        op=str(exactly(g,c,PR.comparisonOperator))
        if op not in ('EQ','NE','LT','LE','GT','GE'):
            raise ValueError('Operatore non ammesso: '+op)
        left=exactly(g,c,PR.hasLeftOperand);right=exactly(g,c,PR.hasRightOperand)
        for operand in (left,right):
            if (operand,RDF.type,PR.Operand) not in g:
                raise ValueError('Operand non tipizzato: '+local(operand))
            elements=sorted(g.objects(operand,PR.referencesContractElement),key=str)
            if len(elements)>1:raise ValueError('Operand con ContractElement ambiguo: '+local(operand))
            if elements and (elements[0],RDF.type,CORE.ContractElement) not in g:
                raise ValueError('ContractElement non tipizzato: '+local(elements[0]))
            result['operands'][str(operand)]={'iri':str(operand),'name':local(operand),
                'contractElement':str(elements[0]) if elements else None,
                'resourceReferences':[str(x) for x in sorted(g.objects(operand,PR.referencesResource),key=str)],
                'valueLocator':[str(x) for x in sorted(g.objects(operand,PR.valueLocator),key=str)],
                'literalValue':[str(x) for x in sorted(g.objects(operand,PR.literalValue),key=str)]}
            stored_refs=sorted(set(g.objects(operand,PR.referencesStoredContent)),key=str)
            if stored_refs:
                result['operands'][str(operand)]['storedContentReferences']=[str(x) for x in stored_refs]
        conditions[str(c)]={'iri':str(c),'name':local(c),'rdfType':'process:AtomicCondition',
                            'operator':op,'members':[],'left':str(left),'right':str(right)}
    for p in processes:
        steps=sorted(g.objects(p,CORE.hasStep),key=str)
        for s in steps:
            node=add_node(s)
            specializations=sorted(set(node['rdfTypes'])&set(data_classes))
            if len(specializations)>1:raise ValueError('Ambiguous DATA Step graphic class: '+str(s))
            if specializations:node['dataStepGraphicClass']=specializations[0]
            access=[]
            for pred in sorted(data_relations):
                for target in sorted(set(g.objects(s,URIRef(pred))),key=str):
                    if not specializations:raise ValueError('DATA access requires a declared DATA Step class: '+str(s))
                    if not any((target,RDF.type,t) in g for t in (CORE.StoredContent,DATA.DataBlock)):
                        raise ValueError('DATA access target must be StoredContent: '+str(target))
                    access.append({'predicate':pred,'target':str(target)})
            if access:node['dataAccessReferences']=access
            for field,rel in (('inputContracts',PR.declaresInputContract),('outputContracts',PR.declaresOutputContract)):
                declared=sorted(set(g.objects(s,rel)),key=str)
                node[field]=[str(c) for c in declared]
                for contract in declared:
                    if (contract,RDF.type,CORE.Contract) not in g:
                        raise ValueError('Contratto Step senza rdf:type ddta:Contract: '+local(contract))
                    elements=sorted(set(g.objects(contract,CORE.hasContractElement)),key=str)
                    for e in elements:
                        if (e,RDF.type,CORE.ContractElement) not in g:
                            raise ValueError('Elemento di contratto Step non tipizzato: '+local(e))
                    result['contracts'][str(contract)]={'iri':str(contract),'name':local(contract),
                        'elements':[{'iri':str(e),'name':local(e),'label':deterministic_label(g,e,local(e)),
                          'minOccurs':int(optional_single(g,e,CORE.minOccurs)) if list(g.objects(e,CORE.minOccurs)) else None,
                          'maxOccurs':int(optional_single(g,e,CORE.maxOccurs)) if list(g.objects(e,CORE.maxOccurs)) else None} for e in elements]}
        add_node(p)
        initial=sorted(set(g.objects(p,PR.hasInitialStep)),key=str)
        if any(entry not in steps for entry in initial):
            raise ValueError('InitialStep fuori da hasStep: '+local(p))
        # R5: a ControlNode directly declares its TRUE/FALSE successor. These
        # are subproperties of CORE hasNextStep (no named transition individual).
        for s in steps:
            criterion=optional_single(g,s,PR.evaluatesCondition)
            if criterion:
                if (s,RDF.type,PR.ControlNode) not in g:
                    raise ValueError('evaluatesCondition richiede ControlNode: '+local(s))
                add_condition(criterion)
            direct_branches=[]
            for rel,polarity in ((PR.hasTrueNextStep,'TRUE'), (PR.hasFalseNextStep,'FALSE')):
                targets=sorted(set(g.objects(s,rel)),key=str)
                if len(targets)>1:raise ValueError('Piu successori per ramo '+polarity+': '+local(s))
                for target in targets:
                    if target not in steps:raise ValueError('Successore fuori hasStep: '+local(target))
                    if (s,CORE.hasNextStep,target) in g:
                        raise ValueError('Successione duplicata nel TTL: '+local(s)+' -> '+local(target))
                    direct_branches.append((target,rel,polarity))
            if direct_branches and ((s,RDF.type,PR.ControlNode) not in g or str(optional_single(g,s,PR.controlKind,''))!='XOR_SPLIT'):
                raise ValueError('Rami TRUE/FALSE riservati a XOR_SPLIT: '+local(s))
            if direct_branches and len(direct_branches)!=2:
                raise ValueError('Controllo binario incompleto: '+local(s))
            for target,rel,polarity in direct_branches:
                trans.append({'iri':None,'process':str(p),'from':str(s),'to':str(target),
                              'guard':str(criterion) if criterion else None,
                              'sourceRelation':local(rel),'branch':polarity})
        direct_pairs={(t['from'],t['to']) for t in trans if t['process']==str(p)}
        for s in steps:
            for target in sorted(set(g.objects(s,CORE.hasNextStep)),key=str):
                if target not in steps:continue
                if (str(s),str(target)) in direct_pairs:continue  # TRUE/FALSE subproperties already modeled
                trans.append({'iri':None,'process':str(p),'from':str(s),'to':str(target),
                              'guard':None,'sourceRelation':'ddta:hasNextStep','branch':None})
        for s in steps:
            for prop in (PR.implementedBy,PR.usesConfiguration,PR.invokesProcess,PR.hasCodeReference):
                for res in sorted(g.objects(s,prop),key=str):
                    if prop==PR.hasCodeReference and (res,RDF.type,PR.CodeReference) not in g:
                        raise ValueError('hasCodeReference richiede process:CodeReference: '+local(res))
                    add_node(res)
                    references.append({'from':str(s),'to':str(res),'predicate':local(prop),'iri':str(prop)})
        for prop in (PR.implementedBy,PR.usesConfiguration,PR.hasCodeReference):
            for res in sorted(g.objects(p,prop),key=str):
                if prop==PR.hasCodeReference and (res,RDF.type,PR.CodeReference) not in g:
                    raise ValueError('hasCodeReference richiede process:CodeReference: '+local(res))
                add_node(res);references.append({'from':str(p),'to':str(res),'predicate':local(prop),'iri':str(prop)})
        funcs=list(g.objects(p,CORE.realizesFunction))
        if len(funcs)>1: raise ValueError('Più realizzaFunction: '+local(p))
        for f in funcs:
            add_node(f);result['realizations'].append({'process':str(p),'function':str(f)})
        result['processes'].append({'iri':str(p),'name':local(p),'initial':str(initial[0]) if initial else None,
         'initials':[str(s) for s in initial],
         'subProcesses':[str(s) for s in sorted(set(g.objects(p,PR.hasSubProcess)),key=str)],
         'steps':[str(s) for s in steps], 'function':str(funcs[0]) if funcs else None})
    declared_steps={s for p in result['processes'] for s in p['steps']}
    for pred in sorted(data_relations):
        for subject in sorted(set(g.subjects(URIRef(pred),None)),key=str):
            if str(subject) not in declared_steps:raise ValueError('DATA access Step not owned by a Process: '+str(subject))
    # hasSubProcess: explicit structural composition only. The YAML requires
    # recursive containment, rejects cycles and does not permit arbitrary
    # multiple visual parents that would duplicate one RDF Process identity.
    composition=guide_rules(guide).get(('relation-style','process:hasSubProcess'))
    if any(p['subProcesses'] for p in result['processes']):
        if not composition or composition.get('representation',{}).get('type')!='containment' or composition['representation'].get('drawEdge') is not False or composition['representation'].get('recursive') is not True or composition.get('validation',{}).get('rejectCycles') is not True:
            raise ValueError('Regola grafica hasSubProcess mancante/incompatibile')
    process_ids={p['iri'] for p in result['processes']}
    parents=collections.defaultdict(set)
    children={p['iri']:p['subProcesses'] for p in result['processes']}
    for parent,subs in sorted(children.items()):
        for sub in subs:
            if sub not in process_ids:
                raise ValueError('hasSubProcess verso Process non dichiarato: '+sub)
            parents[sub].add(parent)
    duplicated={c:sorted(ps) for c,ps in parents.items() if len(ps)>1}
    if duplicated:
        raise ValueError('hasSubProcess con piu contenitori visibili: '+str(duplicated))
    visited=set(); active=set()
    def check_composition(iri):
        if iri in active:raise ValueError('hasSubProcess ciclico: '+iri)
        if iri in visited:return
        active.add(iri)
        for child in children[iri]:check_composition(child)
        active.remove(iri);visited.add(iri)
    for iri in sorted(children):check_composition(iri)
    # Internal output-provenance is an RDF path, not a heuristic from a name
    # or a string valueLocator. Never infer actual data transfer from shared contracts.
    producers=collections.defaultdict(set)
    for pp in result['processes']:
        for step in pp['steps']:
            for contract in nodes[step].get('outputContracts',[]):
                for element in result['contracts'][contract]['elements']:
                    producers[element['iri']].add(step)
    for operand in sorted(result['operands'].values(),key=lambda o:o['iri']):
        elem=operand['contractElement']
        if not elem:continue
        matches=sorted(producers.get(elem,()))
        # A ContractElement describes a shared specification, not an output
        # occurrence. Multiple producing Steps are valid. Preserve all RDF
        # candidates, but never bind a particular Operand to a producer unless
        # the RDF path is unique. No inferred runtime dataflow is asserted.
        result['operandProvenance'].append({'operand':operand['iri'],'contractElement':elem,
            'declaredOutputStep':matches[0] if len(matches)==1 else None,
            'candidateOutputSteps':matches})
    # R6: validate compound CONCURRENT_SPLIT from explicit RDF membership,
    # never from guessed step names or a visual grouping.
    for proc in result['processes']:
        inside=[t for t in trans if t['process']==proc['iri']]
        inc=collections.Counter(t['to'] for t in inside)
        for step in proc['steps']:
            node=nodes[step];members=node.get('participantSteps',[])
            if not members:continue
            if node['controlKind']!='CONCURRENT_SPLIT':
                raise ValueError('hasParticipantStep richiede CONCURRENT_SPLIT: '+node['name'])
            if len(members)<2 or any(x not in proc['steps'] for x in members) or step in members:
                raise ValueError('Partecipanti RDF non validi: '+node['name'])
            if not node['joinPolicy'] or node['joinPolicy'] not in ('ALL','ANY','N_OF_M'):
                raise ValueError('joinPolicy composto mancante/non riconosciuta: '+node['name'])
            if node['completionCriterion'] not in ('SUCCESS','TERMINATED'):
                raise ValueError('completionCriterion non valido: '+node['name'])
            count=len(members)
            if node['joinPolicy']=='N_OF_M':
                if not node['requiredCount'] or int(node['requiredCount'])<1 or int(node['requiredCount'])>count:
                    raise ValueError('N_OF_M incoerente: '+node['name'])
            elif node['requiredCount']:
                raise ValueError('requiredCount non ammesso con ALL/ANY: '+node['name'])
            successors=[t for t in inside if t['from']==step]
            if len(successors)!=1 or successors[0]['sourceRelation']!='ddta:hasNextStep':
                raise ValueError('Controllo composto richiede unico hasNextStep successivo: '+node['name'])
            for participant in members:
                if any(t['from']==participant or t['to']==participant for t in inside):
                    raise ValueError('Step partecipante non deve ricevere arco di controllo implicito: '+local(participant))
    # Validate known aggregate join and transition count per Process.
    for p in result['processes']:
        inside=[t for t in trans if t['process']==p['iri']]
        incoming=collections.Counter(t['to'] for t in inside)
        for s in p['steps']:
            n=nodes[s]
            if n['joinPolicy']=='N_OF_M' and not n['participantSteps']:
                if not n['requiredCount'] or int(n['requiredCount'])>incoming[s] or int(n['requiredCount'])<1:
                    raise ValueError('Sincronizzazione N_OF_M incoerente: '+n['name'])
    if result['realizations']:
        result['diagnostics'].append({'severity':'warning','code':'REALIZES_FUNCTION_LAYOUT_NOT_INTEGRATED_IN_IR_R1','message':'L identita RDF e conservata, ma non la disposizione CORE §24'})
    result['references'].sort(key=lambda x:(x['from'],x['predicate'],x['to']))
    result['realizations'].sort(key=lambda x:(x['process'],x['function']))
    result['transitions'].sort(key=lambda x:(x['process'],x['from'],x['to'],x['iri']))
    return result

class ProcessRenderer:
    def __init__(self,ir,guide,core_guide,contract_view="compact",show_operand_resource_references=False,data_guide=None):
        if contract_view not in ('compact','extended'):raise ValueError('contract_view: compact oppure extended')
        self.contract_view=contract_view
        self.show_operand_resource_references=bool(show_operand_resource_references)
        self.core=core_contract_rules(core_guide);self.core_guide=core_guide;self.guide=guide
        self.data_step_classes,_=data_step_graphic_rules(data_guide)
        self.ir=ir;self.rules=guide_rules(guide);self.lines=[];self.styles=collections.defaultdict(set)
        self.edges=[];self.shown=set();self.condition_uses=[];self.boxes={};self.linkstyles=[];self.emitted_links=0;self.seen_steps=set();self.relation_label_defs=set();self.branch_local_flow_edges=set();self.process_local_flow_edges=set()
        self.nodes=ir['nodes'];self.conds=ir['conditions'];self.steprefs=collections.defaultdict(list)
        for r in ir['references']:self.steprefs[r['from']].append(r)
        self.out=collections.defaultdict(list);self.inc=collections.defaultdict(list)
        for t in ir['transitions']:
            self.out[t['from']].append(t);self.inc[t['to']].append(t)
        for k in self.out:self.out[k].sort(key=lambda t:(t.get('branch')=='FALSE',t['to']))
        self.header_compressions=[]
        self.contract_rule=self.rules[('projection-rule-id','process-step-internal-contracts')]['projection']
        self.ref_rule=self.rules[('projection-rule-id','process-operand-contract-reference')]['projection']
        self.ref_style=self.rules[('relation-style','process:referencesContractElement')]
        self.element_occurrences={} ; self.operand_occurrences=collections.defaultdict(list);self.reference_labels={}
        if self.ref_rule['modes'][contract_view]['kind'] not in ('inline-reference-label','directed-reference-edge','nested-input-contract'):
            raise ValueError('Modalita riferimento non supportata dalla guida')
        self.xor_rule=self.rules[('projection-rule-id','conditional-xor-single-atomic-header')]
        nested=self.xor_rule['projection'].get('nestedBranchFlow')
        self.nested_local_enabled=nested is not None
        if nested is not None and (nested.get('relation')!='ddta:hasNextStep' or
            nested.get('placement')!='within-selected-branch' or
            nested.get('source')!='explicit-rdf-only' or
            nested.get('includeRelationshipLabel') is not True or
            nested.get('drawOutsideBranchAgain') is not False or
            nested.get('groupDoesNotAssertStepComposition') is not True):
            raise ValueError('Guida grafica ramo XOR hasNextStep non compatibile')
    def add(self,line,indent=1):
        self.lines.append('    '*indent+line)
        if not line.lstrip().startswith(('%%','class ','classDef ','linkStyle ','style ','subgraph ','direction ')):
            self.emitted_links += len(re.findall(r'~~~|-->|---|-\.->',line))
    def style(self,kind,id):self.styles[kind].add(id)
    def text_label(self,name,typ,color):
        return quote("<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:6px 10px;background:transparent'>"
            +f"<span style='display:block;font-size:16px;font-weight:700;color:{color}'>{html.escape(name)}</span>"
            +f"<span style='display:block;font-size:11px;color:{color}'>{html.escape(typ)}</span></div>")
    def sid(self,iri):return stable(iri)
    def emit_relation_label(self,source,target,predicate,rule,depth=1):
        """Declares a visualization-only node, preferably inside the Process region."""
        prop=rule['representation']; lab=rule['label']
        if (prop.get('type')!='directed-edge-via-label-node' or not prop.get('drawEdge') or
            prop.get('sourceSegment')!='---' or prop.get('targetSegment')!='-->' or
            lab.get('representation')!='rounded-inline-node' or lab.get('rdfIndividual') is not False):
            raise ValueError('Regola grafica etichetta di relazione non valida: '+predicate)
        ident=stable('rdf-relation-label:'+predicate+':'+source+':'+target)
        if ident not in self.relation_label_defs:
            self.add(ident+'(['+quote(lab['text'])+'])',depth)
            label_style={k:v for k,v in lab.items() if k in ('fill','stroke','color','strokeWidth','strokePattern','dashArray','cornerRadius')}
            self.add('style '+ident+' '+mermaid_style(label_style),depth)
            self.relation_label_defs.add(ident)
        return ident

    def add_semantic_relation(self,source,target,predicate,rule,depth=1):
        """Visual connection derived from existing RDF edge; label is not RDF."""
        prop=rule['representation']
        ident=self.emit_relation_label(source,target,predicate,rule,depth)
        before=self.emitted_links
        self.add(source+' '+prop['sourceSegment']+' '+ident+' '+prop['targetSegment']+' '+target,depth)
        link_style=('stroke-width:'+str(prop['strokeWidth'])+'px'+
                    (',stroke-dasharray:'+str(prop.get('dashArray','6 4')) if prop['strokePattern']=='dashed' else ''))
        self.linkstyles.extend([(before,prop['stroke'],link_style),(before+1,prop['stroke'],link_style)])

    def input_contract_for_operand(self,operand_iri,control_iri):
        """Resolve the *declared* control input Contract, never guess from a name."""
        element=self.ir['operands'][operand_iri].get('contractElement')
        if not element:return None
        cfg=self.rules[('projection-rule-id','process-operand-contract-reference')]['selection']
        if (cfg.get('controlContractRelation')!='process:declaresInputContract' or
            cfg.get('contractElementRelation')!='ddta:hasContractElement' or
            cfg.get('requireUniqueControlInputContract') is not True):
            raise ValueError('Guida contratto INPUT Operand incompatibile')
        hits=[contract for contract in self.nodes[control_iri].get('inputContracts',[])
              if any(x['iri']==element for x in self.ir['contracts'][contract]['elements'])]
        if len(hits)!=1:
            raise ValueError('Contratto INPUT Operand non univoco o mancante: '+local(operand_iri))
        return hits[0]

    def cond_id(self,guard,control):return stable('condition:'+control+':'+guard)
    def show_guard(self,guard,control,depth):
        c=self.conds[guard];cid=self.cond_id(guard,control);oid=stable('op:'+control+':'+guard)
        self.add('subgraph '+cid+'['+self.text_label(c['name'],c['rdfType'],'#A67C00')+']',depth)
        self.add('direction LR',depth+1)
        # The diamond is the declared operator's GRAPHIC, never a new RDF
        # ControlNode. Visible AtomicCondition follows the PROCESS guide:
        # Operand A -- operator EQ/GE/etc -- Operand B (horizontal layout).
        self.add(oid+'{'+quote(c['operator'])+'}',depth+1);self.style('operator',oid)
        if c['rdfType']=='process:AtomicCondition':
            left=stable('operand-left:'+control+':'+guard)
            right=stable('operand-right:'+control+':'+guard)
            def operand_display(iri):
                val=self.ir['operands'].get(iri,{})
                ref=val.get('contractElement')
                mode=self.ref_rule['modes'][self.contract_view]
                return local(iri)+(mode.get('separator',' → ')+local(ref) if ref and mode['kind']=='inline-reference-label' else '')
            def render_operand(iri,occurrence):
                display=operand_display(iri)
                element=self.ir['operands'].get(iri,{}).get('contractElement')
                mode=self.ref_rule['modes'][self.contract_view]
                if element and mode['kind']=='nested-input-contract' and mode.get('contractElementPresentation')=='suppress':
                    contract=self.input_contract_for_operand(iri,control)
                    cdata=self.ir['contracts'][contract]
                    role=self.ref_rule['role']
                    contract_id=stable('operand-input-contract:'+occurrence+':'+contract)
                    self.add('subgraph '+occurrence+'['+self.text_label(display,'process:Operand','#334155')+']',depth+1)
                    self.add('direction TB',depth+2)
                    self.add(contract_id+'['+contract_role_label(cdata['name'],role,self.core['classes']['ddta:Contract'],self.core_guide)+']',depth+2)
                    self.add('end',depth+1)
                    self.style('coreContract',contract_id)
                elif mode['kind']=='nested-input-contract' and element:
                    if (mode.get('drawEdge') is not False or
                        self.ref_rule.get('hostContainment')!='operand-subgraph' or
                        self.ref_style['representation'].get('drawEdge') is not False):
                        raise ValueError('Guida Operand con contratto annidato incompatibile')
                    contract=self.input_contract_for_operand(iri,control)
                    cdata=self.ir['contracts'][contract]
                    role=self.ref_rule['role']
                    if role!='INPUT':raise ValueError('Ruolo di contratto Operand non INPUT')
                    contract_id=stable('operand-input-contract:'+occurrence+':'+contract)
                    self.add('subgraph '+occurrence+'['+self.text_label(display,'process:Operand',self.rules[('class-style','process:Operand')]['style']['color'])+']',depth+1)
                    self.add('direction TB',depth+2)
                    c_rule=self.core['classes']['ddta:Contract']
                    self.add('subgraph '+contract_id+'['+contract_role_label(cdata['name'],role,c_rule,self.core_guide)+']',depth+2)
                    self.add('direction TB',depth+3)
                    element_style=self.core['classes']['ddta:ContractElement']
                    for elt in cdata['elements']:
                        eid=stable('operand-contract-element:'+occurrence+':'+elt['iri'])
                        self.add(eid+'['+self.text_label(elt['name'],'ddta:ContractElement',element_style['style']['color'])+']',depth+3)
                        self.style('coreContractElement',eid)
                        special=contract_element_style(element_style,elt)
                        if special!=element_style['style']:
                            self.add('style '+eid+' '+mermaid_style(special),depth+3)
                    self.add('end',depth+2)
                    self.add('end',depth+1)
                    self.style('coreContract',contract_id)
                else:
                    self.add(occurrence+'['+self.text_label(display,'process:Operand',self.rules[('class-style','process:Operand')]['style']['color'])+']',depth+1)
                self.style(self.rules[('class-style','process:Operand')]['node']['style'],occurrence)
                self.operand_occurrences[iri].append(occurrence)
                # Optional RDF-grounded visual projection; off by default to
                # keep the embedded guide examples reproducible.
                if getattr(self, 'show_operand_resource_references', False):
                    spec=self.rules.get(('relation-style','process:referencesResource'))
                    if not spec:
                        raise ValueError('Guida priva della regola process:referencesResource')
                    rep=spec['representation']; lab=spec['label']; obj=spec['objectPresentation']
                    if (rep['type']!='directed-edge-via-label-node' or
                        rep['direction']!='subject-to-object' or
                        rep['sourceSegment']!='---' or rep['targetSegment']!='-->' or
                        obj['rdfClass']!='ddta:Resource' or not rep['drawEdge']):
                        raise ValueError('Regola grafica referencesResource incompatibile')
                    for ref in sorted(self.ir['operands'].get(iri,{}).get('resourceReferences',[])):
                        label_id=stable('operand-resource-reference-label:'+occurrence+':'+ref)
                        target_id=stable('operand-resource-reference-target:'+occurrence+':'+ref)
                        self.add(label_id+'(['+quote(lab['text'])+'])',depth+1)
                        self.add('style '+label_id+' '+mermaid_style(lab),depth+1)
                        self.add(target_id+'['+self.text_label(local(ref),'ddta:Resource',obj['color'])+']',depth+1)
                        self.add('style '+target_id+' '+mermaid_style(obj),depth+1)
                        before=self.emitted_links
                        self.add(occurrence+' '+rep['sourceSegment']+' '+label_id+' '+rep['targetSegment']+' '+target_id,depth+1)
                        style=('stroke-width:'+str(rep['strokeWidth'])+'px'+
                               (',stroke-dasharray:'+str(rep.get('dashArray','6 4')) if rep['strokePattern']=='dashed' else ''))
                        self.linkstyles.extend([(before,rep['stroke'],style),(before+1,rep['stroke'],style)])
            render_operand(c['left'],left)
            render_operand(c['right'],right)
            self.add(left+' ~~~ '+oid+' ~~~ '+right,depth+1)
        self.add('end',depth);self.style('condition',cid)
        self.condition_uses.append({'control':control,'guard':guard,'wrapper':cid,'members':c.get('members',[])})
    def step_type_label(self,node):
        key=node.get('dataStepGraphicClass')
        return self.data_step_classes[key]['displayType'] if key else 'ddta:ProcessStep'

    def step_label_color(self,node):
        return self.core['classes']['ddta:ProcessStep']['style']['color'] if node.get('dataStepGraphicClass') else '#334155'

    def draw_step(self,iri,depth):
        n=self.nodes[iri];nid=self.sid(iri);self.seen_steps.add(iri)
        if n['controlKind'] in ('END_PROCESS','END_BRANCH','WAIT'):
            self.add(nid+'(['+quote(n['controlKind'])+'])',depth);self.style('terminal',nid)
        elif n['joinPolicy']:
            count=len(self.inc[iri]);rep=n['joinPolicy']
            value=f"{n['requiredCount']}/{count}" if rep=='N_OF_M' else rep
            self.add(nid+'(('+quote(value)+'))',depth);self.style('controlsolid',nid)
        else:
            self.add(nid+'['+self.text_label(n['name'],self.step_type_label(n),self.step_label_color(n))+']',depth)
            self.style('coreProcessStep' if n.get('dataStepGraphicClass') else 'step',nid)
    def draw_contract_step(self,iri,declared,depth):
        """CORE class and group styling, PROCESS relations, RDF-only selection."""
        node=self.nodes[iri]; sid=self.sid(iri)
        self.seen_steps.add(iri)
        self.add('subgraph '+sid+'['+self.text_label(node['name'],self.step_type_label(node),self.step_label_color(node))+']',depth)
        self.add('direction TB',depth+1)
        group=stable('step-contracts-group:'+iri)
        gspec=self.core['group']
        self.add('subgraph '+group+'['+quote(gspec['label'])+']',depth+1)
        self.add('direction '+self.contract_rule['layout']['contractGroupDirection'],depth+2)
        self.style('coreContractGroup',group)
        for direction,contract in sorted(declared,key=lambda x:(self.contract_rule['layout']['roleOrder'].index(x[0]),x[1])):
            data=self.ir['contracts'][contract]
            ci=stable('step-contract:'+iri+':'+direction+':'+contract)
            c_rule=self.core['classes']['ddta:Contract']
            self.add('subgraph '+ci+'['+contract_role_label(data['name'],direction,c_rule,self.core_guide)+']',depth+2)
            self.add('direction TB',depth+3)
            self.style('coreContract',ci)
            for element in data['elements']:
                ei=stable('step-contract-element:'+iri+':'+direction+':'+element['iri'])
                self.add(ei+'['+self.text_label(element['name'],'ddta:ContractElement',self.core['classes']['ddta:ContractElement']['style']['color'])+']',depth+3)
                self.style('coreContractElement',ei)
                es=contract_element_style(self.core['classes']['ddta:ContractElement'],element)
                if es!=self.core['classes']['ddta:ContractElement']['style']:
                    self.add('style '+ei+' '+mermaid_style(es),depth+3)
                if direction=='OUTPUT':
                    key=(iri,element['iri'])
                    if key in self.element_occurrences:raise ValueError('ContractElement duplicato nello stesso Step produttore: '+local(element['iri']))
                    self.element_occurrences[key]=ei
            self.add('end',depth+2)
        self.add('end',depth+1)
        self.add('end',depth)
        self.style('coreProcessStep',sid)

    def nested_input_contracts_in_control(self,control):
        """Inputs already shown inside rendered AtomicCondition operands.

        Select solely from declared RDF guard/operand/contract paths. Never
        infer an input contract from a name or suppress unreferenced inputs.
        """
        policy=self.ref_rule.get('duplicateControlContractPresentation')
        if self.ref_rule['modes'][self.contract_view]['kind']!='nested-input-contract':
            return set()
        expected={'scope':'same-control',
                  'when':'input-contract-already-nested-in-operand',
                  'action':'suppress-control-contract-copy',
                  'preserveRdfDeclaration':True,
                  'preserveOtherInputContracts':True,
                  'preserveOutputContracts':True}
        if policy!=expected:
            raise ValueError('Regola YAML anti-duplicazione contratti controllo mancante o incompatibile')
        header=self.xor_header(control)
        if header:
            guards=[header['positive']]
        else:
            guards=sorted({t['guard'] for t in self.out[control] if t['guard']})
        nested=set()
        for guard in guards:
            cond=self.conds[guard]
            # Composite children do not embed operands in the current view.
            if cond['rdfType']!='process:AtomicCondition':
                continue
            for operand in (cond['left'],cond['right']):
                if self.ir['operands'][operand].get('contractElement'):
                    nested.add(self.input_contract_for_operand(operand,control))
        return nested

    def draw_control_contracts(self,iri,depth):
        """Display declared contracts inside the control region, without a second control node.

        Each Contract/ContractElement is an occurrence of its existing RDF identity;
        the group is visualization only. CORE styles and PROCESS relations come from YAML.
        """
        n=self.nodes[iri]
        # Each Contract IRI stays declared in RDF and IR. Suppress only a
        # second local *visual* occurrence when already nested in an Operand.
        embedded=self.nested_input_contracts_in_control(iri)
        declared=[('INPUT',c) for c in n.get('inputContracts',[]) if c not in embedded]
        declared += [('OUTPUT',c) for c in n.get('outputContracts',[])]
        if not declared:return
        group=stable('control-contracts-group:'+iri)
        self.add('subgraph '+group+'['+quote(self.core['group']['label'])+']',depth)
        self.add('direction '+self.contract_rule['layout']['contractGroupDirection'],depth+1)
        self.style('coreContractGroup',group)
        for role,contract in sorted(declared,key=lambda x:(self.contract_rule['layout']['roleOrder'].index(x[0]),x[1])):
            data=self.ir['contracts'][contract]
            ci=stable('control-contract:'+iri+':'+role+':'+contract)
            self.add('subgraph '+ci+'['+contract_role_label(data['name'],role,self.core['classes']['ddta:Contract'],self.core_guide)+']',depth+1)
            self.add('direction TB',depth+2)
            self.style('coreContract',ci)
            for element in data['elements']:
                ei=stable('control-contract-element:'+iri+':'+role+':'+element['iri'])
                self.add(ei+'['+self.text_label(element['name'],'ddta:ContractElement',self.core['classes']['ddta:ContractElement']['style']['color'])+']',depth+2)
                self.style('coreContractElement',ei)
                es=contract_element_style(self.core['classes']['ddta:ContractElement'],element)
                if es!=self.core['classes']['ddta:ContractElement']['style']:
                    self.add('style '+ei+' '+mermaid_style(es),depth+2)
                if role=='OUTPUT':
                    key=(iri,element['iri'])
                    if key in self.element_occurrences:raise ValueError('ContractElement duplicato nello stesso controllo')
                    self.element_occurrences[key]=ei
            self.add('end',depth+1)
        self.add('end',depth)

    def sync_label(self,iri):
        n=self.nodes[iri];cfg=self.rules[('class-style','process:ControlNode')]['projection'].get('concurrentComposition')
        if not cfg:raise ValueError('Guida senza proiezione R6 concurrentComposition')
        policy=n['joinPolicy'];label_def=cfg['label']
        if policy not in ('ALL','ANY','N_OF_M'):raise ValueError('joinPolicy non valida: '+n['name'])
        label=label_def[policy].format(requiredCount=n['requiredCount'],participantCount=len(n['participantSteps']))
        return label+(' · '+n['completionCriterion'] if label_def.get('showCompletionCriterion') else '')

    def render_compound_control(self,iri,depth,local_seen,stop=None):
        n=self.nodes[iri]
        rule=self.rules[('class-style','process:ControlNode')]
        cfg=rule['projection'].get('concurrentComposition')
        membership=self.rules.get(('relation-style','process:hasParticipantStep'))
        if not cfg or not membership:raise ValueError('Guida R6 hasParticipantStep mancante')
        if cfg['participantRelation']!='process:hasParticipantStep' or cfg['outgoingControlRelation']!='ddta:hasNextStep':
            raise ValueError('Guida R6 composizione incompatibile')
        members=n['participantSteps']
        self.seen_steps.add(iri)
        region=stable('control-region:'+iri)
        self.add('subgraph '+region+'['+self.text_label(n['name']+' · '+self.sync_label(iri),'process:ControlNode',rule['style']['color'])+']',depth)
        self.add('direction TB',depth+1)
        marker_cfg=rule['projection']['splitMarker']['byKind']['CONCURRENT_SPLIT']
        mid=self.sid(iri)
        if marker_cfg['shape']!='circle':raise ValueError('Forma nodo concorrente inattesa dalla guida')
        self.add(mid+'(('+quote(marker_cfg['text'])+'))',depth+1)
        self.style('controlsolid',mid)
        self.draw_control_contracts(iri,depth+1)
        row=stable('participant-row:'+iri)
        self.add('subgraph '+row+'[" "]',depth+1)
        self.add('direction '+rule['projection']['branchRegion']['branchRow']['direction'],depth+2)
        self.style('invisible',row)
        for member in members:
            branch=stable('participant-container:'+iri+':'+member)
            self.add('subgraph '+branch+'[" "]',depth+2)
            self.add('direction TB',depth+3)
            self.style('branchsolid',branch)
            self.draw_step_with_resource(member,depth+3)
            self.add('end',depth+2)
            self.seen_steps.add(member)
        self.add('end',depth+1)
        for member in members:
            # One visual label node per *declared* RDF participation relation.
            self.add_semantic_relation(mid,self.sid(member),'process:hasParticipantStep',membership,depth+1)
        self.add('end',depth)
        self.style('region',region)
        nxt=self.out[iri][0]['to']
        self.render_path(nxt,depth,local_seen,stop=stop)

    def draw_code_reference(self,source_id,source_iri,code_iri,depth):
        """CodeReference is visible only from a declared hasCodeReference RDF triple."""
        class_rule=self.rules[('class-style','process:CodeReference')]
        relation_rule=self.rules[('relation-style','process:hasCodeReference')]
        data=self.nodes[code_iri]
        if str(PR.CodeReference) not in data['rdfTypes']:
            raise ValueError('CodeReference non tipizzato: '+code_iri)
        cfg=class_rule.get('icon',{})
        if cfg.get('required') is not True or cfg.get('type')!='svg-file' or cfg.get('mermaidEncoding')!='data-uri-base64':
            raise ValueError('Icona CodeReference non conforme a YAML')
        icon_path=Path(self.guide).parent/cfg['source']
        if not icon_path.is_file():
            raise ValueError('Icona CodeReference mancante: '+str(icon_path))
        icon_src='data:image/svg+xml;base64,'+base64.b64encode(icon_path.read_bytes()).decode('ascii')
        fields=data.get('codeReferenceFields',{})
        color=class_rule['style']['color']
        details=[]
        symbol=fields.get('symbolIdentifier')
        if symbol:details.append('symbolIdentifier: '+symbol)
        # Only RDF-declared details, read in the exact order specified by YAML.
        for field in class_rule.get('label',{}).get('optionalDetails',[]):
            key=field.split(':',1)[-1]
            if fields.get(key):details.append(key+': '+fields[key])
        label=('<img src="'+icon_src+'" width="'+str(cfg.get('widthPx',28))+
               '" height="'+str(cfg.get('heightPx',28))+'"/> '+
               '<span style="font-weight:700;color:'+color+'">'+html.escape(data['label'])+'</span>'+
               '<div style="font-size:11px;color:'+color+'">process:CodeReference</div>')
        for item in details:
            label+='<div style="font-size:10px;color:'+color+'">'+html.escape(item)+'</div>'
        node=stable('code-reference-instance:'+source_iri+':'+code_iri)
        rel=stable('code-reference-relation:'+source_iri+':'+code_iri)
        self.add(node+'['+quote(label)+']',depth)
        self.add('style '+node+' '+mermaid_style(class_rule['style']),depth)
        self.add(rel+'(['+quote(relation_rule['label']['text'])+'])',depth)
        self.add('style '+rel+' '+mermaid_style(relation_rule['label']),depth)
        r=relation_rule['representation'];ix=self.emitted_links
        if r.get('drawEdge') is not True or r.get('direction')!='subject-to-object':
            raise ValueError('Regola grafica hasCodeReference incompatibile')
        self.add(source_id+' -.-> '+rel+' -.-> '+node,depth)
        details='stroke-width:'+str(r.get('strokeWidth',2))+'px'
        if r.get('strokePattern')=='dashed':details+=',stroke-dasharray:'+str(r.get('dashArray','8 5'))
        self.linkstyles.extend([(ix,r['stroke'],details),(ix+1,r['stroke'],details)])

    def draw_step_with_resource(self,iri,depth):
        refs=[r for r in self.steprefs[iri] if r['predicate'] in ('implementedBy','usesConfiguration','hasCodeReference')]
        n=self.nodes[iri]
        declared=[('INPUT',x) for x in n.get('inputContracts',[])]
        declared += [('OUTPUT',x) for x in n.get('outputContracts',[])]
        if not refs and not declared:return self.draw_step(iri,depth)
        # Implementation references are sibling nodes within a layout-only group.
        # Contract/Element containment is *inside* the RDF Step occurrence.
        if refs:
            group=stable('implementation-group:'+iri)
            self.add('subgraph '+group+'[" "]',depth);self.add('direction TB',depth+1)
            content_depth=depth+1
        else:
            group=None;content_depth=depth
        if declared:
            if n['controlKind'] or n['joinPolicy']:
                raise ValueError('Contratto interno su nodo di controllo non supportato nella vista R4.2: '+n['name'])
            self.draw_contract_step(iri,declared,content_depth)
        else:
            self.draw_step(iri,content_depth)
        for r in refs:
            if r['predicate']=='hasCodeReference':
                self.draw_code_reference(self.sid(iri),iri,r['to'],content_depth)
                continue
            resource=self.nodes[r['to']];rid=stable('resource-instance:'+iri+':'+r['to'])
            rel=stable('implementation-relation:'+iri+':'+r['to']+':'+r['predicate'])
            # The specialization is purely a presentation rule from YAML.
            # It does not create a Configuration class in CORE or PROCESS.
            style_rule=self.rules.get(('relation-style','process:'+r['predicate']))
            if (r['predicate']=='usesConfiguration' and style_rule and
                    style_rule.get('representation',{}).get('useDedicatedRenderer') is True):
                rep=style_rule['representation'];lab=style_rule['label'];obj=style_rule['objectPresentation']
                if obj.get('rdfClass')!='ddta:Resource':
                    raise ValueError('usesConfiguration deve riferirsi a ddta:Resource')
                icon_html=''
                if obj.get('icon'):
                    if obj.get('iconMermaidEncoding')!='data-uri-base64':
                        raise ValueError('Encoding icona configuration non supportato')
                    icon_path=Path(self.guide).parent/obj['icon']
                    if not icon_path.is_file():raise ValueError('Icona configurazione mancante: '+str(icon_path))
                    icon_src='data:image/svg+xml;base64,'+base64.b64encode(icon_path.read_bytes()).decode('ascii')
                    icon_html='<img src="'+icon_src+'" width="24" height="24"/> '
                self.add(rel+'(['+quote(lab['text'])+'])',content_depth)
                self.add('style '+rel+' '+mermaid_style(lab),content_depth)
                resource_html=icon_html+'<span style="color:'+obj['stroke']+'">'+html.escape(resource['label'])+'</span>'
                resource_html+='<div style="font-size:11px;color:'+obj['stroke']+'">ddta:Resource</div>'
                self.add(rid+'['+quote(resource_html)+']',content_depth)
                self.add('style '+rid+' '+mermaid_style(obj),content_depth)
                color=rep['stroke']
            else:
                self.add(rel+'(['+quote(r['predicate'])+'])',content_depth);self.style('impllabel',rel)
                self.add(rid+'['+self.text_label(resource['label'],'ddta:Resource','#37694E')+']',content_depth)
                self.style('resource',rid)
                color='#79B991'
            ix=self.emitted_links
            self.add(self.sid(iri)+' -.-> '+rel+' -.-> '+rid,content_depth)
            self.linkstyles.extend([(ix,color),(ix+1,color)])
        if group:
            self.add('end',depth);self.style('invisible',group)
            self.boxes[iri]=group

    def draw_operand_contract_references(self):
        """Only extended mode draws RDF reference edges, never data transfers."""
        if self.contract_view!='extended':return
        if self.ref_rule['modes']['extended']['kind']=='nested-input-contract':
            return  # RDF reference remains in trace; graphic is inside Operand.
        props=self.ref_style['representation']; mode=self.ref_rule['modes']['extended']
        label=self.ref_style['label']
        if (props.get('type')!='directed-edge-via-label-node' or
            props.get('direction')!='subject-to-object' or
            props.get('strokePattern')!='dashed' or
            mode['kind']!='directed-reference-edge' or
            mode.get('labelPlacement')!='intermediate-node' or
            label.get('representation')!='ellipse-inline-node' or
            label.get('rdfIndividual') is not False or
            label.get('strokePattern')!='dashed' or
            props.get('sourceSegment')!='-.->' or
            props.get('targetSegment')!='-.->'):
            raise ValueError('Guida referencesContractElement incompatible con vista estesa')
        index={p['operand']:p for p in self.ir['operandProvenance']}
        for operand in sorted(self.operand_occurrences):
            if not self.ir['operands'].get(operand,{}).get('contractElement'):continue
            path=index.get(operand)
            if not path or not path['declaredOutputStep']:
                raise ValueError('Provenienza RDF non risolta per: '+local(operand))
            key=(path['declaredOutputStep'],path['contractElement'])
            target=self.element_occurrences.get(key)
            if not target:raise ValueError('ContractElement produttore non visibile: '+local(path['contractElement']))
            for source in sorted(set(self.operand_occurrences[operand])):
                # The label and source->label segment were already emitted
                # inside an invisible Operand-local layout group in show_guard.
                # Only the RDF reference's remaining segment exits the group.
                label_id=self.reference_labels.get((operand,source))
                if label_id is None:
                    raise ValueError('Etichetta locale mancante per: '+local(operand))
                ix=self.emitted_links
                self.add(label_id+' '+props['targetSegment']+' '+target)
                self.linkstyles.append((ix,props['stroke']))
    def xor_header(self,control):
        """Return declared positive/NOT pair only when the YAML semantic pattern matches."""
        if self.nodes[control]['controlKind']!='XOR_SPLIT':return None
        rule=self.xor_rule['selection']
        out=self.out[control]
        if (len(out)==2 and {t.get('branch') for t in out}=={'TRUE','FALSE'}):
            pos=next(t for t in out if t['branch']=='TRUE')
            neg=next(t for t in out if t['branch']=='FALSE')
            if pos['guard'] and pos['guard']==neg['guard'] and self.conds[pos['guard']]['rdfType']=='process:AtomicCondition':
                return {'positive':pos['guard'],'negative':neg['guard'],'directBranches':True}
            return None
        return None
    def visible_step_id(self,iri):
        hdr=self.xor_header(iri) if iri in self.nodes else None
        return self.cond_id(hdr['positive'],iri) if hdr else self.sid(iri)
    def next_step_attachment_id(self,iri):
        """Projection-only external flow endpoint: boundary of visible ControlNode.

        `hasNextStep` links the RDF Step identities, not internal control markers
        (concurrent `||` or XOR's condition).  Mermaid supports edges on
        subgraph identifiers, giving border-to-border attachment for controls.
        True/false branch arrows retain their distinct, declared YAML endpoint.
        The attachment policy is read exclusively from the visualization guide.
        """
        if iri not in self.nodes:
            return self.visible_step_id(iri)
        cfg=self.rules[('class-style','process:ControlNode')]['projection'].get('externalFlowAttachment')
        if not cfg:
            raise ValueError('Guida ControlNode priva di externalFlowAttachment')
        expected={
            'relation':'ddta:hasNextStep',
            'type':'mermaid-subgraph-border',
            'controlKinds':['CONCURRENT_SPLIT','XOR_SPLIT'],
            'source':'control-region-border',
            'destination':'control-region-border',
            'doNotAttachToInternalMarker':True,
            'preserveXorBranchOrigin':True,
            'rdfIndividual':False,
        }
        if cfg!=expected:
            raise ValueError('Guida externalFlowAttachment ControlNode incompatibile')
        if self.nodes[iri]['controlKind'] in cfg['controlKinds']:
            return stable('control-region:'+iri)
        return self.visible_step_id(iri)
    def join_after(self,control):
        # A synchronization is a declared step reached from all direct branches.
        starts=[t['to'] for t in self.out[control]]
        if len(starts)<2:return None
        succ=[{t['to'] for t in self.out[x]} for x in starts]
        common=set.intersection(*succ) if succ else set()
        known=[x for x in common if self.nodes[x]['joinPolicy']]
        return known[0] if len(known)==1 else None
    def render_path(self,s,depth,local_seen,stop=None,branch_scope=None):
        if s==stop:return
        if s in local_seen:raise ValueError('Percorso ciclico: '+self.nodes[s]['name'])
        if s in self.seen_steps:return  # already projected by another declared start
        local_seen.add(s)
        n=self.nodes[s]
        if n['controlKind']=='CONCURRENT_SPLIT' and n.get('participantSteps'):
            self.render_compound_control(s,depth,local_seen,stop=stop)
            return
        if n['controlKind'] in ('XOR_SPLIT','CONCURRENT_SPLIT'):
            self.seen_steps.add(s)
            outgoing=self.out[s]
            if len(outgoing)<2:raise ValueError('Split con meno di 2 rami: '+n['name'])
            region=stable('control-region:'+s);row=stable('branch-row:'+s)
            concurrent=n['controlKind']=='CONCURRENT_SPLIT'
            self.add('subgraph '+region+'['+self.text_label(n['name'],'process:ControlNode','#2563EB')+']',depth)
            self.add('direction TB',depth+1)
            # Both kinds are real ControlNode RDF individuals. Graphic shape
            # and marker text come only from the candidate PROCESS guide:
            # XOR chooses exactly one outgoing guarded branch; CONCURRENT
            # activates all selected outgoing branches. No new RDF node.
            hdr=self.xor_header(s)
            if hdr:
                # The XOR RDF individual is represented by the region header,
                # not an extra marker. Only the AtomicCondition has a yellow box.
                self.show_guard(hdr['positive'],s,depth+1)
                self.header_compressions.append({'control':s,'visibleGuard':hdr['positive'],
                    'negativeGuard':hdr['negative'],'ruleId':self.xor_rule['id']})
            else:
                marker_rule=self.rules[('class-style','process:ControlNode')]['projection']['splitMarker']['byKind'][n['controlKind']]
                shape=marker_rule['shape']; marker_text=marker_rule['text']
                mid=self.sid(s)
                if shape=='rounded-rectangle':
                    self.add(mid+'(['+quote(marker_text)+'])',depth+1)
                elif shape=='circle':
                    self.add(mid+'(('+quote(marker_text)+'))',depth+1)
                else:
                    raise ValueError('Forma splitMarker non supportata dalla guida: '+shape)
                self.style('controlsolid' if concurrent else 'controldashed',mid)
            self.draw_control_contracts(s,depth+1)
            self.add('subgraph '+row+'[" "]',depth+1);self.add('direction LR',depth+2)
            self.style('invisible',row)
            join=self.join_after(s) if concurrent else None
            if concurrent and join is None:raise ValueError('Split concorrente senza join determinabile: '+n['name'])
            for idx,t in enumerate(outgoing):
                branch=stable('branch:'+s+':'+(t['iri'] or t['sourceRelation']+':'+t['to']))
                self.add('subgraph '+branch+'[" "]',depth+2);self.add('direction TB',depth+3)
                self.style('branchsolid' if concurrent else 'branchdashed',branch)
                if t['guard'] and not hdr:
                    self.show_guard(t['guard'],s,depth+3)
                self.render_path(t['to'],depth+3,local_seen.copy(),stop=join,branch_scope=s)
                self.add('end',depth+2)
            self.add('end',depth+1)   # end branch row
            # The declared N/M synchronization belongs VISUALLY in the
            # concurrent split region. It remains a distinct RDF Step.
            if join:self.draw_step_with_resource(join,depth+1)
            self.add('end',depth)     # end control region
            self.style('region',region)
            if join:
                remaining=self.out[join]
                if len(remaining)>1:raise ValueError('Join con piu successori: '+n['name'])
                if remaining:self.render_path(remaining[0]['to'],depth,local_seen,stop=stop)
            return
        self.draw_step_with_resource(s,depth)
        nexts=self.out[s]
        if len(nexts)>1:raise ValueError('Step senza ControlNode con piu uscite: '+n['name'])
        if nexts:
            next_edge=nexts[0]
            self.render_path(next_edge['to'],depth,local_seen,stop=stop,branch_scope=branch_scope)
            # When both RDF Steps are shown inside the same selected branch,
            # place the labelled hasNextStep edge INSIDE that branch, too.
            # The link still comes only from the explicit RDF transition.
            # Edges leaving this scope keep the process-level presentation.
            if (self.nested_local_enabled and branch_scope is not None and next_edge['to'] != stop
                    and next_edge['sourceRelation']=='ddta:hasNextStep'
                    and not next_edge.get('guard')):
                rule=self.rules.get(('relation-style','ddta:hasNextStep'))
                if rule:
                    src=self.next_step_attachment_id(s)
                    dst=self.next_step_attachment_id(next_edge['to'])
                    self.add_semantic_relation(src,dst,'ddta:hasNextStep',rule,depth)
                    self.branch_local_flow_edges.add((s,next_edge['to']))
    def render_process(self,p,depth=1,by_iri=None):
        proc=p['iri'];pid=self.sid(proc)
        subs=p.get('subProcesses',[])
        # A leaf without direct Steps is a Process node; a composed Process is
        # a container even if it has no direct Steps of its own.
        if not p.get('initials',([p['initial']] if p['initial'] else [])) and not subs:
            self.add(pid+'['+self.text_label(p['name'],'ddta:Process','#334155')+']',depth)
            self.style('process',pid)
            return
        self.add('subgraph '+pid+'['+self.text_label(p['name'],'ddta:Process','#334155')+']',depth)
        self.add('direction TB',depth+1)
        initial_steps=p.get('initials',([p['initial']] if p['initial'] else []))
        for entry in initial_steps:
            # A step reachable from two declared entries is shown once;
            # both RDF starts remain visible as distinct START markers.
            if entry not in self.seen_steps:
                self.render_path(entry,depth+1,set())
        start_rule=self.rules.get(('relation-style','process:hasInitialStep'))
        if start_rule and start_rule.get('representation',{}).get('renderStartMarker') is True:
            r=start_rule.get('representation',{})
            if (r.get('type')!='derived-start-marker' or
                r.get('markerIsRdfIndividual') is not False or
                r.get('noAutomaticStartFromGraphTopology') is not True or
                r.get('multipleInitialSteps')!='render-one-marker-per-declared-entry' or
                r.get('direction')!='marker-to-selected-object'):
                raise ValueError('Regola grafica hasInitialStep incompatibile')
            for entry in initial_steps:
                start=stable('start-marker:'+proc+':'+entry)
                self.add(start+'(["'+str(r['markerLabel'])+'"])',depth+1)
                self.add('style '+start+' fill:'+r['markerFill']+',stroke:'+r['markerStroke']+',color:'+r['markerColor'],depth+1)
                self.add(start+' --> '+self.next_step_attachment_id(entry),depth+1)
        step_rel=self.rules.get(('relation-style','ddta:hasNextStep'))
        if step_rel and step_rel['representation'].get('layoutPlacement') not in (None,'selected-branch-else-owning-process'):
            raise ValueError('Guida layoutPlacement hasNextStep incompatibile')
        if step_rel:
            for t in self.ir['transitions']:
                if (t['process']==proc and t['sourceRelation']=='ddta:hasNextStep'
                        and (t['from'],t['to']) not in self.branch_local_flow_edges):
                    self.add_semantic_relation(self.next_step_attachment_id(t['from']),
                        self.next_step_attachment_id(t['to']),'ddta:hasNextStep',step_rel,depth+1)
                    self.process_local_flow_edges.add((t['from'],t['to']))
        # Structural containment from explicitly declared RDF links only.
        for child in subs:
            self.render_process(by_iri[child],depth+1,by_iri)
        self.add('end',depth);self.style('process',pid)
    def render(self):
        if self.ir['schema']!='ddta-process-ir-v1':raise ValueError('Process IR non valido')
        by_iri={p['iri']:p for p in self.ir['processes']}
        parents={child for p in self.ir['processes'] for child in p.get('subProcesses',[])}
        # No inferred process composition: only declared direct children nest.
        for p in self.ir['processes']:
            if p['steps'] and not p.get('initials',([p['initial']] if p['initial'] else [])):
                raise ValueError('Process con Step ma senza hasInitialStep: '+p['name'])
        for p in self.ir['processes']:
            if p['iri'] not in parents:
                self.render_process(p,by_iri=by_iri)
        # Fail closed: no declared ProcessStep may disappear graphically.
        expected=set(x for p in self.ir['processes'] for x in p['steps'])
        if expected != self.seen_steps:
            raise ValueError('Step PROCESS non proiettati: '+str(sorted(expected-self.seen_steps)))
        # Flow edges are projected from declared RDF successors; no inferred transfers.
        positive='#238636';negative='#C62828'
        for t in self.ir['transitions']:
            # An edge already emitted inside its selected control branch must
            # not be redrawn outside the ControlNode region.
            if (t['from'],t['to']) in (self.branch_local_flow_edges | self.process_local_flow_edges) and t['sourceRelation']=='ddta:hasNextStep':
                continue
            source=self.visible_step_id(t['from'])
            target=self.visible_step_id(t['to'])
            if t['sourceRelation']=='ddta:hasNextStep':
                source=self.next_step_attachment_id(t['from'])
                target=self.next_step_attachment_id(t['to'])
            hdr=self.xor_header(t['from'])
            if hdr:
                # Both successor branches share one declared AtomicCondition.
                # Visualization edges are not additional RDF triples.
                ix=self.emitted_links
                self.add(source+' --> '+target)
                if t.get('branch')=='TRUE' or (not t.get('branch') and t['guard']==hdr['positive']):
                    self.linkstyles.append((ix,self.xor_rule['projection']['positiveColor']))
                elif t.get('branch')=='FALSE' or (not t.get('branch') and t['guard']==hdr['negative']):
                    self.linkstyles.append((ix,self.xor_rule['projection']['negativeColor']))
                else:raise ValueError('Uscita XOR non classificata: '+str(t['iri']))
            elif t['guard']:
                raise ValueError('Condizione su arco non XOR non supportata: '+str(t['from']))
            else:
                if t.get('sourceRelation')=='ddta:hasNextStep':
                    rule=self.rules[('relation-style','ddta:hasNextStep')]
                    self.add_semantic_relation(source,target,'ddta:hasNextStep',rule)
                else:
                    self.add(source+' --> '+target)
        self.draw_operand_contract_references()
        for r in self.ir['references']:
            if r['predicate']=='invokesProcess':
                rule=self.rules[('relation-style','process:invokesProcess')]
                rep=rule['representation'];lbl=rule['label']
                src=self.sid(r['from']);dst=self.sid(r['to'])
                lab=stable('invokesLabel:'+r['from']+':'+r['to'])
                self.add(lab+'(['+quote(lbl['text'])+'])')
                self.style('implabel',lab)
                ix=self.emitted_links
                self.add(src+' --- '+lab+' --> '+dst)
                style='stroke-width:'+str(rep.get('strokeWidth',1.8))+'px'
                if rep.get('strokePattern')=='dashed':style+=',stroke-dasharray:'+str(rep.get('dashArray','6 4'))
                # The IR records style for both edge segments.
                self.linkstyles.extend([(ix,rep['stroke']),(ix+1,rep['stroke'])])
            elif r['predicate']=='hasCodeReference' and r['from'] in by_iri:
                self.draw_code_reference(self.sid(r['from']),r['from'],r['to'],1)
        # Link realizesFunction to a function's known CORE occurrence in the composer.
        class_defs={
          'step':'fill:#FFFFFF,stroke:#7B8794,color:#334155,stroke-width:1.5px,stroke-dasharray:5 4',
          'process':'fill:#F8FAFC,stroke:#7B8794,color:#334155,stroke-width:2px,rx:8px,ry:8px',
          'region':'fill:#FFFFFF,stroke:#2563EB,color:#2563EB,stroke-width:2px,stroke-dasharray:6 4',
          'branchsolid':'fill:#FFFFFF,stroke:#2563EB,color:#2563EB,stroke-width:1.5px',
          'branchdashed':'fill:#FFFFFF,stroke:#2563EB,color:#2563EB,stroke-width:1.5px,stroke-dasharray:6 4',
          'controlsolid':'fill:#FFFFFF,stroke:#2563EB,color:#2563EB,stroke-width:2px',
          'controldashed':'fill:#FFFFFF,stroke:#2563EB,color:#2563EB,stroke-width:2px,stroke-dasharray:6 4',
          'terminal':mermaid_style(self.rules[('projection-rule-id','process-control-terminal-ellipse')]['style']),
          'invisible':'fill:transparent,stroke:transparent,stroke-width:0px',
          'condition':'fill:#FFFFFF,stroke:#D6A100,color:#A67C00,stroke-width:2px',
          'operator':'fill:#FFFFFF,stroke:#D6A100,color:#A67C00,stroke-width:1.5px',
          'component':mermaid_style(self.rules[('class-style','process:Operand')]['style']),
          'operand':mermaid_style(self.rules[('class-style','process:Operand')]['style']),
          'impllabel':mermaid_style(self.rules[('relation-style','process:invokesProcess')]['label']),
          'implabel':mermaid_style(self.rules[('relation-style','process:invokesProcess')]['label']),
          'resource':'fill:#FFFFFF,stroke:#79B991,color:#37694E,stroke-width:1.5px,stroke-dasharray:8 5',
          'coreContract':mermaid_style(self.core['classes']['ddta:Contract']['style']),
          'coreContractElement':mermaid_style(self.core['classes']['ddta:ContractElement']['style']),
          'coreContractGroup':mermaid_style(self.core['group']['style']),
          'coreProcessStep':mermaid_style(self.core['classes']['ddta:ProcessStep']['style']),
          'referenceLabel':mermaid_style({k:v for k,v in self.ref_style.get('label',{}).items()
                                         if k in ('fill','stroke','color','strokeWidth','strokePattern','dashArray')}),
        }
        # Validate palette and operators against the guide, no second invented palette.
        class_map={'region':('class-style','process:ControlNode'),'condition':('class-style','process:AtomicCondition'),
            'resource':('relation-style','process:implementedBy')}
        for kind,key in class_map.items():
            spec=self.rules[key]
            style=spec.get('style',spec.get('objectPresentation',{}))
            if kind=='region':style=spec.get('projection',{}).get('branchRegion',{})
            expected={'region':('#2563EB',),'condition':('#D6A100',),'resource':('#79B991',)}[kind]
            if style.get('stroke') not in expected:raise ValueError(f'GUIDA cambiata: {key} -> stroke {style.get("stroke")}')
        for typ,style in class_defs.items():
            if self.styles.get(typ):
                self.add(f'classDef PROC_{typ} '+style)
                self.add('class '+','.join(sorted(self.styles[typ]))+' PROC_'+typ)
        return '\n'.join(self.lines)+'\n',{'processes':len(self.ir['processes']),'transitions':len(self.ir['transitions']),
                 'conditionPlacements':self.condition_uses,'implementationGroups':self.boxes,
                 'xorConditionHeaders':self.header_compressions,
                 'internalContracts':len(self.ir['contracts']),'contractView':self.contract_view,'operandProvenance':self.ir['operandProvenance'],
                 'processEdgeCount':self.emitted_links,'processLinkStylesRelative':self.linkstyles,'omitNeutralInvocationLinkStyle':self.rules[('relation-style','process:invokesProcess')]['representation'].get('emitMermaidLinkStyle') is False,'allProcessStepsShown':True, **({'storedContentReferenceOccurrences': {iri:sorted(set(ids)) for iri,ids in sorted(self.operand_occurrences.items()) if self.ir['operands'][iri].get('storedContentReferences')}} if any(o.get('storedContentReferences') for o in self.ir['operands'].values()) else {})}

def count_mermaid_edges(code):
    n=0
    for line in code.splitlines():
        if line.strip().startswith(('%%','class ','classDef ','linkStyle ','style ','subgraph ','flowchart ')):continue
        n+=len(re.findall(r'~~~|-->|---|-\.->',line))
    return n

def _core_function_occurrence(core_mermaid, function_iri, core_guide):
    """Resolve a CORE graphical occurrence by RDF IRI and System role, not by label.

    Multiple graphical occurrences are legitimate when the same Function is
    both a direct System function and a child of a local composite Function.
    Select the explicitly classified System occurrence using the existing
    CORE grouped-relations-style YAML. Fail rather than make an arbitrary pick.
    """
    projection = Path(core_mermaid).with_name('04_projection.json')
    if not projection.is_file():
        return None  # Offline R4.5 snapshots: retain original matching contract.
    data = json.loads(projection.read_text(encoding='utf-8'))
    entries = data.get('occurrences',{}).get(function_iri,[])
    if not entries:
        return None
    core_text = Path(core_mermaid).read_text(encoding='utf-8')
    entries = [o for o in entries if re.search(r'^\s*(?:subgraph\s+)?'+re.escape(o['id'])+r'(?=[\[(])',core_text,re.M)]
    if not entries:
        raise ValueError('Occorrenza CORE dichiarata nell’IR ma assente nel Mermaid: '+function_iri)
    if len(entries)==1:
        return entries[0]['id']
    # Read the group identifiers from the normative CORE YAML; no hard-coded
    # layout/group identifiers and no invented RDF edges.
    guide = Path(core_guide).read_text(encoding='utf-8')
    groups=[]
    for raw in re.findall(r'```yaml ddta-visualization\s*\n(.*?)\n```',guide,re.S):
        rule=yaml.safe_load(raw)
        if isinstance(rule,dict) and rule.get('record')=='grouped-relations-style' and rule.get('subjectClass')=='ddta:System':
            groups.extend(rule.get('groups',[]))
    role_groups=[g['id'] for prop in ('ddta:hasPrimaryFunction','ddta:hasSupportFunction') for g in groups if g.get('property')==prop]
    classified=[o for o in entries if o.get('path') and o['path'][-1] in role_groups]
    if len(classified)==1:
        return classified[0]['id']
    raise ValueError('Più occorrenze grafiche CORE per IRI, nessuna occorrenza di ruolo univoca: '+function_iri)


def compose(core_mmd,process_fragment,ir,diag,core_guide=None):
    base=Path(core_mmd).read_text(encoding='utf-8')
    if base.count('flowchart')!=1:raise ValueError('CORE base non univoco')
    if 'ProcessStep' in base:raise ValueError('CORE base include Step: evitare duplicazione prima di combinare')
    lines=base.rstrip().splitlines()
    offset=count_mermaid_edges(base)
    lines+=['','    %% DDTA PROCESS: modular RDF projection (independent of CORE renderer)',process_fragment]
    for spec in diag['processLinkStylesRelative']:
        i,color=spec[:2]
        details=spec[2] if len(spec)>2 else 'stroke-width:2.5px'
        lines.append(f'    linkStyle {offset+i} stroke:{color},{details}')
    for pair in ir['realizations']:
        process=ir['nodes'][pair['process']];fn=ir['nodes'][pair['function']]
        # Use RDF IRI -> CORE IR occurrence when available, avoiding label-name ambiguity.
        chosen=_core_function_occurrence(core_mmd,pair['function'],core_guide) if core_guide else None
        if chosen is not None:
            lines.append(f'    {chosen} ~~~ {stable(pair["process"])}')
            continue
        # Preserve the original offline snapshot behavior (R4.5, no CORE IR).
        pat=r'^\s*subgraph\s+(\w+)\[.*>'+re.escape(fn['name'])+r'</span>.*ddta:Function.*\]$'
        hits=re.findall(pat,base,re.M)
        if len(hits)==1:
            lines.append(f'    {hits[0]} ~~~ {stable(pair["process"])}')
        elif len(hits)==0:
            fnid=stable('optional-function:'+pair['function'])
            lines.append('    '+fnid+'['+quote(fn['name']+' · ddta:Function')+']')
            lines.append('    '+fnid+' ~~~ '+stable(pair['process']))
        else:raise ValueError('Funzione CORE ambigua: '+fn['name'])
    return '\n'.join(lines)+'\n'

def main():
    ap=argparse.ArgumentParser(description='Modular DDTA PROCESS projector/renderer (CORE R10.1 unchanged)')
    ap.add_argument('--core-ttl',type=Path,required=True)
    ap.add_argument('--process-ttl',type=Path,required=True)
    ap.add_argument('--process-guide',type=Path,required=True)
    ap.add_argument('--core-guide',type=Path,required=True,help='CORE graphical guide, read-only')
    ap.add_argument('--data-guide',type=Path,help='DATA graphical guide, read-only')
    ap.add_argument('--contract-view',choices=['compact','extended'],default='compact')
    ap.add_argument('--show-operand-resource-references',action='store_true',help='Visualizza gli archi RDF process:referencesResource verso risorse runtime (regola grafica R2)')
    ap.add_argument('--core-mermaid',type=Path,required=True)
    ap.add_argument('--integrated-splice',action='store_true',help='Place Process inside the corresponding CORE Function/System occurrence')
    ap.add_argument('--modules',default='core,process')
    ap.add_argument('--out-dir',type=Path,required=True)
    a=ap.parse_args();modules=[x.strip() for x in a.modules.split(',') if x.strip()]
    if len(modules)!=len(set(modules)) or modules[0]!='core' or any(m not in ('core','process') for m in modules):
        raise ValueError('In questo pilot sono attivi core oppure core,process')
    a.out_dir.mkdir(parents=True,exist_ok=True)
    if modules==['core']:
        # Byte-preserving CORE-only passthrough. On Windows read_text/write_text
        # may normalize LF <-> CRLF, invalidating a SHA256 regression check.
        original_bytes=a.core_mermaid.read_bytes()
        (a.out_dir/'05_graph.mmd').write_bytes(original_bytes)
        separator=b'' if original_bytes.endswith(b'\n') else b'\n'
        (a.out_dir/'05_graph.md').write_bytes(b'```mermaid\n'+original_bytes+separator+b'```\n')
        print(json.dumps({'modules':modules,'coreUnchanged':True,'processEnabled':False},
                         indent=2,ensure_ascii=False))
        return
    else:
        ir=project(a.core_ttl,a.process_ttl,a.process_guide,a.data_guide)
        (a.out_dir/'04_process_projection.json').write_text(json.dumps(ir,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
        fragment,rdiag=ProcessRenderer(ir,a.process_guide,a.core_guide,a.contract_view,show_operand_resource_references=a.show_operand_resource_references,data_guide=a.data_guide).render()
        (a.out_dir/'04_process_fragment.mmd').write_text(fragment,encoding='utf-8',newline='\n')
        if a.integrated_splice:
            from ddta_integrated_compose import compose_integrated
            mmd=compose_integrated(a.core_mermaid,fragment,ir,rdiag,a.core_guide,a.process_guide,a.data_guide)
        else:
            if any(n.get("dataAccessReferences") for n in ir["nodes"].values()):
                raise ValueError("DATA access requires integrated composition")
            if any(o.get("storedContentReferences") for o in ir["operands"].values()):
                raise ValueError("referencesStoredContent requires integrated composition")
            mmd=compose(a.core_mermaid,fragment,ir,rdiag,a.core_guide)
        diag={'modules':modules,'coreUnchanged':True,'processEnabled':True,**rdiag}
        (a.out_dir/'06_process_diagnostics.json').write_text(json.dumps(diag,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    (a.out_dir/'05_graph.mmd').write_text(mmd,encoding='utf-8',newline='\n')
    (a.out_dir/'05_graph.md').write_text('```mermaid\n'+mmd+'```\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in diag.items() if k not in ('conditionPlacements','implementationGroups','processLinkStylesRelative')},indent=2,ensure_ascii=False))
if __name__=='__main__':main()
