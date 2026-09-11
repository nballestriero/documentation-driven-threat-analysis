# Continuation after R36

## Exact baseline for applying this drop-in

```text
6c0c16d493e292c947b1a06359faf628f613f1dc
```

The repository must be clean before extraction. Stop if HEAD or verifier checks fail.

After commit/push, use the actual `git rev-parse HEAD` result as the next exact baseline.

## Frozen method state

```text
BA0 R1
BA1 R1
BA2 R3
BA3 R1
BA4 R1
BA5 R1
top-level BA2 operators = 14
```

## Candidate state

```text
CC-01 consumeData
    CANDIDATE_REJECTED_REDUNDANT

CC-02 provideService
    CANDIDATE_TESTED_POSITIVE
    NOT_ADMITTED
    G1-G8_PENDING

CC-03 storedIn
    CANDIDATE_TESTED_POSITIVE
    NOT_ADMITTED
    G1-G8_PENDING

CC-04 initiate
    CANDIDATE_TESTED_POSITIVE
    NOT_ADMITTED
    G1-G8_PENDING
```

## PR-03 / PR-10 reconciliation

```text
invoke
    -> source wording absorbed by initiate

trigger
    -> no separate primitive
    -> condition + actual governed action

initiationKind REQUEST | START
    -> rejected as redundant / over-specific
```

## Remaining methodology work

This is not the end of the review. Remaining work includes at minimum:

```text
PR-13 bounded/ranked/recency selection
PR-02 pipeline composition/order
PR-04 boundary/interaction
PR-07 structured information contract
PR-09 acquisition/refresh
PR-12 negative non-sufficiency
PR-14 applicability
OBS-OT-01 operation target/effect scope
CL-01..CL-05 formal condition-language review
CMD-OP04 observe.result simplification
CMD-OP05 transition state/value refinement
final source-complete completeness gate
integrated G1-G8 method revision
```

## Next conceptual task

```text
PR-13 BOUNDED_RECENCY_COLLECTION_SELECTION_SEMANTICS
```

Start with FR-18 top-5 similarity retrieval, FR-06 most-recent-20 evidence selection and FR-20
best-checkpoint-by-Macro-F1.
