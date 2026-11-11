#!/usr/bin/env python3
"""R5 authoring: complete the CORE input/output contracts in the R4 RDF fixture.
The only modifications are contracts and contract elements. No Process/Step/Transition
or functional decomposition is changed. Views must be rendered from dh_r5.ttl.
"""
from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS, Literal
from rdflib.namespace import XSD

HERE = Path(__file__).resolve().parent
D = Namespace('https://w3id.org/ddta/core#')
DH = Namespace('https://example.org/ddta/dh-deterministic-r4#')  # preserve existing case identities

# CE identity may be reused only when the same information *and* cardinality
# requirements apply. AcceptedA/B are deliberately split because the validator
# can omit them, whereas the key derivation requires their presence.
ELEMENTS = {
    'ModulusP': ('Modulus p', 'Parametro pubblico del gruppo Diffie-Hellman, modulo p.', 1, 1),
    'GeneratorG': ('Generatore g', 'Generatore pubblico compatibile con il gruppo concordato.', 1, 1),
    'SubgroupOrderQ': ('Ordine q (se applicabile)', 'Ordine del sottogruppo, quando richiesto dai parametri adottati.', 0, 1),
    'EntropyPC': ('Materiale casuale imprevedibile', 'Input informativo richiesto per la generazione di a; la sua fornitura dipende da una risorsa RNG da modellare successivamente.', 1, 1),
    'EnteredB': ('Valore b digitato', 'Valore privato candidato fornito dall’operatore umano; non ancora accettato.', 1, 1),
    'PrivateA': ('Segreto privato a', 'Esponente privato del PC; rimane nel proprio dominio di trust.', 1, 1),
    'PrivateB': ('Segreto privato b', 'Esponente privato accettato dall’ambiente utente; non trasmesso al peer.', 1, 1),
    'PublicA': ('Valore pubblico A', 'Valore pubblico g^a mod p specificato per il canale PC→User.', 1, 1),
    'PublicB': ('Valore pubblico B', 'Valore pubblico g^b mod p specificato per il canale User→PC.', 1, 1),
    'ReceivedA': ('Valore ricevuto A_r', 'Dato ricevuto come presunto A; potrebbe differire da A per alterazioni o sostituzione.', 1, 1),
    'ReceivedB': ('Valore ricevuto B_r', 'Dato ricevuto come presunto B; potrebbe differire da B per alterazioni o sostituzione.', 1, 1),
    'ValidityA': ('Esito validità A_r', 'Esito della verifica di validità matematica del valore remoto A_r; non autenticità.', 1, 1),
    'ValidityB': ('Esito validità B_r', 'Esito della verifica di validità matematica del valore remoto B_r; non autenticità.', 1, 1),
    'AcceptedAOptional': ('A_r accettato (se valido)', 'Dato remoto accettato come matematicamente valido, disponibile soltanto sul percorso valido.', 0, 1),
    'AcceptedBOptional': ('B_r accettato (se valido)', 'Dato remoto accettato come matematicamente valido, disponibile soltanto sul percorso valido.', 0, 1),
    'AcceptedARequired': ('A_r accettato (richiesto)', 'Dato remoto già accettato, richiesto dal calcolo del segreto nell’ambiente utente.', 1, 1),
    'AcceptedBRequired': ('B_r accettato (richiesto)', 'Dato remoto già accettato, richiesto dal calcolo del segreto nell’ambiente PC.', 1, 1),
    'SharedKPC': ('Segreto condiviso K_PC', 'Segreto derivato localmente nel PC; non trasferito sul canale.', 1, 1),
    'SharedKUser': ('Segreto condiviso K_User', 'Segreto derivato localmente nel sistema utente; non trasferito sul canale.', 1, 1),
}

