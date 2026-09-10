# Candidate Additions / Pressure Carry-Forward R2

## Status

`CANDIDATE SEMANTIC PRESSURE REGISTER / NON-NORMATIVE`

R2 supersedes R1 for active review routing while preserving R1 as immutable historical evidence.

Nothing in this register is an admitted BA operator, role, condition primitive or project truth.

## Execution governance

Use semantic-family review under `DDTA_R25_POST_HOLDOUT_OPERATOR_COMPLETE_REVIEW_WORK_PLAN_R3.md`.

```text
characterize adjacent candidates during family review
BUT
admit no method delta until existing constructs/compositions are exhausted
and G1–G8 are satisfied
```

Synthetic examples may clarify semantics but are not governed evidence and cannot satisfy G1.

## Existing PR queue

### PR-01 — function/process/behavior identity binding

Candidate vocabulary: `performs`, `executes`.

Review in SF-02/SF-03 with `realize`, `produce.actor`, `consumeService.provider` and responsibility.

### PR-02 — pipeline composition/order

Candidate vocabulary: `memberOfPipeline`, `precedes`.

Boundary: `precedes != dependOn`.

### PR-03 — interface/path/invocation association

Candidate vocabulary: `invokes`; also test service exposure/path membership.

Boundary: endpoint membership != invocation; endpoint != service automatically.

### PR-04 — boundary/interaction association

Candidate families: `interactsAcross`, `crossesBoundary`, boundary endpoint.

Boundary: boundary crossing != ordinary transfer unless boundary role is preserved.

### PR-05 — ordered comparison vocabulary

Likely CL-01 pressure; test `< <= > >= = !=` before top-level constructs.

### PR-06 — scalar/property-addressed comparison

Test property/value operand shape; likely condition-language/value structure.

### PR-07 — structured data/information contract

Test field membership, required/optional fields, domains and reusable information contracts.

### PR-08 — artifact/store/persistence association

Candidate vocabulary: `persistedIn`, `storedIn`, `trackedIn`.

Boundary: `persistedIn != reference`.

### PR-09 — acquisition/refresh semantics

Candidate vocabulary: `acquire`, `refresh`, `renew`.

Exhaust transfer/observe/produce/lifecycle first.

### PR-10 — conditional action trigger

Candidate vocabulary: `triggers`, `activatedWhen`.

Boundary: trigger != decisionRule.

### PR-11 — data/evidence consumption

Candidate semantic slot:

```text
CC-01 consumeData ?
```

Working distinction:

```text
observe       = inspect/read/query existing meaning
produce.input = input contributes to a governed result
consumeData ? = information/evidence is functionally used
consumeService = capability/service is actually used
```

Status after R26:

```text
CANDIDATE_CHARACTERIZED
ACTIVE_IN_SF-01
NO_METHOD_ADMISSION
```

### PR-12 — negative implication/non-sufficiency

Candidate vocabulary: `doesNotImply`, `notSufficientFor`.

Boundary: negative non-sufficiency != ordinary `constrain`.

### PR-13 — bounded recency/collection selection

Test membership, recency, bounded window, reuse/overlap, deduplication and scope. May be a policy/structured mechanism rather than top-level operator.

### PR-14 — configuration applicability

Candidate vocabulary: `appliesTo`, `applicableVersion`, `configurationFor`.

Boundary: applicability != reference.

## Newly characterized candidate — CC-02 `provideService?`

### Motivation

Current `consumeService` can record an optional provider **inside an actual service-consumption proposition**:

```text
consumer -> C
service  -> S
provider -> P [optional]
```

A general method may also encounter governed source truth of the form:

```text
Provider P provides Service/Capability S
```

with no governed consumer yet.

### Do not admit yet

Before any new construct, exhaust:

```text
consumeService.provider
realize
assignResponsibility
PR-01 performs/executes
PR-03 service exposure
```

Required distinctions:

```text
provides != owns
provides != responsibleFor
provides != performs
provides != realizes
```

### Current status

```text
candidateId: CC-02
candidateName: provideService
status: CANDIDATE_CHARACTERIZED
currentCorpusEvidence: TO_BE_TESTED_IN_SF-01_SF-02_SF-03
normativeMethodDelta: NONE
```

If DermaTriage cannot test autonomous service provision, create/retain the question pack and mark `CANDIDATE_NOT_TESTED`.

## Producer–consumer architecture hypothesis

Do not add a monolithic `producerConsumer` operator.

Test composition:

```text
DATA FLOW
produce -> data/result -> consumeData ?

SERVICE FLOW
provideService ? / realize / responsibility -> service -> consumeService

INTERMEDIARY
queue/topic/store -> transfer / persistence / selection / service as source-grounded
```

The queue/topic/store is not automatically the payload and not automatically a service.

## Remaining existing operators before full pressure admission

```text
OP-09 consumeService
OP-10 realize
OP-11 assignResponsibility
OP-12 constrain
OP-14 decisionRule
```

OP-13 is complete. OP-01..OP-08 are complete with recorded boundary/reconciliation carry-forward.

## Condition language still to review

```text
CL-01 comparison
CL-02 satisfies
CL-03 allOf
CL-04 anyOf
CL-05 not
```

## Final candidate disposition rule

For every PR/CC candidate, final status must be explicit:

```text
existing construct sufficient
composition sufficient
application correction
 guide clarification
extension required
new construct required
rejected/project-specific
NOT_TESTED / insufficient evidence
```

## General Discovery Pack

Execution remains deferred to the third complete analysis cycle.
