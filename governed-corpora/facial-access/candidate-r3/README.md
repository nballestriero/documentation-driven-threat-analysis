# Facial Access — integrated successor candidate R3

**Lifecycle:** current governed
**Authority:** `CURRENT_GOVERNED`
**Corpus revision:** `R3-CANDIDATE-9`
**Authority baseline:** `FACIAL-ACCESS-GOV-R2`
**Primary BA source allowed:** yes
**Promotion provenance:** promoted in place from the regression-closed R3 candidate at `4d6aa85385b79be926125d4e61390ac185f63cfd`; the directory name is retained for provenance and does not reduce current authority.
**Post-promotion BA rebuild baseline:** `8af2257a1df94fa5a83d4853ed0a1eb4d020c429`.
**BA representation-pressure review:** complete; minimum `BA2_RELATION_ACTION_VOCABULARY_R3.md` reopen accepted.
**Post-BA regression:** PASS.
**Facial Access BA baseline:** `FACIAL-ACCESS-BA-R24-R1` at `studies/base-analysis/R24_FACIAL_ACCESS_BASE_ANALYSIS_R1.md`; complete case BA / post-BA regression PASS.
**BA6 integrated acceptance:** OPEN; the earlier BA6 completion artifact is provisional closure-attempt evidence pending the inherited holdout/change/projection gate.
**Documentation authoring guide:** R25 pre-holdout freeze complete at `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4`; Base Analysis operational freeze remains pending Phase 2.

## Purpose

This directory is the **current governed R24 Facial Access validation corpus** after the bounded reviews of `DG-FA-001 — cross-MR consumer binding`, `DG-FA-002 — quality/sufficiency criterion`, `DG-FA-003 — transfer-to-channel/path binding`, `DG-FA-004 — intermediate transport nodes / governed multi-stage flow pressure`, the bounded deferral of `DG-FA-005 — test/code evidence linkage`, the resolution of `DG-FA-006 — positive access-decision branch`, full semantic regression, explicit governance promotion, and the first post-promotion minimum justified Base Analysis rebuild.

It integrates the reviewed `MR-0003` identity-determination branch from `candidate-r2` with the minimum downstream project documentation required to represent a real governed access-decision consumer:

- `MR-0001 — Controllo del tentativo di accesso all'area riservata`;
- `MR-0002 — Gestione delle autorizzazioni di accesso`;
- `MR-0003 — Determinazione dell'identità al punto di accesso`;
- `MR-0001_DECISIONS.md` containing `D-1.1` for the conjunctive access-policy commitment;
- `MR-0001_FUNCTIONAL_REQUIREMENTS.md` containing `FR-1.1` for the reviewed operational cross-MR binding;
- the reviewed `MR-0003` Decisions, Functional Requirements and Security Requirements inherited from candidate R2 and refined where explicitly recorded by bounded R24 gap review.

`candidate-r2/` remains unchanged as the MR-0003-only semantic-successor checkpoint and provenance evidence for this integration sequence.

The post-promotion BA rebuild is **analysis evidence only**. It does not become project authority and does not retroactively rewrite the governed project documents.

## Authority boundary

This corpus is the **current governed R24 Facial Access baseline** under `FACIAL-ACCESS-GOV-R2`.

The promotion is authority-only: the regression-closed `R3-CANDIDATE-9` semantic content was promoted in place, while the path `candidate-r3/` is retained as provenance. `primaryBASourceAllowed: true` permitted the minimum BA rebuild after pinning the promoted authority baseline and the concrete Git commit containing the promotion.

The first post-promotion rebuild has now been completed against:

```text
authorityBaselineKey
    FACIAL-ACCESS-GOV-R2

repository baseline
    8af2257a1df94fa5a83d4853ed0a1eb4d020c429
```

No project document was changed by that rebuild.

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

### Post-promotion BA rebuild result

The minimum justified BA rebuild reproduced the representation failure that the documentation review had retained as pressure:

```text
transfer
  source      -> CameraSubsystem
  destination -> RecognitionProcessor
  content     -> RecognitionCapture
```

is sufficient to represent the delivery itself, but the current `transfer` role contract does not provide a semantic identity for **this governed delivery behavior** to which the consumed connectivity service, current wired-Ethernet realization and segment-specific security obligations can all refer without incorrectly targeting the content, an endpoint or the whole pipeline.

The rebuild reproduced the pressure. The subsequent bounded representation-pressure review falsified broader alternatives and accepted the smallest local BA2 repair:

```text
documentation semantic gap
    -> NONE

BA2 representation pressure
    -> CONFIRMED

transfer.behavior
    -> ACCEPTED IN BA2 R3
    -> BAReferent [0..1]

behavior generalized to other operators
    -> NOT JUSTIFIED
```

This result is not permission to rewrite project truth for tooling convenience.

