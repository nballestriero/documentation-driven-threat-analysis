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

## 8. CDEC-01-02 â€” Adozione della P-scale P1-P4 come prioritÃ  operativa

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

Adozione della P-scale per la prioritÃ  operativa

**Context**

La valutazione di urgenza deve essere resa utilizzabile come prioritÃ  operativa di triage. La documentazione DermaTriage rappresenta tale prioritÃ  mediante quattro livelli P1-P4.

**Decision**

DermaTriage rappresenta la prioritÃ  operativa di triage mediante la scala P1-P4.

**Consequences**

Gli obblighi downstream che producono una prioritÃ  operativa devono produrre un valore appartenente al dominio P1-P4. Le condizioni che determinano quale livello P1-P4 debba essere prodotto non fanno parte dell'identitÃ  di questa Decision e devono essere governate al livello operativo appropriato.

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

- Qual Ã¨ il significato normativo dei valori
  24h / 48h / 72h / 7 giorni associati alla P-scale?

- Da quale evento decorre l'eventuale tempo SLA e quale attore
  possiede la responsabilitÃ  del suo rispetto?
```

These questions are analysis output, not Decision semantics.

### 8.6 Joint disposition

```text
CDEC-01-02
JOINT REVIEW:
ACCEPT AS DECISION CANDIDATE
```

No MR cleanup is currently required specifically for this Decision: MR-01 owns the existence of an operational priority without pre-encoding the P1-P4 vocabulary.

## 9. CDEC-01-03 â€” Pipeline image-based sequenziale a quattro stadi

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

Quando Ã¨ disponibile un'immagine della lesione, la documentazione non descrive la valutazione di triage come il risultato diretto di un singolo passaggio analitico. Il percorso image-based costruisce contributi analitici distinti che vengono progressivamente combinati.

**Decision**

DermaTriage costruisce la valutazione image-based mediante una pipeline sequenziale a quattro stadi analitici, nella quale i risultati intermedi contribuiscono alla successiva sintesi di triage.

**Consequences**

Il percorso image-based deve preservare quattro ruoli analitici distinguibili e la loro composizione sequenziale. Le tecnologie correnti usate per realizzare tali ruoli non definiscono automaticamente l'identitÃ  della Decision.

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

- Quale comportamento Ã¨ governato quando uno stadio intermedio
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

### GP-MR01-PMAP-01 â€” symptom-only urgency to P-scale binding

**Status:** OPEN / NOT YET ESTABLISHED.

OR2 documents both the P-scale mapping and a symptom-only urgency fallback, but the current review must not infer without evidence that symptom-only urgency necessarily traverses the exact same P-scale transformation.

Question for later source/FR review:

> Is the symptom-only urgency result explicitly governed as input to the same P1-P4 mapping used by the image-based path?

### GP-MR01-FR-02 â€” image-present vs image-absent descendant ownership

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

### GP-MR01-OWN-01 â€” single-parent pressure

A future FR MUST NOT be made child of more than one Decision merely because multiple Decisions are relevant to the same runtime path.

If the same candidate FR appears to require two Decision parents, review:

1. which Decision semantically owns the obligation;
2. whether one Decision is too broad or too narrow;
3. whether one candidate meaning is only a realization binding;
4. whether the FR itself contains more than one coherent obligation and needs split.

### GP-MR01-REAL-01 â€” named technologies require classification, not automatic promotion

Current realization bindings observed in OR2:

```text
Stage 1 -> EfficientNet-B4
Stage 2 -> Qwen2-VL
Stage 3 -> ChromaDB
Stage 4 -> BioMistral
```

Their presence in authoritative source evidence is sufficient for preservation, not for Decision status.

The next bounded review starts with Stage 1 / EfficientNet-B4 and applies the Decision-vs-realization gate before deciding whether CDEC-01-04 survives at all.

## 11. Guide-change candidates added by the new review

### GDEC-04 â€” Open analytical questions as a non-normative presentation view

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

### GDEC-05 â€” Architecture Decision versus stage FunctionalRequirement

**Status:** supported candidate refinement; validate again during FR analysis.

Working distinction:

- the Decision governs the structural/project commitment that the image-based path is composed of four sequential analytical stages;
- each stage's observable required behavior is a candidate FunctionalRequirement;
- changing the number or semantic role of the stages can reopen the Decision;
- changing the required behavior of one stage can reopen the corresponding FR.

### GDEC-06 â€” Single semantic parent / no Decision-FR multi-parent shortcut

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

### GDEC-07 â€” Technology names are realization by default, not automatic Decisions

**Status:** working classification rule for CDEC-01-04 review.

For `EfficientNet-B4`, `Qwen2-VL`, `ChromaDB` and `BioMistral`, the default hypothesis is current realization evidence.

A technology binding may be promoted to Decision only if source evidence supports an independently governed architectural/project commitment that remains meaningful after neutralizing the product/model name.

The review question is:

> If this technology is replaced while the four-stage Decision and the stage's required behavior remain unchanged, has a governed project commitment changed or only its realization?

A technology is not promoted merely because it is concrete, named, technically important or source-supported.

## 8. MR-01 provisional Decision inventory

The following list is preserved so subsequent chats do not lose the breadth-first discovery state.

| Working ID | Candidate meaning | State |
|---|---|---|
| `CDEC-01-01` | Continuità del triage in assenza di immagine mediante informazioni sintomatologiche | ACCEPT AS DECISION CANDIDATE |
| `CDEC-01-02` | Adozione della P-scale P1-P4 come prioritÃ  operativa | ACCEPT AS DECISION CANDIDATE |
| `CDEC-01-03` | Pipeline AI image-based sequenziale a quattro stadi | ACCEPT AS DECISION CANDIDATE |
| `CDEC-01-04` | Classificazione dei binding tecnologici dei quattro stadi: Decision autonoma vs realization | PENDING / DECISION-vs-REALIZATION GATE |
| `CDEC-01-05` | Workflow diretto vs B4-integrated | PENDING |
| `CDEC-01-06` | Strategia baseline classifier training | PENDING |
| `CDEC-01-07` | Strategia dataset condiviso retrieval/training | HOLD |

No historical `DEC-*` correspondence is asserted here.

## 12. Next joint review

The next bounded review does not assume that `CDEC-01-04` exists as a valid Decision.

Start with the first technology binding:

```text
Stage 1
functional role:
produce image urgency classification

current realization:
EfficientNet-B4
```

Decision-vs-realization question:

> If EfficientNet-B4 is replaced while CDEC-01-03 and the Stage-1 required behavior remain unchanged, has a governed project commitment changed or only the current realization?

Required discussion package:

1. exact CDEC-01-03 meaning;
2. exact OR2 Stage-1 source text;
3. any additional source evidence governing EfficientNet-B4 as a project commitment;
4. neutralization test: remove the product/model name and identify any remaining architectural commitment;
5. single-parent check against the future Stage-1 FR;
6. disposition: `DECISION CANDIDATE`, `REALIZATION`, `LOWER_LEVEL`, `HOLD`.

Repeat the same classification for Qwen2-VL, ChromaDB and BioMistral only after the Stage-1 test is understood.

`CDEC-01-04` survives only if one or more independently governed technology/architecture commitments remain after this review.

## 13. Retirement condition for this file

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
