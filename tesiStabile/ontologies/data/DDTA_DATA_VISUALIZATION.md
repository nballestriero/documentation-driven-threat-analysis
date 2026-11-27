# DDTA — Regole grafiche dell'ontologia DATA

**Fonte semantica:** `DDTA_DATA.md` (modulo `data`), con riuso di `DDTA_CORE.md`.  
**Documento:** `DDTA_DATA_VISUALIZATION.md`.  
**Ambito:** `StableStore`, `RunningStore`, `StoredContent` composto, `DataBlock`, `hasDataBlock`, `ReadStep`, `readsFrom`, `WriteStep`, `writesTo`.
**Riferimento grafico:** pipeline integrata CORE + PROCESS + DATA, revisione R2, esempio plate-gate, passo 15.

## 1. Principi di rappresentazione

La guida disciplina esclusivamente la rappresentazione grafica degli elementi DATA. Le classi e le proprietà, con il loro significato, appartengono alle ontologie DDTA. La query seleziona il sottografo RDF; le regole grafiche determinano la forma, il colore, il contenimento e le etichette degli elementi selezionati. Non si aggiungono triple RDF per ottenere una particolare disposizione grafica.

Le specializzazioni riutilizzano la forma grafica della classe CORE di riferimento, mantenendo visibile la classe RDF effettiva selezionata per l'individuo. In particolare, uno `StableStore` o un `RunningStore` non è etichettato semplicemente come `ddta:Store`.

La relazione CORE `ddta:stores` conserva la propria rappresentazione mediante contenimento. DATA aggiunge un ulteriore livello di contenimento per i blocchi di dati identificabili all'interno di uno `StoredContent`. Non sono disegnate frecce per le relazioni di contenimento.

Il riferimento di regressione è il Mermaid integrato R2 approvato visivamente. La R3 ha verificato il caricamento dichiarativo delle regole DATA (30 output identici). La revisione R4 conserva la grafica e aggiunge il riconoscimento della specializzazione DataBlock da StoredContent. In particolare, le dichiarazioni di ereditarietà grafica devono essere risolte copiando la forma CORE, e l'estensione di `StoredContent` deve essere applicata senza duplicare la scheda CORE.

---

## 2. Scheda grafica — `data:StableStore`

### 2.1 Identificazione

- **Tipo:** classe ontologica DATA.
- **IRI:** `data:StableStore`.
- **Specializzazione:** `ddta:Store`.

### 2.2 Rappresentazione

Si riutilizzano forma, palette, bordi, geometria, disposizione dei figli e icona database dello `ddta:Store` secondo la guida CORE. Non si introduce un'icona separata per gli Store stabili. In presenza di contenuti visibili, lo Store è rappresentato mediante un contenitore; senza figli visibili rimane un nodo arrotondato, secondo CORE.

L'etichetta presenta il nome dell'individuo e, sotto di esso, `data:StableStore`. Se l'individuo è esplicitamente tipizzato anche come `ddta:Store`, si mostra la specializzazione.

### 2.3 Dichiarazione YAML

```yaml ddta-visualization
record: class-style
module: data
target: data:StableStore
inheritsVisualFormFrom: ddta:Store
displayType: data:StableStore
```

La forma è risolta a partire dalla scheda CORE: i campi grafici ereditati non sono ridefiniti qui. L'etichetta della classe specializzata è mantenuta.

---

## 3. Scheda grafica — `data:RunningStore`

### 3.1 Identificazione

- **Tipo:** classe ontologica DATA.
- **IRI:** `data:RunningStore`.
- **Specializzazione:** `ddta:Store`.

### 3.2 Rappresentazione

Si applicano le medesime regole grafiche CORE di `ddta:Store`, senza introdurre una palette o un'icona diversa da `StableStore`. L'etichetta presenta il nome dell'individuo e, sotto di esso, `data:RunningStore`.

L'eventuale contenimento di `StoredContent` è determinato dalla selezione delle triple `ddta:stores`, non dal nome dell'individuo o dal suo ruolo operativo.

### 3.3 Dichiarazione YAML

```yaml ddta-visualization
record: class-style
module: data
target: data:RunningStore
inheritsVisualFormFrom: ddta:Store
displayType: data:RunningStore
```

---

## 4. Scheda grafica — `ddta:StoredContent` composto (estensione DATA)

### 4.1 Identificazione

- **Tipo:** estensione grafica di una classe CORE, non una nuova classe ontologica.
- **IRI della classe:** `ddta:StoredContent`.
- **Relazione DATA coinvolta:** `data:hasDataBlock`.

### 4.2 Rappresentazione

Un `StoredContent` senza DataBlock selezionati mantiene la rappresentazione individuale CORE: rettangolo con sfondo `#F1F5F9`, bordo grigio `#94A3B8` tratteggiato, spessore 1, raggio 5, testo `#94A3B8`, senza icona.

Quando il sottografo selezionato comprende i DataBlock collegati mediante `data:hasDataBlock`, lo stesso individuo diventa un contenitore Mermaid (`subgraph`). Il nome e la classe `ddta:StoredContent` rimangono nell'intestazione; i DataBlock sono disposti al suo interno, sotto l'intestazione, in direzione TB. La forma mantiene il bordo tratteggiato, la palette e l'assenza di icona CORE. Non si introduce un nuovo individuo per il contenitore.

L'assenza di figli nella vista non implica che il contenuto sia privo di struttura nell'ontologia o nel sistema.

### 4.3 Dichiarazione YAML

```yaml ddta-visualization
record: projection-rule
module: data
target: ddta:StoredContent
id: data-stored-content-container
render:
  classStyleExtension:
    container:
      renderer: mermaid-subgraph
      cornerRadius: 5
    layout:
      childrenDirection: TB
```

Il record estende la scheda `class-style` CORE esistente, mantenendo gli altri campi invariati. `classStyleExtension` è la forma dichiarativa utilizzata dalla pipeline: corrisponde ai due campi `container` e `layout` impostati dal renderer R2. Non costituisce una seconda definizione `class-style` per `ddta:StoredContent`. La proiezione a contenitore dipende dalla presenza di figli visibili tramite la regola di contenimento della sezione 6.

---

## 5. Scheda grafica — `data:DataBlock`

### 5.1 Identificazione

- **Tipo:** classe ontologica DATA.
- **IRI:** `data:DataBlock`.
- **Specializzazione:** `ddta:StoredContent`.

### 5.2 Rappresentazione

Un DataBlock è un rettangolo individuale con sfondo bianco, bordo grigio continuo di spessore 1 e senza icona. L'etichetta segue la convenzione globale CORE: nome in grassetto e classe `data:DataBlock` sotto il nome.

