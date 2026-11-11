#!/usr/bin/env python3
"""Render Diffie-Hellman candidate instance sheets and Mermaid views from model/dh_r5a.ttl.
This renders the current case, not a general DDTA process renderer.
Requires: pip install rdflib. Does not alter the TTL.
"""
from collections import defaultdict
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS

HERE=Path(__file__).resolve().parent.parent
OUT=HERE/'generated'
OUT.mkdir(exist_ok=True)
g=Graph().parse(str(HERE/'model/dh_r5a.ttl'),format='turtle')
D=Namespace('https://w3id.org/ddta/core#')
P=Namespace('https://w3id.org/ddta/process#')
DH=Namespace('https://example.org/ddta/dh-deterministic-r4#')
V=Namespace('https://example.org/ddta/view#')

def n(x):return str(x).split('#')[-1]
def lab(s):return str(g.value(s,RDFS.label) or n(s)).replace('|','/')
def things(*types):
    return sorted(set(s for t in types for s in g.subjects(RDF.type,t)),key=n)
def vals(s,p):return sorted(set(g.objects(s,p)),key=n)
def ns(s,p):return ', '.join('`'+n(o)+'`' for o in vals(s,p))
def ce(s):return vals(s,D.hasContractElement)
def elements_for(f,p):return sorted(set(e for c in vals(f,p) for e in ce(c)),key=n)
def mdcode(s):return '`'+n(s)+'`'
def link_fn(fn,relation):
    contracts=vals(fn,relation)
    if not contracts:return '—'
    return '; '.join('`'+n(c)+'` → '+', '.join('`'+n(e)+'`' for e in ce(c)) for c in contracts)

