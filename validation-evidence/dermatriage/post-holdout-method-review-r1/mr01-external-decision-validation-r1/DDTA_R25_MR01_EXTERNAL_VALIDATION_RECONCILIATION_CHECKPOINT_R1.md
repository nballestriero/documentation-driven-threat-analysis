# DDTA R25 — MR-01 External Decision Validation / Three-Way Reconciliation Checkpoint R1

**Status:** PERMANENT VALIDATION EVIDENCE / NON-NORMATIVE METHODOLOGY INPUT
**Scope:** DermaTriage MR-01 Decision reconstruction only
**Purpose:** preserve the answer-blind external reviews, compare them with the frozen internal result, and record the reconciled state before authoring R7.

## 1. Frozen internal reference

Repository:

`nballestriero/documentation-driven-threat-analysis`

Frozen internal baseline:

`c91dd567564e4a7f61c2e4e11fb4a9495623aa01`

Commit subject:

`R25: close MR01 decision family regression`

Internal temporary ledger at closure:

`methodology/DDTA_R25_DERMATRIAGE_MR01_DECISION_GUIDE_PRESSURES_TEMP_R1.md`

Internal ledger SHA-256 at closure:

`9a8b925ad660c0aab52ff586447b58ce3c8b2cede01506eb0618471027f670f9`

This internal result was frozen before the external reports were compared.

## 2. External review artifacts

### External Review 1

File:

`EXTERNAL_REVIEW_1.md`

SHA-256:

`d1559043d9611a0fbbb7753c7f2a0cc7ed99d517815ec31e59fd0cfc5908faf3`

Declared prior exposure to the hidden internal Decision result:

`NO`

Final accepted external Decision nuclei:

- four-stage image-based pipeline;
- HIGH/MEDIUM/LOW urgency vocabulary;
- P1-P4 operational-priority scale with SLA association;
- symptom-only no-image path.

The review lowers the numeric HIGH threshold, named model bundle, RAG top-5, JSON output and safety targets.

### External Review 2

File:

`EXTERNAL_REVIEW_2_MISTRAL_MEDIUM_3_5.md`

Analyst declaration:

`Mistral Medium 3.5 (Vibe)`

SHA-256:

`5a11bfcf24f5b11e91a8f75a1e4f4c8a75f56130f2c72515c8fcfca01405bb92`

Declared prior exposure to the hidden internal Decision result:

`NO`

Final accepted external Decision nuclei:

- four-stage image-based pipeline;
- urgency-to-P-scale mapping with SLA;
- symptom-only no-image path.

Clinical performance targets are lowered to FunctionalRequirement level.

## 3. Blind-review input provenance

The external experiment was prepared as an **answer-blind** review:

- original DermaTriage source PDFs;
- MR-only DDTA input;
- R5 current authority;
- R6 Candidate R2;
- no internal CDEC/GDEC ledger;
- no R7/Rebuild guide;
- no internal Decision answer set.

Blind-review package generated before external execution:

`DDTA_MR01_EXTERNAL_BLIND_REVIEW_R1.zip`

Package SHA-256:

`e25514e7fd78300bc4e1353aa85ab9bf11f148f078760f96fe1684e97c5ee5e8`

Operational six-PDF source subset SHA-256:

`e9e54d3ba7c06a5a4c215d015bc741e99a254f7337900ad60b783420039a6fed`

Important qualification:

The test is **answer-blind but not example-blind**, because R5/R6 already contain historical DermaTriage examples. Therefore convergence on examples already shown by the guide is not pure independent rediscovery. Boundary/classification disagreements remain useful evidence about guide behavior.

External Review 2 records the operational source-subset SHA as the package ZIP SHA. This metadata mismatch is preserved as an experimental-procedure note and does not affect the semantic comparison.

## 4. Three-way comparison

