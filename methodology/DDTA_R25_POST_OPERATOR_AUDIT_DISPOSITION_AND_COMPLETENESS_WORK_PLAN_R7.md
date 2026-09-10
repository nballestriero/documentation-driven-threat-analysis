# DDTA R25 — Post-Operator-Audit Disposition and Completeness Work Plan R7

## Status

`ACTIVE EXECUTION PLAN / NON-NORMATIVE UNTIL METHOD DELTAS PASS G1-G8`

R7 supersedes R6 for future execution. R6 remains immutable historical evidence.

Exact planning baseline:

```text
68c8a387790c92c7f7e3859bfebd400fa29e242a
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
```

## CC-02 strengthened result

The previous missing-positive-control problem is resolved for conceptual review by the
source-complete service/API/interface test.

Strongest control:

```text
DEC-14 / FR-21
    DermaTriage is governed as project/system actor
    DermaTriage service is explicitly governed
    service/interface availability is explicitly governed
    /analyze is independently reused in invocation semantics
```

Working minimum:

```text
provideService
    provider -> BAReferent
    service  -> BAReferent
```

Do not infer responsibility, implementation, consumption, endpoint inventory completeness or runtime
availability from provision alone.

## Interface and endpoint representation rule under test

Prefer decomposition over a verb-specific `expose` operator.

```text
service offering
    -> provideService

endpoint/access-point identity
    -> BAReferent only when independently reusable/qualified

governed endpoint/interface restriction
    -> constrain

actual service consumption
    -> consumeService

content conveyance
    -> transfer

specific caller/callee activation
    -> invoke ? pending

implementation/materialization
    -> realize only when source establishes realization
```

Endpoint identity must not be invented merely because a service exists.

A list of observed endpoints must not be converted into a closed allowed vocabulary unless the source
actually makes the list exhaustive.

## `expose` disposition

```text
SOURCE WORDING:
    POSITIVE

AUTONOMOUS CONSTRUCT:
    NOT_JUSTIFIED

CURRENT-CORPUS EXHAUSTION:
    REPRESENTABLE_BY_COMPOSITION
```

Do not allocate a candidate ID for `expose`.

This result is local to the current evidence and remains subject to the final source-complete
completeness gate.

## Source stopping rules

### FR-21 / `/analyze`

The endpoint is independently reusable and may require BAReferent identity.

### DEC-14 / `/diagnose`

The integrated path is explicitly governed and can be represented without inferring that the two
known paths are the complete service interface.

### FR-24 administrative operations

Authentication protection is governed. Concrete HTTP paths for each protected administrative
operation are not governed in the current source. Do not invent them.

### DEC-15 / FR-23 B4 APIs

API use, data exchange and retrieval are governed. Exact B4 endpoint paths are not governed. Do not
invent them.

## Next mandatory comparison

Before closing PR-03, test:

```text
PR-03 INVOCATION_ASSOCIATION
    invoke

versus

PR-10 CONDITIONAL_ACTION_TRIGGER_SEMANTICS
    trigger
```

Questions:

1. Is `invoke(A,B)` a specific interaction relation rather than a generic causal trigger?
2. Can trigger conditions activate a behavior without any caller?
3. Can a caller invoke an endpoint without a decision-condition object?
4. Does `invoke` preserve caller/callee topology that `trigger` would lose?
5. Does `trigger` preserve condition-to-action activation that `invoke` would falsely anthropomorphize
   as a call?
6. Can one more general construct represent both without false semantics?
7. If not, are both top-level constructs necessary, or should one/both be local/reusable structures?
8. How do `transfer`, `consumeService`, `produce`, `dependOn`, `reference` and `decisionRule` interact
   with each candidate?

After this comparison, proceed to PR-13 bounded/ranked selection.

The CL-01..CL-05 review and the final completeness gate remain mandatory before any integrated
BA-method revision.
