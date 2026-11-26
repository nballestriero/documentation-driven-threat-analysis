"""Semantic CORE+PROCESS Mermaid composition by shared RDF identities.

No Turtle mutation, no source-specific label knowledge, no copying expected Mermaid.
The CORE renderer owns System/Function/Process placement; PROCESS adds
Step/ControlNode content inside the CORE Process occurrence. Unresolved
identities are errors, never floating replacement nodes.
"""
from __future__ import annotations
import collections
import hashlib
import yaml
import json
import re
from pathlib import Path


def _process_sid(iri):
    import hashlib
    return 'PX_'+hashlib.sha256(str(iri).encode('utf-8')).hexdigest()[:12]


def _edges_from(line):
    l=line.strip()
    if l.startswith(('class ', 'classDef ', 'style ', 'subgraph ', 'flowchart ', 'direction ', 'linkStyle ', '%%')):
        return 0
    return len(re.findall(r'~~~|-->|---|-\.->',l))


def _edge_occurrences(lines):
    counts=collections.Counter()
    result=[]
    for line in lines:
        base=line.strip()
        for _ in range(_edges_from(line)):
            order=counts[base]
            result.append((base,order))
            counts[base]+=1
    return result


def _split_styles(lines):
    i=next((i for i,line in enumerate(lines) if line.strip().startswith('classDef ')),len(lines))
    prefix,tail=lines[:i],lines[i:]
    styles=[line for line in tail if line.strip() and not line.strip().startswith('linkStyle ')]
    links=[line for line in tail if line.strip().startswith('linkStyle ')]
    return prefix,styles,links


def _map_styles(styles,edges):
    out={}
    for line in styles:
        hit=re.match(r'^\s*linkStyle\s+([\d,]+)\s+(.*)$',line)
        if not hit:raise ValueError('Unexpected linkStyle: '+line)
        for idx in hit.group(1).split(','):
            idx=int(idx)
            if idx>=len(edges):raise ValueError('linkStyle outside edge range')
            out[edges[idx]]=hit.group(2)
    return out


def _replace_ids(line,translation):
    for prev,current in translation.items():
        line=re.sub(r'\b'+re.escape(prev)+r'\b',current,line)
    return line


def _blocks(lines,ids):
    """Find balanced process subgraphs, preserving the renderer's source text."""
    blocks={};occupied=set()
    for pid in ids:
        matching=[i for i,line in enumerate(lines) if re.match(r'^\s*subgraph\s+'+re.escape(pid)+r'\[',line)]
        if len(matching)!=1:raise ValueError('Composed Process missing/duplicated in PROCESS: '+pid)
        begin=matching[0];level=0
        for end in range(begin,len(lines)):
            value=lines[end].strip()
            if value.startswith('subgraph '):level+=1
            elif value=='end':level-=1
            if level==0:break
        else:raise ValueError('Unbalanced Process container: '+pid)
        if occupied.intersection(range(begin,end+1)):raise ValueError('Overlapping process definitions')
        occupied.update(range(begin,end+1));blocks[pid]=lines[begin:end+1]
    return blocks,occupied