| Semantic item | Internal pre-external | External 1 | External 2 | Reconciled state |
|---|---|---|---|---|
| No-image symptom continuation | Decision | Decision | Decision | KEEP — stable core |
| Four-stage image-based architecture | Decision | Decision | Decision | KEEP — technology-neutral core |
| P1-P4 operational-priority domain | Decision | Decision + SLA | Decision + mapping + SLA | KEEP NARROW — granularity ambiguity confirmed |
| HIGH/MEDIUM/LOW autonomous Decision | not promoted | Decision | not separate | DO NOT PROMOTE |
| Vector-similarity retrieval strategy | Decision | lower-level | not separate | LOWER_LEVEL after reconciliation |
| Direct + B4-integrated access strategy | Decision | integration/interface realization | endpoint/interface detail | HOLD / BOUNDARY_REVIEW |
| Initial baseline training/validation lifecycle | Decision | model realization | training/configuration | LOWER_LEVEL after reconciliation |
| Shared retrieval/training data lineage | Decision | data facts | dataset/model fact | LOWER_LEVEL after reconciliation |
| Analytical -> operational phase boundary | Decision | not discovered | folded into mapping | KEEP — strong internal finding |
| Concrete Stage 1-4 technologies | realization/binding | lower-level | included in Decision | keep outside Decision identity |
| Exact urgency/confidence -> P-scale mapping | downstream FR behavior | FR-like | Decision | keep downstream |
| SLA trigger/owner/normativity | OPEN | gaps preserved | bundled despite gaps | keep OPEN |
| Clinical performance targets | lower-level | lower-level | FR | lower-level |
| MR no-image prose | cleanup pressure | review uncertain | no cleanup | keep cleanup pressure |
| Decision-family completeness | closed with pressures | PASS + gaps | PASS + no HOLD | closure terminology needs refinement |

## 5. Stable core

### 5.1 CDEC-01-01 — no-image continuation

Reconciled state:

`KEEP / ACCEPT AS DECISION CANDIDATE`

The three reconstructions converge on the policy that triage remains available without an image through symptom information.

The exact symptom vocabulary, required/optional inputs, missing-value semantics and scoring remain downstream/open.

### 5.2 CDEC-01-02 — P1-P4 domain

Reconciled state:

`KEEP / ACCEPT AS DECISION CANDIDATE — NARROW IDENTITY`

Identity retained:

`operational priority is represented in the P1-P4 domain`

Do not absorb automatically:

- exact urgency/confidence mapping;
- 24h / 48h / 72h / 7-day bindings;
- SLA trigger;
- SLA owner;
- SLA normative authority.

The external reviews demonstrate that R5/R6 allow materially different decompositions of the same source bundle.

### 5.3 CDEC-01-03 — four-stage image-based architecture

Reconciled state:

`KEEP / ACCEPT AS DECISION CANDIDATE`

Decision identity remains the four-stage analytical decomposition.

Concrete names such as EfficientNet-B4, Qwen2-VL, ChromaDB, all-MiniLM-L6-v2 and BioMistral-7B remain visible source-supported bindings/realizations unless independent Decision authority is established.

Preserving a concrete referent does not make that referent the identity of the parent Decision.

### 5.4 CDEC-01-08 — analytical-to-operational phase boundary

Reconciled state:

`KEEP / ACCEPT AS DECISION CANDIDATE`

Original OR2 architecture explicitly places a separate Adaptation Layer after the four-stage analytical pipeline.

The following project structures are independently variable while MR-01 can remain stable:

```text
four-stage analytical synthesis
    ->
separate adaptation
    ->
operational priority
```

versus:

```text
analytical synthesis
    ->
operational priority directly
```

Neither external reviewer isolated this phase boundary. The miss is evidence for a stronger phase-boundary family-regression test in R7.

## 6. Demoted / reopened internal candidates

### 6.1 CDEC-01-04A — vector-similarity retrieval strategy

Pre-external status:

`ACCEPT AS DECISION CANDIDATE`

Reconciled status:

`LOWER_LEVEL`

Reason:

Neutralizing ChromaDB, embedding model, cosine and top-5 reveals the meaningful abstraction “vector-similarity retrieval”, but the source does not establish that this abstraction is independently governed as a stable project Decision.

Method lesson:

```text
survives neutralization
!=
Decision authority established
```

Neutralization is candidate generation, not automatic promotion.

### 6.2 CDEC-01-05 — direct + B4-integrated access strategy

Pre-external status:

`ACCEPT AS DECISION CANDIDATE`

Reconciled status:

`HOLD / BOUNDARY_REVIEW`

The evidence is stronger than an incidental endpoint:

```text
/analyze  -> direct full pipeline
/diagnose -> B4-integrated pipeline
```

and OR5 tests both paths.

However the current source set does not yet establish whether preserving both modes is independently governed policy/architecture or the current interface surface.

Do not discard this candidate. Resolve it with an explicit integration-boundary authority gate before R7 finalization.

### 6.3 CDEC-01-06 — initial baseline training/validation lifecycle

