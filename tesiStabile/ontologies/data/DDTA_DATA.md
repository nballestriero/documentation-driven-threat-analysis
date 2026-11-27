# DDTA — Data Ontology: guida di definizione e schede ontologiche (R9, vocabolario approvato)

Questo documento costituisce la **sorgente di authoring** della DDTA Data Ontology, estensione modulare del documento normativo `DDTA_CORE.md`, indipendente dal modulo `DDTA_PROCESS.md`, con il quale può essere utilizzata congiuntamente.

Il **vocabolario autorevole è dichiarato esclusivamente nei blocchi `yaml ddta-ontology`**. Le spiegazioni, le query SPARQL e gli esempi Turtle sono illustrativi e **non devono essere fusi nel vocabolario generato**. Le regole di validazione eseguibili saranno dichiarate in un blocco separato `yaml ontology-validation`, secondo la convenzione di CORE e PROCESS.

**Namespace DATA:** `data: <https://w3id.org/ddta/data#>`. CORE usa `ddta: <https://w3id.org/ddta/core#>`. Nessuna dichiarazione ontologica DATA richiede il vocabolario PROCESS.

```yaml ddta-namespace
module: data
prefix: data
namespace: https://w3id.org/ddta/data#
ontologyIRI: https://w3id.org/ddta/data
```

**Stato della revisione:** R9 conclude la revisione del vocabolario DATA: tutte le otto dichiarazioni sono approvate. La validazione ufficiale e il consolidamento nel repository restano da eseguire.

---

## 1. Scopo e confini

DATA estende esclusivamente CORE. Il vocabolario CORE e DATA è sufficiente per esprimere anche ReadStep e WriteStep, perché ProcessStep appartiene a CORE. PROCESS è un modulo indipendente che può essere utilizzato insieme a DATA. DATA distingue:

- depositi logici destinati alla conservazione (`StableStore`) e depositi logici destinati all'uso operativo (`RunningStore`);
- passi di processo dedicati esclusivamente alla lettura (`ReadStep`) o alla scrittura (`WriteStep`);
- l'identità precisa del contenuto letto o scritto (`ddta:StoredContent`);
- operazioni di copia mediante lettura e scrittura, mantenendo distinte le identità della sorgente e della destinazione.

DATA **non** ridefinisce `ddta:Store`, `ddta:StoredContent`, `ddta:ProcessStep`, `ddta:stores`, i contratti né i meccanismi di comunicazione di CORE. Non introduce nuove classi di funzione remota, protocolli, formati di file o un modello delle esecuzioni avvenute.

`ddta:Store` è un deposito logico e non implica persistenza o uno specifico supporto fisico. `ddta:stores` identifica contenuti conservati direttamente oppure Store annidati; non rappresenta una lettura, una scrittura o un trasferimento. `ddta:StoredContent` identifica il contenuto e non è una sottoclasse di `ddta:Resource`.

### 1.1 Inventario DATA R9

| Elemento DATA | Natura | Specializzazione / dominio e range |
|---|---|---|
| `data:DataBlock` | Classe | `rdfs:subClassOf ddta:StoredContent` |
| `data:hasDataBlock` | Object Property | `ddta:StoredContent` → `data:DataBlock` |
| `data:StableStore` | Classe | `rdfs:subClassOf ddta:Store` |
| `data:RunningStore` | Classe | `rdfs:subClassOf ddta:Store` |
| `data:ReadStep` | Classe | `rdfs:subClassOf ddta:ProcessStep` |
| `data:WriteStep` | Classe | `rdfs:subClassOf ddta:ProcessStep` |
| `data:readsFrom` | Object Property | `ReadStep` → `StoredContent` |
| `data:writesTo` | Object Property | `WriteStep` → `StoredContent` |

**Disgiunzione approvata:** `data:ReadStep owl:disjointWith data:WriteStep`. Non è stata approvata una disgiunzione fra `StableStore` e `RunningStore`.

### 1.2 Riutilizzo di CORE e compatibilità con PROCESS

`ddta:stores` collega gli Store ai contenuti e agli Store annidati. `ddta:hasStep` associa gli Step ai processi, mentre `ddta:hasNextStep` esprime la successione prevista: non dimostra da solo una dipendenza di dati. Contratti e `CommunicationFunction`/`CommunicationChannel` restano definiti nei rispettivi moduli e non vengono ridefiniti in DATA.

---

## 2. Principi di interpretazione

