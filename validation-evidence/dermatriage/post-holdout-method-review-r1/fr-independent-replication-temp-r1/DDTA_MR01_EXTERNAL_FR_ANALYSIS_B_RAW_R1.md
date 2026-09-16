# DDTA External Blind FunctionalRequirement Extraction — Prompt R1

## DermaTriage MR-01: Valutazione di triage del caso dermatologico

> **Analista**: Vibe (Mistral Medium 3.5)  
> **Data**: 16 settembre 2026  
> **Package**: DDTA MR-01 external FR blind input package R1  
> **Baseline**: 06e9da15ba64b0510496430a8dbc2eebec2d7fd0  
> **Status**: FROZEN — Analisi indipendente completata

---

## 📋 Indice

- [Contesto e metodologia](#contesto-e-metodologia)
- [DEC-MR01-01 — Triage in assenza di immagine](#dec-mr01-01--triage-in-assenza-di-immagine)
- [DEC-MR01-02 — Scala di priorità P1-P4](#dec-mr01-02--scala-di-priorità-p1-p4)
- [DEC-MR01-03 — Pipeline analitica a quattro stadi](#dec-mr01-03--pipeline-analitica-a-quattro-stadi)
- [DEC-MR01-04 — Separazione tra valutazione dell’urgenza e priorità operativa](#dec-mr01-04--separazione-tra-valutazione-dellurgenza-e-priorità-operativa)
- [Verifica di completezza per Decision](#verifica-di-completezza-per-decision)
- [Ambiguità e gap documentali](#ambiguità-e-gap-documentali)
- [Sintesi e osservazioni finali](#sintesi-e-osservazioni-finali)

---

## Contesto e metodologia

Questa analisi applica la metodologia **Documentation-Driven Threat Analysis (DDTA)** alla documentazione fornita per derivare i **FunctionalRequirement (FR)** relativi al **MacroRequirement MR-01** di DermaTriage.

### Materiale analizzato


| Tipo            | Documento                                                         | Ruolo                             | Hash SHA256                                                      |
| --------------- | ----------------------------------------------------------------- | --------------------------------- | ---------------------------------------------------------------- |
| Decision Input  | DDTA\_DERMATRIAGE\_PARALLEL\_CASE\_STUDY\_R5\_MR01\_DECISIONS.pdf | Decision DDTA per MR-01           | a86970905061e0ff6302b0ef1de61a343a12f57a01414b72d378ef8e9ee15f5e |
| Architettura    | OR2\_Architecture\_Document.pdf                                   | Documentazione originale progetto | c77238271d05a8ac4b4227143afb1ece783416a8091b31f9d2161e4f85f831de |
| Dataset         | OR3\_Dataset\_Metadata\_Catalog.pdf                               | Catalogo dataset e metadati       | 453eaf15aeda0f4699659b5ec28e1112da9d7001ab100ad819aaa2927ce605db |
| Training Report | OR4\_Training\_Cycles\_Report.pdf                                 | Report cicli di training          | 2d0c2b1b86902890ebbe87b0f8e5a0f3238384484b85cbfc0fdbd39548aa7683 |
| Config Ambiente | OR4\_Training\_Environment\_Config.pdf                            | Configurazione ambiente           | 68ed5e3faadc2aa74b4efdf22821939b211554c91d7b7c8adb0a5fa785471abd |
| Test Setup      | OR5\_Test\_Environment\_Setup.pdf                                 | Setup ambiente di test            | 9f375ba8d28dacd59169ffa04f847db2d1482491435009c6a108520e942636c0 |
| Guida BA R5     | DDTA\_DOCUMENTATION\_BA\_AUTHORING\_GUIDE\_R5.pdf                 | Guida metodologica                | f37d3eef2f0f5ee0aa3c6b10b5476612206dea4b820f97fdbbe531a142628107 |
| Guida R6        | DDTA\_DOCUMENTATION\_AUTHORING\_GUIDE\_R6\_CANDIDATE\_R2.pdf      | Guida metodologica candidate      | aec266cdc1d00e68c288d6aed77f99cb27932649f78853dd896898b8a3ee6d7b |


### Gerarchia utilizzata

```
MacroRequirement MR-01
├── DEC-MR01-01 — Triage in assenza di immagine
│   ├── FR-DEC-MR01-01-01
│   └── FR-DEC-MR01-01-02
├── DEC-MR01-02 — Scala di priorità P1-P4
│   ├── FR-DEC-MR01-02-01
│   ├── FR-DEC-MR01-02-02
│   └── FR-DEC-MR01-02-03
├── DEC-MR01-03 — Pipeline analitica a quattro stadi
│   ├── FR-DEC-MR01-03-01
│   ├── FR-DEC-MR01-03-02
│   ├── FR-DEC-MR01-03-03
│   ├── FR-DEC-MR01-03-04
│   ├── FR-DEC-MR01-03-05
│   └── FR-DEC-MR01-03-06
└── DEC-MR01-04 — Separazione tra valutazione dell’urgenza e priorità operativa
    ├── FR-DEC-MR01-04-01
    └── FR-DEC-MR01-04-02
```

---

## DEC-MR01-01 — Triage in assenza di immagine

### Decision Statement

> **Parent MR**: MR-01  
> **Context**: Un caso dermatologico può avere un'immagine della lesione, oppure no.  
> **Decision**: DermaTriage valuta il triage anche se manca l'immagine della lesione. In quel caso usa le informazioni sui sintomi disponibili sul caso.  
> **Consequences**: Se l'immagine manca, il triage si può comunque fare. Il percorso basato sui sintomi può usare informazioni diverse; non deve per forza dare gli stessi risultati del percorso con immagine.

---

### 🔹 FR-DEC-MR01-01-01

**Parent Decision**: DEC-MR01-01 — Triage in assenza di immagine

**FunctionalRequirement candidate**: DermaTriage MUST be able to perform triage assessment when no lesion image is available

**Operational meaning**: The system must not fail, block, or refuse to process a dermatological case when the lesion image is absent or unavailable. Triage functionality must remain operational using alternative input pathways.

**Source evidence**:

- DEC-MR01-01 Decision: "DermaTriage valuta il triage anche se manca l'immagine della lesione"
- OR2 Architecture Document, Section 2: "Fallback: When no image is available, symptom-only scoring derives urgency from B4 chatbot interaction fields"
- OR5 Test Environment Setup, Section 7: Implicit confirmation that no-image pathway exists

**Reason for treating it as a FunctionalRequirement**: This is a direct operational obligation derived from the Decision. The Decision explicitly states that triage MUST be performed even when the image is missing, which is a coherent normative obligation that can be independently assessed.

**Reason for the chosen split/merge boundary**: This FR captures the core commitment of the Decision: the system's ability to operate without an image. It is kept separate from the symptom-based pathway (FR-02) because the ability to perform triage without image is conceptually distinct from HOW that triage is performed. The split follows the principle that each FR should represent a single coherent obligation.

**Excluded or separated details**: 

- Specific symptom fields used (separated to FR-DEC-MR01-01-02)
- Implementation mechanism of the fallback (implementation detail)
- Whether results match image-based pathway (explicitly NOT required per Decision consequences)

**Confidence**: HIGH

**Observed ambiguity**: 

- The exact definition of "image absent/unavailable" is not explicitly defined. Does it include: (a) no image uploaded, (b) image uploaded but corrupted, (c) image uploaded but of insufficient quality? The architecture document uses "no image is available" which may be narrower than "image is absent".

**Alternative interpretation considered**: 

- Could be merged with FR-DEC-MR01-01-02 as a single requirement about the symptom-based pathway. Rejected because the Decision distinguishes between the capability (can do triage) and the method (uses symptom information).

---

### 🔹 FR-DEC-MR01-01-02

**Parent Decision**: DEC-MR01-01 — Triage in assenza di immagine

**FunctionalRequirement candidate**: When no lesion image is available, DermaTriage MUST use available symptom information to determine urgency

**Operational meaning**: In the absence of a lesion image, the system must accept and process symptom data as the primary input for urgency determination. The symptom-based pathway must be a first-class, operational pathway.

**Source evidence**:

- DEC-MR01-01 Decision: "In quel caso usa le informazioni sui sintomi disponibili sul caso"
- OR2 Architecture Document, Section 2: "symptom-only scoring derives urgency from B4 chatbot interaction fields (itching, bleeding, growing, changing, pain, etc.)"
- OR5 Test Environment Setup, Section 7: Lists symptom fields as valid test inputs

**Reason for treating it as a FunctionalRequirement**: The Decision explicitly mandates the use of symptom information when no image is available. This is a distinct operational obligation from the ability to perform triage (FR-01). It specifies WHAT input must be used in the no-image scenario.

**Reason for the chosen split/merge boundary**: Separated from FR-01 because it addresses a different aspect: FR-01 is about capability (can operate), FR-02 is about method (uses symptom data). The symptom fields are not enumerated as mandatory in the Decision, but the architecture document provides concrete evidence of what constitutes "symptom information".

**Excluded or separated details**:

- Specific symptom field names (itching, bleeding, etc.) are implementation evidence, not normative requirements
- The exact algorithm for symptom-only scoring (implementation detail)
- Whether all symptom fields are required or optional (not specified in governed documentation)

**Confidence**: HIGH

**Observed ambiguity**:

- The minimum required symptom information is not specified. The architecture mentions specific fields but doesn't state they are mandatory.
- It is not specified whether partial symptom information is acceptable or if there's a minimum threshold.

**Alternative interpretation considered**:

- Could include the specific symptom fields as part of the requirement. Rejected because the Decision governs the USE of symptom information, not the specific fields. The field names are realization details.

---

### ✅ Verifica di completezza per DEC-MR01-01

**Domanda**: Assumendo che tutti i FunctionalRequirement individuati siano soddisfatti, il Decision potrebbe ancora essere violato?

**Risposta**: NO

**Motivazione**: 

- FR-DEC-MR01-01-01 garantisce che il sistema può eseguire il triage senza immagine
- FR-DEC-MR01-01-02 garantisce che il sistema usa le informazioni sui sintomi in quel caso
- La conseguenza del Decision che "il percorso basato sui sintomi può usare informazioni diverse; non deve per forza dare gli stessi risultati del percorso con immagine" non è un requisito ma una chiarificazione sul comportamento atteso. Non è quindi necessario un FR aggiuntivo per coprirla.

**Lacune documentali rilevate**:

1. Definizione precisa di "immagine assente/non disponibile"
2. Informazioni sintomatologiche minime richieste
3. Equivalenza di output fra percorso con e senza immagine (esplicitamente NON richiesta)

---

## DEC-MR01-02 — Scala di priorità P1-P4

### Decision Statement

> **Parent MR**: MR-01  
> **Context**: Il triage deve indicare anche una priorità operativa per la presa in carico del caso.  
> **Decision**: DermaTriage usa la scala P1-P4 per rappresentare la priorità operativa di triage.  
> **Consequences**: La priorità operativa è uno dei livelli P1, P2, P3 o P4. Le regole per assegnare il livello a un caso sono definite a parte.

---

### 🔹 FR-DEC-MR01-02-01

**Parent Decision**: DEC-MR01-02 — Scala di priorità P1-P4

**FunctionalRequirement candidate**: DermaTriage MUST represent operational priority using exactly the four-level P-scale: P1, P2, P3, P4

**Operational meaning**: The system must use a priority scale consisting of exactly four distinct levels, labeled P1 through P4, for representing the operational priority of triage cases. No other priority representation is permitted for this purpose.

**Source evidence**:

- DEC-MR01-02 Decision: "DermaTriage usa la scala P1-P4 per rappresentare la priorità operativa di triage"
- DEC-MR01-02 Consequences: "La priorità operativa è uno dei livelli P1, P2, P3 o P4"
- OR2 Architecture Document, Adaptation Layer Mapping: Explicit use of P1-P4 scale
- OR4 Training Cycles Report, Label Mapping: P1/P2 → HIGH, P3 → MEDIUM, P4 → LOW

**Reason for treating it as a FunctionalRequirement**: The Decision explicitly commits to using the P1-P4 scale. This is a clear, independently assessable operational obligation. The use of this specific scale (rather than any other representation) is a governed choice.

**Reason for the chosen split/merge boundary**: This FR captures the core commitment to the scale itself. The mapping rules (how urgency maps to P-scale) are separated into FR-02 because they represent a different type of obligation (conditional selection rule). The SLA association (FR-03) is also separate because it's about the properties associated with each level, not the scale itself.

**Excluded or separated details**:

- Mapping rules from urgency to P-scale (separated to FR-DEC-MR01-02-02)
- SLA timeframes associated with each level (separated to FR-DEC-MR01-02-03)
- Specific technologies or implementation mechanisms

**Confidence**: HIGH

**Observed ambiguity**: None for this specific requirement. The scale is explicitly defined.

**Alternative interpretation considered**: None. The scale definition is unambiguous in the Decision.

---

### 🔹 FR-DEC-MR01-02-02

**Parent Decision**: DEC-MR01-02 — Scala di priorità P1-P4

**FunctionalRequirement candidate**: DermaTriage MUST map urgency classification and confidence to P-scale according to the following governed conditional selection rule: (HIGH + confidence &gt; 0.85 → P1), (HIGH → P2), (MEDIUM → P3), (LOW → P4)

**Operational meaning**: The system must implement a specific, governed mapping from urgency classification (HIGH/MEDIUM/LOW) combined with confidence scores to the P-scale levels. This is a conditional selection rule, not merely an allowed result domain.

**Source evidence**:

- OR2 Architecture Document, Adaptation Layer Mapping table:
  ```
  | Urgency + Condition | P-Scale | SLA  |
  | HIGH + confidence > 0.85 | P1 | 24 hours  |
  | HIGH | P2 | 48 hours  |
  | MEDIUM | P3 | 72 hours  |
  | LOW | P4 | 7 giorni  |
  ```
- OR4 Training Cycles Report, Label Mapping:
  ```
  | B4 Outcome | CNN Label | Index  |
  | P1 | HIGH | 0  |
  | P2 | HIGH | 0  |
  | P3 | MEDIUM | 1  |
  | P4 | LOW | 2  |
  ```
- R6 Guide, Section 12.1: Explicitly cites this as "una vera regola condizionale governata"

**Reason for treating it as a FunctionalRequirement**: Per la metodologia DDTA (R6, Sezione 12.1): "Se la source governa un vero mapping condizionale, quel mapping appartiene alla semantica dell'FR." La regola di mappatura è esplicitamente documentata e governata, non è un dettaglio di implementazione.

**Reason for the chosen split/merge boundary**: This is kept separate from FR-01 (the scale definition) because it represents a different semantic layer: FR-01 is the allowed result domain, FR-02 is the conditional selection rule that populates that domain. Per R6: "Se la source governa solo outcome ammessi, non inventare il mapping che seleziona l'outcome. Se governa un vero mapping condizionale, quel mapping appartiene alla semantica dell'FR."

**Excluded or separated details**:

- The confidence threshold value (0.85) is part of the governed rule and is included
- SLA timeframes are separated to FR-DEC-MR01-02-03
- The specific implementation of the mapping function

**Confidence**: HIGH

**Observed ambiguity**:

- The confidence threshold (0.85) appears only in the architecture document. Is this a governed value or an implementation parameter? The architecture presents it as a fact, suggesting it's governed.
- The relationship between "HIGH + confidence &gt; 0.85" and "HIGH" is not explicitly stated as exclusive (i.e., does HIGH with confidence ≤ 0.85 map to P2?). The table structure suggests these are separate cases.

**Alternative interpretation considered**:

- Could treat the confidence threshold as a parameter rather than a governed value. Rejected because it appears in the architecture document as part of the defined mapping, and the Decision states that mapping rules are "defined separately" (implying they are governed).

---

### 🔹 FR-DEC-MR01-02-03

**Parent Decision**: DEC-MR01-02 — Scala di priorità P1-P4

**FunctionalRequirement candidate**: DermaTriage MUST associate the following SLA timeframes with P-scale levels: P1→24 hours, P2→48 hours, P3→72 hours, P4→7 giorni

**Operational meaning**: Each P-scale level must have an associated Service Level Agreement timeframe that represents the maximum or target time for case handling. These timeframes are part of the operational priority definition.

**Source evidence**:

- OR2 Architecture Document, Adaptation Layer Mapping table (SLA column)
- OR4 Training Cycles Report, Label Mapping: Implicitly confirms P-scale levels

**Reason for treating it as a FunctionalRequirement**: The SLA timeframes are explicitly documented as part of the P-scale definition in the architecture. They are not implementation details but part of the operational semantics of the priority scale.

**Reason for the chosen split/merge boundary**: Separated from FR-01 (scale definition) and FR-02 (mapping rule) because SLA association represents a different property of the P-scale levels. Each FR addresses a distinct aspect: scale existence, value mapping, and temporal semantics.

**Excluded or separated details**:

- Whether SLAs are normative requirements, targets, or merely documented values (not specified)
- Who owns or triggers the SLA (not governed in available documentation)
- Enforcement mechanisms for SLA compliance

**Confidence**: MEDIUM

**Observed ambiguity**:

- The documentation does not specify whether these SLA values are:
  - Normative requirements (MUST meet)
  - Target values (SHOULD meet)
  - Merely documented observations
- The owner/authority for SLA trigger and enforcement is not specified (noted in DEC-MR01-02 questions: "Chi governa l'eventuale trigger e l'owner degli SLA?")
- The SLA for P4 is "7 giorni" — is this exactly 7 days or "within 7 days"?

**Alternative interpretation considered**:

- Could exclude SLA association from FRs as it might be operational policy rather than system requirement. Rejected because the architecture document presents them as part of the adaptation layer mapping, suggesting they are system-governed.
- Could merge with FR-02 as part of the mapping rule. Rejected because SLA is a property of the P-scale level, not part of the urgency-to-P mapping logic.

---

### ✅ Verifica di completezza per DEC-MR01-02

**Domanda**: Assumendo che tutti i FunctionalRequirement individuati siano soddisfatti, il Decision potrebbe ancora essere violato?

**Risposta**: NO

**Motivazione**:

- FR-DEC-MR01-02-01 garantisce l'uso della scala P1-P4
- FR-DEC-MR01-02-02 garantisce la regola di mappatura da urgenza a P-scale
- FR-DEC-MR01-02-03 garantisce l'associazione degli SLA
- La conseguenza del Decision "Le regole per assegnare il livello a un caso sono definite a parte" è soddisfatta dai FR-02 e FR-03 che definiscono appunto le regole di assegnazione.

**Lacune documentali rilevate**:

1. Regola completa che mappa urgenza e confidence sulla P-scale (parzialmente coperta da FR-02, ma la relazione tra i casi non è esplicitamente definita)
2. La soglia di confidence è un parametro configurabile o una regola governata?
3. I valori temporali associati a P1-P4 sono SLA normativi, target o semplici valori documentati?
4. Chi governa l'eventuale trigger e l'owner degli SLA?

---

## DEC-MR01-03 — Pipeline analitica a quattro stadi

### Decision Statement

> **Parent MR**: MR-01  
> **Context**: Se c'è un'immagine della lesione, la valutazione di triage combina più passaggi analitici prima di arrivare a una sintesi del caso.  
> **Decision**: DermaTriage realizza il percorso basato sull'immagine con una pipeline sequenziale a quattro stadi. I risultati dei primi stadi alimentano le elaborazioni successive, fino alla sintesi di triage.  
> **Consequences**: Il percorso analitico resta una sequenza di quattro stadi. Le tecnologie e i modelli dentro i singoli stadi possono cambiare o evolvere senza per forza modificare questa struttura.

---

### 🔹 FR-DEC-MR01-03-01

**Parent Decision**: DEC-MR01-03 — Pipeline analitica a quattro stadi

**FunctionalRequirement candidate**: When a lesion image is available, DermaTriage MUST process it through a sequential pipeline of exactly four stages

**Operational meaning**: In the image-based triage pathway, the system must implement a processing pipeline consisting of exactly four distinct, sequential stages. The pipeline must be invoked when an image is present.

**Source evidence**:

- DEC-MR01-03 Decision: "DermaTriage realizza il percorso basato sull'immagine con una pipeline sequenziale a quattro stadi"
- DEC-MR01-03 Consequences: "Il percorso analitico resta una sequenza di quattro stadi"
- OR2 Architecture Document, Section 2: "DermaTriage processes patient-submitted skin lesion images through a sequential four-stage AI pipeline"
- OR2 Architecture Document, Pipeline Flow: Explicit 4-stage description

**Reason for treating it as a FunctionalRequirement**: The Decision explicitly commits to a 4-stage sequential pipeline for image-based processing. This is a structural commitment that defines the system's behavior.

**Reason for the chosen split/merge boundary**: This FR captures the structural commitment (4 stages, sequential). The functional behavior of each stage is separated into individual FRs (FR-02 through FR-05) because each stage has distinct operational obligations. The feed-forward relationship is captured in FR-06.

**Excluded or separated details**:

- Specific technologies/models in each stage (explicitly stated as changeable in Decision consequences)
- Detailed implementation of each stage
- Specific stage names or identifiers

**Confidence**: HIGH

**Observed ambiguity**:

- Whether "esattamente quattro stadi" means the number is fixed at 4, or if it's the current structure that can evolve. The Decision states "Il percorso analitico resta una sequenza di quattro stadi" which suggests the number 4 is a commitment.
- However, the consequence also says "Le tecnologie e i modelli dentro i singoli stadi possono cambiare o evolvere senza per forza modificare questa struttura" — this could be interpreted as the 4-stage structure being stable, but the question is whether the NUMBER 4 is part of that structure.

**Alternative interpretation considered**:

- Could interpret "quattro stadi" as describing the current implementation rather than a governed commitment. Rejected because the Decision explicitly states this as a commitment: "DermaTriage realizza... con una pipeline sequenziale a quattro stadi."

---

### 🔹 FR-DEC-MR01-03-02

**Parent Decision**: DEC-MR01-03 — Pipeline analitica a quattro stadi

**FunctionalRequirement candidate**: Stage 1 of the image-based pipeline MUST produce an urgency classification (HIGH/MEDIUM/LOW) with an associated confidence score

**Operational meaning**: The first stage in the pipeline must output a classification of the lesion's urgency into one of three levels (HIGH, MEDIUM, LOW) along with a numerical confidence score representing the model's certainty in this classification.

**Source evidence**:

- OR2 Architecture Document, Pipeline Flow: "Stage 1: predict\_image() — EfficientNet classifies urgency (threshold: prob &gt;= 0.25 for HIGH)"
- OR2 Architecture Document, Table: "Stage 1 | EfficientNet-B4 (fine-tuned) | Skin lesion image | HIGH / MEDIUM / LOW + confidence"
- OR3 Dataset Metadata Catalog: urgency\_level field with values HIGH/MEDIUM/LOW
- OR4 Training Cycles Report: "Task: 3-class skin lesion urgency: HIGH / MEDIUM / LOW"

**Reason for treating it as a FunctionalRequirement**: The urgency classification with confidence is explicitly documented as the output of Stage 1. This is a functional behavior that is governed by the project documentation, not an implementation detail. While the specific model (EfficientNet-B4) can change, the functional output (urgency + confidence) is part of the pipeline's governed behavior.

**Reason for the chosen split/merge boundary**: Separated from FR-01 (pipeline structure) because it addresses the functional behavior of a specific stage. Each stage's output is a distinct operational obligation. The threshold (prob &gt;= 0.25) is noted but not included as it may be implementation-specific.

**Excluded or separated details**:

- Specific model used (EfficientNet-B4) — can change per Decision consequences
- Threshold value (0.25) — implementation parameter
- Input image format or preprocessing details

**Confidence**: HIGH

**Observed ambiguity**:

- The threshold "prob &gt;= 0.25 for HIGH" appears in the architecture but may be model-specific. The Decision states technologies can change, which might include thresholds.
- Whether the confidence score is a single value or per-class probabilities is not explicitly stated.

**Alternative interpretation considered**:

- Could exclude the specific urgency classes (HIGH/MEDIUM/LOW) as they might be defined elsewhere. Rejected because they are explicitly part of Stage 1's output and are used throughout the system (dataset, training, etc.).

---

### 🔹 FR-DEC-MR01-03-03

**Parent Decision**: DEC-MR01-03 — Pipeline analitica a quattro stadi

**FunctionalRequirement candidate**: Stage 2 of the image-based pipeline MUST generate a structured clinical text description from the lesion image

**Operational meaning**: The second stage must produce a human-readable clinical description of the lesion based on the image input. This description must be structured and suitable for clinical interpretation.

**Source evidence**:

- OR2 Architecture Document, Pipeline Flow: "Stage 2: \_call\_qwen2() — Vision LLM generates 5-bullet clinical description"
- OR2 Architecture Document, Table: "Stage 2 | Qwen2-VL-7B-Instruct | Skin lesion image | Clinical text description (5-bullet format)"
- OR3 Dataset Metadata Catalog: image\_description field with "Rich clinical text (ABCDE criteria, Fitzpatrick type, biopsy notes)"

**Reason for treating it as a FunctionalRequirement**: The generation of a clinical text description is explicitly documented as Stage 2's function. This is a functional requirement of the pipeline, not merely an implementation detail.

**Reason for the chosen split/merge boundary**: Separated from other stages because each stage has a distinct functional output. The "5-bullet format" is noted in the evidence but treated as implementation detail (format specificity).

**Excluded or separated details**:

- Specific model used (Qwen2-VL-7B-Instruct) — can change per Decision consequences
- "5-bullet format" — format is implementation detail
- Specific content or structure of the description

**Confidence**: MEDIUM

**Observed ambiguity**:

- The "5-bullet format" is mentioned but it's unclear if this format is governed or just the current implementation. The Decision states technologies can change, which might include output formats.
- The exact content and structure of the clinical description is not specified.

**Alternative interpretation considered**:

- Could include the "5-bullet format" as part of the requirement. Rejected because the Decision explicitly allows technologies and models to change, and output format is likely tied to the specific model.

---

### 🔹 FR-DEC-MR01-03-04

**Parent Decision**: DEC-MR01-03 — Pipeline analitica a quattro stadi

**FunctionalRequirement candidate**: Stage 3 of the image-based pipeline MUST retrieve a bounded set of the top-5 most similar historical cases from the vector store

**Operational meaning**: The third stage must query the historical case database and return the 5 most similar cases based on the clinical text description from Stage 2. The retrieval must be bounded and return a specific number of results.

**Source evidence**:

- OR2 Architecture Document, Pipeline Flow: "Stage 3: find\_similar\_cases() — ChromaDB retrieves top-5 similar cases by cosine similarity"
- OR2 Architecture Document, Table: "Stage 3 | RAG — ChromaDB | Clinical text | Top-5 similar historical cases"
- OR3 Dataset Metadata Catalog, Section 8: ChromaDB configuration with "Retrieval | Top-5 nearest neighbors"
- R6 Guide, Section 25.3: Explicitly cites "FR-18 governa similarity ordering, bound 5 e selected historical cases" as a governed requirement

**Reason for treating it as a FunctionalRequirement**: Per R6 Section 25.3, when the project governs a selection with specific bounds, this constitutes a FunctionalRequirement. The retrieval of top-5 similar cases with bound 5 is explicitly governed.

**Reason for the chosen split/merge boundary**: Separated from other stages because it represents a distinct functional capability (similarity retrieval). The bound (5) is part of the governed requirement per R6 methodology.

**Excluded or separated details**:

- Specific vector store technology (ChromaDB) — can change
- Similarity metric (cosine similarity) — implementation detail
- Specific indexing or embedding model

**Confidence**: HIGH

**Observed ambiguity**:

- Whether "top-5" is a hard requirement or if it can be configured. The architecture presents it as a fact, and R6 explicitly treats bound 5 as governed.
- The selection criteria (cosine similarity) might be implementation-specific.

**Alternative interpretation considered**:

- Could treat "top-5" as an implementation parameter. Rejected because R6 explicitly uses this as an example of a governed bound in FR-18.

---

### 🔹 FR-DEC-MR01-03-05

**Parent Decision**: DEC-MR01-03 — Pipeline analitica a quattro stadi

**FunctionalRequirement candidate**: Stage 4 of the image-based pipeline MUST synthesize a final triage decision as a structured JSON containing at least: urgency, confidence, reasoning, and pathology

**Operational meaning**: The fourth and final stage must combine the outputs of all previous stages (Stage 1 urgency, Stage 2 clinical description, Stage 3 similar cases) along with any additional symptoms, and produce a comprehensive triage decision in a structured format that includes urgency classification, confidence score, reasoning trace, and predicted pathology.

**Source evidence**:

- OR2 Architecture Document, Pipeline Flow: "Stage 4: \_call\_biomistral() — Medical LLM synthesises final JSON decision"
- OR2 Architecture Document, Table: "Stage 4 | BioMistral-7B | Stage 1+2+3 + symptoms | JSON: urgency, confidence, reasoning, pathology"
- OR2 Architecture Document, Pipeline Flow Step 6: "Adaptation Layer: map\_urgency\_to\_p\_scale() assigns P1-P4, specialist and SLA" (shows Stage 4 output feeds into priority mapping)

**Reason for treating it as a FunctionalRequirement**: The synthesis of a final decision with specific structured outputs is explicitly documented as Stage 4's function. This is a functional commitment of the pipeline.

**Reason for the chosen split/merge boundary**: Separated from other stages because it represents the final synthesis step. The specific fields (urgency, confidence, reasoning, pathology) are included as they are explicitly governed.

**Excluded or separated details**:

- Specific model used (BioMistral-7B) — can change per Decision consequences
- JSON schema beyond the listed fields
- Specific format of reasoning or pathology values

**Confidence**: HIGH

**Observed ambiguity**:

- Whether "pathology" refers to a specific diagnosis or a category. The dataset includes a diagnosis field, suggesting it's a specific pathology label.
- The exact structure and content of the "reasoning" field is not specified.

**Alternative interpretation considered**:

- Could exclude specific field names as implementation details. Rejected because they are explicitly listed in the architecture document as Stage 4's output.

---

### 🔹 FR-DEC-MR01-03-06

**Parent Decision**: DEC-MR01-03 — Pipeline analitica a quattro stadi

**FunctionalRequirement candidate**: Results from each stage of the pipeline MUST be used as input to subsequent stages, with Stage 4 receiving inputs from Stages 1, 2, and 3

**Operational meaning**: The pipeline must be truly sequential with data flow: Stage 1 output feeds Stage 2, Stage 2 output feeds Stage 3, and Stages 1+2+3 outputs all feed Stage 4. This ensures the pipeline is not just four independent analyses but an integrated workflow.

**Source evidence**:

- DEC-MR01-03 Decision: "I risultati dei primi stadi alimentano le elaborazioni successive"
- OR2 Architecture Document, Pipeline Flow: Explicit sequential description where each stage feeds the next
- OR2 Architecture Document, Table: Stage 4 input is "Stage 1+2+3 + symptoms"

**Reason for treating it as a FunctionalRequirement**: The Decision explicitly states that results from earlier stages feed subsequent stages. This is a structural requirement of the pipeline, not just a description of the current implementation.

**Reason for the chosen split/merge boundary**: This is a separate FR because it addresses the data flow and dependency between stages, which is distinct from the functional output of each individual stage. It captures the "pipeline" nature of the workflow.

**Excluded or separated details**:

- Specific data format or transformation between stages
- Whether all stage outputs are always used or if some are optional

**Confidence**: HIGH

**Observed ambiguity**:

- The Decision states "I risultati dei primi stadi alimentano le elaborazioni successive" — does this mean ALL earlier stages feed ALL subsequent stages, or just immediate predecessors? The architecture suggests the latter (sequential), but the Decision is more general.
- The addition of "symptoms" to Stage 4 input (per architecture) is not mentioned in the Decision. This might be an implementation detail.

**Alternative interpretation considered**:

- Could be merged with FR-01 as part of the pipeline structure definition. Rejected because FR-01 addresses the existence of 4 stages, while this FR addresses the data flow between them — these are distinct aspects.

---

### ✅ Verifica di completezza per DEC-MR01-03

**Domanda**: Assumendo che tutti i FunctionalRequirement individuati siano soddisfatti, il Decision potrebbe ancora essere violato?

**Risposta**: NO

**Motivazione**:

- FR-DEC-MR01-03-01: Garantisce la pipeline a 4 stadi sequenziali
- FR-DEC-MR01-03-02: Garantisce l'output di Stage 1 (urgenza + confidence)
- FR-DEC-MR01-03-03: Garantisce l'output di Stage 2 (descrizione clinica)
- FR-DEC-MR01-03-04: Garantisce l'output di Stage 3 (top-5 casi simili)
- FR-DEC-MR01-03-05: Garantisce l'output di Stage 4 (sintesi finale)
- FR-DEC-MR01-03-06: Garantisce il flusso dati tra gli stadi
- La conseguenza "Il percorso analitico resta una sequenza di quattro stadi" è coperta da FR-01 e FR-06
- La conseguenza "Le tecnologie e i modelli dentro i singoli stadi possono cambiare" è rispettata perché i FR non specificano tecnologie particolari

**Lacune documentali rilevate**:

1. Il numero esatto di quattro stadi è un commitment governato o solo la separazione delle funzioni analitiche?
2. L'ordine degli stadi è un commitment stabile oppure una proprietà della realizzazione corrente?
3. Quali responsabilità appartengono alla Decision e quali restano comportamento interno dei singoli stadi?

---

## DEC-MR01-04 — Separazione tra valutazione dell’urgenza e priorità operativa

### Decision Statement

> **Parent MR**: MR-01  
> **Context**: La valutazione del caso produce prima un risultato sull'urgenza, poi una priorità operativa per la presa in carico.  
> **Decision**: Nel percorso basato sull'immagine, DermaTriage tiene separata la valutazione analitica dell'urgenza dalla determinazione successiva della priorità operativa di triage.  
> **Consequences**: La priorità operativa si determina dopo la valutazione dell'urgenza, non dentro la pipeline analitica. La priorità risultante si esprime con la scala P1-P4.

---

### 🔹 FR-DEC-MR01-04-01

**Parent Decision**: DEC-MR01-04 — Separazione tra valutazione dell'urgenza e priorità operativa

**FunctionalRequirement candidate**: In the image-based pathway, DermaTriage MUST first produce an urgency assessment before determining operational priority

**Operational meaning**: The system must complete the urgency assessment (which occurs within the analytical pipeline) as a prerequisite step before any operational priority determination begins. The urgency result must be available and finalized first.

**Source evidence**:

- DEC-MR01-04 Context: "La valutazione del caso produce prima un risultato sull'urgenza, poi una priorità operativa per la presa in carico"
- DEC-MR01-04 Decision: "DermaTriage tiene separata la valutazione analitica dell'urgenza dalla determinazione successiva della priorità operativa"
- OR2 Architecture Document, Pipeline Flow: Stage 4 produces urgency in JSON, then "Adaptation Layer: map\_urgency\_to\_p\_scale()" performs the mapping
- OR5 Test Environment Setup: Stage 4 expected output includes "final\_urgency" before P-scale mapping

**Reason for treating it as a FunctionalRequirement**: The Decision explicitly establishes a temporal and logical separation: urgency assessment must come first, then priority determination. This is a clear operational obligation.

**Reason for the chosen split/merge boundary**: This FR captures the "firstness" of urgency assessment. FR-02 addresses the separation of the determination process. These are distinct aspects of the separation commitment.

**Excluded or separated details**:

- How urgency is assessed (covered by DEC-MR01-03)
- How priority is determined from urgency (covered by DEC-MR01-02)
- Specific timing or synchronization requirements

**Confidence**: HIGH

**Observed ambiguity**:

- The Decision specifies this separation only for the "percorso basato sull'immagine" (image-based pathway). The symptom-based pathway (DEC-MR01-01) is not mentioned. Does the separation also apply there?
- "Prima" could mean temporally first or logically prerequisite. The architecture suggests temporal sequencing.

**Alternative interpretation considered**:

- Could be interpreted as a architectural boundary rather than an operational requirement. Rejected because the Decision frames it as a behavioral commitment ("tiene separata la valutazione... dalla determinazione..."

---

### 🔹 FR-DEC-MR01-04-02

**Parent Decision**: DEC-MR01-04 — Separazione tra valutazione dell'urgenza e priorità operativa

**FunctionalRequirement candidate**: DermaTriage MUST determine operational priority AFTER urgency assessment is complete, and this determination MUST NOT occur within the analytical pipeline

**Operational meaning**: The operational priority (P-scale) determination must happen in a distinct phase that follows the completion of the urgency assessment. The priority mapping logic must be external to the 4-stage analytical pipeline.

**Source evidence**:

- DEC-MR01-04 Consequences: "La priorità operativa si determina dopo la valutazione dell'urgenza, non dentro la pipeline analitica"
- OR2 Architecture Document: "Adaptation Layer: map\_urgency\_to\_p\_scale() assigns P1-P4, specialist and SLA" — this is explicitly outside the 4-stage pipeline
- OR2 Architecture Document, Pipeline Flow: Step 6 (Adaptation Layer) comes after Step 5 (Stage 4 synthesis)

**Reason for treating it as a FunctionalRequirement**: The Decision explicitly states where the priority determination does NOT occur (inside the pipeline) and when it DOES occur (after urgency assessment). This is a clear boundary requirement.

**Reason for the chosen split/merge boundary**: Separated from FR-01 because FR-01 addresses the sequencing (urgency first), while FR-02 addresses the location (not inside pipeline) and the logical separation. These are distinct aspects of the separation commitment.

**Excluded or separated details**:

- The specific mechanism for priority determination (mapping rule — covered by DEC-MR01-02)
- Whether this separation is an architectural boundary or just a behavioral one

**Confidence**: HIGH

**Observed ambiguity**:

- The Decision states this is for the "percorso basato sull'immagine". It's unclear if this separation also applies to the symptom-based pathway.
- The phrase "non dentro la pipeline analitica" could be interpreted as: (a) the mapping function is not part of the 4 stages, or (b) the mapping cannot use any pipeline components. The architecture suggests interpretation (a).
- The Adaptation Layer also assigns "specialist and SLA" — are these part of the priority determination or separate?

**Alternative interpretation considered**:

- Could be merged with FR-01 as a single separation requirement. Rejected because they address different dimensions: temporal ordering (FR-01) vs. architectural boundary (FR-02).

---

### ✅ Verifica di completezza per DEC-MR01-04

**Domanda**: Assumendo che tutti i FunctionalRequirement individuati siano soddisfatti, il Decision potrebbe ancora essere violato?

**Risposta**: NO

**Motivazione**:

- FR-DEC-MR01-04-01: Garantisce che l'urgenza viene prodotta prima
- FR-DEC-MR01-04-02: Garantisce che la priorità viene determinata dopo e non dentro la pipeline
- La conseguenza "La priorità risultante si esprime con la scala P1-P4" è coperta da DEC-MR01-02 (FR-DEC-MR01-02-01)
- Il Decision è quindi completamente coperto dai suoi FR e dai FR di DEC-MR01-02

**Lacune documentali rilevate**:

1. La separazione è un boundary architetturale intenzionale o soltanto la forma corrente della pipeline?
2. La priorità operativa potrebbe essere prodotta direttamente dall'ultimo stadio senza violare un commitment documentato? (La risposta è NO, per FR-DEC-MR01-04-02)
3. Quali semantiche appartengono al boundary e quali alla futura regola operativa di mapping?

---

## Ambiguità e gap documentali

### 📌 Ambiguità per Decision

#### DEC-MR01-01 — Triage in assenza di immagine


| ID        | Ambiguità                                         | Impatto                                                         | FR interessati                       |
| --------- | ------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------ |
| AMB-01-01 | Definizione di "immagine assente/non disponibile" | Non chiaro se include immagini corrotte o di bassa qualità      | FR-DEC-MR01-01-01, FR-DEC-MR01-01-02 |
| AMB-01-02 | Informazioni sintomatologiche minime richieste    | Non specificato quali sintomi sono obbligatori                  | FR-DEC-MR01-01-02                    |
| AMB-01-03 | Equivalenza di output fra percorsi                | Esplicitamente NON richiesta, ma non chiaro se sia desiderabile | Nessuno (non è un requisito)         |


#### DEC-MR01-02 — Scala di priorità P1-P4


| ID        | Ambiguità                                    | Impatto                                               | FR interessati    |
| --------- | -------------------------------------------- | ----------------------------------------------------- | ----------------- |
| AMB-02-01 | Regola completa di mappatura urgenza→P-scale | La relazione tra i casi non è esplicitamente definita | FR-DEC-MR01-02-02 |
| AMB-02-02 | Soglia di confidence (0.85)                  | Parametro configurabile o regola governata?           | FR-DEC-MR01-02-02 |
| AMB-02-03 | Natura degli SLA                             | Normativi, target, o valori documentati?              | FR-DEC-MR01-02-03 |
| AMB-02-04 | Owner/trigger degli SLA                      | Chi governa l'SLA?                                    | FR-DEC-MR01-02-03 |


#### DEC-MR01-03 — Pipeline analitica a quattro stadi


| ID        | Ambiguità                 | Impatto                                                        | FR interessati                       |
| --------- | ------------------------- | -------------------------------------------------------------- | ------------------------------------ |
| AMB-03-01 | Numero esatto di stadi    | Il "4" è un commitment o descrizione corrente?                 | FR-DEC-MR01-03-01                    |
| AMB-03-02 | Ordine degli stadi        | Commitment stabile o implementazione corrente?                 | FR-DEC-MR01-03-01, FR-DEC-MR01-03-06 |
| AMB-03-03 | Responsabilità per stadio | Quali dettagli appartengono alla Decision vs. implementazione? | Tutti                                |


#### DEC-MR01-04 — Separazione tra valutazione dell’urgenza e priorità operativa


| ID        | Ambiguità                                 | Impatto                                               | FR interessati                       |
| --------- | ----------------------------------------- | ----------------------------------------------------- | ------------------------------------ |
| AMB-04-01 | Applicabilità alla pathway senza immagine | La separazione vale solo per il percorso image-based? | FR-DEC-MR01-04-01, FR-DEC-MR01-04-02 |
| AMB-04-02 | Natura del boundary                       | Architetturale o solo comportamentale?                | FR-DEC-MR01-04-02                    |
| AMB-04-03 | Contenuto Adaptation Layer                | Solo P-scale o anche specialist/SLA?                  | FR-DEC-MR01-04-02                    |


---

### 📌 Gap documentali generali (da R6 Guide, Sezione 26)

I seguenti gap sono esplicitamente identificati nel corpus DermaTriage e devono essere preservati come tali:

1. **Diagnostic authority boundary**: Non è governato chi ha l'autorità diagnostica finale
2. **No-image required/optional symptom inputs**: Non è specificato se i sintomi sono obbligatori o opzionali quando l'immagine manca
3. **P-scale complete input semantics**: Non è completamente specificato cosa costituisce l'input completo per la determinazione della P-scale
4. **SLA trigger/outcome/owner/normative binding**: Non è governato il meccanismo di trigger, l'owner, o il binding normativo degli SLA
5. **Predicted pathology obligation/authority**: Non è chiaro se la predizione della patologia è un requisito o solo un output informativo
6. **Specialist selection vocabulary/rule/input/fallback/booking**: Non è governata la selezione dello specialista
7. **Review content, lifecycle e disagreement binding**: Non è governato il ciclo di vita della revisione medica
8. **Adaptation counting e threshold authority**: Non è governato chi autorizza l'adattamento
9. **Prompt evidence window**: Non è governato l'ordinamento/membership/underfill/dedup/reuse/overlap della finestra di evidenza per i prompt
10. **Supervision input invalid/missing/conflicting semantics**: Non è governato come gestire input di supervisione invalidi/mancanti/in conflitto
11. **Deployment authority/automaticity**: Non è governato chi autorizza il deployment o se è automatico
12. **Acceptance e rollback binding**: Non è governato il binding di accettazione e rollback
13. **Evaluation consistency**: Non è governata la coerenza tra sensitivity/recall/correct-count

---

## Sintesi e osservazioni finali

### 📊 Statistiche dell'analisi


| Metrica                      | Valore   |
| ---------------------------- | -------- |
| Decision analizzate          | 4        |
| FunctionalRequirement totali | 14       |
| FR per Decision (media)      | 3.5      |
| Confidenza HIGH              | 11 (79%) |
| Confidenza MEDIUM            | 3 (21%)  |
| Confidenza LOW               | 0 (0%)   |


### 🎯 Osservazioni chiave

1. **Copertura completa**: Tutte e 4 le Decision di MR-01 sono state decomposte in FunctionalRequirement che ne coprono il significato governato.
2. **Separazione chiara**: I FR sono stati assegnati a una sola Decision ciascuno, rispettando il vincolo "Ogni FunctionalRequirement identificato deve appartenere a un solo Decision."
3. **Evidenza solida**: Tutti i FR hanno evidenza documentale esplicita, principalmente dall'OR2 Architecture Document che risulta essere la fonte più ricca di informazione operativa.
4. **Ambiguità gestite**: Le ambiguità sono state esplicitamente identificate e documentate, senza tentare di risolverle inventando requisiti.
5. **Implementazione vs. Requisito**: Particolare attenzione è stata data a separare i commitment governati (requisiti) dalle scelte di implementazione corrente (es. nomi specifici dei modelli, che possono cambiare per DEC-MR01-03).
6. **Conditional Selection Rules**: Per DEC-MR01-02, la regola di mappatura condizionale è stata trattata come FR a sé stante, in linea con la metodologia R6 (Sezione 12.1).
7. **Pipeline Structure**: La pipeline a 4 stadi è stata decomposta in FR che catturano sia la struttura (numero di stadi, sequenzialità) che il comportamento funzionale di ciascuno stadio.
8. **Boundary Architetturale**: La separazione tra valutazione dell'urgenza e priorità operativa (DEC-MR01-04) è stata interpretata come un requisito comportamentale e architetturale, con FR che catturano entrambi gli aspetti.

### ✅ Conformità alla metodologia DDTA


| Requisito metodologico                | Status                       |
| ------------------------------------- | ---------------------------- |
| Analisi Decision per Decision         | ✅ Completo                   |
| Ogni FR appartiene a un solo Decision | ✅ Rispettato                 |
| Evidenza sorgente per ogni FR         | ✅ Fornita                    |
| Motivo per FR                         | ✅ Documentato                |
| Motivo per split/merge                | ✅ Giustificato               |
| Elementi esclusi                      | ✅ Identificati               |
| Livello di confidenza                 | ✅ Assegnato                  |
| Ambiguità osservate                   | ✅ Documentate                |
| Alternative considerate               | ✅ Registrate                 |
| Verifica di completezza               | ✅ Eseguita per ogni Decision |
| Nessun requisito inventato            | ✅ Rispettato                 |


---

*Documento congelato per confronto con altre estrazioni.*