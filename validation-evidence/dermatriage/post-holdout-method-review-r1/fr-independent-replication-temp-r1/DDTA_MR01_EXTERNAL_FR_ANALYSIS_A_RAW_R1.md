## DEC-MR01-01 — Triage in assenza di immagine

### FR-01 candidato

text

```
Parent Decision:
DEC-MR01-01 — Triage in assenza di immagine

FunctionalRequirement candidate:
FR-01 — Esecuzione del triage in assenza di immagine

Operational meaning:
Quando l'immagine della lesione non è disponibile per un caso, DermaTriage MUST eseguire comunque la valutazione di triage utilizzando le informazioni sintomatologiche disponibili sul caso.

Source evidence:
- DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R5_MR01_DECISIONS.pdf, DEC-MR01-01:
  Context: "Un caso dermatologico può avere un’immagine della lesione, oppure no."
  Decision: "DermaTriage valuta il triage anche se manca l’immagine della lesione. In quel caso usa le informazioni sui sintomi disponibili sul caso."
  Consequences: "Se l’immagine manca, il triage si può comunque fare."
- OR2_Architecture_Document.pdf, sez. 2: "Fallback: When no image is available, symptom-only scoring derives urgency from B4 chatbot interaction fields..."
  → usato solo come evidenza di realizzazione corrente, non come fonte di obbligo aggiuntivo.

Reason for treating it as a FunctionalRequirement:
La Decision governa un obbligo operativo condizionato: se manca l'immagine, il triage deve comunque avvenire e deve usare le informazioni sintomatologiche disponibili. È verificabile e discende da un solo Decision.

Reason for the chosen split/merge boundary:
Condizione "immagine assente" e azione "triage basato su sintomi" costituiscono una singola obbligazione coerente. Separarle produrrebbe una prima obbligazione di rilevamento dell'assenza immagine non governata dalla fonte.

Excluded or separated details:
- Definizione esatta di "immagine assente o non disponibile".
- Insieme minimo di informazioni sintomatologiche richieste.
- Requisito di equivalenza di output tra percorso con immagine e percorso senza immagine.
- Campi B4 specifici (itching, bleeding, growing, changing, pain, ecc.): dettaglio di realizzazione/binding corrente, non commitment governato in questa Decision.

Confidence:
MEDIUM — il nucleo dell'obbligo è chiaro; i confini operativi sono incompleti.

Observed ambiguity:
- Che cosa costituisce esattamente una immagine assente o non disponibile?
- Quali informazioni sintomatologiche minime devono essere disponibili?
- È richiesta equivalenza di output fra percorso con immagine e percorso senza immagine?

Alternative interpretation considered:
Trattare la Decision come due FR separati: (1) rilevare l'assenza immagine; (2) eseguire triage sintomatologico. Scartata perché la semantica di rilevamento non è governata dalla fonte.
```

svgsvg

### Verifica di completezza DEC-MR01-01

Assumendo FR-01 soddisfatto, DEC-MR01-01 può ancora essere violato?

**No, entro il significato governato.**
FR-01 copre la condizione e l'azione principale. Restano però lacune su: definizione di immagine assente, set minimo di sintomi, eventuale equivalenza di output. Queste non autorizzano a inventare FR aggiuntivi.

---

## DEC-MR01-02 — Scala di priorità P1-P4

### FR-02 candidato

text

```
Parent Decision:
DEC-MR01-02 — Scala di priorità P1-P4

FunctionalRequirement candidate:
FR-02 — Rappresentazione della priorità operativa sulla scala P1-P4

Operational meaning:
Quando DermaTriage determina una priorità operativa di triage per un caso, MUST rappresentarla come uno dei livelli P1, P2, P3 o P4.

Source evidence:
- DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R5_MR01_DECISIONS.pdf, DEC-MR01-02:
  Decision: "DermaTriage usa la scala P1-P4 per rappresentare la priorità operativa di triage."
  Consequences: "La priorità operativa è uno dei livelli P1, P2, P3 o P4. Le regole per assegnare il livello a un caso sono definite a parte."
- OR2_Architecture_Document.pdf, Adaptation Layer Mapping: tabella HIGH/MEDIUM/LOW → P1-P4 e SLA.
  → la tabella è trattata come realizzazione/evidenza corrente, non come mapping governato da questa Decision, perché il case study dichiara che le regole sono definite a parte e le interroga come aperte.

Reason for treating it as a FunctionalRequirement:
La Decision fissa un allowed result domain e un obbligo di rappresentazione dell'output. È operationalmente assessabile.

Reason for the chosen split/merge boundary:
Un solo obbligo: la priorità operativa, quando prodotta, deve essere espressa nella scala P1-P4. Non si unisce il mapping condizionale perché non è governato in questa Decision.

Excluded or separated details:
- Regola completa che mappa urgenza e confidence sulla P-scale.
- Soglia di confidence (configurabile o governata).
- Valori temporali associati a P1-P4 (SLA normativi, target o documentati).
- Trigger e owner degli SLA.
- Implementazione concreta dell'Adaptation Layer.

Confidence:
HIGH per la rappresentazione P1-P4; LOW per il mapping, che resta gap.

Observed ambiguity:
- Qual è la regola completa che mappa urgenza e confidence sulla P-scale?
- La soglia di confidence è un parametro configurabile o una regola governata?
- I valori temporali associati a P1-P4 sono SLA normativi, target o semplici valori documentati?
- Chi governa l'eventuale trigger e l'owner degli SLA?

Alternative interpretation considered:
Usare la tabella dell'OR2 Architecture Document come mapping governato e creare un FR condizionale. Scartata: la baseline DDTA R5 MR-01 tratta esplicitamente quelle regole come definite a parte e non chiuse; il mapping non è quindi un obbligo derivabile con sufficiente autorità.
```

