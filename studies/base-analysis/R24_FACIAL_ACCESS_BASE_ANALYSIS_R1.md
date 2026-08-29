# R24 Facial Access — regression-passed minimum Base Analysis R1

**BA baseline key:** `FACIAL-ACCESS-BA-R24-R1`
**Status:** COMPLETE FACIAL ACCESS CASE BA / POST-BA REGRESSION PASS / BA6 INTEGRATED ACCEPTANCE OPEN
**Forward interpretation:** case-validation BA evidence under R25; the earlier BA6 closure-attempt package does not establish integrated BA6 acceptance.
**Project authority baseline:** `FACIAL-ACCESS-GOV-R2`
**Pinned project-source repository baseline:** `8af2257a1df94fa5a83d4853ed0a1eb4d020c429`
**Pre-holdout BA contract set used by this case:** BA0 R1; BA1 R1; BA2 R3; BA3 R1; BA4 R1; BA5 R1. BA6 remains the open integrated-validation gate.
**Authority:** analytical artifact only; NOT project authority.
**Purpose:** materialize the minimum methodology-neutral shared project meaning required by the current DDTA Facial Access validation scope.

## 1. Acceptance boundary

This BA is retained as the complete regression-passed analytical representation for the declared Facial Access shared-analysis scope. It is not, by itself, evidence that integrated BA6 is closed.

It does not claim to be:

- a complete system architecture;
- an implementation design;
- a network topology model;
- an executable requirements model;
- a STRIDE / STRIDE-AI model;
- a complete future-proof ontology.

It is complete only in this sense:

> every material governed meaning needed by the current shared DDTA scope is either represented, explicitly preserved as under-specified / diagnostic, or explicitly outside the current shared-analysis scope.

Governed documentation remains project authority.

## 2. Minimum-detail stopping rule

Further decomposition is required only when an additional distinction is necessary to preserve governed meaning or to answer a material downstream analysis question without invention.

Operational test:

```text
Do we have enough governed semantics to formulate the question
and determine whether the answer is:
    supported
    contradicted
    or NOT SPECIFIED?

YES
    -> stop decomposing

NO
    -> identify the missing governed distinction
       or preserve the uncertainty diagnostically
```

This rule prevents the BA from descending automatically into snapshot/streaming, protocol, packet, provider-hop or implementation detail merely because such detail could be modeled.

## 3. Accepted BAReferents

| Canonical BAReferent | Origin | Governed meaning |
|---|---|---|
| `ControlledAreaAccess` | GROUNDED | MR-0001 responsibility that controls one access attempt and determines its `AccessDecision`. |
| `AccessAttempt` | GROUNDED | The single access attempt whose outcome is controlled by MR-0001. |
| `AccessAuthorizationManagement` | GROUNDED | MR-0002 responsibility that establishes/maintains authorization state and makes it available to access control. |
| `IdentityDetermination` | GROUNDED | MR-0003 responsibility to determine which governed identity corresponds to the person present. |
| `PersonPresentAtAccessPoint` | GROUNDED | The person present when identity determination starts; the specific corresponding governed identity is not yet determined. |
| `FacialRecognitionStrategy` | GROUNDED | Current D-3.1 strategy used to perform identity determination. |
| `IdentityDeterminationRealization` | GROUNDED | The current realization of MR-0003 explicitly addressed by D-3.5 as consumer of connectivity service. |
| `IdentityDeterminationRequest` | GROUNDED | Operational request to determine which governed identity corresponds to the person present; it does not contain/presuppose a preselected `GovernedIdentity`. |
| `RecognitionCapture` | GROUNDED | Governed visual capture used by the recognition capability. |
| `RecognitionCaptureAcquisition` | GROUNDED | FR-3.4.1 acquisition behavior. Its implementation semantics remain deliberately under-specified. |
| `RecognitionCaptureDelivery` | GROUNDED | FR-3.4.2 delivery behavior from `CameraSubsystem` to `RecognitionProcessor`. |
| `CameraSubsystem` | GROUNDED | Functional owner of capture acquisition and delivery in the current baseline. |
| `RecognitionProcessor` | GROUNDED | Distinct capability that performs recognition. |
| `IdentityDeterminationOutcome` | GROUNDED | Governed outcome of identity determination. |
| `GovernedIdentity` | GROUNDED | Existing governed identity meaning; MR-0003 determines correspondence but does not create/administer it. |
| `AccessAuthorizationState` | GROUNDED | Authorization state concerning a `GovernedIdentity`, governed by MR-0002. |
| `RequiredAccessAuthorizationCondition` | GROUNDED | The authorization condition required by D-1.1 / FR-1.1; its internal property/value representation is not governed. |
| `AccessDecision` | GROUNDED | Decision for the individual access attempt, owned by MR-0001. |
| `ConnectivityService` | GROUNDED | Available connectivity service consumed by the current MR-0003 realization. |
| `Confidentiality` | GROUNDED | Security property governed by SEC-3.4.2-C. |
| `Integrity` | GROUNDED | Security property governed by SEC-3.4.2-I. |
| `AuthorizedProvenance` | GROUNDED | Security property governed by SEC-3.4.2-P. |

