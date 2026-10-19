#!/usr/bin/env python3
"""DDTA temporal PoC. Standard library only. Experimental Markdown schema, not canonical BA."""
import argparse, json, re, hashlib
from collections import defaultdict
from pathlib import Path

BLOCK=re.compile(r'```ba-temporal-json\s*(\{.*?\})\s*```',re.S)
PATTERN=re.compile(r"^SELECT\s+(?P<mode>HISTORY|NEIGHBORHOOD\s+(?P<hops>[1-3])|AT\s+'(?P<at>[^']+)')\s+FROM\s+BA\s+WHERE\s+REFERENT\s*=\s*'(?P<focus>[^']+)'\s*;?$",re.I)
class QueryError(ValueError):pass

def indices(items):
    out={}
    for i in items:
        if i['id'] in out:raise QueryError('Identita duplicata: '+i['id'])
        out[i['id']]=i
    return out

def closure(edges,nodes):
    adj={n:set() for n in nodes}
    for x,y in edges:adj[x].add(y)
    out={}
    for x in nodes:
        seen=set();stack=list(adj[x])
        while stack:
            y=stack.pop()
            if y not in seen:seen.add(y);stack.extend(adj[y])
        out[x]=seen
    return out

def validate(d):
    if d.get('schema')!='ba-temporal-poc/dermatriage-weights-1':raise QueryError('schema non supportato')
    ref=indices(d['referents']);versions=indices(d['versions']);contexts=indices(d['contexts']);props=indices(d['propositions']);occ=indices(d['occurrences']);facts=indices(d['temporalFacts'])
    for version in versions.values():
        if version['family'] not in ref:raise QueryError('famiglia mancante')
    for x,y in d['precedes']+d['overlaps']:
        if x not in contexts or y not in contexts or x==y:raise QueryError('tempo non valido')
    c=closure(d['precedes'],contexts)
    if any(x in c[x] for x in contexts):raise QueryError('ciclo di precedenza')
    for x,y in d['overlaps']:
        if y in c[x] or x in c[y]:raise QueryError('sovrapposizione impossibile')
    presence=set()
    for p in d['presence']:
        if p['subject'] not in ref and p['subject'] not in versions:raise QueryError('presenza subject inesistente')
        for t in p['contexts']:
            if t not in contexts or (p['subject'],t) in presence:raise QueryError('presenza invalida/duplicata')
            presence.add((p['subject'],t))
    required={'transfer':{'source','destination','content'},'produce':{'actor','input','result'},'hasPart':{'whole','part'},'realize':{'abstract','realization'}}
    for p in props.values():
        op=p['semanticOperatorKey'];keys=set(p['roles']);allowed=required.get(op)
        if allowed is None or not allowed<=keys or keys-allowed>({'behavior'} if op=='transfer' else set()):raise QueryError('Ruoli BA invalidi: '+p['id'])
        if any(x not in ref for x in p['roles'].values()):raise QueryError('BAReferent mancante '+p['id'])
        if p['status'] not in ('ACCEPTED','CANDIDATE'):raise QueryError('status non valido')
    for o in occ.values():
        if o['context'] not in contexts or o['proposition'] not in props:raise QueryError('occ invalid')
        p=props[o['proposition']]
        for role,v in o['version_bindings'].items():
            if role not in p['roles'] or v not in versions or p['roles'][role]!=versions[v]['family']:raise QueryError('version binding invalid')
            if (v,o['context']) not in presence:raise QueryError('versione vincolata senza presenza attestata')
    for f in facts.values():
        if f['subject'] not in ref or f['context'] not in contexts or not f['source']:raise QueryError('fact or evidence invalid')
    return True

def load(path):
    raw=Path(path).read_text(encoding='utf-8'); blocks=BLOCK.findall(raw)
    if len(blocks)!=1:raise QueryError('esattamente un blocco Markdown ba-temporal-json richiesto')
    d=json.loads(blocks[0]);validate(d);return d

def present(d,focus,ctx):
    if any(p['subject']==focus and ctx in p['contexts'] for p in d['presence']):return 'PRESENT (attestato nella vista)'
    if any(v['family']==focus and any(p['subject']==v['id'] and ctx in p['contexts'] for p in d['presence']) for v in d['versions']):return 'PRESENT (derivato dalla presenza di una versione)'
    return 'UNKNOWN (non e assenza)'

