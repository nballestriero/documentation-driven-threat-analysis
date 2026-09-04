# DDTA R25 - DermaTriage Documentation Work Plan A5 R2

**Status:** ACTIVE A5 WORK PLAN / FR-BRIDGE CONSOLIDATION CHECKPOINT  
**Repository baseline:** `8233469414b3647b09b7d8eb409db95ddfae49bf`  
**Methodology authority:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`  
**BA status:** `NOT STARTED / BLOCKED`

## Current gate state

| Step | Scope | State |
|---|---|---|
| A0 | Authority/source gate | PASS |
| A1 | Project framing | PASS |
| A2 | MacroRequirement / D1 | CUMULATIVE PASS |
| A3 | Semantic sufficiency | PASS for current decomposed scope |
| A4 | Decision / D2 | CLOSED; DEC-01 controlled repair RE-CLOSED during A5 |
| A5 | FunctionalRequirement / D3 | ACTIVE; FR-01..FR-08 preserved |
| A6 | Requirement split | NOT STARTED project-wide; local coherent-unit checks active |
| A7 | SpecializedRequirement | NOT STARTED |
| A8 | SecurityRequirement | NOT STARTED |
| A9 | Cross-MR downstream review | NOT STARTED |
| A10 | Terminology / information / parameter bindings | NOT STARTED; bridge ledger accumulating inputs |
| A11 | Downstream propagation/regression | NOT STARTED |
| A12 | Completeness / promotion readiness | NOT STARTED |
| BA | Base Analysis | BLOCKED until documentation gate PASS |

## A5 preserved progress

- MR-01: FR-01 PASS; FR-02 PASS; cumulative D3 PASS.
- MR-02: STOP AT MR.
- MR-03: FR-03 PASS; cumulative D3 PASS.
- MR-04 / DEC-04: FR-04 prompt accumulation trigger PASS; FR-05 classifier accumulation trigger PASS.
- MR-04 / DEC-09: FR-06 bounded recent prompt-evidence selection PASS / STOP under DEC-09.
- MR-04 / DEC-10: FR-07 disagreement qualification PASS / STOP under DEC-10.
- MR-04 / DEC-11: FR-08 corrected P-scale -> classifier supervision mapping PASS / STOP under DEC-11.

## Parameter Governance Boundary now active

For parameter-like evidence apply:

`concrete value -> neutralize to N -> semantic materiality gate -> exact-value governance gate -> symbolic semantic parameter or realization/configuration STOP`.

Current classified examples:

| Semantic role | Symbolic DDTA form | Current binding | Exact value governance |
|---|---|---:|---|
| prompt evolution accumulation threshold | `PromptEvolutionThreshold=N` | 10 | NOT SPECIFIED |
| classifier adaptation accumulation threshold | `ClassifierAdaptationThreshold=N` | 50 | NOT SPECIFIED |
| prompt recent-evidence window size | `PromptEvidenceWindowSize=N` | 20 | NOT SPECIFIED |

Do not create one Requirement/document per parameter. Preserve selected semantic parameters in a structured registry/binding view and leave large technical configuration inventories below the DDTA semantic boundary.

## GI-21 bridge ledger taxonomy

For each implementation-critical datum determine which bridge applies:

1. semantic concept -> data/state encoding;
2. semantic parameter -> configuration value;
3. semantic reference -> interface identifier;
4. semantic transformation -> realization encoding.

Keep governed semantics and source-observed realization identifiers distinct, but traceably connected.

## Confirmed / unresolved FR relations

- `FR-07 -> FR-05`: CONFIRMED consumption of qualifying disagreement evidence.
- `FR-01 -> FR-02`: UNRESOLVED applicability/binding; do not draw a solid edge.
- `FR-07 -> FR-08`: NO direct producer-consumer edge asserted; shared downstream classifier-adaptation context is insufficient.

## Current A5 gaps added under MR-04

- `GAP-DERMA-ADAPT-COUNTING-01` - reset/dedup/reuse/persistence/concurrency semantics of accumulation triggers.
- `GAP-DERMA-ADAPT-THRESHOLD-AUTH-01` - change authority/lifecycle of concrete trigger thresholds.
- `GAP-DERMA-PROMPT-WINDOW-01` - membership/order/underfilled/dedup/reuse/scope semantics of prompt evidence window.
- `GAP-DERMA-REVIEW-DISAGREEMENT-BINDING-01` - correction vs disagreement vs `agrees` state relationship.
- `GAP-DERMA-SUPERVISION-INPUT-01` - missing/invalid/conflicting corrected P-scale semantics.

Earlier A5 and R4 gaps remain open unless explicitly closed.

## Immediate next execution order

1. DEC-06 comparative pre-adoption acceptance behavior -> FR candidate.
2. DEC-07 quality trade-off and metric constraints -> FR/SR ownership review; test Parameter Governance Boundary on the documented tolerance.
3. DEC-08 post-adoption reversibility -> rollback FR candidate and binding gap review.
4. DEC-05 path-separation cumulative check if downstream FRs reveal missing ownership.
5. MR-04 cumulative D3 review.
6. Project-wide A5 closure review before entering A6.

For every remaining candidate continue:

`source evidence -> candidate obligation -> subtract parent meaning -> exact parent -> semantic sufficiency -> split/coherent unit -> normative clauses -> GI-21 bridge ledger -> parameter boundary when applicable -> assessability -> gap -> disposition -> STOP/routing`.

## Checkpoint discipline

This checkpoint is intentionally created before DEC-06/07/08 because the evidence/supervision half of MR-04 is now semantically closed enough to preserve independently, and GI-21/GI-25 have materially changed the downstream authoring protocol. Methodology R4 remains authoritative; the candidates are preserved for explicit promotion review, not silently applied as new authority.
