# DDTA R25 - DermaTriage MR-01 Decision / Guide Pressure Ledger TEMP R1

**Status:** TEMPORARY / NON-NORMATIVE / RESEARCH WORKING NOTE
**Scope:** MR-01 Decision-family co-review
**Repository baseline at creation:** `f003c0e669820d61f8bef16fcfc7ac22a110cb93`
**Frozen case-study input:** `DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R3_MR`
**Current cumulative guide experiment:** `DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R4`
**Historical Decision-method references:** R5/R6 only as genealogy and comparison material
**Deletion contract:** DELETE FROM ACTIVE REPOSITORY after accepted content is consolidated into the next cumulative guide revision and/or permanent case-study checkpoint and that consolidation is reviewed. Git history remains the audit trail.

## 1. Why this file exists

This file prevents Decision-phase reasoning from being lost between chat sessions without forcing a methodology-guide revision after every micro-step.

It is not:

- project authority;
- methodology authority;
- a replacement for the frozen MR case study;
- a new DDTA metamodel artifact;
- a canonical Decision registry.

It temporarily records:

- source-first candidate Decision analysis;
- joint human/assistant dispositions;
- unresolved downstream pressures;
- candidate guide refinements;
- candidate cleanup to frozen MR wording that must not be applied silently.

## 2. Review protocol used in this ledger

For every candidate Decision:

```text
1. Current MR text
2. Original source evidence
3. Candidate Decision
4. Why Decision rather than MR / FR / realization
5. Pressure on current MR wording
6. Downstream pressure
7. Joint disposition
8. Candidate guide delta
```

No guide change is applied until the full MR-01 Decision family has been reviewed.

## 3. Frozen MR-01 text entering Decision analysis

Source artifact:

`validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R3_MR.tex`

### MR-01 — Valutazione di triage del caso dermatologico

**Intent**

Determinare, a partire dalle informazioni disponibili sul caso dermatologico, l'urgenza del caso e la relativa priorità operativa di triage.

**Context**

La valutazione di triage parte dalle informazioni disponibili sul caso. Quando non è presente un'immagine della lesione, il progetto prevede un percorso basato sui sintomi disponibili.

**Stakeholders**

Paziente.

**Scope**

**IN:** determinazione dell'urgenza del caso e della relativa priorità operativa di triage, anche quando l'immagine non è presente.

**OUT:** indicazione della destinazione specialistica; validazione o correzione medica dell'esito; adattamento successivo del comportamento del sistema sulla base della revisione clinica.

**Assumptions / Constraints**

--

**dependsOn**

`None`

### Initial observation

The second sentence of Context and the phrase “anche quando l'immagine non è presente” in Scope appear to contain a downstream project commitment rather than only the identity/boundary of the macro responsibility.

This is not corrected in the frozen artifact yet. It is a Decision-phase pressure to be resolved explicitly.

## 4. CDEC-01-01 — Continuità della valutazione di triage in assenza di immagine

### 4.1 Original project-documentation evidence

Primary source:

`OR2_Architecture_Document.pdf`

Relevant source meaning:

- the normal image-based path is described as a sequential four-stage AI pipeline;
- OR2 separately specifies a fallback when no image is available;
- in that fallback, urgency is derived through symptom-only scoring from available B4/chatbot symptom information.

Minimum source-supported proposition:

```text
image unavailable
    ->
triage/urgency evaluation can continue
    ->
available symptom information is used
```

Important non-inferences:

- the observed symptom examples do not establish a universal closed symptom vocabulary;
- the source does not, by this statement alone, define every operational rule of symptom scoring;
- the source does not require the no-image Decision to own the image-based processing path.

### 4.2 Candidate Decision formulation

**Working title**

Continuità della valutazione di triage in assenza di immagine

**Context**

Il caso dermatologico può disporre o meno di un'immagine della lesione. La disponibilità dell'immagine determina quali evidenze possono essere utilizzate nella valutazione, ma la documentazione prevede anche un percorso basato sulle informazioni sintomatologiche quando l'immagine non è disponibile.

**Decision**

DermaTriage mantiene disponibile la valutazione di triage anche in assenza di un'immagine della lesione, utilizzando le informazioni sintomatologiche disponibili sul caso.

**Consequences**

L'immagine non costituisce una precondizione necessaria per l'esistenza della valutazione di triage. Il comportamento operativo necessario a determinare l'urgenza nel percorso senza immagine dovrà essere specificato downstream senza assumere un vocabolario dei sintomi più ampio di quello sostenuto dalla documentazione.

### 4.3 Why this is a Decision rather than part of MR-01

Joint conclusion:

The commitment can change while the macro responsibility remains stable.

Alternative projects could retain the same MR-01 responsibility — evaluate dermatological urgency/priority — while adopting materially different policies such as:

```text
no image -> no triage result
```

or:

```text
no image -> request/acquire image before evaluation
```

or the source-supported policy:

```text
no image -> continue from symptom information
```

Therefore:

```text
MR identity:
evaluate dermatological urgency / operational priority

Decision:
what the project does when image evidence is absent
```

The no-image policy narrows the MR; it does not define the existence of the MR.

### 4.4 Joint disposition

```text
CDEC-01-01
JOINT REVIEW:
ACCEPT AS DECISION CANDIDATE
```

Meaning of this disposition:

- accepted as belonging at Decision level for continued family analysis;
- wording may still be refined during MR-01 family closure;
- no canonical `DEC-*` ID is assigned yet;
- the frozen MR artifact is not modified yet;
- no FR is authored yet.

## 5. Candidate cleanup pressure on MR-01

### GP-MR01-DEC-01 — MR prose pre-encodes a downstream commitment

Observed issue:

Current MR Context states:

> Quando non è presente un'immagine della lesione, il progetto prevede un percorso basato sui sintomi disponibili.

Current Scope also states that urgency/priority is determined “anche quando l'immagine non è presente”.