No additional first-class family is introduced for participant, behavior, channel, data flow, pipeline, state, property or requirement.

## 4. Controlled BA-local semantic keys and values

These are BA2/BA5 controlled semantic content, not new project APIs or implementation enums.

### 4.1 Identity-determination outcome kind

```text
property key
    outcomeKind

governed value domain
    SUCCESS
    NEGATIVE
    INCONCLUSIVE
```

The values preserve D-3.2 / FR-3.2.1 semantics.

### 4.2 Current delivery medium

```text
property key
    interconnectionMedium

current governed value
    WIRED_ETHERNET
```

This value is scoped only to `RecognitionCaptureDelivery`.

### 4.3 Access-decision result semantics

```text
typed local value domain
    accessDecisionEffect

values
    ALLOWING_ACCESS_DECISION
    NON_ALLOWING_ACCESS_DECISION
```

These values normalize only the governed distinction “decision that allows access” versus “decision that does not allow access”. They are not asserted as a project-side enum or implementation representation.

## 5. Accepted BAPropositions

### P-01 — request concerns the person present

Source: MR-0003 + FR-3.4.1.

```text
reference
  referencer -> IdentityDeterminationRequest
  referenced -> PersonPresentAtAccessPoint
```

No `GovernedIdentity` is referenced by the request.

### P-02 — current identity-determination strategy

Source: D-3.1.

```text
realize
  abstract    -> IdentityDetermination
  realization -> FacialRecognitionStrategy
```

No sensor/model/score/threshold/network mechanism is implied.

### P-03 — current MR-0003 realization

Source: D-3.5.

```text
realize
  abstract    -> IdentityDetermination
  realization -> IdentityDeterminationRealization
```

The referent exists because the governed source explicitly attributes service-consumption semantics to the current realization.

### P-04 — recognition produces the governed outcome

Sources: D-3.2, D-3.4, FR-3.2.1.

```text
produce
  actor  -> RecognitionProcessor
  input  -> RecognitionCapture
  result -> IdentityDeterminationOutcome
```

The proposition does not expose internal technical recognition output.

### P-05 — governed outcome domain

Sources: D-3.2, FR-3.2.1.

```text
constrain
  constraintTarget -> IdentityDeterminationOutcome
  constraintValue
    property   -> outcomeKind
    vocabulary -> [SUCCESS, NEGATIVE, INCONCLUSIVE]
```

No score, confidence, threshold, ranking or `1:N` semantics are introduced.

### P-06 — successful outcome makes a governed identity available

Sources: D-3.2, FR-3.2.1.

```text
reference
  referencer -> IdentityDeterminationOutcome
  referenced -> GovernedIdentity

scopedModifier
  condition -> IdentityDeterminationOutcome.outcomeKind == SUCCESS
```

No corresponding identity reference is asserted for `NEGATIVE` or `INCONCLUSIVE`.

### P-07 — capture/request binding

Sources: FR-3.4.1, FR-3.4.2.

```text
correlate
  correlatedItem     -> RecognitionCapture
  correlationContext -> IdentityDeterminationRequest
```

The binding must survive delivery.

### P-08 — RecognitionCapture delivery

Source: FR-3.4.2.