1. Le schede descrivono **operazioni previste** nella documentazione del processo, non letture/scritture realmente eseguite.
2. Una relazione fra uno Step e uno `StoredContent` identifica il dato, **non** una comunicazione tra sistemi. Per trasferimenti tra sistemi si riutilizzano `CommunicationFunction` e `CommunicationChannel` di CORE.
3. Un `RunningStore` non implica una specifica tecnologia di memoria, né una particolare durata o persistenza.
4. Un dato temporaneo può essere creato direttamente durante il processo: non è obbligatorio che provenga da uno `StableStore`.
5. I domain/range OWL determinano inferenze di classe; non attestano la completezza della documentazione. Gli obblighi di completezza saranno espressi separatamente mediante controlli documentali quando approvati.
6. I vincoli descritti in questa revisione **non** determinano, da soli, l'appartenenza di uno Step e di uno Store allo stesso sistema. La verifica di località e dell'eventuale canale richiederà le informazioni architetturali effettivamente dichiarate.

---

### 2.1 Principio di disponibilità operativa dei contenuti (approvato)

Ogni `StoredContent` utilizzato operativamente da un processo deve essere disponibile in un `RunningStore`, direttamente tramite `ddta:stores` oppure indirettamente attraverso Store annidati e contenuti composti mediante `data:hasDataBlock`. La disponibilità deve precedere l'utilizzo previsto; il meccanismo che rende disponibile il contenuto deve essere documentato quando rientra nel perimetro di analisi. Il solo riferimento all'identità di un contenuto non descrive un accesso né attesta disponibilità, integrità o autorizzazione.

Il principio riguarda anche i contenuti software e i modelli utilizzati per realizzare un processo: il contenuto software è distinto dalla risorsa che lo esegue. Non è introdotta ora una nuova relazione per l'implementazione software, né viene modificato il range di `process:implementedBy` o `process:usesConfiguration`.

Il `RunningStore` è un deposito logico: può rappresentare memoria, filesystem di lavoro, volume operativo, cache o altro deposito, senza imporre una tecnologia. Un dato può nascere direttamente durante il funzionamento, senza provenire da uno StableStore. La lettura di un contenuto stabile per renderlo disponibile e la scrittura in uno Store stabile sono operazioni di accesso, non violazioni del principio: non si richiede che la sorgente di ogni `ReadStep` sia già in un RunningStore.

Per il caricamento da StableStore a RunningStore sono obbligatori un ReadStep e un distinto WriteStep. Una lettura non implica una scrittura. Per un caricamento da StableStore a RunningStore si distinguono lettura, eventuale trasformazione e scrittura del contenuto operativo; vanno documentate dipendenza informativa e precedenza rispetto all'uso. `ddta:hasNextStep` da sola non garantisce il trasferimento del valore. Il riferimento di un operando o di un processo al contenuto non sostituisce la descrizione dell'accesso. Occorre identificare la lettura, il caricamento o il meccanismo operativo documentato che rende quel contenuto utilizzabile. Un nuovo accesso al RunningStore va esplicitato quando rilevante per l'analisi; non è necessario introdurre una copia fisica fittizia a ogni consumo di un valore già acquisito. Un'eventuale copia esatta non implica sincronizzazione continua.

Per l'analisi delle minacce si distinguono contenuto stabile, operazione di accesso, contenuto operativo e operazione che lo utilizza. La presenza di un `ReadStep` non attesta autorizzazione; i requisiti e le condizioni di accesso sono separati dalle operazioni. La mancanza di informazioni su disponibilità o autorizzazione è una lacuna documentale, non una prova di vulnerabilità. La modellazione delle politiche di autorizzazione resta demandata a un modulo complementare; non si aggiungono proprietà DATA dipendenti da PROCESS o SECURITY. Un eventuale controllo nel flusso può utilizzare un ControlNode PROCESS con condizione e ramo esplicito, senza attribuire al controllo una semantica di autorizzazione non dichiarata.

### 2.2 Controlli documentali conseguenti

| ID | Obbligo documentale |
|---|---|
| DATA-01 | Ogni oggetto di `process:referencesStoredContent` deve essere raggiungibile da un RunningStore per contenimento diretto o indiretto (violazione bloccante). |
| DATA-02 | È identificabile come il contenuto operativo diventa disponibile, quando nel perimetro di analisi. |
| DATA-03 | La disponibilità precede l'utilizzo previsto. |
| DATA-04 | Ogni ReadStep identifica almeno un StoredContent da leggere. |
| DATA-05 | Ogni WriteStep identifica almeno un StoredContent da scrivere (1..*). |
| DATA-06 | La dipendenza informativa tra lettura e scrittura è documentata quando il valore scritto deriva dalla lettura (meccanismo da definire). |