svgsvg

### Verifica di completezza DEC-MR01-02

Assumendo FR-02 soddisfatto, DEC-MR01-02 può ancora essere violato?

**No, per la parte governata.**
La Decision richiede l'uso della scala P1-P4 per rappresentare la priorità operativa. FR-02 copre questo.
Resta fuori il mapping completo: se il sistema non assegna alcuna priorità, la violazione riguarda più MR-01 che questa Decision. La regola di assegnazione resta una lacuna.

---

## DEC-MR01-03 — Pipeline analitica a quattro stadi

### FR-03 candidato

text

```
Parent Decision:
DEC-MR01-03 — Pipeline analitica a quattro stadi

FunctionalRequirement candidate:
FR-03 — Pipeline sequenziale a quattro stadi per il percorso image-based

Operational meaning:
Quando è disponibile un'immagine della lesione, DermaTriage MUST realizzare il percorso di valutazione tramite una pipeline sequenziale a quattro stadi, in cui i risultati degli stadi precedenti alimentano le elaborazioni successive fino alla sintesi di triage.

Source evidence:
- DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R5_MR01_DECISIONS.pdf, DEC-MR01-03:
  Context: "Se c’è un’immagine della lesione, la valutazione di triage combina più passaggi analitici prima di arrivare a una sintesi del caso."
  Decision: "DermaTriage realizza il percorso basato sull’immagine con una pipeline sequenziale a quattro stadi. I risultati dei primi stadi alimentano le elaborazioni successive, fino alla sintesi di triage."
  Consequences: "Il percorso analitico resta una sequenza di quattro stadi. Le tecnologie e i modelli dentro i singoli stadi possono cambiare o evolvere senza per forza modificare questa struttura."
- OR2_Architecture_Document.pdf, sez. 2: Four-Stage AI Pipeline e Pipeline Flow.
  → usato come evidenza della realizzazione corrente, non per fissare modelli o algoritmi.

Reason for treating it as a FunctionalRequirement:
La Decision governa struttura e flusso informativo del percorso image-based. È un obbligo operativo verificabile.

Reason for the chosen split/merge boundary:
Numero di stadi, sequenzialità e alimentazione forward sono un'unica obbligazione strutturale coerente. Non si separano i singoli stadi perché la Decision non assegna loro obblighi specifici e ammette la sostituibilità di tecnologie/modelli.

Excluded or separated details:
- Modelli concreti: EfficientNet-B4, Qwen2-VL-7B-Instruct, ChromaDB/all-MiniLM-L6-v2, BioMistral-7B.
- Input/output specifici di ciascuno stadio.
- Algoritmi interni, threshold, prompt, retrieval top-5, JSON finale.
- Responsabilità interne dei singoli stadi: non governate da questa Decision.

Confidence:
HIGH per la struttura; MEDIUM per le responsabilità interne, che restano non specificate.

Observed ambiguity:
- È governato il numero esatto di quattro stadi o soltanto la separazione delle funzioni analitiche?
- L’ordine degli stadi è un commitment stabile oppure una proprietà della realizzazione corrente?
- Quali responsabilità appartengono alla Decision e quali restano comportamento interno dei singoli stadi?

Alternative interpretation considered:
Derivare quattro FR separati, uno per stadio, dalla documentazione originale. Scartata: la Decision stabilisce che le tecnologie e i modelli dentro gli stadi possono cambiare senza modificare la struttura; la baseline DDTA non promuove i dettagli di stadio a obblighi governati.
```

svgsvg

### Verifica di completezza DEC-MR01-03

Assumendo FR-03 soddisfatto, DEC-MR01-03 può ancora essere violato?

**No, per la parte governata.**
FR-03 copre: percorso image-based, quattro stadi, sequenzialità, alimentazione forward, sintesi di triage.
Restano lacune sulle responsabilità interne degli stadi e sull'esatto output della sintesi. Non si inventano FR di stadio.

---

## DEC-MR01-04 — Separazione tra valutazione dell’urgenza e priorità operativa

### FR-04 candidato

text