If CDEC-01-01 is confirmed during family closure, those phrases duplicate or anticipate the Decision.

Candidate cleanup direction, NOT YET APPLIED:

**Intent** may remain substantially unchanged.

**Context** should describe the project/problem context and variability of available case information without already choosing the no-image response.

A possible later wording is:

> La valutazione di triage utilizza le informazioni disponibili sul caso dermatologico. La disponibilità e la tipologia delle evidenze possono variare tra i casi.

**Scope** should preserve ownership of urgency/priority evaluation without embedding the selected fallback policy.

A possible later wording is:

> IN: determinazione dell'urgenza del caso e della relativa priorità operativa di triage a partire dalle informazioni di caso governate dal progetto.

These are working candidates only. Final MR cleanup occurs only through an explicit Decision↔MR review / successor case-study revision.

## 6. Open downstream pressure — image vs no-image FR topology

### GP-MR01-FR-01 — Decision-local branch versus complete triage descendant structure

Human observation:

After accepting the no-image commitment as a Decision, it is not yet obvious how FunctionalRequirements for the image case and the no-image case should be parented.

This is intentionally left unresolved.

Core question:

```text
Does CDEC-01-01 own only the no-image branch,
while image-based FRs descend from sibling Decision(s),
or does the Decision wording imply a broader parentage than intended?
```

Working hypotheses to test later:

1. CDEC-01-01 should probably govern only the no-image fallback commitment.
2. Image-based obligations may belong below a distinct pipeline/architecture Decision family.
3. A conditional Decision does not necessarily own the complementary/default branch.
4. FR structure must not force us to broaden CDEC-01-01 merely for tree symmetry.
5. Conversely, if no descendant FR can express the operational meaning needed to satisfy CDEC-01-01, the Decision may be too vague.
6. During FR completeness analysis, ask:

```text
Can every current descendant FR pass while CDEC-01-01 is still violated?
```

If yes, descendant coverage is incomplete.

7. If the later FR analysis exposes a real hierarchy failure, reopen the Decision explicitly; do not silently move behavior across parents.

### Status

```text
OPEN PRESSURE
DEFER RESOLUTION UNTIL FR ANALYSIS
BUT PRESERVE AS INPUT TO MR-01 DECISION-FAMILY CLOSURE
```

This pressure may require new guide wording on:

- Decision-local conditional scope;
- complementary paths;
- sibling Decisions;
- descendant completeness;
- when FR pressure legitimately reopens a Decision.

## 7. Guide-change candidate ledger

No change below is normative until MR-01 Decision-family closure.

### GDEC-01 — MR Context must not silently contain an independently variable Decision

**Status:** supported candidate refinement.

Possible future guide rule:

> When MR prose contains both a condition and a chosen project response, test whether the response could change while the macro responsibility remains stable. If yes, retain only the macro context/boundary at MR level and route the chosen response to Decision review.

Important qualification:

The MR may still mention variability that is genuinely part of its context. The rule is not “remove all conditions from MR”; it is “do not encode an independently variable downstream commitment as if it defined the MR”.

### GDEC-02 — Decision-local conditional scope and descendant completeness

**Status:** open pressure; do not promote yet.

Need to determine from later FR analysis whether the guide should say explicitly that:

- a Decision may govern one conditional branch without owning every complementary branch;
- sibling Decisions can govern other strategies/paths under the same MR;
- FR completeness is evaluated against the Decision's actual semantic scope, not tree symmetry;
- descendant failure can reopen Decision wording only through an explicit controlled review.

### GDEC-03 — Guide revision cadence during empirical reconstruction

**Status:** process rule accepted for current research workflow.

During one MR Decision-family review:

- preserve the current R7 guide revision;
- accumulate candidate changes here;
- finish the Decision family;
- review pressures jointly;
- create the minimum cumulative guide successor only then;
- regression-test it;
- delete this temporary ledger only after successful consolidation.

This is a research-process discipline and does not automatically require a new L1 construct.

## 8. CDEC-01-02 — Adozione della P-scale P1-P4 come priorità operativa

### 8.1 Original project-documentation evidence

Primary source:

`OR2_Architecture_Document.pdf`

OR2 documents an Adaptation Layer in which `map_urgency_to_p_scale()` assigns P1-P4 together with specialist and SLA information. The documented mapping is:

```text
HIGH + confidence > 0.85 -> P1 -> 24 hours
HIGH                     -> P2 -> 48 hours
MEDIUM                   -> P3 -> 72 hours
LOW                      -> P4 -> 7 giorni
```

Minimum source-supported meanings must be kept distinct:

```text
A. MR-01 requires an operational priority.
B. The project represents that priority in the P1-P4 domain.
C. A conditional operational rule selects P1/P2/P3/P4.
D. Source evidence also associates SLA values with those levels.
```

### 8.2 Candidate Decision formulation

**Working title**

Adozione della P-scale per la priorità operativa

**Context**

La valutazione di urgenza deve essere resa utilizzabile come priorità operativa di triage. La documentazione DermaTriage rappresenta tale priorità mediante quattro livelli P1-P4.

**Decision**

DermaTriage rappresenta la priorità operativa di triage mediante la scala P1-P4.

**Consequences**

Gli obblighi downstream che producono una priorità operativa devono produrre un valore appartenente al dominio P1-P4. Le condizioni che determinano quale livello P1-P4 debba essere prodotto non fanno parte dell'identità di questa Decision e devono essere governate al livello operativo appropriato.

### 8.3 Why this is a Decision

MR-01 requires an operational priority but does not prescribe the vocabulary used to represent it.

The project could retain the same macro responsibility while selecting a materially different priority convention.

Therefore:

```text
MR-01:
an operational triage priority must exist

CDEC-01-02:
the project represents it as P1-P4
```

The P1-P4 convention can change without eliminating or replacing the macro responsibility.

### 8.4 Mapping boundary

