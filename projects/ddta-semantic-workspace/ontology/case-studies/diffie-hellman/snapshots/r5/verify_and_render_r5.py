#!/usr/bin/env python3
"""Read dh_r5.ttl as the sole source for contract checks, tables and Mermaid.
No functional contents are embedded here. The source Turtle is never modified.
"""
from __future__ import annotations
import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS, Literal, URIRef

HERE=Path(__file__).resolve().parent
D=Namespace('https://w3id.org/ddta/core#')
PROC=Namespace('https://w3id.org/ddta/process#')
V=Namespace('https://example.org/ddta/view#')

def n(x):return str(x).rsplit('#',1)[-1]
def strings(g,s,p):return [str(x) for x in g.objects(s,p)]
def label(g,x):return next((str(v) for v in g.objects(x,RDFS.label)),n(x))
def it_comment(g,x):return '; '.join(str(z) for z in g.objects(x,RDFS.comment))
def allf(g):return set(g.subjects(RDF.type,D.Function))|set(g.subjects(RDF.type,D.CommunicationFunction))
def elem(g,c):return sorted(g.objects(c,D.hasContractElement),key=n)
def contracts(g,f,role):
    return sorted(g.objects(f,D.hasInputContract if role=='input' else D.hasOutputContract),key=n)

def check(g):
    problems=[]
    funs=allf(g)
    conts=set(g.subjects(RDF.type,D.Contract))
    for f in funs:
        for role in ('input','output'):
            cs=contracts(g,f,role)
            if len(cs)!=1:problems.append(f'{n(f)}: expected 1 {role} Contract, got {len(cs)}')
            for c in cs:
                if c not in conts:problems.append(f'{n(f)}: {n(c)} not typed Contract')
                if not elem(g,c):problems.append(f'{n(c)} has no ContractElement')
    for c in conts:
        if not list(g.subjects(D.hasInputContract,c)) and not list(g.subjects(D.hasOutputContract,c)):
            problems.append(f'unused Contract {n(c)}')
        for e in elem(g,c):
            if (e,RDF.type,D.ContractElement) not in g:
                problems.append(f'{n(e)} missing ContractElement type')
            mins=list(g.objects(e,D.minOccurs));maxs=list(g.objects(e,D.maxOccurs))
            if len(mins)!=1 or len(maxs)!=1:
                problems.append(f'{n(e)} cardinality absent or multiple')
            elif int(mins[0])>int(maxs[0]):
                problems.append(f'{n(e)} violates min<=max')
    # For the adopted case: exchanges are identified by shared contracts, not by
    # hardcoded channel or contract names. The two communication directions must
    # have unambiguous sender/receiver roles and same CommunicationChannel.
    comm=set(g.subjects(RDF.type,D.CommunicationFunction))
    sends={f for f in comm if (f,V.communicationRole,Literal('send')) in g}
    recvs={f for f in comm if (f,V.communicationRole,Literal('receive')) in g}
    if len(comm)!=len(sends|recvs) or sends&recvs:
        problems.append('communication role missing or ambiguous')
    exchanges=[]
    for sender in sends:
        for contract in contracts(g,sender,'output'):
            matches=[receiver for receiver in recvs if contract in contracts(g,receiver,'input')]
            if len(matches)!=1:
                problems.append(f'{n(sender)}: ambiguous receiver for shared {n(contract)}')
                continue
            receiver=matches[0]
            sch=set(g.objects(sender,D.usesChannel));rch=set(g.objects(receiver,D.usesChannel))
            if len(sch)!=1 or sch!=rch:
                problems.append(f'{n(sender)} and {n(receiver)} channel mismatch')
                continue
            channel=next(iter(sch))
            src=list(g.objects(channel,D.hasSource));dst=list(g.objects(channel,D.hasDestination))
            if len(src)!=1 or len(dst)!=1:
                problems.append(f'channel {n(channel)} must have one source/destination')
            else:
                for ep in src+dst:
                    enclosing=list(g.subjects(D.encloses,ep))
                    if not enclosing:problems.append(f'{n(ep)} missing Boundary')
            exchanges.append((sender,receiver,channel,contract))
    # Confirm that each receiving CommunicationFunction receives a sender's
    # shared output contract: no guessed pairing.
    for receiver in recvs:
        for contract in contracts(g,receiver,'input'):
            matches=[sender for sender in sends if contract in contracts(g,sender,'output')]
            if len(matches)!=1:problems.append(f'{n(receiver)}: ambiguous sender for {n(contract)}')
    # Case-specific semantic safety and provenance checks (not CORE generic rule).
    byid={n(f):f for f in funs}
    def exact(fn,role,expected):
        if fn not in byid:return
        seen={n(e) for c in contracts(g,byid[fn],role) for e in elem(g,c)}
        if seen!=set(expected):problems.append(f'{fn} {role}: {seen} != {set(expected)}')
    exact('PCCalculatePublic','input', ['PrivateA','ModulusP','GeneratorG'])
    exact('UserCalculatePublic','input', ['PrivateB','ModulusP','GeneratorG'])
    exact('PCDeriveSecret','input', ['PrivateA','AcceptedBRequired','ModulusP'])
    exact('UserDeriveSecret','input', ['PrivateB','AcceptedARequired','ModulusP'])
    exact('PCValidatePublic','output',['ValidityB','AcceptedBOptional'])
    exact('UserValidatePublic','output',['ValidityA','AcceptedAOptional'])
    for sender,receiver,ch,c in exchanges:
        content={n(e) for e in elem(g,c)}
        if content&{'PrivateA','PrivateB','EnteredB','SharedKPC','SharedKUser'}:
            problems.append(f'SECURITY: secret/private declared on communication contract {n(c)}')
        if len(content)!=1:problems.append(f'{n(c)} does not define one public value')
    return sorted(set(problems)),funs,conts,exchanges