**Query diagnostica illustrativa DATA-01 (profilo congiunto CORE + DATA + PROCESS).** Restituisce gli operandi con riferimenti espliciti a contenuti senza collocazione operativa dichiarata. Non controlla l'avvenuto caricamento, la precedenza o la politica di accesso. Il vincolo bloccante equivalente è nella shape congiunta `data-process-shapes.ttl`; la query diagnostica non introduce dipendenze OWL.

```sparql
PREFIX ddta: <https://w3id.org/ddta/core#>
PREFIX data: <https://w3id.org/ddta/data#>
PREFIX process: <https://w3id.org/ddta/process#>
SELECT DISTINCT ?operand ?content WHERE {
  ?operand process:referencesStoredContent ?content .
  FILTER NOT EXISTS {
    ?runningStore a data:RunningStore .
    ?runningStore ddta:stores+/data:hasDataBlock* ?content .
  }
}
ORDER BY ?operand ?content
```

**Query diagnostica illustrativa DATA-04 (CORE + DATA).** Restituisce i ReadStep senza un contenuto letto dichiarato.

```sparql
PREFIX data: <https://w3id.org/ddta/data#>
SELECT DISTINCT ?step WHERE {
  ?step a data:ReadStep .
  FILTER NOT EXISTS { ?step data:readsFrom ?content . }
}
ORDER BY ?step
```

I controlli non creano automaticamente Store, operazioni o precedenze. Le verifiche che combinano DATA e PROCESS appartengono a un profilo congiunto, non al vocabolario DATA. Per DATA-01, un riferimento `process:referencesStoredContent` di un operando operativo è un caso verificabile; la sua collocazione non prova DATA-02 o DATA-03.

---

## 3. Convenzioni di authoring e verificabilità

- Ogni classe o proprietà DATA viene definita **una sola volta** in un blocco `yaml ddta-ontology`, senza duplicarla in esempi normativi Turtle.
- `record: class` identifica le schede di classe; le proprietà sono dichiarate con `record: object-properties`, `module: data`, `owner` e campi `properties` come in CORE e PROCESS.
- Le etichette e le definizioni sono bilingui (`en`, `it`); `status: proposed` indica una definizione ancora candidata.
- Le query SPARQL, gli esempi Turtle e le note di verifica sono **non normativi**. La cardinalità e gli altri obblighi documentali richiederanno, quando approvati, blocchi separati `yaml ontology-validation`.
- La dichiarazione `disjointWith` è collocata nella scheda di `ReadStep` e non viene duplicata nella scheda di `WriteStep`. Il supporto effettivo del generatore per `disjointWith` deve ancora essere verificato; il namespace DATA è stato riconosciuto nella verifica R5_NAMESPACE_FIX.

---

## 4. Scheda ontologica — `StableStore`

### 4.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: data
iri: data:StableStore
status: approved
subClassOf: ddta:Store
label:
  en: Stable Store
  it: Deposito stabile
definition:
  en: >-
    A logical store intended to preserve identifiable contents beyond
    their immediate operational use. It does not imply immutability
    or a particular storage technology.
  it: >-
    Un deposito logico destinato a conservare contenuti identificabili
    oltre il loro utilizzo operativo immediato. Non implica
    immutabilità né una particolare tecnologia di memorizzazione.
```

### 4.2 Relazioni

La specializzazione descrive il **ruolo di conservazione** dello Store, non il suo dispositivo fisico. Un contenuto dello `StableStore` può essere aggiornato. Si riutilizza `ddta:stores` di CORE, senza introdurre una nuova proprietà di contenimento.

### 4.3 Interrogazioni SPARQL

Per interrogare i contenuti si riutilizzano le query CORE su `ddta:stores`; DATA riutilizza stores per gli Store e introduce hasDataBlock per la composizione interna dei contenuti.

### 4.4 Vincoli di completezza e coerenza documentale

Non sono introdotti nuovi `yaml ontology-validation` per `StableStore` in questa revisione. Non si presume che la specializzazione implichi immutabilità o persistenza fisica.

### 4.5 Esempio illustrativo (escluso dal TTL generato)

Nell'esempio integrativo della sezione 9, `ex:StableConfigurationStore` è un `data:StableStore` che contiene `ex:ConfigurationFile` tramite `ddta:stores`.

---

## 5. Scheda ontologica — `RunningStore`

### 5.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: data
iri: data:RunningStore
status: approved
subClassOf: ddta:Store
label:
  en: Running Store
  it: Deposito operativo
definition:
  en: >-
    A logical store that holds identifiable contents made available
    for planned operational activities. It does not imply a specific
    memory device, persistence policy, or observed execution.
  it: >-
    Un deposito logico che contiene dati identificabili resi
    disponibili alle attività operative previste. Non implica
    uno specifico dispositivo di memoria, una politica di
    persistenza o un'esecuzione effettivamente osservata.
```

