# DDTA — Security Ontology: schede ontologiche e matrici di applicabilità

**Stato:** definizione approvata della DDTA Security Ontology.  
**Dipendenze:** `DDTA_CORE.md` e `DDTA_PROCESS.md` (identità e relazioni esistenti).  
**Namespace dell’estensione:** `security: <https://w3id.org/ddta/security#>` (IRI definito nella specifica; la pubblicazione web non è presunta).  
**Confini:** nessuna norma grafica, nessuna modifica a CORE/Process, nessuna ipotesi sul ciclo di vita della documentazione o sull'implementazione di script. Le schede definiscono il vocabolario ontologico, senza attestare la presenza o l’efficacia di protezioni implementate in un sistema.

## 1. Scopo e principi

La DDTA Security Ontology consente di descrivere, sulle **identità RDF già presenti** in CORE e Process:

1. **Proprietà di sicurezza** considerate per ogni entità (`SecurityProperty`).
2. **Stato documentato** della relativa protezione (`SecurityReview`): non specificata, dichiarata presente o dichiarata assente; una dichiarazione non è una garanzia.
3. **Lacune documentali** relative a entità, proprietà e relazioni (`DocumentationGap`).
4. **Segnali di possibile problema** distinti dai gap (`SecuritySignal`), classificati con un tipo (`SecurityIssueType`).
5. **Risposte documentali** ai controlli strutturali di CORE/Process (`DocumentationReview`), necessarie soprattutto quando una relazione facoltativa può essere volutamente assente.
6. **Controlli di protezione e loro applicazioni** (`SecurityControl`, `ProtectionApplication`), distinti dall'entità protetta, dal contesto operativo e dalla prova di efficacia.

Sono previste due matrici **distinte**:

- **M1 — Applicabilità della sicurezza:** per ogni individuo delle classi elencate, le proprietà marcate `R` devono ricevere una risposta documentata. Questo **non** significa che ogni protezione sia necessariamente richiesta o implementata.
- **M2 — Completezza documentale:** per ogni entità si verificano aspetti di documentazione obbligatori, da valutare oppure condizionali. Anche l'assenza intenzionale di un componente facoltativo deve poter essere dichiarata esplicitamente.

Una proprietà non documentata non è una protezione assente. Una protezione dichiarata non è una protezione dimostrata efficace. Una `DocumentationGap` non è di per sé una vulnerabilità. Un `SecuritySignal` non prova che un attacco sia avvenuto.

**Semantica RDF/OWL:** l'assenza di triple non implica falsità. L'eventuale generazione automatica di gap deriva soltanto da regole di completezza applicate a un insieme di dati selezionato, non da inferenze OWL negative. Le matrici descrivono i criteri da formalizzare e validare in seguito, senza prescrivere ora strumenti o procedure di editing.

`DocumentationGap` è collocata nella Security Ontology, ma può riguardare anche incompletezze funzionali o architetturali. Le icone e gli stili Mermaid saranno definiti separatamente, come convenzioni di visualizzazione.

**Vocabolario di riferimento:** CIA = Confidentiality, Integrity, Availability; CIA³-R include inoltre Authenticity, Authorization e NonRepudiation. Le categorie STRIDE-AI sono trattate come possibili **tipi di problema**, non come sinonimi delle proprietà da proteggere.

### 1.1 Estensibilità verso altre ontologie DDTA

L'ontologia Security descrive dichiarazioni che si riferiscono a **identità già presenti** nel grafo del sistema. Il loro oggetto può appartenere al CORE, a Process o a un'ontologia specializzata: non serve duplicare l'individuo e non serve renderlo sottoclasse di `SecurityProperty`, `SecurityReview` o `SecurityControl`.

Un'eventuale ontologia `network:` potrà introdurre `Router`, `Switch`, `ChannelSection`, percorsi e collegamenti, riutilizzando l'identità di `ddta:CommunicationChannel` e `ddta:Resource`. Router e sezioni non sono automaticamente sottoclassi di `CommunicationChannel`: la specializzazione mantiene distinte risorse e collegamenti. Le dichiarazioni Security potranno riferirsi anche a questi nuovi individui tramite gli stessi predicati.

**Estensione delle matrici:** ogni modulo specializzato può aggiungere regole M1/M2 identificate dall'IRI completo della classe e dall'ID della regola. Gli obblighi delle superclassi si conservano; quelli delle sottoclassi si aggiungono come unione, senza duplicare la stessa coppia *(individuo, proprietà)* o *(individuo, controllo)*. Una risposta `NOT_APPLICABLE` o `IGNORED`, con la motivazione prevista, riguarda il caso documentato: non cancella una regola per tutti gli individui della classe. Eventuali conflitti fra regole dichiarative dovranno essere segnalati, non risolti in base all'ordine dei file.

La separazione per modulo riguarda **la conoscenza e le regole di applicabilità**. Le convenzioni grafiche YAML e i livelli Mermaid restano esterni all'ontologia e non definiscono il significato di classi o proprietà.

### 1.2 Oggetto protetto, mezzo e copertura

La proprietà `Integrity`, quando è richiesta per un contenuto informativo, riguarda il **dato** e non la semplice identità del canale che lo trasporta. Analogamente, la riservatezza di un `StoredContent` e l'integrità della configurazione di un router sono proprietà applicate a oggetti diversi.

Un `CommunicationChannel` può dichiarare quali **servizi o meccanismi di protezione** sono previsti per le informazioni che lo attraversano. Questo non significa che il canale sia di per sé un dato dotato di integrità, né che la presenza di un meccanismo assicuri automaticamente protezione end-to-end. La matrice M1 sui canali impone l'**esame delle protezioni di trasporto** per le proprietà pertinenti; la dichiarazione del requisito sul dato rimane distinta.

Un `SecurityControl` identifica la protezione prevista per un oggetto e una proprietà; una `ProtectionApplication` descrive un'applicazione di quella protezione in un ambito. Una stessa protezione può avere **zero o più applicazioni dichiarate**, e uno stesso dato può essere protetto in ambiti differenti (per esempio dal programma e dal tunnel fra router). Le coperture possono sovrapporsi o essere complementari **relativamente al dato, alla proprietà e all'ambito**; tale rapporto non si deduce dalla sola presenza di due meccanismi.

---

## 2. Matrice M1 — applicabilità delle proprietà di sicurezza

**Legenda:** **R** = revisione e documentazione obbligatorie per ogni individuo della classe; **—** = nessun obbligo automatico introdotto dalla prima matrice. «—» **non** significa che la proprietà non sia applicabile in assoluto: può essere richiesta esplicitamente dal progetto. Una revisione obbligatoria può concludersi con `NOT_APPLICABLE` motivato.

**Regola sulle sottoclassi:** la tabella definisce la copertura **effettiva** per ciascuna classe, includendo gli obblighi delle superclassi. Un individuo con più tipi riceve l'unione delle proprietà dovute, senza duplicati. Il controllo non genera due gap per la stessa coppia entità/proprietà. Le ontologie specializzate possono aggiungere righe qualificate dal proprio namespace.

**Interpretazione del bersaglio:** le righe relative a dati (`ContractElement`, `StoredContent`, operandi informativi) riguardano proprietà del contenuto specificato. Le righe relative a canali riguardano la **valutazione dei servizi di protezione forniti durante il trasporto**; quelle relative a router o altre risorse tecniche possono riguardare il loro stato e le configurazioni. Il semplice valore `R` non afferma alcuna protezione attuata.

