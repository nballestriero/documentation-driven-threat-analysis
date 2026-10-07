from pathlib import Path
import re, subprocess, html

ROOT = Path(__file__).resolve().parent

PALETTE = {
    'core': ('#FFFFFF', '#3D637C'),
    'env': ('#FFFDF6', '#B18A22'),
    'part': ('#F4FAFE', '#5C99C1'),
    'profile': ('#F4FBF7', '#4F8B68'),
}
TEXT='#23313D'; MUTED='#66788A'; GREEN='#2F7E58'; BLUE='#4E7195'; MR_BG='#E9F4FE'; MR_BORDER='#73AED6';

def q(s):
    return '"' + s.replace('\\','\\\\').replace('"','\\"') + '"'

def parse_mmd(path):
    text=path.read_text(encoding='utf-8')
    nodes={}; edges=[]; classmap={};
    node_re=re.compile(r'^\s*([A-Za-z0-9_]+)\["(.*)"\]\s*$')
    edge_re=re.compile(r'^\s*([A-Za-z0-9_]+)\s+(-\.->|-->)\|"(.*)"\|\s+([A-Za-z0-9_]+)\s*$')
    class_re=re.compile(r'class\s+([^;]+?)\s+([A-Za-z0-9_]+);')
    for line in text.splitlines():
        m=node_re.match(line)
        if m:
            nodes[m.group(1)] = m.group(2).replace('\\n','\n')
            continue
        m=edge_re.match(line)
        if m:
            edges.append((m.group(1),m.group(2),m.group(3).replace('\\n','\n'),m.group(4)))
            continue
        for m in class_re.finditer(line):
            cls=m.group(2)
            for nid in [x.strip() for x in m.group(1).split(',')]:
                classmap[nid]=cls
    return text,nodes,edges,classmap

def html_label(label, title_size=18, sub_size=11):
    lines=label.split('\n')
    title=html.escape(lines[0])
    rest='<BR/>'.join(html.escape(x) for x in lines[1:])
    if rest:
        return f'''<<TABLE BORDER="0" CELLBORDER="0" CELLPADDING="4"><TR><TD><FONT POINT-SIZE="{title_size}"><B>{title}</B></FONT></TD></TR><TR><TD><FONT POINT-SIZE="{sub_size}" COLOR="{MUTED}">{rest}</FONT></TD></TR></TABLE>>'''
    return f'<<FONT POINT-SIZE="{title_size}"><B>{title}</B></FONT>>'

def edge_attrs(label, dashed=False, color=GREEN):
    parts=label.split('\n')
    op=html.escape(parts[0]); sub='<BR/>'.join(html.escape(x) for x in parts[1:])
    second = f'<TR><TD><FONT POINT-SIZE="9" COLOR="{MUTED}">{sub}</FONT></TD></TR>' if sub else ''
    lab=f'''<<TABLE BORDER="0" CELLBORDER="0" CELLPADDING="1"><TR><TD><FONT POINT-SIZE="11" COLOR="{color}"><B>{op}</B></FONT></TD></TR>{second}</TABLE>>'''
    return f'label={lab}, color="{color}", fontcolor="{color}", penwidth=2.2, arrowsize=0.8' + (', style="dashed"' if dashed else '')

