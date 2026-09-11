# DDTA R25 — CC-04 `initiate` consolidation R36

This checkpoint consolidates the source-complete PR-03 invocation / PR-10 trigger comparison at:

```text
6c0c16d493e292c947b1a06359faf628f613f1dc
```

No normative BA0–BA5 mutation is made. The BA2 top-level operator basis remains 14.

## Main result

```text
CC-04 initiate

working meaning:
    one governed referent directly initiates, starts, or requests execution/activation
    of another governed referent

working minimum signature:
    initiator -> BAReferent [1]
    initiated -> BAReferent [1]

status:
    CANDIDATE_TESTED_POSITIVE
    NOT_ADMITTED
    G1-G8_PENDING
```

## `invoke`

FR-21 preserves directed caller/callee topology. The source wording `invoke` is retained as evidence,
but its material meaning is represented by the more general candidate `initiate`.

```text
invoke operator:
    NOT_JUSTIFIED AS SEPARATE PRIMITIVE
```

## `trigger`

FR-04 and FR-05 preserve threshold-conditioned activation, but the threshold is a condition rather
than a caller. The BA proposition model already has condition/applicability semantics.

```text
generic trigger primitive:
    NOT_JUSTIFIED

conditional initiation:
    initiate + condition

other conditional behavior:
    corresponding governed operator + condition
```

## Minimality — no `initiationKind`

The local values `REQUEST` and `START` were explicitly tested. Removing them loses no independently
governed information in the current corpus.

```text
initiationKind:
    REJECT_REDUNDANT_OVER_SPECIFIC
```

Target identity already distinguishes endpoint, process and adaptation-cycle targets. `START` may
also falsely imply new occurrence or lifecycle transition.

## Non-implications

`initiate` does not automatically assert:

```text
success
completion
synchronous execution
create
transition
transfer
consumeService
automatic trigger
authorization
responsibility
```

## Strong controls

Positive:
- FR-21: DirectClient -> POST /analyze -> DermaTriageTriageProcess.
- FR-04: DermaTriage initiates PromptEvolutionCycle under the prompt threshold condition.
- FR-05: DermaTriage initiates ClassifierAdaptationCycle under the classifier threshold condition.

Negative/boundary:
- FR-10: support for revocation/restoration does not establish automatic rollback initiation.
- FR-25: calls toward B4 do not establish a specific invoked endpoint/operation.
- FR-16 / FR-01 / FR-03: conditional behavior is represented by existing operator + condition.
- FR-27: behavior inside an already-activated cycle does not create another initiation.

## Next review

Proceed to PR-13 bounded/ranked/recency selection. Do not pre-decide whether it requires a top-level
operator, local rule language, reusable structure or composition.
