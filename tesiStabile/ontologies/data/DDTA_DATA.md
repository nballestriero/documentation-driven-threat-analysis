# DDTA — Data Ontology: guida di definizione e schede ontologiche (R0, candidata)

Questo documento costituisce la **sorgente di authoring candidata** della DDTA Data Ontology, estensione modulare del documento normativo `DDTA_CORE.md`, compatibile con le identità e le strutture operative descritte in `DDTA_PROCESS.md`.

Il **vocabolario autorevole è dichiarato esclusivamente nei blocchi `yaml ddta-ontology`**. Le spiegazioni, le query SPARQL e gli esempi Turtle sono illustrativi e **non devono essere fusi nel vocabolario generato**. Un eventuale vincolo documentale futuro sarà dichiarato in un blocco separato `yaml ontology-validation`, secondo la convenzione di CORE e PROCESS.

**Namespace candidato:** `data: <https://w3id.org/ddta/data#>`. Rimangono di proprietà di CORE `ddta: <https://w3id.org/ddta/core#>` e di PROCESS `process: <https://w3id.org/ddta/process#>`.

**Stato della revisione:** questa versione R0 è sottoposta a verifica. La scelta di rendere disgiunte `data:ReadStep` e `data:WriteStep` è già stata approvata; le altre definizioni e i relativi domain/range sono candidate fino alla revisione del documento. Le schede mantengono `status: proposed` e saranno promosse singolarmente ad `approved` dopo l'accettazione. Lo stato di una scheda non afferma che la pipeline attuale abbia già generato `data.ttl`.

---

## 1. Scopo e confini

DATA estende CORE e PROCESS per distinguere:

- depositi logici destinati alla conservazione (`StableStore`) e depositi logici destinati all'uso operativo (`RunningStore`);
- passi di processo dedicati esclusivamente alla lettura (`ReadStep`) o alla scrittura (`WriteStep`);
- l'identità precisa del contenuto letto o scritto (`ddta:StoredContent`);
- copie esatte fra contenuti identificati, mantenendo distinte le identità della sorgente e della copia.

DATA **non** ridefinisce `ddta:Store`, `ddta:StoredContent`, `ddta:ProcessStep`, `ddta:stores`, i contratti né i meccanismi di comunicazione di CORE. Non introduce nuove classi di funzione remota, protocolli, formati di file o un modello delle esecuzioni avvenute.

`ddta:Store` è un deposito logico e non implica persistenza o uno specifico supporto fisico. `ddta:stores` identifica contenuti conservati direttamente oppure Store annidati; non rappresenta una lettura, una scrittura o un trasferimento. `ddta:StoredContent` identifica il contenuto e non è una sottoclasse di `ddta:Resource`.

### 1.1 Inventario minimo R0

| Elemento DATA | Natura | Specializzazione / dominio e range |
|---|---|---|
| `data:StableStore` | Classe | `rdfs:subClassOf ddta:Store` |
| `data:RunningStore` | Classe | `rdfs:subClassOf ddta:Store` |
| `data:ReadStep` | Classe | `rdfs:subClassOf ddta:ProcessStep` |
| `data:WriteStep` | Classe | `rdfs:subClassOf ddta:ProcessStep` |
| `data:readsFrom` | Object Property | `ReadStep` → `StoredContent` |
| `data:writesTo` | Object Property | `WriteStep` → `StoredContent` |
| `data:isExactCopyOf` | Object Property | `StoredContent` → `StoredContent` |

**Disgiunzione approvata:** `data:ReadStep owl:disjointWith data:WriteStep`. Non è stata approvata una disgiunzione fra `StableStore` e `RunningStore`.

### 1.2 Riutilizzo del CORE e di PROCESS

`ddta:stores` collega gli Store ai contenuti e agli Store annidati. `ddta:hasStep` associa gli Step ai processi, mentre `ddta:hasNextStep` esprime la successione prevista: non dimostra da solo una dipendenza di dati. Contratti e `CommunicationFunction`/`CommunicationChannel` restano definiti nei rispettivi moduli e non vengono ridefiniti in DATA.

