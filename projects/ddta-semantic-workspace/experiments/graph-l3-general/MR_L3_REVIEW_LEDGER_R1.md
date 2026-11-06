# Graph L3 — Registro di revisione completa degli MR (R1)

**Stato:** REVIEW / NON CANONICAL. **Nessuna modifica ai documenti MR canonici è autorizzata da questo registro.**

**Obiettivo:** impedire che l'elaborazione di Graph L3 perda informazione generale già descritta nei MacroRequirement, o introduca semantica non documentata. La revisione è parte del processo di costruzione di L3, non soltanto un controllo finale.

## 1. Provenienza e limiti

Fonti esaminate: `dermatriage/mr/MR-01.md`, `MR-02.md`, `MR-03.md`, `MR-04.md`, `MR-C6.md`, `MR-C7.md`, nelle copie disponibili al **5 novembre 2026**. Lo stato del repository locale dell'utente non è direttamente accessibile: eseguire `audit_mr_sources.py` dopo l'applicazione per confrontare i file realmente presenti sul proprio PC.

Risultato della verifica tecnica sulle copie: **6/6 documenti Turtle parsabili; 59 triple RDF uniche; unione valida rispetto al Core R3**. Il risultato verifica solo correttezza strutturale secondo i controlli attualmente implementati: **non dimostra completezza dei requisiti né approvazione delle dichiarazioni**.

**Vincoli generali concordati:** Graph L3 è una proiezione dei *soli MR selezionati*; si conserveranno le identità RDF e il contesto L1/L2, espandendo composizione, modalità funzionali dichiarate, informazioni e contratti quando presenti. Non inferire sottofunzioni, mode, processi o garanzie da assenza di dati. **Le DocumentationGap restano nel Turtle e vengono validate ma, per tutte le viste, sono nascoste di default**; la futura opzione per mostrarle non è ancora progettata. Il focus si definirà **dopo** L3 generale.

## 2. Inventario e decisioni per documento

| MR | Struttura Turtle già esistente | Valutazione per Graph L3 | Azione aperta |
|---|---|---|---|
| **MR-01** | Funzione primaria, `CaseInformation` con `CaseInformationContract` e solo `LesionImageElement (minOccurs=0)`; `TriageOutcome hasPart CaseUrgency, OperationalTriagePriority`. | **Aggiornamento richiesto prima dell'L3 completo definitivo.** Le due `FunctionalMode`, `GeneralCaseInformation`, `maxOccurs`, condizioni e lacune sono solo nel file `MR-01-L3-CANDIDATE.md` dell'esperimento. | Rivedere e approvare il modello candidato per trasferire *solo* la semantica confermata nell'MR canonico. Il gruppo 1..1 e il massimo immagine 0..1 restano candidati; la garanzia della priorità senza immagine è NOT SPECIFIED. |
| **MR-02** | `SpecialistDestinationDetermination` riceve `TriageOutcome` e produce `SpecialistDestinationIndication`. | **Struttura generale già rappresentabile.** Nessun contratto dettagliato o scomposizione da inventare. | Verificare l'impatto delle garanzie incomplete dell'output no-image di MR-01 sull'interfaccia di MR-02. Non tradurre la condivisione di `TriageOutcome` in una nuova dipendenza YAML senza riesaminare il contratto `dependsOn`. |
| **MR-03** | `ClinicalReviewManagement` riceve `TriageOutcome`, `ClinicalReview` e produce `ClinicalReviewRecord`, composto dai due input. | **Struttura di input/output e composizione già rappresentabile**; le identità condivise sono coerenti. | Verificare in seguito se la distinzione fra esito originario e revisione richieda vincoli di contratto al livello MR. Non generare cardinalità automaticamente. |
| **MR-04** | `ControlledAdaptation` riceve `AccumulatedClinicalReviewRecords hasPart ClinicalReviewRecord`, produce `AdaptationCandidate` (`Artifact`) e `AdaptationQualificationResult` (`Information`). | **Struttura generale già rappresentabile**, ma la prosa descrive due tipi di adattamento e la non-adozione automatica, non espressi come relazioni RDF. | Valutare se riaddestramento del classificatore e modifica dei prompt costituiscano `FunctionalMode` a livello MR, oppure scelte/realizzazioni da documentare in DEC. Non aggiungere automaticamente due mode. Verificare come preservare il vincolo 'produzione non implica adozione'. |
| **MR-C6** | `DermaTriageEnvironment hasPart` cinque componenti logici; `EnvironmentPreparation hasOutput DermaTriageEnvironment`; componenti senza tipo RDF specifico. | **Composizione dichiarata ma relazione di preparazione da rivedere.** Il Core prevede `ddta:prepares` per questa responsabilità. | Riesaminare la sostituzione `hasOutput` -> `prepares`, l'eventuale relazione `DermaTriage hasOperationalEnvironment DermaTriageEnvironment`, e il trattamento dei tipi/etichette dei cinque componenti. Non assegnare classi improprie per fini grafici. |
| **MR-C7** | `DermaTriageVerification verifies DermaTriage, DermaTriageEnvironment`, produce `VerificationResults`. | **Struttura macro già rappresentabile.** `verifies` non implica esecuzione né superamento. | Verificare se la funzione di verifica debba o meno avere una relazione di appartenenza/offerta rispetto al `System` (non presumere `providesFunction`). La scomposizione di casi, controlli e criteri appartiene per ora a DEC/FR salvo evidenza MR generale. |

