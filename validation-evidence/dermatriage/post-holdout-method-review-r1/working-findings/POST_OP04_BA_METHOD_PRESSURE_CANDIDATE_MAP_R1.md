# Post-OP04 BA Method Pressure Candidate Map R1

## Status

```text
NON_NORMATIVE_WORKING_FINDING
newOperatorsAuthorized: NONE
newBA2ContractAuthorized: NONE
documentationAuthoringMethodMutation: NONE
```

A pressure topic is not automatically a new operator. Test in order: existing construct -> composition -> application correction -> guide clarification -> extension -> genuinely new construct.

## Current operator posture after OP-04

```text
strong/keep: transfer, produce, classify, observe core
whole-operator redundancy hypothesis: create (not proven)
signature-level redundancy hypothesis: observe.result
open/stabilization: decisionRule + condition language
not yet audited: transition, correlate, reference, dependOn, consumeService, realize, assignResponsibility, constrain
```

## Candidate capability map

| Pressure | Problem | Candidate solution family | Posture |
|---|---|---|---|
| PR-01 | actor/capability vs process/behavior identity | behavior/process binding or performs/executes | strong |
| PR-02 | pipeline identity, membership, order | pipeline membership + ordering/precedes | strong |
| PR-03 | invocation vs data flow; endpoint/interface/path | invocation + interface/path binding | strong |
| PR-04 | interaction/boundary relation | boundary binding/crossing | strong |
| PR-05 | ordered comparison | `= != < <= > >=` | strong repeated |
| PR-06 | scalar/property addressing | `BAReferent.property` operands | strong repeated |
| PR-07 | structured information | Information/Data Contract | strong |
| PR-08 | persistence/store relation | persistedIn/storedIn; possibly persist action | strong repeated |
| PR-09 | obtain/acquire/refresh | acquisition/refresh family | retained |
| PR-10 | condition activates action/process | trigger/activateWhen | retained |
| PR-11 | functional information use | data/evidence consumption relation | retained |
| PR-12 | non-implication/non-sufficiency | explicit negative implication/sufficiency form | retained |
| PR-13 | filter/rank/top-N/recency/membership | structured SelectionPolicy | strong |
| PR-14 | applicability context | applicability binding | retained |

## Likely architecture direction

Prefer fewer orthogonal top-level operators plus structured sublanguages/contracts:

```text
REFERENTS
PROPOSITIONS / OPERATORS
STRUCTURED INFORMATION CONTRACTS
CONDITION LANGUAGE
SELECTION POLICIES
CONTEXT BINDINGS
```

This is a working architectural hypothesis, not a normative method change.

## High-value candidate additions

- PR-07 structured information contract: fields/components/cardinality/optionality.
- PR-13 structured selection policy: predicate/ranking/recency/limit/membership.
- PR-03 invocation/interface/path: distinguish endpoint invocation from data flow.
- PR-04 boundary association: preserve governed boundary/interaction relation.
- PR-01 process/behavior binding: distinguish who performs from which governed process/behavior.
- PR-11 data/evidence consumption: distinct from `consumeService`, `observe`, and merely `produce.input`.
- PR-08 persistence/store binding: distinct from `reference`, `produce`, `create`, `observe`.
- PR-10 conditional action trigger: distinct from `decisionRule` result mapping.

## Watch item — data representation/protection

Potential distinction: semantic information vs representation on an interaction (protected/encoded/encrypted/redacted/aggregate).

Status: `WATCH_ONLY`; no PR-15 created. First test composition with `constrain`, `classify`, `realize`, PR-07 and PR-03/04.

## Minimality principle

Prefer `fewer orthogonal operators + explicit structured sublanguages/contracts` over `one BA operator for every source verb`.
