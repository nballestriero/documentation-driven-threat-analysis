# Candidate Construct Disposition Matrix R3

## Status

`ACTIVE WORKING ARTIFACT / NON-NORMATIVE`

R3 supersedes R2 for current disposition state. R2 remains historical evidence.

| ID | Topic / candidate | Current evidence/result | Next required test | Current disposition |
|---|---|---|---|---|
| PR-01 | function/process/behavior identity binding / `perform?` | FR-16 absorbable by `produce`; FR-27 does not prove irreducible `perform` | future counterexample / completeness recheck | PRESSURE_RETAINED |
| PR-02 | pipeline composition/order | sequencing pressure retained | membership vs ordering; `precedes` vs `dependOn` | OPEN |
| PR-03 | interface/path/invocation | endpoint/path and invocation pressure retained | distinguish expose, invoke, service use and transfer | **NEXT REVIEW** |
| PR-04 | boundary/interaction | boundary semantics open | boundary crossing vs transfer/endpoint semantics | OPEN |
| PR-05 | ordered comparison | ordered/scalar forms exceed equality vocabulary | CL-01 | ROUTE_CL01 |
| PR-06 | scalar/property comparison | typed scalar/property addressing needed | CL-01 | ROUTE_CL01 |
| PR-07 | structured information contract | may be static structure rather than dynamic relation | structure/schema/composition | OPEN |
| PR-08 | at-rest storage association | `transfer+constrain` partial; generic `persist` too bundled; `storedIn` survives delete/exhaustion tests | formal G1-G8 for CC-03 during integrated candidate gate | **RECONCILED / CC-03** |
| PR-09 | acquisition/refresh | action semantics survive initial boundaries | exhaust current operators | OPEN |
| PR-10 | conditional action trigger | survives `constrain`/`decisionRule` boundaries | trigger review after PR-03 | GROUP2_PENDING |
| PR-11 | data/evidence consumption | non-destructive use representable; destructive consume not governed | none current | RECONCILED |
| PR-12 | negative non-sufficiency | A alone insufficient for B is not NOT(B) | logical/cross-cutting representation | OPEN |
| PR-13 | bounded/ranked selection | top-K/recent-N/best-by-score survive current vocabulary | decompose filter/order/rank/bound/select | GROUP2_PENDING |
| PR-14 | applicability | scoped rule/constraint meaning remains | qualifier/reusable structure first | OPEN |
| CC-01 | `consumeData` | redundant in current corpus | none | **REJECT_REDUNDANT** |
| CC-02 | `provideService` | autonomous evidence insufficient | future corpus/completeness recheck | **INSUFFICIENT_EVIDENCE** |
| CC-03 | `storedIn` | positive FR-26/FR-10 evidence; negative/boundary controls; existing-composition exhaustion survives | formal G1-G8, compatibility, final signature/cardinality | **CANDIDATE_TESTED_POSITIVE / NOT_ADMITTED** |
| OBS-OT-01 | operation-target/effect-scope | FR-27 pressure without mutation guarantee | local structure/composition | LEVEL_UNRESOLVED |
| CMD-OP04 | remove `observe.result` | open simplification | integrated review | DEFERRED |
| CMD-OP05 | transition state/value refinement | state identity vs typed value open | integrated review | DEFERRED |

## CC-03 working boundary

```text
storedIn(storedItem, store)
    does not imply:
        transfer/write event
        retention duration
        durability
        history
        versioning
        recoverability
        restore
        writer identity
```

## Rejected PR-08 working hypothesis

```text
persist
    NOT_JUSTIFIED_AS_GENERIC_OPERATOR
```

No row in this matrix is admitted method until the required formal gate is complete.
