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

## 8. MR-01 provisional Decision inventory

The following list is preserved so subsequent chats do not lose the breadth-first discovery state.

| Working ID | Candidate meaning | State |
|---|---|---|
| `CDEC-01-01` | Continuità del triage in assenza di immagine mediante informazioni sintomatologiche | ACCEPT AS DECISION CANDIDATE |
| `CDEC-01-02` | Adozione della P-scale P1-P4 come priorità operativa | PENDING |
| `CDEC-01-03` | Pipeline AI image-based sequenziale a quattro stadi | PENDING |
| `CDEC-01-04` | Allocazione tecnologica ai singoli stadi | PENDING / split-lower-level review |
| `CDEC-01-05` | Workflow diretto vs B4-integrated | PENDING |
| `CDEC-01-06` | Strategia baseline classifier training | PENDING |
| `CDEC-01-07` | Strategia dataset condiviso retrieval/training | HOLD |

No historical `DEC-*` correspondence is asserted here.

## 9. Next joint review

Next candidate:

```text
CDEC-01-02
Adozione della P-scale P1-P4 come rappresentazione della priorità operativa
```

Required discussion package:

1. exact frozen MR-01 text;
2. original source table and surrounding meaning;
3. candidate Decision wording;
4. distinction between adopting P1-P4 and the conditional mapping that computes P1/P2/P3/P4;
5. possible FR pressure;
6. joint disposition.

## 10. Retirement condition for this file

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
