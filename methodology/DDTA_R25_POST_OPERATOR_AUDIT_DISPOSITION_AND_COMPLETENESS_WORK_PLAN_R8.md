# DDTA R25 — Post-Operator-Audit Disposition and Completeness Work Plan R8

## Status

`ACTIVE EXECUTION PLAN / NON-NORMATIVE UNTIL METHOD DELTAS PASS G1-G8`

R8 supersedes R7 for future execution. R7 remains immutable historical evidence.

Exact planning baseline:

```text
6c0c16d493e292c947b1a06359faf628f613f1dc
```

Frozen method:

```text
BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
top-level operator count = 14
```

## Current candidate state

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

## PR-03 / PR-10 result

Source-complete testing supports one narrow candidate:

```text
initiate
    initiator -> BAReferent [1]
    initiated -> BAReferent [1]
```

Working meaning: preserve a governed directed initiation relation in which one project-semantic
referent starts or requests execution/activation of another referent.

It does not assert success, completion, creation, state transition, transfer, service consumption,
synchronous execution or automatic triggering.

### `invoke`

```text
source wording: POSITIVE
separate primitive: NOT_JUSTIFIED
route: CC-04 initiate
```

### `trigger`

```text
source pressure: POSITIVE
separate primitive: NOT_JUSTIFIED
route:
    proposition-local condition
    +
    actual governed action
```

### `initiationKind`

```text
REQUEST | START
DELETE_TEST: NO GOVERNED LOSS
DISPOSITION: REJECT_REDUNDANT_OVER_SPECIFIC
```

## Source controls

FR-21 is the strongest directed-topology positive control.

FR-04 and FR-05 are positive controls for actor-to-cycle initiation under separately governed
conditions.

FR-10 is a negative/boundary control because rollback automaticity is not governed.

FR-25 is a negative/boundary control because authenticated B4 calls do not supply a specific invoked
endpoint/operation target.

FR-16, FR-01 and FR-03 demonstrate that generic conditional behavior remains existing operator +
condition.

FR-27 concerns behavior inside an already-activated retraining cycle.

## CC-04 admission discipline

Use a future `initiate` proposition only when all are source-grounded:

```text
1. initiator identity
2. initiated target identity
3. directed initiation/start/call meaning
4. material semantic loss if that relation is deleted
```

Do not infer `initiate` from mere dependency, transfer, service consumption, a condition becoming
true, support/capability, generic implementation calls, or an unnamed/ungoverned operation target.

## Next review — PR-13

Test independently:

```text
FR-18:
    similarity
    ranking
    top-5 bound
    selected membership

FR-06:
    recency
    pertinence filtering
    most-recent-20 bound
    membership

FR-20:
    candidate checkpoints
    score comparison
    best-by-Macro-F1
    selected result
```

Exhaust existing operators, decisionRule local language, constrain, controlled local values,
reusable selection/query structures and composition before considering a new top-level candidate.

After PR-13 continue the remaining structural, acquisition/state, logical and applicability
pressures, CL-01..CL-05, deferred operator deltas, final completeness gate and integrated G1-G8.