Quando è selezionata la relazione `data:hasDataBlock`, il nodo compare all'interno dello `StoredContent` corrispondente. Non è rappresentato come uno Store né come una risorsa autonoma. Il bordo continuo lo distingue dal bordo tratteggiato dello `StoredContent` che lo contiene.

### 5.3 Dichiarazione YAML

```yaml ddta-visualization
record: class-style
module: data
target: data:DataBlock
specializesVisualClass: ddta:StoredContent
node:
  shape: rectangle
style:
  fill: "#FFFFFF"
  stroke: "#94A3B8"
  color: "#64748B"
  strokeWidth: 1.0
  strokePattern: solid
```

La specializzazione seleziona DataBlock anche in presenza del tipo CORE esplicito, senza ereditarne la forma tratteggiata. I valori corrispondono alla regola R2; la generazione delle etichette rimane quella del renderer condiviso con CORE.

---

## 6. Scheda grafica — `data:hasDataBlock`

### 6.1 Identificazione

- **Tipo:** Object Property DATA.
- **IRI:** `data:hasDataBlock`.
- **Dominio:** `ddta:StoredContent`.
- **Range:** `data:DataBlock`.

### 6.2 Rappresentazione

La proprietà è proiettata mediante contenimento: il soggetto è il contenitore e l'oggetto è il nodo contenuto. Non si disegna una freccia `hasDataBlock` e non si aggiunge un nodo intermedio per la relazione. Il contenimento non rappresenta una lettura, una scrittura o un trasferimento.

La proiezione conserva l'identità RDF del soggetto e dell'oggetto. Non si deducono DataBlock dal contenuto del nome, da un file o da altre relazioni non selezionate.

### 6.3 Dichiarazione YAML

```yaml ddta-visualization
record: relation-style
module: data
target: data:hasDataBlock
representation:
  type: containment
  parent: subject
  child: object
  renderer: mermaid-subgraph
  drawEdge: false
```

---

## 7. Esempio integrativo — Store e DataBlock (plate-gate)

L'esempio seleziona le triple DATA del passo 15 necessarie a esercitare le cinque schede. Non aggiunge nuove identità né relazioni rispetto al TTL del passo 15 aggiornato. Lo Store storico è rappresentato senza contenuti selezionati. La configurazione e lo stato operativo sono `StoredContent` distinti, ciascuno con il proprio DataBlock.

**Turtle sorgente dell'esempio:**


```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix data: <https://w3id.org/ddta/data#> .
@prefix ex: <https://example.org/ddta/plate-gate#> .

ex:OCRConfigurationStableStore a data:StableStore ;
    ddta:stores ex:OCRRetrainingConfigurationFile .
ex:OCRRetrainingConfigurationFile a ddta:StoredContent .
ex:OCRDisagreementHistoryStore a ddta:Store, data:StableStore .
ex:OCRRunningStore a data:RunningStore ;
    ddta:stores ex:OCRRetrainingConfigurationRuntime, ex:OCRRuntimeState .
ex:OCRRetrainingConfigurationRuntime a ddta:StoredContent ;
    data:hasDataBlock ex:OCRRetrainingThresholdRuntime .
ex:OCRRuntimeState a ddta:StoredContent ;
    data:hasDataBlock ex:OCRDisagreementCounterRuntime .
ex:OCRRetrainingThresholdRuntime a ddta:StoredContent, data:DataBlock .
ex:OCRDisagreementCounterRuntime a ddta:StoredContent, data:DataBlock .
```

**Mermaid generato dalla pipeline dichiarativa R4 (`--data-guide`):**

```mermaid
%%{init: {"htmlLabels":true,"theme":"base","layout":"elk"}}%%
flowchart TB
    subgraph O_0afeb03793f0e9["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='27' height='27'/><div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#64748B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#64748B'>OCRConfigurationStableStore</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#64748B'>data:StableStore</span></div>"]
        direction TB
        O_80c494aff3e991["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>OCRRetrainingConfigurationFile</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>ddta:StoredContent</span></div>"]
    end
    O_85fb459ad388eb("<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#64748B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#64748B'>OCRDisagreementHistoryStore</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#64748B'>data:StableStore</span></div>")
    subgraph O_68abdc56045371["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='27' height='27'/><div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#64748B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#64748B'>OCRRunningStore</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#64748B'>data:RunningStore</span></div>"]
        direction TB
        subgraph O_b6bf347df42999["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>OCRRetrainingConfigurationRuntime</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>ddta:StoredContent</span></div>"]
            direction TB
            O_4473024364fdd7["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>OCRRetrainingThresholdRuntime</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>data:DataBlock</span></div>"]
        end
        subgraph O_453bef1914d18c["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>OCRRuntimeState</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>ddta:StoredContent</span></div>"]
            direction TB
            O_a5044a52402339["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>OCRDisagreementCounterRuntime</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>data:DataBlock</span></div>"]
        end
    end
    classDef DDTA_C_2c6e0269ee60 fill:#F1F5F9,stroke:#64748B,color:#64748B,stroke-width:1.5px
    class O_85fb459ad388eb DDTA_C_2c6e0269ee60
    classDef DDTA_C_9c53de845317 fill:#F1F5F9,stroke:#64748B,color:#64748B,stroke-width:1.5px,rx:12px,ry:12px
    class O_0afeb03793f0e9,O_68abdc56045371 DDTA_C_9c53de845317
    classDef DDTA_C_51a0b50eca1f fill:#F1F5F9,stroke:#94A3B8,color:#94A3B8,stroke-width:1.0px,stroke-dasharray:5 4,rx:5px,ry:5px
    class O_453bef1914d18c,O_80c494aff3e991,O_b6bf347df42999 DDTA_C_51a0b50eca1f
    classDef DDTA_C_d75aabb7f485 fill:#FFFFFF,stroke:#94A3B8,color:#64748B,stroke-width:1.0px
    class O_4473024364fdd7,O_a5044a52402339 DDTA_C_d75aabb7f485
```

L’esempio Mermaid è rigenerato dal sottografo Turtle precedente mediante la pipeline dichiarativa. La tipizzazione esplicita sia CORE sia DATA non modifica la classe visualizzata.


---

## 8. Scheda grafica — `data:ReadStep`

La forma è quella di `ddta:ProcessStep`, rettangolo con la convenzione CORE del passo di processo; il nome dell'individuo e la classe effettiva `data:ReadStep` sono visibili. Nella vista integrata il passo appartiene al Process tramite `ddta:hasStep` senza freccia di contenimento. L'eventuale condizione di autorizzazione è distinta dal passo e dalla lettura; non si reintroducono costrutti PROCESS deprecati.