Joint conclusion:

```text
KEEP IN DECISION
P1-P4 is the selected operational-priority domain.

ROUTE DOWNSTREAM
urgency/confidence -> P1/P2/P3/P4 mapping.

PRESERVE AS SEPARATE OPEN MEANING
24h / 48h / 72h / 7 giorni SLA semantics.
```

The exact mapping can change while the Decision to use P1-P4 remains stable. It is therefore not part of the identity of CDEC-01-02.

### 8.5 Open analytical questions

```text
QUESTIONI APERTE EMERSE DALLA RICOSTRUZIONE
NON NORMATIVE

- L'urgenza prodotta dal percorso symptom-only entra nella stessa
  regola P1-P4 usata dal percorso image-based?

- Qual è il significato normativo dei valori
  24h / 48h / 72h / 7 giorni associati alla P-scale?

- Da quale evento decorre l'eventuale tempo SLA e quale attore
  possiede la responsabilità del suo rispetto?
```

These questions are analysis output, not Decision semantics.

### 8.6 Joint disposition

```text
CDEC-01-02
JOINT REVIEW:
ACCEPT AS DECISION CANDIDATE
```

No MR cleanup is currently required specifically for this Decision: MR-01 owns the existence of an operational priority without pre-encoding the P1-P4 vocabulary.

## 9. CDEC-01-03 — Pipeline image-based sequenziale a quattro stadi

### 9.1 Original project-documentation evidence

Primary source:

`OR2_Architecture_Document.pdf`

OR2 documents the image-based flow as four sequential analytical stages:

```text
Stage 1 -> image urgency classification
Stage 2 -> image-derived clinical description
Stage 3 -> retrieval of similar historical cases
Stage 4 -> multi-source synthesis using prior stage outputs + symptoms
```

The four-stage flow is followed by the Adaptation Layer that assigns operational P-scale information.

### 9.2 Candidate Decision formulation

**Working title**

Composizione sequenziale della valutazione image-based a quattro stadi

**Context**

Quando è disponibile un'immagine della lesione, la documentazione non descrive la valutazione di triage come il risultato diretto di un singolo passaggio analitico. Il percorso image-based costruisce contributi analitici distinti che vengono progressivamente combinati.

**Decision**

DermaTriage costruisce la valutazione image-based mediante una pipeline sequenziale a quattro stadi analitici, nella quale i risultati intermedi contribuiscono alla successiva sintesi di triage.

**Consequences**

Il percorso image-based deve preservare quattro ruoli analitici distinguibili e la loro composizione sequenziale. Le tecnologie correnti usate per realizzare tali ruoli non definiscono automaticamente l'identità della Decision.

### 9.3 Why "four stages" remains in the Decision

Joint conclusion:

The number and semantic decomposition of the stages are part of the current governed architectural strategy.

A future redesign that merges, removes or adds stages may materially change this Decision and should reopen it explicitly rather than abstracting the current commitment away.

The Decision is therefore intentionally more concrete than a generic statement such as "use multiple analytical contributions".

### 9.4 Current FR hypothesis

The current hypothesis for later FR analysis is:

```text
CDEC-01-03
Pipeline image-based sequenziale a quattro stadi

    -> candidate FR: produrre la classificazione di urgenza dall'immagine
    -> candidate FR: produrre la descrizione clinica image-derived
    -> candidate FR: recuperare casi storici simili
    -> candidate FR: produrre la sintesi di triage multi-source
```

This is not an FR promotion yet.

It records the expected ownership pressure to be tested when the FunctionalRequirement phase begins.

### 9.5 Relationship with the no-image branch

Joint interpretation:

```text
CDEC-01-01
owns the no-image fallback commitment

CDEC-01-03
owns the image-present four-stage analytical path

CDEC-01-02
owns the P1-P4 representation of operational priority
```

This resolves the earlier hypothesis that CDEC-01-01 might need to own the complete triage path. It does not.

What remains open is the explicit semantic binding from symptom-only urgency to the P-scale mapping.

### 9.6 Open analytical questions

```text
QUESTIONI APERTE EMERSE DALLA RICOSTRUZIONE
NON NORMATIVE

- Ogni stadio giustifica effettivamente un FunctionalRequirement
  autonomo quando verranno eseguiti i gate FR?

- Quale comportamento è governato quando uno stadio intermedio
  non produce il proprio risultato?

- EfficientNet-B4, Qwen2-VL, ChromaDB e BioMistral rappresentano
  scelte progettuali autonome o soltanto realization bindings
  dei quattro ruoli funzionali?
```

The previously open question "four stages or generic multi-stage?" is considered resolved for the current candidate: **four stages belongs to the Decision**.

### 9.7 Joint disposition

```text
CDEC-01-03
JOINT REVIEW:
ACCEPT AS DECISION CANDIDATE
```

## 10. Additional MR-01 pressures exposed by CDEC-01-02 / CDEC-01-03

### GP-MR01-PMAP-01 — symptom-only urgency to P-scale binding

**Status:** OPEN / NOT YET ESTABLISHED.

OR2 documents both the P-scale mapping and a symptom-only urgency fallback, but the current review must not infer without evidence that symptom-only urgency necessarily traverses the exact same P-scale transformation.

Question for later source/FR review:

> Is the symptom-only urgency result explicitly governed as input to the same P1-P4 mapping used by the image-based path?

### GP-MR01-FR-02 — image-present vs image-absent descendant ownership

Current working structure:

```text
MR-01
 |
 +-- CDEC-01-01 no-image fallback
 |      -> future no-image FR family
 |
 +-- CDEC-01-03 image-based four-stage pipeline
 |      -> future image-based FR family
 |
 +-- CDEC-01-02 P1-P4 representation
        -> future mapping FR candidate
```

This is a semantic-ownership hypothesis, not yet a promoted FR tree.

### GP-MR01-OWN-01 — single-parent pressure