def related(d,focus):
    versions=indices(d['versions']); props=indices(d['propositions'])
    if focus not in indices(d['referents']) and focus not in versions:raise QueryError('focus sconosciuto')
    return [(o,props[o['proposition']]) for o in d['occurrences'] if (focus in o['version_bindings'].values() if focus in versions else focus in props[o['proposition']]['roles'].values())]

def nearby(d,focus,hops):
    if focus in indices(d['versions']):raise QueryError('NEIGHBORHOOD su versione non supportato')
    related(d,focus)
    frontier={focus};seen={focus};out=[];covered=set()
    for hop in range(1,hops+1):
        more=set()
        for p in d['propositions']:
            roles=set(p['roles'].values())
            if roles & frontier:
                if p['id'] not in covered:out.append((hop,p));covered.add(p['id'])
                more.update(roles-seen)
        seen|=more;frontier=more
    return out

def query(d,sql):
    m=PATTERN.fullmatch(sql.strip())
    if not m:raise QueryError('sintassi query non riconosciuta')
    focus=m.group('focus');items=related(d,focus);contexts=indices(d['contexts']);props=indices(d['propositions']);mode=m.group('mode').upper()
    out=['# Risultato BA temporale — `'+focus+'`','', '`'+sql.strip()+'`','',
         '> **Ricostruzione di progetto, non execution log.** Temporal facts non sono BAProposition; le fasi future non sono eventi avvenuti.','']
    if mode.startswith('NEIGHBORHOOD'):
        out+=['## Incidenza BA: direzioni e ruoli, non causalita automatica','']
        for hop,p in nearby(d,focus,int(m.group('hops'))):
            out+=['### Hop '+str(hop)+' · '+p['id']+' ['+p['status']+']','- '+p['semanticOperatorKey']+' : '+', '.join(k+'='+v for k,v in p['roles'].items())]
            for o in d['occurrences']:
                if o['proposition']==p['id']:out.append('  - Occorrenza `'+o['id']+'` a `'+o['context']+'` ('+o['mode']+')')
        out+=['','Un hop per proposition e una proiezione di adiacenza, non un transfer implicito.']
    else:
        if mode.startswith('AT'):
            times=[m.group('at')]
            if times[0] not in contexts:raise QueryError('contesto sconosciuto')
        else:times=list(contexts)
        out+=['## Ordine parziale esplicito','- precedes: '+', '.join('`'+a+'` → `'+b+'`' for a,b in d['precedes']),'- overlaps attestati: '+(', '.join(str(x) for x in d['overlaps']) if d['overlaps'] else 'nessuno; non implica che le fasi siano seriali'),'']
        for t in times:
            out+=['## '+t+' — '+contexts[t]['label'],'','**Esistenza:** '+present(d,focus,t),'']
            these=[(o,p) for o,p in items if o['context']==t]
            if these:
                out.append('**BAProposition con partecipazione diretta:**')
                for o,p in these:
                    out.append('- `'+o['id']+'` · `'+p['id']+'` ['+p['status']+'] '+p['semanticOperatorKey']+' ('+o['mode']+'): '+', '.join(k+'='+v for k,v in p['roles'].items())+(' · binding '+str(o['version_bindings']) if o['version_bindings'] else ''))
            else:out.append('- Nessuna BAProposition diretta qui: non significa assenza di comportamento.')
            those=[f for f in d['temporalFacts'] if f['subject']==focus and f['context']==t]
            if those:
                out+=['','**Contesto documentale collegato all’identita (non BAProposition):**']
                for f in those:out+=['- `'+f['id']+'` ['+f['category']+'] '+f['claim']+'  ','  Fonte: '+f['source']]
            out.append('')
        if focus in [v['family'] for v in d['versions']]:
            out+=['### Versioni riconosciute',*['- '+v['id']+' — '+v['note'] for v in d['versions'] if v['family']==focus],'- Nessuna versione candidata di retraining e attestata nella prova.']
    return '\n'.join(out)+'\n'


