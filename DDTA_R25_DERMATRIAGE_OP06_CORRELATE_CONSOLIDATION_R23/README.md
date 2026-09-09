# DDTA R25 — OP-06 `correlate` Consolidation R23

## Purpose

R23 closes the individual OP-06 review while preserving the frozen BA method.

The review establishes that the core semantic operator `correlate` is necessary for governed
same-request/evaluation/operation/context identity matching and that its whole-operator redundancy
hypothesis is falsified by multiple independent DermaTriage cases.

R23 makes **no normative BA2 R3 mutation**. It retains the current signature and records guide /
question-pack clarifications that sharpen the boundary with `reference` and neighboring constructs.

## Immutable predecessor

`9e5176e49845c9184814a17aee550c0afb02fce8`

## Frozen BA2 R3 contract

```text
correlate
    correlatedItem     -> BAReferent [1..*]
    correlationContext -> BAReferent [1]
```

Frozen meaning: assert same-request/evaluation/operation/context identity matching required to bind
items correctly.

## Core semantic rule retained

`correlate` is not a generic `relatedTo`. Use it when governed meaning requires preservation of the
contextual identity under which one or more items must be bound so that cross-matching to a different
context would violate the source.

A one-item case remains meaningful when the governed truth is: `A must remain bound to this specific
context C`. This is distinct from an explicit directional reference.

## Strong positive evidence

- **DEC-12:** four pipeline stages have distinct roles and their outputs must remain correlated to the
  same dermatological case.
- **FR-19:** BioMistral combines the governed multi-source inputs for the same case.
- **FR-22:** the triage outcome produced through `POST /diagnose` must remain associated with the same
  B4 consultation. This validates the existing `[1..*]` lower bound.
- **DEC-15 / FR-23:** the B4-integrated review workflow preserves the same consultation/case identity
  across diagnostic-output write-back, medical-validation write-back, and validated-outcome retrieval.

## Supporting evidence — FR-01

FR-01 requires symptom information in the B4-integrated workflow to be derived from fields associated
with the same B4 consultation. Correlation semantics are positive, but final BA materialization is
deferred because the participating information structures interact with PR-07 structured data /
information contract review.

## Boundary with `reference`

```text
reference
    A -> B
    explicit directional reference

correlate
    A[, B, ...] -> under context C
    context-identity binding required to prevent incorrect cross-matching
```

FR-03 requires `ClinicalReviewResult` to be associated with the `OriginalDermaTriageOutcome` to which
the review refers. The minimum source-grounded relation is therefore a `reference` candidate. Do not
promote `OriginalDermaTriageOutcome` into `correlationContext` merely to force the relation into
`correlate`.

If another governed source additionally establishes a same-case / same-consultation binding, that is
a separate correlation proposition.

## Narrowest governed context rule

When multiple possible contexts exist, use the narrowest context identity actually governed or
necessarily derivable. Prefer `Exam` over `Patient`, `Consultation` over `Project`, etc., when the
narrower identity is governed and is what prevents cross-matching.

A broad shared context such as "same project" does not by itself justify `correlate`; DEC-05 is a
negative control because it preserves independence between adaptation paths even though they share
the same project and may share data.

## Derived-context test

A correlation context need not be named with the words "correlation context". It may be admitted only
when it is either explicitly source-governed or necessarily derivable from governed source relations.
If any source-compliant interpretation permits the candidate items to belong to different context
identities, reject the correlation inference.

Do not create a new context identity merely because it would make `correlate` convenient.

## Negative controls

- FR-21: API invocation alone does not establish request/response correlation.
- FR-18: similarity/retrieval of historical cases is not same-identity correlation.
- FR-06: bounded collection membership / recency selection is not automatically correlation.
- FR-09: comparison against an applicable reference is comparison/applicability, not correlation.
- DEC-05 / FR-13/14/15: shared project or shared data does not imply same lifecycle/context.
- FR-27: a per-case correction/image pairing may be technically plausible but is not sufficiently
  governed by the source.

## Signature result

```text
correlatedItem     -> BAReferent [1..*]  KEEP
correlationContext -> BAReferent [1]     KEEP
```

Do not tighten `correlatedItem` to `[2..*]`: FR-22 provides positive evidence for one item bound to
one governed context. Do not make `correlationContext` optional: doing so would risk degrading
`correlate` into a generic association relation and increase overlap with `reference`.

## OP-06 result

```text
reviewStatus: COMPLETE_GUIDE_CLARIFICATION
reviewClosure: COMPLETE
empiricalStatus: TESTED_POSITIVE_STRONG
operatorCoreDisposition: KEEP_NO_CHANGE
wholeOperatorRedundancy: FALSIFIED
signatureDisposition: KEEP_NO_CHANGE
candidateMethodDelta: NONE
normative BA mutation: NONE
next review: OP-07 reference
```
