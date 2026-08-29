---
title: "DDTA R24 Facial Access BA representation-pressure review checkpoint - R1"
---

# DDTA R24 Facial Access BA representation-pressure review checkpoint

**Status:** PRESSURE REVIEW COMPLETE — MINIMUM BA2 R3 REOPEN ACCEPTED / POST-BA REGRESSION REQUIRED
**Prepared against repository baseline:** `8af2257a1df94fa5a83d4853ed0a1eb4d020c429`
**Project authority baseline:** `FACIAL-ACCESS-GOV-R2`
**Input BA contract:** `BA2_RELATION_ACTION_VOCABULARY_R2.md`
**Output BA contract:** `BA2_RELATION_ACTION_VOCABULARY_R3.md`
**Project documentation semantic change:** NONE

## 1. Purpose

This checkpoint records the bounded representation-pressure review performed after the source-first minimum justified Base Analysis rebuild of the promoted Facial Access corpus.

The review is not a new project-document review. It does not change `FACIAL-ACCESS-GOV-R2`.

Its question is narrower:

> after the promoted source has been rebuilt into the minimum BA without inventing project meaning, which reproduced representation failures survive falsification and force the smallest BA2 reopen?

## 2. Preconditions

The review starts from the exact promoted source state:

```text
repository baseline
    8af2257a1df94fa5a83d4853ed0a1eb4d020c429

authorityBaselineKey
    FACIAL-ACCESS-GOV-R2

authorityStatus
    CURRENT_GOVERNED

primaryBASourceAllowed
    true
```

The immediately preceding minimum BA rebuild recorded:

```text
FR-3.4.1 acquire
    MULTIPLE MATERIAL BA CANDIDATES

FR-3.4.2 segment identity
    CONCRETE BA2 REPRESENTATION FAILURE REPRODUCED

FR-1.1 exact decision rule
    BA REQUIRES UNSUPPORTED FACT

AUTH-C / AUTH-P
    NOT SPECIFIED preserved

project documentation
    unchanged

BA2
    unchanged
```

## 3. Review rule

The pressure review uses the smallest-change rule:

```text
existing BA structure preserves governed meaning
    -> do not reopen

existing BA structure requires loss or invention
    -> identify exact failure

smallest local refinement repairs exact failure
    -> accept only that refinement

broader abstraction/generalization
    -> reject until a second concrete counterexample forces it
```

A familiar verb, implementation pattern, graph convenience or future tooling possibility is not sufficient evidence.

## 4. Pressure A — FR-3.4.1 `acquire`

Source meaning:

```text
when an IdentityDeterminationRequest requires a new RecognitionCapture
CameraSubsystem MUST acquire it for that request
```

Existing BA candidates such as `create`, `observe`, `produce` or combinations impose materially different interpretations.

The source deliberately does not select among them.

### Disposition

```text
source semantics
    sufficient at current abstraction

existing BA2 unique operator
    NONE FORCED

new acquire operator
    NOT JUSTIFIED

documentation rewrite
    REJECTED

diagnosis
    MULTIPLE MATERIAL BA CANDIDATES
```

This pressure does not force BA2 reopen.

A `RecognitionCaptureAcquisition` behavior may be a BAReferent when independent reusable identity is needed, but that fact does not require a new operator.

## 5. Pressure B — reusable identity of the FR-3.4.2 transfer behavior

The delivery itself is representable under BA2 R2:

```text
transfer
  source      -> CameraSubsystem
  destination -> RecognitionProcessor
  content     -> RecognitionCapture
```

However, governed sources separately state that the same delivery:

- is supported by consumed connectivity service;
- currently uses wired Ethernet;
- is subject to `Confidentiality`;
- is subject to `Integrity`;
- is subject to `AuthorizedProvenance`.

Those meanings must remain scoped to this transfer segment.

### 5.1 Falsified alternatives

The review rejects:

```text
target RecognitionCapture
    -> would qualify content rather than delivery behavior

target CameraSubsystem / RecognitionProcessor
    -> would qualify endpoint rather than delivery behavior

target whole pipeline
    -> would incorrectly propagate segment-specific meaning

use BAProposition identity as behavior identity
    -> proposition assertion identity is not reusable project-semantic behavior identity

use BA3 sourceLink as semantic binding
    -> provenance is not BA2 relation semantics

introduce channel/path/pipeline types
    -> broader than the governed counterexample requires
```

### 5.2 Smallest surviving repair

BA1 already permits a behavior to be a `BAReferent` when it needs independent reuse.

The only missing binding is from the transfer proposition to that behavior referent.

Accepted R3 refinement:

```text
transfer
  behavior    -> <BAReferent> [0..1]
  source      -> <BAReferent> [1]
  destination -> <BAReferent> [1..*]
  content     -> <BAReferent> [1..*]
```

