# DDTA — Ontologia PROCESS: architettura dei processi e schede ontologiche

Questo documento costituisce la **definizione di riferimento della DDTA Process Ontology**, estensione modulare del documento normativo `DDTA_CORE.md`. I blocchi `yaml ddta-ontology` dichiarano le classi e proprietà dell'estensione; i blocchi `yaml ontology-validation` dichiarano controlli documentali. Le query SPARQL e i controlli SHACL non sono dichiarazioni aggiuntive del vocabolario e **non** confluiscono automaticamente nel Turtle generato. I casi applicativi e i relativi Turtle sono mantenuti in documenti separati dalla specifica normativa. La rappresentazione visiva degli stessi concetti è definita separatamente nella guida grafica PROCESS.

**Namespace dell'estensione:** `process: <https://w3id.org/ddta/process#>`; `ddta: <https://w3id.org/ddta/core#>` resta riservato al CORE. Si tratta di IRI adottati nella specifica, senza assumere che esista una pubblicazione web o registrazione esterna già attiva.

**Regola di autorialità:** ogni classe e proprietà è dichiarata in una sola scheda. Ogni blocco `yaml ddta-ontology` deve essere selezionato tramite l'info-string esatto; i blocchi didattici sono esclusi. I valori `status: approved` esprimono l'approvazione **nel documento di definizione**, non lo stato dei file `core.ttl` / `process.ttl` presenti nel repository.

## 1. Scopo e confini

La DDTA Process Ontology **estende** il DDTA CORE per descrivere **COME** un processo è organizzato: successioni, confronti atomici, diramazioni, concorrenza logica, sincronizzazioni, composizione e riferimenti granulari al codice e alla configurazione. Non ridefinisce il **COSA**: le capacità funzionali e i relativi contratti restano nel CORE.

Il modello rappresenta il **comportamento previsto**, non singole esecuzioni avvenute. Non assegna lo stato `RUNNING`, `WAITING` o `STOPPED` direttamente a `ddta:Process`; un'eventuale ontologia delle esecuzioni potrà distinguere istanze operative, eventi e stati osservati. Nella Process Ontology si possono descrivere percorsi che *continuano*, *attendono* oppure *terminano* senza affermare che una particolare esecuzione li abbia percorsi.

Sono rappresentabili nel modello: **sequenzialità**, **scelte XOR**, **concorrenza logica**, **sincronizzazione ALL/ANY/N-of-M**, **cicli**, **sottoprocessi richiamati** e **collegamenti granulari al codice**. Il parallelismo fisico (processori, worker, thread, code, scheduling), gli stati effettivi e il grafo delle chiamate software restano specializzazioni possibili.

### 1.1 Riutilizzo del CORE

| Classe o proprietà del CORE | Utilizzo nell'estensione |
|---|---|
| `ddta:Process` | Identità della descrizione operativa |
| `ddta:ProcessStep` | Attività o punto operativo appartenente a un processo |
| `ddta:hasStep` | Appartenenza diretta degli Step a un Process |
| `ddta:hasNextStep` | Successione pianificata e diretta tra Step; l'ordine rimane esplicito nel TTL |
| `ddta:realizesFunction` | Process → Function; non dimostra conformità |
| `ddta:Function`, `ddta:Contract`, `ddta:ContractElement` | Specifica funzionale, distinta dal processo |
| `ddta:Resource` | Risorse tecniche, implementative e di configurazione |

`ddta:ProcessStep` **non è** sottoclasse di `ddta:Process`. Anche i nodi di controllo sono Step, non processi autonomi. La ricorsione operativa può essere ottenuta associando uno Step a un processo richiamato, senza trasformare ogni Step in un processo.

### 1.2 Classi dell’estensione

| Classe | Uso |
|---|---|
| `process:AtomicCondition` | Confronto binario formalizzato, associabile a un nodo decisionale |
| `process:Operand` | Riferimento ai valori del confronto |
| `process:ControlNode` | Specializzazione di `ddta:ProcessStep`; decisioni, controlli e regioni concorrenti |
| `process:CodeReference` | Identificazione granulare di codice |

Una condizione atomica specifica un solo confronto binario. Più confronti possono essere organizzati mediante controlli successivi quando occorre documentarne anche l’ordine di valutazione; una sequenza ordinata non è in generale equivalente a un’espressione booleana priva di ordine.

### 1.3 Relazioni essenziali

| Soggetto | Relazione | Oggetto | Significato |
|---|---|---|---|
| `ddta:Process` | `ddta:hasStep` (CORE) | `ddta:ProcessStep` | Appartenenza diretta di uno Step |
| `ddta:ProcessStep` | `ddta:hasNextStep` (CORE) | `ddta:ProcessStep` | Successione prevista |
| `process:ControlNode` | `rdfs:subClassOf` | `ddta:ProcessStep` | Specializzazione del passo operativo |
| `process:ControlNode` | `process:evaluatesCondition` | `process:AtomicCondition` | Criterio formalizzato del controllo |
| `process:ControlNode` | `process:hasTrueNextStep` / `process:hasFalseNextStep` | `ddta:ProcessStep` | Successione condizionata |
| `process:AtomicCondition` | `process:hasLeftOperand` / `process:hasRightOperand` | `process:Operand` | Identificazione degli operandi |
| `ddta:Process` | `process:hasSubProcess` | `ddta:Process` | Composizione strutturale |
| `ddta:ProcessStep` | `process:invokesProcess` | `ddta:Process` | Richiamo previsto |

`hasNextStep` rappresenta la successione; non implica passaggio o disponibilità dei dati. `invokesProcess` dichiara un richiamo previsto di un processo distinto, senza implicare l'attesa del suo completamento. I contratti dei dati e i collegamenti informativi restano distinti dal flusso di controllo. Le proprietà dei rami sono approvate in questa specifica, ma la promozione nei repository richiede la verifica degli artefatti generati.

## 2. Principi di interpretazione

