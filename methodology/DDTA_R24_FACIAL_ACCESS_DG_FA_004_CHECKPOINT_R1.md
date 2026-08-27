---
title: "DDTA R24 Facial Access DG-FA-004 checkpoint - R1"
---

# DDTA R24 Facial Access DG-FA-004 checkpoint

**Status:** ACTIVE R24 EXECUTION REFINEMENT — BOUNDED DG-FA-004 DISPOSITION
**Prepared against repository baseline:** `1af0975084f8d8d392e8556ac1e267d0ced2545b`

## 1. Purpose

This checkpoint records the bounded review of historical `DG-FA-004 — intermediate transport nodes` against the active experimental Facial Access successor.

The review tests whether the missing provider-internal hops are a documentation defect and then follows the stronger pressure exposed by the actual Facial Access flow: whether governed multi-stage / branched processing and segment-specific properties can be preserved by Base Analysis without inventing intermediate topology.

This microstep does not modify Base Analysis and does not review `DG-FA-005`, `DG-FA-006` or the `AUTH-C` / `AUTH-P` clarification questions.

## 2. Authority state retained

```text
corpusKey
    facial-access-candidate-r3

corpusRevision after this disposition
    R3-CANDIDATE-4

authorityStatus
    EXPERIMENTAL_NON_CANONICAL

researchRole
    CURRENT_THESIS_VALIDATION_CORPUS

primaryBASourceAllowed
    false
```

This review does not promote the candidate and does not authorize an accepted Facial Access Base Analysis.

## 3. Historical DG-FA-004 question

The historical wording focused on intermediate transport nodes such as switches, firewalls or other hops.

The current project documentation does not govern provider-internal transport nodes. `D-3.5` deliberately places the underlying transport infrastructure outside project ownership/management, while `D-3.6` explicitly forbids inferring hidden topology, hops, protocols or ungoverned service properties from the wired-Ethernet realization fact.

Therefore:

```text
provider-internal hop not governed
    -> not a current documentation defect
    -> do not invent it
```

A downstream analysis need does not by itself turn hidden provider topology into project truth.

## 4. Reframing from transport hops to governed pipeline preservation

The bounded review found that the current Facial Access candidate already contains a real governed multi-stage / branched flow.

At the current documentation boundary:

```text
CameraSubsystem
    |
    | RecognitionCapture delivery
    v
RecognitionProcessor
    |
    | produces / makes available
    v
IdentityDeterminationOutcome
    |
    +------------------------------+
                                   |
                                   v
                          ControlledAreaAccess
                                   ^
                                   |
                    AccessAuthorizationState
                    concerning the same
                    GovernedIdentity X
                                   |
                                   v
                            AccessDecision
```

The physical opening of the gate remains outside the currently governed responsibility boundary and is not added to this flow.

The flow is not a homogeneous network path. Different relations carry different meanings: acquisition, delivery, production/availability, same-identity correlation, authorization-state use and access-decision determination.

## 5. Segment-specific security properties are material

The current Security Requirements `SEC-3.4.2-C`, `SEC-3.4.2-I` and `SEC-3.4.2-P` are scoped to execution of `FR-3.4.2`.

They therefore constrain the governed `RecognitionCapture` delivery behavior:

```text
CameraSubsystem
    |
    | RecognitionCapture delivery
    |   Confidentiality
    |   Integrity
    |   AuthorizedProvenance
    v
RecognitionProcessor
```

The review found no authority to propagate these properties automatically to:

- `IdentityDeterminationOutcome`;
- the `AccessAuthorizationState` branch;
- `AccessDecision`;
- the entire end-to-end Facial Access flow.

A Base Analysis that collapses these local properties into a generic "secure pipeline" or global property would strengthen project meaning beyond the sources.

## 6. Working BA pressure test

The pressure test used the retained BA contracts only as working analytical evidence; candidate R3 remains non-canonical and cannot ground an accepted BA.

Results:

```text
BA1 identity families
    -> sufficient for the current pressure test

multiple governed stages
    -> representable

branch / convergence
    -> representable

same-identity correlation
    -> representable

multiple consecutive transfers
    -> representable

opaque ungoverned provider region
    -> representable by omission / no invention

segment-specific reusable qualification
    -> concrete BA2 representation pressure
```

The pressure is not the existence of a first-class `Pipeline` type. It is the need, when the source requires it, to give the particular conveyance behavior reusable semantic identity so that other propositions can address the same behavior.

## 7. Smallest working BA2 candidate retained, not accepted

The smallest candidate that survived the bounded falsification test is an optional behavior binding on `transfer`:

```text
transfer
  behavior    -> <BAReferent> [0..1]   # working candidate only
  source      -> <BAReferent> [1]
  destination -> <BAReferent> [1..*]
  content     -> <BAReferent> [1..*]
```

For the current case the reusable behavior referent would denote the governed `RecognitionCapture` delivery.

That would allow, in principle, the same behavior identity to participate in separate propositions concerning:

```text
consumed ConnectivityService
current wired-Ethernet realization
Confidentiality
Integrity
AuthorizedProvenance
```

without treating the `RecognitionCapture`, the source/destination capabilities or the entire pipeline as the target of those meanings.

This is a **working smallest-solution candidate**, not a BA2 contract change.

## 8. Generalizations not justified by this review

Current evidence does not justify:

```text
new first-class Pipeline family
global Pipeline BAReferent required by default
contains / partOf pipeline-stage relations
new pipeline semantic operator
channel / path document fields
provider-internal network nodes
behavior role generalized to every BA2 operator
generic BAProposition semanticSubject field
```

Those ideas remain outside the action backlog unless a later governed counterexample requires them.

In particular, a behavior referent must not be created automatically merely because every proposition could technically be reified. BA1 identity criteria remain the gate: independently reusable project meaning earns referent identity; assertion identity remains BAProposition identity.

## 9. DG-FA-004 disposition

Historical `DG-FA-004` is therefore:

**REFRAMED — NOT A CURRENT DOCUMENTATION GAP / CONCRETE BA2 SEGMENT-IDENTITY PRESSURE RETAINED.**

The review concludes:

```text
missing hidden provider hops
    -> not a documentation gap

governed intermediate stage
    -> must remain recoverable

segment-specific governed property
    -> must remain attached to the correct governed behavior/segment

current BA working test
    -> exposes reusable transfer-behavior identity pressure

BA2 modification now
    -> NOT AUTHORIZED
```

The pressure must be reproduced during the minimum BA rebuild from an explicitly promoted successor baseline before BA2 is changed.

## 10. Files intentionally not changed semantically

This disposition does not modify:

- `MR-0001_ACCESS_CONTROL.md`;
- `MR-0002_ACCESS_AUTHORIZATION.md`;
- `MR-0003_IDENTITY_DETERMINATION.md`;
- any Decision;
- any Functional Requirement;
- any Security Requirement;
- `BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`;
- `BA2_RELATION_ACTION_VOCABULARY_R2.md`;
- BA3, BA4 or BA5 contracts.

The result is recorded only in gap/status/provenance/work-plan artifacts.

## 11. Required future BA retest

After documentation completion, full semantic regression and explicit promotion:

1. rebuild the minimum justified Facial Access BA from the promoted sources;
2. reproduce the multi-stage / branched flow from source meaning;
3. preserve `RecognitionCapture` delivery/service/medium binding;
4. preserve the local scope of `SEC-3.4.2-C/I/P`;
5. determine whether current BA2 still lacks reusable identity for the transfer behavior;
6. only if the failure persists, reopen the smallest BA contract;
7. rerun semantic regression and downstream usefulness tests.

The currently strongest smallest candidate is `transfer.behavior 0..1`, but promotion/rebuild evidence remains mandatory before acceptance.

## 12. Next microstep

The next bounded documentation-gap review is **DG-FA-005 only — test/code evidence linkage**.

Do not review DG-FA-006, AUTH-C/AUTH-P, promotion, accepted BA rebuild or BA2 modification in the same microstep.