# R2: discovery and query-dependent projection. Never derive new BAPropositions.
DISCOVERY=re.compile(r'^SHOW\s+REFERENTS\s+FROM\s+BA\s*;?$', re.I)
DESCRIBE=re.compile(r"^DESCRIBE\s+REFERENT\s+'(?P<focus>[^']+)'\s*;?$",re.I)

def dispatch(d, sql):
    sql=sql.strip()
    if DISCOVERY.fullmatch(sql):
        counts=defaultdict(set)
        for p in d['propositions']:
            for ref in p['roles'].values(): counts[ref].add(p['id'])
        lines=['# Catalogo BAReferent — PoC R2','','Il conteggio indica le BAProposition **nel dataset sperimentale**, non nell’intero repository DDTA.','','| BAReferent | Kind | BAProposition |','|---|---|---:|']
        lines += [f"| `{r['id']}` | `{r['kind']}` | {len(counts[r['id']])} |" for r in sorted(d['referents'],key=lambda r:r['id'].lower())]
        lines+=['','Esempio: `DESCRIBE REFERENT \'EfficientNetB4WeightsArtifact\';`']
        return '\n'.join(lines)+'\n',None
    md=DESCRIBE.fullmatch(sql)
    if md:
        focus=md.group('focus')
        ref=indices(d['referents'])
        if focus not in ref: raise QueryError('BAReferent non presente: '+focus)
        props=[p for p in d['propositions'] if focus in p['roles'].values()]
        occurrences=[o for o in d['occurrences'] if o['proposition'] in {p['id'] for p in props}]
        facts=[f for f in d['temporalFacts'] if f['subject']==focus]
        lines=[f'# DESCRIBE REFERENT `{focus}`','',f"Kind: `{ref[focus]['kind']}`",'',f'BAProposition incidenti: **{len(props)}** (universo PoC R2)','', '| BAProposition | Operatore | Ruolo/i | Stato |','|---|---|---|---|']
        lines += [f"| `{p['id']}` | `{p['semanticOperatorKey']}` | {', '.join(k for k,v in p['roles'].items() if v==focus)} | {p['status']} |" for p in props]
        lines+=['','## Partecipazioni temporali esplicite','']
        if occurrences:
            lines += [f"- `{o['context']}`: `{o['id']}` ⇒ `{o['proposition']}` [{o['mode']}]" for o in occurrences]
        else:lines+=['- Nessuna occorrenza diretta nel campione.']
        lines+=['','## Fatti temporali contestuali (non BAProposition)','']
        lines += [f"- `{f['context']}` · `{f['id']}`: {f['claim']}" for f in facts] or ['- Nessuno']
        lines+=['','Questa descrizione non prova identità byte-level, causalità o esecuzioni avvenute.']
        return '\n'.join(lines)+'\n',None
    match=PATTERN.fullmatch(sql)
    if not match:raise QueryError('Query non riconosciuta. Supportate SHOW REFERENTS, DESCRIBE REFERENT, SELECT HISTORY/AT/NEIGHBORHOOD.')
    return query(d,sql),match

def select_propositions(d,match,max_nodes=25):
    focus=match.group('focus')
    if focus not in indices(d['referents']):raise QueryError('La proiezione grafica richiede un BAReferent; versione non supportata per questa vista')
    mode=match.group('mode').upper()
    if mode.startswith('NEIGHBORHOOD'):
        ordered=[(p,hop) for hop,p in nearby(d,focus,int(match.group('hops')))]
    elif mode.startswith('AT'):
        ctx=match.group('at')
        if ctx not in indices(d['contexts']):raise QueryError('contesto inesistente: '+ctx)
        pids={o['proposition'] for o in d['occurrences'] if o['context']==ctx}
        ordered=[(p,1) for p in d['propositions'] if p['id'] in pids and focus in p['roles'].values()]
    else:
        ordered=[(p,1) for p in d['propositions'] if focus in p['roles'].values()]
    if max_nodes<1:raise QueryError('max_nodes deve essere >=1')
    included=[]; excluded=[]; seen={focus}
    for p,hop in ordered:
        refs=set(p['roles'].values())
        if len(seen|refs)>max_nodes:excluded.append((p,'MAX_NODES: proposition non inclusa parzialmente'))
        else:included.append((p,hop));seen|=refs
    return included,excluded,seen

def ident(s):
    return re.sub('[^A-Za-z0-9_]','_',s)