### 5.2 Relazioni

Un `RunningStore` può contenere copie operative di dati conservati oppure contenuti prodotti durante il processo, inclusi risultati temporanei. Non si presume che ogni contenuto operativo debba avere un originale persistente. Si riutilizza `ddta:stores` di CORE.

### 5.3 Interrogazioni SPARQL

I contenuti non derivati da copie restano ammessi.

### 5.4 Vincoli di completezza e coerenza documentale

**Non si dichiara** `owl:disjointWith` tra `StableStore` e `RunningStore` in questa revisione. Nessun vincolo impone che un contenuto operativo provenga da uno `StableStore`.

### 5.5 Esempio illustrativo (escluso dal TTL generato)

Nell'esempio integrativo della sezione 9, `ex:OperationalContentStore` contiene sia `ex:ConfigurationWorkingCopy` sia `ex:CounterWorkingContent`.

---

## 6. Scheda ontologica — `ReadStep`

### 6.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: data
iri: data:ReadStep
status: approved
subClassOf: ddta:ProcessStep
disjointWith: data:WriteStep
label:
  en: Read Step
  it: Passo di lettura
definition:
  en: >-
    A planned process step responsible for reading identifiable
    stored content through local access to its store. It does not
    by itself describe communication between systems.
  it: >-
    Un passo di processo previsto responsabile della lettura di un
    contenuto memorizzato identificabile mediante accesso locale
    al relativo Store. Non descrive da solo una comunicazione
    tra sistemi.
```

### 6.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: data
owner: data:ReadStep
properties:
  - iri: data:readsFrom
    status: approved
    domain: data:ReadStep
    range: ddta:StoredContent
    label:
      en: reads from
      it: legge da
    definition:
      en: >-
        Relates a planned read step to the identifiable stored
        content it is expected to read.
      it: >-
        Collega un passo di lettura previsto al contenuto
        memorizzato identificabile che il passo deve leggere.
```

`ReadStep` specializza `ddta:ProcessStep`: l'appartenenza al processo continua a essere dichiarata mediante `ddta:hasStep`. Il collegamento `data:readsFrom` identifica il **contenuto preciso**, non genericamente lo Store. La collocazione del contenuto si esprime con `ddta:stores` (anche attraverso Store annidati) e, per un DataBlock interno, con `data:hasDataBlock`.

La dichiarazione di lettura non implica che il soggetto sia autorizzato ad accedere al contenuto. Le condizioni di esecuzione e i requisiti di autorizzazione possono essere descritti mediante moduli complementari. Non si presume un controllo di autorizzazione già implementato.

Uno Step di sola lettura **non** rappresenta una richiesta di lettura remota o il trasporto della risposta: per quelle operazioni valgono gli elementi di comunicazione CORE. Non si inferisce automaticamente la presenza di un canale.

### 6.3 Interrogazioni SPARQL

**Contenuti letti dagli Step di un processo:**

```sparql
PREFIX ddta: <https://w3id.org/ddta/core#>
PREFIX data: <https://w3id.org/ddta/data#>
PREFIX ex: <https://example.org/ddta/data-example#>

SELECT DISTINCT ?step ?content ?store
WHERE {
  ex:ExampleProcess ddta:hasStep ?step .
  ?step data:readsFrom ?content .
  OPTIONAL { ?store ddta:stores+/data:hasDataBlock* ?content . }
}
```

### 6.4 Vincoli di completezza e coerenza documentale

**Vincolo OWL approvato:** `ReadStep` e `WriteStep` sono classi disgiunte. La dichiarazione normativa `disjointWith` è contenuta unicamente nella sezione 6.1. Il requisito documentale DATA-04 richiede almeno un contenuto letto (1..*); non costituisce una restrizione OWL. La shape SHACL e le verifiche di località restano da implementare.

### 6.5 Esempio illustrativo (escluso dal TTL generato)