# Each entry defines the function's input and output ContractElements.
# An input or output Contract can also carry behavioral requirements as comments,
# which do not create fictitious data objects.
FUNCTIONS = {
    'DiffieHellmanKeyAgreement': (
        ['ModulusP','GeneratorG','SubgroupOrderQ','EnteredB'],
        ['PublicA','PublicB','SharedKPC','SharedKUser'],
        'Specificazione bilaterale: due sistemi indipendenti utilizzano parametri compatibili. Il PC genera internamente a; b è acquisito dall’utente. Nessun segreto privato è comunicato.',
        'Risultati locali nominali; con scambio integro e valori validi K_PC = K_User. Il contratto NON garantisce autenticità o resistenza a MITM.'),
    'PCKeyAgreement': (
        ['ModulusP','GeneratorG','SubgroupOrderQ','PublicB'],
        ['PublicA','SharedKPC'],
        'Il valore B è richiesto come informazione remota ricevibile; a è generato internamente dalla sottofunzione dedicata.',
        'A è esposto al peer tramite CommunicationFunction; K_PC rimane locale. L’uscita segreta è prevista sul percorso nominale valido.'),
    'UserKeyAgreement': (
        ['ModulusP','GeneratorG','SubgroupOrderQ','EnteredB','PublicA'],
        ['PublicB','SharedKUser'],
        'L’operatore fornisce il valore privato candidato b; A è la specifica del valore pubblico atteso dall’altro partecipante.',
        'B è esposto al peer tramite CommunicationFunction; K_User rimane locale. L’uscita segreta è prevista sul percorso nominale valido.'),
    'PCGeneratePrivate': (
        ['ModulusP','SubgroupOrderQ','EntropyPC'],['PrivateA'],
        'Usa un generatore casuale adeguato, risorsa di realizzazione non descritta come ContractElement. Vincolo di intervallo determinato dai parametri del gruppo.',
        'Produce a senza comunicarlo.'),
    'PCCalculatePublic': (
        ['PrivateA','GeneratorG','ModulusP'],['PublicA'],
        'Calcola A = g^a mod p.',
        'A è pubblicabile.'),
    'PCSendPublic': (
        ['PublicA'],['PublicA'],
        'Input locale: A già calcolato. La CommunicationFunction utilizza PCToUserChannel.',
        'Contratto condiviso PublicAOverChannel: A è previsto come informazione inviata, non prova di ricezione.'),
    'PCReceivePublic': (
        ['PublicB'],['ReceivedB'],
        'Contratto condiviso PublicBOverChannel: ci si aspetta B, ma il contenuto concretamente ricevuto potrebbe essere B_r diverso.',
        'ReceivedB è il dato ricevuto grezzo: non è ancora validato né autenticato.'),
    'PCValidatePublic': (
        ['ReceivedB','ModulusP','GeneratorG','SubgroupOrderQ'],['ValidityB','AcceptedBOptional'],
        'Controlla validità matematica secondo i parametri concordati; predicato specifico non ancora formalizzato. Non verifica l’identità del peer.',
        'Fornisce sempre l’esito ValidityB; fornisce AcceptedBOptional solo sul percorso valido. Il ramo non valido resta ? documentale.'),
    'PCDeriveSecret': (
        ['PrivateA','AcceptedBRequired','ModulusP'],['SharedKPC'],
        'Richiede il valore remoto accettato; l’obbligatorietà riguarda il percorso nominale valido.',
        'Produce K_PC soltanto localmente.'),
    'UserAcquirePrivate': (
        ['EnteredB','ModulusP','SubgroupOrderQ'],['PrivateB'],
        'L’utente inserisce un valore privato candidato; il contratto richiede che sia accettabile secondo i vincoli del gruppo.',
        'PrivateB è prodotto soltanto se il candidato è accettato. Il comportamento per input non valido non è ancora documentato (?).'),
    'UserReceivePublic': (
        ['PublicA'],['ReceivedA'],
        'Contratto condiviso PublicAOverChannel: ci si aspetta A, ma il dato concretamente ricevuto potrebbe essere A_r diverso.',
        'ReceivedA è il dato ricevuto grezzo: non è ancora validato né autenticato.'),
    'UserValidatePublic': (
        ['ReceivedA','ModulusP','GeneratorG','SubgroupOrderQ'],['ValidityA','AcceptedAOptional'],
        'Controlla validità matematica del valore remoto ricevuto; predicato non formalizzato. Non verifica provenienza o autenticità.',
        'Fornisce sempre ValidityA; fornisce AcceptedAOptional solo sul percorso valido. Il ramo non valido resta ? documentale.'),
    'UserCalculatePublic': (
        ['PrivateB','GeneratorG','ModulusP'],['PublicB'],
        'Calcola B = g^b mod p.',
        'B è pubblicabile.'),
    'UserSendPublic': (
        ['PublicB'],['PublicB'],
        'Input locale: B già calcolato. La CommunicationFunction utilizza UserToPCChannel.',
        'Contratto condiviso PublicBOverChannel: B è previsto come informazione inviata, non prova di ricezione.'),
    'UserDeriveSecret': (
        ['PrivateB','AcceptedARequired','ModulusP'],['SharedKUser'],
        'Richiede il valore remoto accettato; l’obbligatorietà riguarda il percorso nominale valido.',
        'Produce K_User soltanto localmente.'),
}

