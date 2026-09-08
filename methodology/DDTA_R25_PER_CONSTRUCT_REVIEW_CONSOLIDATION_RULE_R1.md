# DDTA R25 — Per-Construct Review Consolidation Rule R1

## Status

Non-normative BA review-governance refinement introduced by R17.
It does **not** modify BA0–BA5 and does **not** modify the documentation-writing methodology.

## Purpose

Every `OP-*`, `CL-*`, or `PR-*` review must be consolidated before the next review begins.
The goal is to prevent valid evidence, rejected alternatives, documentation QA, and final-BA reconstruction information from remaining only in conversational history.

## Mandatory cycle

```text
SOURCE EXHAUSTION
    -> PREVIOUS BA / HOLDOUT EVIDENCE
    -> REPRESENTATION TESTS
    -> CONSTRUCT BOUNDARY TESTS
    -> QUESTION PACK (when useful)
    -> DOCUMENTATION QA
    -> G1–G8 when a delta exists
    -> LOCAL VERDICT
    -> FINAL_BA_TRACE
    -> CONSOLIDATION ARTIFACT
    -> NEXT REVIEW
```

## Closure rule

A review is not complete until its artifact allows another analyst to reconstruct, without chat history:

- source anchors and evidence-bearing meaning;
- frozen construct/signature;
- accepted and rejected representations;
- semantic boundaries with neighboring constructs;
- documentation QA;
- candidate guide/method delta, if any;
- `FINAL_BA_TRACE`;
- exact deferred review ownership.

## Construct-specific question packs

A review MAY define a question pack when systematic questions improve:

- documentation clarity checking;
- analyst reproducibility;
- LLM non-inference behavior;
- discovery of adjacent BA semantic needs;
- later downstream-analysis readiness.

Question packs are diagnostic aids, not project authority.

```text
question asked
    != requirement exists

question unanswered
    != automatic governed gap

question answer
    MUST be source-grounded if asserted
```

Use the controlled documentation-QA outcomes:

```text
ANSWERED
CLARITY_OPPORTUNITY
GOVERNED_GAP
NOT_APPLICABLE
```

A question-pack answer may identify evidence for another BA construct. In that case, route the evidence to the owning review rather than overloading the current construct.

## Documentation-authoring relationship

Question packs may later be evaluated for reuse by an AI-assisted documentation-authoring workflow. During the current CR/OP/CL/PR cycle this remains an observation/candidate only. The stabilized documentation-writing methodology MUST NOT be changed by an individual BA construct review.