---

## 2. Principi di interpretazione

1. Le schede descrivono **operazioni previste** nella documentazione del processo, non letture/scritture realmente eseguite.
2. Una relazione fra uno Step e uno `StoredContent` identifica il dato, **non** una comunicazione tra sistemi. Per trasferimenti tra sistemi si riutilizzano `CommunicationFunction` e `CommunicationChannel` di CORE.
3. Un `RunningStore` non implica una specifica tecnologia di memoria, né una particolare durata o persistenza.
4. Un dato temporaneo può essere creato direttamente durante il processo: non è obbligatorio che provenga da uno `StableStore`.
5. I domain/range OWL determinano inferenze di classe; non attestano la completezza della documentazione. Gli obblighi di completezza saranno espressi separatamente mediante controlli documentali quando approvati.
6. I vincoli descritti in questa R0 **non** determinano, da soli, l'appartenenza di uno Step e di uno Store allo stesso sistema. La verifica di località e dell'eventuale canale richiederà le informazioni architetturali effettivamente dichiarate.

---

## 3. Convenzioni di authoring e verificabilità

- Ogni classe o proprietà DATA viene definita **una sola volta** in un blocco `yaml ddta-ontology`, senza duplicarla in esempi normativi Turtle.
- `record: class` identifica le schede di classe; le proprietà sono dichiarate con `record: object-properties`, `module: data`, `owner` e campi `properties` come in CORE e PROCESS.
- Le etichette e le definizioni sono bilingui (`en`, `it`); `status: proposed` indica una definizione ancora candidata.
- La relazione `data:isExactCopyOf` è dichiarata sotto la scheda della propria proprietà perché riguarda `ddta:StoredContent`, classe appartenente a CORE; non si modifica la scheda CORE per introdurla.
- Le query SPARQL, gli esempi Turtle e le note di verifica sono **non normativi**. La cardinalità e gli altri obblighi documentali richiederanno, quando approvati, blocchi separati `yaml ontology-validation`.
- La dichiarazione `disjointWith` è collocata nella scheda di `ReadStep` e non viene duplicata nella scheda di `WriteStep`. Il supporto effettivo del generatore per questo campo e per `module: data` deve ancora essere verificato.

---

## 4. Scheda ontologica — `StableStore`

### 4.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: data
iri: data:StableStore
status: proposed
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

Per interrogare i contenuti si riutilizzano le query CORE su `ddta:stores`; DATA R0 non definisce nuove proprietà specifiche di contenimento.

### 4.4 Vincoli di completezza e coerenza documentale

Non sono introdotti nuovi `yaml ontology-validation` per `StableStore` in R0. Non si presume che la specializzazione implichi immutabilità o persistenza fisica.

### 4.5 Esempio illustrativo (escluso dal TTL generato)

Nell'esempio integrativo della sezione 9, `ex:StableConfigurationStore` è un `data:StableStore` che contiene `ex:ConfigurationFile` tramite `ddta:stores`.

---

## 5. Scheda ontologica — `RunningStore`

### 5.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: data
iri: data:RunningStore
status: proposed
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

La query per le copie esatte in uno Store operativo è presentata nella scheda `isExactCopyOf` (sezione 8.3); i contenuti non derivati da copie restano ammessi.

### 5.4 Vincoli di completezza e coerenza documentale

**Non si dichiara** `owl:disjointWith` tra `StableStore` e `RunningStore` nella R0. Nessun vincolo impone che un contenuto operativo provenga da uno `StableStore`.

### 5.5 Esempio illustrativo (escluso dal TTL generato)

Nell'esempio integrativo della sezione 9, `ex:OperationalContentStore` contiene sia `ex:ConfigurationWorkingCopy` sia `ex:CounterWorkingContent`.

---

## 6. Scheda ontologica — `ReadStep`