A future FR MUST NOT be made child of more than one Decision merely because multiple Decisions are relevant to the same runtime path.

If the same candidate FR appears to require two Decision parents, review:

1. which Decision semantically owns the obligation;
2. whether one Decision is too broad or too narrow;
3. whether one candidate meaning is only a realization binding;
4. whether the FR itself contains more than one coherent obligation and needs split.

### GP-MR01-REAL-01 — completed technology-binding classification for Stages 1-4

**Status:** REVIEWED / RESULTS PRESERVED.

The four current technology bindings were reviewed using the same source-first Decision-vs-realization gate.

```text
Stage 1
functional role:
image -> urgency classification + confidence

current binding:
EfficientNet-B4

disposition:
REALIZATION
NO STANDALONE DECISION
```

The source establishes EfficientNet-B4 as the current Stage-1 classifier and technology-stack component. Replacing it while preserving the Stage-1 functional behavior and CDEC-01-03 does not, on current evidence, necessarily change an independently governed project commitment.

Open sub-pressure:

```text
CNN as architectural class
-> independent Decision status NOT ESTABLISHED
```

```text
Stage 2
functional role:
image -> clinical textual description

current binding:
Qwen2-VL-7B-Instruct

disposition:
REALIZATION
NO STANDALONE DECISION
```

The current source also describes the implementation class as a Vision LLM and the output as a five-bullet clinical description.

Open sub-pressures:

```text
Vision LLM as architectural class
-> independent Decision status NOT ESTABLISHED

5-bullet format
-> SOURCE-SUPPORTED BINDING
-> governed FR/configuration status NOT YET ESTABLISHED
```

```text
Stage 3
functional role:
ClinicalDescription -> HistoricalCaseContext

current bindings:
ChromaDB
sentence-transformers/all-MiniLM-L6-v2
cosine similarity
top-5

classification:
ChromaDB -> REALIZATION
all-MiniLM-L6-v2 -> REALIZATION
cosine similarity -> LOWER-LEVEL / BINDING, status to be tested
top-5 -> LOWER-LEVEL / PARAMETER BINDING, status to be tested
```

Neutralizing the concrete products leaves a project choice that can vary while the Stage-3 functional outcome remains stable:

```text
retrieve historical cases
using vector-similarity retrieval
```

This surviving meaning is routed to a derived Decision candidate recorded as `CDEC-01-04A`.

```text
Stage 4
functional role:
Stage 1 + Stage 2 + Stage 3 + symptoms
    ->
multi-source triage synthesis

current binding:
BioMistral-7B

disposition:
REALIZATION
NO STANDALONE DECISION
```

The source describes BioMistral-7B as the current Medical LLM. The evidence does not currently establish "Medical LLM" as an independent architectural Decision.

Open sub-pressures:

```text
Medical LLM as architectural class
-> independent Decision status NOT ESTABLISHED

JSON output representation
-> SOURCE-SUPPORTED BINDING
-> governed FR/configuration status NOT YET ESTABLISHED
```

The source-supported Stage-4 output meanings include urgency, confidence, reasoning and pathology. Their exact required set and the semantic authority of pathology remain FR/downstream review questions.

### GP-MR01-BIND-01 — source-supported bindings remain visible without automatic Decision promotion

**Status:** SUPPORTED PRESSURE.

The review produced a repeated pattern:

```text
source explicitly names technical detail
        !=
detail is automatically a Decision
```

Examples preserved for later classification:

- Stage-1 threshold and model-specific details;
- Stage-2 five-bullet format;
- Stage-3 cosine similarity and top-5;
- Stage-4 JSON representation and exact output-field contract.

These meanings must remain visible in reconstructed documentation even when their stable normative level is not yet established.

## 11. Guide-change candidates added by the new review

### GDEC-04 — Open analytical questions as a non-normative presentation view

**Status:** supported L2 presentation candidate; do not promote to L1.

The DermaTriage analytical documentation should be able to show unresolved questions immediately below the DDTA element that exposed them, using a visually subordinate grey box such as:

```text
QUESTIONI APERTE EMERSE DALLA RICOSTRUZIONE
NON NORMATIVE
```

The box is not part of the normative semantics of the Decision, does not create a new metamodel field and MUST distinguish at least:

- governed meaning;
- checked but `NOT SPECIFIED` / open question;
- not yet analyzed.

Research purpose:

The analytical documentation should make visible not only what DDTA can govern, but also which material questions become observable because the documentation has been decomposed semantically.

### GDEC-05 — Architecture Decision versus stage FunctionalRequirement

**Status:** supported candidate refinement; validate again during FR analysis.

Working distinction:

- the Decision governs the structural/project commitment that the image-based path is composed of four sequential analytical stages;
- each stage's observable required behavior is a candidate FunctionalRequirement;
- changing the number or semantic role of the stages can reopen the Decision;
- changing the required behavior of one stage can reopen the corresponding FR.

### GDEC-06 — Single semantic parent / no Decision-FR multi-parent shortcut

**Status:** strong hierarchy pressure.

If two candidate Decisions appear to own the same future FunctionalRequirement, do not solve the conflict by assigning two Decision parents and do not place a Decision below an FR.

Required review:

```text
same FR appears owned by Decision A and Decision B
        ->
review semantic owner
        ->
review Decision granularity
        ->
review whether one candidate is only realization/configuration
        ->
KEEP one semantic parent or explicitly restructure the Decision family
```

This preserves the regular DDTA hierarchy:

```text
MR
  -> Decision
      -> FR
```

### GDEC-07 — Technology names are realization by default, not automatic Decisions

**Status:** supported candidate refinement after the Stage 1-4 technology-binding review.

For `EfficientNet-B4`, `Qwen2-VL`, `ChromaDB` and `BioMistral`, the default hypothesis is current realization evidence.

A technology binding may be promoted to Decision only if source evidence supports an independently governed architectural/project commitment that remains meaningful after neutralizing the product/model name.

