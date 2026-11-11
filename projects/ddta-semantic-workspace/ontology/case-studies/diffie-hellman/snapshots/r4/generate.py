#!/usr/bin/env python3
"""Build, validate, and render a DDTA Diffie-Hellman model exclusively from RDF.
Python builds the *ontology test fixture*; renderers only read the saved TTL.
"""
from __future__ import annotations
import argparse
import csv
import io
from collections import defaultdict
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS, Literal
from rdflib.namespace import XSD

HERE = Path(__file__).resolve().parent
D = Namespace("https://w3id.org/ddta/core#")
P = Namespace("https://w3id.org/ddta/process#")
DH = Namespace("https://example.org/ddta/dh-deterministic-r4#")
V = Namespace("https://example.org/ddta/view#")


def name(term):
    return str(term).rsplit('#', 1)[-1]


def build():
    g=Graph()
    for x,ns in [('ddta',D),('proc',P),('dh',DH),('viz',V)]:
        g.bind(x,ns)
    def node(id,kind,label):
        s=DH[id]
        g.add((s,RDF.type,kind));g.add((s,RDFS.label,Literal(label)))
        return s
    def link(s,p,o):g.add((s,p,o))
    def contract(id,element):
        c=node(id,D.Contract,id)
        e=node(element,D.ContractElement,element)
        link(c,D.hasContractElement,e)
        return c
    # System, environment, endpoints, boundaries.
    for who in ['PC','User']:
        sys=node(who+'System',D.System,who+'System')
        env=node(who+'Environment',D.Environment,who+'Environment')
        b=node(who+'Boundary',D.Boundary,who+' trust boundary')
        ep=node(who+'Endpoint',D.Resource,who+' logical endpoint')
        link(sys,D.hasOperationalEnvironment,env)
        link(sys,D.hasBoundary,b)
        link(env,D.makesAvailable,ep)
        link(b,D.encloses,ep)
        pf=node(who+'KeyAgreement',D.Function,who+'KeyAgreement')
        link(sys,D.hasPrimaryFunction,pf)
    cAB=node('PCToUserChannel',D.CommunicationChannel,'PC → User')
    cBA=node('UserToPCChannel',D.CommunicationChannel,'User → PC')
    for chan,src,dest in [(cAB,DH.PCEndpoint,DH.UserEndpoint),(cBA,DH.UserEndpoint,DH.PCEndpoint)]:
        link(chan,D.hasSource,src);link(chan,D.hasDestination,dest)

    # Root global function without inventing a third system.
    globalF=node('DiffieHellmanKeyAgreement',D.Function,'Diffie-Hellman · bilateral key agreement')
    for who in ['PC','User']: link(globalF,D.hasSubFunction,DH[who+'KeyAgreement'])

    # Each subfunction may have independent local IO contracts.
    specs={
      'PC': [
        ('GeneratePrivate','Genera segreto a',None,None,'PCPrivateOutput','PrivateA'),
        ('CalculatePublic','Calcola A', 'PCPublicCalcInput','InputsPCPublic','PCPublicCalcOutput','PublicA'),
        ('SendPublic','Invia A','PCSendInput','LocalPublicA','PublicAOverChannel','PublicA', 'send','PCToUserChannel'),
        ('ReceivePublic','Riceve B','PublicBOverChannel','PublicB','PCReceiveOutput','ReceivedB','receive','UserToPCChannel'),
        ('ValidatePublic','Verifica validità B','PCValidationInput','ReceivedB','PCValidationOutput','ValidityB'),
        ('DeriveSecret','Deriva K_PC','PCDeriveInput','InputsPCDerive','PCDeriveOutput','SharedKPC')
      ],
      'User': [
        ('AcquirePrivate','Acquisisce segreto b','UserSecretInput','EnteredB','UserPrivate','PrivateB'),
        ('ReceivePublic','Riceve A','PublicAOverChannel','PublicA','UserReceiveOutput','ReceivedA','receive','PCToUserChannel'),
        ('ValidatePublic','Verifica validità A','UserValidationInput','ReceivedA','UserValidationOutput','ValidityA'),
        ('CalculatePublic','Calcola B','UserPublicCalcInput','InputsUserPublic','UserPublicCalcOutput','PublicB'),
        ('SendPublic','Invia B','UserSendInput','LocalPublicB','PublicBOverChannel','PublicB','send','UserToPCChannel'),
        ('DeriveSecret','Deriva K_User','UserDeriveInput','InputsUserDerive','UserDeriveOutput','SharedKUser')
      ]
    }
    # Reuse same shared crossing contract for sender output / recipient input.
    shared={}
    for s,elt in [('PublicAOverChannel','PublicA'),('PublicBOverChannel','PublicB')]:
        shared[s]=contract(s,elt)
    for who,fs in specs.items():
        for f in fs:
            short, desc,ic,ie,oc,oe,*comm=f
            kind=D.CommunicationFunction if comm else D.Function
            fn=node(who+short,kind,desc)
            link(DH[who+'KeyAgreement'],D.hasSubFunction,fn)
            if ic:
                link(fn,D.hasInputContract,shared.get(ic) or contract(ic,ie))
            if oc:
                link(fn,D.hasOutputContract,shared.get(oc) or contract(oc,oe))
            if comm:
                role,channel=comm
                link(fn,D.usesChannel,DH[channel])
                # role is explicit query-level view metadata, not core ontology semantics.
                link(fn,V.communicationRole,Literal(role))
    # Process decomposition: independently ordered ProcessSteps invoking sub-processes.
    processes={}
    for who,fs in specs.items():
        proc=node(who+'Process',D.Process,who+'Process')
        processes[who]=proc
        link(proc,D.realizesFunction,DH[who+'KeyAgreement'])
        steps=[]
        for i,f in enumerate(fs,1):
            short,desc=f[:2]
            sub=node(who+short+'Process',D.Process,who+' '+short+' subprocess')
            link(proc,P.hasSubProcess,sub)
            link(sub,D.realizesFunction,DH[who+short])
            st=node(who+short+'Step',D.ProcessStep,desc)
            link(proc,D.hasStep,st)
            link(st,P.invokesProcess,sub)
            link(st,V.localOrder,Literal(i,datatype=XSD.integer))
            steps.append(st)
            if short=='ValidatePublic':
                decision=node(who+'PublicValidityDecision',P.ControlNode,who+' peer public valid?')
                link(proc,D.hasStep,decision)
                link(decision,V.localOrder,Literal(i,datatype=XSD.integer))
                # False branch is DOCUMENTATION GAP, not ProcessStep.
                gap=node(who+'InvalidPublicGap',V.DocumentationGap,'? valore remoto non valido')
                link(decision,V.unresolvedFalseBranch,gap)
                steps.append(decision)
        end=node(who+'End',P.ControlNode,who+' fine processo')
        link(proc,D.hasStep,end)
        link(end,P.controlKind,Literal('EndProcess'))
        steps.append(end)
        link(proc,V.initialStep,steps[0])
        for idx,(a,b) in enumerate(zip(steps,steps[1:]),1):
            trans=node(who+'Transition'+str(idx).zfill(2),P.ProcessTransition,'T '+str(idx))
            link(proc,P.hasTransition,trans)
            link(trans,P.fromStep,a);link(trans,P.toStep,b)
            if name(a)==who+'PublicValidityDecision':
                cond=node(who+'PeerPublicValid',P.AtomicCondition,'PeerPublicValid '+who)
                operand=node(who+'ReceivedPublicOperand',P.Operand,who+' remote public operand')
                link(cond,P.leftOperand,operand)
                link(operand,P.referencesContractElement,DH['ReceivedB' if who=='PC' else 'ReceivedA'])
                link(trans,P.hasGuard,cond)
                link(trans,V.guardExpected,Literal('true'))
        # Direct sibling functional precedence; the order intentionally includes some implementation choices.
        relations={
          'PC':[('GeneratePrivate','CalculatePublic'),('CalculatePublic','SendPublic'),
                ('GeneratePrivate','DeriveSecret'),('ReceivePublic','ValidatePublic'),
                ('ValidatePublic','DeriveSecret')],
          'User':[('AcquirePrivate','CalculatePublic'),('CalculatePublic','SendPublic'),
                  ('AcquirePrivate','DeriveSecret'),('ReceivePublic','ValidatePublic'),
                  ('ValidatePublic','DeriveSecret')]
        }
        for first,second in relations[who]:
            link(DH[who+first],D.mustPrecede,DH[who+second])
    path=HERE/'dh_r4.ttl'
    g.serialize(destination=str(path),format='turtle')
    return g