1. **COSA / COME:** `Function` e contratti descrivono la capacità e i requisiti; `Process` e i suoi Step descrivono l'organizzazione operativa. Nessuna corrispondenza uno-a-uno obbligatoria.
2. **Descrizione / esecuzione:** una transizione prevista non è una transizione avvenuta; una condizione descritta non è automaticamente vera; un End non documenta un'esecuzione terminata.
3. **Concorrenza logica / parallelismo fisico:** rami concorrenti possono procedere indipendentemente senza richiedere thread, macchine o tempi effettivamente sovrapposti.
4. **Assenza / falsità:** l'assenza di un fatto RDF non prova che il fatto sia falso (OWL open-world); i controlli SHACL operano sul grafo validato con criteri documentali espliciti.
5. **Estensibilità:** processi distribuiti, code, agenti, telemetria, sicurezza e analisi del codice potranno estendere le identità esistenti.
6. **Configurazione:** il parametro concreto può mutare mantenendo l'identità semantica del criterio; una variazione del parametro può però modificare il comportamento richiesto e deve essere tracciabile.
7. **Controllo non equivale a garanzia operativa:** i grafi modellano il comportamento previsto. Cancellazione effettiva, atomicità, scheduling e completamento fisico richiedono una semantica esecutiva specifica.

## 3. Convenzioni di authoring e verificabilità

- Gli IRI dell'estensione utilizzano il prefisso `process:`; `ddta:` designa le entità definite nel CORE.
- Le definizioni bilingui sono incluse nei blocchi `yaml ddta-ontology` con `module: process`, `status: approved` e `owner` per le proprietà.
- Si dichiara **una sola volta** ciascuna Object Property / Datatype Property. Le altre schede la richiamano senza ridichiarla.
- Le cardinalità documentali devono essere specificate separatamente dagli assiomi OWL. La generazione degli Shape SHACL è una fase successiva.
- I controlli obbligatori sono definiti come requisiti della prima implementazione; non si presume che il generatore attuale li implementi già.
- Gli esempi applicativi e i relativi Turtle sono conservati fuori da questo documento, senza diventare sorgenti normative del vocabolario.

---

## 4. Successioni dirette e rami dichiarati

La successione prevista tra Step è descritta da `ddta:hasNextStep` (CORE).
Le due specializzazioni `process:hasTrueNextStep` e
`process:hasFalseNextStep` qualificano le uscite binarie fra Step.
Ogni relazione dichiara una successione prevista, non un evento eseguito.

I dettagli degli Step e la topologia dei rami sono dichiarati nei dati RDF;
la guida grafica specifica esclusivamente la rappresentazione.

## 5. Scheda ontologica — `AtomicCondition`

### 5.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: process
iri: process:AtomicCondition
status: approved
label: {en: Atomic Condition, it: Condizione atomica}
definition:
  en: >-
    A condition specifying a single binary comparison between
    semantically identified operands.
  it: >-
    Una condizione che specifica un confronto binario elementare
    fra operandi identificati semanticamente.
```

### 5.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: process
owner: process:AtomicCondition
properties:
  - iri: process:hasLeftOperand
    status: approved
    domain: process:AtomicCondition
    range: process:Operand
    label: {en: has left operand, it: ha operando sinistro}
    definition:
      en: Identifies the evaluated operand of an atomic comparison.
      it: Identifica l'operando valutato in un confronto atomico.
  - iri: process:hasRightOperand
    status: approved
    domain: process:AtomicCondition
    range: process:Operand
    label: {en: has right operand, it: ha operando destro}
    definition:
      en: Identifies the reference operand of an atomic comparison.
      it: Identifica l'operando di riferimento di un confronto atomico.
```

```yaml ddta-ontology
record: datatype-properties
module: process
owner: process:AtomicCondition
properties:
  - iri: process:comparisonOperator
    status: approved
    domain: process:AtomicCondition
    range: xsd:string
    label: {en: comparison operator, it: operatore di confronto}
    definition:
      en: Controlled identifier of the comparison operation.
      it: Identificatore controllato dell'operazione di confronto.
```

Operatori di confronto definiti: `EQ`, `NE`, `LT`, `LE`, `GT`, `GE`; ulteriori operatori richiederanno una definizione semantica esplicita. Se il confronto non è ancora formalizzato, si documenta lo Step o il `ControlNode` senza attribuirgli un criterio `AtomicCondition` fittizio.

### 5.3 Interrogazione SPARQL

```sparql
PREFIX process: <https://w3id.org/ddta/process#>
SELECT ?condition ?left ?op ?right WHERE {
  ?condition a process:AtomicCondition ;
    process:hasLeftOperand ?left ;
    process:comparisonOperator ?op ;
    process:hasRightOperand ?right .
}
```

### 5.4 Vincoli

Cardinalità documentale **1..1** per ciascun operando e per `comparisonOperator` quando un individuo è classificato come `AtomicCondition`; valori dell'operatore limitati all'insieme controllato. Si tratta di **validazioni SHACL**, non di assiomi che determinano la verità del predicato.

**Controlli documentali per una condizione formalizzata:**

```yaml ontology-validation
kind: OntologyValidation
target: process:AtomicCondition
engine: SHACL
constraints:
  - id: PRC-ATOM-01
    type: property-count
    properties:
      - {path: process:hasLeftOperand, minCount: 1, maxCount: 1}
      - {path: process:hasRightOperand, minCount: 1, maxCount: 1}
      - {path: process:comparisonOperator, minCount: 1, maxCount: 1}
  - id: PRC-ATOM-02
    type: sparql
    message:
      en: Comparison operator must belong to the defined vocabulary.
      it: L'operatore di confronto deve appartenere al vocabolario definito.
    select: |-
      PREFIX process: <https://w3id.org/ddta/process#>
      SELECT $this WHERE {
        $this process:comparisonOperator ?op .
        FILTER(?op NOT IN ("EQ", "NE", "LT", "LE", "GT", "GE"))
      }
```

## 6. Scheda ontologica — `Operand`

### 6.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: process
iri: process:Operand
status: approved
label: {en: Operand, it: Operando}
definition:
  en: >-
    An identifiable operand in a process condition, used to
    refer to a functional specification element, a parameter,
    an operational value or a literal without conflating them.
  it: >-
    Un operando identificabile in una condizione di processo,
    utilizzato per riferirsi a un elemento di specifica
    funzionale, un parametro, un valore operativo o un
    letterale senza confondere tali identità.