```text
transfer
  behavior    -> RecognitionCaptureDelivery
  source      -> CameraSubsystem
  destination -> RecognitionProcessor
  content     -> RecognitionCapture
```

This uses the BA2 R3 optional `behavior` role only because other governed meanings must target the same delivery behavior.

### P-09 — connectivity service consumption

Source: D-3.5.

```text
consumeService
  consumer -> IdentityDeterminationRealization
  service  -> ConnectivityService
```

No provider is asserted because no provider identity is governed.

### P-10 — delivery depends on connectivity

Sources: D-3.4, D-3.5.

```text
dependOn
  dependent    -> RecognitionCaptureDelivery
  prerequisite -> ConnectivityService
```

Service use does not transfer project responsibility or authority to a provider.

### P-11 — identity-determination outcome depends on delivery in the current placement

Source: D-3.4.

```text
dependOn
  dependent    -> IdentityDeterminationOutcome
  prerequisite -> RecognitionCaptureDelivery
```

This captures the governed consequence that unavailability of the interaction can prevent completion of identity determination in the current separated placement.

### P-12 — current delivery medium

Source: D-3.6.

```text
constrain
  constraintTarget -> RecognitionCaptureDelivery
  constraintValue
    property   -> interconnectionMedium
    vocabulary -> [WIRED_ETHERNET]
```

No end-to-end provider topology is inferred.

### P-13 — delivery confidentiality

Source: SEC-3.4.2-C.

```text
constrain
  constraintTarget -> RecognitionCaptureDelivery
  constraintValue  -> Confidentiality
```

### P-14 — delivery integrity

Source: SEC-3.4.2-I.

```text
constrain
  constraintTarget -> RecognitionCaptureDelivery
  constraintValue  -> Integrity
```

P-07 preserves the capture/request binding protected by this requirement.

### P-15 — delivery authorized provenance

Source: SEC-3.4.2-P.

```text
constrain
  constraintTarget -> RecognitionCaptureDelivery
  constraintValue  -> AuthorizedProvenance
```

### P-16 — authorization management makes authorization state available

Source: MR-0002.

```text
produce
  actor  -> AccessAuthorizationManagement
  result -> AccessAuthorizationState
```

This does not define internal authorization-state values, lookup, cache, freshness or persistence mechanisms.

### P-17 — authorization state concerns a governed identity

Source: MR-0002.

```text
reference
  referencer -> AccessAuthorizationState
  referenced -> GovernedIdentity
```

### P-18 — macro access-decision production

Sources: MR-0001, D-1.1, FR-1.1.

```text
produce
  actor  -> ControlledAreaAccess
  input  -> IdentityDeterminationOutcome
  input  -> AccessAuthorizationState
  result -> AccessDecision
```

### P-19 — macro decision dependencies

Source: MR-0001.

```text
dependOn
  dependent    -> AccessDecision
  prerequisite -> IdentityDeterminationOutcome
  prerequisite -> AccessAuthorizationState
```

This supports dependency/impact analysis but does not replace the exact rule.

### P-20 — outcome is pertinent to the access attempt

Source: FR-1.1.

```text
correlate
  correlatedItem     -> IdentityDeterminationOutcome
  correlationContext -> AccessAttempt
```

### P-21 — decision belongs to the access attempt

Source: MR-0001.

```text
correlate
  correlatedItem     -> AccessDecision
  correlationContext -> AccessAttempt
```

### P-22 — same-GovernedIdentity cross-MR binding

Sources: MR-0001, D-1.1, FR-1.1.

```text
correlate
  correlatedItem     -> IdentityDeterminationOutcome
  correlatedItem     -> AccessAuthorizationState
  correlationContext -> GovernedIdentity

scopedModifier
  condition -> IdentityDeterminationOutcome.outcomeKind == SUCCESS
```

This preserves same-identity semantics without normalizing authorization state.

### P-23 — exact access-decision rule

Sources: D-1.1, FR-1.1.

```text
decisionRule
  actor  -> ControlledAreaAccess
  input  -> IdentityDeterminationOutcome
  input  -> AccessAuthorizationState
  result -> AccessDecision

  rule
    IF allOf

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

    THEN
      resultAssignment
        target -> AccessDecision
        value  -> ALLOWING_ACCESS_DECISION

    ELSE
      resultAssignment
        target -> AccessDecision
        value  -> NON_ALLOWING_ACCESS_DECISION
```