def compose_integrated(core_mmd,process_fragment,ir,diag,core_guide=None):
    """Splice PROCESS structure into CORE Process occurrences, preserve links.

    Requires the CORE graph to be rendered from the internal projection that
    retains ddta:Process and ddta:realizesFunction, but delegates Steps to PROCESS.
    """
    core=Path(core_mmd)
    source=core.read_text(encoding='utf-8')
    if source.count('flowchart TB')!=1:raise ValueError('Expected unique CORE flowchart')
    if 'ddta:ProcessStep' in source:raise ValueError('CORE view still owns ProcessStep')
    projection=core.with_name('04_projection.json')
    if not projection.is_file():raise ValueError('CORE occurrence IR missing for integrated composition')
    occurrences=json.loads(projection.read_text(encoding='utf-8')).get('occurrences',{})
    process_specs={p['iri']:p for p in ir['processes']}
    realization_processes={p['process'] for p in ir['realizations']}
    if not realization_processes.issubset(process_specs):raise ValueError('Missing realized Process in IR')
    mapped={}
    for iri,p in sorted(process_specs.items()):
        matched=occurrences.get(iri,[])
        if len(matched)!=1:
            raise ValueError(f'Expected one CORE occurrence of {iri}: found {len(matched)}')
        mapped[_process_sid(iri)]=matched[0]['id']
    full_blocks=[_process_sid(p['iri']) for p in process_specs.values() if p['steps']]
    core_body,core_styles,core_links=_split_styles(source.rstrip('\n').splitlines())
    fragment_body,fragment_styles,_=_split_styles(process_fragment.rstrip('\n').splitlines())
    process_blocks,consumed=_blocks(fragment_body,full_blocks)
    replace_map={mapped[proc_id]:[_replace_ids(line,mapped) for line in block]
                 for proc_id,block in process_blocks.items()}
    # A Process lacking its own Steps already exists as a normal CORE occurrence.
    # It must never be recreated as an unparented PROCESS node.
    other=[]
    for idx,line in enumerate(fragment_body):
        if idx in consumed:continue
        if any(re.match(r'^\s*'+re.escape(pid)+r'\[',line) for pid in mapped):continue
        other.append(_replace_ids(line,mapped))
    composed=[];inserted=set()
    for line in core_body:
        hit=re.match(r'^(\s*)(O_[a-f0-9]+)\(',line)
        if hit and hit.group(2) in replace_map:
            rid=hit.group(2);inserted.add(rid)
            # Align nested indentation to the CORE occurrence; never move
            # the Process outside its System/Function container.
            indent=len(hit.group(1))
            for part in replace_map[rid]:
                leading=len(part)-len(part.lstrip());composed.append(' '*(indent+leading-4)+part.lstrip())
        else:composed.append(line)
    if inserted != set(replace_map):raise ValueError('CORE Process placeholders not found')
    composed.extend(other)
    # The original CORE class already styles Process occurrences, including the
    # shared IDs now representing subgraphs.  PROCESS-specific classes apply
    # only to internal Steps/conditions/edges, not duplicate Process containers.
    extra_styles=[line for line in fragment_styles if not
                  (line.strip().startswith('class ') and line.strip().endswith(' PROC_process'))]
    # Once PROCESS supplies visible Steps, a CORE ddta:Process occurrence is
    # a container, not the leaf Process that existed in the ownership view.
    # Its style is computed from the existing CORE class-style YAML.
    if core_guide and replace_map:
        guide_text=Path(core_guide).read_text(encoding='utf-8')
        rules=[yaml.safe_load(x) for x in re.findall(r'```yaml ddta-visualization\s*\n(.*?)\n```', guide_text,re.S)]
        process_rules=[r for r in rules if isinstance(r,dict) and r.get('record')=='class-style' and r.get('target')=='ddta:Process']
        if len(process_rules)!=1:raise ValueError('Expected one CORE ddta:Process style')
        rule=process_rules[0]
        from ddta_viz.render_mermaid import css
        simple_css=css(rule['style'])
        container_css=css({**rule['style'],'cornerRadius':rule['container']['cornerRadius']})
        def class_id(value):return 'DDTA_C_'+hashlib.sha256(value.encode('utf-8')).hexdigest()[:12]
        leaf_id=class_id(simple_css)
        container_id=class_id(container_css)
        replaced=False
        updated=[]
        for line in core_styles:
            m=re.match(r'^\s*class\s+([A-Za-z0-9_,]+)\s+'+re.escape(leaf_id)+r'$',line)
            if m:
                ids=m.group(1).split(',')
                remaining=[x for x in ids if x not in replace_map]
                if remaining:updated.append('    class '+','.join(remaining)+' '+leaf_id)
                replaced=True
                updated.append('    classDef '+container_id+' '+container_css)
                updated.append('    class '+','.join(sorted(set(ids)&set(replace_map)))+' '+container_id)
                continue
            updated.append(line)
        if not replaced:raise ValueError('Composed CORE Process style not found')
        core_styles=updated

    original_core_edges=_edge_occurrences(core_body)
    original_process_edges=_edge_occurrences(fragment_body)
    core_edge_styles=_map_styles(core_links,original_core_edges)
    proc_edge_styles={}
    for spec in diag.get('processLinkStylesRelative',[]):
        idx,color=spec[:2]
        details=spec[2] if len(spec)>2 else 'stroke-width:2.5px'
        if idx>=len(original_process_edges):raise ValueError('PROCESS styled edge out of range')
        key=original_process_edges[idx]
        proc_edge_styles[(_replace_ids(key[0],mapped),key[1])]='stroke:'+color+','+details
    out_edges=_edge_occurrences(composed)
    final_pos={edge:i for i,edge in enumerate(out_edges)}
    missing=set(core_edge_styles|proc_edge_styles)-set(final_pos)
    if missing:raise ValueError('Styled links lost: '+repr(sorted(missing)[:5]))
    # Preserve the two original styling orders.  CORE groups its adjacent
    # indices into a single directive, PROCESS records individual link styles.
    relink=[]
    for line in core_links:
        m=re.match(r'^\s*linkStyle\s+([\d,]+)\s+(.*)$',line)
        if not m:raise ValueError('Bad CORE linkStyle: '+line)
        locations=[final_pos[original_core_edges[int(k)]] for k in m.group(1).split(',')]
        relink.append('    linkStyle '+','.join(map(str,locations))+' '+m.group(2))
    for spec in diag.get('processLinkStylesRelative',[]):
        idx,color=spec[:2]
        details=spec[2] if len(spec)>2 else 'stroke-width:2.5px'
        edge=original_process_edges[idx]
        mapped_key=(_replace_ids(edge[0],mapped),edge[1])
        if color=='#7B8794' and diag.get('omitNeutralInvocationLinkStyle',False):
            # Avoid redundant Mermaid linkStyle for the standard invocation connector.
            continue
        relink.append(f'    linkStyle {final_pos[mapped_key]} stroke:{color},{details}')
    return '\n'.join(composed+core_styles+extra_styles+relink)+'\n'
