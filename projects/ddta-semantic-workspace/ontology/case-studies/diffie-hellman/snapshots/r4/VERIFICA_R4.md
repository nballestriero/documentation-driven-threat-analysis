# DDTA Diffie-Hellman — verifica ontologica R4

**Data:** 2026-11-11  
**Oggetto:** verifica critica dei file `dh_r4.ttl`, `generate.py`, `flow_generated.mmd`, `sequence_generated.mmd`, `steps_generated.md`.  
**Ambito:** esclusivamente la documentazione ontologica del comportamento previsto, **non** l'esecuzione Python dei peer né una validazione di sicurezza crittografica.  
**Esito sintetico:** **PARZIALMENTE CONFORME (R4 non ancora approvabile come generatore ontologico affidabile)**.

## 1. Verifiche positive

| ID | Verifica | Risultato | Evidenza |
|---|---|---|---|
| V-01 | Il Turtle è leggibile da RDFLib | PASS | 440 triple RDF |
| V-02 | Due System, Environment e Boundary distinti | PASS | `PCSystem`, `UserSystem`; ambienti e Boundary associati con proprietà CORE |
| V-03 | Due canali direzionali con endpoint Resource | PASS | `PCToUserChannel` e `UserToPCChannel` |
| V-04 | Le funzioni di invio/ricezione sono CommunicationFunction | PASS | Quattro funzioni, ognuna con `usesChannel` e contratti |
| V-05 | Due processi principali e relativi sottoprocessi | PASS | `PCProcess`, `UserProcess`, 6 sottoprocessi per partecipante, `realizesFunction` |
| V-06 | Navigazione Step → sottoprocesso → Function → Contract | PASS | `hasStep`, `invokesProcess`, `realizesFunction`, `hasInputContract`/`hasOutputContract` |
| V-07 | Ordine nominale espresso dalle transizioni | PASS con limite | 14 `ProcessTransition` locali; grafici nominali leggibili |
| V-08 | Associazione di due scambi tra processi | PASS per il solo caso | Contratto condiviso, canale comune, ruolo di invio/ricezione esplicito in `viz:communicationRole` |
| V-09 | Due rami di validazione con lacuna | PASS con limite | `ControlNode`, guardia sul ramo positivo, `viz:unresolvedFalseBranch` per il `?` |
| V-10 | Controllo di proprietà delle transizioni al processo | PASS | Mutazione negativa rilevata: `PRC-TRANS-01 violated: PCTransition01` |
| V-11 | Rigenerazione delle viste dal TTL esistente | PASS | `python generate.py --render-only`: `440 triples; 12 steps; 2 exchanges; 14 transitions` |
| V-12 | Integrità del pacchetto di partenza | PASS | `sha256sum -c SHA256SUMS.txt`: tutti i file elencati OK |

## 2. Test di mutazione sul Turtle: errori riproducibili

I test sono stati eseguiti su copie temporanee, senza alterare R4 e senza modificare il repository.

| Test | Mutazione nel solo TTL | Esito del validatore R4 | Problema |
|---|---|---|---|
| M-01 | Scambio `viz:localOrder` di `UserValidatePublicStep` e `UserCalculatePublicStep` | **Accettata** | La tabella colloca il calcolo prima della validazione, ma `flow_generated.mmd` conserva `Validate → Decision → Calculate` secondo le transizioni. Due fonti dell'ordine sono incoerenti. |
| M-02 | Rimozione di `proc:hasGuard` dalla transizione uscente dal controllo di validità del PC | **Accettata** | La tabella e il sequence diagram continuano a menzionare `PeerPublicValid` grazie al nome della funzione; il flow non mostra più l'etichetta `true`. |
| M-03 | Rimozione di `viz:unresolvedFalseBranch` per il controllo User | **Accettata** | Il flow non contiene più il `?` User; l'elenco dei passi continua ad affermare che esiste il gap, perché basato sul suffisso `ValidatePublic`. |
| M-04 | Rimozione del `UserBoundary` dal grafo | **Accettata** | Né la vista dei passi né il sequence diagram evidenziano l'assenza della copertura del confine di trust. |

**Conclusione dei test M-01–M-04:** la riproducibilità del codice non basta. Le viste devono discendere dalle *relazioni ontologiche pertinenti*, non da `viz:localOrder`, convenzioni basate sui nomi o una struttura attesa hard-coded.

## 3. Lacune semantiche indipendenti dal generatore

### 3.1 Contratti principali non dichiarati

Le funzioni `PCKeyAgreement` e `UserKeyAgreement` non hanno nel Turtle alcun `hasInputContract` né `hasOutputContract`. Perciò la vista della funzione principale non può ricostruire formalmente gli ingressi/uscite complessivi.

### 3.2 Contratti delle operazioni troppo generici

- `PCCalculatePublic` ha come unico ContractElement di input `InputsPCPublic`, non i ruoli identificabili `PrivateA`, `GeneratorG`, `ModulusP`.
- `PCDeriveSecret` ha un unico input `InputsPCDerive`, non `PrivateA`, `ReceivedB`, `ModulusP`.
- Gli analoghi contratti User usano `InputsUserPublic` e `InputsUserDerive`.

Questa compressione impedisce di ricostruire la provenienza dei singoli dati fino alla derivazione delle chiavi; rende insufficiente un controllo successivo della propagazione di un valore attaccato o sostituito.

### 3.3 Condizioni non formalizzate

`PCPeerPublicValid` e `UserPeerPublicValid` hanno un `leftOperand` che cita il ContractElement ricevuto, ma non descrivono il predicato di validazione. Il test documenta l'identità del criterio, non la sua valutazione matematica, e non dimostra autenticità o integrità.