Nell'esempio integrativo (sezione 9), `ex:ReadCounter` è un `data:ReadStep`, legge `ex:CounterValue` ed è collegato a `ex:WriteCounter` tramite `ddta:hasNextStep`.

---

## 7. Scheda ontologica — `WriteStep`

### 7.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: data
iri: data:WriteStep
status: approved
subClassOf: ddta:ProcessStep
label:
  en: Write Step
  it: Passo di scrittura
definition:
  en: >-
    A planned process step responsible for creating, writing,
    or updating identifiable stored content through local access
    to its store. It does not by itself describe communication
    between systems.
  it: >-
    Un passo di processo previsto responsabile della creazione,
    scrittura o modifica di un contenuto memorizzato identificabile
    mediante accesso locale al relativo Store. Non descrive da
    solo una comunicazione tra sistemi.
```

### 7.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: data
owner: data:WriteStep
properties:
  - iri: data:writesTo
    status: approved
    domain: data:WriteStep
    range: ddta:StoredContent
    label:
      en: writes to
      it: scrive su
    definition:
      en: >-
        Relates a planned write step to the identifiable stored
        content it is expected to create, write, or update.
      it: >-
        Collega un passo di scrittura previsto al contenuto
        memorizzato identificabile che deve creare, scrivere
        o aggiornare.
```

`data:writesTo` identifica il contenuto che lo Step prevede di creare, scrivere o aggiornare. La relazione documenta l'operazione **prevista**: non attesta che la scrittura sia avvenuta. `ddta:stores` descrive il contenimento logico e non va usata come sinonimo di scrittura.

### 7.3 Interrogazioni SPARQL

**Contenuti scritti dagli Step di un processo:**

```sparql
PREFIX ddta: <https://w3id.org/ddta/core#>
PREFIX data: <https://w3id.org/ddta/data#>
PREFIX ex: <https://example.org/ddta/data-example#>

SELECT DISTINCT ?step ?content ?store
WHERE {
  ex:ExampleProcess ddta:hasStep ?step .
  ?step data:writesTo ?content .
  OPTIONAL { ?store ddta:stores+/data:hasDataBlock* ?content . }
}
```

### 7.4 Vincoli di completezza e coerenza documentale

Un `WriteStep` può scrivere un contenuto precedentemente letto da un **distinto** `ReadStep`. La separazione è ontologica: non si assegna allo stesso individuo contemporaneamente il tipo `data:ReadStep` e `data:WriteStep`. La disgiunzione è dichiarata una sola volta nella scheda `ReadStep`. Il requisito documentale DATA-05 richiede almeno un contenuto scritto (1..*). La scrittura può avere come destinazione un contenuto in StableStore o RunningStore; il diritto di scrittura non è implicito.

### 7.5 Esempio illustrativo (escluso dal TTL generato)

Nell'esempio integrativo (sezione 9), `ex:WriteCounter` è un `data:WriteStep` e scrive `ex:CounterValue`.

---

## 8. Copia mediante operazioni di lettura e scrittura

La copia è descritta mediante un ReadStep e un WriteStep che scrive il valore letto senza trasformazioni. Le identità RDF della sorgente e della destinazione restano distinte; la copia non implica sincronizzazione successiva. La sola successione degli Step non garantisce il trasferimento dello stesso valore. La verifica della dipendenza informativa resta da definire. Non si introduce una relazione statica di copia.

---

## 9. Esempi integrativi del modello DATA

L'esempio serve unicamente a verificare la leggibilità delle relazioni e a non confondere le triple dei casi di prova con le schede normative. **Non è un incremento approvato dell'esempio targhe.**

```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix data: <https://w3id.org/ddta/data#> .
@prefix ex: <https://example.org/ddta/data-example#> .

ex:StableConfigurationStore a data:StableStore ;
    ddta:stores ex:ConfigurationFile .
ex:OperationalContentStore a data:RunningStore ;
    ddta:stores ex:ConfigurationWorkingCopy, ex:CounterWorkingContent .

ex:ConfigurationFile a ddta:StoredContent .
ex:ConfigurationWorkingCopy a ddta:StoredContent .
ex:CounterWorkingContent a ddta:StoredContent ;
    data:hasDataBlock ex:CounterValue .
ex:CounterValue a data:DataBlock .

ex:ExampleProcess a ddta:Process ;
    ddta:hasStep ex:ReadCounter, ex:WriteCounter .
ex:ReadCounter a data:ReadStep ;
    data:readsFrom ex:CounterValue ;
    ddta:hasNextStep ex:WriteCounter .
ex:WriteCounter a data:WriteStep ;
    data:writesTo ex:CounterValue .
```

