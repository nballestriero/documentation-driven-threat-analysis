# Candidate Additions / Pressure Carry-Forward R3

## Status

`CANDIDATE SEMANTIC PRESSURE REGISTER / NON-NORMATIVE`

R3 supersedes the R26/R2 carry-forward for active execution status while preserving all prior
candidate history.

Nothing in this artifact is an admitted BA operator, role, condition primitive or project truth.

## Governance

```text
existing construct exhaustion
    -> composition
    -> source-supported missing semantic slot
    -> candidate characterization/question pack
    -> G1-G8 only when admission becomes possible
```

Synthetic examples are diagnostic only.

## CC-01 / PR-11 — `consumeData?`

### Current evidence

DermaTriage directly exercises functional data/evidence consumption:

```text
HistoricalCaseContext consumed by BioMistral
FR-19 multi-source synthesis consumes governed inputs
FR-05 consumes evidence qualified according to FR-07
FR-27 uses correction/image evidence for retraining
```

### Current status

```text
candidate: consumeData
owner: PR-11
status: CANDIDATE_CHARACTERIZED
sourceEvidence: STRONG
admissionStatus: NOT_ADMITTED
```

### Why not admitted

Existing composition still requires complete pressure-level exhaustion:

```text
produce.input
observe
transfer
selection/persistence semantics
```

The evidence proves the semantic family exists; it does not yet prove a new top-level operator is
minimal.

### Key boundary

```text
consume data/evidence
    != consumeService
```

## CC-02 — `provideService?`

### Candidate meaning

Potential independent fact:

```text
Provider P provides Service/Capability S
```

### Current evidence

DermaTriage governs service exposure and consumed external service/system semantics, but does not yet
provide sufficient evidence that independent provision cannot be represented by existing
composition.

### Current status

```text
candidate: provideService
status: CANDIDATE_CHARACTERIZED
sourceEvidence: INSUFFICIENT_FOR_INDEPENDENT_CONSTRUCT
admissionStatus: NOT_ADMITTED
```

### Required exhaustion

```text
consumeService.provider
OP-10 realize
OP-11 assignResponsibility
PR-01 performs/executes
PR-03 invocation/exposure
```

## Existing PR topics retained

```text
PR-01 function/process/behavior identity binding
PR-02 pipeline composition/order
PR-03 interface/path/invocation association
PR-04 boundary/interaction association
PR-05 ordered comparison vocabulary
PR-06 scalar/property-addressing comparison
PR-07 structured data/information contract
PR-08 artifact/store/persistence
PR-09 acquisition/refresh
PR-10 conditional action trigger
PR-11 data/evidence consumption
PR-12 negative implication/non-sufficiency
PR-13 bounded recency/collection selection
PR-14 configuration applicability
```

All prior boundaries remain in force.

## Current semantic-family queue

```text
SF-01
    OP-09 closed
    CC-01 / CC-02 retained
    PR-03 / PR-07 / PR-08 / PR-11 retained

SF-02
    next: OP-10 realize
    revisit capability vs technology
    revisit technical/library dependency
    revisit service provision/exposure

SF-03
    OP-11 assignResponsibility
    provider vs owner vs responsible vs performer

SF-04
    OP-12 constrain
    OP-14 decisionRule
    CL-01..CL-05
    PR-05 / PR-06 / PR-10 / PR-12 / PR-14

SF-05
    PR-08 / PR-09 / PR-14

SF-06
    PR-02 / PR-03 / PR-04
```

General Discovery Pack remains deferred to the third complete analysis cycle.
