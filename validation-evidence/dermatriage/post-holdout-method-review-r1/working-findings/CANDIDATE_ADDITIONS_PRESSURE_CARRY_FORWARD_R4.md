# Candidate Additions / Pressure Carry-Forward R4

## Status

`NON-NORMATIVE / RETAINED FOR LATER PR/CC REVIEW`

R4 carries forward the prior candidate register and records SF-02 findings from OP-10.

No candidate in this file is admitted BA method.

## Existing candidates retained

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
PR-10 conditional trigger
PR-11 data/evidence consumption
PR-12 negative non-sufficiency
PR-13 bounded recency/collection selection
PR-14 applicability binding

CC-01 consumeData
CC-02 provideService
```

## OP-10 update — PR-01 strengthened

The governed source states that EfficientNet-B4 **executes** image-based urgency classification.

The OP-10 review establishes:

```text
realize
    != performs/executes
```

Therefore PR-01 has strong source evidence for an execution/performer relation.

Status:

```text
PR-01
    SOURCE_EVIDENCE_STRONG
    CHARACTERIZED
    NOT_ADMITTED
```

Required future questions include:

```text
what is the performed/executed meaning?
who/what is the performer?
is the target a behavior, process, function or capability?
does produce already preserve the needed fact?
does realize already preserve a distinct abstraction/implementation fact?
```

## OP-10 update — PR-03 retained

FastAPI/Uvicorn exposure and `POST /analyze` invocation are not automatically realization.

PR-03 remains strongly relevant.

## CC-02 provideService remains unadmitted

OP-10 does not eliminate the possible autonomous meaning:

```text
Provider P provides Service S
```

but it also does not prove a new construct is needed.

Remaining exhaustion:

```text
OP-11 assignResponsibility
PR-01 performs/executes
PR-03 invocation/exposure
consumeService.provider
realize
```

OP-10 exhaustion contribution is now complete.

## Composite realization observation

FR-18 exposes a potential future distinction:

```text
multiple independent realizations
vs
multiple constituents of one realization
```

This is **not** promoted to a new PR/CC because current source evidence does not show that the
distinction must be first-class.

Status:

```text
COMPOSITE_REALIZATION_SEMANTICS
    NOT_SUFFICIENTLY_TESTED
    RETAIN_AS_REVIEW_OBSERVATION
```

## General Discovery

The General Discovery Pack remains deferred to the third complete analysis cycle.