```

`Operand` **non** è sottoclasse di `ddta:ContractElement`: quest'ultimo rappresenta un elemento richiesto o ammesso da un contratto; l'operando rappresenta il suo **ruolo nell'espressione**. Un riferimento a un elemento contrattuale non ne crea un duplicato e non prova che il processo produca effettivamente un valore conforme.

### 6.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: process
owner: process:Operand
properties:
  - iri: process:referencesContractElement
    status: approved
    domain: process:Operand
    range: ddta:ContractElement
    label: {en: references contract element, it: fa riferimento a elemento contrattuale}
    definition:
      en: Identifies a functionally specified element referenced by an operand.
      it: Identifica l'elemento funzionalmente specificato cui si riferisce l'operando.
  - iri: process:referencesResource
    status: approved
    domain: process:Operand
    range: ddta:Resource
    label: {en: references resource, it: fa riferimento a risorsa}
    definition:
      en: Identifies a resource from which an operand may be resolved.
      it: Identifica una risorsa da cui un operando può essere risolto.
```

```yaml ddta-ontology
record: datatype-properties
module: process
owner: process:Operand
properties:
  - iri: process:literalValue
    status: approved
    domain: process:Operand
    range: rdfs:Literal
    label: {en: literal value, it: valore letterale}
    definition:
      en: Constant literal used as an operand when explicitly defined.
      it: Costante letterale utilizzata come operando quando esplicitamente definita.
  - iri: process:valueLocator
    status: approved
    domain: process:Operand
    range: xsd:string
    label: {en: value locator, it: localizzatore del valore}
    definition:
      en: Logical locator of the value within a named resource or operational context.
      it: Localizzatore logico del valore in una risorsa o contesto operativo identificato.
```

**Disciplina dei riferimenti.** Un operando può riferirsi a un elemento contrattuale, a un valore di configurazione, a uno stato operativo o a una costante. Per una condizione automaticamente valutabile è necessario che il riferimento sia risolvibile e abbia semantica e tipo del valore noti. `valueLocator` non è un linguaggio di query standardizzato: la sua sintassi e interpretazione appartengono alla specializzazione o al valutatore, non sono inferite dall’ontologia. Non viene inferita una variabile di codice a partire dal nome di un `ContractElement`.

### 6.3 Interrogazione SPARQL

```sparql
PREFIX process: <https://w3id.org/ddta/process#>
SELECT ?operand ?contractElement ?resource ?locator ?literal WHERE {
  ?operand a process:Operand .
  OPTIONAL { ?operand process:referencesContractElement ?contractElement . }
  OPTIONAL { ?operand process:referencesResource ?resource . }
  OPTIONAL { ?operand process:valueLocator ?locator . }
  OPTIONAL { ?operand process:literalValue ?literal . }
}
```

### 6.4 Vincoli

Un operando per cui è prevista una valutazione automatica deve avere un meccanismo di risoluzione non ambiguo. La mutua esclusione esatta tra `literalValue` e riferimenti esterni, nonché la tipizzazione e la semantica di `valueLocator`, sono criteri che richiedono un valutatore specializzato e non costituiscono vincoli SHACL universali. Non imponiamo ora che ogni `Operand` sia esclusivamente un letterale o esclusivamente un riferimento, perché alcuni parametri possono avere valore predefinito e riferimento configurabile.

## 7. Scheda ontologica — `ControlNode`

### 7.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: process
iri: process:ControlNode
status: approved
subClassOf: ddta:ProcessStep
label: {en: Control Node, it: Nodo di controllo}
definition:
  en: >-
    A process step whose role is to govern planned control
    flow rather than to represent an application activity.
  it: >-
    Un passo di processo il cui ruolo consiste nel governare
    il flusso previsto anziché rappresentare un'attività applicativa.
```

### 7.2 Relazioni

```yaml ddta-ontology
record: datatype-properties
module: process
owner: process:ControlNode
properties:
  - iri: process:controlKind
    status: approved
    domain: process:ControlNode
    range: xsd:string
    label: {en: control kind, it: tipo di controllo}
    definition:
      en: Controlled identifier of a control node's behavior.
      it: Identificatore controllato del comportamento di un nodo di controllo.
