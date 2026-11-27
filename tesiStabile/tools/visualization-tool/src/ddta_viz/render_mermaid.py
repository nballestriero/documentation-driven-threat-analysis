"""Renderer Mermaid puro: IR + primitive grafiche delle guide; senza accesso RDF."""
from __future__ import annotations
import argparse, base64, hashlib, html, json
from collections import defaultdict
from pathlib import Path
from .catalog import Catalog, RuleError


def id_for(value):
    return 'G_'+hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False).encode('utf-8')).hexdigest()[:14]



def _group_child_identity(item):
    """Unambiguous stable group fingerprint from actual RDF occurrences."""
    if item.get('kind') == 'individual':
        return item['occurrence']
    if item.get('kind') == 'group':
        return _group_id(item)
    if item.get('kind') == 'realization-layout':
        # Each realization has its own RDF occurrence. Without this case,
        # groups containing one realization have a [None] fingerprint:
        # unrelated "Primary Functions" boxes reuse one Mermaid subgraph ID.
        return ['realization-layout', item['function']['occurrence'],
                item['process']['occurrence']]
    return item.get('occurrence', item.get('key'))


def _group_id(group):
    return id_for(['group',group.get('key'),group.get('groupRuleClass'),
                   group.get('group'), [_group_child_identity(x) for x in group.get('children',[])]])


def css(style):
    if not isinstance(style,dict):return ''
    result=[]
    for field,name in [('fill','fill'),('stroke','stroke'),('color','color')]:
        if style.get(field) is not None:result.append(f'{name}:{style[field]}')
    if style.get('strokeWidth') is not None:result.append('stroke-width:'+str(style['strokeWidth'])+'px')
    if style.get('strokePattern')=='dashed':
        result.append('stroke-dasharray:'+str(style.get('dashArray','5 4')))
    if style.get('cornerRadius') is not None:
        result.extend([f'rx:{style["cornerRadius"]}px',f'ry:{style["cornerRadius"]}px'])
    return ','.join(result)


def q(s):
    return json.dumps(str(s),ensure_ascii=False)


def shape(item_type):
    if item_type=='rectangle':return '[',']'
    if item_type=='rounded':return '(',')'  # Mermaid rounded rectangle, not stadium
    raise RuleError(f'Forma Mermaid non supportata dallo standard: {item_type}')