The `ELSE` is supported because the governed source explicitly excludes allowing decisions for `NEGATIVE`, `INCONCLUSIVE`, and successful determination without the required authorization condition.

## 6. Acquisition representation boundary

FR-3.4.1 explicitly leaves the BA operator choice open.

The source-governed meaning remains:

```text
RecognitionCaptureAcquisition
    responsible capability = CameraSubsystem
    acquired meaning       = RecognitionCapture
    request context        = IdentityDeterminationRequest
```

Current operator candidates impose materially different semantics:

```text
create
observe
produce
combination
```

Therefore:

```text
diagnosis
    MULTIPLE MATERIAL BA CANDIDATES

accepted acquisition operator
    NONE

new acquire operator
    NOT JUSTIFIED
```

The behavior has BAReferent identity because it may be referenced or qualified later, but no unsupported proposition is invented merely to mirror the verb `acquire`.

## 7. BA3 provenance attachments

Every accepted referent/proposition above resolves to the immutable project baseline:

```text
governedBaselineKey
    FACIAL-ACCESS-GOV-R2

source repository revision
    8af2257a1df94fa5a83d4853ed0a1eb4d020c429
```

All accepted current elements are `GROUNDED`: they normalize governed meaning but do not add a methodology-neutral derived project relation requiring a separate derivation rule.

### 7.1 Referent source matrix

| Referent(s) | Baseline-relative source locator |
|---|---|
| `ControlledAreaAccess`, `AccessAttempt`, `AccessDecision` | `candidate-r3/MR-0001_ACCESS_CONTROL.md` / MR-0001 |
| `AccessAuthorizationManagement`, `AccessAuthorizationState` | `candidate-r3/MR-0002_ACCESS_AUTHORIZATION.md` / MR-0002 |
| `IdentityDetermination`, `PersonPresentAtAccessPoint`, `GovernedIdentity` boundary | `candidate-r3/MR-0003_IDENTITY_DETERMINATION.md` / MR-0003 |
| `FacialRecognitionStrategy` | `candidate-r3/MR-0003_DECISIONS.md` / D-3.1 |
| `IdentityDeterminationOutcome` | `candidate-r3/MR-0003_DECISIONS.md` / D-3.2; `MR-0003_FUNCTIONAL_REQUIREMENTS.md` / FR-3.2.1 |
| `CameraSubsystem`, `RecognitionProcessor` | `candidate-r3/MR-0003_DECISIONS.md` / D-3.4 |
| `IdentityDeterminationRealization`, `ConnectivityService` | `candidate-r3/MR-0003_DECISIONS.md` / D-3.5 |
| `IdentityDeterminationRequest`, `RecognitionCapture`, `RecognitionCaptureAcquisition` | `candidate-r3/MR-0003_FUNCTIONAL_REQUIREMENTS.md` / FR-3.4.1 |
| `RecognitionCaptureDelivery` | `candidate-r3/MR-0003_FUNCTIONAL_REQUIREMENTS.md` / FR-3.4.2 |
| `RequiredAccessAuthorizationCondition` | `candidate-r3/MR-0001_DECISIONS.md` / D-1.1; `MR-0001_FUNCTIONAL_REQUIREMENTS.md` / FR-1.1 |
| `Confidentiality` | `candidate-r3/MR-0003_SECURITY_REQUIREMENTS.md` / SEC-3.4.2-C |
| `Integrity` | `candidate-r3/MR-0003_SECURITY_REQUIREMENTS.md` / SEC-3.4.2-I |
| `AuthorizedProvenance` | `candidate-r3/MR-0003_SECURITY_REQUIREMENTS.md` / SEC-3.4.2-P |

### 7.2 Proposition source matrix