| Ontologia | Classe | C | I | A | Au | Az | Nr | Motivazione e confine dell'esame |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| CORE | `System` | R | R | R | R | R | — | Dati, comportamento, disponibilità, identità e accesso al sistema |
| CORE | `Function` | R | R | R | R | R | — | Dati trattati, risultati, disponibilità e utilizzo della capacità |
| CORE | `Environment` | — | R | R | — | R | — | Integrità, disponibilità e accesso alle risorse dell'ambiente; non è un dato |
| CORE | `Resource` | R | R | R | R | R | — | Risorsa generica: il documentatore può dichiarare N/A per singole proprietà |
| CORE | `Contract` | — | R | — | — | — | — | Integrità della specifica, non del dato runtime |
| CORE | `ContractElement` | R | R | — | R | R | — | Proprietà **richieste ai dati specificati**, non a un valore runtime già osservato |
| CORE | `Store` | R | R | R | R | R | — | Controlli del deposito logico e del suo stato/configurazione, distinti dai requisiti sui contenuti |
| CORE | `StoredContent` | R | R | R | R | R | — | Contenuto identificabile conservato nello Store |
| CORE | `Boundary` | — | — | — | — | — | — | Confine logico: contesto per individuare attraversamenti; non è di per sé un controllo |
| CORE | `CommunicationFunction` | R | R | R | R | R | R | Capacità comunicativa; non ripudio dell'azione/scambio da valutare esplicitamente |
| CORE | `CommunicationChannel` | R | R | R | R | R | — | **Esame delle protezioni offerte al traffico** e degli estremi; integrità/riservatezza dei dati da identificare separatamente |
| CORE | `Process` | R | R | R | R | R | — | Dati trattati e correttezza/disponibilità del processo previsto |
| CORE | `ProcessStep` | R | R | R | R | R | — | Dati e operazioni dello Step, senza affermare esecuzione avvenuta |
| PROCESS | `ProcessTransition` | — | R | R | — | — | — | Integrità del flusso di controllo e possibilità di prosecuzione |
| PROCESS | `Condition` | — | R | — | — | — | — | Integrità del criterio e della sua valutazione prevista |
| PROCESS | `AtomicCondition` | — | R | — | — | — | — | Eredita la copertura di `Condition` |
| PROCESS | `CompositeCondition` | — | R | — | — | — | — | Eredita la copertura di `Condition` |
| PROCESS | `Operand` | R | R | — | — | — | — | Riservatezza e integrità del valore cui fa riferimento, se pertinente |
| PROCESS | `ControlNode` | R | R | R | R | R | — | Eredita la copertura di `ProcessStep`; controlli del flusso |
| PROCESS | `SynchronizationNode` | R | R | R | R | R | — | Eredita la copertura di `ControlNode` |
| PROCESS | `CodeReference` | — | R | — | R | — | — | Integrità e provenienza del riferimento al sorgente, non della build eseguita |

**Criteri di interpretazione della matrice, senza modifiche alle schede CORE:** la copertura ampia di `Resource`, `Function` e `ProcessStep` può produrre molte dichiarazioni `NOT_APPLICABLE`, ma è intenzionale come scelta conservativa di revisione. `Boundary` costituisce un elemento di contesto: l'attraversamento del confine dovrà essere verificato su canali e comunicazioni, non inferito come una vulnerabilità del confine stesso. L'applicabilità di `NonRepudiation` ad altri elementi potrà essere ampliata in seguito con regole più specifiche.

### 2.1 Dichiarazione strutturata della matrice

Il blocco seguente è la **dichiarazione strutturata della matrice M1**, utilizzabile come fonte dei controlli e della tabella. Non è un blocco `ddta-ontology` e pertanto **non genera classi o proprietà OWL**. Le voci `reviewByDefault` elencano i valori **effettivi** per ogni classe; non vanno cumulati due volte con l'ereditarietà. La semantica di ciascuna riga è definita anche dalla motivazione nella matrice: una sigla senza contesto non indica l'oggetto materiale protetto.

```yaml security-applicability
module: security
status: approved
scope: [core, process]
policy: review-every-applicable-property
properties:
  C: security:Confidentiality
  I: security:Integrity
  A: security:Availability
  Au: security:Authenticity
  Az: security:Authorization
  Nr: security:NonRepudiation
rules:
  - {class: ddta:System, reviewByDefault: [C, I, A, Au, Az]}
  - {class: ddta:Function, reviewByDefault: [C, I, A, Au, Az]}
  - {class: ddta:Environment, reviewByDefault: [I, A, Az]}
  - {class: ddta:Resource, reviewByDefault: [C, I, A, Au, Az]}
  - {class: ddta:Contract, reviewByDefault: [I]}
  - {class: ddta:ContractElement, reviewByDefault: [C, I, Au, Az]}
  - {class: ddta:Store, reviewByDefault: [C, I, A, Au, Az]}
  - {class: ddta:StoredContent, reviewByDefault: [C, I, A, Au, Az]}
  - {class: ddta:Boundary, reviewByDefault: []}
  - {class: ddta:CommunicationFunction, reviewByDefault: [C, I, A, Au, Az, Nr]}
  - {class: ddta:CommunicationChannel, reviewByDefault: [C, I, A, Au, Az]}
  - {class: ddta:Process, reviewByDefault: [C, I, A, Au, Az]}
  - {class: ddta:ProcessStep, reviewByDefault: [C, I, A, Au, Az]}
  - {class: process:ProcessTransition, reviewByDefault: [I, A]}
  - {class: process:Condition, reviewByDefault: [I]}
  - {class: process:AtomicCondition, reviewByDefault: [I]}
  - {class: process:CompositeCondition, reviewByDefault: [I]}
  - {class: process:Operand, reviewByDefault: [C, I]}
  - {class: process:ControlNode, reviewByDefault: [C, I, A, Au, Az]}
  - {class: process:SynchronizationNode, reviewByDefault: [C, I, A, Au, Az]}
  - {class: process:CodeReference, reviewByDefault: [I, Au]}
```

### 2.2 Contributi da ontologie specializzate

L'estensione di M1 deve mantenere lo stesso significato di `R` e delle identità `SecurityProperty`. Per esempio, una `network:ChannelSection` potrà aggiungere il controllo dei meccanismi che proteggono il traffico **nel singolo tratto**; un `network:Router` potrà richiedere l'esame della disponibilità della risorsa e dell'integrità della configurazione. Questo non equivale a trasferire automaticamente le protezioni del tratto all'intero `CommunicationChannel`.

Una specializzazione può definire ulteriori classi e regole senza modificare le schede del CORE. Le regole aggiunte sono identificabili per modulo e classe, mentre l'esame rimane collegato **all'individuo RDF effettivo**. La valutazione di un oggetto composto non viene inferita semplicemente dalla valutazione di una sua parte, né il contrario.

## 3. Matrice M2 — completezza e precisione della documentazione

La matrice M1 (sezione 2) determina **quali proprietà di sicurezza devono essere esaminate** per ciascuna entità. La matrice M2 determina **quali aspetti della descrizione di un'entità devono ricevere una risposta documentale esplicita**, indipendentemente dal fatto che siano proprietà di sicurezza.

**Principio:** una mancanza documentale non è automaticamente una vulnerabilità; è un oggetto `security:DocumentationGap` da rendere visibile all'autore. Per questo `DocumentationGap` appartiene alla Security Ontology ma può riferirsi anche a un aspetto funzionale o architetturale. La lacuna può riguardare la descrizione di un'entità, una relazione non stabilita o l'insufficiente precisione di una specifica.

**La matrice non altera i vincoli del CORE e di Process.** In particolare `ddta:Function` può legittimamente non avere contratti di input/output, `ddta:Contract` può non elencare elementi e `ddta:Process` può non avere Step. La matrice richiede in tali casi una *risposta documentale esplicita*; non inventa le triple mancanti né introduce cardinalità minime OWL. Per le relazioni già obbligatorie, come sorgente e destinazione di un canale, un errore di validazione resta un errore anche quando è accompagnato da una lacuna.

Legenda: **E** = obbligo strutturale **già presente** nella guida CORE/Process; **R** = **obbligo aggiuntivo di revisione documentale**, soddisfacibile con informazione esistente o dichiarazione esplicita e motivata; **C** = controllo condizionale, attivato soltanto nel contesto indicato. Una cella `R` non significa che la relazione debba necessariamente essere asserita.