### 3.4 Non tutti i rami già discussi sono nel modello

Esistono soltanto due gap, entrambi per valore pubblico remoto invalido. Il caso del segreto privato digitato dall'utente non valido, discusso in precedenza, non è documentato mediante una condizione e un gap.

### 3.5 La vista completa non comprende ancora tutto il sistema

Il Turtle possiede Environment, Boundary, canali e risorse endpoint, ma le viste generate non integrano il quadro dei trust boundary, né i contratti delle funzioni primarie. Il `sequenceDiagram` è una linearizzazione nominale valida: non rappresenta tutte le alternative possibili né l'intero ordine parziale del protocollo.

### 3.6 Dipendenze dal caso specifico

`generate.py` cerca esplicitamente `PC`, `User`, `PublicAOverChannel`, `PublicBOverChannel` e il suffisso `ValidatePublic`. Inoltre utilizza `viz:communicationRole`, `viz:initialStep`, `viz:localOrder`, `viz:unresolvedFalseBranch`, `viz:guardExpected` come metadati ausiliari. Pertanto non è ancora una traduzione generale di tutte le istanze ammesse da DDTA Process Ontology.

### 3.7 La tabella esclude i nodi di controllo

Il grafo dichiara **12 `ProcessStep` applicativi** e **4 `ControlNode`** (due decisioni e due terminazioni), questi ultimi appartenenti ontologicamente alla famiglia `ProcessStep`. `steps_generated.md` contiene solo le dodici attività che possiedono `invokesProcess`, perché il generatore esclude esplicitamente gli Step di controllo. La vista passo-passo non è quindi una traccia completa dei nodi del processo, e colloca la condizione nella riga dell’attività di validazione invece che sul nodo/transizione che effettivamente la governa.

### 3.8 Rappresentazione di End

Il generatore Mermaid disegna anche `EndProcess` con forma romboidale, pur essendo un nodo terminale e non una decisione: errore di resa grafica, non del modello `ControlNode`.

### 3.9 Validazione formale delle ontologie non eseguita

Il test su R4 è basato su RDFLib e su controlli Python dedicati; **non** prova che l’intero grafo sia conforme alle definizioni formali OWL/SHACL di CORE e Process. Per esempio i `ControlNode` sono istanziati come tali e collegati con `hasStep`, ma il Turtle del caso non importa gli assiomi della gerarchia Process per eseguire inferenza di classe. Serve un controllo successivo sulle ontologie effettive e sui relativi Shape SHACL.

## 4. Decisioni che NON occorre riaprire

- Le due direzioni possono essere modellate con `CommunicationFunction` separate, `usesChannel` e contratti: non serve introdurre `Message`, `Transfer` o `carries` in CORE.
- `Process --hasSubProcess--> Process` è strutturale e non transitiva; `ProcessStep --invokesProcess--> Process` ne specifica l'impiego in un punto del flusso (proprietà Process ancora candidata).
- Le transizioni non devono collegare direttamente Step di processi differenti.
- Gli errori non documentati restano `?` documentali, non Step eseguibili.
- Lo stato effettivo `RUNNING/WAITING/STOPPED` appartiene a una eventuale ontologia di esecuzione, non direttamente all'identità `Process`.

## 5. Correzioni proposte per R5, nell'ordine

1. **Unica sorgente dell'ordine operativo:** estrarre le sequenze da `hasStep` + `hasTransition/fromStep/toStep/hasGuard`; rimuovere `viz:localOrder` come fonte indipendente, oppure renderlo soltanto dato derivato. L'ordine è parziale in presenza di concorrenza.
2. **Condizioni e gap:** derivare i rami dalle guardie e dal meccanismo di gap documentale, senza dedurre `PeerPublicValid` dai nomi Python/RDF. Rilevare se la guardia manca mentre viene rappresentata come presente.
3. **Contratti completi:** aggiungere i contratti alle funzioni primarie; decomporre input di calcolo e derivazione in `ContractElement` con ruoli distinti, senza confondere la specifica col valore runtime.
4. **Correlazione interprocesso:** per il caso attuale, individuare in maniera generale le `CommunicationFunction` con lo stesso contratto di attraversamento (output lato mittente; input lato ricevente) e lo stesso canale; verificare direzione source/destination tramite endpoint e Boundary. Non usare una lista di due contratti codificata nel generatore. Imporre un controllo di ambiguità.
5. **Copertura dei Boundary:** aggiungere una vista/diagnostica che segnali se gli endpoint di un canale non hanno una collocazione esplicita nel modello dei trust boundary.
6. **Condizioni candidate:** collegare in modo interrogabile validazione ed esito, mantenendo separati validità matematica e autenticità. Documentare con `?` ogni ramo effettivamente richiesto ma ancora non specificato.
7. **Viste unificate:** dalla stessa fonte produrre una vista funzionale+contratti, una vista processo/Step+condizioni, un sequence diagram delle interazioni e una tabella che includa **anche i ControlNode e le transizioni condizionali**. I diagrammi non devono inventare contenuto.
8. **Test di regressione:** includere sistematicamente le mutazioni M-01–M-04 e una mutazione che renda ambiguo l'abbinamento fra invio e ricezione.

## 6. Criteri di accettazione della prossima iterazione

La R5 sarà considerata verificata quando una modifica delle sole relazioni RDF che governano ordine, guardia, gap, contenuti e Boundary cambierà coerentemente **tutte** le viste interessate oppure produrrà un errore di validazione documentale; nessuna vista potrà continuare a presentare come certo un fatto che è stato rimosso dal grafo.

**Stato:** rapporto di verifica; nessuna modifica a ontologia CORE, ontologia Process, Turtle R4 o repository.
