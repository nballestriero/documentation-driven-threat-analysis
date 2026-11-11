# Verifica R5 — completamento contratti del caso Diffie-Hellman

## Ambito e criterio

Confronto tra `dh_r4_baseline.ttl` e `dh_r5.ttl`: **l'unica modifica logica prevista è ai contratti e ai ContractElement**. Le relazioni di System, Environment, Boundary, CommunicationChannel, Function/hasSubFunction, Process, ProcessStep, ProcessTransition, guardie e lacune RDF devono rimanere identiche.

## Esiti

- **15/15 funzioni** con almeno un input Contract e un output Contract; nel caso esattamente uno di ciascuno.
- **28 Contract distinti**, 30 associazioni funzione-contratto (due contratti condivisi per il traffico pubblico).
- **Tutti i Contract hanno ContractElement espliciti** con `minOccurs` e `maxOccurs` dichiarati.
- **Due scambi associati univocamente** attraverso contratto condiviso, funzioni di comunicazione, ruolo e canale identico.
- **Nessun segreto privato o derivato** è dichiarato nei contratti di attraversamento dei canali.
- **16 nodi dei processi** nella tabella Step, comprendendo 12 Step applicativi e 4 ControlNode; gli ordinali sono ricavati dalle transizioni, non dal metadato `viz:localOrder`.
- **10 test automatici**: completamento contratti, preservazione delle triple extra-contrattuali, query SPARQL, separazione ricevuto/accettato, regressione su mancanze, canali, ambiguità, cardinalità e modifica della sola fonte RDF.

## Esempio di navigazione ontologica

`PCProcess` → `hasStep` → `PCDeriveSecretStep` → `invokesProcess` → `PCDeriveSecretProcess` → `realizesFunction` → `PCDeriveSecret` → `hasInputContract` → `PCDeriveSecretInputContract` → `hasContractElement` → `PrivateA`, `AcceptedBRequired`, `ModulusP`.

Il contenuto `AcceptedBRequired` è **richiesto** dalla derivazione; il valore `AcceptedBOptional` è **ammesso** dall'output della validazione. I due requisiti condividono un significato applicativo, ma non sono automaticamente lo stesso individuo RDF.

## Rischi documentali residui

- L'esito `ValidityB`/`ValidityA` non è ancora collegato formalmente al predicato `PeerPublicValid` nelle guardie del processo. Il controllo operativo non viene quindi provato solo dal contratto.
- Il ramo di errore per valore b digitato non valido, pur discusso, è tuttora mancante dal grafo R4 e quindi anche R5; non lo abbiamo simulato.
- Il generatore di sequenze R4 non è stato dichiarato conforme; la R5 completa i contratti e rigenera una vista dei passi dai loro collegamenti, non corregge ogni lacuna della Process Ontology.
- Nessuna validazione crittografica runtime o test di mitigazione MITM è inclusa.

**Stato:** completamento contratti verificato; non modifica il repository.
