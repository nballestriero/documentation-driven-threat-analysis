# CR-02 Working Finding — `decisionRule` and Comparison Language Candidate R1

**Status:** `CANDIDATE_SOLUTION_IDENTIFIED_NOT_NORMATIVE`  
**Frozen method mutation:** `NONE`  
**Purpose:** preserve the interactive CR-02 result so it can be completed and integrated without relying on chat history.

## 1. Inherited pressure

The first DermaTriage BA/holdout carried:

```text
P-05 ORDERED COMPARISON VOCABULARY
    STRONG_REPEATED

P-06 SCALAR / PROPERTY-ADDRESSING COMPARISON
    STRONG_REPEATED
```

The pressure is narrower than “decisionRule is missing”. Evidence so far indicates that `decisionRule` itself is useful; the weak point is comparison expressiveness/readability.

## 2. Governed evidence to retain

### FR-02 — P-scale derivation

Material meaning includes:

```text
urgency = HIGH
AND
applicable confidence > 0.85
    -> P1
```

with other governed mappings for P2/P3/P4.

Do not automatically rewrite “HIGH in the other applicable cases” as `confidence <= 0.85` unless the governed applicability/absence semantics make that equivalence valid.

### Candidate/reference comparison evidence

Pre/post-adaptation evidence includes property-to-property comparison needs, for example candidate performance relative to an applicable reference.

When source wording such as “not worse than” is accompanied by a governed metric orientation, represent the actual ordered comparison (`>=` or `<=`) rather than creating a semantic `notWorseThan` operator. If orientation is not governed, do not invent it.

## 3. Human-readable candidate syntax

Preferred authoring form:

```text
UrgencyAssessment.urgency = HIGH
UrgencyAssessment.confidence > 0.85
Candidate.sensitivity >= ApplicableReference.sensitivity
```

Candidate operator vocabulary:

```text
=  !=  <  <=  >  >=
```

Candidate property addressing:

```text
BAReferent.property
```

This is intentionally closer to standard mathematical/programming notation than a verbose form such as:

```text
property(UrgencyAssessment, urgency)
```

The conceptual internal model may still be understood as:

```text
comparison(left, operator, right)
```

but the operational guide should prefer the infix notation if the final integrated review accepts it.

## 4. Logical composition

Current semantics appear reusable:

```text
allOf  <-> AND
anyOf  <-> OR
not    <-> NOT
```

A human-readable rule may therefore be presented as:

```text
IF
    UrgencyAssessment.urgency = HIGH
    AND UrgencyAssessment.confidence > 0.85
THEN
    PScalePriority = P1
```

while deterministic machine serialization may preserve structured condition nodes.

## 5. Current local finding

```text
decisionRule:
    provisionally sufficient as a construct

comparison:
    P-05 confirmed
    P-06 confirmed
    candidate solution identified

satisfies:
    retain for semantic criteria pending complete CL-02 audit

allOf / anyOf / not:
    retain pending complete CL-03..CL-05 audit

conditional action trigger:
    do not absorb into decisionRule without separate review

negative implication / non-sufficiency:
    do not absorb into decisionRule without separate review
```

## 6. FINAL_BA_TRACE

The final DermaTriage BA reconstruction must preserve at least:

- exact FR-02 decision mappings and applicable-condition semantics;
- candidate/reference property comparisons used in adaptation qualification/revocation evidence;
- source anchors for every threshold and comparison direction;
- explicit non-inference where a fallback/applicability rule is not fully governed;
- human-readable infix presentation aligned with deterministic machine structure.

## 7. Required work before closure

CR-02 is **not complete** until:

1. all material governed decision/comparison occurrences are enumerated;
2. the previous BA representations are compared against the candidate notation;
3. CL-01..CL-05 receive explicit dispositions under the R2 work plan;
4. P-05/P-06 are dispositioned after the condition-language audit;
5. G1–G8 are completed for any normative signature/grammar change.