def esc(s):
    return str(s).replace('&','&amp;').replace('"','&quot;').replace('<','&lt;').replace('>','&gt;')

def projection(d,match,max_nodes=25):
    """Project BA propositions with EXACT graph idioms borrowed from C7_FR07_01_GRAPH_R50.mmd.

    This reads the selected BA propositions from the structured Markdown source,
    not from an existing Mermaid diagram.  No layout helper is a BA proposition.
    """
    focus=match.group('focus')
    included,excluded,used=select_propositions(d,match,max_nodes)
    refs=indices(d['referents'])
    lines=[];edges=[]
    frame_on=False
    def add(x):
        # An explicitly white layout-only frame preserves black produce edges
        # in the VS Code preview, independently of the editor's dark theme.
        # The frame MUST NOT be interpreted as hasPart or a BA boundary.
        if frame_on and x.startswith('    '): x='  '+x
        lines.append(x)
    def edge(txt,operator):add('    '+txt);edges.append(operator)
    # Profile B: user-verified document icons and white viewing surface.
    add('%%{init: {"theme":"base","themeVariables":{"background":"#FFFFFF","lineColor":"#171717","edgeLabelBackground":"#FFFFFF"}}}%%')
    add('')
    add('flowchart LR')
    add('')
    add('    %% Selected from structured BA Markdown: source is NOT the cumulative Mermaid.')
    add('    %% Profile B (verified in VS Code): R3 document icons, R50 actor/edge classes.')
    add('    %% BA_VIEW_WHITE is visual-only: not hasPart and not a trust boundary.')
    add('    subgraph BA_VIEW_WHITE["BA view — layout only"]')
    frame_on=True
    add('    direction LR')
    id_of=lambda x:'R_'+ident(x)
    by_whole=defaultdict(list)
    for prop,hop in included:
        if prop['semanticOperatorKey']=='hasPart':by_whole[prop['roles']['whole']].append(prop)
    # A visual label may show a proposition ID but MUST NOT change the BA identity.
    annotations=defaultdict(list)
    for prop,hop in included:
        op=prop['semanticOperatorKey'];roles=prop['roles']
        if op=='produce':annotations[roles['actor']].append(prop['id'])
        elif op=='realize':annotations[roles['realization']].append(prop['id'])
    def node(ref,nid=None,indent='    ',occurrence=False):
        nid=nid or id_of(ref)
        kind=refs[ref]['kind']
        label=esc(ref)
        if occurrence:
            label+="<br/><span style='font-size:8px'>same BAReferent / view occurrence</span>"
        else:
            for pid in annotations[ref]:
                color='#FFFFFF' if kind in ('actor','activity','candidate-activity','realization') else '#17324D'
                label+="<br/><span style='font-size:7px;color:"+color+"'>"+esc(pid)+"</span>"
        # Shape conventions tested successfully by the user in diagnostic B:
        # artifact/content=doc, actor=rounded, store=cylinder, realization=box.
        if kind=='store':return indent+nid+'[("'+label+'")]'
        if kind in ('actor','activity','candidate-actor','candidate-activity','behavior'):return indent+nid+'("'+label+'")'
        if kind in ('content','candidate-content'):return indent+nid+'@{ shape: doc, label: "'+label+'" }'
        return indent+nid+'["'+label+'"]'
    placed=set()
    for whole,props in by_whole.items():
        add('    subgraph HP_'+ident(whole)+'["'+esc(whole)+' — hasPart (semantic frame)"]')
        add('        direction TB')
        add(node(whole,indent='        '));placed.add(whole)
        for prop in props:
            part=prop['roles']['part']
            add(node(part,nid='O_'+ident(prop['id']),indent='        ',occurrence=True))
        add('    end')
    for ref in sorted(used):
        if ref not in placed:
            add(node(ref));placed.add(ref)
    if focus not in placed:add(node(focus))
    add('')
    # A proposition contributes its complete role pattern. Record edge index at insertion.
    for prop,hop in included:
        op=prop['semanticOperatorKey'];r=prop['roles'];pid=prop['id']
        tag=esc(pid)+(' / CANDIDATE' if prop['status']=='CANDIDATE' else '')
        if op=='hasPart':continue
        if op=='transfer':
            # Cumulative R50 labels the first edge, and keeps the destination role an edge target.
            edge(id_of(r['source'])+' -->|"transfer<br/>'+tag+'"| '+id_of(r['content']),op)
            edge(id_of(r['content'])+' --> '+id_of(r['destination']),op)
            if 'behavior' in r:
                edge(id_of(r['behavior'])+' -.-|"behavior role / projection only"| '+id_of(r['content']),'view')
        elif op=='produce':
            edge(id_of(r['input'])+' --> '+id_of(r['actor']),op)
            edge(id_of(r['actor'])+' -->|"produce<br/>'+tag+'"| '+id_of(r['result']),op)
        elif op=='realize':
            edge(id_of(r['realization'])+' -.->|realize| '+id_of(r['abstract']),op)
        else:raise QueryError('operatore non supportato dal renderer: '+op)
    frame_on=False
    add('    end')
    add('')
    # The user chose the B profile: R3 document icons + R50-like classes.
    add('    classDef BAProduceActor fill:#212121,stroke:#000000,stroke-width:2px,color:#FFFFFF;')
    add('    classDef BARealizationD2 fill:#8F9295,stroke:#4C5054,stroke-width:2px,color:#FFFFFF;')
    add('    classDef BAStore fill:#EEF4F9,stroke:#275D86,stroke-width:2px,color:#17324D;')
    add('    classDef BAContent fill:#FFFFFF,stroke:#275D86,stroke-width:2px,color:#17324D;')
    add('    classDef BALogicalData fill:#FFFFFF,stroke:#5C99C1,stroke-width:2px,color:#23313D;')
    add('    classDef BATransferBehavior fill:#FFF4E3,stroke:#A96A16,stroke-width:2px,color:#17324D;')
    add('    classDef BAGap fill:#FFFFFF,stroke:#C62828,stroke-width:3px,color:#C62828;')
    add('    style BA_VIEW_WHITE fill:#FFFFFF,stroke:#D4DCE3,stroke-width:1px,color:#17324D;')
    assigned=defaultdict(list)
    # A repeated visual occurrence must have the same BAContent style as its
    # canonical referent, without creating another BA identity.
    for whole,part_props in by_whole.items():
        for prop in part_props:
            part=prop['roles']['part']
            cls='BAContent' if refs[part]['kind'] in ('content','candidate-content') else 'BALogicalData'
            assigned[cls].append('O_'+ident(prop['id']))
    for ref in sorted(used):
        kind=refs[ref]['kind']
        cls='BAStore' if kind=='store' else ('BAContent' if kind in ('content','candidate-content') else ('BARealizationD2' if kind=='realization' else ('BATransferBehavior' if kind=='behavior' else 'BAProduceActor')))
        assigned[cls].append(id_of(ref))
    for cls,ids in assigned.items():add('    class '+','.join(ids)+' '+cls+';')
    for whole,props in by_whole.items():
        external=refs[whole].get('boundary')=='EXTERNAL'
        add('    style HP_'+ident(whole)+(' fill:#FFF8F8,stroke:#C62828,stroke-width:3px,stroke-dasharray:7 5,color:#8B1A1A;' if external else ' fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D;'))
    for i,op in enumerate(edges):
        style={'transfer':'stroke:#0047B3,stroke-width:2px','produce':'stroke:#171717,stroke-width:3px','realize':'stroke:#5F6368,stroke-width:2px,stroke-dasharray:6 4','view':'stroke:#909090,stroke-width:1.3px,stroke-dasharray:3 5'}[op]
        add(f'    linkStyle {i} {style};')
    return '\n'.join(lines)+'\n',edges,included,excluded,used