```yaml ddta-visualization
record: class-style
module: data
target: data:ReadStep
inheritsVisualFormFrom: ddta:ProcessStep
displayType: data:ReadStep
```

## 9. Scheda grafica — `data:readsFrom`

Stessa convenzione grafica di `ddta:mustPrecede`: due segmenti grigio scuro tratteggiati, etichetta in nodo arrotondato intermedio e unica punta verso il contenuto letto (direzione RDF soggetto→oggetto). Il nodo intermedio non è un individuo RDF. La stessa convenzione è approvata per `data:writesTo` (sezione 11). L'estremità deve raggiungere l'occorrenza esistente del StoredContent o DataBlock nella sua collocazione; nessuna duplicazione del dato o dello Store, nessuna freccia di contenimento aggiuntiva. Non rappresenta il verso di trasporto dei byte, un permesso o una scrittura. La regola integrata è applicata alle sole triple esplicite; in caso di destinazione non visibile o ambigua il renderer segnala l'errore.

```yaml ddta-visualization
record: relation-style
module: data
target: data:readsFrom
representation:
  type: directed-edge
  direction: subject-to-object
  drawEdge: true
  targetOccurrence: existing-core-occurrence
  stroke: "#374151"
  strokeWidth: 1.8
  strokePattern: dashed
  dashArray: "6 4"
  arrowhead: target
label:
  text: readsFrom
  representation: rounded-inline-node
  fill: "#F3F4F6"
  stroke: "#374151"
  color: "#374151"
  cornerRadius: 12
```

## 10. Esempio di lettura — configurazione (generico)

L'esempio minimale usa individui diversi da quelli delle targhe per verificare la generalità del renderer. `ReadSettings` legge il DataBlock `LimitValue` annidato nel file persistente; la lettura del file intero è verificata nel passo 15 delle targhe. La lettura non attesta la disponibilità runtime né un diritto di accesso. I Mermaid sono generati dalla pipeline, non scritti manualmente.


### 10.1 CORE + DATA (senza PROCESS)

```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix data: <https://w3id.org/ddta/data#> .
@prefix process: <https://w3id.org/ddta/process#> .
@prefix ex: <https://example.org/ddta/data-read-example#> .

ex:ConfigurationLoader a ddta:System ;
    ddta:hasPrimaryFunction ex:LoadConfiguration ;
    ddta:hasOperationalEnvironment ex:LoaderEnvironment .
ex:LoadConfiguration a ddta:Function .
ex:LoaderEnvironment a ddta:Environment ;
    ddta:makesAvailable ex:PersistentConfigurationStore .
ex:PersistentConfigurationStore a data:StableStore ;
    ddta:stores ex:SettingsFile .
ex:SettingsFile a ddta:StoredContent ;
    data:hasDataBlock ex:LimitValue .
ex:LimitValue a data:DataBlock .
ex:LoadConfigurationProcess a ddta:Process ;
    ddta:realizesFunction ex:LoadConfiguration ;
    ddta:hasStep ex:ReadSettings .
ex:ReadSettings a ddta:ProcessStep, data:ReadStep ;
    data:readsFrom ex:LimitValue .
```

```mermaid
%%{init: {"htmlLabels":true,"theme":"base","layout":"elk"}}%%
flowchart TB
    subgraph O_428db40059bd9d["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#45845B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#45845B'>LoaderEnvironment</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#45845B'>ddta:Environment</span></div>"]
        direction TB
        subgraph G_7cba527d1798e5["Associated Systems"]
            direction TB
            subgraph O_581087f5f70b34["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#2563EB'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#2563EB'>ConfigurationLoader</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#2563EB'>ddta:System</span></div>"]
                direction LR
                subgraph G_233ab816f687a9["Primary Functions"]
                    direction LR
                    subgraph G_e73c7a6f53f652[" "]
                        direction TB
                        O_503683d3653ff2("<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#374151'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#374151'>LoadConfiguration</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#374151'>ddta:Function</span></div>")
                        subgraph G_eecbb3a6825262[" "]
                            direction TB
                            G_160d72ae92be71@{ img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSI0OCIgdmlld0JveD0iMCAwIDMyIDQ4IiBmaWxsPSJub25lIj48cGF0aCBkPSJNMTYgNDJWMTBNNiAyMCAxNiAxMGwxMCAxMCIgc3Ryb2tlPSIjN0I4Nzk0IiBzdHJva2Utd2lkdGg9IjMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPjwvc3ZnPg==", h: 42, constraint: "on" }
                            G_7823478af52c45(["realizesFunction"])
                            G_160d72ae92be71 ~~~ G_7823478af52c45
                        end
                        subgraph O_0314064ee76ee4["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#7B8794'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#7B8794'>LoadConfigurationProcess</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#7B8794'>ddta:Process</span></div>"]
                            direction LR
                            O_c03310a9031124["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#7B8794'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#7B8794'>ReadSettings</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#7B8794'>data:ReadStep</span></div>"]
                        end
                        O_503683d3653ff2 ~~~ G_eecbb3a6825262
                        G_eecbb3a6825262 ~~~ O_0314064ee76ee4
                    end
                end
            end
        end
        subgraph G_2181b40be36f66["Available Resources"]
            direction TB
            subgraph G_43e55451d9535f[" "]
                direction TB
                subgraph O_c92ec625d81fe8["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='27' height='27'/><div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#64748B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#64748B'>PersistentConfigurationStore</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#64748B'>data:StableStore</span></div>"]
                    direction TB
                    subgraph O_df442b376c32b7["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>SettingsFile</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>ddta:StoredContent</span></div>"]
                        direction TB
                        O_585e66346c49e2["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>LimitValue</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>data:DataBlock</span></div>"]
                    end
                end
                G_8cb802b5c4e0d7["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='32' height='32'/>Stores"]
                O_c92ec625d81fe8 ~~~ G_8cb802b5c4e0d7
            end
        end
    G_0e2d011f5758ba(["readsFrom"])
    O_c03310a9031124 --- G_0e2d011f5758ba --> O_585e66346c49e2
    end
    classDef DDTA_C_ec3c1934ce4a fill:#E8F1FF,stroke:#2563EB,color:#2563EB,stroke-width:1.5px
    class O_581087f5f70b34 DDTA_C_ec3c1934ce4a
    classDef DDTA_C_764b3983e628 fill:#E8F1FF,stroke:#2563EB,color:#2563EB,stroke-width:1.5px,stroke-dasharray:5 4
    class G_233ab816f687a9 DDTA_C_764b3983e628
    classDef DDTA_C_47a0c203a3c4 fill:#EAF5EC,stroke:#45845B,color:#45845B,stroke-width:1.5px
    class G_2181b40be36f66,G_7cba527d1798e5,O_428db40059bd9d DDTA_C_47a0c203a3c4
    classDef DDTA_C_f87c22e49ae1 fill:#EAF5EC,stroke:#45845B,color:#45845B,stroke-width:1.5px,stroke-dasharray:5 4
    class G_43e55451d9535f DDTA_C_f87c22e49ae1
    classDef DDTA_C_9c53de845317 fill:#F1F5F9,stroke:#64748B,color:#64748B,stroke-width:1.5px,rx:12px,ry:12px
    class O_c92ec625d81fe8 DDTA_C_9c53de845317
    classDef DDTA_C_51a0b50eca1f fill:#F1F5F9,stroke:#94A3B8,color:#94A3B8,stroke-width:1.0px,stroke-dasharray:5 4,rx:5px,ry:5px
    class O_df442b376c32b7 DDTA_C_51a0b50eca1f
    classDef DDTA_C_e3db535a2f49 fill:#F3F4F6,stroke:#374151,color:#374151,rx:12px,ry:12px
    class G_0e2d011f5758ba DDTA_C_e3db535a2f49
    classDef DDTA_C_a6bdc037a9c8 fill:#F8FAFC,stroke:#7B8794,color:#7B8794,stroke-width:2px,rx:8px,ry:8px
    class O_0314064ee76ee4 DDTA_C_a6bdc037a9c8
    classDef DDTA_C_1a97e3c85c24 fill:#FFFFFF,stroke:#374151,color:#374151,stroke-width:1.5px
    class O_503683d3653ff2 DDTA_C_1a97e3c85c24
    classDef DDTA_C_a6141e99742b fill:#FFFFFF,stroke:#7B8794,color:#7B8794,stroke-width:1.5px,stroke-dasharray:5 4
    class O_c03310a9031124 DDTA_C_a6141e99742b
    classDef DDTA_C_d75aabb7f485 fill:#FFFFFF,stroke:#94A3B8,color:#64748B,stroke-width:1.0px
    class O_585e66346c49e2 DDTA_C_d75aabb7f485
    classDef DDTA_C_8158d1a47075 fill:#FFFFFF,stroke:transparent,color:#7B8794,stroke-width:0px
    class G_7823478af52c45 DDTA_C_8158d1a47075
    classDef DDTA_C_dd44c4d967c8 fill:transparent,stroke:transparent,stroke-width:0px
    class G_160d72ae92be71,G_8cb802b5c4e0d7,G_e73c7a6f53f652,G_eecbb3a6825262 DDTA_C_dd44c4d967c8
    linkStyle 0 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 1 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 2 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 3 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 4,5 stroke:#374151,stroke-width:1.8px,stroke-dasharray:6 4
```