SHARED_CROSSING = {
    ('PCSendPublic','output'): 'PublicAOverChannel',
    ('UserReceivePublic','input'): 'PublicAOverChannel',
    ('UserSendPublic','output'): 'PublicBOverChannel',
    ('PCReceivePublic','input'): 'PublicBOverChannel',
}


def main():
    g = Graph().parse(HERE/'dh_r4_baseline.ttl',format='turtle')
    g.bind('ddta',D);g.bind('dh',DH)
    funs=set(g.subjects(RDF.type,D.Function)) | set(g.subjects(RDF.type,D.CommunicationFunction))
    missing={DH[k] for k in FUNCTIONS}-funs
    extras=funs-{DH[k] for k in FUNCTIONS}
    if missing or extras:
        raise ValueError(f'Function catalog mismatch; missing={missing}, extras={extras}')

    # Remove the old contract layer; no change to functions, processes, channels,
    # environments, boundaries, controls or transitions.
    old_contracts=set(g.subjects(RDF.type,D.Contract))
    old_elements=set(g.subjects(RDF.type,D.ContractElement))
    for s,p,o in list(g.triples((None,None,None))):
        if p in (D.hasInputContract,D.hasOutputContract) or s in old_contracts:
            g.remove((s,p,o))
    for s in old_elements:
        if s not in [DH[x] for x in ELEMENTS]:
            # Legacy unused elements can only be removed if no other RDF object refers to them.
            if not list(g.subjects(None,s)):
                for t in list(g.triples((s,None,None))):g.remove(t)

    for key,(label,definition,minn,maxx) in ELEMENTS.items():
        s=DH[key]
        g.remove((s,RDFS.label,None))
        g.add((s,RDF.type,D.ContractElement))
        g.add((s,RDFS.label,Literal(label,lang='it')))
        g.add((s,RDFS.comment,Literal(definition,lang='it')))
        g.add((s,D.minOccurs,Literal(minn,datatype=XSD.nonNegativeInteger)))
        g.add((s,D.maxOccurs,Literal(maxx,datatype=XSD.nonNegativeInteger)))

    contract_details={}
    for fn,(inp,out,desc_in,desc_out) in FUNCTIONS.items():
        for role,items,descr,prop in [('input',inp,desc_in,D.hasInputContract),('output',out,desc_out,D.hasOutputContract)]:
            key=SHARED_CROSSING.get((fn,role),fn+('InputContract' if role=='input' else 'OutputContract'))
            c=DH[key]
            desired=frozenset(items)
            if key in contract_details and contract_details[key]!=desired:
                raise ValueError(f'Contract {key} reused with different elements')
            contract_details[key]=desired
            g.add((c,RDF.type,D.Contract))
            # Keep comments without creating misleading additional contract identities.
            if (c,RDFS.label,None) not in g:
                g.add((c,RDFS.label,Literal(key)))
            g.add((c,RDFS.comment,Literal(f'{fn}/{role}: {descr}',lang='it')))
            g.add((DH[fn],prop,c))
            for e in items:g.add((c,D.hasContractElement,DH[e]))

    target=HERE/'dh_r5.ttl'
    g.serialize(destination=target,format='turtle')
    print('Generated',target.name,'triples',len(g),'functions',len(FUNCTIONS),'contracts',len(set(g.subjects(RDF.type,D.Contract))))

if __name__=='__main__':main()