def render(ir, rules:Catalog):
    if ir.get('schema')!='ddta-graph-ir-v2':
        raise RuleError('IR non riconosciuto: atteso ddta-graph-ir-v2')
    ll=rules.global_label['mermaid']['labelTemplate']
    # DDTA-SINGLE-RENDERER-R10: one deterministic final rendering path.
    # The approved R9 experiment used ELK and did not override title margins.
    # Icons, labels and styles still come from the compiled graphical guides.
    mermaid_spec = rules.global_label.get('mermaid', {})
    diagram_init = {
        'htmlLabels': mermaid_spec.get('htmlLabels', True),
        'theme': 'base',
        'layout': 'elk',
    }
    lines = ['%%{init: ' + json.dumps(diagram_init, ensure_ascii=False, separators=(',', ':')) + '}%%', 'flowchart TB']
    to_style=[]; edge_styles=[]; link_idx=0
    occurrence_ids=defaultdict(list)
    ancestor_ids={}
    # Relation placement is computed using the graphical containment tree,
    # not names of RDF individuals or names of CORE classes.  A relation
    # linking siblings belongs inside their closest common subgraph.
    # This prevents presentation-only relation label nodes from floating
    # outside the group that contains both linked individuals.
    occurrence_paths=defaultdict(list)
    buckets=defaultdict(list)
    emitted_edges=set()

    def index_tree(items, parents=()):
        for item in items:
            kind=item['kind']
            if kind=='individual':
                occurrence_paths[item['iri']].append((item['occurrence'], parents))
            if kind in ('group','individual','realization-layout'):
                index_tree(item.get('children',[]), parents+(id(item),))

    index_tree(ir.get('roots',[]))

    def common_container(path_a,path_b):
        common=[]
        for a,b in zip(path_a,path_b):
            if a!=b:break
            common.append(a)
        return common[-1] if common else None, len(common)

    for e in sorted(ir.get('edges',[]),key=lambda x:(x['kind'],x['predicate'],x['source'],x['target'])):
        if e['kind']=='semantic-relation-with-visual-symbol' and (
            e['rdfSubject'],e['rdfObject'],e['predicate']) in ir.get('realizationPlacements',[]):
            # Already represented inside the function/process graphical pair.
            continue
        src_occ=occurrence_paths.get(e['source'],[])
        dst_occ=occurrence_paths.get(e['target'],[])
        if not src_occ or not dst_occ:continue
        pairs=[]
        for s_id,s_path in src_occ:
            for d_id,d_path in dst_occ:
                common, depth=common_container(s_path,d_path)
                pairs.append((depth,s_id,d_id,common))
        # Deepest shared owner first, deterministic tie-break by occurrence IDs.
        depth,s_id,d_id,container = sorted(pairs,key=lambda pair:(-pair[0],pair[1],pair[2]))[0]
        buckets[container].append((e,s_id,d_id))

    def invisible_link(a,b,depth=1):
        """Layout-only Mermaid link; reserve its index so later linkStyle never
        styles a different edge. The link is not a DDTA semantic relation.
        """
        nonlocal link_idx
        lines.append('    '*depth+f'{a} ~~~ {b}')
        edge_styles.append((str(link_idx),'stroke:transparent,stroke-width:0px,opacity:0'))
        link_idx += 1

    def add_style(identifier, style):
        s=css(style)
        if s:to_style.append((identifier,s))

    def svg_embed(related,relpath,source_record):
        if not relpath:return None
        file=rules.icon_path(source_record.get('module'),relpath)
        if not file:
            raise RuleError(f'Icona dichiarata nel catalogo ma mancante: {relpath}')
        data=base64.b64encode(file.read_bytes()).decode('ascii')
        return f'data:image/svg+xml;base64,{data}'

    def style_for(node):
        rec=rules.classes[node['rdfType']]
        st=dict(rec.get('style',{}))
        for conditional in rec.get('conditionalStyles',[]):
            when=conditional['when']; value=node.get('attributes',{}).get(when['property'])
            match = (when['operator']=='equals' and value==when['value'] or
                     when['operator']=='greater-than' and isinstance(value,(int,float)) and value>when['value'])
            if match:
                st.update({k:v for k,v in conditional.items() if k!='when'})
        if node.get('children'):
            corner=rec.get('container',{}).get('cornerRadius')
            if corner is not None:st['cornerRadius']=corner
        return st

    def label_for(node,rec,style):
        stroke=style.get('stroke','#374151')
        label=ll.format(stroke=html.escape(str(stroke)),
                        name=html.escape(node['name'],quote=True),
                        rdfType=html.escape(rec.get('displayType',node['rdfType']),quote=True))
        extra=[]
        role=node.get('role')
        if role:
            # DDTA-COMPACT-HEADER-R1: preserve INPUT/OUTPUT on the *rdfType*
            # line, inside the measured HTML header, never outside its div.
            # Visual role labels are not RDF types or new RDF individuals.
            trailer='</span></div>'
            if label.endswith(trailer):
                label=label[:-len(trailer)]+' · '+html.escape(str(role))+trailer
            else:
                extra.append(role)
        attrs=node.get('attributes',{})
        label_settings=rec.get('label',{})
        if label_settings.get('showDeclaredCardinality'):
            mi=next((v for k,v in attrs.items() if k.endswith(':minOccurs')),None)
            ma=next((v for k,v in attrs.items() if k.endswith(':maxOccurs')),None)
            if mi is not None and ma is not None:extra.append(f'{mi}..{ma}')
            elif mi is not None:extra.append(f'min: {mi}')
            elif ma is not None:extra.append(f'max: {ma}')
        if extra:
            # Keep declared cardinality/supplementary text inside the
            # existing HTML box, so Mermaid can measure the label height.
            additional=''.join(
                "<span style='display:block;text-align:center;font-size:12px'>"
                +html.escape(str(x))+'</span>' for x in extra)
            if label.endswith('</div>'):
                label=label[:-6]+additional+'</div>'
            else:
                label+='<br/>'+additional
        icon=rec.get('icon',{})
        if icon.get('source'):
            data=svg_embed(node,icon['source'],rec)
            label=f"<img src='{data}' width='27' height='27'/>"+label
        elif node.get('children') and rec.get('container',{}).get('icon'):
            key=rec['container']['icon']
            for r in rules.groups.values():
                icon_spec=r.get('icons',{}).get(key)
                if icon_spec and icon_spec.get('svg'):
                    data=svg_embed(node,icon_spec['svg'],r)
                    label=f"<img src='{data}' width='27' height='27'/>"+label
                    break
        return label

    def group_style(g):
        """Resolve group styles declared in a guide, including inherited aliases.

        Class style aliases such as 'environment', 'system' and 'function' are
        obtained from class-style.node.style; they are NOT hard-coded here.
        """
        ref=g.get('styleRef')
        rule=rules.groups.get(g.get('groupRuleClass'),{})
        def inherited_class_style(alias):
            matches=[r for r in rules.classes.values() if r.get('node',{}).get('style')==alias]
            if len(matches)!=1:
                raise RuleError(f'InheritsFrom={alias}: attesa esattamente una class-style con node.style corrispondente, trovate {len(matches)}')
            return dict(matches[0].get('style',{}))
        if isinstance(ref,dict):
            style=dict(ref)
        elif isinstance(ref,str):
            style=dict(rule.get('styles',{}).get(ref,{}))
            if not style:
                raise RuleError(f'Gruppo {g.get("key")}: style {ref} non dichiarato')
        else:
            style={}
        if style.get('inheritsFrom'):
            base=inherited_class_style(style.pop('inheritsFrom'))
            style=dict(base,**style)
        if not style and (rule.get('inheritFunctionContainerStyle') or rule.get('inheritSubclassContainerStyle')):
            source=rules.classes.get(g.get('groupRuleClass'))
            if source:
                style=dict(source.get('style',{}))
        # Pure layout groups not assigned an appearance in the guide must
        # remain unpainted; Mermaid's default black fill is not a new rule.
        if not style:
            style={'fill':'transparent','stroke':'transparent','strokeWidth':0}
        return style

    def group_direction(g):
        rule=rules.groups.get(g.get('groupRuleClass'),{})
        lay=rule.get('layout',{})
        if g.get('key') in lay.get('groupOrder',[]) and lay.get('contractsSideBySide') and g.get('key')==lay['groupOrder'][0]:
            return 'LR'
        return lay.get('direction','TB')

    def line_style(r):
        return r.get('line') if isinstance(r.get('line'),dict) else r.get('representation',{})

    def add_edge(src,dst,rule, label=None, mode='plain'):
        nonlocal link_idx
        ls=line_style(rule)
        label_spec=rule.get('label',{})
        if mode=='semantic-relation-with-visual-symbol':
            rep=rule.get('representation',{})
            # Semantic RDF: Process -> Function, graphical order Function above Process.
            symbol=rep.get('symbolSource')
            ico=id_for([src,dst,rule.get('target'),'symbol'])
            if symbol:
                data=svg_embed(None,symbol,rule)
                h=27
                lines.append(f'    {ico}@{{ img: {q(data)}, h: {h}, constraint: "on" }}')
            else:
                raise RuleError(f'Simbolo SVG mancante in {rule.get("target")}')
            text=label_spec.get('text','')
            labelid=id_for([src,dst,text,'label'])
            lines.append(f'    {labelid}([{q(text)}])')
            # Linee grafiche (non frecce) e simbolo di realizzazione dalla guida.
            lines.append(f'    {dst} --- {labelid} --- {ico} --- {src}')
            style={'fill':label_spec.get('fill','#FFFFFF'),'color':label_spec.get('color','#7B8794'),
                   'stroke':label_spec.get('color','#7B8794'),'strokeWidth':0.5}
            add_style(labelid,style)
            add_style(ico,{'fill':'transparent','stroke':'transparent','strokeWidth':0})
            link_idx += 3
            return
        if label_spec.get('representation')=='rounded-inline-node' or rule.get('representation',{}).get('renderer')=='mermaid-intermediate-label-node':
            txt=label_spec.get('text','') if label is None else label
            mid=id_for([src,dst,rule.get('target'),txt,'intermediate'])
            lines.append(f'    {mid}([{q(txt)}])')
            lines.append(f'    {src} --- {mid} --> {dst}')
            add_style(mid,{k:v for k,v in label_spec.items() if k in ('fill','stroke','color','strokeWidth','cornerRadius','strokePattern')})
            if css(ls): edge_styles.append((f'{link_idx},{link_idx+1}',css(ls)))
            link_idx += 2
        else:
            label = label or label_spec.get('text')
            clause=f'    {src} -->|{label}| {dst}' if label else f'    {src} --> {dst}'
            lines.append(clause)
            if css(ls):edge_styles.append((str(link_idx),css(ls)))
            link_idx += 1

    def projection_edge_rule(edge):
        # All graphical properties of projected communication labels originate
        # in the compiled guide, never in fixed Python color/shape constants.
        rule=edge['rule']
        role_key=edge.get('renderRole')
        if role_key not in ('outputEdge', 'inputEdge'):
            raise RuleError('Proiezione comunicativa priva del ruolo grafico dichiarato')
        expected=rule.get(role_key)
        if not isinstance(expected,dict) or expected.get('label') != edge.get('label'):
            raise RuleError('Proiezione comunicativa: etichetta diversa dal ruolo dichiarato in YAML')
        if expected.get('direction') != 'forward':
            raise RuleError('Proiezione comunicativa: direzione non supportata dalla regola YAML')
        label_style=rule.get('labelStyle')
        if not isinstance(label_style,dict) or label_style.get('representation')!='rounded-inline-node':
            raise RuleError('Proiezione funzionale priva di render.labelStyle (rounded-inline-node)')
        if label_style.get('shape')!='rounded':
            raise RuleError('Etichetta funzionale: shape rounded richiesta dalla guida')
        required=('fill','stroke','color','strokeWidth','cornerRadius')
        missing=[key for key in required if key not in label_style]
        if missing:
            raise RuleError('Etichetta funzionale incompleta: '+', '.join(missing))
        return {'label': dict(label_style, text=edge.get('label')),
                'line': rule.get('line',{})}

    def emit_bucket(container,depth=1):
        # An edge emitted before a Mermaid subgraph is closed is scoped
        # geometrically to that subgraph.  No new RDF relation is asserted.
        for edge,src,dst in buckets.pop(id(container),[]):
            if edge['kind']=='semantic-relation-with-visual-symbol':
                add_edge(src,dst,edge['rule'],mode=edge['kind'])
            elif edge['kind']=='projection-edge':
                r=projection_edge_rule(edge)
                add_edge(src,dst,r,label=edge.get('label'))
            else:
                add_edge(src,dst,edge['rule'])

    def node(node, depth=1):
        prefix='    '*depth
        if node['kind']=='realization-layout':
            rule=node['rule']
            process=node['process']; function=node['function']
            symbol_source=rule['representation'].get('symbolSource')
            if not symbol_source:
                raise RuleError('realizesFunction: symbolSource assente dalla guida')
            uid=id_for(['realization-layout',process['iri'],function['iri'],rule.get('target')])
            lines.append(f'{prefix}subgraph {uid}[{q(" ")}]')
            # Mermaid can ignore nested subgraph directions when a node also
            # participates in an edge leaving the subgraph.  The guide
            # explicitly requests subjectBelowObject: the visual stack must
            # therefore be Function -> symbol -> Process (top to bottom).
            # The upward SVG expresses the RDF realizesFunction direction.
            layout=rule.get('layout',{})
            stack_direction='TB' if layout.get('subjectBelowObject') else node.get('direction','BT')
            lines.append(f'{prefix}    direction {stack_direction}')
            # Follow the guide's three-part schematic: Function, REL_SYMBOL,
            # Process.  The Process stays below the Function in direction BT.
            node_emit(function,depth+1)
            symbol_group=id_for(['realization-symbol-group',process['iri'],function['iri'],rule.get('target')])
            lines.append(f'{prefix}    subgraph {symbol_group}[{q(" ")}]')
            lines.append(f'{prefix}        direction TB')
            icon_id=id_for(['realization-icon',process['iri'],function['iri'],rule.get('target')])
            icon_data=svg_embed(None,symbol_source,rule)
            lines.append(f'{prefix}        {icon_id}@{{ img: {q(icon_data)}, h: 42, constraint: "on" }}')
            add_style(icon_id,{'fill':'transparent','stroke':'transparent','strokeWidth':0})
            caption=rule.get('label',{}).get('text')
            if caption:
                cap_id=id_for(['realization-caption',process['iri'],function['iri'],rule.get('target')])
                lines.append(f'{prefix}        {cap_id}([{q(caption)}])')
                add_style(cap_id,{'fill':rule['label'].get('fill','#FFFFFF'),
                                  'stroke':'transparent','strokeWidth':0,
                                  'color':rule['label'].get('color','#7B8794')})
                invisible_link(icon_id,cap_id,depth+2)
            lines.append(f'{prefix}    end')
            add_style(symbol_group,{'fill':'transparent','stroke':'transparent','strokeWidth':0})
            node_emit(process,depth+1)
            if layout.get('subjectBelowObject'):
                invisible_link(function['occurrence'],symbol_group,depth+1)
                invisible_link(symbol_group,process['occurrence'],depth+1)
            else:
                invisible_link(process['occurrence'],symbol_group,depth+1)
                invisible_link(symbol_group,function['occurrence'],depth+1)
            emit_bucket(node,depth+1)
            lines.append(f'{prefix}end')
            # The neutral outer realization box is presentation-only.
            # The visual style comes from the guide YAML, not from a
            # class-specific Python constant.
            outer_style=layout.get('graphicalContainerStyle')
            if outer_style is not None:
                if not isinstance(outer_style,dict):
                    raise RuleError('graphicalContainerStyle deve essere una mappa YAML')
                add_style(uid,outer_style)
            else:
                add_style(uid,{'fill':'transparent','stroke':'transparent','strokeWidth':0})
            return
        if node['kind']=='group':
            gid=_group_id(node)
            rule=rules.groups.get(node.get('groupRuleClass'),{})
            caption_rule=rule.get('layout',{}).get('resourceGroupCaption',{})
            caption_bottom=bool(node.get('iconKey') and caption_rule.get('position')=='bottom')
            lines.append(f'{prefix}subgraph {gid}[{q(' ' if caption_bottom else node.get('label', ''))}]')
            lines.append(f"{prefix}    direction {visual_plan[gid]['direction']}")
            for child in node.get('children',[]): node_emit(child,depth+1)
            if caption_bottom:
                icon_spec=rule.get('icons',{}).get(node['iconKey'],{})
                label=html.escape(node.get('label',''))
                if icon_spec.get('svg'):
                    data=svg_embed(None,icon_spec['svg'],rule)
                    label=f"<img src='{data}' width='32' height='32'/>"+label
                caption_id=id_for(['caption',gid])
                lines.append(f'{prefix}    {caption_id}[{q(label)}]')
                add_style(caption_id,{'fill':'transparent','stroke':'transparent','strokeWidth':0})
                if node.get('children'):
                    last=node['children'][-1]
                    anchor=last.get('occurrence')
                    if anchor:
                        invisible_link(anchor,caption_id,depth+1)
            emit_bucket(node,depth+1)
            lines.append(f'{prefix}end')
            add_style(gid,visual_plan[gid]['style'])
            return
        nid=node['occurrence']
        occurrence_ids[node['iri']].append(nid)
        rec=rules.classes[node['rdfType']]
        planned=visual_plan[nid]
        style=planned['style']
        label=planned['label']
        if node.get('children'):
            container=rec.get('container',{})
            if container.get('renderer') != 'mermaid-subgraph':
                raise RuleError(f'Contenitore non definito per {node["rdfType"]}')
            lines.append(f'{prefix}subgraph {nid}[{q(label)}]')
            # Direction from grouped-relations-style if present, otherwise from class container.
            gr=rules.group_rule(node['rdfType'])
            direction=planned['direction']
            lines.append(f'{prefix}    direction {direction}')
            for child in node['children']:node_emit(child,depth+1)
            emit_bucket(node,depth+1)
            lines.append(f'{prefix}end')
        else:
            op,cl=shape(rec.get('node',{}).get('shape','rounded'))
            lines.append(f'{prefix}{nid}{op}{q(label)}{cl}')
        add_style(nid,style)

    def node_emit(item,depth=1):
        if item['kind']=='group':node(item,depth)
        else:node(item,depth)

    # DDTA-SINGLE-RENDERER-R10 -- GLOBAL GRAPHICAL PLANNING PASS.
    # project_view.project() has already constructed the entire graph: no
    # Mermaid is emitted until all individuals/groups have a resolved visual
    # label, real guide icon, declared style and child direction.
    visual_plan = {}
    def prepare_visual_plan(items):
        for item in items:
            kind = item['kind']
            if kind == 'individual':
                rid = item['occurrence']
                record = rules.classes[item['rdfType']]
                styling = style_for(item)
                graphical_group = rules.group_rule(item['rdfType'])
                direction = ((graphical_group.get('layout', {}).get('direction') if graphical_group else None)
                             or record.get('layout', {}).get('childrenDirection', 'TB'))
                visual_plan[rid] = {
                    'label': label_for(item, record, styling),
                    'style': styling,
                    'direction': direction,
                }
            elif kind == 'group':
                rid = _group_id(item)
                visual_plan[rid] = {'style': group_style(item), 'direction': group_direction(item)}
            # realization-layout has a declared graphical structure handled
            # by the existing renderer; its Function/Process children are
            # planned here before any Mermaid output is emitted.
            prepare_visual_plan(item.get('children', []))

    prepare_visual_plan(ir.get('roots', []))
    if any(item.get('kind') == 'individual' and item['occurrence'] not in visual_plan
           for item in ir.get('roots', [])):
        raise RuleError('Piano grafico incompleto')

    for root in ir.get('roots',[]):node_emit(root)
    # Cross-container edges are intentionally global.  Edges that share a
    # graphical parent were already emitted inside that parent by emit_bucket.
    for edge,src,dst in buckets.pop(None,[]):
        if edge['kind']=='semantic-relation-with-visual-symbol':
            add_edge(src,dst,edge['rule'],mode=edge['kind'])
        elif edge['kind']=='projection-edge':
            r=projection_edge_rule(edge)
            add_edge(src,dst,r,label=edge.get('label'))
        else:
            add_edge(src,dst,edge['rule'])
    if buckets:
        raise RuleError(f'Archiviazione archi non completata: {len(buckets)} contenitori')
    # DDTA-SINGLE-RENDERER-R10 -- classDef/class, generated only from
    # actual YAML-derived style values. Group by exact CSS declarations;
    # no fixed CORE class names/colors or additional graphical relations.
    styles_by_css = defaultdict(set)
    last_style = {}
    for node_id, declaration in to_style:
        # Preserve the original renderer's last-declaration-wins semantics.
        last_style[node_id] = declaration
    for node_id, declaration in last_style.items():
        styles_by_css[declaration].add(node_id)
    for declaration, ids in sorted(styles_by_css.items()):
        cls = 'DDTA_C_' + hashlib.sha256(declaration.encode('utf-8')).hexdigest()[:12]
        lines.append(f'    classDef {cls} {declaration}')
        lines.append(f'    class {",".join(sorted(ids))} {cls}')
    for idx,st in edge_styles:
        lines.append(f'    linkStyle {idx} {st}')
    # A Mermaid subgraph ID denotes one graphical container. Duplicates
    # silently merge different systems in ELK; fail closed instead.
    subgraph_ids = [line.strip().split()[1].split('[')[0]
                    for line in lines if line.lstrip().startswith('subgraph ')]
    if len(set(subgraph_ids)) != len(subgraph_ids):
        counts = defaultdict(int)
        for identifier in subgraph_ids:
            counts[identifier] += 1
        duplicates = sorted(k for k, n in counts.items() if n > 1)
        raise RuleError('Identificativi Mermaid subgraph duplicati: ' + ', '.join(duplicates))
    return '\n'.join(lines)+'\n'


def main(argv=None):
    ap=argparse.ArgumentParser(description='Renderizza IR JSON con sole primitive e colori dichiarati nelle guide YAML.')
    ap.add_argument('--projection',type=Path,required=True,help='IR JSON')
    ap.add_argument('--rules',type=Path,nargs='+',required=True,help='YAML compilati')
    ap.add_argument('--out-dir',type=Path,required=True,help='Cartella per graph.mmd e graph.md')
    args=ap.parse_args(argv)
    ir=json.loads(args.projection.read_text(encoding='utf-8'))
    mmd=render(ir,Catalog(args.rules))
    args.out_dir.mkdir(parents=True,exist_ok=True)
    (args.out_dir/'graph.mmd').write_text(mmd,encoding='utf-8',newline='\n')
    (args.out_dir/'graph.md').write_text('```mermaid\n'+mmd+'```\n',encoding='utf-8',newline='\n')
    print(f'Grafico Mermaid -> {args.out_dir}')
    return 0

if __name__=='__main__':raise SystemExit(main())