def mermaid_id(x):return 'x_'+''.join(ch if ch.isalnum() else '_' for ch in n(x))
def mermaid_text(x):return str(x).replace('"',"'").replace('<','(').replace('>',')')
def contract_summary(g,functions,sysnode=None):
    lines=['flowchart TB']
    done=set()
    def put(uri,typ,txt):
        if uri in done:return
        done.add(uri)
        lines.append(f'    {mermaid_id(uri)}["{mermaid_text(txt)}<br/>{typ}"]')
    if sysnode:
        put(sysnode,'System',label(g,sysnode))
    for fn in functions:
        put(fn,'Function',label(g,fn))
        for role in ('input','output'):
            for c in contracts(g,fn,role):
                es=', '.join(label(g,e) for e in elem(g,c))
                put(c,'Contract',n(c)+'<br/>'+es)
                lines.append(f'    {mermaid_id(fn)} -->|"has{role.title()}Contract"| {mermaid_id(c)}')
    if sysnode:
        prim=list(g.objects(sysnode,D.hasPrimaryFunction))
        for pf in prim:
            lines.append(f'    {mermaid_id(sysnode)} -->|"hasPrimaryFunction"| {mermaid_id(pf)}')
    for fn in functions:
        for sf in g.objects(fn,D.hasSubFunction):
            if sf in functions:lines.append(f'    {mermaid_id(fn)} -->|"hasSubFunction"| {mermaid_id(sf)}')
    return '\n'.join(lines)+'\n'


def contract_detail(g,f):
    lines=['flowchart TB']
    lines.append(f'    F["{mermaid_text(label(g,f))}<br/>Function"]')
    for role in ('input','output'):
        for i,c in enumerate(contracts(g,f,role)):
            alias=f'C{role[0]}{i}'
            lines.append(f'    {alias}["{mermaid_text(n(c))}<br/>Contract"]')
            lines.append(f'    F -->|"has{role.title()}Contract"| {alias}')
            for j,e in enumerate(elem(g,c)):
                ea=f'E{role[0]}{i}_{j}'
                mn=','.join(strings(g,e,D.minOccurs))
                mx=','.join(strings(g,e,D.maxOccurs))
                lines.append(f'    {ea}["{mermaid_text(label(g,e))}<br/>ContractElement [{mn}..{mx}]"]')
                lines.append(f'    {alias} -->|"hasContractElement"| {ea}')
    return '\n'.join(lines)+'\n'