def temporal_projection(d, match):
    """Metadata-only time diagram, independent of the BA graph."""
    focus=match.group('focus')
    contextual={f['context'] for f in d['temporalFacts'] if f['subject']==focus}
    contextual|={ctx for p in d['presence'] if p['subject']==focus or any(v['family']==focus and v['id']==p['subject'] for v in d['versions']) for ctx in p['contexts']}
    for o in d['occurrences']:
        prop=next((p for p in d['propositions'] if p['id']==o['proposition']),None)
        if prop and focus in prop['roles'].values(): contextual.add(o['context'])
    if match.group('at'): contextual={match.group('at')}
    times=[c for c in d['contexts'] if c['id'] in contextual]
    lines=['flowchart LR','  %% Pure temporal metadata; NO edges here are BAPropositions.']
    for c in times:
        state='PRESENT' if present(d,focus,c['id']).startswith('PRESENT') else 'UNKNOWN'
        lines.append('  TC_'+ident(c['id'])+'["'+esc(c['id'])+' / '+state+' / '+esc(c['kind'])+'"]')
    tset={c['id'] for c in times}
    for a,b in d['precedes']:
        if a in tset and b in tset:
            lines.append('  TC_'+ident(a)+' -.->|"precedes / NON BA"| TC_'+ident(b))
    lines.append('  classDef BATemporalView fill:#F5F6F8,stroke:#8B949E,stroke-width:1.5px,stroke-dasharray:3 3,color:#40464E;')
    if times: lines.append('  class '+','.join('TC_'+ident(c['id']) for c in times)+' BATemporalView;')
    return '\n'.join(lines)+'\n'