### 10.2 CORE + DATA + PROCESS (vista integrata)

```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix data: <https://w3id.org/ddta/data#> .
@prefix process: <https://w3id.org/ddta/process#> .
@prefix ex: <https://example.org/ddta/data-read-example#> .

ex:ConfigurationLoader a ddta:System ;
    ddta:hasPrimaryFunction ex:LoadConfiguration ;
    ddta:hasOperationalEnvironment ex:LoaderEnvironment .
ex:LoadConfiguration a ddta:Function .
ex:LoaderEnvironment a ddta:Environment ;
    ddta:makesAvailable ex:PersistentConfigurationStore .
ex:PersistentConfigurationStore a data:StableStore ;
    ddta:stores ex:SettingsFile .
ex:SettingsFile a ddta:StoredContent ;
    data:hasDataBlock ex:LimitValue .
ex:LimitValue a data:DataBlock .
ex:LoadConfigurationProcess a ddta:Process ;
    ddta:realizesFunction ex:LoadConfiguration ;
    ddta:hasStep ex:ReadSettings ;
    process:hasInitialStep ex:ReadSettings .
ex:ReadSettings a ddta:ProcessStep, data:ReadStep ;
    data:readsFrom ex:LimitValue .
```

```mermaid
%%{init: {"htmlLabels":true,"theme":"base","layout":"elk"}}%%
flowchart TB
    subgraph O_428db40059bd9d["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#45845B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#45845B'>LoaderEnvironment</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#45845B'>ddta:Environment</span></div>"]
        direction TB
        subgraph G_7cba527d1798e5["Associated Systems"]
            direction TB
            subgraph O_581087f5f70b34["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#2563EB'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#2563EB'>ConfigurationLoader</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#2563EB'>ddta:System</span></div>"]
                direction LR
                subgraph G_233ab816f687a9["Primary Functions"]
                    direction LR
                    subgraph G_e73c7a6f53f652[" "]
                        direction TB
                        O_503683d3653ff2("<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#374151'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#374151'>LoadConfiguration</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#374151'>ddta:Function</span></div>")
                        subgraph G_eecbb3a6825262[" "]
                            direction TB
                            G_160d72ae92be71@{ img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSI0OCIgdmlld0JveD0iMCAwIDMyIDQ4IiBmaWxsPSJub25lIj48cGF0aCBkPSJNMTYgNDJWMTBNNiAyMCAxNiAxMGwxMCAxMCIgc3Ryb2tlPSIjN0I4Nzk0IiBzdHJva2Utd2lkdGg9IjMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPjwvc3ZnPg==", h: 42, constraint: "on" }
                            G_7823478af52c45(["realizesFunction"])
                            G_160d72ae92be71 ~~~ G_7823478af52c45
                        end
                        subgraph O_0314064ee76ee4["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:6px 10px;background:transparent'><span style='display:block;font-size:16px;font-weight:700;color:#334155'>LoadConfigurationProcess</span><span style='display:block;font-size:11px;color:#334155'>ddta:Process</span></div>"]
                            direction TB
                            PX_4d0cc6763ee2["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:6px 10px;background:transparent'><span style='display:block;font-size:16px;font-weight:700;color:#7B8794'>ReadSettings</span><span style='display:block;font-size:11px;color:#7B8794'>data:ReadStep</span></div>"]
                            PX_f1438d311c32(["START"])
                            style PX_f1438d311c32 fill:#F3F5F7,stroke:#B6BEC8,color:#596674
                            PX_f1438d311c32 --> PX_4d0cc6763ee2
                        end
                        O_503683d3653ff2 ~~~ G_eecbb3a6825262
                        G_eecbb3a6825262 ~~~ O_0314064ee76ee4
                    end
                end
            end
        end
        subgraph G_2181b40be36f66["Available Resources"]
            direction TB
            subgraph G_43e55451d9535f[" "]
                direction TB
                subgraph O_c92ec625d81fe8["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='27' height='27'/><div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#64748B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#64748B'>PersistentConfigurationStore</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#64748B'>data:StableStore</span></div>"]
                    direction TB
                    subgraph O_df442b376c32b7["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>SettingsFile</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>ddta:StoredContent</span></div>"]
                        direction TB
                        O_585e66346c49e2["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>LimitValue</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>data:DataBlock</span></div>"]
                    end
                end
                G_8cb802b5c4e0d7["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='32' height='32'/>Stores"]
                O_c92ec625d81fe8 ~~~ G_8cb802b5c4e0d7
            end
        end
    end
    PX_393b3aded543(["readsFrom"])
    PX_4d0cc6763ee2 --- PX_393b3aded543 --> O_585e66346c49e2
    classDef DDTA_C_ec3c1934ce4a fill:#E8F1FF,stroke:#2563EB,color:#2563EB,stroke-width:1.5px
    class O_581087f5f70b34 DDTA_C_ec3c1934ce4a
    classDef DDTA_C_764b3983e628 fill:#E8F1FF,stroke:#2563EB,color:#2563EB,stroke-width:1.5px,stroke-dasharray:5 4
    class G_233ab816f687a9 DDTA_C_764b3983e628
    classDef DDTA_C_47a0c203a3c4 fill:#EAF5EC,stroke:#45845B,color:#45845B,stroke-width:1.5px
    class G_2181b40be36f66,G_7cba527d1798e5,O_428db40059bd9d DDTA_C_47a0c203a3c4
    classDef DDTA_C_f87c22e49ae1 fill:#EAF5EC,stroke:#45845B,color:#45845B,stroke-width:1.5px,stroke-dasharray:5 4
    class G_43e55451d9535f DDTA_C_f87c22e49ae1
    classDef DDTA_C_9c53de845317 fill:#F1F5F9,stroke:#64748B,color:#64748B,stroke-width:1.5px,rx:12px,ry:12px
    class O_c92ec625d81fe8 DDTA_C_9c53de845317
    classDef DDTA_C_51a0b50eca1f fill:#F1F5F9,stroke:#94A3B8,color:#94A3B8,stroke-width:1.0px,stroke-dasharray:5 4,rx:5px,ry:5px
    class O_df442b376c32b7 DDTA_C_51a0b50eca1f
    classDef DDTA_C_db520d489522 fill:#F8FAFC,stroke:#7B8794,color:#7B8794,stroke-width:2px
    classDef DDTA_C_a6bdc037a9c8 fill:#F8FAFC,stroke:#7B8794,color:#7B8794,stroke-width:2px,rx:8px,ry:8px
    class O_0314064ee76ee4 DDTA_C_a6bdc037a9c8
    classDef DDTA_C_1a97e3c85c24 fill:#FFFFFF,stroke:#374151,color:#374151,stroke-width:1.5px
    class O_503683d3653ff2 DDTA_C_1a97e3c85c24
    classDef DDTA_C_d75aabb7f485 fill:#FFFFFF,stroke:#94A3B8,color:#64748B,stroke-width:1.0px
    class O_585e66346c49e2 DDTA_C_d75aabb7f485
    classDef DDTA_C_8158d1a47075 fill:#FFFFFF,stroke:transparent,color:#7B8794,stroke-width:0px
    class G_7823478af52c45 DDTA_C_8158d1a47075
    classDef DDTA_C_dd44c4d967c8 fill:transparent,stroke:transparent,stroke-width:0px
    class G_160d72ae92be71,G_8cb802b5c4e0d7,G_e73c7a6f53f652,G_eecbb3a6825262 DDTA_C_dd44c4d967c8
    classDef PROC_process fill:#F8FAFC,stroke:#7B8794,color:#334155,stroke-width:2px,rx:8px,ry:8px
    classDef PROC_coreProcessStep fill:#FFFFFF,stroke:#7B8794,color:#7B8794,stroke-width:1.5px,stroke-dasharray:5 4
    class PX_4d0cc6763ee2 PROC_coreProcessStep
    style PX_393b3aded543 fill:#F3F4F6,stroke:#374151,color:#374151,rx:12px,ry:12px
    linkStyle 0 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 2 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 3 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 4 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 5,6 stroke:#374151,stroke-width:1.8px,stroke-dasharray:6 4
```

