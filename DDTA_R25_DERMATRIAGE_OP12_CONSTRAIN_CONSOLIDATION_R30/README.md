# DDTA R25 — OP-12 `constrain` Consolidation R30

## Purpose

R30 closes the source-complete review of OP-12 `constrain` under semantic family
`SF-04 RESTRICTION_DECISION_CONDITION`.

Prepared against exact baseline:

`3b32afc8961c63a487e131dc0e0277b79aa6e2d9`

R30 makes no normative BA0–BA5 mutation and no documentation-authoring-method mutation.

## Frozen BA2 R3 contract

```text
constrain
    constraintTarget -> BAReferent [1]
    constraintValue  -> [1..*]
```

Frozen guide meaning:

```text
reusable/queryable restriction
```

The guide also permits structured local values such as:

```text
constraintValue
    property   -> governed semantic key
    vocabulary -> [governed admissible values]
```

R30 keeps this operator narrow. It does not turn every `MUST`, number, threshold, comparison,
configuration value or section labelled "Constraints" into an OP-12 proposition.

## Core application discipline

Use `constrain` when the governed source establishes an independently meaningful restriction on a
target, property, value, domain or admissible space.

A candidate OP-12 proposition should preserve:

```text
T = identifiable governed constraint target
C = governed reusable/queryable restriction applied to T
```

Strong positive forms include:

```text
property/domain restriction
required configuration restriction
admissible input/value restriction
explicitly governed prohibition when the prohibited space itself is the reusable meaning
```

Do not use OP-12 merely because the source contains restrictive-looking language.

## Strong positive — governed domains

DermaTriage requires `ImageUrgencyClassification` to belong to:

```text
HIGH | MEDIUM | LOW
```

This is a canonical domain restriction and is representable conceptually as:

```text
constrain
    constraintTarget -> ImageUrgencyClassification
    constraintValue
        property   -> urgency
        vocabulary -> [HIGH, MEDIUM, LOW]
```

Final BA referent and property naming remains subject to integrated reconstruction.

The P-scale similarly exposes an admissible domain:

```text
P1 | P2 | P3 | P4
```

when represented as the allowed priority space.

## Critical boundary — admissible domain vs result selection

The same governed documentation may contain both:

```text
priority ∈ {P1,P2,P3,P4}
```

and:

```text
IF urgency = HIGH
AND confidence > 0.85
THEN priority = P1
```

The first is a reusable restriction.

The second is decision logic.

Disposition:

```text
CONSTRAINT
    describes admissible space

DECISION_RULE
    selects a result under governed conditions
```

OP-12 and OP-14 are therefore orthogonal rather than redundant.

## Threshold boundary

A numeric threshold is not automatically a constraint.

DermaTriage includes:

```text
confidence > 0.85
10 accumulated corrections -> prompt-evolution activation
50 qualifying corrections  -> classifier-adaptation activation
```

These literals participate in local conditions or trigger semantics.

R30 rejects automatic extraction such as:

```text
constrain(confidence, >0.85)
```

when the source actually means:

```text
IF confidence > 0.85 THEN choose/trigger/result ...
```

Disposition:

```text
THRESHOLD_PRESENT
    !=
CONSTRAINT_PRESENT
```

## Same literal, different semantics

DermaTriage uses a current `5%` literal in at least two materially different contexts:

```text
pre-adoption:
    permitted accuracy degradation tolerance

post-adoption:
    rollback/revocation trigger threshold
```

The governed source explicitly preserves these as semantically distinct even when the current
literal happens to coincide.

Therefore:

```text
same literal
    !=
same governed meaning

numeric equality
    !=
semantic identity
```

Do not create a universal `5% constraint` referent merely from literal equality.

## Configuration boundary

Documented configuration is not automatically governed restriction.

A source-supported configuration fact may be descriptive or implementation-specific without
establishing a reusable normative restriction.

By contrast, FR-20 and FR-27 contain required training/retraining configuration, including governed
optimizer, learning-rate, epoch, class-weight and input-media restrictions.

Disposition:

```text
DOCUMENTED_CONFIGURATION
    != automatically
GOVERNED_RESTRICTION

GOVERNED_REQUIRED_CONFIGURATION
    may be
CONSTRAINT
```

## Authentication boundary

A protected-operation authentication mechanism can form a reusable restriction when the source
governs which mechanism is required.

Conceptually:

```text
ProtectedDermaTriageOperation
    authenticationMechanism ∈ {X-API-Key}
```

But token acquisition, refresh and presentation remain behavior/interaction meaning and must not be
collapsed into the constraint merely because they occur in the same requirement.