L’esempio usa soltanto CORE e DATA: il singolo `CounterValue` è un DataBlock, perciò è uno StoredContent per specializzazione. La successione `hasNextStep` **non** prova da sola la dipendenza di dati tra gli Step: questa prima versione consente di interrogare che cosa viene letto e scritto, non di ricostruire ogni trasformazione interna. Il modello non introduce un canale remoto fittizio.

---

## 10. Verifiche di integrazione CORE ↔ PROCESS ↔ DATA

Questi punti descrivono **verifiche da affrontare**, non regole SHACL già approvate o controlli già implementati.

1. **CORE / contenimento:** identificare i contenuti con `ddta:StoredContent` e la loro collocazione con `ddta:stores`, senza duplicare la proprietà in DATA.
2. **PROCESS / Step:** mantenere `ddta:hasStep` e `ddta:hasNextStep`; la successione non dimostra automaticamente il trasferimento del valore letto verso quello scritto.
3. **Comunicazione:** non introdurre Object Property DATA che duplichino le comunicazioni CORE. L'accesso a uno Store remoto deve essere rappresentato attraverso gli elementi di comunicazione effettivamente dichiarati.
4. **Località degli accessi:** le definizioni DATA, da sole, non dimostrano che Step e Store appartengano al medesimo sistema; i controlli dipenderanno dalle informazioni architetturali dichiarate.
5. **Contenuti operativi:** un dato temporaneo può nascere nel `RunningStore` senza origine in uno `StableStore`. La disgiunzione fra le due tipologie di Store non è stata approvata.
6. **Validazione:** DATA-01 è obbligatorio nel profilo congiunto; restano da definire i controlli sulla località, sulla disponibilità temporale e sulla tracciabilità tra contratti.

---

## 11. Generazione del vocabolario OWL/Turtle

La **sorgente autorevole** è costituita dai blocchi `yaml ddta-ontology` delle sezioni 4–7 e 12. Il generatore seleziona esclusivamente tali blocchi; esempi, query e testo discorsivo non aggiungono dichiarazioni al vocabolario.

L'inventario dichiarato contiene **5 classi e 3 Object Property**, senza modifiche alle definizioni CORE e senza dipendenze ontologiche da PROCESS.

Prima di considerare completa l'integrazione con la pipeline ufficiale, occorre verificare:

1. il riconoscimento del nuovo `module: data` e del relativo namespace (risolto nella verifica R5_NAMESPACE_FIX);
2. il supporto di `disjointWith: data:WriteStep` nella scheda `data:ReadStep` e la sua resa come `owl:disjointWith`;
3. la generazione del Turtle esclusivamente dalle schede, escludendo l'esempio integrativo.

L'assenza del supporto va segnalata: **non autorizza a scrivere il vocabolario normativo direttamente in Turtle**. La guida grafica `DDTA_DATA_VISUALIZATION.md` documenta le regole già approvate.

---

## 12. Scheda ontologica — `DataBlock` (approvata)

```yaml ddta-ontology
record: class
module: data
iri: data:DataBlock
status: approved
subClassOf: ddta:StoredContent
label:
  en: Data Block
  it: Blocco di dati
definition:
  en: >-
    An identifiable logical unit within stored content, consisting
    of a single value or a structured collection of values.
  it: >-
    Unità logica identificabile interna a un contenuto memorizzato,
    costituita da un singolo valore o da un insieme strutturato di valori.
```

```yaml ddta-ontology
record: object-properties
module: data
owner: ddta:StoredContent
properties:
  - iri: data:hasDataBlock
    status: approved
    domain: ddta:StoredContent
    range: data:DataBlock
    label:
      en: has data block
      it: contiene blocco di dati
    definition:
      en: Relates stored content to an identifiable logical data unit within it.
      it: Collega un contenuto memorizzato a una unità logica di dati interna.
```

DataBlock specializza StoredContent, non Resource. Può essere collocato indirettamente in uno Store tramite il contenuto padre. Il dominio di hasDataBlock ammette ora anche DataBlock come soggetto per inferenza; non si impongono cardinalità, ricorsione obbligatoria o transività. La rappresentazione grafica della composizione ricorsiva non è ancora stabilita.
I range di readsFrom e writesTo restano invariati e ammettono DataBlock per specializzazione. PROCESS può riferire StoredContent senza dipendere da DATA.