The review question is:

> If this technology is replaced while the four-stage Decision and the stage's required behavior remain unchanged, has a governed project commitment changed or only its realization?

A technology is not promoted merely because it is concrete, named, technically important or source-supported.

### GDEC-08 — Neutralization may expose a Decision behind a technology bundle

**Status:** supported candidate refinement.

A technology bundle must not be classified only at the product-name level.

Required test:

```text
remove concrete product/model names
        ->
ask what project strategy remains
        ->
if the remaining strategy can change while the MR and functional outcome stay stable,
route that surviving meaning to Decision review
```

DermaTriage Stage 3 is the current example:

```text
ChromaDB + all-MiniLM-L6-v2
        -> realization

vector-similarity retrieval
        -> derived Decision candidate
```

This prevents both Decision inflation from product names and Decision loss from over-neutralizing meaningful architecture.

### GDEC-09 — A more specific sibling Decision may own a stage FR

**Status:** strong hierarchy pressure; validate during FR authoring.

A broad architecture Decision may establish that a stage exists without necessarily remaining the direct parent of that stage's future FR.

If later Decision review discovers a more specific project commitment that governs the behavior, the future FR may have that more specific Decision as its single semantic parent.

Example hypothesis:

```text
MR-01
 |
 +-- CDEC-01-03
 |     four-stage architecture
 |
 +-- CDEC-01-04A
       vector-similarity retrieval strategy
          |
          `-- future Stage-3 FR
```

The relationship between the Stage-3 FR and CDEC-01-03 remains traceable, but it must not be represented by a second containment parent.

This refines `GDEC-06`: single-parent hierarchy is preserved by reviewing semantic ownership, not by forcing every stage FR to descend directly from the broadest architecture Decision.

## 8. MR-01 provisional Decision inventory

The following list is preserved so subsequent chats do not lose the breadth-first discovery state.

| Working ID | Candidate meaning | State |
|---|---|---|
| `CDEC-01-01` | Continuità del triage in assenza di immagine mediante informazioni sintomatologiche | ACCEPT AS DECISION CANDIDATE |
| `CDEC-01-02` | Adozione della P-scale P1-P4 come priorità operativa | ACCEPT AS DECISION CANDIDATE |
| `CDEC-01-03` | Pipeline AI image-based sequenziale a quattro stadi | ACCEPT AS DECISION CANDIDATE |
| `CDEC-01-04` | Allocazione tecnologica ai singoli stadi | REWORK — uniform technology-allocation Decision did not survive neutralization |
| `CDEC-01-04A` | Recupero dei casi storici mediante similarità vettoriale | ACCEPT AS DECISION CANDIDATE — derived from CDEC-01-04 review |
| `CDEC-01-05` | Coesistenza di un percorso diretto e di un percorso di triage integrato con B4 | ACCEPT AS DECISION CANDIDATE |
| `CDEC-01-06` | Costruzione separata della baseline classificatoria mediante training e validazione | ACCEPT AS DECISION CANDIDATE — reworked to technology-neutral meaning after direct source pass |
| `CDEC-01-07` | Uso di una base dati dermatologica condivisa per retrieval storico e training della baseline | ACCEPT AS DECISION CANDIDATE — previous HOLD resolved by direct OR3 evidence |

No historical `DEC-*` correspondence is asserted here.

## 12. CDEC-01-04 — Review dell'allocazione tecnologica ai quattro stadi

### 12.1 Original candidate

Initial working meaning:

```text
CDEC-01-04
allocazione tecnologica ai singoli stadi
```

The candidate was intentionally not accepted before checking whether the named technologies represented autonomous project commitments or current realization.

### 12.2 Decision-vs-realization gate applied to all four stages

Joint review result:

| Stage | Source-supported current binding | Disposition |
|---|---|---|
| Stage 1 | EfficientNet-B4 | REALIZATION |
| Stage 2 | Qwen2-VL-7B-Instruct | REALIZATION |
| Stage 3 | ChromaDB + all-MiniLM-L6-v2 | REALIZATION |
| Stage 4 | BioMistral-7B | REALIZATION |

The review therefore does **not** support one uniform Decision whose identity is the allocation of those four named technologies.

### 12.3 CDEC-01-04 joint disposition

```text
CDEC-01-04
JOINT REVIEW:
REWORK
```

Reason:

The product/model names do not survive the neutralization gate as a coherent four-part Decision family. They remain source-supported realization evidence.

`REWORK` is used rather than `REJECT AS DECISION` because the review exposed a narrower project strategy inside the Stage-3 bundle that does survive neutralization.

### 12.4 Derived candidate CDEC-01-04A

**Working title**

Recupero dei casi storici mediante similarità vettoriale

**Context**

Lo Stage 3 deve arricchire la sintesi successiva con contesto proveniente da casi dermatologici storici simili. La documentazione corrente realizza questo recupero attraverso una rappresentazione vettoriale dei contenuti clinici e una ricerca di similarità.

**Decision**

DermaTriage costruisce il contesto storico dello Stage 3 recuperando casi dermatologici simili mediante una strategia di ricerca basata su rappresentazioni vettoriali.

**Consequences**

Il comportamento downstream dello Stage 3 deve essere compatibile con una strategia di retrieval per similarità vettoriale. Il prodotto di vector storage, il modello di embedding, la metrica concreta e il numero di risultati non fanno automaticamente parte dell'identità di questa Decision e devono essere governati separatamente se il source review ne stabilisce la stabilità normativa.

### 12.5 Why CDEC-01-04A is a Decision candidate

The following alternatives can preserve both MR-01 and the Stage-3 functional purpose of obtaining similar historical cases:

```text
vector-similarity retrieval
keyword / lexical retrieval
rule-based matching
other retrieval strategy
```

Therefore the retrieval strategy can vary while the macro responsibility and high-level Stage-3 functional outcome remain stable.

This is the material difference that survived technology-name neutralization.

### 12.6 Single-parent consequence for later FR analysis

The current earlier hypothesis:

```text
CDEC-01-03
    -> direct FR for every one of the four stages
