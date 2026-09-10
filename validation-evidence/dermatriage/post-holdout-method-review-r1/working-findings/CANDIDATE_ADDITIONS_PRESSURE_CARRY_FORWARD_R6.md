# Candidate Additions / Pressure Carry-Forward R6

## Status

`NON-NORMATIVE / RETAINED FOR LATER PR/CC REVIEW`

R6 carries forward the R5 candidate register and records SF-04 findings from OP-12.

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

## Prior OP-10 / OP-11 findings retained

PR-01 still carries the established boundaries:

```text
realize != performs/executes
assignResponsibility != performs/executes
```

CC-02 `provideService` still survives OP-10/OP-11 exhaustion as autonomous possible meaning but
remains unadmitted.

```text
CC-02 provideService
    CHARACTERIZED
    REALIZE_EXHAUSTION_COMPLETE
    ASSIGN_RESPONSIBILITY_EXHAUSTION_COMPLETE
    AUTONOMOUS_MEANING_SURVIVES
    NOT_ADMITTED
```

Remaining exhaustion continues to involve PR-01 and PR-03.

## OP-12 update — PR-05 ordered comparison vocabulary

DermaTriage contains source-grounded ordered comparison forms including:

```text
confidence > 0.85
accuracy degradation at most 5%
accuracy degradation > 5%
```

The current condition comparison vocabulary does not fully capture this ordered semantics.

OP-12 establishes that these meanings must not be hidden by widening `constrain`.

Status:

```text
PR-05
    SOURCE_EVIDENCE_STRONG
    OP12_BOUNDARY_CONFIRMED
    CHARACTERIZED
    NOT_ADMITTED
    NEXT_EXHAUSTION: OP14_AND_CL01
```

## OP-12 update — PR-06 scalar/property-addressing comparison

The current method supports a local property key and categorical vocabulary for some constraints.

DermaTriage additionally requires typed scalar/property comparison semantics.

Status:

```text
PR-06
    SOURCE_EVIDENCE_STRONG
    EXISTING_PROPERTY_SUPPORT_PARTIAL
    ORDERED_SCALAR_GAP_CONFIRMED
    CHARACTERIZED
    NOT_ADMITTED
    NEXT_EXHAUSTION: OP14_AND_CL01
```

No OP-12 signature mutation is admitted.

## OP-12 update — PR-10 conditional trigger

The source contains:

```text
reaches 10 -> prompt evolution
reaches 50 -> classifier adaptation
```

OP-12 establishes that these thresholds are not automatically reusable global constraints.

The autonomous trigger meaning therefore survives.

Status:

```text
PR-10
    SOURCE_EVIDENCE_STRONG
    NOT_ABSORBED_BY_CONSTRAIN
    SURVIVES
    NOT_ADMITTED
    NEXT_EXHAUSTION: OP14
```

## OP-12 update — PR-12 negative non-sufficiency

The source contains rules where one path fact must not by itself imply another path fact.

This meaning is not equivalent to prohibiting the second fact.

```text
A MUST NOT imply B
    !=
B is prohibited
```

Status:

```text
PR-12
    SOURCE_EVIDENCE_STRONG
    NOT_EQ_NEGATIVE_CONSTRAINT
    SURVIVES
    NOT_ADMITTED
    NEXT_EXHAUSTION: OP14_CL03_CL04_CL05_AS_APPLICABLE
```

## OP-12 update — PR-13 bounded recency/collection selection

The source contains:

```text
top-5 most similar historical cases
20 most recent pertinent clinical corrections
```

A scalar restriction does not preserve ranking, recency, membership or selection semantics.

Status:

```text
PR-13
    SOURCE_EVIDENCE_STRONG
    NOT_REDUCIBLE_TO_CONSTRAINT_VALUE
    SURVIVES
    NOT_ADMITTED
```

## OP-12 update — PR-14 applicability binding

A restriction, comparison, trigger or rule may be limited to a path, phase, operation, reference,
population or other governed context.

OP-12 does not absorb this distinction into arbitrary `constraintValue` prose.

Status:

```text
PR-14
    SOURCE_EVIDENCE_STRONG
    NOT_ABSORBED_BY_CONSTRAIN
    SURVIVES
    NOT_ADMITTED
    NEXT_EXHAUSTION: OP14_AND_SF05
```

## No new constraint-specialized operator

The review does not justify specialized operators for:

```text
threshold
configuration
prohibition
domain
authentication mechanism
numeric bound
```

The current OP-12 nucleus plus structured values remains preferred until integrated review proves
semantic loss.

Status:

```text
NEW_CONSTRAINT_SPECIALIZED_OPERATOR
    NOT_JUSTIFIED
```

## Same-literal observation

The pre-adoption and post-adoption `5%` values remain semantically distinct even when their literal
values coincide.

```text
SAME_LITERAL_NOT_SEMANTIC_IDENTITY
    REVIEW_OBSERVATION
    NO_NEW_PR_OR_CC
```

## Not-governed observation

```text
NOT_GOVERNED != PROHIBITED
```

This remains a source-grounding discipline, not a new operator candidate.

## Minimal operator basis observation

OP-12 reinforces:

```text
existing operator + structured value
    before
new primitive

condition/decision composition
    before
overloading constrain

semantic loss
    required
before candidate admission
```

This remains non-normative until integrated method review.

## General Discovery

The General Discovery Pack remains deferred to the third complete analysis cycle.