def mmd_report(d,match,sql,max_nodes=25):
    mmd,edges,included,excluded,used=projection(d,match,max_nodes)
    focus=match.group('focus');context_map=indices(d['contexts']);occ=defaultdict(list)
    for o in d['occurrences']:occ[o['proposition']].append(o)
    md=[f'# DermaTriage — proiezione BA dinamica · `{focus}`','',f'Query: `{sql}`','',
        '> **PoC R2, non modifica della BA canonica.** Una proposition è inclusa solo se compare nei dati BA selezionati. Il diagramma non afferma la realizzazione di un evento operativo. Le relazioni mancanti non vengono inventate.','',
        f'**{len(included)} BAProposition incluse · {len(used)} BAReferent canonici coinvolti · {len(edges)} archi grafici (compresi eventuali helper di ruolo) · {len(excluded)} proposition escluse per limite.**','',
        '```mermaid',mmd.rstrip(),'```','','## Tempo logico — diagramma SEPARATO, metadati non BA','', 'Il seguente grafo rappresenta solo i contesti e le precedenze documentate: non è connesso alla topologia BA perché non sono BAProposition.','', '```mermaid',temporal_projection(d,match).rstrip(),'```','','## Perché questi elementi sono inclusi','',
        '| BAProposition | Selezione | Semantica e ruoli | Stato | Contesti di occorrenza | Fonte BA |','|---|---|---|---|---|---|']
    for p,hop in included:
        roles=', '.join(f'{k}: `{v}`' for k,v in p['roles'].items())
        contexts=', '.join(sorted({o['context']+' ('+o['mode']+')' for o in occ[p['id']]})) or 'Non identificato nel campione'
        md.append(f"| `{p['id']}` | {'diretta' if hop==1 else 'espansione hop '+str(hop)} | **{p['semanticOperatorKey']}** · {roles} | {p['status']} | {contexts} | {p.get('origin','—')} |")
    if not included:md.append('| — | — | Nessuna proposition diretta selezionata | — | — | — |')
    md+=['','**Regola di completezza:** tutti i ruoli di ciascuna BAProposition inclusa sono rappresentati; le ripetizioni grafiche entro i frame `hasPart` non rappresentano nuove identità BA.','',
         '## Relazioni non incluse','']
    if excluded:
        for p,reason in excluded:md.append(f"- `{p['id']}`: {reason}")
    else:md.append('- Nessuna proposition scartata per il limite di nodi.')
    chosen={p['id'] for p,h in included}
    unselected=[p for p in d['propositions'] if p['id'] not in chosen and p['id'] not in {p['id'] for p,r in excluded}]
    for p in unselected:
        md.append(f"- `{p['id']}`: non raggiunta dai criteri della query (focus / hop / contesto).")
    md+=['**Assenza dalla vista ≠ assenza dalla BA.**','',
         '## Tempo logico e informazioni contestuali','',
         'I contesti qui sotto qualificano occorrenze o fatti documentali: **non sono edges BA inventati**. `precedes` descrive solo l’ordine parziale esplicitato nel campione.','',
         '- Precedenze dichiarate: '+', '.join('`'+a+'` → `'+b+'`' for a,b in d['precedes'])+'.',
         '- Sovrapposizioni dichiarate: '+(', '.join('`'+x+'`/`'+y+'`' for x,y in d['overlaps']) if d['overlaps'] else 'nessuna (non implica serialità)')+'.','',
         '| Contesto | Esistenza focus | Fatto contestuale specifico (NON BAProposition) | Fonte |','|---|---|---|---|']
    for c in d['contexts']:
        fs=[f for f in d['temporalFacts'] if f['subject']==focus and f['context']==c['id']]
        md.append(f"| `{c['id']}` | {present(d,focus,c['id'])} | "+('<ul>'+''.join('<li>'+esc(f['id']+' ['+f['category']+']: '+f['claim'])+'</li>' for f in fs)+'</ul>' if fs else '—')+' | '+('; '.join(esc(f['source']) for f in fs) if fs else '—')+' |')
    md+=['','## Interpretazione e limiti','',
         '- La selezione usa la co-partecipazione ai ruoli di una **BAProposition intera**, non un percorso di causalità automatico.','- Il grafo non collega automaticamente pesi, modello e retraining quando manca la BAProposition corrispondente.','- `produce` è la coppia di frecce nere continue `input -> actor -> result`, con BAProposition ID sull’arco actor -> result secondo lo stile del cumulativo R50; `realize` è la freccia grigia tratteggiata con etichetta realize. Gli archi `produce`, `transfer` e `realize` corrispondono a proposition selezionate; `hasPart` viene mostrato come frame. Gli archi grigi `precedes / NON BA` nel pannello temporale sono metadati di ordine logico, **non** BAProposition; l’eventuale arco grigio `behavior role / projection only` è un helper di visualizzazione.','- L’esistenza `UNKNOWN` indica che non ci sono prove sufficienti in questo dataset, non che l’elemento sia assente.','- Le versioni logiche non certificano uguaglianza crittografica fra copie di file.','']
    return mmd,'\n'.join(md)+'\n'