```
Parent Decision:
DEC-MR01-04 — Separazione tra valutazione dell’urgenza e priorità operativa

FunctionalRequirement candidate:
FR-04 — Separazione e ordine tra valutazione dell’urgenza e priorità operativa

Operational meaning:
Nel percorso basato sull’immagine, DermaTriage MUST mantenere separata la valutazione analitica dell’urgenza dalla determinazione successiva della priorità operativa di triage; la determinazione della priorità MUST avvenire dopo la valutazione dell’urgenza e MUST NOT avvenire dentro la pipeline analitica.

Source evidence:
- DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R5_MR01_DECISIONS.pdf, DEC-MR01-04:
  Context: "La valutazione del caso produce prima un risultato sull’urgenza, poi una priorità operativa per la presa in carico."
  Decision: "Nel percorso basato sull’immagine, DermaTriage tiene separata la valutazione analitica dell’urgenza dalla determinazione successiva della priorità operativa di triage."
  Consequences: "La priorità operativa si determina dopo la valutazione dell’urgenza, non dentro la pipeline analitica. La priorità risultante si esprime con la scala P1-P4."
- OR2_Architecture_Document.pdf, Adaptation Layer Mapping: la mappatura P-scale è mostrata dopo la pipeline.
  → evidenza di realizzazione, non fonte di obbligo aggiuntivo.

Reason for treating it as a FunctionalRequirement:
La Decision governa un boundary e un ordine temporale tra due risultati. È un obbligo operativo verificabile.

Reason for the chosen split/merge boundary:
Separazione e determinazione successiva sono un’unica obbligazione coerente: la priorità non solo è distinta, ma segue la valutazione dell’urgenza e non è interna alla pipeline analitica.

Excluded or separated details:
- Rappresentazione P1-P4: già coperta da FR-02, appartiene a DEC-MR01-02.
- Regola di mapping urgenza/confidence → P-level.
- SLA e relativi owner.
- Dettagli interni della pipeline.

Confidence:
HIGH.

Observed ambiguity:
- La separazione è un boundary architetturale intenzionale o soltanto la forma corrente della pipeline?
- La priorità operativa potrebbe essere prodotta direttamente dall’ultimo stadio senza violare un commitment documentato?
- Quali semantiche appartengono al boundary e quali alla futura regola operativa di mapping?

Alternative interpretation considered:
Dividere in due FR: uno per la separazione, uno per l’ordine temporale. Scartata: l’ordine “dopo” e il divieto “non dentro la pipeline” presuppongono la separazione; la fonte li tratta come un unico commitment.
```

svgsvg

### Verifica di completezza DEC-MR01-04

Assumendo FR-04 soddisfatto, DEC-MR01-04 può ancora essere violato?

**No, per la parte governata.**
FR-04 copre separazione, ordine successivo e divieto di determinazione dentro la pipeline analitica.
Resta fuori la regola di mapping, che appartiene a un altro significato o a una lacuna.

---

# Ambiguità e lacune trasversali

1. **DEC-MR01-01:** definizione di immagine assente/non disponibile; set minimo di informazioni sintomatologiche; eventuale equivalenza di output tra percorso con immagine e senza immagine.
2. **DEC-MR01-02:** regola completa di mapping urgenza/confidence → P1-P4; natura della soglia di confidence; statuto degli SLA; owner e trigger degli SLA.
3. **DEC-MR01-03:** se il numero quattro sia un commitment o una realizzazione corrente; se l’ordine sia stabile; quali responsabilità appartengano ai singoli stadi.
4. **DEC-MR01-04:** se la separazione sia boundary intenzionale o forma corrente; se la priorità possa essere prodotta direttamente dall’ultimo stadio senza violare un commitment documentato.

# Elementi esclusi e non promossi a FR

- Modelli e tecnologie concrete: EfficientNet-B4, Qwen2-VL-7B-Instruct, ChromaDB, all-MiniLM-L6-v2, BioMistral-7B.
- Parametri: soglia 0.25, confidence > 0.85, top-5, 20 esempi, 50 correzioni, 10 epoche, 5% rollback.
- Binding: campi B4, `agrees == False`, `consulto_id`, API endpoint, JWT, percorsi file.
- Valori SLA P1-P4 e relativi owner.
- Dettagli di realizzazione della pipeline e dell’Adaptation Layer.
- Eventuali SpecializedRequirement non ancora governati (es. proprietà di sicurezza, qualità, lifecycle).

# Sintesi mapping FR → Decision

| **FRParent DecisionOggetto** |             |                                                                   |
| ---------------------------- | ----------- | ----------------------------------------------------------------- |
| FR-01                        | DEC-MR01-01 | Triage in assenza di immagine tramite sintomi disponibili         |
| FR-02                        | DEC-MR01-02 | Rappresentazione priorità operativa come P1-P4                    |
| FR-03                        | DEC-MR01-03 | Pipeline sequenziale a quattro stadi per percorso image-based     |
| FR-04                        | DEC-MR01-04 | Separazione e ordine tra valutazione urgenza e priorità operativa |

**Esito:** derivazione indipendente completata e congelata. Le lacune sono registrate come gap documentali, non colmate con requisiti inventati.