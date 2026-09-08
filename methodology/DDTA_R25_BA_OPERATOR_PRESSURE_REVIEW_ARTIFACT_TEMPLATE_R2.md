# DDTA R25 — BA Operator / Condition / Pressure Review Artifact Template R2

> R2 adds the mandatory per-construct consolidation and optional construct-specific question-pack sections. It does not change BA0–BA5.

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

```text
candidate:
meaning preserved:
meaning lost:
meaning distorted:
new meaning accidentally introduced:
```

## 5. Existing-construct exhaustion and semantic boundaries

Test neighboring operators/compositions explicitly. Record what the construct intentionally does **not** mean.

## 6. All-occurrences coverage

State which source occurrences were searched/tested and whether any remain uncovered.

## 7. Construct-specific question pack — optional but recommended when useful

For each question retained in the pack record:

```text
question:
why it matters:
source answer or NONE:
QA disposition: ANSWERED | CLARITY_OPPORTUNITY | GOVERNED_GAP | NOT_APPLICABLE
adjacent review routing, if any:
```

Question packs MUST NOT create project truth or silently extend the construct.

## 8. Rejected alternatives / non-inferences

Record shortcuts that must not be reconstructed later.

## 9. Local verdict

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

## 10. Generalization and minimality

Explain why the finding is method-general or project-specific.

## 11. G1–G8 evaluation

Required for any candidate method delta.

## 12. FINAL_BA_TRACE

Record:

- referents involved;
- proposition/condition meaning;
- source anchors;
- accepted representation candidate or unresolved marker;
- explicit non-inferences;
- dependencies on another review.

## 13. Documentation QA — separate from BA-method delta

```text
ANSWERED
CLARITY_OPPORTUNITY
GOVERNED_GAP
NOT_APPLICABLE
```

## 14. Open/deferred questions and owning review

List each unresolved item and the exact future review that owns it.

## 15. Per-construct consolidation result

Record the stable closure state that must be carried into the next review and the ledger.

## Closure check

The review is not complete unless another analyst can reconstruct the finding from this artifact plus governed repository sources without conversation history.