## Bounded selection boundary

The following meanings are not reducible to a scalar constraint:

```text
top-5 most similar historical cases
20 most recent pertinent clinical corrections
```

They preserve ranking/recency, membership, bounded cardinality, applicability and selection meaning.

Therefore PR-13 bounded-recency/collection-selection semantics survives OP-12.

## Negative non-sufficiency boundary

DermaTriage contains rules such as:

```text
ActivationConditionOfPathA
    MUST NOT imply
ActivationConditionOfPathB
```

This does not mean `PathB` is prohibited.

It means that one fact is not sufficient to infer another.

Therefore:

```text
MUST NOT
    != automatically
negative constrain
```

PR-12 negative non-sufficiency survives OP-12.

## Not-governed boundary

A documented absence of governance must not be rewritten as a negative constraint.

Examples include scopes where specialist-selection rules, deployment automaticity or final
promotion authority are not governed.

Disposition:

```text
NOT_GOVERNED
    !=
PROHIBITED
```

This boundary is required to preserve source incompleteness honestly.

## Property and scalar representation pressure

The current operator already supports a local `property` + `vocabulary` pattern for domain
restrictions.

That is sufficient for strong categorical examples such as:

```text
urgency ∈ {HIGH, MEDIUM, LOW}
```

The corpus also contains scalar and ordered meanings such as:

```text
confidence > 0.85
accuracy degradation <= 5%
reaches 10
reaches 50
```

These do not justify widening OP-12 into a generic predicate language.

Instead, they strengthen existing non-normative pressures:

```text
PR-05 ordered comparison vocabulary
PR-06 scalar/property-addressing comparison
```

Their final home must be tested against OP-14 and condition-language constructs before integrated
method revision.

## Candidate-pressure disposition from OP-12

```text
PR-05 ordered comparison vocabulary
    SOURCE_EVIDENCE_STRONG
    OP12_BOUNDARY_CONFIRMED
    CHARACTERIZED
    NOT_ADMITTED

PR-06 scalar/property-addressing comparison
    SOURCE_EVIDENCE_STRONG
    EXISTING_PROPERTY_SUPPORT_PARTIAL
    ORDERED_SCALAR_GAP_CONFIRMED
    CHARACTERIZED
    NOT_ADMITTED

PR-10 conditional trigger
    SOURCE_EVIDENCE_STRONG
    NOT_ABSORBED_BY_CONSTRAIN
    SURVIVES
    NOT_ADMITTED

PR-12 negative non-sufficiency
    SOURCE_EVIDENCE_STRONG
    NOT_EQ_NEGATIVE_CONSTRAINT
    SURVIVES
    NOT_ADMITTED

PR-13 bounded recency/collection selection
    SOURCE_EVIDENCE_STRONG
    NOT_REDUCIBLE_TO_CONSTRAINT_VALUE
    SURVIVES
    NOT_ADMITTED

PR-14 applicability binding
    SOURCE_EVIDENCE_STRONG
    NOT_ABSORBED_BY_CONSTRAIN
    SURVIVES
    NOT_ADMITTED
```

No new operator is created by R30.

## Delete test

Without `constrain`, the BA could still preserve production, decision logic, classification,
dependency, realization and other facts, but could not deterministically recover independently
governed admissible domains and reusable restrictions.

Whole-operator redundancy is therefore falsified.

## Projection value

OP-12 enables useful deterministic views such as:

```text
allowed-value/domain view
configuration-restriction view
interface/security restriction view
compliance restriction view
constraint-gap view
```

without requiring a specialized operator for each source verb or configuration property.

## Minimal operator basis result

OP-12 reinforces the non-normative working principle:

```text
prefer
    existing operator
    + structured semantic value
    + composition/projection

before proposing
    a new primitive
```

A number, comparison or new natural-language form is not sufficient evidence for operator
proliferation.

## Local verdict

```text
reviewStatus: COMPLETE_GUIDE_CLARIFICATION
reviewClosure: COMPLETE
empiricalStatus: TESTED_POSITIVE
testCoverage: TESTED_POSITIVE + TESTED_NEGATIVE + TESTED_BOUNDARY
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
normativeBAMutation: NONE
```

## Provenance discipline

This consolidation records the OP-12 review against the governed DermaTriage documentation and the
frozen method. It does not retroactively alter the independent-review package.

The prior provenance limitation remains unchanged: the independent-review evidence records the
governed documentation PDF and Documentation/BA Authoring Guide R5 as actual inputs, while Base
Analysis Operational Guide R3 was intended but was not supplied for strict independent replication.

## Next existing operator

`OP-14 decisionRule`
