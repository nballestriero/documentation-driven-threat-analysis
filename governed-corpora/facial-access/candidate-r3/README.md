# Facial Access — integrated successor candidate R3

**Lifecycle:** candidate
**Authority:** `EXPERIMENTAL_NON_CANONICAL`
**Corpus revision:** `R3-CANDIDATE-3`
**Primary BA source allowed:** no

## Purpose

This directory is the **active R24 experimental Facial Access successor candidate** after the bounded reviews of `DG-FA-001 — cross-MR consumer binding`, `DG-FA-002 — quality/sufficiency criterion` and `DG-FA-003 — transfer-to-channel/path binding`.

It integrates the reviewed `MR-0003` identity-determination branch from `candidate-r2` with the minimum downstream project documentation required to represent a real governed access-decision consumer:

- `MR-0001 — Controllo del tentativo di accesso all'area riservata`;
- `MR-0002 — Gestione delle autorizzazioni di accesso`;
- `MR-0003 — Determinazione dell'identità al punto di accesso`;
- `MR-0001_DECISIONS.md` containing `D-1.1` for the conjunctive access-policy commitment;
- `MR-0001_FUNCTIONAL_REQUIREMENTS.md` containing `FR-1.1` for the reviewed operational cross-MR binding;
- the reviewed `MR-0003` Decisions, Functional Requirements and Security Requirements inherited from candidate R2 and refined where explicitly recorded by bounded R24 gap review.

`candidate-r2/` remains unchanged as the MR-0003-only semantic-successor checkpoint and provenance evidence for this integration sequence.

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

## DG-FA-002 result carried into R3

The historical phrase "quality sufficient to support the access decision" is not carried forward as a standalone capture-quality obligation.

The bounded review distinguishes:

```text
RecognitionCapture quality criterion
    -> NOT SPECIFIED / no standalone SpecializedRequirement justified

governed identity-determination outcome
    -> SUCCESS | NEGATIVE | INCONCLUSIVE

INCONCLUSIVE
    -> available recognition information supports neither
       successful determination of a specific GovernedIdentity
       nor a negative determination
```

The semantic owners of this retained meaning are `D-3.2` and `FR-3.2.1`. No score, confidence, threshold, ranking, `1:N` rule or other quantitative realization criterion is introduced.

The historical placeholder `@IDENTITY_EVIDENCE_QUALITY_CRITERION` is retired. If a future project baseline governs a concrete quality obligation for `RecognitionCapture`, that obligation must be reviewed separately rather than inferred from this disposition.

## DG-FA-003 result carried into R3

The bounded review found no missing project-level transport-binding fact that requires a new cross-document relation.

The existing documentation already identifies one governed interaction through shared meaning:

```text
FR-3.4.2
    RecognitionCapture delivery
    CameraSubsystem -> RecognitionProcessor

D-3.5
    available ConnectivityService supports that delivery
    underlying transport infrastructure is not project-owned/managed

D-3.6
    current governed interaction medium = WIRED_ETHERNET
```

No new hard-coded reference from `D-3.5` or `D-3.6` to `FR-3.4.2` is added merely to make Base Analysis extraction easier, and no `channel`/`path` field is introduced. The historical placeholder `@FR-3.4.2-TRANSPORT-BINDING` is retired as a documentation gap.

The future promoted BA rebuild must still prove that it can preserve this binding reproducibly. Failure to do so remains a BA2 representation pressure, not permission to rewrite project truth for tooling convenience.

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

The next documentation-gap microstep is **DG-FA-004 only — intermediate transport nodes**. DG-FA-005, DG-FA-006 and the existing Security Requirement authorization-evidence clarification questions remain pending.
