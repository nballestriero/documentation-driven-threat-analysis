#!/usr/bin/env python3
"""Optional step table from the R5 RDF. No localOrder or hardcoded step names.
Processes are required to have a single nominal acyclic path in this fixture.
ControlNodes and their documented gaps are included as explicit rows.
"""
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS
from verify_and_render_r5 import D, V, n, label, contracts, elem

HERE=Path(__file__).resolve().parent
P=Namespace('https://w3id.org/ddta/process#')


def table(g):
    rows=[]
    for sys in sorted(g.subjects(RDF.type,D.System),key=n):
        for rootfn in g.objects(sys,D.hasPrimaryFunction):
            processes=list(g.subjects(D.realizesFunction,rootfn))
            if len(processes)!=1:raise ValueError(f'{n(rootfn)} should have one principal Process for this case')
            proc=processes[0]
            step_set=set(g.objects(proc,D.hasStep))
            trans=list(g.objects(proc,P.hasTransition))
            successors={}
            for t in trans:
                a=list(g.objects(t,P.fromStep));b=list(g.objects(t,P.toStep))
                if len(a)!=1 or len(b)!=1 or a[0] not in step_set or b[0] not in step_set:
                    raise ValueError(f'PRC-TRANS-01: invalid {n(t)}')
                successors.setdefault(a[0],[]).append((t,b[0]))
            starts=list(g.objects(proc,V.initialStep))
            if len(starts)!=1:raise ValueError(f'{n(proc)} ambiguous initialStep')
            current=starts[0];visited=set();index=0
            while current is not None:
                if current in visited:raise ValueError(f'{n(proc)} loop unsupported in linear table')
                visited.add(current);index+=1
                sp=list(g.objects(current,P.invokesProcess))
                fns=list(g.objects(sp[0],D.realizesFunction)) if len(sp)==1 else []
                if len(fns)>1:raise ValueError('Multiple function realizations require expanded table')
                f=fns[0] if fns else None
                def elements(role):
                    return ', '.join(sorted({n(e) for c in contracts(g,f,role) for e in elem(g,c)})) if f else '—'
                outgoing=successors.get(current,[])
                if len(outgoing)>1:raise ValueError(f'{n(current)} branches require graph view, not linear trace')
                guards=[]
                if outgoing:
                    t,target=outgoing[0]
                    for condition in g.objects(t,P.hasGuard):
                        guards.append(f'{n(condition)} on transition {n(t)}')
                gaps=[n(x) for x in g.objects(current,V.unresolvedFalseBranch)]
                notes='; '.join(guards+(['gap ? → '+', '.join(gaps)] if gaps else [])) or '—'
                kind='ControlNode' if (current,RDF.type,P.ControlNode) in g else 'ProcessStep'
                rows.append((n(proc),index,n(current),kind,n(f) if f else '—',elements('input'),elements('output'),notes))
                current=outgoing[0][1] if outgoing else None
            if visited!=step_set:raise ValueError(f'{n(proc)} disconnected steps')
    return rows


def main():
    g=Graph().parse(HERE/'dh_r5.ttl',format='turtle')
    rows=table(g)
    result=['# Diffie-Hellman R5 — passi ricavati dalle transizioni e dai contratti','',
        '**Fonte unica:** `dh_r5.ttl`. Gli ordinali sono locali al processo e *derivati* dalle transizioni; `viz:localOrder` viene ignorato.','',
        '| Processo | Ordine locale | Step | Tipo | Funzione realizzata | ContractElement di input | ContractElement di output | Guardia / gap |',
        '|---|---:|---|---|---|---|---|---|']
    for r in rows:result.append('| '+' | '.join(str(x).replace('|','/') for x in r)+' |')
    result += ['', f'**{len(rows)} nodi complessivi**, inclusi i ControlNode. Non è una sequenza globale obbligatoria.',
        '', 'La guardia è mostrata sul ControlNode che possiede la transizione condizionata; gli Step precedenti non ne ereditano automaticamente il significato.',
        '', 'Il ramo per `EnteredB` non valido, non presente nel grafo R4, è una lacuna da affrontare quando rivedremo i processi; non è stato aggiunto qui.', '']
    (HERE/'steps_with_contracts_generated.md').write_text('\n'.join(result),encoding='utf-8')
    print(f'Generated {len(rows)} steps/control nodes')

if __name__=='__main__':main()
