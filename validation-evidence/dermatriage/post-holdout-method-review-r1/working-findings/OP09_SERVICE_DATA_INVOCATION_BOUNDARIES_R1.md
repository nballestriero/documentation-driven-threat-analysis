# OP-09 Working Finding — Service / Data / Invocation Boundaries R1

## Status

`ACCEPTED_REVIEW_FINDING / NON-NORMATIVE`

## Core

`consumeService` is not a generic "uses" relation.

Use it only when the consumed object itself carries governed service/capability meaning.

```text
consumeService(C,S)
    C genuinely uses service/capability S
```

## Strong positive — B4

FR-22 explicitly characterizes B4 as an external service/system consumed by DermaTriage.

This source meaning is not reconstructible from:

```text
transfer of ConsultationData / CaseDocuments
produce of B4CorrelatedTriageOutcome
correlation to B4 consultation
```

alone.

Whole-operator redundancy is therefore falsified.

## Data consumption boundary

FR-18 states:

```text
HistoricalCaseContext consumed by BioMistral
```

The consumed item is data/result, not a service.

This strengthens PR-11 / CC-01 but does not authorize `consumeData` admission during OP-09.

```text
consume data
    != consumeService
```

## Endpoint / invocation boundary

FR-21 explicitly governs invocation of `POST /analyze`.

The endpoint is a concrete interface/path and is not automatically the service term.

Potential future composition:

```text
consumeService(Client, Service)
invokes(Client, Endpoint)
```

only if both meanings are independently source-grounded.

## Technology / realization boundary

FR-18 governs actual use of ChromaDB for indexing/query/retrieval.

That is insufficient by itself to assert:

```text
consumeService(DermaTriage, ChromaDB)
```

because ChromaDB may be:

```text
technology
store
realization
component
```

and existing/adjacent constructs may preserve the source more accurately.

Route to OP-10 `realize` and PR-08 as necessary.

## Stable capability vs concrete interface diagnostic

The interface-replacement test is useful:

```text
if endpoint/technology changes,
does the same service-use meaning survive?
```

If yes, the service/capability and the realization/interface are distinct semantic targets.

This diagnostic cannot invent either identity.

## Internal-component non-inference

A parent system containing or using an internal component does not automatically consume that
component as a service.

```text
participatesIn / realizedBy / contains
    != consumeService
```

unless the source separately governs a genuine service-use relation.

## Ownership / responsibility boundary

Service consumption never transfers ownership or responsibility by itself.

FR-22 provides a strong explicit control: B4 is consumed but is not the owner of the triage
evaluation.

## Provider role

The frozen optional `provider` role remains useful in principle:

```text
consumer [1..*]
service  [1]
provider [0..1]
```

DermaTriage does not sufficiently test an independently distinct provider role.

Disposition:

```text
KEEP FROZEN ROLE
EMPIRICAL COVERAGE NOT SUFFICIENT
```

## Multiple-consumer cardinality

DermaTriage does not sufficiently test whether several consumers should be represented in one
proposition or separate propositions.

Disposition:

```text
KEEP FROZEN [1..*]
NOT_SUFFICIENTLY_TESTED
```

## Candidate `provideService`

R27 records no new method delta.

`provideService?` remains a candidate semantic slot because provider/service meaning may exist
independently from consumption, but existing composition has not yet been exhausted.

Required future boundary work:

```text
OP-10 realize
OP-11 assignResponsibility
PR-01 performs/executes
PR-03 interface/exposure
consumeService.provider
```

## Candidate `consumeData`

Source evidence for functional data/evidence consumption is strong.

However:

```text
source evidence for data consumption
    != proof that a new top-level operator is required
```

PR-11 must still test:

```text
produce.input
observe
transfer
selection/persistence compositions
```

before any method delta.

## Dependency projection

Service consumption may produce a derived dependency edge downstream when the derivation rule is
validated.

Do not duplicate `dependOn` solely for graph convenience.