| Ontologia | Classe | Aspetto/documentazione da esaminare | Tipo | Esempio di esito insufficiente |
|---|---|---|:---:|---|
| CORE | `System` | Funzione primaria (`hasPrimaryFunction`) | **E** | Nessuna funzione primaria identificata |
| CORE | `Function` | **Decisione sul contratto di ingresso**: contratto definito, assenza intenzionale oppure decisione ancora aperta | **R** | `hasInputContract` assente senza decisione documentata; registrare una lacuna relativa alla decisione |
| CORE | `Function` | **Decisione sul contratto di uscita**: contratto definito, assenza intenzionale oppure decisione ancora aperta | **R** | `hasOutputContract` assente senza decisione documentata; registrare una lacuna relativa alla decisione |
| CORE | `Environment` | Risorse rese disponibili (`makesAvailable`, oppure dichiarazione sul livello di dettaglio) | **R** | Ambiente citato, risorse non caratterizzate |
| CORE | `Resource` | Ruolo e significato della risorsa nella descrizione | **R** | Risorsa nominata senza caratterizzazione sufficiente |
| CORE | `Contract` | **Decisione sul dettaglio degli elementi** (`hasContractElement`, oppure livello di decomposizione intenzionalmente non previsto) | **R** | Contratto definito, ma non è chiaro quali elementi debba ricevere o produrre la funzione |
| CORE | `ContractElement` | Molteplicità `minOccurs` / `maxOccurs` o esplicita mancata specificazione | **R** | Campo elencato ma obbligatorietà non chiara |
| CORE | `Store` | Contenuti o Store annidati (`stores`, oppure ambito non dettagliato motivato) | **R** | Non è chiaro che cosa lo Store conservi |
| CORE | `StoredContent` | Identità e relazione con lo Store, oppure contenuto deliberatamente non localizzato | **R** | Contenuto descritto senza contesto di conservazione |
| CORE | `Boundary` | Risorse incluse (`encloses`) o esplicita delimitazione soltanto concettuale | **R** | Confine nominato senza criterio di appartenenza |
| CORE | `CommunicationFunction` | Canale di comunicazione (`usesChannel`) o mancata scelta esplicitata | **R** | Non sappiamo quale canale sia previsto |
| CORE | `CommunicationChannel` | Estremo sorgente (`hasSource`) | **E** | Canale senza sorgente |
| CORE | `CommunicationChannel` | Estremo destinazione (`hasDestination`) | **E** | Canale senza destinazione |
| CORE | `Process` | Funzione realizzata (`realizesFunction`) o collegamento non ancora specificato | **R** | Processo senza ruolo funzionale chiarito |
| CORE | `Process` | Decomposizione (`hasStep`) o processo volutamente non dettagliato | **R** | Non è chiaro se gli Step siano sconosciuti o omessi intenzionalmente |
| CORE | `ProcessStep` | Appartenenza a un processo e collegamenti di flusso, quando il contesto richiede una vista operativa | **C** | Step isolato per errore, o terminalità non chiarita |
| PROCESS | `ProcessTransition` | Proprietario e Step sorgente/destinazione | **E** | Transizione priva di proprietario oppure di un estremo |
| PROCESS | `Condition` | Significato/criterio del controllo, quando usato in una guardia o attivazione | **C** | Nome della condizione senza significato interpretabile |
| PROCESS | `AtomicCondition` | Operando sinistro, destro e operatore di confronto | **E** | Confronto non formalmente determinato |
| PROCESS | `CompositeCondition` | Operatore logico e condizioni componenti | **E** | Condizione composta incompleta o ciclica |
| PROCESS | `Operand` | Riferimento risolvibile e tipo/semantica del valore, se previsto un confronto automatico | **C** | Locator ambiguo o riferimento a valore non determinato |
| PROCESS | `ControlNode` | Tipo di controllo, salvo la specializzazione di sincronizzazione | **E** | Nodo privo di `controlKind` riconosciuto |
| PROCESS | `SynchronizationNode` | `joinPolicy`, `completionCriterion` e `requiredCount` ove richiesto | **E** | Join privo di politica o soglia non valida |
| PROCESS | `CodeReference` | `repositoryLocator`, `sourcePath` e simbolo se necessario per la navigazione | **C** | Riferimento al metodo senza localizzazione navigabile |

Le righe **E** devono essere collegate ai controlli normativi già definiti nelle schede, senza duplicarne la semantica. Le righe **R/C** sono **regole aggiuntive di qualità documentale**, non requisiti funzionali nuovi del sistema. Per le righe **C**, un controllo non può attivarsi soltanto sulla presenza della classe: deve essere documentata e verificabile anche la condizione di applicazione. Un modulo specializzato potrà aggiungere righe M2 per i suoi elementi (per esempio estremi di `ChannelSection` e collegamenti di un `Router`) mantenendo la stessa classificazione E/R/C; soltanto vincoli già approvati in quel modulo possono essere indicati come **E**.

### 3.1 Differenza fra assenza, incompiutezza e imprecisione

| Tipo di lacuna | Definizione operativa | Rilevabilità iniziale |
|---|---|---|
| `MISSING` | Non è presente una risposta richiesta dalla matrice | Automatica, su un grafo selezionato e con regola esplicita |
| `INCOMPLETE` | Alcuni elementi richiesti della risposta sono presenti, altri no | Automatica quando la struttura attesa è formalizzata |
| `AMBIGUOUS` | La descrizione permette interpretazioni incompatibili o non univoche | Manuale, salvo pattern formali specifici |
| `INCONSISTENT` | Sono presenti dichiarazioni incompatibili rispetto a un vincolo dichiarato | Automatica per i vincoli formalizzati; resta anche l'eventuale errore di validazione |
| `UNVERIFIABLE` | La descrizione non ha precisione sufficiente per la verifica richiesta | Automatica solo con criteri di verificabilità espliciti, altrimenti manuale |

Non si presume che una generica procedura Python possa comprendere automaticamente l'ambiguità di qualsiasi testo naturale. Una lacuna può essere creata anche manualmente per difetti che non sono riconoscibili da regole deterministiche.

### 3.2 Risposta documentale esplicita

Per ciascun controllo M2 applicabile, l'autore deve poter registrare una risposta identificabile, senza asserire triple false e senza cancellare il controllo. Stati documentali:

- `DOCUMENTED`: l'informazione è presente e riconducibile a dichiarazioni o evidenze identificate;
- `EXPLICITLY_NONE`: per il caso specifico è dichiarata e motivata l'assenza intenzionale dell'elemento (per esempio una funzione senza ingressi informativi);
- `NOT_APPLICABLE`: il controllo non si applica al contesto, con motivazione;
- `IGNORED`: il controllo viene escluso intenzionalmente dall'esame, con motivazione; non significa completezza;
- `UNRESOLVED`: la risposta non è disponibile oppure resta insufficiente e deve essere rappresentata da una lacuna.

La classe `DocumentationReview` (scheda 9) collega una risposta esplicita alla coppia *(entità, ID controllo M2)*. È distinta da `SecurityReview`, che riguarda la coppia *(entità, proprietà di sicurezza)*.

Un valore `DOCUMENTED` non sostituisce il controllo sul contenuto: per esempio, per una riga **E** un'affermazione manuale non può rendere valido un canale privo di `hasDestination`. `EXPLICITLY_NONE` non può annullare un vincolo strutturale obbligatorio già approvato. Per le righe **R**, invece, un'assenza intenzionale esplicitata e motivata risolve il dubbio documentale senza creare un falso `Contract` o un falso `ProcessStep`.

**Caso particolare — contratti di `Function`.** La decisione sui contratti può essere espressa con le tre risposte leggibili `UNDECIDED`, `DEFINED`, `NONE`, senza introdurre un secondo vocabolario RDF indipendente:

| Risposta per la direzione | Stato M2 corrispondente | Semantica e conseguenza |
|---|---|---|
| `UNDECIDED` | `UNRESOLVED` | Non è stato deciso se serva un contratto; lacuna relativa alla decisione mancante |
| `DEFINED` | `DOCUMENTED` | Il contratto appropriato è dichiarato tramite `hasInputContract` oppure `hasOutputContract`; il relativo contenuto è soggetto a ulteriori controlli M2 |
| `NONE` | `EXPLICITLY_NONE` | È stata motivata l'assenza intenzionale del contratto per **questa direzione**; non si asserisce un contratto vuoto |

