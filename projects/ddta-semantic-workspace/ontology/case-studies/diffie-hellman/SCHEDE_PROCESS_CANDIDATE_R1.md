# DDTA Process — schede candidate emerse dalla prova Diffie-Hellman

> **BOZZA NON NORMATIVA**. Le decisioni delle classi generali sono nella copia `context/DDTA_PROCESS_DRAFT_R1.md`; qui registriamo soltanto gli elementi **effettivamente usati** nella prova e ciò che rimane da rendere definitivo nelle schede generali.

## Scheda PS-01 — `hasSubProcess`

- **Categoria:** ObjectProperty candidata della DDTA Process Ontology.
- **Dominio:** `ddta:Process`.
- **Range:** `ddta:Process`.
- **Stato:** **approvata concettualmente** durante il caso di studio; non ancora inserita nell'ontologia definitiva.
- **Semantica:** composizione strutturale diretta; **non transitiva**, non descrive attivazione o ordine.
- **Esempio:** `dh:PCProcess proc:hasSubProcess dh:PCSendPublicProcess`.
- **Interrogazione desiderata:** percorrere `proc:hasSubProcess+` per individuare le funzioni realizzate dai sottoprocessi.

## Scheda PS-02 — `invokesProcess`

- **Categoria:** ObjectProperty candidata.
- **Dominio:** `ddta:ProcessStep`.
- **Range:** `ddta:Process`.
- **Stato:** da approvare.
- **Semantica:** uno Step designa il sottoprocesso chiamato dal flusso; non rende `ProcessStep` una specializzazione di Process.
- **Esempio:** `dh:PCSendPublicStep proc:invokesProcess dh:PCSendPublicProcess`.
- **Rilevanza:** `Step → Process → realizesFunction → CommunicationFunction → Contract/Channel`.

## Scheda PS-03 — `ProcessTransition`

- **Categoria:** classe candidata con `Process --hasTransition--> ProcessTransition` e `fromStep`/`toStep` verso `ProcessStep`.
- **Stato:** da formalizzare.
- **Vincolo strutturale prioritario:** `PRC-TRANS-01`: gli estremi appartengono **allo stesso Process** che dichiara la transizione.
- **Esempio:** `PCTransition01 ... PCGeneratePrivateStep → PCCalculatePublicStep`.
- **Note:** `hasNextStep` del CORE può essere derivato dalle transizioni locali, non viceversa; ordine funzionale `mustPrecede` resta distinto.

## Scheda PS-04 — `ControlNode`, condizioni e lacune

- **Categoria:** `ControlNode` candidato specializzazione di `ProcessStep`; `AtomicCondition`, `Operand`, `hasGuard` candidati.
- **Esempio:** `PCPublicValidityDecision` con percorso nominale verso `PCDeriveSecretStep`, guardia `PCPeerPublicValid` e gap documentale `PCInvalidPublicGap`.
- **Operando corretto in R5A:** `ValidityB`, elemento output di `PCValidatePublic`, **non** `ReceivedB`.
- **Metadati provvisori:** `viz:unresolvedFalseBranch`, `viz:guardExpected`; non sono classi/proprietà normative della Process Ontology.
- **Manca:** rappresentazione formale completa della regola `ValidityB = true` e della possibile relazione fra accepted output e required input; non serve completarla ai fini di questa prova.

## Scheda PS-05 — Collegamento a CommunicationFunction e Boundary

- **Riutilizzo CORE:** `realizesFunction`, `hasInputContract`, `hasOutputContract`, `hasContractElement`, `usesChannel`, `hasSource`, `hasDestination`, `hasBoundary`, `encloses`.
- **Stato:** nessuna nuova proprietà CORE necessaria per il caso.
- **Associazione degli scambi:** nel caso i contratti `PublicAOverChannel` e `PublicBOverChannel` sono **individui condivisi** fra invio e ricezione sullo stesso canale. `viz:communicationRole` dichiara il ruolo del caso. Non inferire una regola universale di correlazione per scambi ripetuti.
- **Sicurezza futura:** la provenienza del dato remoto e l'attraversamento del boundary sono punti di analisi; validità matematica non dimostra autenticità.

## Condizione di consolidamento

Prima di approvare le dichiarazioni normative: verificare l'IRI dei namespace, la compatibilità con `DDTA_CORE.md`, la struttura delle proprietà e gli Shape SHACL, con particolare attenzione alla validazione di `PRC-TRANS-01`. I grafici del caso NON sono fonte normativa.
