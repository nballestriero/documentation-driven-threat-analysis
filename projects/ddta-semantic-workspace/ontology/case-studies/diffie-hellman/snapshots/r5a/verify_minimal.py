#!/usr/bin/env python3
"""Minimal DDTA-DH structural acceptance checks. Read-only; does not execute protocol."""
from pathlib import Path
from rdflib import Graph, Namespace, RDF, Literal

ROOT=Path(__file__).resolve().parent
D=Namespace('https://w3id.org/ddta/core#')
P=Namespace('https://w3id.org/ddta/process#')
DH=Namespace('https://example.org/ddta/dh-deterministic-r4#')
V=Namespace('https://example.org/ddta/view#')


def verify(graph: Graph):
    notes=[]
    def check(ok,detail):
        if not ok: raise AssertionError(detail)
        notes.append('PASS '+detail)
    # Every function must have both IO contracts, and each contract must contain at least one ContractElement.
    functions=set(graph.subjects(RDF.type,D.Function)) | set(graph.subjects(RDF.type,D.CommunicationFunction))
    check(len(functions)==15,'15 funzioni identificate')
    for fn in functions:
        for prop in (D.hasInputContract,D.hasOutputContract):
            contracts=list(graph.objects(fn,prop))
            check(bool(contracts),f'Contratto {prop.split("#")[-1]} per {fn.split("#")[-1]}')
            for c in contracts:
                check(bool(list(graph.objects(c,D.hasContractElement))),f'Elementi specificati per {c.split("#")[-1]}')
    # Two separated environments, trust boundaries and bidirectional channels.
    for who in ('PC','User'):
        system=DH[who+'System'];env=DH[who+'Environment'];boundary=DH[who+'Boundary'];endpoint=DH[who+'Endpoint']
        check((system,D.hasOperationalEnvironment,env) in graph, f'{who} system/ambiente')
        check((system,D.hasBoundary,boundary) in graph and (boundary,D.encloses,endpoint) in graph,f'{who} trust boundary/endpoint')
    for ch,src,dst in [('PCToUserChannel','PCEndpoint','UserEndpoint'),('UserToPCChannel','UserEndpoint','PCEndpoint')]:
        c=DH[ch]
        check((c,D.hasSource,DH[src]) in graph and (c,D.hasDestination,DH[dst]) in graph,f'Canale {ch} orientato')
    # Two separate process decompositions, each of 6 subprocesses and linked to the principal Function.
    for who in ('PC','User'):
        proc=DH[who+'Process'];sub=list(graph.objects(proc,P.hasSubProcess))
        check(len(sub)==6 and (proc,D.realizesFunction,DH[who+'KeyAgreement']) in graph,f'{who} process and 6 subprocesses')
        for s in sub:check(bool(list(graph.objects(s,D.realizesFunction))),f'{s.split("#")[-1]} realizes function')
    # Every ProcessTransition endpoint is a step of its owning process.
    for trans in graph.subjects(RDF.type,P.ProcessTransition):
        owners=list(graph.subjects(P.hasTransition,trans))
        check(len(owners)==1 and all(len(list(graph.objects(trans,role)))==1 and (owners[0],D.hasStep,next(graph.objects(trans,role))) in graph for role in (P.fromStep,P.toStep)),f'PRC-TRANS-01 {trans.split("#")[-1]}')
    # Validation result itself, not received raw input, is the operand of the positive guarded transition.
    for who,result in (('PC','ValidityB'),('User','ValidityA')):
        cond=DH[who+'PeerPublicValid'];operand=DH[who+'ValidationOutcomeOperand']
        check((cond,P.leftOperand,operand) in graph and (operand,P.referencesContractElement,DH[result]) in graph,f'{who} condizione collegata a esito {result}')
        producer=DH[who+'ValidatePublic']
        check(any((contract,D.hasContractElement,DH[result]) in graph for contract in graph.objects(producer,D.hasOutputContract)),f'{who} esito presente nel contratto di output validazione')
        guards=list(graph.subjects(P.hasGuard,cond))
        check(len(guards)==1 and (guards[0],V.guardExpected,Literal('true')) in graph,f'{who} ramo nominale con guardia true (metadato view)')
        node=DH[who+'PublicValidityDecision'];gap=DH[who+'InvalidPublicGap']
        check((node,V.unresolvedFalseBranch,gap) in graph and (gap,RDF.type,V.DocumentationGap) in graph and not list(graph.subjects(D.hasStep,gap)),f'{who} ramo negativo documentale ?')
    # Keep the two shared contracts and match their send/receive functions on same channel.
    for cid in ('PublicAOverChannel','PublicBOverChannel'):
        c=DH[cid]
        send=list(graph.subjects(D.hasOutputContract,c))
        recv=list(graph.subjects(D.hasInputContract,c))
        check(len(send)==len(recv)==1 and next(graph.objects(send[0],D.usesChannel))==next(graph.objects(recv[0],D.usesChannel)),f'{cid} send/receive sullo stesso canale')
    # No private or derived secret may be declared as contract element of crossing channels.
    for cid in ('PublicAOverChannel','PublicBOverChannel'):
        bad={'PrivateA','PrivateB','SharedKPC','SharedKUser'}
        check(not any(elt.split('#')[-1] in bad for elt in graph.objects(DH[cid],D.hasContractElement)),f'{cid} nessun segreto privato sul canale')
    return notes


def main():
    g=Graph().parse(ROOT/'dh_r5a.ttl',format='turtle')
    checks=verify(g)
    print(f'OK — {len(g)} triple, {len(checks)} asserzioni strutturali')
    # Mandatory negative test: rewire guard operand to raw received public value.
    wrong=Graph();wrong+=g
    operand=DH.PCValidationOutcomeOperand
    wrong.remove((operand,P.referencesContractElement,DH.ValidityB))
    wrong.add((operand,P.referencesContractElement,DH.ReceivedB))
    try:verify(wrong)
    except AssertionError:
        print('OK — mutazione negativa: guardia sull’input grezzo rilevata')
    else:raise AssertionError('Mutazione negativa non rilevata')
    (ROOT/'CHECK_RESULTS.txt').write_text('\n'.join(checks)+'\n',encoding='utf-8')
if __name__=='__main__':main()