| Proposition | Source locator(s) |
|---|---|
| P-01 | MR-0003; FR-3.4.1 |
| P-02 | D-3.1 |
| P-03 | D-3.5 |
| P-04 | D-3.2; D-3.4; FR-3.2.1 |
| P-05 | D-3.2; FR-3.2.1 |
| P-06 | D-3.2; FR-3.2.1 |
| P-07 | FR-3.4.1; FR-3.4.2 |
| P-08 | FR-3.4.2 |
| P-09 | D-3.5 |
| P-10 | D-3.4; D-3.5 |
| P-11 | D-3.4 |
| P-12 | D-3.6 |
| P-13 | SEC-3.4.2-C |
| P-14 | SEC-3.4.2-I |
| P-15 | SEC-3.4.2-P |
| P-16 | MR-0002 |
| P-17 | MR-0002 |
| P-18 | MR-0001; D-1.1; FR-1.1 |
| P-19 | MR-0001 |
| P-20 | FR-1.1 |
| P-21 | MR-0001 |
| P-22 | MR-0001; D-1.1; FR-1.1 |
| P-23 | D-1.1; FR-1.1 |

No proposition uses `DOCUMENTATION_GAPS.md` as standalone project authority.

## 8. Documentation-to-BA coverage matrix

The BA6 completion test treats coverage as semantic coverage for the declared shared scope, not line-by-line prose transcription.

| Governed source | Material shared meaning | BA disposition |
|---|---|---|
| `MR-0001_ACCESS_CONTROL.md` | access-attempt responsibility; inputs; `AccessDecision`; same-identity boundary | P-18, P-19, P-21, P-22 |
| `MR-0001_DECISIONS.md` | conjunctive access policy; positive branch | P-22, P-23 |
| `MR-0001_FUNCTIONAL_REQUIREMENTS.md` | operational use of pertinent outcome; same identity; allowing/non-allowing result rule | P-20, P-22, P-23 |
| `MR-0002_ACCESS_AUTHORIZATION.md` | authorization-management responsibility; state concerning identity; no internal vocabulary | P-16, P-17 + forbidden-inference register |
| `MR-0003_IDENTITY_DETERMINATION.md` | person present; identity not preselected; responsibility boundary; downstream outcome | referents + P-01, P-02, P-04 |
| `MR-0003_DECISIONS.md` / D-3.1 | facial strategy | P-02 |
| D-3.2 | governed outcome distinct from authorization/access decision | P-04, P-05, P-06 |
| D-3.4 | acquisition/recognition separation; delivery necessity | acquisition boundary; P-04, P-08, P-10, P-11 |
| D-3.5 | consumed connectivity service; no transport ownership | P-03, P-09, P-10 |
| D-3.6 | current wired-Ethernet medium; no hidden topology inference | P-12 + forbidden-inference register |
| FR-3.2.1 | outcome domain and success identity | P-04, P-05, P-06 |
| FR-3.2.2 | governed outcome made available downstream without technical-output coupling | P-04 + downstream input in P-18; abstraction boundary preserved |
| FR-3.4.1 | new capture for request; binding; acquisition wording intentionally abstract | P-01, P-07 + acquisition boundary |
| FR-3.4.2 | delivery to processor preserving request binding | P-07, P-08 |
| SEC-3.4.2-C | confidentiality during delivery | P-13 + AUTH-C diagnostic |
| SEC-3.4.2-I | integrity of capture and request binding during delivery | P-07, P-14 |
| SEC-3.4.2-P | authorized provenance for request during delivery | P-15 + AUTH-P diagnostic |
| `DOCUMENTATION_GAPS.md` | governed diagnostic dispositions, not standalone project commitments | diagnostic register only |

Result:

```text
material governed meaning in declared BA6 shared scope
    REPRESENTED or EXPLICITLY PRESERVED AS UNDER-SPECIFIED

unacknowledged semantic omission
    NONE FOUND
```

## 9. Accepted diagnostic register

These are analytical diagnostics / explicit under-specification. They are not project facts created by BA.

### DIAG-01 — acquisition operator ambiguity

```text
source
    FR-3.4.1

status
    MULTIPLE MATERIAL BA CANDIDATES

resolution
    preserve RecognitionCaptureAcquisition behavior identity
    but materialize no acquisition proposition

project-document gap
    NO

BA2 reopen
    NO
```

### DIAG-02 — AUTH-C

```text
source
    SEC-3.4.2-C + DOCUMENTATION_GAPS/AUTH-C

complete basis determining which subjects may know
RecognitionCapture content
    NOT SPECIFIED

blocking current BA acceptance
    NO
```