## 3. Aspetti trasversali da non perdere

### X-01 — Differenza tra funzione primaria e sue modalità

`DermatologicalTriageEvaluation` è una sola Function. Il candidato MR-01 usa `FunctionalMode` per le varianti con/senza immagine, **non** due Function, Process o pipeline implementative. Le modalità sono visualmente contenute ma non con `hasPart` RDF. È necessario approvare la modifica di MR-01 prima di considerarla parte di Graph L3 canonico.

### X-02 — Contratto e struttura dell'informazione

`Contract hasPart ContractElement` non equivale a `Information hasPart Information`. Le cardinalità appartengono agli elementi del contratto; la vista può presentarli dentro l'informazione con opportuna proiezione grafica, senza modificare la semantica RDF. Il valore `minOccurs=0` documenta opzionalità, **non** automaticamente un massimo pari a 1.

### X-03 — Garanzia dell'output in assenza d'immagine e MR-02/MR-03

`WithoutImageMode` è documentata per la derivazione di `CaseUrgency`, ma la garanzia di `OperationalTriagePriority` resta **NOT SPECIFIED**. Non affermare né che l'output della modalità senza immagine sia un sottoinsieme stretto né che sia equivalente a quello con immagine. La mancanza potrebbe incidere sull'interpretazione degli input per MR-02/MR-03 e va preservata come gap RDF esplicito, senza mostrarlo di default nella vista.

### X-04 — Ambiente separato dal sistema

`DermaTriage` e `DermaTriageEnvironment` conservano identità separate. `EnvironmentPreparation` è una responsabilità distinta da `DermaTriageVerification`; non inventare un processo ordinato setup -> verifica. La composizione dell'ambiente non implica un trasferimento né una sequenza.

### X-05 — Composizioni informative condivise

`TriageOutcome` è unico per MR-01, MR-02 e MR-03; `ClinicalReviewRecord` è unico per MR-03 e MR-04. La proiezione L3 deve evitare copie o nuovi IRI per mere scelte grafiche.

### X-06 — Gap RDF vs visualizzazione

`DocumentationGap` è semantica documentale, non una relazione accertata. I gap devono avere `rdfs:label` valida, anche quando nascosti. **Default grafico per L1, L2 e L3: non visualizzare gap.** La gestione del selettore sarà distinta dalla definizione del focus e arriverà successivamente. La query L3 generale deve rispettare questo default; l'esperimento L3 precedente mostrava i gap per esigenze di test.

## 4. Decisioni ancora da approvare (ordine suggerito)

| ID | Domanda / scelta necessaria | Effetto sulla prossima implementazione | Stato |
|---|---|---|---|
| L3-R01 | Promuovere in MR-01 le `FunctionalMode` e i collegamenti di input/output già testati? | Completa parte funzionale L3 | REVIEW |
| L3-R02 | `GeneralCaseInformation (1..1)` e `LesionImage (0..1)` sono requisiti approvati o restano candidati? | Contratti/cardinalità L3 | REVIEW |
| L3-R03 | In MR-C6 sostituire `hasOutput Environment` con `prepares Environment`? Aggiungere `hasOperationalEnvironment`? | Composizione ambiente L3 | REVIEW |
| L3-R04 | Il differente adattamento dei modelli e dei prompt in MR-04 richiede modalità esplicite a livello MR? | Eventuale `FunctionalMode` non primaria | REVIEW |
| L3-R05 | È sufficiente la proiezione attuale di MR-02/03/C7, oppure la prosa contiene ulteriori identità generali che devono comparire? | Copertura di tutti gli MR | REVIEW |
| L3-R06 | La nuova query L3 generale seleziona tutti gli elementi previsti e omette ogni gap di default? | Implementazione/validazione vista | TODO |
| L3-R07 | Una volta approvata L3 generale, come definire il focus? | Post-L3; NON implementare ora | DEFERRED |

Le decisioni R01-R05 sono controlli di **semantica dell'authoring**, non esigenze create dal renderer. Non promuovere nuovi predicati o classi per migliorare un diagramma se manca evidenza nella documentazione.

## 5. Criteri di completamento della revisione MR per L3

- [ ] Tutti e sei i documenti riesaminati contro la propria prosa, con disposition approvata.
- [ ] Ogni modifica Turtle richiesta da L3 applicata solo dopo revisione semantica, preservando gli stessi IRI condivisi.
- [ ] Nessuna lacuna non documentata trasformata in asserzione RDF; gap espliciti validati.
- [ ] Generazione L3 completa da soli MR, senza selezione di focus o DEC/FR.
- [ ] Nessun nodo `DocumentationGap` nelle viste standard, salvo futura richiesta esplicita.
- [ ] Regressione Graph L1 e Graph L2, inclusi MR-C6/MR-C7 e i cambiamenti autorizzati.
- [ ] Esecuzione sul checkout effettivo dell'utente di `audit_mr_sources.py` e confronto con questo inventario.

**Questo registro è la fonte di lavoro per l'audit L3, non una nuova versione della guida metodologica.**