Le decisioni su input e output sono **indipendenti**. Se l'IRI della relazione contrattuale manca, **non** si presume `NONE`: in assenza di una decisione documentata il controllo è irrisolto. Se una dichiarazione `NONE` convive con una relazione `hasInputContract` o `hasOutputContract` verso un contratto effettivo, la documentazione è contraddittoria e deve essere riesaminata. Non si richiede a ogni funzione di produrre necessariamente un risultato informativo o di ricevere necessariamente dati; si richiede di esplicitare la scelta.


### 3.3 Dichiarazione strutturata della matrice M2

Il seguente blocco non è una dichiarazione OWL: definisce la matrice documentale M2 mediante identificatori stabili, classi interessate, aspetti e modalità di controllo. I controlli condizionali richiedono una condizione applicativa verificabile per l’esecuzione automatica; nessuna condizione non documentata può essere presunta.

```yaml documentation-completeness
module: security
status: approved
scope: [core, process]
policy: review-every-applicable-documentation-aspect
rules:
  - {id: DOC-SYS-PRIMARY, class: ddta:System, aspect: ddta:hasPrimaryFunction, mode: existing-mandatory}
  - {id: DOC-FUN-INPUT, class: ddta:Function, aspect: ddta:hasInputContract, mode: review, decision: independent-input}
  - {id: DOC-FUN-OUTPUT, class: ddta:Function, aspect: ddta:hasOutputContract, mode: review, decision: independent-output}
  - {id: DOC-ENV-RESOURCES, class: ddta:Environment, aspect: ddta:makesAvailable, mode: review}
  - {id: DOC-RESOURCE-ROLE, class: ddta:Resource, aspect: resource-description, mode: review}
  - {id: DOC-CON-ELEMENTS, class: ddta:Contract, aspect: ddta:hasContractElement, mode: review}
  - {id: DOC-CE-MIN, class: ddta:ContractElement, aspect: ddta:minOccurs, mode: review}
  - {id: DOC-CE-MAX, class: ddta:ContractElement, aspect: ddta:maxOccurs, mode: review}
  - {id: DOC-STORE-CONTENTS, class: ddta:Store, aspect: ddta:stores, mode: review}
  - {id: DOC-CONTENT-STORE, class: ddta:StoredContent, aspect: inverse-ddta:stores, mode: review}
  - {id: DOC-BOUNDARY-SCOPE, class: ddta:Boundary, aspect: ddta:encloses, mode: review}
  - {id: DOC-COMMF-CHANNEL, class: ddta:CommunicationFunction, aspect: ddta:usesChannel, mode: review}
  - {id: DOC-CHANNEL-SOURCE, class: ddta:CommunicationChannel, aspect: ddta:hasSource, mode: existing-mandatory}
  - {id: DOC-CHANNEL-DEST, class: ddta:CommunicationChannel, aspect: ddta:hasDestination, mode: existing-mandatory}
  - {id: DOC-PROC-FUNCTION, class: ddta:Process, aspect: ddta:realizesFunction, mode: review}
  - {id: DOC-PROC-STEPS, class: ddta:Process, aspect: ddta:hasStep, mode: review}
  - {id: DOC-STEP-FLOW, class: ddta:ProcessStep, aspect: step-context-and-flow, mode: conditional}
  - {id: DOC-TRANS-ENDPOINTS, class: process:ProcessTransition, aspect: transition-owner-and-endpoints, mode: existing-mandatory}
  - {id: DOC-COND-MEANING, class: process:Condition, aspect: criterion-description, mode: conditional}
  - {id: DOC-ATOMIC-COMPLETE, class: process:AtomicCondition, aspect: atomic-comparison-components, mode: existing-mandatory}
  - {id: DOC-COMPOSITE-COMPLETE, class: process:CompositeCondition, aspect: composite-logic-and-members, mode: existing-mandatory}
  - {id: DOC-OPERAND-RESOLVE, class: process:Operand, aspect: operand-resolution, mode: conditional}
  - {id: DOC-CONTROL-KIND, class: process:ControlNode, aspect: control-kind-or-specialization, mode: existing-mandatory}
  - {id: DOC-SYNC-SEMANTICS, class: process:SynchronizationNode, aspect: join-policy-and-criterion, mode: existing-mandatory}
  - {id: DOC-CODE-LOCATOR, class: process:CodeReference, aspect: navigable-code-reference, mode: conditional}
```

---

## 4. Scheda ontologica — `SecurityProperty`

### 4.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: security
iri: security:SecurityProperty
status: approved
label: {en: Security Property, it: Proprietà di sicurezza}
definition:
  en: An identifiable security objective that can be examined in relation to a DDTA entity.
  it: Un obiettivo di sicurezza identificabile che può essere esaminato rispetto a un'entità DDTA.
```

### 4.2 Individui del vocabolario

Le seguenti identità sono **individui** di `SecurityProperty`, non sei sottoclassi. Le definizioni indicano il significato generale; la loro applicabilità a un'entità specifica è descritta dalla matrice M1 e dalle dichiarazioni del sistema.

| IRI | Definizione (IT) | Definition (EN) |
|---|---|---|
| `security:Confidentiality` | Protezione delle informazioni dalla divulgazione non autorizzata | Protection of information against unauthorized disclosure |
| `security:Integrity` | Protezione da modifiche o alterazioni non autorizzate | Protection against unauthorized modification or alteration |
| `security:Availability` | Disponibilità dei servizi o delle informazioni quando richiesti dai soggetti autorizzati | Availability of services or information when required by authorized parties |
| `security:Authenticity` | Possibilità di stabilire l'autenticità di un'identità, origine o informazione pertinente | Ability to establish the authenticity of a relevant identity, origin or information |
| `security:Authorization` | Rispetto delle autorizzazioni definite per soggetti e operazioni | Enforcement of defined permissions for subjects and operations |
| `security:NonRepudiation` | Possibilità di disporre di evidenze attribuibili che contrastino la negazione di un'azione pertinente | Availability of attributable evidence against denial of a relevant action |

Gli individui sono dichiarati in un blocco `yaml ddta-ontology` con `record: named-individuals`. Il generatore Turtle dovrà riconoscere questo tipo di record; la presenza della dichiarazione non implica che il generatore sia già implementato.

```yaml ddta-ontology
record: named-individuals
module: security
status: approved
class: security:SecurityProperty
individuals:
  - {iri: security:Confidentiality, label: {en: Confidentiality, it: Riservatezza}}
  - {iri: security:Integrity, label: {en: Integrity, it: Integrità}}
  - {iri: security:Availability, label: {en: Availability, it: Disponibilità}}
  - {iri: security:Authenticity, label: {en: Authenticity, it: Autenticità}}
  - {iri: security:Authorization, label: {en: Authorization, it: Autorizzazione}}
  - {iri: security:NonRepudiation, label: {en: Non-repudiation, it: Non ripudiabilità}}
```

### 4.3 Interpretazione

L'individuo `Integrity` identifica una proprietà, non un controllo di integrità e non un problema `Tampering`. La stessa proprietà può essere esaminata per uno `Store`, uno `StoredContent` o un `ProcessTransition`, con significati contestuali distinti. Nessuna relazione di protezione viene inferita automaticamente da `stores`, `usesChannel` o `hasStep`.

---

## 5. Scheda ontologica — `SecurityReview`

### 5.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: security
iri: security:SecurityReview
status: approved
label: {en: Security Review, it: Esame di sicurezza}
definition:
  en: A documented statement about the applicability and declared protection status of one security property in the context of one identified DDTA entity, including a protection service offered to data transported by a channel.
  it: Una dichiarazione documentale sull'applicabilità e sullo stato dichiarato della protezione di una proprietà di sicurezza riferita a una singola entità DDTA identificata; su un canale può riguardare il servizio di protezione offerto al traffico.
```