## 11. Schede grafiche — `data:WriteStep` e `data:writesTo`

WriteStep eredita la forma CORE di ProcessStep. writesTo usa la stessa convenzione di readsFrom e mustPrecede, verso il contenuto scritto già presente nella proiezione.

```yaml ddta-visualization
record: class-style
module: data
target: data:WriteStep
inheritsVisualFormFrom: ddta:ProcessStep
displayType: data:WriteStep
```

```yaml ddta-visualization
record: relation-style
module: data
target: data:writesTo
representation:
  type: directed-edge
  direction: subject-to-object
  drawEdge: true
  targetOccurrence: existing-core-occurrence
  stroke: "#374151"
  strokeWidth: 1.8
  strokePattern: dashed
  dashArray: "6 4"
  arrowhead: target
label:
  text: writesTo
  representation: rounded-inline-node
  fill: "#F3F4F6"
  stroke: "#374151"
  color: "#374151"
  cornerRadius: 12
```

## 12. Esempio generico di caricamento — lettura e scrittura

I due Step sono distinti; il valore scritto è in un RunningStore. Il flusso informativo effettivo non è ancora vincolato.

### 12.1 CORE + DATA

```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix data: <https://w3id.org/ddta/data#> .
@prefix process: <https://w3id.org/ddta/process#> .
@prefix ex: <https://example.org/ddta/data-read-example#> .

ex:ConfigurationLoader a ddta:System ;
    ddta:hasPrimaryFunction ex:LoadConfiguration ;
    ddta:hasOperationalEnvironment ex:LoaderEnvironment .
ex:LoadConfiguration a ddta:Function .
ex:LoaderEnvironment a ddta:Environment ;
    ddta:makesAvailable ex:PersistentConfigurationStore .
ex:PersistentConfigurationStore a data:StableStore ;
    ddta:stores ex:SettingsFile .
ex:SettingsFile a ddta:StoredContent ;
    data:hasDataBlock ex:LimitValue .
ex:LimitValue a data:DataBlock .
ex:LoadConfigurationProcess a ddta:Process ;
    ddta:realizesFunction ex:LoadConfiguration ;
    ddta:hasStep ex:ReadSettings .
ex:ReadSettings a ddta:ProcessStep, data:ReadStep ;
    data:readsFrom ex:LimitValue .

ex:LoaderEnvironment ddta:makesAvailable ex:WorkingStore .
ex:WorkingStore a data:RunningStore ; ddta:stores ex:SettingsRuntime .
ex:SettingsRuntime a ddta:StoredContent ; data:hasDataBlock ex:LimitRuntime .
ex:LimitRuntime a data:DataBlock .
ex:LoadConfigurationProcess ddta:hasStep ex:WriteSettings .
ex:ReadSettings ddta:hasNextStep ex:WriteSettings .
ex:WriteSettings a ddta:ProcessStep, data:WriteStep ; data:writesTo ex:LimitRuntime .
```

