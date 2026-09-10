# DDTA R25 — OP-14 `decisionRule` Review

## Review identity

```text
review_id: OP-14
semantic_family: SF-04 RESTRICTION_DECISION_CONDITION
status: COMPLETE_GUIDE_CLARIFICATION
baseline_commit: 6b9c2981107544db71544014ff3d9dcc3ff1acef
frozen_method: BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
```

## Construct

```text
decisionRule
    actor  -> BAReferent [1]
    input  -> BAReferent [1..*]
    result -> BAReferent [1]

    rule
      IF    decisionCondition
      THEN  resultAssignment [1..*]
      ELSE  resultAssignment [0..*]
```

Frozen guide meaning:

```text
operational mapping from governed conditions/inputs to a governed result
```

## Source coverage

The complete governed DermaTriage baseline was reviewed semantically across triage priority mapping,
clinical-review qualification, adaptation triggering, candidate qualification, acceptance criteria,
rollback/revocation, fallback behavior, bounded retrieval and training/checkpoint selection.

A source clause was not admitted merely because it used `when`, `if`, a threshold, or a Boolean-looking encoding.

## Admission discipline

A candidate OP-14 proposition requires:

```text
A = governed actor
I = one or more governed inputs
R = governed result
C = source-grounded condition structure sufficient to determine/assign R
```

Do not mint R merely to force a conditional behavior into `decisionRule`.

## Strong positive control — DEC-02 / FR-02 P-scale mapping

The source governs:

```text
HIGH and confidence > 0.85 -> P1
HIGH otherwise             -> P2
MEDIUM                      -> P3
LOW                         -> P4
```

This is direct positive evidence for condition/input-to-result mapping.

The `> 0.85` clause simultaneously proves that the current `equals | notEquals` comparison vocabulary is insufficient for the full corpus.

Disposition:

```text
OPERATIONAL_MAPPING
    STRONG_POSITIVE

PR-05 / PR-06
    PRESSURE_CONFIRMED
    ROUTE_TO_CL01
```

## Strong positive control — FR-08 supervision target derivation

The source maps corrected operational priority to supervision target:

```text
P1 -> HIGH
P2 -> HIGH
P3 -> MEDIUM
P4 -> LOW
```

This is a clean equality-based rule and demonstrates that OP-14 does not depend on ordered comparison in order to be semantically valid.

## Result cardinality

P1..P4 or HIGH/MEDIUM/LOW are values of one governed result semantic object, not evidence for multiple top-level `result` roles.

```text
result [1]
    KEEP
```

## `constrain` boundary

The allowed domain:

```text
OperationalPriority in {P1,P2,P3,P4}
```

and the rule selecting a value from that domain are distinct governed meanings.

```text
CONSTRAIN_EQ_DECISION_RULE
    FALSE
```

## FR-07 — concept versus payload encoding

The governed meaning is `ClinicianDisagreement` qualifying evidence for the classifier-adaptation path.
The documented `agrees == False` is a current data/state encoding and must not become the normative semantic identity of the condition.

```text
PROJECT_CONCEPT_EQ_CURRENT_ENCODING
    FALSE
```

## FR-09 — conjunction evidence

The candidate adaptation is qualified only if all applicable governed comparative criteria are satisfied.

This is strong source evidence for conjunction semantics and therefore relevant to CL-03 `allOf`.

It does not close the CL-03 audit inside OP-14.

## Ordered comparison pressure

The corpus requires:

```text
confidence > 0.85
accuracy degradation at most 5%
accuracy degradation > 5%
non-degradation / no-worse-than comparison to reference
```

The current local comparison vocabulary is therefore not corpus-complete.

Disposition:

```text
CL01_CURRENT_VOCABULARY
    INSUFFICIENT_FOR_DERMATRIAGE

NEW_TOP_LEVEL_OPERATOR
    NOT_JUSTIFIED_BY_THIS_GAP
```

## FR-04 / FR-05 trigger boundary

The source governs:

```text
reaches 10 -> activate prompt evolution
reaches 50 -> activate classifier adaptation
```

These clauses are conditional, but the consequent is governed action/activation semantics rather than necessarily a result assignment.

Do not manufacture an activation-result referent simply to admit OP-14.

```text
CONDITIONALITY_EQ_DECISION_RULE
    FALSE

PR-10 CONDITIONAL_ACTION_TRIGGER
    SURVIVES_OP14
```

## FR-10 rollback boundary

The source requires support for revocation/restoration after post-adoption degradation greater than 5% and explicitly does not establish automatic rollback.

Therefore:

```text
IF degradation > 5% THEN rollback
```

would overstate the source.

```text
ROLLBACK_CAPABILITY_EQ_AUTOMATIC_RULE
    FALSE
```

## FR-13 / FR-14 / FR-15 negative non-sufficiency boundary

The source governs forms equivalent to:

```text
A MUST NOT, by itself, imply B
```

This does not mean:

```text
IF A THEN NOT B
```

It expresses insufficiency of A as evidence for B.

```text
PR-12
    SURVIVES_OP14
```

These clauses must not be used as automatic positive evidence for local `not`.

## FR-01 conditional path boundary

Image absence selects symptom-based urgency determination behavior. It does not itself assign a specific urgency result.

```text
CONDITIONAL_BEHAVIOR_EQ_DECISION_RULE
    FALSE
```

## FR-18 bounded ranked retrieval

Top-5 most-similar retrieval combines similarity, ranking, membership and bounded selection.
A simple binary decision rule does not preserve the complete meaning.

```text
PR-13
    SURVIVES_OP14
```

## FR-20 best-checkpoint selection

Selecting the best checkpoint by validation Macro F1 is decision-like mapping from candidates/scores to a selected result, but the current local condition language does not demonstrate a compact representation for ranked/argmax selection.

```text
RANKED_SELECTION_LOCAL_RULE_EXPRESSIVENESS
    PRESSURE_RETAINED
    NO_NEW_OPERATOR_ADMITTED
```

## Applicability

Rules, comparisons and triggers may be scoped to a path, phase, operation, reference or population.
Do not hide this meaning inside arbitrary prose.

```text
PR-14
    SURVIVES_OP14
```

## Delete test

Remove OP-14 while retaining all other frozen operators and local restriction semantics.
The BA can still preserve domains, constraints, flows, realization and responsibility, but cannot deterministically reconstruct governed mappings such as the P-scale rule or corrected-priority-to-supervision-target rule.

Whole-operator redundancy is therefore falsified.

## Projection test

OP-14 enables deterministic projections including:

```text
decision mapping view
rule traceability view
result reachability view
qualification logic view
condition coverage/gap view
```

without proliferating one top-level operator per project rule.

## Q1–Q20 result summary

| Q | Test | Result |
|---|---|---|
| Q1 | governed actor | PASS |
| Q2 | governed inputs | STRONG PASS |
| Q3 | governed result | STRONG PASS |
| Q4 | condition/input -> result mapping | STRONG PASS |
| Q5 | source grounding | STRONG PASS |
| Q6 | constrain boundary | PASS / DISTINCT |
| Q7 | result vs behavior/action | STRONG BOUNDARY |
| Q8 | conditional trigger | NOT AUTOMATICALLY DECISIONRULE |
| Q9 | equality comparison | PASS |
| Q10 | ordered comparison | PRESSURE CONFIRMED |
| Q11 | conjunction / allOf | STRONG SOURCE EVIDENCE |
| Q12 | named-condition / satisfies relevance | POSITIVE / FORMAL CL REVIEW PENDING |
| Q13 | ELSE / otherwise | STRONG POSITIVE |
| Q14 | negative non-sufficiency | DISTINCT / PR-12 SURVIVES |
| Q15 | applicability | PRESSURE CONFIRMED |
| Q16 | ranking/selection | LOCAL-LANGUAGE PRESSURE |
| Q17 | result cardinality | KEEP [1] |
| Q18 | delete test | WHOLE-OPERATOR REDUNDANCY FALSIFIED |
| Q19 | projection test | STRONG PASS |
| Q20 | final admission | PASS WITH SOURCE-GROUNDING GATE |

See `DECISIONRULE_QUESTION_PACK_R1.md`.

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
operationalConditionToResultMapping: STRONG_POSITIVE
conditionAutomaticallyDecisionRule: FALSE
conditionalBehaviorAutomaticallyDecisionRule: FALSE
triggerAutomaticallyDecisionRule: FALSE
rollbackCapabilityEquivalentToAutomaticRollbackRule: FALSE
negativeNonSufficiencyEquivalentToDecisionRule: FALSE
orderedComparisonSupport: CURRENT_CL01_INSUFFICIENT_PRESSURE_CONFIRMED
candidateMethodDelta: NONE
```

## Existing-operator milestone

```text
EXISTING_OPERATOR_AUDIT
    COMPLETE_14_OF_14

METHODOLOGY_REVIEW
    NOT_COMPLETE
```

Next: formal CL-01..CL-05 audit, then PR/CC disposition and the mandatory source-complete pre-rewrite completeness re-check.