`behavior` is optional so ordinary transfers do not pay an identity cost when no governed downstream proposition needs to address the transfer behavior itself.

### Disposition

```text
representation failure
    CONFIRMED

BA1 reopen
    NO

new operator
    NO

new BA family
    NO

transfer.behavior
    ACCEPTED IN BA2 R3

general behavior role on other operators
    NOT JUSTIFIED
```

## 6. Pressure C — FR-1.1 exact authorization condition

`D-1.1` / `FR-1.1` govern a genuine decision mapping:

```text
SUCCESS
AND required authorization condition satisfied
    for the same GovernedIdentity
    -> AccessDecision MUST ALLOW

otherwise, within the governed branches
    -> AccessDecision MUST NOT ALLOW
```

A mere `dependOn` representation loses the result-selection rule.

`decisionRule` is therefore required.

The identity-determination side has a governed semantic outcome domain and can be represented with property-addressed `comparison`.

The authorization side does **not** govern:

```text
AccessAuthorizationState.authorized
TRUE / FALSE
AUTHORIZED / NOT_AUTHORIZED
```

Any such comparison would invent project meaning.

### 6.1 Falsified alternatives

Rejected:

```text
AccessAuthorizationState.authorized = TRUE
    -> unsupported project property/value

property-less comparison
    -> treats a rich referent as a scalar condition/value without governed evidence

free-text constrain
    -> hides decision semantics

dependOn
    -> expresses prerequisite, not conditional result selection

new global predicate/operator
    -> broader than the counterexample requires
```

### 6.2 Smallest surviving repair

The source does govern one opaque condition: the required authorization condition is satisfied.

BA2 needs to preserve that condition without pretending to know its internal property/value representation.

Accepted local `decisionCondition` form:

```text
satisfies
  subject   -> <BAReferent>
  condition -> <BAReferent>
```

Example:

```text
allOf
  condition ->
    comparison
      referent      -> IdentityDeterminationOutcome
      property      -> outcomeKind
      comparisonKey -> equals
      value         -> SUCCESS

  condition ->
    satisfies
      subject       -> AccessAuthorizationState
      condition     -> RequiredAccessAuthorizationCondition
```

The same-`GovernedIdentity` binding remains separate and is not absorbed into `satisfies`.

### Disposition

```text
decisionRule
    RETAINED / REQUIRED

comparison.property
    RETAINED / REQUIRED

property-less comparison
    NOT JUSTIFIED

decisionRule.satisfies
    ACCEPTED IN BA2 R3

new top-level satisfies operator
    NO

normalized authorization vocabulary
    NOT INTRODUCED
```

## 7. Accepted BA2 R3 delta

The complete accepted delta from R2 to R3 is exactly:

```text
transfer
  + behavior -> BAReferent [0..1]

decisionRule.decisionCondition
  + satisfies
      subject   -> BAReferent
      condition -> BAReferent
```

Everything else is carry-forward or explicit rejection.

## 8. Project-document effect

This review does not change:

- `MR-0001_ACCESS_CONTROL.md`;
- `MR-0001_DECISIONS.md`;
- `MR-0001_FUNCTIONAL_REQUIREMENTS.md`;
- `MR-0002_ACCESS_AUTHORIZATION.md`;
- `MR-0003_IDENTITY_DETERMINATION.md`;
- `MR-0003_DECISIONS.md`;
- `MR-0003_FUNCTIONAL_REQUIREMENTS.md`;
- `MR-0003_SECURITY_REQUIREMENTS.md`.

No new `Decision`, `FunctionalRequirement`, `SecurityRequirement`, project property, protocol, channel/path field, topology, mechanism or policy is introduced.

`AUTH-C` and `AUTH-P` remain `NOT SPECIFIED`.

## 9. Contract effect

```text
BA0
    unchanged

BA1
    unchanged

BA2
    R3 created from R2 with two minimum refinements

BA3
    unchanged

BA4
    unchanged

BA5
    unchanged

BA6
    not yet completed
```

R2 remains historical research evidence. R3 supersedes it only for active forward R24 BA work.

## 10. Next bounded step

The next step is:

**POST-BA REGRESSION AGAINST THE FULL PROMOTED FACIAL ACCESS CORPUS ONLY.**

The regression must verify at minimum:

```text
acquisition under-specification
    preserved without invented operator

capture/request binding
    preserved

delivery segment
    representable with transfer.behavior

service + Ethernet + security obligations
    remain scoped to that delivery

FR-1.1
    representable without invented authorization vocabulary

same GovernedIdentity
    preserved

AUTH-C / AUTH-P
    remain NOT SPECIFIED

new BA representation pressure
    none, or explicitly recorded
```

Do not combine this checkpoint with:

- BA6 closure;
- guide rewrite;
- thesis consolidation;
- STRIDE / STRIDE-AI;
- lifecycle/test/code traceability;
- stage/commit/push.