```mermaid
%%{init: {"htmlLabels":true,"theme":"base","layout":"elk"}}%%
flowchart TB
    subgraph O_428db40059bd9d["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#45845B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#45845B'>LoaderEnvironment</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#45845B'>ddta:Environment</span></div>"]
        direction TB
        subgraph G_7cba527d1798e5["Associated Systems"]
            direction TB
            subgraph O_581087f5f70b34["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#2563EB'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#2563EB'>ConfigurationLoader</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#2563EB'>ddta:System</span></div>"]
                direction LR
                subgraph G_233ab816f687a9["Primary Functions"]
                    direction LR
                    subgraph G_e73c7a6f53f652[" "]
                        direction TB
                        O_503683d3653ff2("<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#374151'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#374151'>LoadConfiguration</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#374151'>ddta:Function</span></div>")
                        subgraph G_eecbb3a6825262[" "]
                            direction TB
                            G_160d72ae92be71@{ img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSI0OCIgdmlld0JveD0iMCAwIDMyIDQ4IiBmaWxsPSJub25lIj48cGF0aCBkPSJNMTYgNDJWMTBNNiAyMCAxNiAxMGwxMCAxMCIgc3Ryb2tlPSIjN0I4Nzk0IiBzdHJva2Utd2lkdGg9IjMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPjwvc3ZnPg==", h: 42, constraint: "on" }
                            G_7823478af52c45(["realizesFunction"])
                            G_160d72ae92be71 ~~~ G_7823478af52c45
                        end
                        subgraph O_0314064ee76ee4["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#7B8794'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#7B8794'>LoadConfigurationProcess</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#7B8794'>ddta:Process</span></div>"]
                            direction LR
                            O_c03310a9031124["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#7B8794'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#7B8794'>ReadSettings</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#7B8794'>data:ReadStep</span></div>"]
                            O_bd524904342c7f["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#7B8794'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#7B8794'>WriteSettings</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#7B8794'>data:WriteStep</span></div>"]
    G_040a4d4b25b72a(["hasNextStep"])
    O_c03310a9031124 --- G_040a4d4b25b72a --> O_bd524904342c7f
                        end
                        O_503683d3653ff2 ~~~ G_eecbb3a6825262
                        G_eecbb3a6825262 ~~~ O_0314064ee76ee4
                    end
                end
            end
        end
        subgraph G_94e45325e68a72["Available Resources"]
            direction TB
            subgraph G_0527177b918bf1[" "]
                direction TB
                subgraph O_c92ec625d81fe8["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='27' height='27'/><div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#64748B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#64748B'>PersistentConfigurationStore</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#64748B'>data:StableStore</span></div>"]
                    direction TB
                    subgraph O_df442b376c32b7["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>SettingsFile</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>ddta:StoredContent</span></div>"]
                        direction TB
                        O_585e66346c49e2["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>LimitValue</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>data:DataBlock</span></div>"]
                    end
                end
                subgraph O_4be059eb594a51["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='27' height='27'/><div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#64748B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#64748B'>WorkingStore</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#64748B'>data:RunningStore</span></div>"]
                    direction TB
                    subgraph O_902c118f0ac149["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>SettingsRuntime</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>ddta:StoredContent</span></div>"]
                        direction TB
                        O_04e831307b68ed["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>LimitRuntime</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>data:DataBlock</span></div>"]
                    end
                end
                G_b79e146897bde4["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='32' height='32'/>Stores"]
                O_4be059eb594a51 ~~~ G_b79e146897bde4
            end
        end
    G_0e2d011f5758ba(["readsFrom"])
    O_c03310a9031124 --- G_0e2d011f5758ba --> O_585e66346c49e2
    G_42a24754eb168e(["writesTo"])
    O_bd524904342c7f --- G_42a24754eb168e --> O_04e831307b68ed
    end
    classDef DDTA_C_ec3c1934ce4a fill:#E8F1FF,stroke:#2563EB,color:#2563EB,stroke-width:1.5px
    class O_581087f5f70b34 DDTA_C_ec3c1934ce4a
    classDef DDTA_C_764b3983e628 fill:#E8F1FF,stroke:#2563EB,color:#2563EB,stroke-width:1.5px,stroke-dasharray:5 4
    class G_233ab816f687a9 DDTA_C_764b3983e628
    classDef DDTA_C_47a0c203a3c4 fill:#EAF5EC,stroke:#45845B,color:#45845B,stroke-width:1.5px
    class G_7cba527d1798e5,G_94e45325e68a72,O_428db40059bd9d DDTA_C_47a0c203a3c4
    classDef DDTA_C_f87c22e49ae1 fill:#EAF5EC,stroke:#45845B,color:#45845B,stroke-width:1.5px,stroke-dasharray:5 4
    class G_0527177b918bf1 DDTA_C_f87c22e49ae1
    classDef DDTA_C_9c53de845317 fill:#F1F5F9,stroke:#64748B,color:#64748B,stroke-width:1.5px,rx:12px,ry:12px
    class O_4be059eb594a51,O_c92ec625d81fe8 DDTA_C_9c53de845317
    classDef DDTA_C_51a0b50eca1f fill:#F1F5F9,stroke:#94A3B8,color:#94A3B8,stroke-width:1.0px,stroke-dasharray:5 4,rx:5px,ry:5px
    class O_902c118f0ac149,O_df442b376c32b7 DDTA_C_51a0b50eca1f
    classDef DDTA_C_e3db535a2f49 fill:#F3F4F6,stroke:#374151,color:#374151,rx:12px,ry:12px
    class G_0e2d011f5758ba,G_42a24754eb168e DDTA_C_e3db535a2f49
    classDef DDTA_C_a6bdc037a9c8 fill:#F8FAFC,stroke:#7B8794,color:#7B8794,stroke-width:2px,rx:8px,ry:8px
    class O_0314064ee76ee4 DDTA_C_a6bdc037a9c8
    classDef DDTA_C_1a97e3c85c24 fill:#FFFFFF,stroke:#374151,color:#374151,stroke-width:1.5px
    class O_503683d3653ff2 DDTA_C_1a97e3c85c24
    classDef DDTA_C_c5903718b18b fill:#FFFFFF,stroke:#7B8794,color:#7B8794,rx:12px,ry:12px
    class G_040a4d4b25b72a DDTA_C_c5903718b18b
    classDef DDTA_C_a6141e99742b fill:#FFFFFF,stroke:#7B8794,color:#7B8794,stroke-width:1.5px,stroke-dasharray:5 4
    class O_bd524904342c7f,O_c03310a9031124 DDTA_C_a6141e99742b
    classDef DDTA_C_d75aabb7f485 fill:#FFFFFF,stroke:#94A3B8,color:#64748B,stroke-width:1.0px
    class O_04e831307b68ed,O_585e66346c49e2 DDTA_C_d75aabb7f485
    classDef DDTA_C_8158d1a47075 fill:#FFFFFF,stroke:transparent,color:#7B8794,stroke-width:0px
    class G_7823478af52c45 DDTA_C_8158d1a47075
    classDef DDTA_C_dd44c4d967c8 fill:transparent,stroke:transparent,stroke-width:0px
    class G_160d72ae92be71,G_b79e146897bde4,G_e73c7a6f53f652,G_eecbb3a6825262 DDTA_C_dd44c4d967c8
    linkStyle 0 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 1,2 stroke:#7B8794,stroke-width:1.5px
    linkStyle 3 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 4 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 5 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 6,7 stroke:#374151,stroke-width:1.8px,stroke-dasharray:6 4
    linkStyle 8,9 stroke:#374151,stroke-width:1.8px,stroke-dasharray:6 4
```