```

#### Scelta binaria e successioni condizionate

Le seguenti proprietà rendono esplicite nel TTL le due uscite di una decisione binaria. La sottoproprietà assicura che ogni ramo sia anche una successione CORE, senza duplicare nell'authoring una tripla `ddta:hasNextStep`. La relazione al criterio è facoltativa: il nodo può essere dichiarato prima di formalizzare il confronto.

```yaml ddta-ontology
record: object-properties
module: process
owner: process:ControlNode
properties:
  - iri: process:hasTrueNextStep
    status: approved
    subPropertyOf: ddta:hasNextStep
    domain: process:ControlNode
    range: ddta:ProcessStep
    label: {en: has true next step, it: passo successivo sul vero}
    definition: {en: Successor selected by the true outcome of the control criterion., it: Successore scelto dall'esito vero del criterio del controllo.}
  - iri: process:hasFalseNextStep
    status: approved
    subPropertyOf: ddta:hasNextStep
    domain: process:ControlNode
    range: ddta:ProcessStep
    label: {en: has false next step, it: passo successivo sul falso}
    definition: {en: Successor selected by the false outcome of the control criterion., it: Successore scelto dall'esito falso del criterio del controllo.}
  - iri: process:evaluatesCondition
    status: approved
    domain: process:ControlNode
    range: process:AtomicCondition
    label: {en: evaluates condition, it: valuta condizione}
    definition: {en: Identifies the optional atomic criterion evaluated by a decision control., it: Identifica il criterio atomico facoltativamente valutato da un controllo decisionale.}
```

**Validazione documentale:** al massimo un successore TRUE e uno FALSE per un controllo binario; entrambi devono appartenere allo stesso processo che dichiara il controllo; `evaluatesCondition` 0..1. L’esito previsto da ciascuna relazione non documenta un’esecuzione reale. La scelta TRUE/FALSE è compatibile con `ddta:hasNextStep` tramite `rdfs:subPropertyOf`; richiede inferenza RDFS o proiezione esplicita quando si interroga il CORE.

#### Partecipanti e criteri di completamento del controllo composto

Un `ControlNode` con `controlKind` `CONCURRENT_SPLIT` può rappresentare un blocco composto: identifica esplicitamente gli Step partecipanti e la condizione che abilita la continuazione. I partecipanti rimangono `ddta:ProcessStep` con identità RDF distinta, input/output e risorse implementative. `hasParticipantStep` indica partecipazione, **non** successione né trasferimento di dati. Il blocco è preceduto e seguito mediante `ddta:hasNextStep`.

```yaml ddta-ontology
record: object-properties
module: process
owner: process:ControlNode
properties:
  - iri: process:hasParticipantStep
    status: approved
    domain: process:ControlNode
    range: ddta:ProcessStep
    label: {en: has participant step, it: ha step partecipante}
    definition:
      en: Identifies one direct process step coordinated by a compound control without asserting step order or data transfer.
      it: Identifica uno Step coordinato dal controllo composto, senza asserirne l'ordine o un trasferimento di dati.
```

```yaml ddta-ontology
record: datatype-properties
module: process
owner: process:ControlNode
properties:
  - iri: process:joinPolicy
    status: approved
    domain: process:ControlNode
    range: xsd:string
    label: {en: join policy, it: politica di sincronizzazione}
    definition:
      en: >-
        Completion rule ALL, ANY or N_OF_M over the declared participant steps.
      it: >-
        Regola di completamento ALL, ANY o N_OF_M sugli Step partecipanti dichiarati.
  - iri: process:requiredCount
    status: approved
    domain: process:ControlNode
    range: xsd:positiveInteger
    label: {en: required count, it: numero richiesto}
    definition: {en: Minimum number of eligible participants needed by N_OF_M., it: Numero minimo di partecipanti idonei richiesto da N_OF_M.}
  - iri: process:completionCriterion
    status: approved
    domain: process:ControlNode
    range: xsd:string
    label: {en: completion criterion, it: criterio di completamento}
    definition: {en: Eligible completion condition SUCCESS or TERMINATED., it: Criterio di completamento valido SUCCESS o TERMINATED.}
```

Le regole `ALL`, `ANY` e `N_OF_M` si applicano agli Step dichiarati con `hasParticipantStep`. Nel caso `N_OF_M`, `requiredCount` è obbligatorio, con `1 <= N <= M` e `M` uguale al numero di partecipanti RDF distinti. In `ALL` e `ANY` non si dichiara `requiredCount`. Nessuna politica di cancellazione, attesa o gestione tardiva di altri partecipanti viene inferita.

Valori controllati: `XOR_SPLIT`, `XOR_MERGE`, `CONCURRENT_SPLIT`, `WAIT`, `END_BRANCH`, `END_PROCESS`. Un controllo concorrente può includere una regola di completamento sugli Step partecipanti. La prosecuzione prevista si dichiara mediante `ddta:hasNextStep`.

**Semantica da preservare:**

- `XOR_SPLIT`: seleziona un ramo in base a un criterio documentato; per una scelta booleana il ramo può essere identificato direttamente con `hasTrueNextStep` e `hasFalseNextStep`.
- `XOR_MERGE`: ricongiunge percorsi alternativi senza introdurre una barriera che attenda rami non selezionati.
- `CONCURRENT_SPLIT`: abilita più rami logicamente indipendenti; non afferma esecuzione simultanea fisica.
- `WAIT`: rappresenta una sospensione prevista fino a una condizione di prosecuzione; non registra lo stato attuale di un'esecuzione.
- `END_BRANCH`: termina il ramo logico rappresentato; non implica la terminazione di tutti gli altri rami.
- `END_PROCESS`: prescrive la terminazione del processo descritto secondo la semantica della futura esecuzione; **non certifica** che worker in corso siano già stati fisicamente interrotti.

### 7.3 Interrogazione SPARQL

```sparql
PREFIX process: <https://w3id.org/ddta/process#>
SELECT ?node ?kind WHERE {
  ?node a process:ControlNode ; process:controlKind ?kind .
}
```

### 7.4 Vincoli

Un `ControlNode` deve avere esattamente un `controlKind` riconosciuto; il controllo composto di partecipanti conserva `controlKind` `CONCURRENT_SPLIT` e può dichiarare `joinPolicy`. La coerenza tra tipo di controllo e numero di ingressi/uscite sarà soggetta a SHACL e, per aspetti dinamici, a verifica del flusso. Non si impone che ogni `ProcessStep` sia un nodo di controllo.

**Controllo del tipo per ogni `ControlNode`:**

```yaml ontology-validation
kind: OntologyValidation
target: process:ControlNode
engine: SHACL
constraints:
  - id: PRC-CTRL-01
    type: sparql
    message:
      en: Each control node needs exactly one recognized control kind.
      it: Ogni nodo di controllo richiede esattamente un tipo riconosciuto.
    select: |-
      PREFIX process: <https://w3id.org/ddta/process#>
      SELECT $this WHERE {
        {
          FILTER NOT EXISTS { $this process:controlKind ?kind . }
        } UNION {
          $this process:controlKind ?kind .
          FILTER(?kind NOT IN
            ("XOR_SPLIT", "XOR_MERGE", "CONCURRENT_SPLIT",
             "WAIT", "END_BRANCH", "END_PROCESS"))
        } UNION {
          $this process:controlKind ?kind1, ?kind2 .
          FILTER(?kind1 != ?kind2)
        }
      }
```

Il nodo ordinario deve possedere **esattamente un** `controlKind`; l'insieme dei valori ammissibili è elencato nella scheda. Il controllo composto utilizza anche `joinPolicy`, ma continua a richiedere `controlKind` come gli altri `ControlNode`.

#### Validazioni di rami e controlli concorrenti

Le verifiche agiscono sul grafo RDF documentale (senza inferenza RDFS
che aggiungerebbe materialmente le sottoproprietà a `hasNextStep`).
La mancanza di un ramo o una condizione in una scheda ancora parziale
non è automaticamente una violazione, salvo che la semantica XOR sia già
stata dichiarata mediante una delle due uscite.

```yaml ontology-validation
kind: OntologyValidation
target: process:ControlNode
engine: SHACL
constraints:
  - id: PRC-CTRL-02
    type: property-count
    properties:
      - {path: process:hasTrueNextStep, maxCount: 1}
      - {path: process:hasFalseNextStep, maxCount: 1}
      - {path: process:evaluatesCondition, maxCount: 1}
  - id: PRC-CTRL-03
    type: sparql
    message:
      en: Declared binary branches must be paired and belong to an XOR_SPLIT control.
      it: I rami binari dichiarati devono essere entrambi presenti e appartenere a un XOR_SPLIT.
    select: |-
      PREFIX process: <https://w3id.org/ddta/process#>
      SELECT $this WHERE {
        {
          $this process:hasTrueNextStep ?target .
          FILTER NOT EXISTS { $this process:hasFalseNextStep ?other . }
        } UNION {
          $this process:hasFalseNextStep ?target .
          FILTER NOT EXISTS { $this process:hasTrueNextStep ?other . }
        } UNION {
          $this (process:hasTrueNextStep|process:hasFalseNextStep) ?target .
          FILTER NOT EXISTS { $this process:controlKind "XOR_SPLIT" . }
        }
      }
  - id: PRC-CTRL-04
    type: sparql
    message:
      en: A declared branch successor must belong directly to the same Process.
      it: Il successore di ramo dichiarato deve appartenere direttamente allo stesso Process.
    select: |-
      PREFIX process: <https://w3id.org/ddta/process#>
      PREFIX ddta: <https://w3id.org/ddta/core#>
      SELECT $this ?value WHERE {
        $this (process:hasTrueNextStep|process:hasFalseNextStep) ?value .
        FILTER NOT EXISTS { ?p ddta:hasStep $this ; ddta:hasStep ?value . }
      }
  - id: PRC-SYNC-01
    type: sparql
    message:
      en: A concurrent control must have participants, completion policy and criterion.
      it: Un controllo concorrente deve dichiarare partecipanti, regola e criterio di completamento.
    select: |-
      PREFIX process: <https://w3id.org/ddta/process#>
      SELECT $this WHERE {
        $this process:controlKind "CONCURRENT_SPLIT" .
        FILTER (
          NOT EXISTS { $this process:hasParticipantStep ?p . } ||
          NOT EXISTS { $this process:joinPolicy ?policy . } ||
          NOT EXISTS { $this process:completionCriterion ?criterion . }
        )
      }
  - id: PRC-SYNC-02
    type: sparql
    message:
      en: Synchronization policy or completion criterion has an unsupported value.
      it: La regola di sincronizzazione o il criterio di completamento non è riconosciuto.
    select: |-
      PREFIX process: <https://w3id.org/ddta/process#>
      SELECT $this WHERE {
        { $this process:joinPolicy ?policy . FILTER(?policy NOT IN ("ALL", "ANY", "N_OF_M")) }
        UNION
        { $this process:completionCriterion ?criterion . FILTER(?criterion NOT IN ("SUCCESS", "TERMINATED")) }
      }
  - id: PRC-SYNC-03
    type: sparql
    message:
      en: N_OF_M needs a valid positive count; ALL/ANY must not declare one.
      it: N_OF_M richiede un conteggio valido; ALL/ANY non devono dichiararlo.
    select: |-
      PREFIX process: <https://w3id.org/ddta/process#>
      SELECT $this WHERE {
        $this process:joinPolicy ?policy .
        {
          FILTER(?policy = "N_OF_M")
          FILTER NOT EXISTS { $this process:requiredCount ?n . FILTER(?n >= 1) }
        } UNION {
          FILTER(?policy IN ("ALL", "ANY"))
          $this process:requiredCount ?n .
        }
      }
  - id: PRC-SYNC-04
    type: property-count
    properties:
      - {path: process:joinPolicy, maxCount: 1}
      - {path: process:completionCriterion, maxCount: 1}
      - {path: process:requiredCount, maxCount: 1}
  - id: PRC-SYNC-05
    type: sparql
    message:
      en: Every concurrent participant must be a direct Step of the same Process.
      it: Ogni partecipante concorrente deve essere uno Step diretto dello stesso Process.
    select: |-
      PREFIX process: <https://w3id.org/ddta/process#>
      PREFIX ddta: <https://w3id.org/ddta/core#>
      SELECT $this ?value WHERE {
        $this process:hasParticipantStep ?value .
        FILTER(?value = $this || NOT EXISTS { ?p ddta:hasStep $this ; ddta:hasStep ?value . })
      }
  - id: PRC-SYNC-06
    type: sparql
    message:
      en: N_OF_M requiredCount cannot exceed distinct participant count.
      it: Il conteggio N_OF_M non può superare il numero di partecipanti distinti.
    select: |-
      PREFIX process: <https://w3id.org/ddta/process#>
      SELECT $this WHERE {
        $this process:joinPolicy "N_OF_M" ; process:requiredCount ?n .
        OPTIONAL { $this process:hasParticipantStep ?member . }
      }
      GROUP BY $this ?n
      HAVING (?n > COUNT(DISTINCT ?member))
```

**Controllo supplementare:** `PRC-SYNC-06` verifica il limite N/M mediante il conteggio dei partecipanti distinti. La conformità degli Shape resta da verificare con un motore SHACL indipendente prima della promozione normativa.

## 8. Scheda ontologica — `CodeReference`

### 8.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: process
iri: process:CodeReference
status: approved
label: {en: Code Reference, it: Riferimento al codice}
definition:
  en: >-
    An identifiable reference locating a source-code unit
    such as a file, module, class, function or method.
    It is not the resource that necessarily runs the code.
  it: >-
    Un riferimento identificabile che localizza un'unità
    di codice sorgente, come file, modulo, classe, funzione
    o metodo. Non coincide necessariamente con la risorsa
    che esegue tale codice.
```

`CodeReference` **non** è sottoclasse di `ddta:Resource`. Distinguere la navigazione del sorgente dall'implementazione effettiva è essenziale: codice in un repository, artefatto distribuibile, servizio attivo e configurazione possono essere entità differenti; il riferimento al sorgente non dimostra quale build o istanza sia stata eseguita.

### 8.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: process
owner: process:CodeReference
properties:
  - iri: process:hasCodeReference
    status: approved
    domain:
      unionOf: [ddta:Process, ddta:ProcessStep]
    range: process:CodeReference
    label: {en: has code reference, it: ha riferimento al codice}
    definition:
      en: Associates a process or step with relevant identifiable source code.
      it: Associa un processo o passo al codice sorgente identificabile pertinente.
  - iri: process:implementedBy
    status: approved
    domain:
      unionOf: [ddta:Process, ddta:ProcessStep]
    range: ddta:Resource
    label: {en: implemented by, it: implementato da}
    definition:
      en: Associates a process or step with a technical implementing resource.
      it: Associa un processo o passo a una risorsa tecnica implementativa.
  - iri: process:usesConfiguration
    status: approved
    domain:
      unionOf: [ddta:Process, ddta:ProcessStep]
    range: ddta:Resource
    label: {en: uses configuration, it: utilizza configurazione}
    definition:
      en: Associates a process or step with a configuration resource.
      it: Associa un processo o passo a una risorsa di configurazione.
```

```yaml ddta-ontology
record: datatype-properties
module: process
owner: process:CodeReference
properties:
  - iri: process:repositoryLocator
    status: approved
    domain: process:CodeReference
    range: xsd:string
    label: {en: repository locator, it: localizzatore del repository}
    definition:
      en: Identifies the repository containing the referenced source code.
      it: Identifica il repository del codice sorgente riferito.
  - iri: process:sourcePath
    status: approved
    domain: process:CodeReference
    range: xsd:string
    label: {en: source path, it: percorso sorgente}
    definition:
      en: Relative path of the referenced file or module.
      it: Percorso relativo del file o modulo riferito.
  - iri: process:symbolIdentifier
    status: approved
    domain: process:CodeReference
    range: xsd:string
    label: {en: symbol identifier, it: identificatore del simbolo}
    definition:
      en: Qualified symbol name for a class, function or method.
      it: Nome qualificato del simbolo di classe, funzione o metodo.
  - iri: process:codeElementKind
    status: approved
    domain: process:CodeReference
    range: xsd:string
    label: {en: code element kind, it: tipo elemento di codice}
    definition:
      en: Controlled category such as file, module, class, function or method.
      it: Categoria controllata come file, modulo, classe, funzione o metodo.
  - iri: process:sourceRevision
    status: approved
    domain: process:CodeReference
    range: xsd:string
    label: {en: source revision, it: revisione del sorgente}
    definition:
      en: Optional immutable source revision identifier such as a Git commit.
      it: Identificatore facoltativo di revisione immutabile come un commit Git.
```

`hasCodeReference` e `implementedBy` **non implicano l'una l'altra**. `usesConfiguration` riguarda la risorsa che parametrizza il comportamento. Gli identificatori dei file non richiedono la modellazione delle chiamate tra simboli. Una futura **DDTA Code Ontology** potrà approfondire file, classi, metodi, build, dipendenze e deployment senza modificare questa identità.

### 8.3 Interrogazioni SPARQL

```sparql
PREFIX process: <https://w3id.org/ddta/process#>
SELECT ?activity ?ref ?path ?symbol ?revision WHERE {
  ?activity process:hasCodeReference ?ref .
  OPTIONAL { ?ref process:sourcePath ?path . }
  OPTIONAL { ?ref process:symbolIdentifier ?symbol . }
  OPTIONAL { ?ref process:sourceRevision ?revision . }
}
```

### 8.4 Vincoli

Per un riferimento di codice navigabile, `repositoryLocator` e `sourcePath` dovrebbero essere valorizzati; `symbolIdentifier` è facoltativo per il file intero, mentre una categoria `method` o `function` richiede la localizzazione del simbolo. Una revisione specifica è raccomandata per analisi riproducibili, ma non obbligatoria universalmente. Le regole precise su identificatori, URI, linguaggio e versioni saranno definite dalla futura Code Ontology.

## 9. Estensione delle classi CORE — composizione e richiamo dei processi

### 9.1 Identificazione e definizione

La composizione strutturale è distinta dall'attivazione prevista nel flusso: un `ddta:Process` può comprendere direttamente altri Process mediante `hasSubProcess`; un `ddta:ProcessStep` può rappresentare il punto nel flusso che richiama un Process mediante `invokesProcess`. Nessuna delle due relazioni implica che il processo richiamato sia già stato eseguito. `ProcessStep` **non** è una sottoclasse di `Process`.

`hasSubProcess` non è transitiva; la struttura dichiarata di composizione non deve essere ciclica. Un processo può essere riutilizzato mediante `invokesProcess`, anche da un processo diverso dal suo proprietario strutturale: **richiamo e contenimento non si inferiscono reciprocamente**. Un ciclo di richiamo, se espressamente previsto, non è automaticamente un ciclo di composizione.

Per rendere ricostruibile la navigazione del flusso senza ricorrere a un ordinamento artificiale, `hasInitialStep` individua gli ingressi previsti del flusso di un processo. Può essercene più di uno, per processi con avvii indipendenti. L'assenza della proprietà in una documentazione parziale non deve essere interpretata come assenza di avvio.

### 9.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: process
owner: ddta:Process
properties:
  - iri: process:hasSubProcess
    status: approved
    domain: ddta:Process
    range: ddta:Process
    label: {en: has subprocess, it: ha un sottoprocesso}
    definition:
      en: >-
        Relates a process to a process belonging directly to its structural
        decomposition; it neither determines invocation nor execution order.
      it: >-
        Collega un processo a un processo appartenente direttamente alla sua
        decomposizione strutturale; non ne determina il richiamo né l'ordine.
  - iri: process:hasInitialStep
    status: approved
    domain: ddta:Process
    range: ddta:ProcessStep
    label: {en: has initial step, it: ha un passo iniziale}
    definition:
      en: >-
        Identifies an entry step of the declared flow of a process,
        without recording an actual execution.
      it: >-
        Identifica un passo di ingresso del flusso dichiarato di un processo,
        senza registrare un'esecuzione effettiva.
```

```yaml ddta-ontology
record: object-properties
module: process
owner: ddta:ProcessStep
properties:
  - iri: process:invokesProcess
    status: approved
    domain: ddta:ProcessStep
    range: ddta:Process
    label: {en: invokes process, it: richiama un processo}
    definition:
      en: >-
        Identifies the process whose planned activation is represented
        by this step; the assertion is not an execution event.
      it: >-
        Identifica il processo il cui richiamo previsto è rappresentato
        dal passo; la dichiarazione non è un evento eseguito.
  - iri: process:declaresInputContract
    status: approved
    domain: ddta:ProcessStep
    range: ddta:Contract
    label: {en: declares input contract, it: dichiara contratto di ingresso}
    definition:
      en: >-
        Declares a contract governing data consumed by this process step,
        including internal data received from other steps.
        Does not assert a transfer or redefine a function interface.
      it: >-
        Dichiara un contratto dei dati consumati dal passo, inclusi
        risultati intermedi di altri passi. Non asserisce un trasferimento
        e non ridefinisce l'interfaccia della funzione.
  - iri: process:declaresOutputContract
    status: approved
    domain: ddta:ProcessStep
    range: ddta:Contract
    label: {en: declares output contract, it: dichiara contratto di uscita}
    definition:
      en: >-
        Declares a contract governing data produced by this process step,
        including internal data consumed by conditions or other steps.
        Does not assert runtime production or redefine a function interface.
      it: >-
        Dichiara un contratto dei dati prodotti dal passo, inclusi
        risultati intermedi usati da condizioni o da altri passi.
        Non asserisce una produzione avvenuta né ridefinisce l'interfaccia della funzione.
```

**Cardinalità documentali:** `hasSubProcess` 0..*, `hasInitialStep` 0..*, `invokesProcess` 0..1 per Step nella definizione di base; `declaresInputContract` 0..* e `declaresOutputContract` 0..* per Step. L'eventuale invocazione di più processi distinti richiede Step o controlli distinti, per non lasciare ambigua la semantica. Un `hasInitialStep` deve riferirsi a uno Step appartenente direttamente allo stesso processo mediante `ddta:hasStep`.

#### Contratti dichiarati dai singoli Step

I contratti **esterni** del processo sono già quelli di `ddta:Function`, raggiungibili mediante `ddta:realizesFunction` e `ddta:hasInputContract` / `ddta:hasOutputContract`. **Non vengono ricreati** come contratti del processo o di ogni Step. Le proprietà `process:declaresInputContract` e `process:declaresOutputContract` si usano soltanto quando occorre esplicitare i dati consumati/prodotti da singoli passi. La stessa istanza `ddta:Contract` può essere referenziata dall'output di uno Step e dall'input di un altro senza duplicazione. Questa coincidenza non asserisce un trasferimento effettivo di dati: la topologia del flusso è descritta mediante `ddta:hasNextStep` e le sue specializzazioni, mentre l'eventuale provenienza dei valori richiede un'identificazione risolvibile.

Per un confronto fra output di due Step, ogni Step può dichiarare il rispettivo contratto di output, il contratto può contenere `ddta:ContractElement` e l'operando `process:Operand` può riferirsi all'elemento mediante `process:referencesContractElement`. Una `process:AtomicCondition` non è un `ddta:ProcessStep` e **non** dichiara contratti di input tramite queste proprietà: usa `hasLeftOperand`, `hasRightOperand` e `comparisonOperator`. Il valore concreto dell'output durante un'esecuzione non coincide con la descrizione contrattuale.

**Validazione documentale di base:** tutti gli oggetti di queste proprietà sono `ddta:Contract`; i loro elementi sono `ddta:ContractElement`. Quando occorre attribuire a uno Step la provenienza documentale di un operando, il percorso `Operand → ContractElement ← Contract ← declaresOutputContract ← ProcessStep` deve individuare **esattamente uno Step**; in caso contrario, la provenienza resta ambigua e non deve essere inferita per supposizione.

### 9.3 Interrogazioni SPARQL

**Ricostruire i contratti interni dichiarati dai ProcessStep:**

```sparql
PREFIX ddta: <https://w3id.org/ddta/core#>
PREFIX process: <https://w3id.org/ddta/process#>
SELECT ?step ?direction ?contract ?element WHERE {
  ?step a ddta:ProcessStep .
  { ?step process:declaresInputContract ?contract . BIND("input" AS ?direction) }
  UNION
  { ?step process:declaresOutputContract ?contract . BIND("output" AS ?direction) }
  OPTIONAL { ?contract ddta:hasContractElement ?element }
}
ORDER BY ?step ?direction ?contract ?element
```

**Individuare le funzioni realizzate dai sottoprocessi, anche a profondità arbitraria:**

```sparql
PREFIX ddta: <https://w3id.org/ddta/core#>
PREFIX process: <https://w3id.org/ddta/process#>
SELECT DISTINCT ?subprocess ?function WHERE {
  ?root process:hasSubProcess+ ?subprocess .
  ?subprocess ddta:realizesFunction ?function .
}
```

**Ricostruire la funzione realizzata da un passo e i contenuti del relativo contratto di output:**

```sparql
PREFIX ddta: <https://w3id.org/ddta/core#>
PREFIX process: <https://w3id.org/ddta/process#>
SELECT ?step ?subprocess ?function ?contract ?element WHERE {
  ?parent ddta:hasStep ?step .
  ?step process:invokesProcess ?subprocess .
  ?subprocess ddta:realizesFunction ?function .
  OPTIONAL {
    ?function ddta:hasOutputContract ?contract .
    OPTIONAL { ?contract ddta:hasContractElement ?element . }
  }
}
```

### 9.4 Vincoli di validazione

| ID | Controllo | Requisito |
|---|---|---|
| `PRC-COMP-01` | La decomposizione strutturale `hasSubProcess+` non presenta cicli | Obbligatorio |
| `PRC-COMP-02` | Ogni `hasInitialStep` appartiene allo stesso processo via `hasStep` | Obbligatorio |
| `PRC-COMP-03` | Uno Step dichiara al massimo un `invokesProcess` | Obbligatorio |

```yaml ontology-validation
kind: OntologyValidation
target: ddta:Process
engine: SHACL
constraints:
  - id: PRC-COMP-01
    type: sparql
    message:
      en: Subprocess composition contains a cycle.
      it: La decomposizione dei processi contiene un ciclo.
    select: |-
      PREFIX process: <https://w3id.org/ddta/process#>
      SELECT $this WHERE { $this process:hasSubProcess+ $this . }
  - id: PRC-COMP-02
    type: sparql
    message:
      en: An initial step must directly belong to the declaring process.
      it: Il passo iniziale deve appartenere direttamente al processo che lo dichiara.
    select: |-
      PREFIX ddta: <https://w3id.org/ddta/core#>
      PREFIX process: <https://w3id.org/ddta/process#>
      SELECT $this ?value WHERE {
        $this process:hasInitialStep ?value .
        FILTER NOT EXISTS { $this ddta:hasStep ?value . }
      }
```

```yaml ontology-validation
kind: OntologyValidation
target: ddta:ProcessStep
engine: SHACL
constraints:
  - id: PRC-COMP-03
    type: property-count
    properties:
      - {path: process:invokesProcess, maxCount: 1}
```

I controlli SPARQL devono essere tradotti e verificati come `sh:sparql`; l’esistenza del blocco YAML non implica che il generatore corrente li supporti già. L’informazione `hasInitialStep` è richiesta **per una descrizione completa degli ingressi previsti del flusso**, non per l’identificazione parziale di un processo.

## 10. Verifiche di integrazione CORE ↔ Process

| Verifica | Risultato atteso / controllo |
|---|---|
| Riutilizzo delle identità | Nessuna ridefinizione di classi/proprietà CORE |
| Classificazione | `ControlNode ⊑ ProcessStep` |
| Process ≠ ProcessStep | Nessuna inferenza `ProcessStep ⊑ Process` |
| Uscite condizionate | I rami TRUE/FALSE qualificano il nodo di controllo e sono sottoproprietà di `hasNextStep` |
| Proprietà di base | Le successioni sono dichiarate fra Step mediante `hasNextStep` oppure sue sottoproprietà |
| Specifica funzionale | `ContractElement` resta una specifica, non un valore osservato |
| Configurazione | I valori di soglia si riferiscono a una configurazione identificabile |
| Concorrenza | Non implica parallelismo fisico |
| Join N-of-M | Soglia, partecipanti e criterio di completamento documentati |
| Codice | `CodeReference` distinta da `Resource`; nessuna inferenza da codice a componente eseguito |
| Stato | Nessuno `hasState` reale su `ddta:Process` |

## 11. Requisiti di implementazione e compatibilità

### 11.1 Vocabolario approvato e artefatti

Le dichiarazioni marcate `approved` in questo documento costituiscono il **vocabolario dell’estensione PROCESS**. Il Turtle OWL è generato dai soli blocchi normativi `yaml ddta-ontology`; i controlli documentali `yaml ontology-validation` sono specifiche distinte per la validazione SHACL. Il presente documento non comporta sovrascrittura né approvazione dei Turtle già presenti sul filesystem. Le regole grafiche e la relativa generazione sono documentate nella guida PROCESS.

- Le dichiarazioni sono selezionate esclusivamente da blocchi con info-string esatto `yaml ddta-ontology`.
- `module: process` evita l'emissione accidentale di dichiarazioni nel CORE.
- I riferimenti a classi e proprietà `ddta:` sono **riusi**, non nuove dichiarazioni.
- Eventuali proprietà con unione di domini rappresentano una vera `owl:unionOf`: non devono essere trasformate in più `rdfs:domain` indipendenti.
- La validazione SHACL non viene sostituita da inferenza OWL: dominio e range non sono controlli di integrità.

### 11.2 Controlli documentali

I controlli documentali dichiarati nelle singole schede comprendono:

| Identificatore | Oggetto della verifica |
|---|---|
| `PRC-COMP-01` | Composizione `hasSubProcess` aciclica |
| `PRC-COMP-02` | Gli Step iniziali sono Step diretti del processo |
| `PRC-COMP-03` | Al massimo un sottoprocesso richiamato per Step |
| `PRC-SYNC-01..06` | Coerenza di partecipanti, regola, soglia, criterio e appartenenza nel controllo composto |
| `PRC-ATOM-01..02` | Forma delle condizioni atomiche e operatori ammessi |
| `PRC-CTRL-01` | Tipi riconosciuti dei nodi di controllo |

Per gli altri vincoli di cardinalità e operatori descritti nelle schede, valgono i requisiti testuali e le eventuali dichiarazioni strutturate presenti. Le proprietà dei rami richiedono i controlli SHACL `PRC-CTRL-02..04` dichiarati nella scheda `ControlNode`. Gli Shape devono essere testati con casi validi e negativi; gli eventuali test Python sui casi applicativi non sostituiscono una validazione SHACL completa.

### 11.3 Limiti semantici

La DDTA Process Ontology descrive **il funzionamento previsto**, non lo stato osservato di un'esecuzione. Non introduce `ProcessExecution`, `RUNNING`, `WAITING`, `STOPPED`, né una semantica generale di gestione dei worker residui; non prova il rispetto dei contratti, l'autenticità dei dati comunicati o la sicurezza di un protocollo. Le lacune documentali sono responsabilità dell’authoring DDTA, distinto dal vocabolario dei processi: un’informazione non dichiarata non giustifica la creazione di individui `ProcessStep` o di collegamenti operativi per supposizione.

Una futura DDTA Code Ontology può approfondire sorgenti, build, servizi e deployment; una Execution Ontology può descrivere le istanze reali e gli stati di avanzamento; una Security Ontology può rappresentare minacce, ipotesi di attacco e contromisure. Le nuove ontologie possono riutilizzare le identità definite qui senza reimpostarle.

---

## 12. Generazione del vocabolario OWL/Turtle

Le dichiarazioni normative `yaml ddta-ontology` di questo documento costituiscono la sorgente del vocabolario OWL/Turtle dell’estensione PROCESS. Il tool `ontology_from_md.py` valida tali dichiarazioni e genera il file `process.ttl`. Le sezioni SPARQL e i controlli `yaml ontology-validation` non producono dichiarazioni OWL; i casi applicativi sono mantenuti separati dall'ontologia.

I comandi seguenti si eseguono **dalla directory che contiene `ontology_from_md.py`**, utilizzando la CLI con l’opzione `--source` descritta nella sezione equivalente dell’ontologia CORE. Il percorso del Markdown sorgente e la directory di output sono espliciti: non è richiesta una struttura fissa del repository.

PROCESS riutilizza classi e proprietà dichiarate nel CORE. Il generatore verifica che tutti i riferimenti siano risolti **nell'insieme dei Markdown selezionati**; per questo i comandi devono includere **entrambi** `DDTA_CORE.md` e `DDTA_PROCESS.md` mediante due opzioni `--source`. I file possono trovarsi in directory differenti e i percorsi non sono fissati dal tool.

**Validazione senza scrittura:**

```powershell
python .\ontology_from_md.py --source "<percorso-DDTA_CORE.md>" --source "<percorso-DDTA_PROCESS.md>" --validate-only
```

**Generazione dei Turtle:**

```powershell
python .\ontology_from_md.py --source "<percorso-DDTA_CORE.md>" --source "<percorso-DDTA_PROCESS.md>" --generate --output-dir "<directory-di-output>"
```

**Confronto dei Turtle esistenti, senza sovrascriverli:**

```powershell
python .\ontology_from_md.py --source "<percorso-DDTA_CORE.md>" --source "<percorso-DDTA_PROCESS.md>" --check --output-dir "<directory-di-output>"
```

La generazione scrive **`core.ttl` e `process.ttl`** nella directory di output indicata; il secondo file contiene il vocabolario PROCESS e i riferimenti alle entità CORE, senza ridefinirle. Il controllo `--check` richiede **entrambi** i Turtle già generati. La riproducibilità byte per byte e il parsing RDF devono essere verificati prima della promozione in `tesiStabile`.