## DG-FA-004 result carried into R3

The historical intermediate-node question is not a current documentation defect. Provider-internal switches, firewalls, routers, hops or topology are not governed by the candidate and are not invented.

The bounded review instead used the actual Facial Access responsibility chain as a multi-stage / branched pressure test:

```text
CameraSubsystem
    -> RecognitionProcessor
    -> IdentityDeterminationOutcome
    -> ControlledAreaAccess
         ^
         |
         +-- AccessAuthorizationState
             concerning the same GovernedIdentity
    -> AccessDecision
```

The review found that current BA1 identity semantics are sufficient and current BA2 can represent the stages, branching/convergence, same-identity correlation and opaque ungoverned provider regions.

A concrete BA2 representation pressure remains when several independently governed facts must address the same transfer segment. For `FR-3.4.2`, the consumed connectivity service, current wired-Ethernet realization and `Confidentiality` / `Integrity` / `AuthorizedProvenance` obligations all concern the governed `RecognitionCapture` delivery and must not be generalized to the whole pipeline.

The smallest working candidate retained from the bounded falsification test is optional reusable behavior identity on `transfer`:

```text
transfer.behavior -> <BAReferent> [0..1]
```

The post-promotion minimum BA rebuild independently reproduced the need for segment identity. The subsequent bounded pressure review accepted exactly one optional `transfer.behavior -> BAReferent [0..1]` role in BA2 R3. The role is not generalized to other operators.

No first-class `Pipeline` type, `contains` / `partOf` relation, generalized behavior role, channel/path document field or provider-internal node is justified.

## FR-3.4.1 acquisition representation note

The post-promotion BA rebuild also confirmed that the governed verb **acquire** in `FR-3.4.1` does not currently force one unique BA2 operator.

`create`, `observe`, `produce` or a combination would each add a more specific interpretation than the project source currently governs.

Therefore:

```text
FR-3.4.1 acquire
    -> MULTIPLE MATERIAL BA CANDIDATES

operator selected
    -> NONE

documentation rewrite
    -> NONE

BA2 extension
    -> NONE
```

The ambiguity is preserved diagnostically rather than guessed away.

## AUTH-C disposition carried into R3

`SEC-3.4.2-C` remains the governed `Confidentiality` obligation for `RecognitionCapture` during the `FR-3.4.2` delivery behavior.

The complete project-specific basis that determines who is authorized to know the capture content remains explicitly `NOT SPECIFIED`. For the current process-demonstration corpus this is preserved as an analysis-relevant clarification rather than filled with an invented authorization policy.

AUTH-C was non-blocking for promotion and remains preserved in the governed baseline. No new Decision, Functional Requirement, Security Requirement, authorization vocabulary, BA contract or technical mechanism is introduced.

## AUTH-P disposition carried into R3

`SEC-3.4.2-P` remains the governed `AuthorizedProvenance` obligation for `RecognitionCapture` during the `FR-3.4.2` delivery behavior.

`CameraSubsystem` remains the governed functional acquisition/delivery owner, but the complete project-specific evidence or authorization basis that establishes an origin as authorized for a particular `IdentityDeterminationRequest` remains explicitly `NOT SPECIFIED`.

For the current process-demonstration corpus this is preserved as an analysis-relevant clarification rather than filled with an invented provenance or attestation policy.

AUTH-P was non-blocking for promotion and remains preserved in the governed baseline. No new Decision, Functional Requirement, Security Requirement, origin vocabulary, BA contract or technical mechanism is introduced.

## DG-FA-006 resolution carried into R3

The bounded semantic-owner review confirmed that the positive access-decision branch is part of the core functional meaning owned by `MR-0001`.

`D-1.1` and `FR-1.1` govern:

```text
successful identity determination
AND required authorization condition satisfied
    for the same GovernedIdentity
    -> AccessDecision MUST ALLOW
```

The existing negative constraints remain unchanged: `NEGATIVE` and `INCONCLUSIVE` cannot result in an allowing decision, and a successful determination without the required authorization condition cannot result in an allowing decision.

This resolution does not introduce an internal vocabulary such as `AUTHORIZED / NOT_AUTHORIZED`, `TRUE / FALSE / UNKNOWN`, or `AccessAuthorizationState.authorized = TRUE`. It also does not introduce retry, exception, contextual-policy or physical gate-opening semantics.

### Post-promotion BA rebuild result

The exact conjunctive `FR-1.1` decision meaning is governed by project documentation, but the current BA2 `decisionRule` lower bound requires a property-addressed comparison. The current `MR-0002` source intentionally does not govern an `authorized` property or normalized authorization-value vocabulary.

Therefore any BA such as:

```text
AccessAuthorizationState.authorized = TRUE
```

would invent project semantics.

The rebuild recorded a BA representation pressure. The subsequent bounded pressure review accepted one local `decisionRule` condition form:

```text
satisfies
  subject   -> BAReferent
  condition -> BAReferent
```

The result is:

```text
FR-1.1 exact decision rule
    -> REPRESENTABLE UNDER BA2 R3

new documentation gap
    -> NO

normalized authorization property/value
    -> NOT INVENTED

decisionRule.satisfies
    -> ACCEPTED LOCALLY IN BA2 R3
```

This is a BA representation refinement, not a reason to alter the governed project documentation.

## Full successor semantic regression result

The full documentation regression passes after correction of propagation-only defects:

- the DG-FA-006 positive branch is propagated consistently into the MR-0003 cross-branch integration text;
- the MR-0003 Security Requirement set reflects the completed `AUTH-C` / `AUTH-P` dispositions and candidate R3 state;
- forward-facing candidate, repository, work-plan and authority metadata were aligned to completed gap review and regression closure.

No new project-semantics gap was found by the post-promotion BA rebuild.

## Governance promotion result

The regression-closed R3 corpus has been **PROMOTED IN PLACE** by explicit human governance.

```text
authorityStatus
    CURRENT_GOVERNED

authorityBaselineKey
    FACIAL-ACCESS-GOV-R2

primaryBASourceAllowed
    true
```

No project semantic content was changed by the promotion.

## Post-promotion minimum BA rebuild result

The first source-first rebuild against the promoted baseline is complete.

```text
core referents
    -> derivable

MR-0001 macro production
    -> representable

MR-0002 GovernedIdentity binding
    -> representable

no preselected GovernedIdentity
    -> preserved

RecognitionProcessor -> IdentityDeterminationOutcome
    -> representable

RecognitionCapture <-> IdentityDeterminationRequest
    -> representable

FR-3.4.2 transfer
    -> representable

FR-3.4.1 acquire semantics
    -> MULTIPLE MATERIAL BA CANDIDATES

FR-1.1 exact conjunctive decision rule
    -> BA REQUIRES UNSUPPORTED FACT

FR-3.4.2 segment identity
    -> CONCRETE BA2 REPRESENTATION FAILURE REPRODUCED

transfer.behavior
    -> working candidate retained
    -> NOT accepted

AUTH-C / AUTH-P
    -> NOT SPECIFIED preserved

project documentation
    -> unchanged

BA2
    -> unchanged
```

## BA representation-pressure review result

The bounded review of the reproduced failures is complete.

```text
FR-3.4.1 acquire
    -> no BA2 change

FR-3.4.2 reusable transfer-segment identity
    -> transfer.behavior -> BAReferent [0..1]
    -> accepted in BA2 R3

FR-1.1 opaque governed authorization condition
    -> decisionRule.satisfies(subject, condition)
    -> accepted in BA2 R3

new top-level operator
    -> NONE

new BA1 family
    -> NONE

project documentation semantic change
    -> NONE
```

The accepted BA2 changes are working methodology refinements and must now survive full post-BA regression.

## Post-BA regression result

The full promoted corpus has been rebuilt using BA2 R3 and materialized as:

```text
studies/base-analysis/R24_FACIAL_ACCESS_BASE_ANALYSIS_R1.md
```

Regression result:

```text
acquisition under-specification
    PASS

capture/request binding
    PASS

transfer.behavior segment identity
    PASS

service / medium distinction
    PASS

delivery-scoped Confidentiality / Integrity / AuthorizedProvenance
    PASS

FR-1.1 with decisionRule.satisfies
    PASS

same GovernedIdentity
    PASS

AUTH-C / AUTH-P
    NOT SPECIFIED PRESERVED

new BA pressure
    NONE FOUND

new project semantic gap
    NONE FOUND

project documentation change
    NONE
```

BA2 R3 therefore survives the current Facial Access corpus regression.

## R25 state-reconciliation disposition

The Facial Access source-to-BA work remains valid case evidence:

```text
FACIAL-ACCESS-GOV-R2
    CURRENT_GOVERNED

FACIAL-ACCESS-BA-R24-R1
    complete Facial Access BA
    post-BA regression PASS

BA2 R3
    current pre-holdout revision

new project semantic gap
    NONE FOUND
```

The repository coherence audit found that the integrated BA6 acceptance gate was not fully executed.

Still pending outside this corpus-specific regression:

```text
structurally different holdout
multiple BA4 projections
governed change
BA3 impact/revalidation
rebuild/re-analysis
```

Therefore:

```text
BA6 integrated acceptance
    OPEN
```

No governed Facial Access project document is reopened by this status correction.

## Next bounded step

R25 Phase 1 is complete. The documentation method is frozen pre-holdout.

The next authorized step is **R25 PHASE 2 — BA PRE-HOLDOUT CONTRACT FREEZE ONLY**.

Do not select or author the new holdout yet.