### 12.2 CORE + DATA + PROCESS

```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix data: <https://w3id.org/ddta/data#> .
@prefix process: <https://w3id.org/ddta/process#> .
@prefix ex: <https://example.org/ddta/data-read-example#> .

ex:ConfigurationLoader a ddta:System ;
    ddta:hasPrimaryFunction ex:LoadConfiguration ;
    ddta:hasOperationalEnvironment ex:LoaderEnvironment .
ex:LoadConfiguration a ddta:Function .
ex:LoaderEnvironment a ddta:Environment ;
    ddta:makesAvailable ex:PersistentConfigurationStore .
ex:PersistentConfigurationStore a data:StableStore ;
    ddta:stores ex:SettingsFile .
ex:SettingsFile a ddta:StoredContent ;
    data:hasDataBlock ex:LimitValue .
ex:LimitValue a data:DataBlock .
ex:LoadConfigurationProcess a ddta:Process ;
    ddta:realizesFunction ex:LoadConfiguration ;
    ddta:hasStep ex:ReadSettings ;
    process:hasInitialStep ex:ReadSettings .
ex:ReadSettings a ddta:ProcessStep, data:ReadStep ;
    data:readsFrom ex:LimitValue .

ex:LoaderEnvironment ddta:makesAvailable ex:WorkingStore .
ex:WorkingStore a data:RunningStore ; ddta:stores ex:SettingsRuntime .
ex:SettingsRuntime a ddta:StoredContent ; data:hasDataBlock ex:LimitRuntime .
ex:LimitRuntime a data:DataBlock .
ex:LoadConfigurationProcess ddta:hasStep ex:WriteSettings .
ex:ReadSettings ddta:hasNextStep ex:WriteSettings .
ex:WriteSettings a ddta:ProcessStep, data:WriteStep ; data:writesTo ex:LimitRuntime .
```