def render(g,allfunctions,exchanges):
    systems=sorted(g.subjects(RDF.type,D.System),key=n)
    prims=set()
    for sysnode in systems:prims|=set(g.objects(sysnode,D.hasPrimaryFunction))
    children=set()
    for f in allfunctions:children|=set(g.objects(f,D.hasSubFunction))
    root=sorted(allfunctions-children,key=n)
    lines=['# Diffie-Hellman R5 — contratti derivati dal Turtle','',
      'Fonte unica: `dh_r5.ttl`. Il renderer non legge l’elenco degli elementi da Python.','',
      'I contratti descrivono **specifiche**: non sono eventi runtime, non autenticano il peer e non descrivono i rami di errore.', '',
      '## Funzione complessiva','']
    rootfile=HERE/'contracts_global.mmd'
    rootfile.write_text(contract_summary(g,root),encoding='utf-8')
    lines += ['```mermaid',rootfile.read_text().strip(),'```','']
    for sysnode in systems:
        primary=sorted(g.objects(sysnode,D.hasPrimaryFunction),key=n)
        seq=[];visited=set()
        def visit(f):
            if f in visited:return
            visited.add(f);seq.append(f)
            for child in sorted(g.objects(f,D.hasSubFunction),key=n):visit(child)
        for f in primary:visit(f)
        prefix=n(sysnode).removesuffix('System')
        filename=HERE/f'contracts_{prefix}.mmd'
        filename.write_text(contract_summary(g,seq,sysnode),encoding='utf-8')
        lines += [f'## {n(sysnode)} — funzione primaria e sottofunzioni','',
                  '```mermaid',filename.read_text().strip(),'```','']
        lines += ['| Funzione | Contratto di input | Input (ContractElement) | Contratto di output | Output (ContractElement) |',
                  '|---|---|---|---|---|']
        for f in seq:
            a=contracts(g,f,'input');b=contracts(g,f,'output')
            def desc(cs):return '; '.join(', '.join(label(g,e)+(' (0..1)' if str(next(g.objects(e,D.minOccurs),''))=='0' else '') for e in elem(g,c)) for c in cs)
            lines.append('| '+ ' | '.join([n(f),', '.join(n(x) for x in a),desc(a),', '.join(n(x) for x in b),desc(b)])+' |')
        lines.append('')
    lines += ['## Funzione complessiva: contratti','',
      '| Funzione | Input | Output |','|---|---|---|']
    for f in root:
        a=contracts(g,f,'input');b=contracts(g,f,'output')
        lines.append('| '+n(f)+' | '+', '.join(label(g,e) for c in a for e in elem(g,c))+' | '+', '.join(label(g,e) for c in b for e in elem(g,c))+' |')
    lines += ['', '## Comunicazioni ricostruite dai contratti condivisi','',
     '| Mittente | Ricevente | Canale | Contratto in comune | Elementi trasmessi secondo specifica |',
     '|---|---|---|---|---|']
    for s,r,ch,c in sorted(exchanges,key=lambda x:n(x[2])):
        lines.append('| '+' | '.join([n(s),n(r),n(ch),n(c),', '.join(label(g,e) for e in elem(g,c))])+' |')
    lines += ['', '## Limiti documentali da mantenere', '',
       '- `ReceivedA` e `ReceivedB` descrivono valori ricevuti, non necessariamente quelli trasmessi: il canale non implica integrità/autenticità.',
       '- `ValidityA/B` rappresentano l’esito della validazione matematica, non l’identità del mittente.',
       '- `AcceptedA/BOptional` (0..1) e `AcceptedA/BRequired` (1..1) sono ContractElement distinti: il CORE non può assegnare cardinalità differenti alla stessa identità.',
       '- L’eventuale corrispondenza informativa fra questi due ruoli è ancora da formalizzare, senza inventarla nell’interrogazione.',
       '- I contratti delle funzioni primarie esprimono input/output del comportamento nominale; nessun ramo di errore è stato inventato.',
       '- Il comportamento per valore privato digitato non valido rimane un gap `?` non ancora rappresentato nel grafo dei Process R4.',
       '- Il predicato completo di validazione e la condizione che abilita la derivazione non sono ancora collegati formalmente.',
       '- Modulo `p`, generatore `g` e ordine `q` non sono stati introdotti come nuovi Resource: qui sono elementi di specifica contrattuale.',
       '']
    (HERE/'contracts_generated.md').write_text('\n'.join(lines),encoding='utf-8')
    (HERE/'contracts_global.md').write_text('# Funzione complessiva — contratti\n\n```mermaid\n'+rootfile.read_text()+'```\n',encoding='utf-8')
    for sysnode in systems:
        prefix=n(sysnode).removesuffix('System')
        (HERE/f'contracts_{prefix}.md').write_text(f'# {n(sysnode)} — funzioni e contratti\n\n```mermaid\n'+(HERE/f'contracts_{prefix}.mmd').read_text()+'```\n',encoding='utf-8')
    details=HERE/'details';details.mkdir(exist_ok=True)
    for f in sorted(allfunctions,key=n):
        core=contract_detail(g,f)
        (details/(n(f)+'.mmd')).write_text(core,encoding='utf-8')
        (details/(n(f)+'.md')).write_text(f'# {n(f)} — contratti ed elementi\n\n```mermaid\n'+core+'```\n',encoding='utf-8')
    with (HERE/'contract_elements_generated.csv').open('w',encoding='utf-8',newline='') as fp:
        w=csv.writer(fp)
        w.writerow(['funzione','verso','contratto','ContractElement','label','minOccurs','maxOccurs','descrizione'])
        for f in sorted(allfunctions,key=n):
            for role in ('input','output'):
                for c in contracts(g,f,role):
                    for e in elem(g,c):
                        w.writerow([n(f),role,n(c),n(e),label(g,e),str(next(g.objects(e,D.minOccurs),'')),str(next(g.objects(e,D.maxOccurs),'')),it_comment(g,e)])
    (HERE/'queries_r5.rq').write_text('''# Q-1: Every function, its contracts and elements (run as SPARQL SELECT)\nPREFIX ddta: <https://w3id.org/ddta/core#>\nSELECT ?function ?direction ?contract ?element ?min ?max WHERE {\n  { ?function ddta:hasInputContract ?contract . BIND("input" AS ?direction) }\n  UNION\n  { ?function ddta:hasOutputContract ?contract . BIND("output" AS ?direction) }\n  ?contract ddta:hasContractElement ?element .\n  OPTIONAL { ?element ddta:minOccurs ?min }\n  OPTIONAL { ?element ddta:maxOccurs ?max }\n} ORDER BY ?function ?direction ?contract ?element\n''',encoding='utf-8')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--file',default='dh_r5.ttl',help='Source Turtle in this directory')
    parser.add_argument('--validate-only',action='store_true')
    args=parser.parse_args()
    source=HERE/args.file
    g=Graph().parse(source,format='turtle')
    issues,funs,conts,exchanges=check(g)
    if issues:
        print('FAIL',len(issues),'issues:')
        for x in issues:print(' -',x)
        raise SystemExit(1)
    print('PASS',len(g),'triples;',len(funs),'functions;',len(conts),'contracts;',len(exchanges),'exchanges')
    if not args.validate_only:render(g,funs,exchanges)

if __name__=='__main__':main()
