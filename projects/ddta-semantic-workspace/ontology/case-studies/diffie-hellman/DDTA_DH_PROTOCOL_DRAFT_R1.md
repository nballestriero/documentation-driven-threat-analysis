# DDTA — Diffie-Hellman: bozza di documentazione del protocollo (R1)

> **STATO: BOZZA DI CASO DI STUDIO, NON NORMATIVO.** Fonte dei dati di istanza: `model/dh_r5a.ttl` (R5A, 596 triple). Il Turtle contiene una rappresentazione *candidata* del caso e non costituisce la versione definitiva delle ontologie CORE/Process o del protocollo. Le schede analitiche derivate esattamente dal grafo sono in `DDTA_DH_INSTANCE_SHEETS_R1.md`.

## 1. Scopo e criterio di arresto

La prova verifica se DDTA può **rappresentare** un protocollo bilaterale reale (Diffie-Hellman non autenticato), distinguendo le capacità funzionali dal processo che le organizza e conservando contratti, comunicazioni e trust boundary per successive analisi di sicurezza. **Non** intende verificare l'esecuzione di uno scambio reale, dimostrare correttezza crittografica, classificare attacchi o introdurre nuove classi a priori. Non si sta descrivendo un protocollo di autenticazione o proteggendo traffico applicativo.

## 2. Perimetro e identità

I partecipanti sono `PCSystem` e `UserSystem`, ciascuno associato rispettivamente a `PCEnvironment` e `UserEnvironment`. Non c'è un terzo sistema coordinatore. `DiffieHellmanKeyAgreement` è l'identità funzionale complessiva candidata, con parti `PCKeyAgreement` e `UserKeyAgreement`; non la attribuiamo artificialmente a un terzo `System`.

| Prospettiva | Elementi individuati | Interpretazione |
|---|---|---|
| Ambiente | `PCEnvironment`, `UserEnvironment` | Dove sono disponibili le risorse logiche |
| Sistema | `PCSystem`, `UserSystem` | Quali capacità sono offerte |
| Funzioni | 2 primarie, 12 sottofunzioni, 1 complessiva | COSA, indipendentemente dall'ordine applicativo |
| Contratti | 28 identità di contratto, 19 elementi informativi | Specifiche di input/output, non valori runtime |
| Comunicazione | `PCToUserChannel`, `UserToPCChannel` | Due canali logici direzionali |
| Boundary | `PCBoundary`, `UserBoundary` | Confini logici; nel test assunti come domini di trust separati |
| Processo | `PCProcess`, `UserProcess`, 12 sottoprocessi | COME, senza coordinatore esterno |
| Controllo | 12 Step, 4 ControlNode, 14 transizioni | Ordine locale, condizioni e terminazioni |
| Gap | `PCInvalidPublicGap`, `UserInvalidPublicGap` | Rami negativi non documentati |

## 3. Struttura funzionale — COSA

Il CORE associa `System --hasPrimaryFunction--> Function`, `Function --hasSubFunction--> Function`, `Function --hasInputContract/hasOutputContract--> Contract` e `Contract --hasContractElement--> ContractElement`.

- `PCKeyAgreement` comprende `PCGeneratePrivate`, `PCCalculatePublic`, `PCSendPublic`, `PCReceivePublic`, `PCValidatePublic`, `PCDeriveSecret`.
- `UserKeyAgreement` comprende `UserAcquirePrivate`, `UserReceivePublic`, `UserValidatePublic`, `UserCalculatePublic`, `UserSendPublic`, `UserDeriveSecret`.
- La generazione/acquisizione del valore privato differisce fra i partecipanti. Il modulo pubblico `p`, il generatore `g` e l'eventuale parametro `q` sono requisiti contrattuali, non un'implementazione scelta.
- `mustPrecede` esprime precedenze obbligatorie fra sottofunzioni **dirette**, senza definire da sola una traccia esecutiva globale.

Le schede complete, incluse le cardinalità, sono generate dal Turtle; non si devono dedurre elementi da etichette come `InputsPCDerive` o dall'aspetto del Mermaid.

## 4. Comunicazioni fra sistemi e confini di trust

`PCSendPublic` e `UserReceivePublic` utilizzano `PCToUserChannel` e condividono **per scelta esplicita del caso** l'identità del contratto `PublicAOverChannel` (rispettivamente output e input). La coppia inversa `UserSendPublic` / `PCReceivePublic` condivide `PublicBOverChannel` sul canale `UserToPCChannel`.

Non è stata introdotta alcuna classe CORE `Message` o `Transfer`, né una proprietà `carries`: le informazioni comunicate sono ricavabili dai contratti delle **CommunicationFunction**. Questa correlazione è univoca *in questa prova*, non dimostra l'associazione generale di più messaggi ripetuti sullo stesso canale.

Le due funzioni `ReceivePublic` producono `ReceivedA`/`ReceivedB`, distinguibili dal valore atteso (`PublicA`/`PublicB`). Questa distinzione permette di ragionare successivamente su sostituzione o alterazione nel transito. Un valore matematicamente valido non implica che il mittente sia autenticato.

Il CORE modella i confini con `System --hasBoundary--> Boundary`, `Boundary --encloses--> Resource` e le comunicazioni con `CommunicationChannel --hasSource/hasDestination--> Resource`. In questo caso i due endpoint risultano in boundary diversi; l'identità dei boundary, da sola, non dimostra sicurezza/insicurezza.

## 5. Processi — COME

`PCProcess` e `UserProcess` realizzano le due funzioni primarie attraverso `realizesFunction`. `hasSubProcess` (proprietà Process **approvata nella discussione**) collega ciascun processo ai sei sottoprocessi che realizzano le relative sottofunzioni.