def getone(g,s,p):
    vals=list(g.objects(s,p))
    if len(vals)!=1: raise ValueError(f'Expected precisely one {name(p)} for {name(s)}; got {len(vals)}')
    return vals[0]


def validate(g):
    processes=list(g.subjects(RDF.type,D.Process))
    parent_steps={}
    for p in processes:
        for s in g.objects(p,D.hasStep):
            parent_steps.setdefault(s,[]).append(p)
    for t in g.subjects(RDF.type,P.ProcessTransition):
        parents=list(g.subjects(P.hasTransition,t))
        if len(parents)!=1: raise ValueError('Transition owner ambiguous '+name(t))
        a=getone(g,t,P.fromStep);b=getone(g,t,P.toStep)
        if parent_steps.get(a)!=parents or parent_steps.get(b)!=parents:
            raise ValueError('PRC-TRANS-01 violated: '+name(t))
    for s in g.subjects(P.invokesProcess,None):
        sub=getone(g,s,P.invokesProcess)
        owner=parent_steps.get(s,[])
        if len(owner)!=1 or (owner[0],P.hasSubProcess,sub) not in g:
            raise ValueError('Step invocation outside owning process: '+name(s))
    for p in [DH.PCProcess,DH.UserProcess]:
        start=getone(g,p,V.initialStep)
        localtrans=list(g.objects(p,P.hasTransition))
        adj=defaultdict(list)
        for t in localtrans:adj[getone(g,t,P.fromStep)].append(getone(g,t,P.toStep))
        cur=start;seen=set()
        while True:
            if cur in seen:raise ValueError('Process cycle '+name(p))
            seen.add(cur)
            if not adj[cur]: break
            if len(adj[cur])!=1: raise ValueError('Unexpected multi-branch transition '+name(cur))
            cur=adj[cur][0]
        if len(seen)!=len(set(g.objects(p,D.hasStep))):raise ValueError('Disconnected steps in '+name(p))
    # Identical explicit communication contract and channel; exactly one sending/receiving function per exchange.
    for contract in [DH.PublicAOverChannel,DH.PublicBOverChannel]:
        send=list(g.subjects(D.hasOutputContract,contract))
        recv=list(g.subjects(D.hasInputContract,contract))
        if len(send)!=1 or len(recv)!=1:raise ValueError('Ambiguous send/receive pairing '+name(contract))
        a,b=send[0],recv[0]
        if (a,V.communicationRole,Literal('send')) not in g or (b,V.communicationRole,Literal('receive')) not in g:
            raise ValueError('Missing explicit communication roles')
        if getone(g,a,D.usesChannel)!=getone(g,b,D.usesChannel):raise ValueError('Channel mismatch')
    # Check monotone process order for all mustPrecede under same function parent.
    for who in ['PC','User']:
        ranks={}
        for s in g.objects(DH[who+'Process'],D.hasStep):
            sub=list(g.objects(s,P.invokesProcess))
            if sub:
                f=getone(g,sub[0],D.realizesFunction)
                ranks[f]=int(getone(g,s,V.localOrder))
        for f in g.objects(DH[who+'KeyAgreement'],D.hasSubFunction):
            for later in g.objects(f,D.mustPrecede):
                if ranks[f] >= ranks[later]:raise ValueError('Function precedence violation '+name(f))
    return len(list(g.triples((None,P.hasTransition,None))))


