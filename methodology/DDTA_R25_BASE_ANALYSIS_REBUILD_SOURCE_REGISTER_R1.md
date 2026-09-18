# DDTA R25 - Base Analysis Rebuild Source Register R1

**Status:** MANDATORY REBUILD INPUT REGISTER / NON-NORMATIVE

**Repository baseline:** `e88ebee4be20246e1af6f2b37dd402c848ed22f3`

## 1. Purpose

This register prevents the Base Analysis guide rebuild from silently losing prior semantic distinctions, candidate constructs, rejected hypotheses, counterexamples or deferred method deltas.

A source listed here is input evidence for review. Inclusion does not grant authority.

## 2. Current authority stack

- `methodology/BA0_BASE_ANALYSIS_RESPONSIBILITY_BOUNDARY_R1.md`
- `methodology/BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`
- `methodology/BA2_RELATION_ACTION_VOCABULARY_R3.md`
- `methodology/BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`
- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_INTERPRETATION_COVERAGE_CONTRACT_R1.md`
- `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CONTROLLED_AUTHORING_CONTRACT_R1.md`
- `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex`
- `methodology/DDTA_R25_BA_PRE_HOLDOUT_CONTRACT_ALIGNMENT_R1.md`
- `methodology/DDTA_R25_BA_PRE_HOLDOUT_CONTRACT_FREEZE_CHECKPOINT_R1.md`

## 3. Updated candidate guide surfaces

- `methodology/DDTA_BASE_ANALYSIS_CORE_GUIDE_R1_CANDIDATE_R1.tex`
- `methodology/DDTA_BASE_ANALYSIS_COMPLETE_GUIDE_R1_CANDIDATE_R1.tex`
- `methodology/DDTA_BASE_ANALYSIS_QUESTION_DRIVEN_DISCRIMINATION_MATRIX_R1.md`
- `methodology/DDTA_BASE_ANALYSIS_SEMANTIC_COUPLING_MATRIX_R1.md`
- `methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_SET_INDEX_R1.md`

These files are the preferred updated reading surfaces, but they remain candidate/non-normative until an explicit future promotion.

## 4. Historical BA0-BA5 derivation corpus

The rebuild must preserve access to the complete textual history represented by these repository families:

```text
methodology/BA0_*.md
methodology/BA1_*.md
methodology/BA2_*.md
methodology/BA3_*.md
methodology/BA4_*.md
methodology/BA5_*.md
methodology/BA6_*.md
```

Particular attention is required for candidate derivations, T1/T2/T3/T4 pressure tests, provisional ledgers, closure reviews and predecessor revisions. Their rejected alternatives are part of the evidence base.

## 5. R24 pressure and regression evidence

Mandatory key artifacts include:

- `methodology/DDTA_R24_FACIAL_ACCESS_BA_REPRESENTATION_PRESSURE_REVIEW_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_POST_BA_REGRESSION_CHECKPOINT_R1.md`
- `methodology/DDTA_R24_FACIAL_ACCESS_BA6_INTEGRATED_COMPLETION_CHECKPOINT_R1.md`
- `methodology/DDTA_BA_BEHAVIORAL_NONBEHAVIORAL_PRESSURE_POINT_R24.md`

The behavioral/non-behavioral BAReferent pressure remains research input when BAReferent and `classify` are reviewed.

## 6. DermaTriage post-holdout evidence tree

The entire tree below is retained as rebuild research evidence:

`validation-evidence/dermatriage/post-holdout-method-review-r1/`

Mandatory subgroups:

- `operator-reviews/`
- `construct-reviews/`
- `working-findings/`
- `question-packs/`
- `question-pack-evidence/`
- `post-validations/`
- all `OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R*.yml`
- `CONSTRUCT_REVIEW_LEDGER.yml`
- `CONSTRUCT_REVIEW_TEMPLATE.md`
- `CHAT_REVIEW_PRESENTATION_PROTOCOL.md`

## 7. Current consolidated R25 disposition artifacts

Use at least:

- `validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R22.yml`
- `validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R5.md`
- `validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_ADDITIONS_PRESSURE_CARRY_FORWARD_R8.md`
- `validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/DDTA_R25_REVIEW_COVERAGE_MATRIX_R1.md`
- `validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/SEMANTIC_FAMILY_REVIEW_MAP_R1.md`

## 8. Construct-specific working findings that must not be lost

- `CC02_PROVIDESERVICE_STRENGTHENING_R1.md`
- `PR08_STORAGE_ASSOCIATION_RECONCILIATION_R1.md`
- `PR03_PR10_INITIATION_RECONCILIATION_R1.md`
- `PR13_SELECTION_RECONSTRUCTION_R1.md`
- `POST_OP04_BA_METHOD_PRESSURE_CANDIDATE_MAP_R1.md`
- `OP05_TRANSITION_STATE_REPRESENTATION_CANDIDATE_R1.md`
- `CR-02_DECISIONRULE_COMPARISON_CANDIDATE_R1.md`
- `DEPENDENCY_GRAPH_PROJECTION_HYPOTHESIS_R1.md`

The full `working-findings/` directory remains searchable even when an individual file is not named above.

## 9. Current semantic inventory to preserve for review

### Current top-level BA2 R3 operator inventory

```text
transfer
produce
create
observe
transition
correlate
reference
dependOn
consumeService
realize
assignResponsibility
constrain
classify
decisionRule
```

### Candidate constructs / structures

```text
CC-02 provideService        TESTED_POSITIVE / NOT_ADMITTED
CC-03 storedIn              TESTED_POSITIVE / NOT_ADMITTED
CC-04 initiate              TESTED_POSITIVE / NOT_ADMITTED
selection                   REUSABLE_LOCAL_STRUCTURE / NON-NORMATIVE
```

### Rejected candidate

```text
CC-01 consumeData           REJECT_REDUNDANT
```

### Open / deferred items

```text
PR-01 perform / execution identity
PR-02 pipeline composition/order
PR-04 boundary/interaction
PR-05 ordered comparison
PR-06 scalar/property comparison
PR-07 structured information contract
PR-09 acquisition/refresh
PR-12 negative implication/non-sufficiency
PR-14 applicability/configuration binding
CMD-OP04 observe.result removal
CMD-OP05 transition state/value refinement
OBS-OT-01 operation-target/effect-scope
```

PR-03, PR-08 and PR-10 remain relevant through their reconciled candidate constructs; PR-11 remains important negative evidence against a generic data-consumption operator; PR-13 is retained through the selection structure.

## 10. Search aliases required during construct review

A construct review must search not only its canonical name but common historical wording. Examples:

```text
produce       -> output, result, generate, make available
create        -> create, new identity, occurrence, instantiate
observe       -> read, query, retrieve, inspect
transition    -> state, lifecycle, update, rollback, revoke, restore
transfer      -> send, exchange, deliver, convey, write-back
consumeService-> use service, API use, capability use
realize       -> implementation, materialize, concrete realization, performs?
constrain     -> restriction, allowed domain, threshold, mechanism
classify      -> kind, category, semantic nature, behavioral/non-behavioral
decisionRule  -> mapping, if/then, result assignment, comparison
provideService-> expose, offer service, provider relation
storedIn      -> store, persist, at-rest, residence
initiate      -> invoke, call, start, trigger
selection     -> select, rank, top-K, recent-N, best, argmax, membership
```

## 11. Closure rule for one construct

No construct may receive `REVIEWED` status in the rebuild until:

1. its current authority definition is inspected;
2. its R42 candidate description is inspected;
3. its operator/construct review evidence is inspected where present;
4. associated PR/CC/CL/CMD/OBS material is inspected;
5. rejected alternatives and negative controls are accounted for;
6. DermaTriage application is attempted using only the governed DDTA documentation in scope;
7. the Construct Description Contract is fully populated or fields are explicitly marked `NOT APPLICABLE`, `NOT FROZEN` or `OPEN`.
