# DDTA R25 — BA Operator / Condition / Pressure Review Artifact Template R1

> Copy this template for each `OP-*`, `CL-*`, or `PR-*` review. Do not close a review from chat notes alone.

## Review identity

```text
review_id:
review_kind: OPERATOR | CONDITION_LANGUAGE | PRESSURE
status:
frozen_method: BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
baseline_commit:
```

## 1. Construct or pressure under review

- name:
- frozen definition/signature, if applicable:
- inherited pressure IDs, if applicable:

## 2. Governed source evidence

For every material occurrence:

- source anchor: MR / DEC / FR / exact section
- evidence-bearing excerpt:
- governed semantic claim:

## 3. Previous BA / holdout representation

Record the actual earlier representation, including rejected attempts where relevant.

## 4. Representation experiments

For each candidate representation:

```text
candidate:
meaning preserved:
meaning lost:
meaning distorted:
new meaning accidentally introduced:
```

## 5. Existing-construct exhaustion

Explicitly test neighboring operators and compositions. Record why each succeeds or fails.

## 6. All-occurrences coverage

State which source occurrences were searched/tested and whether any remain uncovered.

## 7. Rejected alternatives / non-inferences

Record shortcuts that must not be reconstructed later.

## 8. Local verdict

Choose one or justify another controlled value:

```text
COMPLETE_NO_CHANGE
COMPLETE_GUIDE_CLARIFICATION
COMPLETE_APPLICATION_CORRECTION
EXTENSION_CANDIDATE
NEW_CONSTRUCT_PRESSURE_RETAINED
NOT_TESTED
DEFERRED_WITH_REASON
REJECTED
```

## 9. Generalization and minimality

Explain why the finding is method-general or why it remains project-specific.

## 10. G1–G8 evaluation

Required for any candidate method delta:

```text
G1 source evidence:
G2 general formulation:
G3 construct exhaustion:
G4 no false semantics:
G5 minimality:
G6 non-redundancy:
G7 backward compatibility:
G8 projection/feedback value:
```

## 11. FINAL_BA_TRACE

Record exactly what must be reconstructable later:

- referents involved;
- proposition/condition meaning;
- source anchors;
- accepted representation candidate or unresolved marker;
- explicit non-inferences;
- dependencies on another review.

## 12. Documentation QA — separate from BA-method delta

Use only as applicable:

```text
ANSWERED
CLARITY_OPPORTUNITY
GOVERNED_GAP
NOT_APPLICABLE
```

A documentation QA finding is not automatically a documentation-method change.

## 13. Open/deferred questions

List dependencies and the exact review that should resolve them.

## Closure check

The review is not complete unless another analyst can use this artifact plus the governed repository source to reconstruct the finding without conversation history.