```

is no longer assumed universally.

For Stage 3, the candidate ownership becomes:

```text
MR-01
 |
 +-- CDEC-01-03
 |     establishes the four-stage image-based architecture
 |
 +-- CDEC-01-04A
       governs vector-similarity retrieval
          |
          `-- future Stage-3 FR candidate
```

This is not an FR promotion yet.

During FR analysis, Stage 3 must receive one semantic parent. CDEC-01-03 remains a traceable architecture relation, not a second containment parent.

### 12.7 Open analytical questions

```text
QUESTIONI APERTE EMERSE DALLA RICOSTRUZIONE
NON NORMATIVE

Stage 1
- Is CNN an independently governed architectural class or current realization?

Stage 2
- Is Vision LLM an independently governed architectural class?
- Is the five-bullet format a stable output contract or current prompt/format binding?

Stage 3
- Is cosine similarity a stable governed part of the retrieval strategy?
- Is top-5 a stable output requirement or a current parameter?
- Is the embedding model independently governed or realization?
- Which historical-case fields must be returned to Stage 4?

Stage 4
- Is Medical LLM an independently governed architectural class?
- Is JSON a stable output contract or current representation?
- Which synthesis fields are mandatory for the downstream operational mapping?
- What governed meaning, if any, does pathology carry without implying definitive clinical diagnosis?
```

### 12.8 Joint disposition of the derived candidate

```text
CDEC-01-04A
JOINT REVIEW:
ACCEPT AS DECISION CANDIDATE
```

Meaning:

- temporary working ID only;
- no historical/canonical `DEC-*` correspondence asserted;
- no FR authored yet;
- concrete technology bindings remain preserved as realization evidence;
- lower-level binding questions remain open for FR/configuration review.

## 13. CDEC-01-05 — Coesistenza di un percorso diretto e di un percorso di triage integrato con B4

### 13.1 Original project-documentation evidence

Primary source:

`OR2_Architecture_Document.pdf`

OR2 documents two distinct DermaTriage entry paths:

```text
POST /analyze
-> full four-step pipeline
-> direct upload

POST /diagnose
-> B4-integrated pipeline
```

For the integrated path, the source also documents B4 interactions for consultation/case acquisition, document listing and image download, together with write-back of the AI result.

The same source separately documents medical-validation and validated-outcome interactions. Those later interactions are not absorbed into MR-01 merely because they use the same external system: their semantic ownership remains for MR-03 / MR-04 review as appropriate.

Minimum source-supported proposition:

```text
MR-01 triage
    can be entered directly
    OR
    through a B4-integrated workflow
```

Important non-inferences:

- B4 is not a universal precondition for MR-01;
- MR-01 does not gain `dependsOn B4`;
- endpoint names do not define the Decision identity;
- X-API-Key and bearer JWT do not define this Decision;
- medical validation is not owned by MR-01.

### 13.2 Candidate Decision formulation

**Working title**

Coesistenza di un percorso diretto e di un percorso di triage integrato con B4

**Context**

La valutazione di triage può essere avviata direttamente a partire dalle informazioni fornite al servizio oppure nel contesto di un consulto gestito dal sistema esterno B4. La documentazione DermaTriage espone entrambi i percorsi e, nel percorso integrato, prevede lo scambio delle informazioni di caso e dell'esito di triage con B4.

**Decision**

DermaTriage mantiene disponibile la valutazione di triage sia attraverso un percorso diretto sia attraverso un percorso integrato con B4; nel percorso integrato acquisisce da B4 le informazioni di caso necessarie alla valutazione e rende disponibile a B4 l'esito di triage associato al consulto.

**Consequences**

B4 non costituisce una precondizione universale per l'esecuzione di MR-01. Il percorso integrato deve preservare la correlazione tra il caso/consulto B4 e l'esito di triage prodotto. Endpoint, protocolli e meccanismi di autenticazione non appartengono automaticamente all'identità della Decision.

### 13.3 Decision-vs-realization gate

Neutralizing the concrete endpoint names leaves a stable project strategy:

```text
direct triage path
+
B4-integrated triage path
```

The following are therefore preserved separately:

```text
/analyze
/diagnose
specific B4 paths
    -> REALIZATION / INTERFACE BINDING

direct + B4-integrated access strategy
    -> DECISION MEANING
```

The same MR-01 responsibility could exist with direct-only, integrated-only or dual access. The dual-path commitment therefore narrows the MR without defining the MR itself.

### 13.4 Open analytical questions

```text
QUESTIONI APERTE EMERSE DALLA RICOSTRUZIONE
NON NORMATIVE

- I percorsi direct e B4-integrated devono offrire esattamente
  le stesse capacità di triage?

- Il write-back verso B4 è obbligatorio per ogni esecuzione
  del percorso integrato?

- Quali informazioni del consulto B4 costituiscono il minimo
  necessario per il triage?

- La persistenza locale dell'esito è un obbligo di progetto
  o current realization?

- Qual è il comportamento governato se B4 non è raggiungibile
  durante acquisition o write-back?

- La correlazione tra consultation identity e risultato è
  un contratto esplicito dell'integrazione?
```

### 13.5 Joint disposition

```text
CDEC-01-05
JOINT REVIEW:
ACCEPT AS DECISION CANDIDATE
```

No MR-01 cleanup is currently required by this Decision. The current `dependsOn None` remains consistent with the existence of a direct path.

## 14. Direct-source completeness pass for the remaining MR-01 Decision candidates

Before closing CDEC-01-06 and CDEC-01-07, the original source subset was reopened directly.

Human-provided source subset:

```text
OR2_Architecture_Document.pdf
OR2_Model_Test_Report.pdf
OR3_Dataset_Metadata_Catalog.pdf
OR4_Training_Environment_Config.pdf
OR4_Training_Cycles_Report.pdf
OR5_Test_Environment_Setup.pdf
```

The human explicitly confirmed that these are the same original documents from the pinned DermaTriage source package, with non-needed artifacts removed from the transfer subset.

Independent byte-level continuity check available in-session:

```text
OR2_Architecture_Document.pdf
SHA-256
c77238271d05a8ac4b4227143afb1ece783416a8091b31f9d2161e4f85f831de
```

This matches the previously pinned OR2 hash.

Scope rule:

- the subset is used as direct original-document evidence;
- the transfer ZIP itself is not treated as a replacement authority package;
- removal of the binary `.pth` does not change the semantic Decision review because that artifact is realization evidence;
- old DDTA reconstructions remain comparison material, not project authority.

The pass covered all pages of the six retained PDFs and removed the earlier source-completeness hold on the baseline-training and shared-dataset candidates.

## 15. CDEC-01-06 — Costruzione separata della baseline classificatoria mediante training e validazione

### 15.1 Direct original-source evidence

Direct sources:

- `OR2_Model_Test_Report.pdf`;
- `OR4_Training_Cycles_Report.pdf`;
- `OR4_Training_Environment_Config.pdf`;
- corroborating architecture evidence from `OR2_Architecture_Document.pdf`.

The training-cycle source explicitly distinguishes:

```text
Cycle 0 — Initial Training
```

from the later:

```text
Continuous Retraining Protocol
```

The initial baseline evidence includes a training split, validation split and test split, balancing of the training data, early stopping and checkpoint selection using validation evidence. The documented baseline identifies the best checkpoint by validation Macro F1.

The later retraining protocol is driven by accumulated clinician disagreement/correction evidence and belongs to the subsequent adaptation lifecycle rather than to the identity of initial baseline establishment.

Minimum surviving meaning after technology/configuration neutralization:

```text
initial classifier baseline
    is established through a distinct
    training + validation process

selected baseline/checkpoint
    is chosen using validation evidence

later feedback-driven retraining
    is a separate lifecycle process
```

### 15.2 Reworked Decision formulation

The earlier working wording was too closely tied to the current model technology.

**Working title**

Costruzione separata della baseline classificatoria mediante training e validazione

**Context**

Il percorso image-based richiede un classificatore iniziale dell'urgenza prima che possano operare i successivi meccanismi di adattamento basati sulla revisione clinica. La documentazione distingue la costruzione della baseline iniziale dal successivo retraining feedback-driven.

**Decision**

DermaTriage stabilisce la baseline iniziale del classificatore di urgenza mediante un processo di training e validazione distinto dal successivo adattamento basato sulla revisione clinica, utilizzando evidence di validation per selezionare il modello/checkpoint da assumere come baseline operativa.

**Consequences**

La baseline iniziale e il successivo retraining sono lifecycle process distinti. La selezione della baseline usa evidence di validation e non coincide con la valutazione finale sul test set. Modello concreto, algoritmo di balancing, optimizer, scheduler, hyperparameter e valori numerici non fanno automaticamente parte dell'identità della Decision.

### 15.3 Classification of preserved source detail

```text
EfficientNet-B4
ImageNet-pretrained initialization
    -> REALIZATION / CURRENT BINDING

SMOTE
Adam
LinearWarmup
CosineAnnealing
CrossEntropyLoss
AMP
    -> SOURCE-SUPPORTED TRAINING BINDINGS
       stable normative status NOT YET ESTABLISHED

learning rates
batch size
epoch bounds
patience
label smoothing
split sizes
    -> SOURCE-SUPPORTED CONFIGURATION / BINDINGS

observed stop epoch
observed best epoch
    -> OBSERVED TRAINING RESULT
       NOT DECISION IDENTITY

validation-based checkpoint selection
    -> DECISION MEANING

Macro F1
    -> SOURCE-SUPPORTED SELECTION BINDING
       stable normative status NOT YET ESTABLISHED
```

### 15.4 Ownership boundary

```text
MR-01
  -> initial classifier baseline establishment

MR-04
  -> later controlled adaptation/retraining
     from clinician-review evidence
```

The initial-state Decision must not absorb the later feedback-driven adaptation family.

### 15.5 Open analytical questions

```text
QUESTIONI APERTE EMERSE DALLA RICOSTRUZIONE
NON NORMATIVE

- Il balancing del training set è un commitment stabile
  oppure una tecnica corrente?

- Validation Macro F1 è un criterio normativo stabile
  oppure il criterio della baseline corrente?

- Quali condizioni rendono una baseline sufficientemente
  qualificata per l'uso operativo?

- Qual è la relazione tra quality target assoluti della
  baseline e relative replacement gate del retraining?

- Gli split train/validation/test sono governati oppure
  current realization/configuration?

- Una futura ricostruzione completa della baseline resta
  sotto MR-01 oppure entra nel lifecycle di MR-04?
```

### 15.6 Joint disposition

```text
CDEC-01-06
INITIAL WORKING FORM:
REWORK

TECHNOLOGY-NEUTRAL REFORMULATION:
ACCEPT AS DECISION CANDIDATE
```

The same working ID is retained because the original candidate already concerned baseline-training strategy; the review refines its identity rather than discovering an unrelated sibling Decision.

## 16. CDEC-01-07 — Uso di una base dati dermatologica condivisa per retrieval storico e training della baseline

### 16.1 Direct original-source evidence

Primary source:

`OR3_Dataset_Metadata_Catalog.pdf`

The dataset catalog explicitly identifies the DermaTriage RAG Dataset and states its purpose as:

```text
RAG retrieval + CNN training base
```

The same source documents both:

- use in Stage 3 historical-case retrieval;
- processed data used to prepare the classifier training base.

`OR4_Training_Environment_Config.pdf` corroborates the coexistence of the RAG dataset and processed train/validation/test material in the documented training environment.

