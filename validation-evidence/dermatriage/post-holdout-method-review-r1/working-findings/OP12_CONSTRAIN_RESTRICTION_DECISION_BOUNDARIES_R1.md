# OP-12 `constrain` — Restriction/Decision Boundaries R1

## Status

`NON-NORMATIVE / OP-12 REVIEW FINDING`

This finding records the SF-04 boundary test performed during OP-12. It does not mutate BA0–BA5.

## Family under test

The review tested whether the following meanings can be collapsed into OP-12:

```text
reusable restriction
admissible domain
required configuration
decision logic
comparison condition
numeric threshold
conditional trigger
bounded selection
negative non-sufficiency
applicability
not-governed absence
```

The result is deliberately selective.

## Stable OP-12 nucleus

```text
target T
    is restricted by
governed reusable/queryable restriction C
```

The operator is useful when `C` describes the admissible/restricted space rather than the logic that
chooses a result or triggers an action.

## Boundary matrix

| Meaning | Same as OP-12? | R1 finding |
|---|---:|---|
| reusable restriction | YES / CORE | direct OP-12 meaning |
| categorical admissible domain | YES | strong positive |
| required governed configuration | YES, when independently meaningful | positive with property/applicability discipline |
| descriptive current configuration | NO AUTOMATIC ADMISSION | source fact alone is insufficient |
| decision mapping | NO | route to OP-14 |
| comparison condition | NO | condition language / PR-05/PR-06 |
| trigger threshold | NO | route pressure to PR-10 / OP-14 |
| bounded ranking/recency selection | NO | PR-13 survives |
| negative non-sufficiency | NO | PR-12 survives |
| applicability qualifier | ORTHOGONAL PRESSURE | PR-14 survives |
| not-governed absence | NO | must not become prohibition |

## Admissible-space vs selection rule

DermaTriage gives a strong same-source control.

```text
Priority ∈ {P1,P2,P3,P4}
```

is a domain restriction.

```text
HIGH + confidence > 0.85 -> P1
```

is result-selection logic.

Collapsing the second into OP-12 would wrongly globalize a local condition.

## Thresholds are semantically typed by use

A literal can participate in different relation families.

Examples:

```text
0.85
    ordered decision condition

10
    prompt-evolution trigger threshold

50
    classifier-adaptation trigger threshold

5%
    pre-adoption tolerance
    or
    post-adoption rollback threshold
```

Therefore a threshold must not be classified by lexical/numeric form alone.

## Same-literal identity rule

The two current `5%` values demonstrate:

```text
literal equality
    does not establish
semantic identity
```

A stable BA must bind values to their governed relation/property/applicability rather than create one
global referent merely because textual literals match.

## Required vs descriptive configuration

Required configuration can be modeled as a restriction when the source imposes it on a governed
target.

Descriptive configuration remains a project fact but does not become OP-12 merely because a value is
recorded.

The key question is:

```text
Does the source restrict the admissible configuration?
```

rather than:

```text
Does the source mention a configuration value?
```

## Negative non-sufficiency

Rules of the form:

```text
A MUST NOT, by itself, be treated as B
```

preserve inference non-sufficiency.

They are not equivalent to:

```text
B is prohibited
```

Therefore OP-12 cannot absorb PR-12.

## Bounded selection

```text
top-5 most similar
20 most recent pertinent
```

require ranking/recency/membership/selection semantics.

A plain `constraintValue = 5` or `20` loses those invariants.

Therefore OP-12 cannot absorb PR-13.

## Applicability

A restriction may be path-, phase-, operation- or population-specific.

Applicability is material because the same property/value may carry different meaning in different
contexts.

OP-12 does not receive a new top-level role in R30. PR-14 remains for integrated testing.

## Scalar representation

The frozen guide's local property + vocabulary representation is strong for categorical domains.

Ordered scalar forms remain under pressure:

```text
>
<=
at most
no worse than
reaches
```

These cases strengthen PR-05/PR-06 and should be tested directly during OP-14 / CL-01 review.

## Central non-equivalence rules

```text
constraint
    != decision rule

constraint
    != comparison condition

constraint
    != trigger

constraint
    != bounded selection

constraint
    != negative non-sufficiency

documented configuration
    != automatically constraint

NOT_GOVERNED
    != negative constraint
```

The relations may coexist in one requirement when independently governed.

## Delete test

OP-12 cannot be deleted because other operators do not recover reusable admissible domains and
configuration restrictions deterministically.

```text
whole-operator redundancy
    FALSIFIED
```

## Minimal operator basis result

The review supports retaining a small operator nucleus while routing specialized semantics to local
structured values, condition constructs and candidate pressures only where demonstrated.

```text
new number / comparator / source verb
    !=
new operator
```

## Disposition

```text
OP-12 core                              KEEP_NO_CHANGE
OP-12 signature                         KEEP_NO_CHANGE
whole-operator redundancy               FALSIFIED
categorical domain restriction          STRONG_POSITIVE
required configuration restriction      STRONG_POSITIVE
documented configuration equivalence    FALSE
decisionRule equivalence                FALSE
threshold equivalence                   FALSE
negative non-sufficiency equivalence    FALSE
bounded-selection equivalence           FALSE
not-governed/prohibited equivalence     FALSE
ordered scalar representation           PARTIALLY_SUPPORTED_PRESSURE_CONFIRMED
PR-05 / PR-06                           SURVIVE
PR-10                                   SURVIVES
PR-12                                   SURVIVES
PR-13                                   SURVIVES
PR-14                                   SURVIVES
new operator                            NOT_JUSTIFIED
```
