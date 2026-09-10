# Candidate Construct Disposition Matrix R4

## Status

`ACTIVE WORKING ARTIFACT / NON-NORMATIVE`

R4 supersedes R3 for current disposition state. R3 remains historical evidence.

| ID | Topic / candidate | Current evidence/result | Next required test | Current disposition |
|---|---|---|---|---|
| PR-01 | function/process/behavior identity binding / `perform?` | execution evidence exists but irreducibility not demonstrated | future counterexample / completeness recheck | PRESSURE_RETAINED |
| PR-02 | pipeline composition/order | sequencing pressure retained | membership vs ordering; `precedes` vs `dependOn` | OPEN |
| PR-03 | interface/path/invocation | exposure facet decomposed; invocation survives current operator exhaustion | compare `invoke` with PR-10 `trigger` | **ACTIVE / PARTIALLY RECONCILED** |
| PR-04 | boundary/interaction | boundary semantics open | boundary crossing vs transfer/interface semantics | OPEN |
| PR-05 | ordered comparison | ordered/scalar forms exceed equality vocabulary | CL-01 | ROUTE_CL01 |
| PR-06 | scalar/property comparison | typed scalar/property addressing needed | CL-01 | ROUTE_CL01 |
| PR-07 | structured information contract | may be static structure rather than dynamic relation | structure/schema/composition | OPEN |
| PR-08 | at-rest storage association | `storedIn` survives current exhaustion | formal G1-G8 for CC-03 | RECONCILED / CC-03 |
| PR-09 | acquisition/refresh | action semantics survive initial boundaries | exhaust current operators | OPEN |
| PR-10 | conditional action trigger | source evidence strong; must now be compared with invocation | `invoke` vs `trigger` full-corpus test | **NEXT REVIEW** |
| PR-11 | data/evidence consumption | non-destructive use representable; destructive consume not governed | none current | RECONCILED |
| PR-12 | negative non-sufficiency | A alone insufficient for B is not NOT(B) | logical/cross-cutting representation | OPEN |
| PR-13 | bounded/ranked selection | top-K/recent-N/best-by-score survive current vocabulary | decompose filter/order/rank/bound/select | GROUP2_PENDING |
| PR-14 | applicability | scoped rule/constraint meaning remains | qualifier/reusable structure first | OPEN |
| CC-01 | `consumeData` | redundant in current corpus | none | **REJECT_REDUNDANT** |
| CC-02 | `provideService` | DEC-14/FR-21 provide positive provider/service evidence; survives consumeService/realize/responsibility/transfer/produce exhaustion | formal G1-G8; compatibility/final signature | **CANDIDATE_TESTED_POSITIVE / NOT_ADMITTED** |
| CC-03 | `storedIn` | FR-26/FR-10 positive evidence; survives current exhaustion | formal G1-G8; compatibility/final signature | **CANDIDATE_TESTED_POSITIVE / NOT_ADMITTED** |
| OBS-OT-01 | operation-target/effect-scope | FR-27 pressure without mutation guarantee | local structure/composition | LEVEL_UNRESOLVED |
| CMD-OP04 | remove `observe.result` | open simplification | integrated review | DEFERRED |
| CMD-OP05 | transition state/value refinement | state identity vs typed value open | integrated review | DEFERRED |

## PR-03 exposure facet

```text
expose
    source wording: PRESENT
    autonomous construct: NOT_JUSTIFIED
    current-corpus result: REPRESENTABLE_BY_COMPOSITION
```

No `expose` candidate ID is allocated.

## Endpoint discipline

```text
endpoint needs independent reuse/qualification
    -> BAReferent candidate identity

method/path/protocol/framework/auth restriction is governed
    -> constrain as applicable

source gives no endpoint/path
    -> do not invent one

source lists some endpoints but not a complete inventory
    -> do not close the endpoint vocabulary
```

## Next review

```text
PR-03 invoke
    vs
PR-10 trigger
```

No current matrix row is an admitted method delta until the required formal gate is complete.