Pre-external status:

`ACCEPT AS DECISION CANDIDATE`

Reconciled status:

`LOWER_LEVEL`

The source clearly distinguishes initial training from later feedback-driven retraining, but it does not sufficiently establish that the initial baseline-development lifecycle is an MR-01 Decision rather than the development realization that produced the current classifier.

Lifecycle discovery remains useful, but Decision promotion requires an independent-governance and runtime/development-boundary gate.

### 6.4 CDEC-01-07 — shared dermatology data lineage

Pre-external status:

`ACCEPT AS DECISION CANDIDATE`

Reconciled status:

`LOWER_LEVEL`

OR3 directly proves that one current data source serves:

`RAG retrieval + CNN training base`

This relationship must be preserved as evidence.

The current source does not establish that a shared lineage must remain a stable project policy rather than current data architecture/realization.

Cross-capability relationship discovery remains useful; automatic Decision promotion does not.

## 7. External-only HIGH/MEDIUM/LOW candidate

External Review 1 promotes the urgency vocabulary to an autonomous Decision.
External Review 2 does not.
The internal reconstruction does not.

Reconciled state:

`DO NOT PROMOTE TO DECISION ON CURRENT EVIDENCE`

Preserve HIGH/MEDIUM/LOW as source-supported lower-level governed meaning.

Critical rule:

```text
can vary while MR remains stable
```

is necessary for Decision review but is not sufficient for promotion.

## 8. MR-01 wording pressure

The frozen MR says:

> Quando non è presente un'immagine della lesione, il progetto prevede un percorso basato sui sintomi disponibili.

All three analyses recognize the selected no-image response as material project meaning.

Because the selected response can vary while the macro responsibility remains stable, the existing internal cleanup pressure is retained.

Reconciled state:

`GP-MR01-DEC-01 — KEEP`

The external reviewers' willingness to leave the sentence in MR Context is evidence that R5/R6 do not make MR-to-Decision leakage review sufficiently mandatory.

## 9. Closure semantics

The experiment demonstrates that “Decision discovery complete” is ambiguous unless scoped by semantic layer.

Required future distinction:

```text
DECISION DISCOVERY CLOSED FOR CURRENT SOURCE SET
!=
ALL PROJECT SEMANTICS RESOLVED
!=
FR CLOSED
!=
PARAMETER/CONFIGURATION CLOSED
```

A Decision family may be closed while lower-level open questions remain.

However a question that changes Decision identity must remain HOLD or trigger controlled reopen.

Current MR-01 state after reconciliation:

```text
DECISION FAMILY:
REOPENED BY EXTERNAL VALIDATION / RECONCILIATION

STABLE ACCEPTED CORE:
CDEC-01-01
CDEC-01-02
CDEC-01-03
CDEC-01-08

HOLD / BOUNDARY_REVIEW:
CDEC-01-05

LOWER_LEVEL AFTER RECONCILIATION:
CDEC-01-04A
CDEC-01-06
CDEC-01-07

FR AUTHORING:
NOT STARTED
```

## 10. R7 findings supported by the experiment

### R7-F01 — change test is necessary, not sufficient

Require:

```text
MR stability
+
semantic-level fit
+
source-supported independent governance
```

### R7-F02 — neutralization generates candidates; it does not prove Decision authority

### R7-F03 — concrete referent preservation does not define parent Decision identity

### R7-F04 — separate domain, conditional selection rule, numeric binding and service semantics

### R7-F05 — make MR-prose Decision-leakage review mandatory

### R7-F06 — add integration-boundary discovery plus independent-governance promotion gate

### R7-F07 — add explicit phase-boundary family-regression test

### R7-F08 — lifecycle and data-lineage tests require independent governance and runtime/development boundary checks

### R7-F09 — define closure by semantic layer

### R7-F10 — validate R7 on an example-blind holdout project

## 11. Immediate next step

Do not author FRs yet.

Do not copy the old GDEC list mechanically into R7.

Next controlled step:

1. resolve `CDEC-01-05` under an explicit integration-boundary authority gate;
2. freeze the final reconciled MR-01 Decision family;
3. derive R7 from the reconciled findings;
4. validate R7 on an example-blind holdout;
5. only then use the updated guide for the remaining DermaTriage MR Decision families.

This checkpoint preserves the methodological refinement rule:

```text
previous evidence
+
new external counterevidence
+
explicit resolution
=
refined state
```
