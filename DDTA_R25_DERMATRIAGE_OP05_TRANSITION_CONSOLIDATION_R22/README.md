# DDTA R25 — OP-05 `transition` Consolidation R22

## Purpose

R22 closes the individual OP-05 review while preserving the frozen BA method.

The review establishes that the **core semantic operator `transition` is necessary** and that its
whole-operator redundancy hypothesis is falsified by governed DermaTriage evidence in FR-10.

R22 does **not** normatively modify BA2 R3. It records one candidate signature-value-domain delta
for integrated review.

## Immutable predecessor

`20dd07f1bf856e0a1bbf218c5e3fb9837456c93a`

## Frozen BA2 R3 contract

```text
transition
    subject   -> BAReferent [1]
    toState   -> BAReferent [1]
    actor     -> BAReferent [0..1]
    fromState -> BAReferent [0..1]
```

Meaning: governed state/lifecycle change of a subject.

## Core semantic rule retained

```text
subject
    = project-semantic identity whose state/lifecycle changes

actor
    = independently governed identity that causes/performs the change
      when the source establishes it
```

Therefore:

```text
actor may equal subject
actor may differ from subject
actor may be omitted
```

`transition` is **not** restricted to self-transition and `actor` is not removed.

## Positive governed evidence — FR-10

FR-10 governs an adaptation that is already adopted and can be revoked when the governed
post-adoption degradation condition applies.

The minimum lifecycle meaning is:

```text
same ClassificationAdaptation identity
    ADOPTED -> REVOKED
```

Deleting `transition` loses the governed same-identity lifecycle change. `produce`, `create`,
`classify`, `decisionRule`, trigger semantics, persistence and version selection do not preserve
that fact by themselves.

The source only requires DermaTriage to **support** revocation; it does not sufficiently establish
the exact actor that authorizes/performs it. Therefore the positive transition does not force an
`actor` participation.

## FR-10 restoration is a separate fact

Restoring a previous acceptable model version/state must not be collapsed into the same
transition if different version identities are involved.

```text
adaptation lifecycle
    -> transition candidate/positive

active-version restoration
    -> version selection / applicability binding candidate
```

The latter remains routed toward PR-14 / version-selection semantics.

## Secondary evidence — FR-09

FR-09 governs a candidate adaptation becoming qualified for adoption only when governed
acceptance criteria are satisfied. The source also treats qualification/acceptance/progression as
lifecycle results.

This may require composition:

```text
decisionRule
    -> determines qualification outcome under governed criteria

transition
    -> preserves lifecycle progression of the same adaptation identity
```

The exact final BA application remains an application recheck because qualification-result
semantics and lifecycle-state representation must not be conflated.

## Candidate state representation delta

BA2 R3 already permits controlled typed local participation values when independent identity is
not required, but the operator-scoped transition contract currently forces state terms to be
BAReferents.

Candidate integrated contract:

```text
transition
    subject   -> BAReferent [1]
    toState   -> BAReferent | controlled typed local state value [1]
    actor     -> BAReferent [0..1]
    fromState -> BAReferent | controlled typed local state value [0..1]
```

Admission rule candidate:

```text
state meaning needs independent reuse / qualification / correlation / comparison / change identity
    -> BAReferent

otherwise
    -> controlled typed local state value
```

No normative contract change is made in R22.

## General Discovery Pack

R21 introduced the General BA Semantic Discovery Pack as a non-normative candidate mechanism.
R22 records the execution decision to **defer its full-document use to a third complete analysis
cycle**. The current cycle continues operator-by-operator with construct-specific source exhaustion.

## OP-05 result

```text
reviewStatus: EXTENSION_CANDIDATE
reviewClosure: COMPLETE
empiricalStatus: TESTED_POSITIVE_STRONG
operatorCoreDisposition: KEEP_NO_CHANGE
actorRoleDisposition: KEEP_NO_CHANGE
stateCardinalities: KEEP_NO_CHANGE
candidateDelta: CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
normative BA mutation: NONE
next review: OP-06 correlate
```
