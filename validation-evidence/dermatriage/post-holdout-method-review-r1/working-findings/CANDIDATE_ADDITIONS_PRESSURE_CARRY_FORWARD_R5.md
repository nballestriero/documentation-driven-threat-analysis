# Candidate Additions / Pressure Carry-Forward R5

## Status

`NON-NORMATIVE / RETAINED FOR LATER PR/CC REVIEW`

R5 carries forward the prior candidate register and records SF-03 findings from OP-11.

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

## OP-10 carry-forward — PR-01

The governed source states that EfficientNet-B4 executes image-based urgency classification.

The prior OP-10 result remains:

```text
realize
    != performs/executes

PR-01
    SOURCE_EVIDENCE_STRONG
    CHARACTERIZED
    NOT_ADMITTED
```

## OP-11 update — PR-01 boundary strengthened

OP-11 establishes an additional non-equivalence:

```text
performs/executes
    != assignResponsibility
```

A performer may execute a function without being the responsible/accountable party for that
function.

PR-01 therefore survives both OP-10 and OP-11 exhaustion.

## OP-11 update — authority does not create a new candidate

The governed corpus distinguishes responsibility and authority, but the existing
`responsibilityKind` preserves the distinction without demonstrated loss.

```text
authorityAsResponsibilityKind
    SUPPORTED

assignAuthority
    NOT_JUSTIFIED
```

No `assignAuthority` CC is created.

## OP-11 update — ownership remains corpus-limited

Governance/accountability ownership may fit an ownership-like `responsibilityKind`.

Generic legal/asset/property ownership remains:

```text
NOT_TESTED
```

Current evidence does not justify a generic `owns` candidate.

No ownership CC is created.

## CC-02 `provideService` survives OP-11 exhaustion

OP-11 rules out the equivalence:

```text
provides Service
    ==
is responsible for Service
```

A provider relation can preserve autonomous project meaning even when responsibility lies
elsewhere.

Status:

```text
CC-02 provideService
    CHARACTERIZED
    ASSIGN_RESPONSIBILITY_EXHAUSTION_COMPLETE
    RESPONSIBILITY_EQUIVALENCE_FALSIFIED
    AUTONOMOUS_MEANING_SURVIVES
    NOT_ADMITTED
```

Remaining exhaustion before final disposition:

```text
PR-01 performs/executes
PR-03 invocation/exposure
```

The existing `consumeService.provider` role and OP-10 `realize` boundary remain part of the prior
exhaustion record and are not reopened.

## Responsibility-kind identity observation

The current signature requires:

```text
responsibilityKind -> BAReferent [1]
```

Current DermaTriage evidence does not determine whether all kinds require independent BA identity or
whether some future cases could use controlled typed local values without loss.

Status:

```text
NOT_SUFFICIENTLY_TESTED
RETAIN_AS_REVIEW_OBSERVATION
NO_PR_OR_CC_CREATED
```

## Multi-party responsibility observation

The current signature permits:

```text
responsibleParty [1..*]
```

Current evidence does not determine whether plurality means independent, joint, shared or collective
responsibility.

Do not infer composition from cardinality.

Status:

```text
NOT_SUFFICIENTLY_TESTED
RETAIN_AS_REVIEW_OBSERVATION
NO_PR_OR_CC_CREATED
```

## Negative-governance encoding observation

The guide meaning allows placement or negation of responsibility/authority, but OP-11 has no
operator-local `polarity` role.

R5 does not create a new candidate. If integrated BA reconstruction shows a deterministic
representation gap, route the issue to cross-cutting proposition semantics.

Status:

```text
OBSERVATION_ONLY
NO_INVENTED_POLARITY
NO_PR_OR_CC_CREATED
```

## Minimal operator basis observation

OP-11 supports the working discipline:

```text
existing operator
    before
new operator

existing operator + kind
    before
lexically specialized operator

composition/projection
    before
new primitive
```

A candidate is justified by demonstrated semantic loss, not by a new verb in the source.

This is a review principle for integrated consideration, not an admitted method rule in R5.

## General Discovery

The General Discovery Pack remains deferred to the third complete analysis cycle.
