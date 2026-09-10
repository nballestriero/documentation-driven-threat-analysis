# Continuation after R30

## Baseline discipline

R30 is prepared against:

`3b32afc8961c63a487e131dc0e0277b79aa6e2d9`

After commit/push, the resulting R30 commit SHA becomes the exact next baseline.

Do not begin formal OP-14 consolidation from an assumed post-R30 SHA.

## Closed operator

```text
OP-12 constrain
    COMPLETE_GUIDE_CLARIFICATION
    TESTED_POSITIVE
    TESTED_NEGATIVE
    TESTED_BOUNDARY
    core KEEP_NO_CHANGE
    signature KEEP_NO_CHANGE
    whole-operator redundancy FALSIFIED
```

## Core rule

```text
constrain(T,C)

T = governed target of a restriction
C = governed reusable/queryable restriction
```

Use OP-12 for the admissible space, domain or independently meaningful restriction.

Do not use it merely because the source contains `MUST`, `MUST NOT`, a number, a threshold, a
comparison or a configuration literal.

## Strong positives

```text
ImageUrgencyClassification.urgency ∈ {HIGH, MEDIUM, LOW}
Priority ∈ {P1, P2, P3, P4}
required training/retraining configuration restrictions
governed authentication-mechanism restriction
```

Final BA referent/property naming remains deferred to integrated reconstruction.

## Critical distinction

```text
constrain
    describes allowed/restricted space

decisionRule
    maps governed condition/input to governed result
```

The two meanings may appear in the same requirement and must be extracted separately when both are
independently governed.

## Threshold controls

```text
confidence > 0.85
reaches 10
reaches 50
accuracy degradation > 5%
```

are not automatically OP-12 propositions.

Their semantic role must be determined from the source:

```text
restriction
comparison condition
trigger
qualification criterion
rollback condition
```

before BA admission.

## Same-literal control

The current `5%` literals used for pre-adoption tolerance and post-adoption rollback remain
semantically distinct.

```text
same number != same governed meaning
```

Do not canonicalize literals across different semantic roles without source evidence.

## Configuration control

```text
documented configuration
    != automatically
constraint

required governed configuration
    may be
constraint
```

Keep descriptive technical facts separate from reusable normative restrictions.

## Negative controls

```text
MUST NOT
    != automatically
negative constrain

NOT_GOVERNED
    !=
PROHIBITED

A MUST NOT imply B
    !=
B is forbidden
```

PR-12 therefore survives OP-12.

## Bounded-selection control

```text
top-5 most similar
20 most recent pertinent
```

cannot be reduced to `value = 5` or `value = 20` without losing ranking/recency/membership meaning.

PR-13 survives OP-12.

## Property/scalar pressure

The current local property + vocabulary pattern is useful for categorical restrictions.

Ordered/scalar cases strengthen:

```text
PR-05 ordered comparison vocabulary
PR-06 scalar/property-addressing comparison
```

but R30 does not admit a method mutation.

Their final disposition must be tested against OP-14 and the condition-language review.

## Remaining existing operator

After R30 exactly one existing-operator review remains:

```text
OP-14 decisionRule
```

OP-13 `classify` remains already complete.

OP-03 `create` remains complete-deferred-with-reason / NOT_TESTED.

OP-05 `transition` remains review-complete with deferred method-delta candidate.

## Condition language remains separate

Closing OP-14 will close the existing-operator audit, not automatically the condition-language audit.

Still separate:

```text
CL-01 comparison
CL-02 satisfies
CL-03 allOf
CL-04 anyOf
CL-05 not
```

OP-14 may characterize pressures affecting these constructs, but must not silently dispose of them
unless the review evidence actually performs those tests and the ledger records them explicitly.

## Other work still pending after existing operators

```text
CL-01..CL-05 disposition
pressure/candidate disposition
integrated method revision
final DermaTriage BA
third-cycle General Discovery Pack
publication/thesis packaging as applicable
```

## Next review

`OP-14 decisionRule` within `SF-04 RESTRICTION_DECISION_CONDITION`.

The review should use at least these governed controls:

```text
P-scale mapping:
    HIGH + confidence > 0.85 -> P1
    HIGH otherwise          -> P2
    MEDIUM                  -> P3
    LOW                     -> P4

prompt trigger:
    reaches 10 -> prompt evolution

classifier trigger:
    reaches 50 -> classifier adaptation

evidence qualification:
    agrees == False -> qualifying classifier evidence

supervision mapping:
    P1/P2 -> HIGH
    P3    -> MEDIUM
    P4    -> LOW

acceptance qualification:
    all governed comparative criteria satisfied -> qualified

post-adoption degradation:
    > 5% -> rollback/revocation support
```

The review must distinguish the operator core from CL-01..CL-05 and from PR-05/06/10/12/14.