def make_sheets():
    a=['# DDTA Diffie-Hellman — schede delle istanze RDF, R5A', '',
       '> **GENERATO dal Turtle, non normativo.** Modificare `model/dh_r5a.ttl`, quindi rigenerare con `python tools/render_case.py`. Non inserire in questa scheda relazioni che non figurano nel grafo.','',
       '## 1. Schede architetturali', '']
    groups=[('Environment',D.Environment),('System',D.System),('Boundary',D.Boundary),('Resource',D.Resource),('CommunicationChannel',D.CommunicationChannel)]
    rel=[('hasOperationalEnvironment',D.hasOperationalEnvironment),('hasPrimaryFunction',D.hasPrimaryFunction),('hasBoundary',D.hasBoundary),('makesAvailable',D.makesAvailable),('encloses',D.encloses),('hasSource',D.hasSource),('hasDestination',D.hasDestination)]
    for title,typ in groups:
        a += ['### '+title,'']
        for node in things(typ):
            a += ['#### '+n(node), '',f'- **Classe:** `{n(typ)}`',f'- **Etichetta:** {lab(node)}']
            for r,p in rel:
                if vals(node,p):a+=['- **'+r+'**: '+ns(node,p)]
            a+=['']
    a+=['## 2. Schede Function: input, output e gerarchia', '']
    for f in things(D.Function,D.CommunicationFunction):
        a+=['### '+n(f),'',f'- **Classe:** `{n(next(g.objects(f,RDF.type)))}`',f'- **Etichetta:** {lab(f)}']
        parents=sorted(g.subjects(D.hasSubFunction,f),key=n)
        if parents:a+=['- **Sottofunzione di:** '+', '.join(map(mdcode,parents))]
        if vals(f,D.hasSubFunction):a+=['- **hasSubFunction:** '+ns(f,D.hasSubFunction)]
        if vals(f,D.mustPrecede):a+=['- **mustPrecede:** '+ns(f,D.mustPrecede)]
        if vals(f,D.usesChannel):a+=['- **usesChannel:** '+ns(f,D.usesChannel)]
        if vals(f,V.communicationRole):a+=['- **Ruolo comunicazione (viz, ausiliario):** '+', '.join(str(x) for x in vals(f,V.communicationRole))]
        a+=['- **hasInputContract:** '+link_fn(f,D.hasInputContract),'- **hasOutputContract:** '+link_fn(f,D.hasOutputContract),'']
    a+=['## 3. Schede Contract', '']
    for c in things(D.Contract):
        a+=['### '+n(c),'', '- **Classe:** `Contract`', '- **Definizione:** '+str(g.value(c,RDFS.comment) or 'Non specificata'), '- **Usato in input da:** '+(', '.join(map(mdcode,sorted(g.subjects(D.hasInputContract,c),key=n))) or '—'),
            '- **Usato in output da:** '+(', '.join(map(mdcode,sorted(g.subjects(D.hasOutputContract,c),key=n))) or '—'),
            '- **hasContractElement:** '+(', '.join(map(mdcode,ce(c))) or '—'),'']
    a+=['## 4. Schede ContractElement e cardinalità','','| Elemento | Significato | Definizione | minOccurs | maxOccurs |','|---|---|---|---:|---:|']
    for e in things(D.ContractElement):
        mi=g.value(e,D.minOccurs);ma=g.value(e,D.maxOccurs)
        a.append(f'| `{n(e)}` | {lab(e)} | {str(g.value(e,RDFS.comment) or "—").replace(chr(124),chr(47))} | {mi if mi is not None else "?"} | {ma if ma is not None else "?"} |')
    a+=['','## 5. Schede Process e sottoprocessi','']
    for pr in things(D.Process):
        a+=['### '+n(pr),'', '- **realizesFunction:** '+(ns_for(pr,D.realizesFunction)),
             '- **hasSubProcess (candidata approvata):** '+ns_for(pr,P.hasSubProcess),
             '- **hasStep:** '+ns_for(pr,D.hasStep),
             '- **hasTransition (Process):** '+ns_for(pr,P.hasTransition),'']
    a+=['## 6. Schede Step, ControlNode, condizioni e gap','','> Le righe `?` sono `viz:DocumentationGap`, non `ProcessStep`.','']
    for step in things(D.ProcessStep,P.ControlNode):
        owners=sorted(g.subjects(D.hasStep,step),key=n)
        a+=['### '+n(step),'', '- **Classe:** '+(', '.join('`'+n(t)+'`' for t in vals(step,RDF.type))),'- **Etichetta:** '+lab(step),
             '- **Process owner:** '+', '.join(map(mdcode,owners)),
             '- **invokesProcess (candidata):** '+ns_for(step,P.invokesProcess),
             '- **controlKind:** '+', '.join(str(x) for x in vals(step,P.controlKind)) if vals(step,P.controlKind) else '- **controlKind:** —',
             '- **gap ramo negativo:** '+ns_for(step,V.unresolvedFalseBranch),'']
    for cond in things(P.AtomicCondition):
        a+=['### '+n(cond),'','- **Classe:** `AtomicCondition`','- **leftOperand:** '+ns_for(cond,P.leftOperand)]
        for op in vals(cond,P.leftOperand):a+=['- **referencesContractElement:** '+ns_for(op,P.referencesContractElement)]
        a+=['']
    for gap in things(V.DocumentationGap):
        a+=['### '+n(gap),'', '- **Classe:** `viz:DocumentationGap` (ausiliaria, non ProcessStep)',
             '- **Etichetta:** '+lab(gap),'']
    a+=['## 7. Schede ProcessTransition (ordine locale e guardie)','',
         '| Transizione | Processo | Da Step | A Step | Guardia | Valore atteso (viz) |',
         '|---|---|---|---|---|---|']
    for t in things(P.ProcessTransition):
        own=sorted(g.subjects(P.hasTransition,t),key=n)
        a.append('| '+ ' | '.join('`'+x+'`' if x!='—' else x for x in [n(t),n(own[0]) if len(own)==1 else '—',
                 n(vals(t,P.fromStep)[0]) if len(vals(t,P.fromStep))==1 else '—',
                 n(vals(t,P.toStep)[0]) if len(vals(t,P.toStep))==1 else '—',
                 ','.join(map(n,vals(t,P.hasGuard))) or '—',
                 ','.join(str(v) for v in vals(t,V.guardExpected)) or '—'])+' |')
    a+=['', '**Nota sulle denominazioni:** non si deduce causalità da un nome di classe o di individuo. L’ordine dichiarato è quello delle `ProcessTransition` nel Turtle.']
    (HERE/'DDTA_DH_INSTANCE_SHEETS_R1.md').write_text('\n'.join(a)+'\n',encoding='utf-8')

def ns_for(s,p):return ', '.join(map(mdcode,vals(s,p))) or '—'

def safe_label(s):return lab(s).replace('"', "'").replace('\n',' ')

def save_mermaid(file,lines,title):
    mmd='\n'.join(lines)+'\n'
    (OUT/(file+'.mmd')).write_text(mmd,encoding='utf-8')
    (OUT/(file+'.md')).write_text(f'# {title}\n\nFonte: `../model/dh_r5a.ttl`. Schema illustrativo generato da relazioni RDF.\n\n```mermaid\n{mmd}```\n',encoding='utf-8')