This direct source pass resolves the previous `HOLD`: the shared-data relationship is not merely inferred by correlating two old DDTA reconstructions.

### 16.2 Neutralization test

Neutralize concrete names and file bindings:

```text
ISIC
RAG_dataset.csv
ChromaDB
all-MiniLM-L6-v2
SMOTE
```

A meaningful project choice remains:

```text
one governed dermatology data lineage
    supports
        Stage-3 historical retrieval
    AND
        Stage-1 baseline training preparation
```

An alternative project could use independent datasets for the two purposes while preserving MR-01 and the stage functional roles. Therefore the shared-data strategy can vary independently from the MR identity.

### 16.3 Candidate Decision formulation

**Working title**

Uso di una base dati dermatologica condivisa per retrieval storico e training della baseline

**Context**

Il retrieval dei casi storici dello Stage 3 e la costruzione iniziale del classificatore dello Stage 1 richiedono evidence dermatologica. La documentazione identifica una stessa base dati di progetto come origine per entrambe le finalità.

**Decision**

DermaTriage utilizza una base dati dermatologica condivisa come origine sia del contesto indicizzato per il retrieval dei casi storici sia dei dati preparati per il training della baseline classificatoria.

**Consequences**

Le due capability condividono una lineage informativa comune, pur utilizzando rappresentazioni e trasformazioni differenti. La specifica sorgente del dataset, i file, il vector store, il modello di embedding e la tecnica concreta di balancing non fanno automaticamente parte dell'identità di questa Decision.

### 16.4 Classification of preserved source detail

```text
shared dataset lineage
    -> DECISION MEANING

ISIC-derived provenance
    -> SOURCE-SUPPORTED DATASET PROVENANCE
       independent Decision status NOT ESTABLISHED

RAG_dataset.csv
processed split filenames
    -> FILE / REALIZATION BINDINGS

image_description indexed field
    -> STAGE-3 DATA BINDING TO CLASSIFY

SMOTE
    -> BASELINE-TRAINING BINDING TO CLASSIFY
```

### 16.5 Joint disposition

```text
CDEC-01-07
PREVIOUS STATE:
HOLD

DIRECT OR3 SOURCE PASS:
HOLD RESOLVED

JOINT REVIEW:
ACCEPT AS DECISION CANDIDATE
```

## 17. Guide-change candidates added by CDEC-01-05 / 01-06 / 01-07

### GDEC-10 — External integration strategy does not automatically create a macro dependency

**Status:** supported candidate refinement.

A consumed external service may participate in one selected workflow without becoming a universal MR dependency.

Required test:

```text
external system appears in one runtime/integration path
        !=
MR dependsOn external system

check whether the MR can still be satisfied
through another documented path
```

If yes, preserve the external integration as downstream Decision/FR meaning and do not promote it to macro `dependsOn` merely from runtime dataflow.

### GDEC-11 — Separate initial-state establishment from later adaptive lifecycle

**Status:** supported candidate refinement.

When source documentation distinguishes an initial baseline-construction process from later feedback-driven adaptation, do not collapse both into one Decision merely because they act on the same model/capability.

Review:

```text
initial establishment evidence
        vs
later adaptation evidence
        ->
test separate lifecycle ownership
```

The two meanings may belong to different Decision families or even different MRs.

### GDEC-12 — Shared data lineage may be a Decision after concrete data technology is neutralized

**Status:** supported candidate refinement.

A dataset name, file path or storage technology is not automatically a Decision. However, after neutralizing those concrete bindings, a project strategy may remain if the same governed data lineage is intentionally reused across materially distinct capabilities.

Required test:

```text
remove dataset/file/product names
        ->
ask whether one shared data lineage still links
multiple capabilities
        ->
if that shared-lineage commitment can vary
while the MR and individual functional outcomes remain stable,
route it to Decision review
```

### GDEC-13 — Direct-source completeness gate before closing source-sensitive Decision candidates

**Status:** research-process candidate.

When a candidate Decision depends materially on evidence from dataset, training, test or configuration documents, old DDTA reconstructions must not substitute for unavailable original source.

Use explicit states:

```text
DIRECT SOURCE CHECKED
DIRECT SOURCE NOT YET AVAILABLE
DERIVED ARTIFACT ONLY
```

Do not convert `DERIVED ARTIFACT ONLY` into project authority.

## 18. MR-01 Decision-family closure is next

The breadth-first discovery pass for the currently identified MR-01 Decision candidates is now complete.

Current working family:

```text
MR-01
 |
 +-- CDEC-01-01  ACCEPT
 +-- CDEC-01-02  ACCEPT
 +-- CDEC-01-03  ACCEPT
 +-- CDEC-01-04  REWORK / genealogy retained
 +-- CDEC-01-04A ACCEPT
 +-- CDEC-01-05  ACCEPT
 +-- CDEC-01-06  REWORK -> ACCEPT
 `-- CDEC-01-07  HOLD -> ACCEPT
```

No FR authoring starts yet.

Next controlled step:

1. review all candidate Decisions together;
2. test overlap, duplication and granularity;
3. test single semantic ownership;
4. re-run neutralization/change tests where useful;
5. execute Decision ↔ MR-01 cross-check;
6. resolve MR cleanup pressure;
7. stabilize the candidate Decision family;
8. only then create the successor DermaTriage documentation view and evaluate cumulative guide consolidation.

## 19. Retirement condition for this file

Do not keep this file as permanent normative documentation.

It is retired when:

1. the MR-01 Decision family has been reviewed;
2. accepted guide pressures have been resolved;
3. the minimum cumulative R7 successor has been created, if required;
4. any necessary permanent Decision/MR checkpoint has been created;
5. regression review passes;
6. the accepted content no longer depends on this temporary note for reconstruction.

At that point remove this file in an explicit repository commit.

Git history is sufficient to preserve the temporary research trail.
