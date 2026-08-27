# Facial Access — integrated successor candidate R3

**Lifecycle:** candidate
**Authority:** `EXPERIMENTAL_NON_CANONICAL`
**Primary BA source allowed:** no

## Purpose

This directory is the **active R24 experimental Facial Access successor candidate** after the bounded review of `DG-FA-001 — cross-MR consumer binding`.

It integrates the reviewed `MR-0003` identity-determination branch from `candidate-r2` with the minimum downstream project documentation required to represent a real governed access-decision consumer:

- `MR-0001 — Controllo del tentativo di accesso all'area riservata`;
- `MR-0002 — Gestione delle autorizzazioni di accesso`;
- `MR-0003 — Determinazione dell'identità al punto di accesso`;
- `MR-0001_DECISIONS.md` containing `D-1.1` for the conjunctive access-policy commitment;
- `MR-0001_FUNCTIONAL_REQUIREMENTS.md` containing `FR-1.1` for the reviewed operational cross-MR binding;
- the already-reviewed `MR-0003` Decisions, Functional Requirements and Security Requirements inherited from candidate R2 in branch-specific files.

`candidate-r2/` remains unchanged as the MR-0003-only semantic-successor checkpoint and provenance evidence for this integration step.

## Authority boundary

This candidate is current **for R24 experimentation and further documentation-gap review only**.

It is not `CURRENT_GOVERNED`, it is not a primary Base Analysis source, and it does not authorize an accepted Facial Access BA. Explicit governance promotion remains mandatory before accepted BA derivation.

## DG-FA-001 result carried into R3

The cross-MR consumer is no longer an unresolved placeholder. The integrated candidate governs the following responsibility chain:

```text
MR-0003
  -> IdentityDeterminationOutcome
  -> on successful determination: GovernedIdentity X

MR-0002
  -> AccessAuthorizationState concerning a GovernedIdentity

MR-0001 / ControlledAreaAccess
  -> uses the outcome for the access attempt
  -> when identity determination succeeds, evaluates authorization
     with respect to the same GovernedIdentity X
  -> determines AccessDecision
```

This resolves the semantic question represented by historical `@ACCESS_DECISION_CONSUMER` without inventing a technical component or protocol.

## Deliberately unresolved meaning

R3 does **not** state that:

```text
successful identity determination
AND authorization condition satisfied
    -> MUST ALLOW
```

The historical documentation governed the necessary conditions for an allowing decision but did not fully govern that positive branch as a mandatory result. This remains an explicit diagnostic gap (`DG-FA-006`) rather than being repaired by Base Analysis.

R3 also does not introduce an internal vocabulary such as `AUTHORIZED / NOT_AUTHORIZED`, `TRUE / FALSE / UNKNOWN`, or `AccessAuthorizationState.authorized = TRUE`.

## Next bounded review

The next documentation-gap microstep is **DG-FA-002 only**. DG-FA-003 through DG-FA-005 and the existing Security Requirement authorization-evidence clarification questions remain pending.
