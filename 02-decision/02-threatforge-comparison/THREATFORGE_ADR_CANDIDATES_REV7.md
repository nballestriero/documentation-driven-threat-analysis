# ThreatForge / DDTA Decision candidates after Revision 7 regression

> **Non-canonical research rewrite.**
>
> This document does not patch ThreatForge. It rewrites the sixteen historical construction slots after the Revision 7 regression. A slot may remain a ThreatForge Decision, move to another semantic owner/layer, keep its parent unresolved, or cease to be a standalone Decision.

## Reading rule

The canonical Decision-specific semantic shape remains:

```text
Decision
|- title
|- context
|- decision
`- consequences
```

Each section below also carries **study annotations** (`Disposition`, `Semantic owner`, `Proposed parent`, `DDTA contract supported`). These annotations exist only to evaluate layering and ownership. They are **not proposed fields of the Decision model**.

## Corrected construction corpus

## MR-0001 / ADR-0001

**Disposition:** Relocated Decision candidate

**Semantic owner:** DDTA method

**Proposed parent:** Not assigned inside the ThreatForge MR hierarchy

**DDTA contract supported / related:** Document classification policy (method-level candidate)

### Title

Diátaxis come classificazione comune della funzione documentale

### Context

Una documentazione governata usata in progetti diversi deve permettere a lettori e strumenti di riconoscere la funzione editoriale di un documento senza dover apprendere ogni volta una classificazione proprietaria. Il metodo deve quindi scegliere se proporre una classificazione comune oppure lasciare interamente ai singoli progetti la distinzione fra materiale per apprendere, eseguire un compito, consultare un riferimento o comprendere un argomento.

### Decision

Il metodo DDTA adotta Diátaxis come classificazione comune della funzione editoriale dei documenti, distinguendo tutorial, how-to guide, reference ed explanation secondo il bisogno del lettore. La classificazione editoriale non determina da sola l'autorità semantica del contenuto, che rimane definita dal modello governato e dalle fonti che possiedono l'informazione.

### Consequences

- Progetti diversi possono condividere una classificazione leggibile senza inventare una tassonomia editoriale locale.
- La classificazione richiede giudizio editoriale e non può essere ridotta alla sola posizione del file.
- Il supporto ThreatForge a Diátaxis diventa una questione di conformance/tooling distinta dalla scelta di metodo.

### Study note

Resta una candidata Decision di metodo; la gerarchia DDTA che dovrebbe possederla non è definita in questo checkpoint.

---

## MR-0001 / ADR-0002

**Disposition:** Relocated Decision candidate

**Semantic owner:** DDTA method / cross-document governance

**Proposed parent:** Not assigned inside the ThreatForge MR hierarchy

**DDTA contract supported / related:** Shared terminology governance (status still open)

### Title

Vocabolario governato come fonte unica del linguaggio condiviso

### Context

Concetti condivisi possono ricorrere in documenti, progetti, sessioni e strumenti differenti. Se definizioni e sinonimi vengono ricostruiti localmente, il corpus può divergere semanticamente anche quando ogni singolo documento rimane formalmente valido. Occorre quindi scegliere se il significato dei termini condivisi dipenda da convenzioni locali oppure da conoscenza governata comune.

### Decision

DDTA usa, quando il profilo/metodo adottato lo richiede, una fonte governata unica per i termini condivisi e per il loro significato. Le definizioni comuni vengono referenziate o risolte dalla fonte che le possiede invece di essere copiate cumulativamente nei documenti discendenti.

### Consequences

- Persone e strumenti possono ricostruire il significato senza dipendere dalla memoria di una sessione precedente.
- Le modifiche terminologiche hanno un proprietario governato invece di richiedere copie sincronizzate.
- Resta da stabilire se il controlled vocabulary sia universale, opzionale, profile-specific o soltanto raccomandato.

### Study note

Questa formulazione evita di chiudere prematuramente l'obbligatorietà universale del vocabolario.

---

## MR-0001 / ADR-0003

**Disposition:** Rewritten ThreatForge Decision candidate; proposed re-parenting

**Semantic owner:** ThreatForge product capability

**Proposed parent:** MR-0002 - Sviluppo tracciabile dai requisiti

**DDTA contract supported / related:** Future governed realization/verification trace semantics (not yet closed)

### Title

Tracciabilità esplicita della realizzazione invece di inferenza dal repository

### Context

ThreatForge deve aiutare a collegare il lavoro tecnico alle conoscenze governate che lo giustificano. Se la realizzazione viene dedotta soltanto dalla presenza di file, da naming convention o da prosa dispersa, il tool non può distinguere in modo affidabile ciò che è pianificato, ciò che esiste e ciò che costituisce evidenza di verifica. Una strategia alternativa è mantenere una traccia esplicita e governabile che il tool possa risolvere senza interpretare implicitamente il filesystem come fonte semantica.

### Decision

ThreatForge tratta la relazione fra contesto governato, artefatti di realizzazione ed evidenze di verifica come informazione esplicita consumata e resa osservabile dal tool. ThreatForge non considera la sola esistenza di un file né una menzione in prosa come prova sufficiente di soddisfazione; usa invece le relazioni e le evidenze previste dal modello/progetto e ne rende interrogabile lo stato.

### Consequences

- La realizzazione può essere verificata senza ricostruire intenzioni da naming o posizione dei file.
- Il tool deve restare allineato alle future semantiche di Requirement, realization trace ed evidence invece di inventarle.
- La soluzione richiede dati/relazioni espliciti e quindi più disciplina rispetto a inferenze opportunistiche dal repository.

### Study note

La nuova formulazione introduce una vera alternativa di prodotto; non si limita a dire che ThreatForge 'supporta il modello'.

---

## MR-0001 / ADR-0004

**Disposition:** Retained ThreatForge Decision candidate

**Semantic owner:** ThreatForge tool architecture/support

**Proposed parent:** MR-0001 - Documentazione di progetto governata e tracciabile

**DDTA contract supported / related:** Controlled values owned by governed model/representation sources

### Title

Risoluzione contestuale dei valori controllati da fonti governate

### Context

Campi e label controllati possono avere significati diversi in contesti differenti. Se i consumer ThreatForge codificano enum globali o interpretano autonomamente stringhe come status, possono attribuire un significato diverso da quello posseduto dalla fonte governata. ThreatForge deve scegliere se mantenere interpretazioni locali nei consumer oppure risolvere i valori nel contesto che li governa.

### Decision

ThreatForge risolve label e valori controllati rispetto alla fonte e al contesto governato che ne possiedono il significato, invece di mantenere enum semantici globali nei consumer generici. Il tool può materializzare cache o proiezioni tecniche, ma tali rappresentazioni devono restare riconducibili alla fonte contestuale da cui derivano.

### Consequences

- Consumer differenti possono condividere significati senza duplicare inventari locali.
- L'evoluzione dei value set può propagarsi senza reinterpretazioni manuali in ogni adapter.
- Resolution e provenance diventano dipendenze esplicite; cache obsolete possono applicare significati non correnti.

---

## MR-0001 / ADR-0006

**Disposition:** Retained Decision candidate; parent unresolved

**Semantic owner:** ThreatForge project operations

**Proposed parent:** Open - do not force into MR-0001 or MR-0002 until MR ownership is retested

**DDTA contract supported / related:** Recoverability/continuity evidence; not a universal DDTA contract

### Title

Handoff governato per la continuità dello sviluppo ThreatForge

### Context

Lo sviluppo di ThreatForge attraversa sessioni di lavoro, programmatori e LLM differenti. Affidare la continuita alla memoria di una chat o a un riassunto manuale rende facile perdere Decision, stato del repository, verifiche e sorgenti necessarie a proseguire il lavoro in modo riproducibile.

Occorre quindi decidere se la continuita operativa dello sviluppo ThreatForge resti una pratica informale oppure venga resa ricostruibile a partire dallo stato governato del progetto.

### Decision

Il processo di sviluppo di ThreatForge usa un **handoff governato e ricostruibile** derivato dallo stato canonico del repository e dalle evidenze operative necessarie a riprendere il lavoro.

L'handoff non sostituisce le fonti governate e non rende canonico il riassunto della sessione: serve a trasportare abbastanza contesto e sorgenti per consentire al nuovo agente di verificare e ricostruire lo stato rilevante.

### Consequences

- Il cambio di sessione o agente non dipende dalla memoria dell'operatore precedente.
- La continuità viene verificata rispetto allo stato del progetto, non rispetto a una narrazione isolata.
- L'handoff deve essere mantenuto riproducibile e sufficientemente completo.
- Un handoff incompleto o obsoleto può dare falsa confidenza sulla continuità.

### Study note

La Decision è significativa; il problema aperto è la collocazione gerarchica nel set MR ThreatForge.

---

## MR-0001 / ADR-0007

**Disposition:** Retained ThreatForge Decision candidate

**Semantic owner:** ThreatForge tool architecture

**Proposed parent:** MR-0001 - Documentazione di progetto governata e tracciabile

**DDTA contract supported / related:** L1/L2 governed model and canonical representation contracts

### Title

Contratti eseguibili condivisi per i consumer ThreatForge

### Context

Validatori, editor, generatori e migrazioni ThreatForge devono interpretare lo stesso modello documentale, ma possono farlo in modi diversi. Se ogni consumer ricodifica autonomamente struttura, valori e regole, implementazioni formalmente separate possono divergere pur dichiarando di supportare lo stesso modello. ThreatForge deve quindi scegliere fra interpretazioni locali per consumer e una rappresentazione eseguibile comune derivata dalle fonti governate.

### Decision

ThreatForge deriva o materializza contratti eseguibili comuni dai modelli e dai contratti di rappresentazione governati e fa dipendere da tali contratti i consumer che necessitano di interpretazione strutturale. Schemi, validator contract, editor contract e altre viste tecniche possono differire per formato, ma non diventano inventari semantici indipendenti mantenuti a mano.

### Consequences

- Consumer differenti possono condividere struttura e diagnostica senza ricodificare il modello in più punti.
- Le proiezioni eseguibili devono restare tracciabili alla fonte governata e aggiornabili quando essa cambia.
- Una proiezione obsoleta o arricchita con semantica tool-specifica può diventare una fonte concorrente.
- La scelta aumenta la disciplina necessaria per generazione, versionamento e verifica delle proiezioni.

### Study note

Questa è una Decision L3 di ThreatForge; il principio generale delle proiezioni non viene più trattato come invariante L1.

---

## MR-0001 / ADR-0008

**Disposition:** Relocated representation Decision candidate

**Semantic owner:** DDTA canonical representation contract (L2)

**Proposed parent:** Not assigned inside the ThreatForge MR hierarchy

**DDTA contract supported / related:** Governed entity reference representation; identity/reference semantics still deferred

### Title

Rappresentazione Doc-as-Code canonica dei riferimenti governati

### Context

Quando il modello governato permette a un documento di riferirsi a un'altra entita, la rappresentazione Markdown deve poter distinguere un riferimento governato da testo ordinario e deve preservare identita stabile e leggibilita senza ridefinire la semantica dell'entita referenziata.

Occorre quindi scegliere una rappresentazione Doc-as-Code comune per serializzare tali riferimenti.

### Decision

La rappresentazione Doc-as-Code studiata per DDTA usa un payload di riferimento canonico nella forma `[<canonical-id>] <canonical-title>`, in cui l'identificativo rappresenta l'identita e il titolo e un mirror leggibile risolto dalla fonte governata.

La rappresentazione di riferimento non crea origine, provenienza, derivazione o altra relazione semantica: tali relazioni restano definite dal modello dell'entita e dal contesto che ammette il riferimento.

### Consequences

- Persone e tool possono leggere e risolvere la stessa rappresentazione senza affidarsi a forme libere.
- La serializzazione resta separata da origine, provenienza, derivazione e altre relazioni semantiche più forti.
- Parser e authoring devono conoscere le posizioni in cui il payload ha significato governato.
- La scelta non viene chiusa definitivamente prima dello studio identity/reference/mapping.

---

## MR-0001 / ADR-0009

**Disposition:** Removed as standalone Decision candidate

**Semantic owner:** ThreatForge L4 support/conformance case

**Proposed parent:** No Decision parent

**DDTA contract supported / related:** Future Security Requirement + Finding contracts

### Disposition rationale

La rewrite non conserva una scelta ThreatForge autonoma sufficiente. Una volta scelti contratti eseguibili condivisi (ADR-0007) e consumer estensibili dall'inventario governato (ADR-0010), supportare un futuro Security Requirement tramite quei contratti è principalmente una prova di coverage/conformance. La semantica Security Requirement/Finding resta nelle rispettive fasi L1/L2. Questo slot storico deve quindi diventare un caso di verifica: ThreatForge dimostra di poter supportare l'estensione senza hard-code metodologico, parentage o lifecycle non posseduti dal tool.

---

## MR-0001 / ADR-0010

**Disposition:** Retained ThreatForge Decision candidate

**Semantic owner:** ThreatForge tool architecture

**Proposed parent:** MR-0001 - Documentazione di progetto governata e tracciabile

**DDTA contract supported / related:** Governed active document-model inventory/catalog

### Title

Inventario dei modelli ThreatForge derivato dal catalogo governato

### Context

Quando entrano nuovi tipi documentali, consumer generici possono scoprire l'inventario attivo tramite liste locali, cardinalità fisse, filesystem discovery oppure una fonte governata comune. Liste e cardinalità codificate nei consumer possono divergere dall'inventario realmente attivo anche se ciascun consumer continua a funzionare.

### Decision

ThreatForge deriva l'inventario dei modelli documentali supportati e dei relativi contratti dal catalogo governato o da sue proiezioni deterministiche. I consumer generici non ridefiniscono localmente quali modelli esistono e non usano cardinalità numeriche come vincolo architetturale permanente.

### Consequences

- Nuovi modelli possono entrare attraverso un'estensione esplicita invece di una serie di eccezioni scollegate.
- I consumer possono essere verificati contro lo stesso inventario attivo.
- L'attivazione richiede coverage dichiarata dei consumer necessari.
- Registrare un modello prima che i consumer richiesti lo supportino può produrre falsa estensibilità.

---

## MR-0002 / ADR-0001

**Disposition:** Retained ThreatForge Decision candidate

**Semantic owner:** ThreatForge product architecture

**Proposed parent:** MR-0002 - Sviluppo tracciabile dai requisiti

**DDTA contract supported / related:** Multiple DDTA contracts can be consumed; no single contract defines this architecture

### Title

Separazione tra capacità ThreatForge, orchestrazione applicativa e adapter

### Context

ThreatForge deve esporre capacità di supporto alla documentazione e al lavoro governato attraverso superfici differenti. Se comportamento applicativo, interpretazione dei contratti e interazione con l'utente vengono incorporati direttamente in ogni superficie, ciascun adapter può diventare una variante autonoma del prodotto.

### Decision

ThreatForge separa le capacità riutilizzabili del tool, l'orchestrazione applicativa e gli adapter di delivery/authoring. Le capacità consumano i contratti governati necessari; l'applicazione orchestra i casi d'uso; gli adapter traducono interazione e trasporto senza possedere la logica applicativa o ridefinire i contratti consumati.

### Consequences

- CLI, editor, CI e applicazione possono riusare le stesse capacità.
- Cambiare adapter non richiede una nuova interpretazione del modello DDTA.
- I confini fra capacità, orchestrazione e delivery devono essere mantenuti esplicitamente.
- La scelta del primo adapter concreto resta separata.

### Study note

Rimosso il riferimento normativo a VS Code come prima superficie per non anticipare ADR-0005.

---

## MR-0002 / ADR-0002

**Disposition:** Retained ThreatForge Decision candidate

**Semantic owner:** ThreatForge project operations

**Proposed parent:** MR-0002 - Sviluppo tracciabile dai requisiti

**DDTA contract supported / related:** Repository-specific governance, not a universal DDTA contract

### Title

Pubblicazione governata del repository ThreatForge

### Context

Nel repository di sviluppo ThreatForge, commit e push diretti possono pubblicare uno stato in cui proiezioni versionate sono obsolete o i gate locali non sono stati eseguiti. Affidare la sequenza corretta alla memoria dello sviluppatore rende la governance del repository facoltativa.

Occorre quindi decidere se la pubblicazione di **ThreatForge stesso** resti una sequenza manuale di comandi Git oppure un'operazione governata del progetto.

### Decision

Il progetto ThreatForge usa una **operazione governata di pubblicazione Git** che esegue le precondizioni dichiarate dal repository prima di stage, commit e push e mantiene distinta una modalita di sola verifica priva di mutazioni Git.

L'operazione orchestra gate e materializzazioni posseduti dalle rispettive fonti senza duplicarne la logica.

### Consequences

- La normale pubblicazione di ThreatForge incorpora le verifiche del progetto invece di affidarsi alla disciplina individuale.
- Fonti e proiezioni versionate possono essere pubblicate in uno stato coerente.
- Il workflow del repository è più strutturato del Git diretto.
- Un orchestratore errato può introdurre side effect o staging inattesi.

---

## MR-0002 / ADR-0003

**Disposition:** Retained ThreatForge Decision candidate

**Semantic owner:** ThreatForge product capability

**Proposed parent:** MR-0002 - Sviluppo tracciabile dai requisiti

**DDTA contract supported / related:** Future realization trace/lifecycle contracts

### Title

Scaffold esplicito come avvio governato della realizzazione

### Context

Quando ThreatForge aiuta ad avviare lavoro tecnico da un contesto governato, la creazione manuale di un file può perdere il collegamento con ciò che ne giustifica l'esistenza oppure essere interpretata come realizzazione completata. ThreatForge deve scegliere se limitarsi a creare artefatti tecnici o rappresentare esplicitamente l'avvio come operazione distinta dal completamento.

### Decision

ThreatForge offre una operazione di scaffold che crea un punto di partenza tecnico collegato al contesto governato selezionato e alla tracciabilità prevista dal progetto. La presenza dello scaffold non costituisce da sola evidenza di soddisfazione o completamento; eventuali stati formali e transizioni vengono consumati dai contratti che li possiedono.

### Consequences

- L'avvio del lavoro conserva il legame con il contesto governato.
- Uno scaffold non viene confuso con completamento.
- La creazione tecnica richiede una operazione tool-aware aggiuntiva.
- Hard-code di stati o transizioni anticiperebbe semantiche non ancora chiuse.

---

## MR-0002 / ADR-0004

**Disposition:** Retained ThreatForge Decision candidate

**Semantic owner:** ThreatForge product capability

**Proposed parent:** MR-0002 - Sviluppo tracciabile dai requisiti

**DDTA contract supported / related:** Governed document/model contracts and future effective-context projections

### Title

Authoring ThreatForge guidato dai contratti governati del modello

### Context

La sola validazione a posteriori costringe autori e LLM a ricostruire manualmente identita, relazioni, struttura e valori controllati, aumentando la probabilita di creare documenti incoerenti prima che i check li rilevino.

Occorre quindi decidere se ThreatForge limiti il proprio supporto ai controlli finali oppure usi la conoscenza governata del modello anche durante l'authoring.

### Decision

ThreatForge offre **authoring guidato e deterministico** derivando suggerimenti, generatori e vincoli dai contratti governati del modello/progetto anziche mantenere copie locali delle regole nei singoli adapter.

L'authoring riduce gli errori prima della validazione, mentre i check restano un controllo indipendente finale. Il tool guida l'uso del modello ma non diventa la fonte della sua semantica.

### Consequences

- Persone e LLM ricevono contesto rilevante durante la scrittura invece di ricordare manualmente tutte le regole.
- CLI/editor possono condividere conoscenza derivata.
- Proiezioni e contratti di authoring devono restare freschi e tracciabili alla fonte governata.
- Assistenza obsoleta può guidare verso contenuto incompatibile con il modello corrente.

---

## MR-0002 / ADR-0005

**Disposition:** Retained ThreatForge Decision candidate

**Semantic owner:** ThreatForge adapter decision

**Proposed parent:** MR-0002 - Sviluppo tracciabile dai requisiti

**DDTA contract supported / related:** ThreatForge capabilities exposed without duplicating their semantics

### Title

VS Code task come adapter locale sottile di ThreatForge

### Context

Le capacita ThreatForge disponibili via CLI sono riutilizzabili ma poco ergonomiche durante il lavoro quotidiano in VS Code. Duplicare regole o valori nell'editor creerebbe una seconda implementazione, mentre una integrazione piu complessa non e necessaria per semplici operazioni di lancio.

Occorre quindi scegliere la prima superficie locale con cui esporre tali capacita nell'editor.

### Decision

ThreatForge usa un **catalogo di task VS Code** come adapter locale sottile sopra gli entrypoint governati esistenti. I task espongono operazioni e input senza possedere semantica del modello, valori canonici o logica applicativa e mantengono distinguibili operazioni read-only e operazioni con side effect.

### Consequences

- Le operazioni frequenti diventano accessibili dall'editor senza una seconda implementazione delle regole.
- La capacità sottostante resta riusabile fuori da VS Code.
- Il catalogo deve seguire l'evoluzione degli entrypoint.
- Regole locali nei task potrebbero trasformare l'adapter in una fonte concorrente.

---

## MR-0002 / ADR-0006

**Disposition:** Retained ThreatForge Decision candidate

**Semantic owner:** ThreatForge product architecture

**Proposed parent:** MR-0002 - Sviluppo tracciabile dai requisiti

**DDTA contract supported / related:** Canonical document/model contracts consumed for live assistance

### Title

Core ThreatForge condiviso per assistenza Markdown contestuale

### Context

I task possono lanciare operazioni ma non interpretano il testo non salvato e la posizione del cursore. Se VS Code e un editor web implementassero separatamente completion e diagnostica, ciascun adapter potrebbe ricostruire una propria versione delle regole documentali.

Occorre quindi decidere dove ThreatForge esegua l'analisi contestuale usata dall'assistenza live.

### Decision

ThreatForge usa un **core di assistenza Markdown indipendente dall'editor e privo di side effect** che consuma i contratti/proiezioni governate del modello e restituisce informazione di assistenza sul testo corrente. VS Code e altri editor restano adapter di presentazione e non possiedono inventari o regole semantiche autonome.

### Consequences

- Editor differenti possono produrre assistenza semanticamente coerente sullo stesso stato documentale.
- Il core può essere verificato indipendentemente dall'interfaccia.
- Il contratto fra core e adapter deve restare stabile.
- Trasformazioni adapter-specifiche possono ancora produrre differenze di range, ordine o presentazione.

---

## MR-0002 / ADR-0007

**Disposition:** Retained ThreatForge Decision candidate

**Semantic owner:** ThreatForge product architecture

**Proposed parent:** MR-0002 - Sviluppo tracciabile dai requisiti

**DDTA contract supported / related:** No single DDTA semantic contract; this is internal application architecture

### Title

Architettura applicativa ThreatForge indipendente dai delivery adapter

### Context

Le capacita di prodotto ThreatForge devono poter essere esposte da CLI e successivamente da interfacce web. Incorporare comportamento applicativo, accesso infrastrutturale e traduzione del transport nello stesso runner renderebbe ogni nuova superficie una migrazione o una duplicazione.

Occorre quindi scegliere un confine applicativo riutilizzabile interno al tool.

### Decision

ThreatForge organizza le capacita di prodotto riutilizzabili attorno a **servizi applicativi con dipendenze esplicite verso porte**, implementate da adapter infrastrutturali e composte in un confine di assembly della feature. CLI, HTTP e altre superfici traducono input/output ma non possiedono il comportamento applicativo.

Questa architettura organizza il tool ThreatForge; non definisce la struttura interna dei progetti governati ne la semantica del metamodello DDTA.

### Consequences

- CLI e web possono condividere comportamento e test applicativi.
- Infrastruttura e transport restano sostituibili dietro confini espliciti.
- Una feature richiede responsabilità e assembly più espliciti di un runner monolitico.
- Astrazioni premature o leakage di logica negli adapter possono annullare il vantaggio.

### Study note

Zod, OpenAPI, React e framework HTTP restano downstream o candidate Decision separate se acquisiscono trade-off autonomi.

---

## Corpus-level observations

1. The corrected set is intentionally asymmetric. No quota of Decisions per Macro Requirement is assumed.
2. Tool architecture Decisions are allowed to choose a concrete realization strategy even when that strategy supports an L1/L2 DDTA contract.
3. A DDTA contract being supported is not itself sufficient to justify a ThreatForge Decision; the ThreatForge document must still contain an autonomous choice.
4. Historical identifiers are retained only to preserve evidence traceability. Relocated candidates will need a new owning hierarchy before any canonical migration.
5. MR-0001/ADR-0009 demonstrates that some historical ADR content is better represented as L4 support/conformance coverage rather than as another Decision.

## Validation target

The next validation step is to apply the Revision 7 Decision tests to this corrected corpus itself. If a rewritten candidate still lacks one natural parent, one coherent choice, or non-redundant contribution, the defect remains in the authoring/corpus rather than being hidden by historical structure.
