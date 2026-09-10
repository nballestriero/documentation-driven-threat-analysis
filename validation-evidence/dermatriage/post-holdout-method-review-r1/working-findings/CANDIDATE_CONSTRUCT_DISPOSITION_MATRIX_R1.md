# Candidate Construct Disposition Matrix R1

## Status

`ACTIVE WORKING ARTIFACT / NON-NORMATIVE`

Baseline at creation:

```text
ca99122b2f628f169bed85e04e731c8f3f89ca3c
```

Purpose: ensure every retained pressure, explicit candidate and deferred method delta receives an explicit
disposition before any BA method or guide rewrite.

No entry in this matrix is admitted method merely because it appears here.

## Disposition vocabulary

```text
ABSORBED_BY_EXISTING_OPERATOR
CONTROLLED_KIND_OR_VALUE
LOCAL_CONDITION_LANGUAGE_EXTENSION
REUSABLE_CROSS_CUTTING_STRUCTURE
COMPOSITION_OR_PROJECTION
APPLICATION_CORRECTION
METHOD_DELTA_TO_EXISTING_OPERATOR
NEW_TOP_LEVEL_OPERATOR
DEFER_NOT_TESTED
REJECT_REDUNDANT
REJECT_FALSE_SEMANTICS
NOT_GOVERNED
```

## Required evidence fields per item

Every item must eventually record:

```text
SOURCE MEANING
SOURCE CASES
CURRENT REPRESENTATION
PRESERVED MEANING
LOST / DISTORTED MEANING
NEAREST EXISTING CONSTRUCT
ABSORPTION TEST
COMPOSITION TEST
PROJECTION TEST
DELETE TEST
PROVISIONAL SOLUTION
SEMANTIC LEVEL
EVIDENCE STATUS
G1-G8 STATUS
FINAL DISPOSITION
```

## Initial matrix

| ID | Topic / candidate | Why it exists | Nearest current construct(s) | Provisional solution to test | Current status |
|---|---|---|---|---|---|
| PR-01 | function/process/behavior identity binding | governed execution/perform semantics survived `realize` and `assignResponsibility` boundaries | `produce`, `realize`, `assignResponsibility` | `perform(actor, behavior)` or composition | OPEN / SOURCE_EVIDENCE_STRONG |
| PR-02 | pipeline composition/order | governed sequential stages and order are not equivalent to dependency | `dependOn`, `realize` | small `contains/memberOf` + `precedes` relations or structure | OPEN / SF06 |
| PR-03 | interface/path/invocation association | endpoint/path identity and invocation can matter independently of service consumption | `consumeService`, `transfer`, `realize` | `invoke` / interface-operation relation or composition | OPEN / STRENGTHENED |
| PR-04 | boundary/interaction association | crossing/using a governed boundary can be material beyond ordinary transfer | `transfer`, `consumeService` | `interactsThrough` or boundary qualifier | OPEN / SF06 |
| PR-05 | ordered comparison vocabulary | `> 0.85`, `at most 5%`, `> 5%`, no-worse-than exceed equals/notEquals | CL-01 `comparison` | extend controlled `comparisonKey` vocabulary | OPEN / ROUTE_CL01 |
| PR-06 | scalar/property-addressing comparison | governed typed scalar comparison needs local property addressing | CL-01 `comparison`, `constrain` structured value | typed scalar + property representation in CL-01 | OPEN / ROUTE_CL01 |
| PR-07 | structured data/information contract | governed fields/domains/contracts can be static structure rather than dynamic relation | `classify`, `constrain` | reusable structured information/value contract | OPEN |
| PR-08 | artifact/store/persistence | persisted/stored-in meaning is not obviously produce/reference/transition | `produce`, `reference`, `transition` | `persist(content, store)` / `storedIn` | OPEN / SF05 |
| PR-09 | acquisition/refresh | acquire/refresh/renew action semantics survive observation/state boundaries | `observe`, `create`, `transition`, `transfer` | behavior relation or method-neutral acquisition/refresh construct | OPEN / SF05 |
| PR-10 | conditional action trigger | threshold condition activates behavior; not result-selection decisionRule | `decisionRule`, CL constructs | local action consequence, trigger structure, or top-level `trigger` | OPEN / SOURCE_EVIDENCE_STRONG |
| PR-11 | data/evidence consumption | consuming information is not service consumption and not always observation | `observe`, `produce.input`, `consumeService` | CC-01 `consumeData` | OPEN / SOURCE_EVIDENCE_STRONG |
| PR-12 | negative implication/non-sufficiency | `A MUST NOT by itself imply B` means insufficiency, not `NOT B` | CL-03..CL-05, `constrain`, `decisionRule` | logical/governance non-sufficiency structure | OPEN / SOURCE_EVIDENCE_STRONG |
| PR-13 | bounded recency/collection selection | top-5, recent-20, best-checkpoint preserve ranking/selection semantics | `constrain`, `decisionRule`, CL-01 | reusable selection/ranking structure or `select` | OPEN / SOURCE_EVIDENCE_STRONG |
| PR-14 | configuration/applicability binding | rules/constraints/thresholds are scoped to path/phase/reference/context | `reference`, `constrain`, rule-local context | reusable applicability qualifier/structure | OPEN / SOURCE_EVIDENCE_STRONG |
| CC-01 | `consumeData` | explicit candidate for autonomous data/evidence consumption semantics | `observe`, `produce.input`, `consumeService` | test candidate signature and G1-G8 | CANDIDATE_CHARACTERIZED / NOT_ADMITTED |
| CC-02 | `provideService` | provision relation survives realization/responsibility exhaustion | `consumeService.provider`, `realize`, `assignResponsibility` | test provider-service proposition without invented consumer | CANDIDATE_CHARACTERIZED / NOT_ADMITTED |
| CMD-OP04 | remove `observe.result` | prior application review questioned whether optional result belongs to observe nucleus | OP-04 `observe` | signature simplification vs retain/defer | DEFERRED |
| CMD-OP05 | admit transition state/value refinement | prior review exposed state/value representation pressure | OP-05 `transition` | existing-operator method delta vs local structured state | DEFERRED |

## Candidate names that are diagnostic only

The following names are working hypotheses, not allocated CC identities and not admitted constructs:

```text
perform
invoke
persist
trigger
select
precedes
contains / memberOf
interactsThrough
```

A name becomes a candidate construct only after the pressure review demonstrates an independently
governed semantic slot that remains lost after existing-construct exhaustion.

## First disposition target

```text
CL-01 comparison
    -> resolves/clarifies PR-05
    -> resolves/clarifies PR-06
```

After CL-01, update this matrix before moving to CL-02.

## Closure rule

This matrix is complete only when every row has one explicit final disposition and any admitted method
delta has passed G1-G8. No row may disappear because another review happened to touch adjacent meaning.
