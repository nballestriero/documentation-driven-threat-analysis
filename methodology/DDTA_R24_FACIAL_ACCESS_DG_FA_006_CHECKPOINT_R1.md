---
title: "DDTA R24 Facial Access DG-FA-006 checkpoint - R1"
---

# DDTA R24 Facial Access DG-FA-006 checkpoint

**Status:** ACTIVE R24 EXECUTION REFINEMENT — BOUNDED DG-FA-006 RESOLUTION
**Prepared against repository baseline:** `4b2dce0a2817ce94daeedaa620a81097308dfad1`

## 1. Purpose

This checkpoint records the bounded human-governance resolution of `DG-FA-006 — positive access-decision branch`.

The gap asks whether the current conjunctive access policy merely states necessary conditions for an allowing decision or whether, when both conditions are satisfied, the project requires the positive branch.

## 2. Source state before resolution

Before this microstep, candidate R3 already governed:

```text
AccessDecision that allows access
    requires successful identity determination
    AND the required authorization condition
        satisfied for the same GovernedIdentity

NEGATIVE
    -> MUST NOT ALLOW

INCONCLUSIVE
    -> MUST NOT ALLOW
```

The stronger positive proposition remained explicitly `NOT SPECIFIED`:

```text
successful identity determination
AND required authorization condition satisfied
    -> MUST ALLOW ?
```

## 3. Disposition

`DG-FA-006` is resolved as:

**CONFIRMED CORE FUNCTIONAL SEMANTIC GAP / MINIMAL POSITIVE BRANCH GOVERNED / HUMAN GOVERNANCE RESOLUTION.**

The project meaning is now:

```text
IF IdentityDeterminationOutcome represents SUCCESS
AND the required authorization condition from D-1.1
    is satisfied for the same GovernedIdentity
THEN ControlledAreaAccess MUST produce
    an AccessDecision that allows access
```

The semantic owners are:

- `D-1.1` for the project-level conjunctive access-policy commitment;
- `FR-1.1` for the normative operational positive branch.

No new Decision or Functional Requirement is introduced.

## 4. Resulting functional decision table

The candidate now preserves the following minimum behavior:

```text
Identity outcome     Required authorization     AccessDecision

SUCCESS              satisfied                  ALLOW
SUCCESS              not satisfied              NOT ALLOW
NEGATIVE             any                        NOT ALLOW
INCONCLUSIVE         any                        NOT ALLOW
```

The table expresses only the current governed branch semantics. It does not introduce an internal value vocabulary for `AccessAuthorizationState`.

## 5. Boundaries retained

This resolution does **not** introduce or infer:

- `AccessAuthorizationState.authorized = TRUE | FALSE`;
- `AUTHORIZED / NOT_AUTHORIZED / UNKNOWN`;
- authorization lookup, cache, freshness or synchronization semantics;
- retry or exception policy;
- time-of-day, role, risk or contextual access policy;
- physical gate-opening behavior;
- a technical consumer component, API or protocol;
- any score, confidence, threshold, ranking or `1:N` recognition semantics;
- any new BA contract or accepted BA representation.

The physical realization of allowing access remains outside the current responsibility boundary.

## 6. Why DG-FA-006 differs from AUTH-C and AUTH-P

`AUTH-C` and `AUTH-P` are analysis-relevant project meanings that may remain explicitly `NOT SPECIFIED` in the current process-demonstration corpus because the existing Security Requirements still provide stable governed anchors.

`DG-FA-006` instead concerns the central functional semantics by which `MR-0001` determines `AccessDecision`. Leaving the positive branch open would permit multiple materially different project behaviors for the same governed input conditions.

The bounded human-governance step therefore supplies only the smallest missing project commitment.

## 7. Base Analysis boundary

No BA contract is modified in this microstep.

After explicit governance promotion, the minimum BA rebuild must derive this positive branch from the promoted `D-1.1` / `FR-1.1` documentation. It must not invent an internal authorization-state property or value vocabulary.

## 8. Candidate state after this resolution

```text
corpusKey
    facial-access-candidate-r3

corpusRevision
    R3-CANDIDATE-8

authorityStatus
    EXPERIMENTAL_NON_CANONICAL

primaryBASourceAllowed
    false
```

The bounded documentation-gap review is now complete for the currently registered R3 gap set.

## 9. Next bounded step

The next authorized step is **full successor semantic regression**.

Do not perform governance promotion, accepted BA rebuild, STRIDE/STRIDE-AI integration, or lifecycle/test/code traceability work in the same microstep.