def extract_steps(g,who):
    proc=DH[who+'Process']; out=[]
    for st in g.objects(proc,D.hasStep):
        if (st,P.invokesProcess,None) not in g:continue
        sub=getone(g,st,P.invokesProcess)
        f=getone(g,sub,D.realizesFunction)
        item={'step':st,'function':f,'order':int(getone(g,st,V.localOrder)),
              'label':str(getone(g,st,RDFS.label)),
              'input':[], 'output':[], 'channel':None,'role':None}
        for prop,field in [(D.hasInputContract,'input'),(D.hasOutputContract,'output')]:
            for c in g.objects(f,prop):
                item[field].extend(name(e) for e in g.objects(c,D.hasContractElement))
        channels=list(g.objects(f,D.usesChannel))
        if channels:
            item['channel']=channels[0]
            item['role']=str(getone(g,f,V.communicationRole))
        out.append(item)
    return sorted(out,key=lambda x:(x['order'],name(x['step'])))


def exchanges(g,bywho):
    items={}
    for who,steps in bywho.items():
        for x in steps:items[x['function']]=(who,x)
    result=[]
    for contract in [DH.PublicAOverChannel,DH.PublicBOverChannel]:
        sf=getone_by_reverse(g,D.hasOutputContract,contract)
        rf=getone_by_reverse(g,D.hasInputContract,contract)
        sw,s=items[sf];rw,r=items[rf]
        channel=getone(g,sf,D.usesChannel)
        result.append({'from':sw,'to':rw,'send':s,'receive':r,'contract':contract,
                       'channel':channel,
                       'content':sorted(name(e) for e in g.objects(contract,D.hasContractElement))})
    return result


