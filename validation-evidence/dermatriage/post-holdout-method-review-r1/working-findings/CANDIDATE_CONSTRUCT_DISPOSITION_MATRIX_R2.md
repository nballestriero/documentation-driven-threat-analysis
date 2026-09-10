# Candidate Construct Disposition Matrix R2

## Status

`ACTIVE WORKING ARTIFACT / NON-NORMATIVE`

R2 supersedes R1 for current disposition state. R1 remains historical evidence. R2 incorporates the first candidate-group reconciliation and the R33 lineage repair.

| ID | Topic / candidate | Current evidence/result | Next required test | Current disposition |
|---|---|---|---|---|
| PR-01 | function/process/behavior identity binding / `perform?` | FR-16 absorbable by `produce`; FR-27 does not prove irreducible `perform` | seek actor→behavior meaning surviving full decomposition | **PRESSURE_RETAINED / IRREDUCIBILITY_NOT_DEMONSTRATED** |
| PR-02 | pipeline composition/order | sequencing pressure retained | membership separately from ordering; `precedes` vs `dependOn` | OPEN |
| PR-03 | interface/path/invocation | endpoint/path and invocation pressure retained | distinguish expose, invoke, service use and transfer | **NEXT GROUP** |
| PR-04 | boundary/interaction | boundary semantics open | boundary crossing vs transfer/endpoint semantics | OPEN |
| PR-05 | ordered comparison | ordered/scalar forms exceed equality vocabulary | formal CL-01 review | ROUTE_CL01 |
| PR-06 | scalar/property comparison | typed scalar/property addressing needed | formal CL-01 review | ROUTE_CL01 |
| PR-07 | structured information contract | may be static structure rather than dynamic relation | test L1 structure vs schema and composition | OPEN |
| PR-08 | persistence / storedIn | persistence meaning not yet exhausted | distinguish existence, write, storage, persistence, retention, restoration | **NEXT GROUP** |
| PR-09 | acquisition/refresh | action semantics survive initial boundaries | exhaust transfer/observe/create/transition | OPEN |
| PR-10 | conditional action trigger | survives constrain/decisionRule boundaries | distinguish eligibility, required activation, automatic start, result assignment | **NEXT GROUP** |
| PR-11 | data/evidence consumption | non-destructive use representable; destructive consume not governed | retain historical pressure only | **RECONCILED** |
| PR-12 | negative non-sufficiency | A alone insufficient for B is not NOT(B) | logical/cross-cutting representation | OPEN |
| PR-13 | bounded/ranked selection | top-K/recent-N/best-by-score survive current rule/constraint vocabulary | decompose filter/order/rank/bound/select | **NEXT GROUP** |
| PR-14 | applicability | scoped rule/constraint meaning remains | proposition qualifier/reusable structure first | OPEN |
| CC-01 | `consumeData` | non-destructive sense redundant; destructive sense not governed | no admission test warranted on current evidence | **REJECT_REDUNDANT** |
| CC-02 | `provideService` | distinction plausible; autonomous positive control insufficient | future corpus/completeness recheck | **INSUFFICIENT_EVIDENCE** |
| OBS-OT-01 | operation-target/effect-scope | FR-27 governs target/frozen scope without proving mutation/value difference | local operation structure and existing composition | **LEVEL_UNRESOLVED** |
| CMD-OP04 | remove `observe.result` | open simplification | integrated review | DEFERRED |
| CMD-OP05 | transition state/value refinement | state identity vs typed local value open | integrated review | DEFERRED |

Rejected working hypotheses: generic `consume` is not justified; generic `modify` is rejected because `x_after = f(x_before)` does not establish `x_after != x_before`.

Before method/guidance rewrite, every row must have an explicit disposition and every proposed method delta must pass G1–G8.
