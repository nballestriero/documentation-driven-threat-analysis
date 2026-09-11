# Candidate Construct Disposition Matrix R5

## Status

`ACTIVE WORKING ARTIFACT / NON-NORMATIVE`

R5 supersedes R4 for current disposition state. R4 remains historical evidence.

| ID | Topic / candidate | Current evidence/result | Next required test | Current disposition |
|---|---|---|---|---|
| PR-01 | function/process/behavior identity binding / `perform?` | execution evidence exists but irreducibility not demonstrated | future counterexample / completeness recheck | PRESSURE_RETAINED |
| PR-02 | pipeline composition/order | sequencing pressure retained | membership vs ordering; `precedes` vs `dependOn` | OPEN |
| PR-03 | interface/path/invocation | exposure decomposed; invocation reconciled to CC-04 `initiate` | formal CC-04 G1-G8 later | **RECONCILED / CC-04** |
| PR-04 | boundary/interaction | boundary semantics open | boundary crossing vs transfer/interface/initiation semantics | OPEN |
| PR-05 | ordered comparison | ordered/scalar forms exceed equality vocabulary | CL-01 | ROUTE_CL01 |
| PR-06 | scalar/property comparison | typed scalar/property addressing needed | CL-01 | ROUTE_CL01 |
| PR-07 | structured information contract | may be static structure rather than dynamic relation | structure/schema/composition | OPEN |
| PR-08 | at-rest storage association | `storedIn` survives current exhaustion | formal G1-G8 for CC-03 | RECONCILED / CC-03 |
| PR-09 | acquisition/refresh | action semantics survive initial boundaries | exhaust current operators | OPEN |
| PR-10 | conditional action trigger | separate trigger primitive unnecessary; directed activation uses CC-04 + condition | formal CC-04 G1-G8 later | **RECONCILED / CC-04 + CONDITION** |
| PR-11 | data/evidence consumption | non-destructive use representable; destructive consume not governed | none current | RECONCILED |
| PR-12 | negative non-sufficiency | A alone insufficient for B is not NOT(B) | logical/cross-cutting representation | OPEN |
| PR-13 | bounded/ranked selection | top-K/recent-N/best-by-score survive current vocabulary | decompose filter/order/rank/bound/select | **NEXT REVIEW** |
| PR-14 | applicability | scoped rule/constraint meaning remains | qualifier/reusable structure first | OPEN |
| CC-01 | `consumeData` | redundant in current corpus | none | **REJECT_REDUNDANT** |
| CC-02 | `provideService` | positive provider/service evidence; survives current exhaustion | formal G1-G8; compatibility/final signature | **CANDIDATE_TESTED_POSITIVE / NOT_ADMITTED** |
| CC-03 | `storedIn` | positive at-rest storage evidence; survives current exhaustion | formal G1-G8; compatibility/final signature | **CANDIDATE_TESTED_POSITIVE / NOT_ADMITTED** |
| CC-04 | `initiate` | FR-21 + FR-04/05 positive controls; survives 14-operator exhaustion and minimality test | formal G1-G8; cross-corpus compatibility | **CANDIDATE_TESTED_POSITIVE / NOT_ADMITTED** |
| OBS-OT-01 | operation-target/effect-scope | FR-27 pressure without mutation guarantee | local structure/composition | LEVEL_UNRESOLVED |
| CMD-OP04 | remove `observe.result` | open simplification | integrated review | DEFERRED |
| CMD-OP05 | transition state/value refinement | state identity vs typed value open | integrated review | DEFERRED |

## PR-03 / PR-10 reconciliation

```text
invoke
    -> source wording absorbed by CC-04 initiate

trigger
    -> no separate primitive
    -> condition + actual governed action

initiationKind REQUEST | START
    -> rejected redundant / over-specific
```

## CC-04 minimum boundary

```text
initiate
    initiator -> BAReferent [1]
    initiated -> BAReferent [1]

does not imply:
    success
    completion
    transfer
    service consumption
    create
    transition
    automatic trigger
    synchronous execution
```

## Next review

```text
PR-13 bounded / ranked / recency selection
```

No current row is an admitted method delta until the required formal gate is complete.
