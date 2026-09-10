# DDTA R25 — OP-09 `consumeService` Consolidation R27

## Purpose

R27 closes OP-09 `consumeService` under the semantic-family execution strategy introduced by R26.

Prepared against exact repository baseline:

`89da80e0459ba2a3578c961fb8f6e71b213bb99c`

R27 makes no normative BA0–BA5 change.

## Frozen BA2 R3 contract

```text
consumeService
    consumer -> BAReferent [1..*]
    service  -> BAReferent [1]
    provider -> BAReferent [0..1]
```

Frozen meaning:

```text
Assert actual consumption/use of a capability/service
without transferring ownership/responsibility.
```

## Refined application discipline

Operationally:

```text
consumeService(C,S)
```

means that governed documentation establishes a genuine use relation in which `C` functionally uses
an independently identifiable governed service/capability `S`.

The consumed object must carry service/capability meaning. Do not select `consumeService` merely
because the source mentions something being "used" or "consumed".

## Strong positive control — FR-22

FR-22 explicitly states that B4 remains an external service/system consumed by DermaTriage and does
not become the owner of the triage evaluation.

This preserves an autonomous source fact not recoverable from data transfer, production or
correlation alone.

Candidate representation:

```text
consumeService
    consumer -> DermaTriage
    service  -> B4
```

`provider` is omitted unless a distinct governed provider identity is available.

## Data is not a service

FR-18 explicitly states that `HistoricalCaseContext` is consumed by BioMistral.

This is strong source evidence for data/evidence consumption semantics, but not for
`consumeService`, because the consumed object is information/result rather than a service/capability.

Disposition:

```text
PR-11 / CC-01 consumeData
    source evidence strengthened
    NOT admitted
```

## Endpoint is not a service

FR-21 governs:

```text
DirectClient invokes POST /analyze
POST /analyze invokes DermaTriageTriageProcess
```

and DEC-14 states that the DermaTriage service is exposed through FastAPI/Uvicorn.

The review therefore distinguishes:

```text
service/capability use
    consumeService

concrete endpoint invocation
    PR-03 invocation semantics
```

An endpoint/path is not automatically the `service` term of `consumeService`.

## Technology/component use is not automatically service consumption

FR-18 governs indexing/querying in ChromaDB, but the source does not independently establish a
generic ChromaDB service-consumption proposition.

More-specific/currently adjacent semantics include:

```text
observe/query
produce input/result
realize capability with technology
store/persistence
```

Therefore:

```text
technology T is used
    != automatically
consumeService(..., T)
```

The ChromaDB case is retained for OP-10 `realize`.

## Capability identity test

Before using `consumeService`, ask whether the proposed service is really an independently
identifiable governed service/capability meaning, rather than a relabeled:

```text
technology
component
endpoint
protocol
medium
data artifact
store
```

"Independently identifiable" does not require abstraction. A concrete system such as B4 may be the
service term when the source itself governs it as the consumed service/system.

## Genuine consumer relation

Containment or internal participation is insufficient.

Do not infer:

```text
SystemA consumeService InternalComponentX
```

merely because `InternalComponentX` participates in `SystemA`.

The source must govern a genuine use relation between independently identifiable meanings.

## Relationship to `produce`

`produce` and `consumeService` are orthogonal and composable:

```text
consumeService
    which service/capability is being used?

produce
    who/what makes which governed result available?
```

A service may produce outputs, but service consumption does not imply a production proposition and
production does not imply service consumption.

## Relationship to `transfer`

Service use does not imply content conveyance.

A scenario may independently require:

```text
consumeService(C,S)
transfer(source,destination,content)
```

when both meanings are governed.

## Relationship to `observe`

Read/query semantics may coexist with service consumption but are not equivalent.

Use `observe` for governed inspection/query of existing project state or meaning. Use
`consumeService` only when the service/capability use itself is independently governed.

## Relationship to `dependOn`

Actual service consumption may support a downstream derived dependency edge.

Do not automatically duplicate:

```text
consumeService(C,S)
dependOn(C,S)
```

unless the source separately governs prerequisite meaning.

## Ownership and responsibility

`consumeService` explicitly does not transfer ownership/responsibility.

This is strongly supported by FR-22, which distinguishes B4 consumption from ownership of triage
evaluation.

## Signature review

```text
consumer [1..*]
    lower bound retained
    plural-cardinality behavior not sufficiently tested by DermaTriage

service [1]
    retained

provider [0..1]
    retained
    independent provider role not sufficiently tested by DermaTriage
```

Lack of empirical coverage does not justify removal.

## `provideService?`

R27 does not admit `provideService`.

The fact:

```text
Provider P provides Service S
```

may carry autonomous meaning, but current evidence is insufficient to prove that existing
composition cannot preserve it.

Required exhaustion remains:

```text
OP-10 realize
OP-11 assignResponsibility
PR-01 performs/executes
PR-03 invocation/exposure
consumeService.provider
```

Status:

```text
CC-02 provideService
    CANDIDATE_CHARACTERIZED
    NOT_ADMITTED
```

## Local verdict

```text
OP-09 consumeService
    COMPLETE_GUIDE_CLARIFICATION
    TESTED_POSITIVE_STRONG
    core KEEP_NO_CHANGE
    signature KEEP_NO_CHANGE
    whole-operator redundancy FALSIFIED
    candidate method delta NONE
```

## Next review

`OP-10 realize` within `SF-02 CAPABILITY_REALIZATION_EXECUTION`.