### 5.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: security
owner: security:SecurityReview
properties:
  - iri: security:reviewsEntity
    status: approved
    domain: security:SecurityReview
    range: owl:Thing
    label: {en: reviews entity, it: esamina entità}
    definition:
      en: Identifies the DDTA entity to which this review refers.
      it: Identifica l'entità DDTA cui si riferisce l'esame.
  - iri: security:reviewsProperty
    status: approved
    domain: security:SecurityReview
    range: security:SecurityProperty
    label: {en: reviews property, it: esamina proprietà}
    definition:
      en: Identifies the security property reviewed for that entity or context.
      it: Identifica la proprietà di sicurezza esaminata per l'entità o il contesto.
  - iri: security:declaresControl
    status: approved
    domain: security:SecurityReview
    range: security:SecurityControl
    label: {en: declares control, it: dichiara controllo}
    definition:
      en: Associates the review with a security control declared for the examined property.
      it: Associa l'esame a un controllo di sicurezza dichiarato per la proprietà esaminata.
```

```yaml ddta-ontology
record: datatype-properties
module: security
owner: security:SecurityReview
properties:
  - iri: security:reviewDecision
    status: approved
    domain: security:SecurityReview
    range: xsd:string
    label: {en: review decision, it: decisione di esame}
    definition:
      en: Controlled applicability decision PENDING, REQUIRED, NOT_APPLICABLE or IGNORED.
      it: Decisione controllata di applicabilità PENDING, REQUIRED, NOT_APPLICABLE oppure IGNORED.
  - iri: security:protectionStatus
    status: approved
    domain: security:SecurityReview
    range: xsd:string
    label: {en: protection documentation status, it: stato documentale della protezione}
    definition:
      en: Controlled state UNSPECIFIED, DECLARED_PRESENT or DECLARED_ABSENT.
      it: Stato controllato UNSPECIFIED, DECLARED_PRESENT oppure DECLARED_ABSENT.
  - iri: security:reviewRationale
    status: approved
    domain: security:SecurityReview
    range: xsd:string
    label: {en: review rationale, it: motivazione dell'esame}
    definition:
      en: Explanation supplied for a security review, including non-applicability or intentional exclusion.
      it: Spiegazione fornita per l'esame di sicurezza, inclusi non applicabilità o esclusione intenzionale.
  - iri: security:evidenceReference
    status: approved
    domain: security:SecurityReview
    range: xsd:string
    label: {en: evidence reference, it: riferimento documentale}
    definition:
      en: Reference to documentation supporting a declaration about a protection.
      it: Riferimento alla documentazione che sostiene una dichiarazione sulla protezione.
```

### 5.3 Significato degli stati

| Asse | Valore | Significato |
|---|---|---|
| Applicabilità | `PENDING` | Non è presente una decisione documentata sull'applicabilità |
| Applicabilità | `REQUIRED` | La proprietà è dichiarata richiesta per l'entità |
| Applicabilità | `NOT_APPLICABLE` | La proprietà è dichiarata non pertinente in questo caso, con motivazione |
| Applicabilità | `IGNORED` | La proprietà viene intenzionalmente esclusa dall'esame, con motivazione; non implica sicurezza |
| Protezione | `UNSPECIFIED` | Non sono disponibili informazioni sufficienti sulla protezione |
| Protezione | `DECLARED_PRESENT` | È dichiarata la presenza di un meccanismo protettivo, non necessariamente verificato |
| Protezione | `DECLARED_ABSENT` | È dichiarata esplicitamente l'assenza della protezione |

I due assi non vanno confusi. Una decisione `NOT_APPLICABLE` non indica che la protezione è assente. `DECLARED_ABSENT` non è una lacuna: è un'informazione dichiarata. `DECLARED_PRESENT` non equivale a «garantita». Una successiva ontologia potrà descrivere verifiche tecniche, ma non è necessaria per questa scheda.

### 5.4 Vincoli documentali

- La revisione si riferisce a **una** entità e a **una** proprietà di sicurezza.
- Una coppia *(entità, proprietà)* deve avere una risposta coerente; risposte contraddittorie devono essere rilevate.
- `NOT_APPLICABLE` e `IGNORED` richiedono motivazione.
- `DECLARED_PRESENT` richiede una descrizione, un riferimento documentale o un `SecurityControl` identificato, senza presumerne l'efficacia. Un controllo collegato deve essere coerente con l'oggetto e la proprietà esaminati.
- Quando M1 richiede la revisione, l'assenza di risposta o `UNSPECIFIED` comporta una `DocumentationGap`; non comporta `DECLARED_ABSENT`.
- Gli insiemi controllati di valori devono essere vincolati dalla validazione documentale (per esempio con SHACL), non dal solo `range: xsd:string`.

---

## 6. Scheda ontologica — `DocumentationGap`

### 6.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: security
iri: security:DocumentationGap
status: approved
label: {en: Documentation Gap, it: Lacuna documentale}
definition:
  en: An identified insufficiency or uncertainty in the documentation of an entity, relationship or security property, without asserting that the undocumented fact is false.
  it: Una insufficienza o incertezza identificata nella documentazione di un'entità, relazione o proprietà di sicurezza, senza affermare che un fatto non documentato sia falso.
```

La Security Ontology definisce le due specializzazioni `EntityDocumentationGap` e `RelationDocumentationGap`. Le relative identità appartengono al namespace `security:` e sono dichiarate direttamente nelle schede seguenti.

```yaml ddta-ontology
record: class
module: security
iri: security:EntityDocumentationGap
status: approved
subClassOf: security:DocumentationGap
label: {en: Entity Documentation Gap, it: Lacuna documentale di entità}
definition:
  en: A documentation gap concerning an entity or a declared aspect of its description.
  it: Una lacuna documentale relativa a un'entità o a un aspetto identificato della sua descrizione.
```

```yaml ddta-ontology
record: class
module: security
iri: security:RelationDocumentationGap
status: approved
subClassOf: security:DocumentationGap
label: {en: Relation Documentation Gap, it: Lacuna documentale di relazione}
definition:
  en: A documentation gap concerning whether a specified relationship between identified endpoints is established.
  it: Una lacuna documentale relativa al fatto che sia stabilita una relazione specifica fra estremi identificati.
```

### 6.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: security
owner: security:DocumentationGap
properties:
  - iri: security:concernsEntity
    status: approved
    domain: security:DocumentationGap
    range: owl:Thing
    label: {en: concerns entity, it: riguarda entità}
    definition:
      en: Identifies the entity whose description contains a gap.
      it: Identifica l'entità della cui descrizione è stata rilevata una lacuna.
  - iri: security:concernsReview
    status: approved
    domain: security:DocumentationGap
    range: security:SecurityReview
    label: {en: concerns security review, it: riguarda esame di sicurezza}
    definition:
      en: Associates a gap with a security review, when the missing information concerns a security property.
      it: Associa una lacuna a un esame di sicurezza quando manca un'informazione relativa a una proprietà di sicurezza.
  - iri: security:concernsSecurityProperty
    status: approved
    domain: security:DocumentationGap
    range: security:SecurityProperty
    label: {en: concerns security property, it: riguarda proprietà di sicurezza}
    definition:
      en: Identifies the security property for which the documentation is insufficient even if no review is stated.
      it: Identifica la proprietà di sicurezza la cui documentazione è insufficiente, anche senza un esame dichiarato.
  - iri: security:gapPredicate
    status: approved
    domain: security:DocumentationGap
    range: rdf:Property
    label: {en: questioned predicate, it: predicato non documentato}
    definition:
      en: Identifies the RDF predicate whose documentation is missing or uncertain, without asserting the corresponding relation.
      it: Identifica il predicato RDF la cui documentazione è mancante o incerta, senza asserire la relativa relazione.
  - iri: security:gapSource
    status: approved
    domain: security:RelationDocumentationGap
    range: owl:Thing
    label: {en: questioned source, it: sorgente della relazione incerta}
    definition:
      en: Identifies the subject of an unresolved candidate relationship.
      it: Identifica il soggetto di una relazione candidata non stabilita.
  - iri: security:gapTarget
    status: approved
    domain: security:RelationDocumentationGap
    range: owl:Thing
    label: {en: questioned target, it: destinazione della relazione incerta}
    definition:
      en: Identifies the object of an unresolved candidate relationship.
      it: Identifica l'oggetto di una relazione candidata non stabilita.
```

```yaml ddta-ontology
record: datatype-properties
module: security
owner: security:DocumentationGap
properties:
  - iri: security:gapKind
    status: approved
    domain: security:DocumentationGap
    range: xsd:string
    label: {en: gap kind, it: tipo di lacuna}
    definition:
      en: Controlled kind MISSING, INCOMPLETE, AMBIGUOUS, INCONSISTENT or UNVERIFIABLE.
      it: Categoria controllata MISSING, INCOMPLETE, AMBIGUOUS, INCONSISTENT oppure UNVERIFIABLE.
  - iri: security:concernsDocumentationRule
    status: approved
    domain: security:DocumentationGap
    range: xsd:string
    label: {en: concerns documentation rule, it: riguarda controllo documentale}
    definition:
      en: Identifies the M2 rule whose documentation is insufficient, when applicable.
      it: Identifica il controllo M2 la cui documentazione è insufficiente, quando pertinente.
```

### 6.3 Distinzione tra due forme di lacuna

- **Proprietà senza valore dichiarato:** se `PatientDataChannel` non specifica `ddta:hasSource`, sappiamo quale relazione necessita documentazione ma non conosciamo la sorgente. È una `EntityDocumentationGap` su `PatientDataChannel`, collegata a `ddta:hasSource` mediante `gapPredicate`. **Non** si inventa una risorsa sorgente per riempire `gapTarget`.
- **Relazione specifica incerta:** se sono noti soggetto, predicato e oggetto, ma non è stabilito se la loro relazione valga, usiamo `RelationDocumentationGap` con `gapSource`, `gapPredicate`, `gapTarget`. Questo **non** asserisce la relazione candidata.

Una lacuna di sicurezza può inoltre indicare `concernsSecurityProperty`, oppure `concernsReview` se un esame è già documentato. I due collegamenti non vanno usati per creare copie della medesima lacuna. `rdfs:label` descrive la lacuna; il testo della didascalia non ne costituisce l'identità.

### 6.4 Vincoli documentali

- Ogni lacuna possiede una descrizione (`rdfs:label`) non vuota.
- `EntityDocumentationGap` deve identificare l'entità interessata; se pertinente, il predicato o la proprietà di sicurezza mancante.
- `RelationDocumentationGap` deve identificare sorgente, predicato e destinazione della relazione non stabilita.
- I campi relativi al controllo M2 e alla proprietà CIA³-R sono alternativi o combinabili solo con semantica non contraddittoria.
- Una lacuna non dimostra un fatto negativo e non sostituisce gli errori di validazione definiti da CORE e Process.

---

## 7. Scheda ontologica — `SecurityIssueType`

### 7.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: security
iri: security:SecurityIssueType
status: approved
label: {en: Security Issue Type, it: Tipo di problema di sicurezza}
definition:
  en: An identifiable category used to classify a potential security issue independently of the security property it may affect.
  it: Una categoria identificabile che classifica un possibile problema di sicurezza separatamente dalla proprietà che può essere compromessa.
```

### 7.2 Vocabolario dei tipi di problema

Le sei categorie STRIDE possono essere rappresentate come **individui** di `SecurityIssueType`, senza creare automaticamente una sottoclasse per ognuna.

| Individuo | Tipo di problema | Proprietà CIA³-R usualmente associata |
|---|---|---|
| `security:Spoofing` | Impersonificazione | Authenticity |
| `security:Tampering` | Alterazione non autorizzata | Integrity |
| `security:Repudiation` | Negazione dell'azione | NonRepudiation |
| `security:InformationDisclosure` | Divulgazione non autorizzata | Confidentiality |
| `security:DenialOfService` | Interruzione o degradazione del servizio | Availability |
| `security:ElevationOfPrivilege` | Uso di privilegi non autorizzati | Authorization |

Un tipo più specifico, come `ManInTheMiddle`, potrà essere descritto senza cambiare la classe generale. **La tabella non è una regola di inferenza automatica**: un problema concreto può interessare più proprietà e richiede una motivazione riferita al sistema.

```yaml ddta-ontology
record: named-individuals
module: security
status: approved
class: security:SecurityIssueType
individuals:
  - {iri: security:Spoofing, label: {en: Spoofing, it: Impersonificazione}}
  - {iri: security:Tampering, label: {en: Tampering, it: Alterazione non autorizzata}}
  - {iri: security:Repudiation, label: {en: Repudiation, it: Ripudio dell'azione}}
  - {iri: security:InformationDisclosure, label: {en: Information disclosure, it: Divulgazione non autorizzata}}
  - {iri: security:DenialOfService, label: {en: Denial of service, it: Negazione del servizio}}
  - {iri: security:ElevationOfPrivilege, label: {en: Elevation of privilege, it: Elevazione dei privilegi}}
```

---

## 8. Scheda ontologica — `SecuritySignal`

### 8.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: security
iri: security:SecuritySignal
status: approved
label: {en: Security Signal, it: Segnale di sicurezza}
definition:
  en: An identifiable observation indicating a possible security issue for one or more DDTA entities, without asserting that an attack occurred or that a vulnerability is proven.
  it: Un'osservazione identificabile che segnala un possibile problema di sicurezza relativo a una o più entità DDTA, senza affermare l'avvenimento di un attacco o la dimostrazione di una vulnerabilità.
```

### 8.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: security
owner: security:SecuritySignal
properties:
  - iri: security:signalConcernsEntity
    status: approved
    domain: security:SecuritySignal
    range: owl:Thing
    label: {en: signal concerns entity, it: segnala problema per entità}
    definition:
      en: Identifies a DDTA entity implicated by the signal.
      it: Identifica un'entità DDTA interessata dalla segnalazione.
  - iri: security:hasIssueType
    status: approved
    domain: security:SecuritySignal
    range: security:SecurityIssueType
    label: {en: has issue type, it: ha tipo di problema}
    definition:
      en: Identifies the issue category of a security signal.
      it: Identifica la categoria di problema segnalata.
  - iri: security:affectsProperty
    status: approved
    domain: security:SecuritySignal
    range: security:SecurityProperty
    label: {en: affects property, it: interessa proprietà}
    definition:
      en: Identifies a security property potentially affected by the issue.
      it: Identifica una proprietà di sicurezza potenzialmente interessata dal problema.
```

```yaml ddta-ontology
record: datatype-properties
module: security
owner: security:SecuritySignal
properties:
  - iri: security:signalRationale
    status: approved
    domain: security:SecuritySignal
    range: xsd:string
    label: {en: signal rationale, it: motivazione del segnale}
    definition:
      en: Documented reason for considering this possible issue relevant to the identified entities.
      it: Motivazione documentata della pertinenza del possibile problema per le entità indicate.
```

### 8.3 Interpretazione

- Un `SecuritySignal` non è una `DocumentationGap`: il primo indica una possibile situazione di pericolo, la seconda una informazione mancante o incerta.
- Un `SecuritySignal` non deve essere dedotto automaticamente dalla sola presenza di `DECLARED_ABSENT`: serve una motivazione contestuale (per esempio una proprietà richiesta o un comportamento rilevante).
- Un `SecuritySignal` può indicare più entità o proprietà interessate, senza inventare nuove classi OWL per ogni tipo di problema.
- La visualizzazione di un segnale non ne determina il significato ontologico.

---

## 9. Scheda ontologica — `DocumentationReview`

### 9.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: security
iri: security:DocumentationReview
status: approved
label: {en: Documentation Review, it: Esame documentale}
definition:
  en: An identifiable statement giving an explicit answer about one documentation aspect required by a named completeness rule for a DDTA entity.
  it: Una dichiarazione identificabile che fornisce una risposta esplicita su un aspetto documentale richiesto da un controllo di completezza identificato, relativo a un'entità DDTA.
```

La classe serve per distinguere, nella matrice M2, **relazione effettivamente dichiarata**, **assenza intenzionale di una relazione facoltativa** e **risposta mancante**. Non descrive un workflow di revisione né un ciclo di vita.

### 9.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: security
owner: security:DocumentationReview
properties:
  - iri: security:documentationEntity
    status: approved
    domain: security:DocumentationReview
    range: owl:Thing
    label: {en: documentation entity, it: entità esaminata}
    definition:
      en: Identifies the DDTA entity covered by the documentation response.
      it: Identifica l'entità DDTA cui si riferisce la risposta documentale.
```

```yaml ddta-ontology
record: datatype-properties
module: security
owner: security:DocumentationReview
properties:
  - iri: security:documentationRuleId
    status: approved
    domain: security:DocumentationReview
    range: xsd:string
    label: {en: documentation rule identifier, it: identificatore controllo documentale}
    definition:
      en: Identifier of the M2 completeness rule answered by this statement.
      it: Identificatore del controllo M2 cui risponde la dichiarazione.
  - iri: security:documentationResponse
    status: approved
    domain: security:DocumentationReview
    range: xsd:string
    label: {en: documentation response, it: risposta documentale}
    definition:
      en: Controlled response DOCUMENTED, EXPLICITLY_NONE, NOT_APPLICABLE, IGNORED or UNRESOLVED.
      it: Risposta controllata DOCUMENTED, EXPLICITLY_NONE, NOT_APPLICABLE, IGNORED oppure UNRESOLVED.
  - iri: security:documentationRationale
    status: approved
    domain: security:DocumentationReview
    range: xsd:string
    label: {en: documentation rationale, it: motivazione documentale}
    definition:
      en: Explanation of the chosen documentation response, when necessary.
      it: Spiegazione della risposta documentale adottata, quando necessaria.
```

### 9.3 Interpretazione e vincoli documentali

Una `DocumentationReview` identifica la coppia *(entità, controllo M2)*. Il valore `DOCUMENTED` non può rendere valida una struttura incompatibile con le schede CORE/Process. `EXPLICITLY_NONE` è utilizzabile solo quando l'assenza dell'aspetto è ammessa dalle regole applicabili. `NOT_APPLICABLE` e `IGNORED` richiedono motivazione. `UNRESOLVED` registra che la risposta è ancora insufficiente. Se un controllo è applicabile ma non riceve risposta sufficiente, la matrice richiede una `DocumentationGap`.

---

## 10. Scheda ontologica — `SecurityControl`

### 10.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: security
iri: security:SecurityControl
status: approved
label: {en: Security Control, it: Controllo di sicurezza}
definition:
  en: >-
    An identifiable planned or declared protection intended to address
    a security property for a specified entity. Its declaration does not
    establish effectiveness or successful execution.
  it: >-
    Una protezione prevista o dichiarata e identificabile, destinata ad
    affrontare una proprietà di sicurezza per un'entità specificata.
    La dichiarazione non dimostra efficacia né avvenuta esecuzione.
```

### 10.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: security
owner: security:SecurityControl
properties:
  - iri: security:protectsEntity
    status: approved
    domain: security:SecurityControl
    range: owl:Thing
    label: {en: protects entity, it: protegge entità}
    definition:
      en: Identifies the entity whose security property this control is intended to protect.
      it: Identifica l'entità la cui proprietà di sicurezza il controllo intende proteggere.
  - iri: security:addressesProperty
    status: approved
    domain: security:SecurityControl
    range: security:SecurityProperty
    label: {en: addresses property, it: affronta proprietà}
    definition:
      en: Identifies the security property targeted by the control.
      it: Identifica la proprietà di sicurezza affrontata dal controllo.
  - iri: security:implementedThrough
    status: approved
    domain: security:SecurityControl
    range: security:ProtectionApplication
    label: {en: implemented through, it: attuato tramite}
    definition:
      en: Associates a control with an application of a protection mechanism in a specified scope.
      it: Associa un controllo a un'applicazione di un meccanismo di protezione in un ambito specificato.
```

### 10.3 Interpretazione e cardinalità documentali

- `protectsEntity`: **1..1**, per mantenere identificato senza ambiguità l'oggetto protetto.
- `addressesProperty`: **1..1**, per mantenere identificata la proprietà interessata. Se un meccanismo protegge più proprietà o più dati, si possono dichiarare più controlli, anche riferiti alle stesse applicazioni di protezione.
- `implementedThrough`: **0..***. Una protezione dichiarata può non precisare ancora la realizzazione; più applicazioni possono contribuire allo stesso obiettivo.
- La presenza di un `SecurityControl` non equivale a una dichiarazione `VERIFIED` e non rende vera automaticamente una promessa di protezione.
- Non si deduce da un controllo applicato a una parte la protezione dell'intero oggetto composto, né la protezione di ogni parte dal solo controllo generale.

---

## 11. Scheda ontologica — `ProtectionApplication`

### 11.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: security
iri: security:ProtectionApplication
status: approved
label: {en: Protection Application, it: Applicazione di protezione}
definition:
  en: >-
    An identifiable application of a protection mechanism to a declared
    operational scope, distinct from the security objective and from the
    resource or data being protected.
  it: >-
    Un'applicazione identificabile di un meccanismo di protezione a un
    ambito operativo dichiarato, distinta dall'obiettivo di sicurezza e
    dalla risorsa o dal dato che si intende proteggere.
```

### 11.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: security
owner: security:ProtectionApplication
properties:
  - iri: security:hasProtectionScope
    status: approved
    domain: security:ProtectionApplication
    range: owl:Thing
    label: {en: has protection scope, it: ha ambito di protezione}
    definition:
      en: Identifies the DDTA entity or specialized network element where protection is applied.
      it: Identifica l'entità DDTA o l'elemento di rete specializzato cui si applica la protezione.
  - iri: security:usesImplementationResource
    status: approved
    domain: security:ProtectionApplication
    range: ddta:Resource
    label: {en: uses implementation resource, it: utilizza risorsa di realizzazione}
    definition:
      en: Identifies a technical resource involved in applying the protection, when declared.
      it: Identifica una risorsa tecnica coinvolta nell'applicazione della protezione, quando dichiarata.
```

```yaml ddta-ontology
record: datatype-properties
module: security
owner: security:ProtectionApplication
properties:
  - iri: security:mechanismDescription
    status: approved
    domain: security:ProtectionApplication
    range: xsd:string
    label: {en: mechanism description, it: descrizione del meccanismo}
    definition:
      en: Describes the applied mechanism without requiring a specialized algorithm taxonomy.
      it: Descrive il meccanismo applicato senza richiedere una tassonomia degli algoritmi.
```

### 11.3 Interpretazione

- `hasProtectionScope` collega l'applicazione a **uno o più elementi individuati**, ad esempio un intero `CommunicationChannel`, una futura `network:ChannelSection` o una risorsa tecnica. L'ambito esatto deve essere comprensibile dalla descrizione; la sola indicazione di un canale aggregato non prova la copertura di tutti i suoi tratti.
- `usesImplementationResource` (**0..***) collega risorse implementative, ad esempio un router. Non equivale a `protectsEntity`: il router può applicare una protezione a un dato senza essere il dato protetto.
- `mechanismDescription` (**0..1** come vincolo documentale) può identificare un tunnel di rete, un controllo applicativo, un protocollo o altro meccanismo, senza anticipare una tassonomia crittografica. Una futura ontologia specifica potrà aggiungere un IRI del meccanismo senza modificare le classi CORE.
- Una sovrapposizione si riferisce a **porzioni comuni della copertura** sul medesimo oggetto e rispetto a una determinata proprietà. La complementarità riguarda coperture o aspetti differenti che contribuiscono a un medesimo obiettivo. Nessuna di queste relazioni implica automaticamente indipendenza, efficacia o incremento misurabile della sicurezza.
- Se la descrizione delle sezioni di rete non esiste, il modello può dichiarare i controlli e i loro ambiti noti, ma **non può dedurre deterministici dettagli di copertura che il grafo non contiene**.

---

## 12. Esempio concettuale — `CommunicationChannel`

Un canale può avere insieme **un fatto CORE**, **una lacuna strutturale**, **dichiarazioni sui servizi di protezione del traffico** e **una lacuna di sicurezza**. Un requisito d'integrità di un contenuto che attraversa il canale resta riferito al dato, non alla natura del canale.

| Aspetto di `PatientDataChannel` | Informazione disponibile | Rappresentazione ontologica |
|---|---|---|
| Destinazione | `ClinicalService` nota | `ddta:hasDestination` |
| Sorgente | Non documentata | `EntityDocumentationGap` su `ddta:hasSource` |
| Confidentiality | Protezione dichiarata presente | `SecurityReview` con `DECLARED_PRESENT` |
| Integrity | Protezione di integrità del traffico dichiarata assente | `SecurityReview` del **servizio di trasporto** con `DECLARED_ABSENT`; non nega altri controlli applicativi sui dati |
| Availability | Non documentata | `SecurityReview` con `UNSPECIFIED` e `DocumentationGap` |
| Authenticity e Authorization | Ancora senza risposta | Rimangono aspetti da documentare secondo M1 |

```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix security: <https://w3id.org/ddta/security#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <https://example.org/ddta/security-example#> .

ex:ClinicalService a ddta:Resource .
ex:PatientDataChannel a ddta:CommunicationChannel ;
    ddta:hasDestination ex:ClinicalService .

ex:MissingChannelSource a security:EntityDocumentationGap ;
    security:concernsEntity ex:PatientDataChannel ;
    security:gapPredicate ddta:hasSource ;
    security:gapKind "MISSING" ;
    rdfs:label "Sorgente del canale non documentata"@it .

ex:ChannelConfidentiality a security:SecurityReview ;
    security:reviewsEntity ex:PatientDataChannel ;
    security:reviewsProperty security:Confidentiality ;
    security:reviewDecision "REQUIRED" ;
    security:protectionStatus "DECLARED_PRESENT" ;
    security:evidenceReference "Specifica del canale: protezione dichiarata" .

ex:ChannelIntegrity a security:SecurityReview ;
    security:reviewsEntity ex:PatientDataChannel ;
    security:reviewsProperty security:Integrity ;
    security:reviewDecision "REQUIRED" ;
    security:protectionStatus "DECLARED_ABSENT" .

ex:ChannelAvailability a security:SecurityReview ;
    security:reviewsEntity ex:PatientDataChannel ;
    security:reviewsProperty security:Availability ;
    security:reviewDecision "REQUIRED" ;
    security:protectionStatus "UNSPECIFIED" .
ex:MissingAvailability a security:EntityDocumentationGap ;
    security:concernsEntity ex:PatientDataChannel ;
    security:concernsReview ex:ChannelAvailability ;
    security:concernsSecurityProperty security:Availability ;
    security:gapKind "MISSING" ;
    rdfs:label "Protezione della disponibilità non documentata"@it .
```

*Esempio illustrativo, non dichiarazione RDF del progetto reale.* Non esiste un individuo `Contract` inventato per il canale: i contratti di input/output si riferiscono alle funzioni. L'assenza di `hasSource` viola anche la completezza strutturale CORE; annotare la lacuna non annulla l'errore.

### 12.1 Esempio di coperture parzialmente sovrapposte

Supponiamo che un documento identificato da `ddta:ContractElement` sia protetto con un meccanismo applicativo fra il PC e l'utente, mentre un tunnel di rete protegga il traffico soltanto tra Router 1 e Router 2.

| Applicazione | Oggetto di riferimento | Ambito dichiarato | Interpretazione |
|---|---|---|---|
| Protezione applicativa | Contenuto del documento | Applicazioni PC e User | Può coprire la comunicazione fra applicazioni secondo il meccanismo usato |
| Tunnel di rete | Traffico che contiene il documento | Collegamento Router 1–Router 2 | Protegge il tratto dichiarato, non automaticamente i segmenti esterni |

**La zona comune di copertura** è il tratto Router 1–Router 2, ma solo per le proprietà che entrambi i meccanismi effettivamente intendono proteggere. La cifratura non autenticata, da sola, non documenta protezione dell'integrità. Le relazioni d'ambito potranno riferirsi in futuro a entità `network:` senza cambiare `ddta:CommunicationChannel`.

La stessa protezione logica può dichiarare due applicazioni distinte. Il seguente Turtle è **puramente illustrativo** e assume che `ex:DocumentContent` e gli ambiti indicati siano identità del sistema già dichiarate altrove:

```turtle
@prefix security: <https://w3id.org/ddta/security#> .
@prefix ex: <https://example.org/ddta/security-example#> .

ex:DocumentConfidentialityControl a security:SecurityControl ;
    security:protectsEntity ex:DocumentContent ;
    security:addressesProperty security:Confidentiality ;
    security:implementedThrough ex:ApplicationLayerProtection,
                                ex:NetworkTunnelProtection .

ex:ApplicationLayerProtection a security:ProtectionApplication ;
    security:hasProtectionScope ex:PCToUserApplicationScope ;
    security:mechanismDescription "Protezione applicativa del contenuto" .

ex:NetworkTunnelProtection a security:ProtectionApplication ;
    security:hasProtectionScope ex:RouterToRouterScope ;
    security:mechanismDescription "Tunnel di rete protetto" .
```

La presenza degli IRI `PCToUserApplicationScope` e `RouterToRouterScope` in questo esempio **non definisce** nuove classi di topologia: servono solo a indicare ambiti specificati dal progetto. Una singola `ProtectionApplication` può essere richiamata da controlli diversi quando il medesimo meccanismo dichiara di affrontare più proprietà per lo stesso oggetto; ciò non attribuisce automaticamente le proprietà al meccanismo.

Questo esempio non asserisce che un `SecurityControl` sia stato verificato, né introduce nuovi tipi di router, switch o algoritmo nella Security Ontology.

---

## 13. Vincoli di completezza e coerenza documentale

| ID | Oggetto | Regola |
|---|---|---|
| `SEC-RVW-01` | SecurityReview | Una entità e una proprietà per dichiarazione; insiemi controllati per decisione e stato |
| `SEC-RVW-02` | SecurityReview | Per `NOT_APPLICABLE` / `IGNORED` motivazione obbligatoria |
| `SEC-RVW-03` | SecurityReview | `DECLARED_PRESENT` richiede indicazione documentale del meccanismo |
| `SEC-GAP-01` | DocumentationGap | Didascalia non vuota e riferimento all'aspetto mancante |
| `SEC-GAP-02` | RelationDocumentationGap | Due estremi e predicato identificati, senza asserire la relazione candidata |
| `SEC-SIG-01` | SecuritySignal | Tipo di problema e motivazione identificabili |
| `SEC-DOC-01` | DocumentationReview | Coppia entità/ID M2 e risposta coerente, motivazione per le esclusioni |
| `SEC-M1-01` | Matrice M1 | Coppie dovute prive di risposta sufficiente individuabili come gap, con ereditarietà e namespace di estensione |
| `SEC-M2-01` | Matrice M2 | Aspetti dovuti privi di risposta sufficiente individuabili come gap |
| `SEC-CTRL-01` | SecurityControl | Oggetto protetto e proprietà interessata identificati; `implementedThrough` 0..* |
| `SEC-APP-01` | ProtectionApplication | Ambito dichiarato coerente con quanto è effettivamente specificato, senza dedurre protezione dell'intero percorso |

Questi sono **vincoli documentali della specifica**. La loro implementazione mediante Shape SHACL, query o controlli deterministici è distinta dall’approvazione del modello ontologico. Nessun controllo è dichiarato già eseguibile soltanto perché compare in questa tabella.

---