def slugify(s):
    s=re.sub('[^A-Za-z0-9_-]','_',s)
    return s[:95]

def run_cli():
    cli=argparse.ArgumentParser(description='BA temporal PoC R2 ICONS_R1. SQL-like su Markdown e proiezione Mermaid per focus.')
    cli.add_argument('--source',default=str(Path(__file__).with_name('CASO_DERMATRIAGE_PESI.md')))
    cli.add_argument('--query',default="SHOW REFERENTS FROM BA;")
    cli.add_argument('--out',default=None)
    cli.add_argument('--mermaid',action='store_true')
    cli.add_argument('--max-nodes',type=int,default=25)
    args=cli.parse_args();d=load(args.source); result,match=dispatch(d,args.query)
    if args.out:
        out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
        if match:
            name=slugify(match.group('focus'))+'_'+('AT_'+slugify(match.group('at')) if match.group('at') else 'NEIGHBORHOOD_'+match.group('hops') if match.group('hops') else 'HISTORY')
        else:name='REFERENTS_CATALOG' if DISCOVERY.fullmatch(args.query.strip()) else 'DESCRIBE_'+slugify(DESCRIBE.fullmatch(args.query.strip()).group('focus'))
        (out/(name+'_RESULT_R2_ICONS_R1.md')).write_text(result,encoding='utf-8')
        if args.mermaid:
            if match is None:raise QueryError('Mermaid disponibile solo per le SELECT su un BAReferent')
            mmd,md=mmd_report(d,match,args.query,args.max_nodes)
            (out/(name+'_VIEW_R2_ICONS_R1.mmd')).write_text(mmd,encoding='utf-8')
            (out/(name+'_TIME_R2_ICONS_R1.mmd')).write_text(temporal_projection(d,match),encoding='utf-8')
            (out/(name+'_VIEW_R2_ICONS_R1.md')).write_text(md,encoding='utf-8')
            print('Mermaid:',name,'archi:',sum(x.strip().startswith('linkStyle ') for x in mmd.splitlines()),'file:',out)
        else:print('Risultato:',out/(name+'_RESULT_R2_ICONS_R1.md'))
    else:
        print(result)
        if args.mermaid:raise QueryError('Specifica --out per generare i Mermaid')

if __name__=='__main__':run_cli()