### 6.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: data
iri: data:ReadStep
status: proposed
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
    status: proposed
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

`ReadStep` specializza `ddta:ProcessStep`: l'appartenenza al processo continua a essere dichiarata mediante `ddta:hasStep`. Il collegamento `data:readsFrom` identifica il **contenuto preciso**, non genericamente lo Store. La collocazione del contenuto si esprime con `ddta:stores` (anche attraverso Store annidati).

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
  OPTIONAL { ?store ddta:stores+ ?content . }
}
```

### 6.4 Vincoli di completezza e coerenza documentale

**Vincolo OWL approvato:** `ReadStep` e `WriteStep` sono classi disgiunte. La dichiarazione normativa `disjointWith` è contenuta unicamente nella sezione 6.1. Non è stato ancora approvato un vincolo SHACL sulla completezza della collocazione o sulla località degli accessi.

### 6.5 Esempio illustrativo (escluso dal TTL generato)

Nell'esempio integrativo (sezione 9), `ex:ReadCounter` è un `data:ReadStep`, legge `ex:CounterWorkingContent` ed è collegato a `ex:WriteCounter` tramite `ddta:hasNextStep`.

---

## 7. Scheda ontologica — `WriteStep`

### 7.1 Identificazione e definizione

```yaml ddta-ontology
record: class
module: data
iri: data:WriteStep
status: proposed
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
    status: proposed
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
  OPTIONAL { ?store ddta:stores+ ?content . }
}
```

### 7.4 Vincoli di completezza e coerenza documentale

Un `WriteStep` può scrivere un contenuto precedentemente letto da un **distinto** `ReadStep`. La separazione è ontologica: non si assegna allo stesso individuo contemporaneamente il tipo `data:ReadStep` e `data:WriteStep`. La disgiunzione è dichiarata una sola volta nella scheda `ReadStep`.

### 7.5 Esempio illustrativo (escluso dal TTL generato)

Nell'esempio integrativo (sezione 9), `ex:WriteCounter` è un `data:WriteStep` e scrive `ex:CounterWorkingContent`.

---

## 8. Scheda ontologica — relazione `isExactCopyOf`

### 8.1 Identificazione e definizione

La proprietà `data:isExactCopyOf` collega il contenuto copiato a quello di origine, quando i byte coincidevano al momento della copia; non afferma né identità RDF né sincronizzazione successiva.

### 8.2 Relazioni

```yaml ddta-ontology
record: object-properties
module: data
owner: ddta:StoredContent
properties:
  - iri: data:isExactCopyOf
    status: proposed
    domain: ddta:StoredContent
    range: ddta:StoredContent
    label:
      en: is exact copy of
      it: è copia esatta di
    definition:
      en: >-
        Relates identifiable copied content to its source
        content when their bytes matched at the time of copying.
        It does not assert persistent synchronization or RDF identity.
      it: >-
        Collega un contenuto copiato identificabile al contenuto
        di origine, quando i byte coincidevano al momento della
        copia. Non afferma sincronizzazione successiva né
        identità RDF.
```

La relazione collega **due contenuti con identità distinte**, senza ricorrere a `owl:sameAs`. Non è dichiarata simmetrica, transitiva o funzionale. La proprietà non impone che la copia si trovi in un `RunningStore`: la collocazione è espressa autonomamente tramite `ddta:stores` di CORE. Un contenuto creato direttamente durante il processo può trovarsi in un `RunningStore` senza essere una copia di alcun contenuto conservato.

### 8.3 Interrogazioni SPARQL

**Copie esatte contenute direttamente in un `RunningStore`:**

```sparql
PREFIX ddta: <https://w3id.org/ddta/core#>
PREFIX data: <https://w3id.org/ddta/data#>