def diagrams():
    # Architecture via CORE properties; directionality comes from hasSource/hasDestination.
    lines=['flowchart LR']
    for s in things(D.System,D.Environment,D.Boundary,D.Resource,D.CommunicationChannel):
        lines.append(f'    {n(s)}["{n(s)}<br/>{n(next(g.objects(s,RDF.type)))}"]')
    for s in things(D.System,D.Environment,D.Boundary,D.CommunicationChannel):
        for p in (D.hasOperationalEnvironment,D.hasBoundary,D.makesAvailable,D.encloses,D.hasSource,D.hasDestination):
            for o in vals(s,p):lines.append(f'    {n(s)} -->|"{n(p)}"| {n(o)}')
    save_mermaid('architecture',lines,'Architettura CORE e confini di trust')
    lines=['flowchart TB']
    for f in things(D.Function,D.CommunicationFunction):lines.append(f'    {n(f)}["{n(f)}<br/>{"CommunicationFunction" if (f,RDF.type,D.CommunicationFunction) in g else "Function"}"]')
    for f in things(D.Function,D.CommunicationFunction):
        for child in vals(f,D.hasSubFunction):lines.append(f'    {n(f)} -->|"hasSubFunction"| {n(child)}')
    save_mermaid('function_tree',lines,'Decomposizione funzionale')
    for who in ('PC','User'):
        proc=DH[who+'Process'];steps=vals(proc,D.hasStep)
        lines=['flowchart TB']
        for s in steps:
            kind='ControlNode' if (s,RDF.type,P.ControlNode) in g else 'ProcessStep'
            sub=vals(s,P.invokesProcess)
            f=vals(sub[0],D.realizesFunction) if len(sub)==1 else []
            txt=n(s)+'<br/>'+kind+('<br/>→ '+n(f[0]) if len(f)==1 else '')
            if kind=='ControlNode':lines.append(f'    {n(s)}{{"{txt}"}}')
            else:lines.append(f'    {n(s)}["{txt}"]')
        for t in vals(proc,P.hasTransition):
            fr=vals(t,P.fromStep);to=vals(t,P.toStep)
            if len(fr)!=1 or len(to)!=1:raise ValueError('Malformed transition '+n(t))
            guard=vals(t,P.hasGuard)
            label=('guard: '+n(guard[0])) if guard else ''
            lines.append(f'    {n(fr[0])} -->'+(f'|"{label}"|' if label else '')+f' {n(to[0])}')
        for s in steps:
            for gap in vals(s,V.unresolvedFalseBranch):
                lines.append(f'    {n(gap)}(("?"))')
                lines.append(f'    {n(s)} -.->|"false: non documentato"| {n(gap)}')
                lines.append(f'    style {n(gap)} stroke:#dc2626,stroke-width:2px,stroke-dasharray:5 4,fill:#fff1f1,color:#b91c1c')
        save_mermaid(who+'_process',lines,who+'Process: Step e condizioni')

def trace():
    out=['# Traccia locale ricostruita dalle transizioni R5A','',
       '> Generata dal Turtle, non dall’ordine alfabetico, da `viz:localOrder` o da un evento runtime. Rappresenta il solo percorso nominale con i gap negativi dichiarati.','',
       '| Processo | N. locale | Step | Tipo | Sottoprocesso → Function | Input | Output | Guardia/gap |',
       '|---|---:|---|---|---|---|---|---|']
    for who in ('PC','User'):
        proc=DH[who+'Process'];steps=set(vals(proc,D.hasStep));initial=vals(proc,V.initialStep)
        if len(initial)!=1:raise ValueError('Initial step count not 1')
        succ=defaultdict(list)
        for t in vals(proc,P.hasTransition):
            fr=vals(t,P.fromStep);to=vals(t,P.toStep)
            if len(fr)!=1 or len(to)!=1 or fr[0] not in steps or to[0] not in steps:raise ValueError('PRC-TRANS-01')
            succ[fr[0]].append((t,to[0]))
        st=initial[0];seen=set();i=0
        while st:
            if st in seen:raise ValueError('Cycle; cannot use linear renderer')
            seen.add(st);i+=1
            sp=vals(st,P.invokesProcess)
            fn=vals(sp[0],D.realizesFunction) if len(sp)==1 else []
            if fn and len(fn)!=1:raise ValueError('Ambiguous sub-function')
            f=fn[0] if fn else None
            outs=succ.get(st,[])
            if len(outs)>1:raise ValueError('Multiple nominal branches unsupported')
            guard=(', '.join(n(c) for c in vals(outs[0][0],P.hasGuard))) if outs else '—'
            gaps=vals(st,V.unresolvedFalseBranch)
            note=('guard='+guard if guard!='—' else '') + (' / ❓ gap='+','.join(n(x) for x in gaps) if gaps else '')
            values=[who+'Process',str(i),n(st),'ControlNode' if (st,RDF.type,P.ControlNode) in g else 'ProcessStep',
                    (n(sp[0])+' → '+n(f)) if f else '—',
                    ', '.join(map(n,elements_for(f,D.hasInputContract))) if f else '—',
                    ', '.join(map(n,elements_for(f,D.hasOutputContract))) if f else '—',note or '—']
            out.append('| '+' | '.join(z.replace('|','/') for z in values)+' |')
            st=outs[0][1] if outs else None
        if seen!=steps:raise ValueError('Disconnected steps')
    out+=['','La tabella non implica precedenza obbligatoria fra PC e User. I messaggi si associano attraverso canali e contratti condivisi.','']
    (OUT/'steps_from_rdf.md').write_text('\n'.join(out),encoding='utf-8')

if __name__=='__main__':
    make_sheets();diagrams();trace()
    print('OK: RDF triples',len(g),'15 function sheets / 28 contracts; views regenerated')
