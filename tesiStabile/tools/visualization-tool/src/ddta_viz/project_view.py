"""Proiezione dichiarativa di RDF + cataloghi grafici in un IR con provenance.

Nessun nome di classe/individuo CORE è fissato nel Python. Le relazioni di contenimento
provengono da grouped-relations-style, relation-style.containment o visibleChildRelations.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import defaultdict
from pathlib import Path
from rdflib import Graph, RDF, URIRef, Literal
from .catalog import Catalog, RuleError
from .common import dump_json, load_graph, local_name, qname_or_uri




def _order_declared_sibling_edges(items, edges, predicates, diagnostics, group_name=''):
    """Topological visual order of RDF-declared sibling precedence edges.

    Graphical ordering ONLY: no new RDF triples, nodes, edges, or occurrences.
    The ordering predicates are selected from the already compiled visual guide,
    not hard-coded by ontology name. Keep disconnected items in their original
    deterministic order. A cycle is diagnosed rather than arbitrarily broken.
    """
    if len(items) < 2 or not predicates:
        return items
    # Never reorder mixed containment/group blocks or repeated RDF identities.
    if any(item.get('kind') != 'individual' for item in items):
        return items
    iris = [item['iri'] for item in items]
    if len(set(iris)) != len(iris):
        return items
    index = {iri:i for i,iri in enumerate(iris)}
    adjacency = {iri:set() for iri in iris}
    indegree = {iri:0 for iri in iris}
    for edge in edges:
        if edge['predicate'] not in predicates:
            continue
        source, target = edge['source'], edge['target']
        if source == target or source not in index or target not in index:
            continue
        if target not in adjacency[source]:
            adjacency[source].add(target)
            indegree[target] += 1
    if not any(adjacency.values()):
        return items
    # Kahn topological sorting, with original order as deterministic tie-break.
    import heapq
    available = [(index[iri],iri) for iri in iris if indegree[iri] == 0]
    heapq.heapify(available)
    ordered = []
    while available:
        _, iri = heapq.heappop(available)
        ordered.append(iri)
        for successor in sorted(adjacency[iri], key=index.__getitem__):
            indegree[successor] -= 1
            if indegree[successor] == 0:
                heapq.heappush(available, (index[successor], successor))
    if len(ordered) != len(iris):
        diagnostics.append({
            'code':'CYCLIC_SIBLING_LAYOUT_ORDER', 'severity':'warning',
            'group':group_name, 'individuals':sorted(iri for iri in iris if indegree[iri] > 0),
            'predicates':sorted(predicates),
            'message':'Precedenze cicliche: conservato ordine originale di emissione; nessuna inferenza RDF.'
        })
        return items
    lookup = {item['iri']:item for item in items}
    return [lookup[iri] for iri in ordered]

def project(graph: Graph, rules: Catalog, *, focus=None, view='association', strict=False):
    diag = []
    defs = {}
    def curie(value):
        return graph.namespace_manager.qname(value)
    def iri(value):
        try: return graph.namespace_manager.expand_curie(value)
        except ValueError: return None  # regole di un'altra ontologia assente nel TTL
    def rdf_types(subject):
        return {curie(x) for x in graph.objects(subject, RDF.type)}
    def selected_type(subject):
        try: return rules.preferred_class(rdf_types(subject))
        except RuleError as exc: raise RuleError(f'{subject}: {exc}') from exc
    def matches(subject, expected):
        return rules.matches(rdf_types(subject), expected)
    def props(s, predicate, inverse=False):
        pred = iri(predicate)
        if pred is None: return []
        return sorted((graph.subjects(pred,s) if inverse else graph.objects(s,pred)),key=str)
    def attributes(subject):
        values = {}
        for p,o in graph.predicate_objects(subject):
            if isinstance(o,Literal):
                values[curie(p)] = o.toPython()
        return values
    all_subjects=sorted({s for s,o in graph.subject_objects(RDF.type)},key=str)
    for subject in all_subjects:
        if not isinstance(subject,URIRef):
            diag.append({'code':'UNSUPPORTED_BNODE','severity':'warning','individual':str(subject)})
        elif not rdf_types(subject).intersection(rules.classes):
            diag.append({'code':'NO_CLASS_STYLE','severity':'warning','individual':str(subject),
                         'types':sorted(rdf_types(subject))})
    typed = sorted({s for s in all_subjects if isinstance(s,URIRef) and rdf_types(s).intersection(rules.classes)}, key=str)
    selected = set(typed)
    for s in typed:
        typ = selected_type(s)
        defs[str(s)] = {'iri':str(s),'name':local_name(str(s)),'rdfType':typ,'types':sorted(rdf_types(s)),'attributes':attributes(s)}

    ownership = defaultdict(set)
    # Graph of RDF-declared parent-child relationships, prior to generating any layout.
    for subj in typed:
        t = selected_type(subj)
        grouped = rules.group_rule(t)
        if grouped:
            for g in grouped.get('groups',[]):
                for spec in (g.get('relations') or [g]):
                    prop = spec.get('property') or spec.get('inverseProperty')
                    if not prop: continue
                    for obj in props(subj, prop, bool(spec.get('inverseProperty'))):
                        if obj in selected: ownership[str(obj)].add(str(subj))
        for rule in rules.relations.values():
            if rule['representation']['type'] != 'containment': continue
            repr_ = rule['representation']
            if repr_.get('parent') == 'subject':
                for child in props(subj, rule['target']):
                    if child in selected: ownership[str(child)].add(str(subj))
            elif repr_.get('parent') == 'object':
                for child in props(subj, rule['target'], inverse=True):
                    if child in selected: ownership[str(child)].add(str(subj))
        for prop in rules.classes[t].get('container',{}).get('visibleChildRelations',[]):
            for child in props(subj,prop):
                if child in selected: ownership[str(child)].add(str(subj))
    # Compose nested graphical containment from declared rules, without cloning RDF systems.
    # An inverse grouped association (e.g. Environment <- System) can point to an
    # individual already wrapped by a "parent: object" containment relation
    # (e.g. System -> Boundary). In that case the declared graphical wrapper
    # must sit between the environment group and the system.
    display_bridges = {}
    for parent in typed:
        grouped = rules.group_rule(selected_type(parent))
        if not grouped:
            continue
        for group in grouped.get('groups', []):
            for spec in (group.get('relations') or [group]):
                prop = spec.get('inverseProperty')
                if not prop:
                    continue
                for member in props(parent, prop, inverse=True):
                    if member not in selected:
                        continue
                    wrappers = []
                    for rel in rules.relations.values():
                        rep = rel.get('representation', {})
                        if rep.get('type') != 'containment' or rep.get('parent') != 'object' or rep.get('child') != 'subject':
                            continue
                        wrappers.extend(obj for obj in props(member, rel['target']) if obj in selected)
                    wrappers = sorted(set(wrappers), key=str)
                    if len(wrappers) == 1:
                        wrapper = wrappers[0]
                        display_bridges[(str(parent), str(member), prop)] = str(wrapper)
                        ownership[str(member)].discard(str(parent))
                        ownership[str(wrapper)].add(str(parent))
                    elif len(wrappers) > 1:
                        diag.append({'code': 'AMBIGUOUS_GRAPHICAL_WRAPPER', 'severity': 'warning',
                                     'subject': str(member), 'parent': str(parent),
                                     'wrappers': [str(x) for x in wrappers]})
    # Explicit multipleParents:error on containment relations cannot be downgraded to warning.
    for rule in rules.relations.values():
        if rule['representation']['type']!='containment' or rule.get('validation',{}).get('multipleParents')!='error':
            continue
        pred=iri(rule['target'])
        if pred is None: continue
        seen=defaultdict(set)
        for subj,obj in graph.subject_objects(pred):
            if rule['representation'].get('parent')=='subject':
                seen[str(obj)].add(str(subj))
            else:
                seen[str(subj)].add(str(obj))
        for child,parents in seen.items():
            if len(parents)>1:
                raise RuleError(f"{rule['target']}: multipleParents:error per {child}: {sorted(parents)}")
    # Do not diagnose graphical sharing yet: a focused view can show only one
    # of several RDF parents. Report only identities actually rendered repeatedly.
    roots = [str(x) for x in typed if str(x) not in ownership]
    if focus is not None:
        root_iri = str(focus)
        if root_iri not in defs: raise RuleError(f'Radice richiesta non tipizzata/visibile: {root_iri}')
        roots = [root_iri]
    if not roots and typed:
        raise RuleError('Nessuna radice grafica (possibile ciclo di contenimento): specificare --focus')

    used_triples = set()
    occurrences = defaultdict(list)
    active = []

    def mark(s,p,o):
        used_triples.add((str(s),str(iri(p)),str(o)))
    def group_order(rule, groups):
        preferred = rule.get('layout',{}).get('groupOrder',[])
        return sorted(groups,key=lambda g:(preferred.index(g['id']) if g['id'] in preferred else len(preferred),g['id']))

    def build(subject, parent_path=(), role=None):
        key = str(subject)
        if key in active:
            raise RuleError('Ciclo di contenimento: '+' -> '.join(active+[key]))
        if key not in defs:
            raise RuleError(f'Individuo privo di rdf:type/class-style nella selezione: {key}')
        active.append(key)
        occurrence = 'O_'+hashlib.sha256(json.dumps([key,parent_path,role],sort_keys=True).encode()).hexdigest()[:14]
        element = {'kind':'individual', **defs[key], 'occurrence': occurrence, 'role':role, 'children':[]}
        occurrences[key].append({'id':occurrence,'path':list(parent_path),'role':role})
        group_rule = rules.group_rule(defs[key]['rdfType'])
        claimed = set()
        if group_rule:
            for group in group_order(group_rule,group_rule.get('groups',[])):
                target_items=[]
                rels=group.get('relations') or [group]
                relation_mode=bool(group.get('relations'))
                for spec in rels:
                    pred = spec.get('property') or spec.get('inverseProperty')
                    if not pred:continue
                    inverse = 'inverseProperty' in spec
                    linked=props(subject,pred,inverse)
                    # Diagnostic role group (providesFunction without specific role).
                    if group.get('displayWhen')=='generic-relation-without-selected-specific-role':
                        resolution=group_rule.get('resolution',{})
                        specific=set()
                        for rp in resolution.get('specificRoleProperties',[]):
                            specific.update(props(subject,rp))
                        linked=[x for x in linked if x not in specific]
                    linked=[obj for obj in linked if obj in selected]
                    if linked:claimed.add((pred,inverse))
                    if group.get('subgroups'):
                        subgroups=group['subgroups']
                        preferred=group_rule.get('layout',{}).get('resourceGroupOrder',[])
                        remaining=list(linked)
                        for sub in sorted(subgroups,key=lambda x:(preferred.index(x['id']) if x['id'] in preferred else len(preferred),x['id'])):
                            filtered=[obj for obj in remaining if matches(obj,sub['class'])]
                            if not filtered:continue
                            remaining=[x for x in remaining if x not in filtered]
                            children=[build(obj,parent_path+(occurrence,sub['id'])) for obj in filtered]
                            target_items.append({'kind':'group','key':sub['id'],'label':sub.get('label',''),
                                                 'children':children,'styleRef':sub.get('style'),
                                                 'groupRuleClass':group_rule['subjectClass'],'group':group['id'],
                                                 'iconKey':sub.get('icon')})
                            for obj in filtered: mark(obj if inverse else subject,pred,subject if inverse else obj)
                        if remaining:
                            diag.append({'code':'UNCLASSIFIED_SUBGROUP','severity':'warning','subject':key,
                                         'group':group['id'],'individuals':[str(x) for x in remaining]})
                    else:
                        for obj in linked:
                            if spec.get('targetClass') and not matches(obj,spec['targetClass']):
                                raise RuleError(f'{obj}: atteso {spec["targetClass"]} per {pred}')
                            mark(obj if inverse else subject,pred,subject if inverse else obj)
                            bridge = display_bridges.get((key,str(obj),pred)) if inverse else None
                            display_subject = URIRef(bridge) if bridge else obj
                            target_items.append(build(display_subject,parent_path+(occurrence,group['id']),spec.get('roleLabel')))
                if target_items:
                    role_sort=group_rule.get('layout',{}).get('contractOrder',[])
                    if relation_mode and role_sort:
                        target_items.sort(key=lambda x:(role_sort.index(x.get('role')) if x.get('role') in role_sort else len(role_sort),x['iri']))
                    element['children'].append({'kind':'group','key':group['id'],'label':group.get('label',''),
                                                'children':target_items,'styleRef':group.get('style'),
                                                'groupRuleClass':group_rule['subjectClass'],'group':group['id']})

        # Relation-style containment (the rule determines whether parent is subject or object).
        for rule in rules.relations.values():
            rep=rule['representation']
            if rep['type']!='containment':continue
            pred=rule['target']
            if (pred,False) in claimed:continue
            parent_subject=rep.get('parent')=='subject'
            parent_object=rep.get('parent')=='object'
            if not (parent_subject or parent_object):continue
            for obj in props(subject,pred,inverse=parent_object):
                if obj not in selected:continue
                mark(subject if parent_subject else obj,pred,obj if parent_subject else subject)
                element['children'].append(build(obj,parent_path+(occurrence,)))
        # For class containers with visibleChildRelations not necessarily declared as relation-style.
        for cls in rules.lineage(defs[key]['rdfType']):
            for pred in rules.classes[cls].get('container',{}).get('visibleChildRelations',[]):
                if (pred,False) in claimed or pred in rules.relations:continue
                for obj in props(subject,pred):
                    if obj not in selected:continue
                    mark(subject,pred,obj)
                    element['children'].append(build(obj,parent_path+(occurrence,)))
        active.pop()
        return element

    result_roots=[build(URIRef(k)) for k in roots]
    # A semantic "realizes" relation may request a graphical-only outer container.
    # Relocate an independent source root next to the realized target's occurrence.
    # Only unambiguous one-to-one layouts are composed; multi-target cases receive
    # an explicit diagnostic, rather than an arbitrary graphical decision.
    realization_placements = []
    for relation in rules.relations.values():
        if relation['representation']['type'] != 'semantic-relation-with-visual-symbol':
            continue
        if not relation.get('layout',{}).get('graphicalOuterContainer'):
            continue
        predicate = iri(relation['target'])
        if predicate is None:
            continue
        for s,o in sorted(graph.subject_objects(predicate), key=lambda pair:(str(pair[0]),str(pair[1]))):
            source_iri,target_iri=str(s),str(o)
            roots_matching=[r for r in result_roots if r['iri']==source_iri]
            target_locations=[]
            def find_targets(items):
                for idx,item in enumerate(items):
                    if item.get('kind')=='individual' and item['iri']==target_iri:
                        target_locations.append((items,idx,item))
                    else:
                        find_targets(item.get('children',[]))
            find_targets(result_roots)
            if len(roots_matching)!=1 or len(target_locations)!=1:
                diag.append({'code':'REALIZATION_LAYOUT_NOT_DETERMINABLE','severity':'warning',
                             'predicate':relation['target'],'source':source_iri,'target':target_iri,
                             'sourceRoots':len(roots_matching),'targetOccurrences':len(target_locations)})
                continue
            parent_items, index, target_element = target_locations[0]
            process_element = roots_matching[0]
            wrapper={
                'kind':'realization-layout', 'key':relation['target'], 'label':'',
                'direction':relation['layout'].get('preferredDirection','BT'),
                'process':process_element, 'function':target_element,
                'rule':relation, 'children':[process_element,target_element],
                'presentationOnly':True,
            }
            parent_items[index]=wrapper
            result_roots.remove(process_element)
            realization_placements.append((source_iri,target_iri,relation['target']))
    # This is a property of the view, not an assertion of a new RDF relation.
    repeated={iri:loc for iri,loc in occurrences.items() if len(loc)>1}
    # Multiple graphical occurrences are intentional projections of one RDF
    # individual, not an ambiguity: each occurrence has its own Mermaid id,
    # while 'iri' and the definition in 'nodes' remain identical.
    # A nested ancestor does not create a second RDF parent. Multiple parents
    # are reported only when this view renders the shared individual repeatedly.
    for child, parents in sorted(ownership.items()):
        if len(parents)>1 and child in repeated:
            diag.append({'code':'MULTIPLE_GRAPHIC_PARENTS','severity':'info',
                         'subject':child,'parents':sorted(parents),
                         'message':'Occorrenze grafiche lecite in più contesti; identità RDF invariata'})
    if repeated:
        diag.append({'code':'SHARED_RDF_INDIVIDUAL','severity':'info',
                     'message':'Più occorrenze grafiche per uno stesso IRI RDF; nessun nuovo individuo RDF creato',
                     'individuals':{k:len(v) for k,v in sorted(repeated.items())}})
    visible=set(occurrences)
    edges=[]
    for pred,rule in sorted(rules.relations.items()):
        rep=rule['representation']
        if rep['type']=='containment':continue
        p=iri(pred)
        if p is None: continue
        for s,o in sorted(graph.subject_objects(p),key=lambda so:(str(so[0]),str(so[1]))):
            if str(s) not in visible or str(o) not in visible:continue
            scope=rule.get('scope',{})
            if scope.get('subjectClass') and not matches(s,scope['subjectClass']):continue
            if scope.get('objectClass') and not matches(o,scope['objectClass']):continue
            mark(s,pred,o)
            src= str(s) if rep.get('source')!='object' else str(o)
            dst= str(o) if rep.get('destination')!='subject' else str(s)
            edges.append({'kind':rep['type'], 'predicate':pred,'rdfSubject':str(s),'rdfObject':str(o),
                          'source':src,'target':dst,'rule':rule})
    # A communication-flow projection is driven by RDF *directional channel
    # associations*, never inferred from the presence/identity of contracts.
    # All predicate names and presentation rules come from the compiled YAML.
    if view == 'functional-flow':
        communication_rules = [pr for pr in rules.projections.values()
                               if pr.get('view') == 'communication-functional-flow']
        suppressed = set()
        for pr in communication_rules:
            for key in ('association', 'outputAssociation', 'inputAssociation'):
                value = pr.get('inputs', {}).get(key)
                if value:
                    suppressed.add(value)
        edges = [edge for edge in edges if edge['predicate'] not in suppressed]
        for pr in communication_rules:
            config = pr.get('inputs', {})
            generic = config.get('association')
            output_pred = config.get('outputAssociation')
            input_pred = config.get('inputAssociation')
            if not output_pred or not input_pred:
                raise RuleError('Proiezione comunicativa: outputAssociation/inputAssociation mancanti')
            pred_out, pred_in = iri(output_pred), iri(input_pred)
            if pred_out is None or pred_in is None:
                raise RuleError('Proiezione comunicativa: prefisso delle proprietà direzionali sconosciuto')
            predicate_generic = iri(generic) if generic else None
            for channel in sorted((URIRef(x) for x in visible
                                   if rules.matches(defs[x]['types'], pr['target'])), key=str):
                explicit_roles = set()
                for role_key, predicate, source_from_function in (
                    ('outputEdge', output_pred, True),
                    ('inputEdge', input_pred, False),
                ):
                    predicate_uri = iri(predicate)
                    for function in sorted(graph.subjects(predicate_uri, channel), key=str):
                        if str(function) not in visible:
                            continue
                        required_class = config.get('functionClass')
                        if required_class and not rules.matches(defs[str(function)]['types'], required_class):
                            diag.append({
                                'code': 'COMMUNICATION_ROLE_SUBJECT_NOT_FUNCTION',
                                'severity': 'warning', 'channel': str(channel),
                                'function': str(function), 'predicate': predicate,
                                'expectedClass': required_class,
                            })
                            continue
                        explicit_roles.add(str(function))
                        role_rule = pr['render'][role_key]
                        if source_from_function:
                            source, target = function, channel
                        else:
                            source, target = channel, function
                        edges.append({
                            'kind': 'projection-edge', 'predicate': predicate,
                            'rdfSubject': str(function), 'rdfObject': str(channel),
                            'source': str(source), 'target': str(target),
                            'rule': pr['render'], 'label': role_rule['label'],
                            'renderRole': role_key,
                        })
                        mark(function, predicate, channel)
                # A non-qualified usesChannel still denotes an association,
                # but does not tell us whether any information is sent/received.
                if predicate_generic is not None:
                    legacy_functions = sorted((f for f in graph.subjects(predicate_generic, channel)
                                               if str(f) in visible and str(f) not in explicit_roles), key=str)
                    for function in legacy_functions:
                        diag.append({
                            'code': 'COMMUNICATION_CHANNEL_ROLE_UNSPECIFIED',
                            'severity': 'warning', 'channel': str(channel),
                            'function': str(function),
                            'reason': 'generic-association-has-no-input-output-role',
                        })
    # Order graphical siblings only where a rule explicitly describes a
    # directed relationship scoped to selected sibling functions. The rule
    # identifies the RDF predicate; this renderer contains no fixed CORE IRI.
    order_predicates = {
        name for name, rule in rules.relations.items()
        if rule.get('scope',{}).get('selectedSiblingFunctionsOnly')
        and rule.get('representation',{}).get('type') == 'directed-edge'
        and rule.get('representation',{}).get('direction') == 'subject-to-object'
    }
    if order_predicates:
        def order_nested_siblings(items, group_name=''):
            for item in items:
                if item.get('children'):
                    item['children'] = order_nested_siblings(
                        item['children'], item.get('key') or item.get('name') or group_name)
            return _order_declared_sibling_edges(items, edges, order_predicates, diag, group_name)
        result_roots = order_nested_siblings(result_roots)

    # Relazioni selezionate senza regola grafica: mai inventare un edge.
    graphical_props={str(iri(x)) for x in rules.relations if iri(x) is not None}
    for rule in rules.groups.values():
        for group in rule.get('groups',[]):
            for spec in (group.get('relations') or [group]):
                prop=spec.get('property') or spec.get('inverseProperty')
                if prop and iri(prop) is not None:graphical_props.add(str(iri(prop)))
    for rule in rules.classes.values():
        for prop in rule.get('container',{}).get('visibleChildRelations',[]):
            if iri(prop) is not None: graphical_props.add(str(iri(prop)))
    for s,p,o in sorted(graph, key=lambda t: tuple(map(str,t))):
        if p != RDF.type and isinstance(o,URIRef) and str(p) not in graphical_props:
            diag.append({'code':'NO_VISUAL_RULE','severity':'warning','rdfSubject':str(s),
                         'rdfPredicate':str(p),'rdfObject':str(o)})
    if strict and any(x['severity']=='warning' for x in diag):
        raise RuleError('Ambiguità della proiezione (modalità --strict): '+str(diag))
    return {'schema':'ddta-graph-ir-v2','view':view,'roots':result_roots,'nodes':defs,
            'occurrences':dict(sorted(occurrences.items())),'edges':edges,
            'diagnostics':diag,'realizationPlacements':realization_placements,'statistics':{'selectedTriples':len(graph),'rdfIndividuals':len(defs),
                                            'roots':len(result_roots),'visualOccurrences':sum(map(len,occurrences.values())),
                                            'edges':len(edges)}}


def main(argv=None):
    ap=argparse.ArgumentParser(description='Proietta un modello TTL selezionato sul catalogo grafico (IR JSON).')
    ap.add_argument('--ttl',nargs='+',required=True,type=Path,help='TTL già selezionati dalla query')
    ap.add_argument('--rules',nargs='+',required=True,type=Path,help='YAML compilati')
    ap.add_argument('--focus',help='IRI/QName radice; se omesso tutte le radici selezionate')
    ap.add_argument('--view',choices=['association','functional-flow'],default='association')
    ap.add_argument('--strict',action='store_true',help='Tratta anche le ambiguità come errori')
    ap.add_argument('--out',type=Path,required=True,help='IR JSON')
    args=ap.parse_args(argv)
    g=load_graph(args.ttl)
    ir=project(g,Catalog(args.rules),focus=URIRef(qname_or_uri(g,args.focus)) if args.focus else None,
               view=args.view,strict=args.strict)
    dump_json(ir,args.out)
    print(f"IR: {ir['statistics']} -> {args.out}")
    return 0

if __name__=='__main__':raise SystemExit(main())