SELECT DISTINCT ?runningStore ?copy ?sourceContent
WHERE {
  ?runningStore a data:RunningStore ;
                ddta:stores ?copy .
  ?copy data:isExactCopyOf ?sourceContent .
}
```

La query recupera copie esatte dichiarate direttamente negli Store operativi. Non presume che tutti i contenuti di un `RunningStore` siano copie o che un contenuto vi sia stato effettivamente eseguito.

### 8.4 Vincoli di completezza e coerenza documentale

Non è richiesto che ogni contenuto di `RunningStore` dichiari `isExactCopyOf`. Questa proprietà non stabilisce un trasferimento tra sistemi e non sostituisce le comunicazioni CORE.

### 8.5 Esempio illustrativo (escluso dal TTL generato)

Nell'esempio integrativo (sezione 9), `ex:ConfigurationWorkingCopy data:isExactCopyOf ex:ConfigurationFile` identifica una copia distinta dalla sorgente.

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
ex:ConfigurationWorkingCopy a ddta:StoredContent ;
    data:isExactCopyOf ex:ConfigurationFile .
ex:CounterWorkingContent a ddta:StoredContent .

ex:ExampleProcess a ddta:Process ;
    ddta:hasStep ex:ReadCounter, ex:WriteCounter .
ex:ReadCounter a data:ReadStep ;
    data:readsFrom ex:CounterWorkingContent ;
    ddta:hasNextStep ex:WriteCounter .
ex:WriteCounter a data:WriteStep ;
    data:writesTo ex:CounterWorkingContent .
```

La successione `hasNextStep` **non** prova da sola la dipendenza di dati tra gli Step: questa prima versione consente di interrogare che cosa viene letto e scritto, non di ricostruire ogni trasformazione interna. Il modello non introduce un canale remoto fittizio.

---

## 10. Verifiche di integrazione CORE ↔ PROCESS ↔ DATA

Questi punti descrivono **verifiche da affrontare**, non regole SHACL già approvate o controlli già implementati.

1. **CORE / contenimento:** identificare i contenuti con `ddta:StoredContent` e la loro collocazione con `ddta:stores`, senza duplicare la proprietà in DATA.
2. **PROCESS / Step:** mantenere `ddta:hasStep` e `ddta:hasNextStep`; la successione non dimostra automaticamente il trasferimento del valore letto verso quello scritto.
3. **Comunicazione:** non introdurre Object Property DATA che duplichino le comunicazioni CORE. L'accesso a uno Store remoto deve essere rappresentato attraverso gli elementi di comunicazione effettivamente dichiarati.
4. **Località degli accessi:** le definizioni R0, da sole, non dimostrano che Step e Store appartengano al medesimo sistema; i controlli dipenderanno dalle informazioni architetturali dichiarate.
5. **Contenuti operativi:** un dato temporaneo può nascere nel `RunningStore` senza origine in uno `StableStore`. La disgiunzione fra le due tipologie di Store non è stata approvata.
6. **Validazione:** non sono ancora approvate shape `yaml ontology-validation` per località degli accessi, completezza della collocazione negli Store o tracciabilità tra contratti.

---

## 11. Generazione del vocabolario OWL/Turtle

La **sorgente autorevole** è costituita dai blocchi `yaml ddta-ontology` delle sezioni 4–8. Il generatore seleziona esclusivamente tali blocchi; esempi, query e testo discorsivo non aggiungono dichiarazioni al vocabolario.

L'inventario dichiarato contiene **4 classi e 3 Object Property**, senza modifiche alle definizioni CORE o PROCESS.

Prima di considerare completa l'integrazione con la pipeline ufficiale, occorre verificare:

1. il riconoscimento del nuovo `module: data` e del relativo namespace;
2. il supporto di `disjointWith: data:WriteStep` nella scheda `data:ReadStep` e la sua resa come `owl:disjointWith`;
3. la generazione del Turtle esclusivamente dalle schede, escludendo l'esempio integrativo.

L'assenza del supporto va segnalata: **non autorizza a scrivere il vocabolario normativo direttamente in Turtle**. La guida grafica `DDTA_DATA_VISUALIZATION.md` e le modifiche agli esempi targhe verranno affrontate solo dopo la revisione delle schede DATA.
