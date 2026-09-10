# DDTA R25 — OP-12 `constrain` Review

## Review identity

```text
review_id: OP-12
semantic_family: SF-04 RESTRICTION_DECISION_CONDITION
status: COMPLETE_GUIDE_CLARIFICATION
baseline_commit: 3b32afc8961c63a487e131dc0e0277b79aa6e2d9
frozen_method: BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
```

## Construct

```text
constrain
    constraintTarget -> BAReferent [1]
    constraintValue  -> [1..*]
```

Frozen guide meaning:

```text
reusable/queryable restriction
```

The frozen guide permits a structured local form such as:

```text
constraintValue
    property   -> governed semantic key
    vocabulary -> [governed values]
```

## Source coverage

The complete governed DermaTriage baseline was reviewed across urgency and priority domains,
decision thresholds, adaptation triggers, training and retraining configuration, authentication,
bounded retrieval/recency, qualification criteria, rollback criteria, negative non-sufficiency and
explicitly not-governed scopes.

The scan was semantic rather than keyword-only. A source section labelled `Constraints`, a `MUST`,
a `MUST NOT`, a number or a configuration literal was never treated as sufficient evidence by
itself.

## Admission discipline

A candidate OP-12 proposition requires:

```text
T = governed target whose admissible space is restricted
C = independently meaningful governed restriction
```

The source must establish restriction semantics rather than merely a conditional comparison,
trigger, decision branch, descriptive configuration fact, applicability qualifier or documentation
gap.

## Positive control — urgency domain

FR-16 requires an `ImageUrgencyClassification` belonging to:

```text
HIGH | MEDIUM | LOW
```

This is a strong domain constraint.

Conceptual representation:

```text
constrain
    constraintTarget -> ImageUrgencyClassification
    constraintValue
        property   -> urgency
        vocabulary -> [HIGH, MEDIUM, LOW]
```

Final BA naming is deferred to integrated reconstruction.

Disposition:

```text
DOMAIN_RESTRICTION
    STRONG_POSITIVE
```

## Positive control — priority domain

DermaTriage uses the governed operational priority space:

```text
P1 | P2 | P3 | P4
```

Represented as the admissible domain, this is a constraint.

However, the rule selecting one priority from that domain is not itself OP-12.

This same-source distinction is a strong boundary test.

## Decision-rule boundary — confidence > 0.85

DEC-02 / FR-02 governs:

```text
IF urgency = HIGH
AND confidence > 0.85
THEN priority = P1
```

The source does not state that `confidence` must globally be greater than `0.85`.

Therefore:

```text
constrain(confidence, >0.85)
```

would be an invalid scope expansion.

Disposition:

```text
ORDERED_COMPARISON_PRESENT
DECISION_CONDITION_PRESENT
GLOBAL_CONSTRAINT_ABSENT
```

Route the ordered-comparison pressure to PR-05/PR-06 and the mapping itself to OP-14.

## Trigger boundary — thresholds 10 and 50

FR-04 and FR-05 govern activation after accumulated evidence reaches path-specific thresholds.

```text
reaches 10 -> prompt evolution
reaches 50 -> classifier adaptation
```

The numeric values are governed, but their semantic role is trigger condition.

They are not admissible as global OP-12 constraints merely because they are thresholds.

Disposition:

```text
PR-10 CONDITIONAL_TRIGGER
    SURVIVES_OP12
```

## Same literal — pre-adoption vs post-adoption 5%

The corpus gives a particularly strong identity control.

Pre-adoption, `5%` is a tolerated accuracy degradation inside acceptance policy.

Post-adoption, a degradation greater than `5%` participates in the rollback/revocation condition.

The source preserves these meanings as distinct even when the literal is currently equal.

Therefore:

```text
same literal
    !=
same semantic constraint
```

A BA must not merge them solely by numeric equality.

## Required configuration — FR-20

FR-20 governs required baseline-training choices such as:

```text
optimizer = Adam
learning rate = 0.0001
weight decay = 1e-4
warmup = 5 epochs
maximum epochs = 50
patience = 10
batch size = 16
label smoothing = 0.1
```

These clauses provide strong OP-12 evidence where the relevant meaning is a reusable required
configuration restriction.

They also show that `constraintValue` must preserve the addressed property rather than becoming an
untyped bag of literals.

## Required configuration and media — FR-27

FR-27 governs retraining settings and allowed/excluded training input media.

Examples include:

```text
backbone learning rate = 5e-6
classifier learning rate = 3e-5
epochs = 10
class weights = [3.0,2.0,1.0]
CNN input includes applicable JPEG/PNG
CNN input excludes PDF
```

Some clauses are configuration restrictions; other parts of the same requirement describe
behavior.

Do not force the entire requirement into one OP-12 proposition.

## Documented configuration is not enough

The governed documentation explicitly distinguishes source-supported technical facts from complete
normative semantics for every configuration/detail.

A literal such as a documented threshold, model size or implementation setting therefore requires a
separate semantic test:

```text
Is this source establishing a reusable restriction?
```

before OP-12 admission.

Disposition:

```text
DOCUMENTED_CONFIGURATION_EQ_CONSTRAINT
    FALSE
```

## Authentication boundary

FR-24 requires protected DermaTriage administrative operations to use the governed `X-API-Key`
mechanism.

This can support a reusable authentication-mechanism restriction.

FR-25 also governs bearer JWT use for authenticated B4 calls.

However:

```text
token acquisition
token refresh
token presentation
```

remain behavior/interaction meaning rather than automatic OP-12 values.

## Bounded retrieval — top-5

FR-18 requires retrieval of the five most similar historical cases.

This preserves more than a scalar value:

```text
ranking
similarity relation
membership
bounded cardinality
selection
```

Therefore:

```text
constrain(topK, 5)
```

cannot substitute for the full governed meaning.

Disposition:

```text
PR-13
    SURVIVES_OP12
```

## Bounded recency — 20 most recent pertinent corrections

FR-06 requires a sliding bounded evidence set of the 20 most recent pertinent clinical corrections.

The meaning includes:

```text
recency
pertinence/applicability
selection
bounded cardinality
per-cycle evidence set
```

while ordering, deduplication, underfill and reuse remain incompletely governed.

A scalar constraint alone would both lose governed meaning and risk inventing missing semantics.

## Negative non-sufficiency — FR-13/14/15

The source states, in different adaptation dimensions, that a fact from one path must not by itself
be treated as sufficient for another path.

For example:

```text
ActivationConditionOfPathA
    MUST NOT imply
ActivationConditionOfPathB
```

This is not equivalent to prohibiting Path B.

Disposition:

```text
MUST_NOT_EQ_NEGATIVE_CONSTRAINT
    FALSE

PR-12
    SURVIVES_OP12
```

## Not-governed is not prohibited

The corpus contains deliberately ungoverned scopes, including complete specialist-selection rules
and final deployment/promotion authority.

The correct representation is absence/not-governed.

Do not convert such gaps into:

```text
MUST NOT
```

or negative `constrain` propositions.

Disposition:

```text
NOT_GOVERNED_EQ_PROHIBITED
    FALSE
```

## Applicability boundary

A constraint may be valid only for a governed path, operation, phase, population or configuration
scope.

That does not justify hiding applicability inside arbitrary prose in `constraintValue`.

DermaTriage therefore strengthens PR-14 applicability binding while leaving OP-12 signature
unchanged.

## Structured categorical values

The local `property` + `vocabulary` shape works well for categorical admissible domains.

Example:

```text
property   -> urgency
vocabulary -> [HIGH, MEDIUM, LOW]
```

Disposition:

```text
PROPERTY_LOCAL_KEY
    SUPPORTED

STRUCTURED_VOCABULARY
    SUPPORTED
```

## Scalar and ordered representation pressure

The corpus also requires precise handling of:

```text
>
<= / at most
no worse than
reaches threshold
```

These forms are not evidence for widening `constrain` into a general predicate DSL.

They strengthen:

```text
PR-05 ordered comparison vocabulary
PR-06 scalar/property-addressing comparison
```

for OP-14 / CL-01 / integrated reconciliation.

Disposition:

```text
ORDERED_SCALAR_RANGE_REPRESENTATION
    PARTIALLY_SUPPORTED
    PRESSURE_CONFIRMED
```

## Delete test

Remove OP-12 while retaining every other frozen operator and candidate meaning.

The remaining BA can preserve classifications, production, dependencies, realization and decision
logic, but cannot deterministically recover reusable allowed-value domains or required configuration
restrictions.

Whole-operator redundancy is therefore falsified.

## Projection test

OP-12 enables deterministic views such as:

```text
admissible-value/domain view
required-configuration view
security/authentication restriction view
compliance restriction view
restriction-gap view
```

without proliferating specialized top-level operators.

## Minimal operator basis result

OP-12 supports the following non-normative working principle:

```text
A new literal, comparator, source verb or configuration field
does not by itself justify a new operator.

First test:
1. existing operator instance;
2. structured value within the operator;
3. composition/projection with condition/decision constructs.

Escalate only when material governed meaning is otherwise lost.
```

## Q1–Q20 result summary

| Q | Test | Result |
|---|---|---|
| Q1 | identifiable constraint target | PASS |
| Q2 | reusable restriction meaning | PASS |
| Q3 | property addressing | PASS |
| Q4 | value/domain grounding | STRONG PASS |
| Q5 | source grounding | STRONG PASS |
| Q6 | reusability | PASS |
| Q7 | queryability | STRONG PASS |
| Q8 | condition boundary | STRONG PASS / DISTINCT |
| Q9 | decisionRule boundary | STRONG PASS / DISTINCT |
| Q10 | ordered comparison | PRESSURE CONFIRMED |
| Q11 | threshold semantics | STRONG BOUNDARY |
| Q12 | configuration semantics | STRONG BOUNDARY |
| Q13 | applicability | PRESSURE CONFIRMED |
| Q14 | prohibition semantics | PASS |
| Q15 | not-governed vs prohibited | STRONG PASS |
| Q16 | structured value | PARTIAL PASS |
| Q17 | scalar/property addressing | PARTIAL PASS |
| Q18 | delete test | WHOLE-OPERATOR REDUNDANCY FALSIFIED |
| Q19 | projection test | STRONG PASS |
| Q20 | final admission | PASS |

See `CONSTRAIN_QUESTION_PACK_R1.md`.

## Local verdict

```text
reviewStatus: COMPLETE_GUIDE_CLARIFICATION
reviewClosure: COMPLETE
empiricalStatus: TESTED_POSITIVE
testCoverage:
    TESTED_POSITIVE
    TESTED_NEGATIVE
    TESTED_BOUNDARY
operatorCoreDisposition: KEEP_NO_CHANGE
wholeOperatorRedundancy: FALSIFIED
signatureDisposition: KEEP_NO_CHANGE
reusableRestrictionSemantics: SUPPORTED
domainConstraint: STRONG_POSITIVE
requiredConfigurationConstraint: STRONG_POSITIVE
documentedConfigurationAutomaticallyConstraint: FALSE
conditionEquivalentToConstraint: FALSE
decisionRuleEquivalentToConstraint: FALSE
thresholdAutomaticallyConstraint: FALSE
notGovernedEquivalentToProhibition: FALSE
negativeNonSufficiencyEquivalentToConstraint: FALSE
boundedSelectionEquivalentToConstraint: FALSE
propertyLocalKey: SUPPORTED
structuredVocabulary: SUPPORTED
orderedScalarRangeRepresentation: PARTIALLY_SUPPORTED_PRESSURE_CONFIRMED
candidateMethodDelta: NONE
```

## Next existing-operator review

`OP-14 decisionRule`