def getone_by_reverse(g,property,obj):
    vals=list(g.subjects(property,obj))
    if len(vals)!=1:raise ValueError('Ambiguous function for contract '+name(obj))
    return vals[0]


def ordered_events(g,bywho,ex):
    # Global partial order = local transition order + send->receive causal edges.
    events={name(x['step']):(who,x) for who,v in bywho.items() for x in v}
    edges=defaultdict(set); indeg={k:0 for k in events}
    def edge(a,b):
        if b not in edges[a]:edges[a].add(b);indeg[b]+=1
    for who,v in bywho.items():
        for a,b in zip(v,v[1:]):edge(name(a['step']),name(b['step']))
    for x in ex:edge(name(x['send']['step']),name(x['receive']['step']))
    # deterministic stable topological sort; does not claim a required global total order
    result=[]
    while indeg:
        ready=sorted(k for k,v in indeg.items() if v==0)
        if not ready:raise ValueError('Cross-process communication deadlock / cycle')
        item=ready[0]
        result.append(events[item])
        del indeg[item]
        for nextid in edges[item]:
            if nextid in indeg:indeg[nextid]-=1
    return result


def render(g):
    count=validate(g)
    bywho={who:extract_steps(g,who) for who in ('PC','User')}
    ex=exchanges(g,bywho)
    order=ordered_events(g,bywho,ex)
    # sequence events are generated from local Step order + matched output/input Contract.
    lines=['sequenceDiagram','    autonumber','    participant PC as PCProcess','    participant User as UserProcess',
           '    Note over PC,User: Percorso nominale; una linearizzazione valida, non ordine globale unico']
    sent={}
    received={}
    for x in ex:
        sent[name(x['send']['step'])]=x
        received[name(x['receive']['step'])]=x
    for who,step in order:
        send=sent.get(name(step['step']))
        recv=received.get(name(step['step']))
        if send:
            lines.append(f"    {send['from']}->>{send['to']}: {','.join(send['content'])} via {name(send['channel'])}")
        elif recv:
            lines.append(f"    Note over {who}: Ricezione di {','.join(recv['content'])}")
        else:
            lbl=step['label'].replace(':',' - ')
            lines.append(f'    {who}->>{who}: {lbl}')
        if name(step['function']).endswith('ValidatePublic'):
            lines.append(f'    Note over {who}: PeerPublicValid true: prosegue; false: ❓ GAP non documentato')
    (HERE/'sequence_generated.mmd').write_text('\n'.join(lines)+'\n',encoding='utf-8')

    # A second view preserves BOTH partial orders and branch gaps, without forcing global order.
    flow=['flowchart LR']
    for who,steps in bywho.items():
        proc=DH[who+'Process']
        flow.append(f'    subgraph {who}["{who}Process · ordine locale"]')
        for step in steps:
            st=name(step['step'])
            flow.append(f'        {st}["{step["label"]}"]')
        for ctrl in g.objects(proc,D.hasStep):
            if (ctrl,RDF.type,P.ControlNode) in g:
                flow.append(f'        {name(ctrl)}{{"{str(getone(g,ctrl,RDFS.label))}"}}')
        flow.append('    end')
        for trans in g.objects(proc,P.hasTransition):
            a=getone(g,trans,P.fromStep);b=getone(g,trans,P.toStep)
            guard=list(g.objects(trans,P.hasGuard))
            if guard:
                flow.append(f'    {name(a)} -->|"true"| {name(b)}')
            else:
                flow.append(f'    {name(a)} --> {name(b)}')
        for ctrl in g.objects(proc,D.hasStep):
            for gap in g.objects(ctrl,V.unresolvedFalseBranch):
                flow.append(f'    {name(gap)}(("?"))')
                flow.append(f'    {name(ctrl)} -.->|"false / non documentato"| {name(gap)}')
                flow.append(f'    style {name(gap)} fill:#fff1f1,stroke:#dc2626,color:#dc2626,stroke-width:2px,stroke-dasharray:4 3')
    for x in ex:
        flow.append(f'    {name(x["send"]["step"])} -.->|"{",".join(x["content"])} / {name(x["channel"])}"| {name(x["receive"]["step"])}')
    (HERE/'flow_generated.mmd').write_text('\n'.join(flow)+'\n',encoding='utf-8')

    # exact local orders, not spurious globally numbered steps
    rows=[]
    gapnotes={}
    for who,steps in bywho.items():
        for step in steps:
            rows.append([who,step['order'],name(step['step']),name(step['function']),
                  ', '.join(sorted(set(step['input']))) or '—',
                  ', '.join(sorted(set(step['output']))) or '—',
                  name(step['channel']) if step['channel'] else '—',
                  'PeerPublicValid; false → ❓ GAP' if name(step['function']).endswith('ValidatePublic') else '—'])
    with (HERE/'steps_generated.csv').open('w',encoding='utf-8',newline='') as fp:
        w=csv.writer(fp);w.writerow(['processo','ordine_locale','step','funzione','input','output','canale','condizione_gap']);w.writerows(rows)
    md=['# Traccia dei passi generata dal grafo RDF','','> Gli ordini sono locali a ciascun processo: non costituiscono una cronologia globale.','',
        '| Processo | Ordine | Step | Funzione | Input | Output | Canale | Condizione/gap |',
        '|---|---:|---|---|---|---|---|---|']
    for row in rows:md.append('| '+' | '.join(str(x).replace('|','/') for x in row)+' |')
    md += ['', '## Scambi associati deterministicamente', '',
           'L’associazione è ottenuta da **identico contratto di attraversamento**, canale comune e ruoli espliciti di invio/ricezione.']
    for x in ex:
        md.append(f"- `{x['from']}` → `{x['to']}`: `{', '.join(x['content'])}` su `{name(x['channel'])}` (contratto `{name(x['contract'])}`).")
    md+=['','**Nota:** la tabella documenta il comportamento previsto, non eventi runtime né garanzie di autenticità.']
    (HERE/'steps_generated.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    return len(rows),len(ex),count


def main():
    arg=argparse.ArgumentParser()
    arg.add_argument('--render-only',action='store_true',help='Render only the existing RDF; do not rebuild it')
    arg.add_argument('--negative-test',action='store_true',help='Deliberately mutate a transition endpoint; must fail')
    opt=arg.parse_args()
    g=Graph().parse(str(HERE/'dh_r4.ttl'),format='turtle') if opt.render_only else build()
    if opt.negative_test:
        t=DH.PCTransition01
        a=getone(g,t,P.toStep)
        g.remove((t,P.toStep,a));g.add((t,P.toStep,DH.UserReceivePublicStep))
        try:validate(g)
        except ValueError as e:
            print('PASS negative test:',e);return
        raise SystemExit('FAIL: invalid transition was accepted')
    print('PASS: %s triples; %s steps, %s exchanges, %s transitions' %
          (len(g),*render(g)))


if __name__=='__main__': main()