def make_dot(level, nodes, edges, classmap):
    # Graphviz is used only as a deterministic vector renderer. Topology and labels come from Mermaid.
    lines=['digraph G {', 'graph [rankdir=LR, compound=true, bgcolor="#F5F8FB", pad="0.28", nodesep="0.65", ranksep="1.0", splines=ortho, outputorder=edgesfirst];',
           'node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=12, margin="0.18,0.12", penwidth=1.8];',
           'edge [fontname="Helvetica", fontsize=10];']
    # helper
    def ndecl(nid, label, cls=None):
        fill,stroke=PALETTE.get(cls,PALETTE['core'])
        width='3.6' if nid in ('DT','EP','PROC') else ('3.2' if nid=='HCP' else '2.6')
        return f'{nid} [label={html_label(label, 18 if nid in ("DT","EP","PROC","HCP") else 14, 10)}, fillcolor="{fill}", color="{stroke}", fontcolor="{TEXT}", width={width}, height=1.05];'
    # outer MR cluster
    lines += ['subgraph cluster_MRC6 {', f'label={q("MR-C6 - Predisposizione e inizializzazione dell ambiente DermaTriage")};',
              f'color="{MR_BORDER}"; fillcolor="{MR_BG}"; style="rounded,filled"; penwidth=1.8; fontsize=16; fontname="Helvetica-Bold"; fontcolor="#2D6A93"; margin=26;']
    for nid in ('DT','EP','PROC'):
        if nid in nodes: lines.append(ndecl(nid,nodes[nid],classmap.get(nid)))
    # Keep left-side top-level referents stacked in one rank/column.
    lines.append('{rank=same; DT; EP; PROC;}')
    lines.append('DT -> EP [style=invis, weight=30]; EP -> PROC [style=invis, weight=30];')
    if level==0:
        lines.append(ndecl('ENV',nodes['ENV'],classmap.get('ENV')))
        target='ENV'; cluster_target=None
        lines.append('{rank=same; ENV;}')
    else:
        # ENV is a semantic whole represented by a nested cluster; parts are derived from Mermaid node declarations.
        lines += ['subgraph cluster_ENV {', f'label={html_label("DermaTriageEnvironment\\nBAReferent - execution environment / whole",20,10)};',
                  f'color="{PALETTE["env"][1]}"; fillcolor="{PALETTE["env"][0]}"; style="rounded,filled"; penwidth=1.8; margin=24;']
        # invisible anchor is rendering-only and is not a BAReferent.
        lines.append('ENV_ANCHOR [shape=point, width=0.01, height=0.01, label="", style=invis];')
        for nid in ('CR','SC','MR','DR','EC'):
            if nid in nodes: lines.append(ndecl(nid,nodes[nid],classmap.get(nid)))
        # two-column internal arrangement without semantic edges
        lines += ['{rank=same; CR; MR; EC;}', '{rank=same; SC; DR;}',
                  'CR -> MR -> EC [style=invis, weight=20];', 'SC -> DR [style=invis, weight=20];',
                  'CR -> SC [style=invis, weight=10];', 'MR -> DR [style=invis, weight=10];',
                  'ENV_ANCHOR -> CR [style=invis, weight=1];', '}']
        target='ENV_ANCHOR'; cluster_target='cluster_ENV'
        if level==2 and 'HCP' in nodes:
            lines.append(ndecl('HCP',nodes['HCP'],classmap.get('HCP')))
            lines.append('{rank=same; ENV_ANCHOR; HCP;}')
            lines.append('ENV_ANCHOR -> HCP [style=invis, weight=5];')
    # semantic edges are taken from Mermaid, with cluster target substitution for ENV in G1/G2.
    for src,etype,label,dst in edges:
        dashed = etype=='-.->'
        color = BLUE if label.startswith('realize') or label.startswith('constrain') else GREEN
        s=src; d=dst; extra=''
        if level>0 and dst=='ENV':
            d=target; extra=', lhead=cluster_ENV'
        attrs=edge_attrs(label,dashed,color)
        # constrain is intentionally value/profile -> target, matching the accepted graph grammar.
        lines.append(f'{s} -> {d} [{attrs}{extra}];')
    lines.append('}')
    lines.append('}')
    return '\n'.join(lines)

for level in (0,1,2):
    mmd=ROOT/f'MRC6_G{level}_R2.mmd'
    text,nodes,edges,classmap=parse_mmd(mmd)
    dot=make_dot(level,nodes,edges,classmap)
    dotpath=ROOT/f'MRC6_G{level}_R2.dot'
    dotpath.write_text(dot,encoding='utf-8')
    for fmt in ('pdf','svg'):
        out=ROOT/f'MRC6_G{level}_R2.{fmt}'
        subprocess.run(['dot',f'-T{fmt}',str(dotpath),'-o',str(out)],check=True)
    print(level, 'nodes', sorted(nodes), 'edges', edges)