```mermaid
%%{init: {"htmlLabels":true,"theme":"base","layout":"elk"}}%%
flowchart TB
    subgraph O_428db40059bd9d["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#45845B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#45845B'>LoaderEnvironment</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#45845B'>ddta:Environment</span></div>"]
        direction TB
        subgraph G_7cba527d1798e5["Associated Systems"]
            direction TB
            subgraph O_581087f5f70b34["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#2563EB'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#2563EB'>ConfigurationLoader</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#2563EB'>ddta:System</span></div>"]
                direction LR
                subgraph G_233ab816f687a9["Primary Functions"]
                    direction LR
                    subgraph G_e73c7a6f53f652[" "]
                        direction TB
                        O_503683d3653ff2("<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#374151'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#374151'>LoadConfiguration</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#374151'>ddta:Function</span></div>")
                        subgraph G_eecbb3a6825262[" "]
                            direction TB
                            G_160d72ae92be71@{ img: "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSI0OCIgdmlld0JveD0iMCAwIDMyIDQ4IiBmaWxsPSJub25lIj48cGF0aCBkPSJNMTYgNDJWMTBNNiAyMCAxNiAxMGwxMCAxMCIgc3Ryb2tlPSIjN0I4Nzk0IiBzdHJva2Utd2lkdGg9IjMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPjwvc3ZnPg==", h: 42, constraint: "on" }
                            G_7823478af52c45(["realizesFunction"])
                            G_160d72ae92be71 ~~~ G_7823478af52c45
                        end
                        subgraph O_0314064ee76ee4["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:6px 10px;background:transparent'><span style='display:block;font-size:16px;font-weight:700;color:#334155'>LoadConfigurationProcess</span><span style='display:block;font-size:11px;color:#334155'>ddta:Process</span></div>"]
                            direction TB
                            PX_4d0cc6763ee2["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:6px 10px;background:transparent'><span style='display:block;font-size:16px;font-weight:700;color:#7B8794'>ReadSettings</span><span style='display:block;font-size:11px;color:#7B8794'>data:ReadStep</span></div>"]
                            PX_6a389943f0d2["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:6px 10px;background:transparent'><span style='display:block;font-size:16px;font-weight:700;color:#7B8794'>WriteSettings</span><span style='display:block;font-size:11px;color:#7B8794'>data:WriteStep</span></div>"]
                            PX_f1438d311c32(["START"])
                            style PX_f1438d311c32 fill:#F3F5F7,stroke:#B6BEC8,color:#596674
                            PX_f1438d311c32 --> PX_4d0cc6763ee2
                            PX_9b8571101ed9(["hasNextStep"])
                            style PX_9b8571101ed9 fill:#F3F4F6,stroke:#374151,color:#374151,rx:12px,ry:12px
                            PX_4d0cc6763ee2 --- PX_9b8571101ed9 --> PX_6a389943f0d2
                        end
                        O_503683d3653ff2 ~~~ G_eecbb3a6825262
                        G_eecbb3a6825262 ~~~ O_0314064ee76ee4
                    end
                end
            end
        end
        subgraph G_94e45325e68a72["Available Resources"]
            direction TB
            subgraph G_0527177b918bf1[" "]
                direction TB
                subgraph O_c92ec625d81fe8["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='27' height='27'/><div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#64748B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#64748B'>PersistentConfigurationStore</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#64748B'>data:StableStore</span></div>"]
                    direction TB
                    subgraph O_df442b376c32b7["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>SettingsFile</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>ddta:StoredContent</span></div>"]
                        direction TB
                        O_585e66346c49e2["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>LimitValue</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>data:DataBlock</span></div>"]
                    end
                end
                subgraph O_4be059eb594a51["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='27' height='27'/><div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#64748B'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#64748B'>WorkingStore</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#64748B'>data:RunningStore</span></div>"]
                    direction TB
                    subgraph O_902c118f0ac149["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>SettingsRuntime</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>ddta:StoredContent</span></div>"]
                        direction TB
                        O_04e831307b68ed["<div style='display:inline-block;text-align:center;white-space:nowrap;line-height:1.4;padding:8px 12px;background:transparent;opacity:1;color:#94A3B8'><span style='display:block;text-align:center;font-size:17px;font-weight:700;color:#94A3B8'>LimitRuntime</span><span style='display:block;text-align:center;font-size:12px;font-weight:400;color:#94A3B8'>data:DataBlock</span></div>"]
                    end
                end
                G_b79e146897bde4["<img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiM0NTg0NUIiIHN0cm9rZS13aWR0aD0iMS43NSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1djE0YzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTNWNSIvPjxwYXRoIGQ9Ik0zIDEyYzAgMS42NiA0LjAzIDMgOSAzczktMS4zNCA5LTMiLz48L3N2Zz4=' width='32' height='32'/>Stores"]
                O_4be059eb594a51 ~~~ G_b79e146897bde4
            end
        end
    end
    PX_393b3aded543(["readsFrom"])
    PX_4d0cc6763ee2 --- PX_393b3aded543 --> O_585e66346c49e2
    PX_978f55b893d8(["writesTo"])
    PX_6a389943f0d2 --- PX_978f55b893d8 --> O_04e831307b68ed
    classDef DDTA_C_ec3c1934ce4a fill:#E8F1FF,stroke:#2563EB,color:#2563EB,stroke-width:1.5px
    class O_581087f5f70b34 DDTA_C_ec3c1934ce4a
    classDef DDTA_C_764b3983e628 fill:#E8F1FF,stroke:#2563EB,color:#2563EB,stroke-width:1.5px,stroke-dasharray:5 4
    class G_233ab816f687a9 DDTA_C_764b3983e628
    classDef DDTA_C_47a0c203a3c4 fill:#EAF5EC,stroke:#45845B,color:#45845B,stroke-width:1.5px
    class G_7cba527d1798e5,G_94e45325e68a72,O_428db40059bd9d DDTA_C_47a0c203a3c4
    classDef DDTA_C_f87c22e49ae1 fill:#EAF5EC,stroke:#45845B,color:#45845B,stroke-width:1.5px,stroke-dasharray:5 4
    class G_0527177b918bf1 DDTA_C_f87c22e49ae1
    classDef DDTA_C_9c53de845317 fill:#F1F5F9,stroke:#64748B,color:#64748B,stroke-width:1.5px,rx:12px,ry:12px
    class O_4be059eb594a51,O_c92ec625d81fe8 DDTA_C_9c53de845317
    classDef DDTA_C_51a0b50eca1f fill:#F1F5F9,stroke:#94A3B8,color:#94A3B8,stroke-width:1.0px,stroke-dasharray:5 4,rx:5px,ry:5px
    class O_902c118f0ac149,O_df442b376c32b7 DDTA_C_51a0b50eca1f
    classDef DDTA_C_db520d489522 fill:#F8FAFC,stroke:#7B8794,color:#7B8794,stroke-width:2px
    classDef DDTA_C_a6bdc037a9c8 fill:#F8FAFC,stroke:#7B8794,color:#7B8794,stroke-width:2px,rx:8px,ry:8px
    class O_0314064ee76ee4 DDTA_C_a6bdc037a9c8
    classDef DDTA_C_1a97e3c85c24 fill:#FFFFFF,stroke:#374151,color:#374151,stroke-width:1.5px
    class O_503683d3653ff2 DDTA_C_1a97e3c85c24
    classDef DDTA_C_d75aabb7f485 fill:#FFFFFF,stroke:#94A3B8,color:#64748B,stroke-width:1.0px
    class O_04e831307b68ed,O_585e66346c49e2 DDTA_C_d75aabb7f485
    classDef DDTA_C_8158d1a47075 fill:#FFFFFF,stroke:transparent,color:#7B8794,stroke-width:0px
    class G_7823478af52c45 DDTA_C_8158d1a47075
    classDef DDTA_C_dd44c4d967c8 fill:transparent,stroke:transparent,stroke-width:0px
    class G_160d72ae92be71,G_b79e146897bde4,G_e73c7a6f53f652,G_eecbb3a6825262 DDTA_C_dd44c4d967c8
    classDef PROC_process fill:#F8FAFC,stroke:#7B8794,color:#334155,stroke-width:2px,rx:8px,ry:8px
    classDef PROC_coreProcessStep fill:#FFFFFF,stroke:#7B8794,color:#7B8794,stroke-width:1.5px,stroke-dasharray:5 4
    class PX_4d0cc6763ee2,PX_6a389943f0d2 PROC_coreProcessStep
    style PX_393b3aded543 fill:#F3F4F6,stroke:#374151,color:#374151,rx:12px,ry:12px
    style PX_978f55b893d8 fill:#F3F4F6,stroke:#374151,color:#374151,rx:12px,ry:12px
    linkStyle 0 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 4 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 5 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 6 stroke:transparent,stroke-width:0px,opacity:0
    linkStyle 2 stroke:#374151,stroke-width:1.8px,stroke-dasharray:6 4
    linkStyle 3 stroke:#374151,stroke-width:1.8px,stroke-dasharray:6 4
    linkStyle 7,8 stroke:#374151,stroke-width:1.8px,stroke-dasharray:6 4
    linkStyle 9,10 stroke:#374151,stroke-width:1.8px,stroke-dasharray:6 4
```