Per il flusso operativo `Process --hasStep--> ProcessStep`; `ProcessStep --invokesProcess--> Process` è ancora **candidato** e collega ogni attività al sottoprocesso. `Process --hasTransition--> ProcessTransition`, `fromStep`, `toStep`, `hasGuard` sono candidate dell'ontologia Process. Le transizioni appartengono sempre al processo che le dichiara; non si creano transizioni dirette fra i due processi partecipanti.

La lettura nominale scelta per questo esperimento è:

- PC: genera `a`, calcola `A`, invia `A`, riceve `B_r`, lo valida, deriva `K_PC` sul ramo valido, termina.
- User: acquisisce `b`, riceve `A_r`, lo valida, calcola `B`, invia `B`, deriva `K_User` sul ramo valido, termina.

L'avvio dei due processi è indipendente; l'ordine trasversale deriva dalle comunicazioni causali. Non esiste un ordine totale obbligatorio fra le operazioni locali indipendenti. Un coordinatore esterno non fa parte del caso.

La bozza contiene due `ControlNode` per la validazione pubblica e due nodi di terminazione; i rami negativi dei due controlli puntano a lacune `?` come **metadato documentale**, senza creare Step di gestione degli errori.

## 6. Condizioni e loro relazione con i contratti

`PCPeerPublicValid` valuta l'**esito `ValidityB`** prodotto da `PCValidatePublic`. `UserPeerPublicValid` valuta l'**esito `ValidityA`** prodotto da `UserValidatePublic`. Questo collegamento è presente in R5A e impedisce di confondere il valore remoto ricevuto con il risultato della sua validazione.

Il dato facoltativamente accettato dall'output di `ValidatePublic` e il dato obbligatorio richiesto dall'input di `DeriveSecret` sono rappresentati da `ContractElement` distinti con cardinalità differenti. **La corrispondenza semantica fra i due non è ancora formalizzata**; una semplice uguaglianza dei nomi non deve essere interpretata come equivalenza RDF.

Il metadato `viz:guardExpected "true"` non è la formalizzazione completa di un predicato booleano nell'ontologia Process. Il nostro scopo presente si ferma al fatto che la prosecuzione nominale richiede l'esito di validazione positivo.

## 7. Viste del modello

- `generated/architecture.mmd` e `.md`: sistemi, ambienti, risorse, boundary, canali.
- `generated/function_tree.mmd` e `.md`: funzione complessiva e decomposizione funzionale.
- `generated/PC_process.mmd` e `.md`, `User_process.mmd` e `.md`: Step, transizioni, guardia, gap e sottoprocessi richiamati (etichettati).
- `generated/steps_from_rdf.md`: lettura dei passi, ricostruita dal grafo, con funzione, contratti e canali.
- `DDTA_DH_INSTANCE_SHEETS_R1.md`: schede delle istanze RDF con relazioni e contratti effettivi.

Le viste Mermaid sono **derivate** dal Turtle mediante lo script del pacchetto. I nodi grafici di gap non vengono trasformati in `ProcessStep`; nessun ordine globale viene inventato.

## 8. Validazione già eseguita e limiti

La baseline R5A è stata verificata in precedenza con 596 triple RDF, 107 asserzioni strutturali superate e un test negativo riuscito che collega intenzionalmente la condizione PC al dato grezzo anziché all'esito. Il rapporto originario è conservato in `snapshots/r5a/VERIFICA_MINIMA_R5A.md`.

Restano **non dimostrati e fuori perimetro**: sicurezza del Diffie-Hellman non autenticato; autenticità del peer; formalizzazione completa dell'espressione booleana di `AtomicCondition`; equivalenza fra alcuni elementi di contratti diversi; regole di correlazione per scambi ripetuti; comportamento dettagliato dei rami negativi; modellazione del caso `b` non valido; equivalenza di funzioni o processi mediante reasoning OWL; completezza delle verifiche SHACL. Anche il generatore di sequence diagram R4 va considerato **prototipo storico**, non vista definitiva del caso.

## 9. Stato delle scelte da consolidare in futuro

| Elemento | Stato | Implicazione |
|---|---|---|
| Classi del CORE | Esistenti, definite nel CORE | Nessuna modifica richiesta per il caso |
| `hasSubProcess` | Approvata nella discussione Process | Da formalizzare nella scheda normativa Process |
| `ProcessTransition`, `hasTransition`, `fromStep`, `toStep` | Bozza candidata | Usate come strutture del caso, da consolidare |
| `invokesProcess` | Candidata | Necessaria nel caso per risalire dallo Step alla Function |
| `ControlNode`, `AtomicCondition`, `Operand` | Bozza candidata | Usati per condizioni e ramo nominale |
| `viz:initialStep`, `viz:communicationRole`, `viz:unresolvedFalseBranch`, `viz:guardExpected`, `viz:localOrder` | Ausiliarie, **non CORE né Process** | Servono alla prova; eventuale migrazione alle convenzioni ufficiali DDTA |
| `EndProcess` | Valore di tipo di controllo nel caso | Semantica esecutiva e scope terminale non ancora formalizzati |

## 10. Ripresa del lavoro

Per riprendere: **aprire prima** `DDTA_DH_INSTANCE_SHEETS_R1.md`, verificare le identità e le relazioni rispetto al Turtle R5A e decidere quali correzioni siano necessarie. Solo **dopo** consolidare le schede e applicare le eventuali modifiche al TTL; non correggere il Mermaid manualmente lasciando il modello invariato. Le modifiche al protocollo vanno distinte dalle modifiche normative dell'ontologia Process.