### DIAG-03 — AUTH-P

```text
source
    SEC-3.4.2-P + DOCUMENTATION_GAPS/AUTH-P

complete evidence/authorization basis establishing which origins
may provide RecognitionCapture for a specific request
    NOT SPECIFIED

blocking current BA acceptance
    NO
```

### DIAG-04 — provider-internal topology

```text
source
    D-3.5 + D-3.6

provider nodes / hops / end-to-end medium
    NOT GOVERNED

BA action
    do not invent
```

## 10. Forbidden-inference register

The accepted BA does not contain or imply:

```text
IdentityDeterminationRequest -> preselected GovernedIdentity
AccessAuthorizationState.authorized
TRUE/FALSE authorization property
AUTHORIZED / NOT_AUTHORIZED / UNKNOWN authorization enum
RecognitionCapture quality score
confidence
threshold
ranking
1:N semantics
DeliveryOutcome
delivery acknowledgement
retry
acceptance state
validation state
provider-internal topology
provider hop list
end-to-end wired provider network
specific communication protocol
TLS
mTLS
certificate
signature
credential
key
MAC
VLAN
attestation
physical gate-opening behavior
```

## 11. Security-scope regression

The three Security Requirements remain scoped only to:

```text
RecognitionCaptureDelivery
```

They are not automatically propagated to:

```text
IdentityDeterminationOutcome
GovernedIdentity
AccessAuthorizationState
AccessDecision
whole facial-access pipeline
```

This regression passes because P-08 provides reusable transfer-behavior identity.

## 12. Decision-rule regression

The BA preserves:

```text
SUCCESS
AND required authorization condition satisfied
AND same GovernedIdentity
    -> ALLOWING_ACCESS_DECISION
```

and the governed non-allowing branches, without inventing an authorization property/value model.

This regression passes because BA2 R3 admits local:

```text
satisfies
  subject
  condition
```

inside `decisionRule`.

## 13. BA4 projection-readiness check

A downstream selective projection may trace:

```text
P-12
    RecognitionCaptureDelivery.interconnectionMedium = WIRED_ETHERNET
```

and construct a method-owned interpretation such as:

```text
a threat whose necessary precondition is
"the governed RecognitionCapture delivery uses an RF/wireless medium"
    -> precondition not satisfied by the governed interaction
```

The same projection must **not** conclude:

```text
the entire consumed connectivity infrastructure
is wired Ethernet end-to-end
```

because provider-internal topology is not governed.

This demonstrates that the BA preserves a useful material distinction while BA4 prevents projection overreach.

## 14. Facial Access BA6-readiness subset matrix

| Gate | Result |
|---|---|
| Exact governed source baseline pinned | PASS |
| Project authority remains upstream of BA | PASS |
| BA1 two-family identity boundary sufficient | PASS |
| BA2 R3 represents all material current relations/actions | PASS |
| Every accepted BA element has source localization | PASS |
| `NOT SPECIFIED` / ambiguity preserved | PASS |
| No unsupported project fact required | PASS |
| No material governed distinction lost | PASS |
| Segment-specific security scope preserved | PASS |
| Same-identity access-decision semantics preserved | PASS |
| Post-BA regression passed | PASS |
| Controlled projection-readiness test passed | PASS |
| New BA1/BA2/BA3/BA4/BA5 counterexample | NONE |
| New project-document semantic gap | NONE |
| Project documentation rewrite required | NO |

## 15. BA baseline disposition

```text
baBaselineKey
    FACIAL-ACCESS-BA-R24-R1

governedBaselineKey
    FACIAL-ACCESS-GOV-R2

sourceRepositoryRevision
    8af2257a1df94fa5a83d4853ed0a1eb4d020c429

declaredSharedScope
    current Facial Access DDTA shared semantics

case BA status
    COMPLETE / POST-BA REGRESSION PASS

integrated BA6 acceptance
    OPEN

universal completeness claim
    NO

future reopen
    concrete governed counterexample
    OR governed source-baseline change requiring revalidation
```

This artifact is retained as immutable Facial Access case-validation evidence once committed.

The R25 pre-holdout program must still execute the structurally different holdout, multiple-projection and governed-change/rebuild gate before an integrated BA6 closure can be claimed.
