---
title: "DDTA R24 Facial Access AUTH-P checkpoint - R1"
---

# DDTA R24 Facial Access AUTH-P checkpoint

**Status:** ACTIVE R24 EXECUTION REFINEMENT — BOUNDED AUTH-P DISPOSITION
**Prepared against repository baseline:** `59f7d09b98112139bb0445e48e6a99cfe748d5aa`

## 1. Purpose

This checkpoint records the bounded disposition of the Facial Access clarification question `AUTH-P`:

> quale evidenza governata determina quali origini sono autorizzate a fornire `RecognitionCapture` per una `IdentityDeterminationRequest`?

The current validation corpus is intended to demonstrate the DDTA documentation-to-Base-Analysis process and later the controlled integration of multiple analysis methods. It is not intended to fully specify every project authorization or attestation mechanism before that process is exercised.

## 2. Current governed meaning

`FR-3.4.1` and `FR-3.4.2` already govern that `CameraSubsystem` acquires a `RecognitionCapture` for an `IdentityDeterminationRequest` and delivers it to `RecognitionProcessor` while preserving the binding to that same request.

`SEC-3.4.2-P` separately governs:

```text
parent behavior
    FR-3.4.2 RecognitionCapture delivery

protectedSecurityProperty
    AuthorizedProvenance

normative obligation
    provenance of the delivered RecognitionCapture
    MUST be established as authorized to provide
    that capture for the relevant IdentityDeterminationRequest

failure mode
    delivery occurs without the provenance being
    established as authorized for that request
```

The current corpus does **not** govern the complete evidence or authorization basis by which an origin is established as authorized for a specific request.

## 3. Bounded disposition

`AUTH-P` is retained as:

**PRESERVED CLARIFICATION / ANALYSIS-RELEVANT PROJECT MEANING NOT SPECIFIED / NON-BLOCKING FOR THE CURRENT PROCESS-DEMONSTRATION CORPUS.**

This means:

```text
AuthorizedProvenance obligation
    -> GOVERNED

security-property anchor SEC-3.4.2-P
    -> GOVERNED

functional acquisition/delivery owner = CameraSubsystem
    -> GOVERNED

capture/request binding
    -> GOVERNED

complete evidence/authorization basis proving
an origin is authorized for a specific request
    -> NOT SPECIFIED

silently infer the provenance policy
    -> FORBIDDEN

new attestation/authentication policy now
    -> NOT REQUIRED

new Decision / FR / SR now
    -> NOT JUSTIFIED

new BA contract now
    -> NOT JUSTIFIED

promotion blocker for this demonstration corpus
    -> NO
```

## 4. Functional source is not the complete provenance policy

The documentation governs `CameraSubsystem` as the functional owner of acquisition and delivery. That fact must not be silently strengthened into a complete project rule saying that the functional source identity alone constitutes sufficient authorization evidence for every delivered capture.

The distinction retained is:

```text
CameraSubsystem
    -> governed functional source / responsibility owner

evidence establishing an origin as authorized
for IdentityDeterminationRequest X
    -> NOT SPECIFIED
```

This preserves the project meaning without inventing device identity, instance identity, trust anchors, credentials, certificates, keys, signatures or attestation semantics.

## 5. Why this is sufficient for the thesis process experiment

`SEC-3.4.2-P` remains a stable project-owned SecurityRequirement that future analysis methods can address.

A later analysis may ask what proves that a particular origin is authorized for a particular request. DDTA can preserve that question and trace it back to the existing SecurityRequirement without allowing the analysis method to invent the project answer.

The intended process is:

```text
project documentation
      |
      v
SEC-3.4.2-P
      |
      v
Base Analysis
      |
      +--------------------------+
      |                          |
      v                          v
future method A              future method B
      |                          |
      +------------+-------------+
                   |
                   v
        analysis-relevant question
                   |
                   v
          AUTH-P / NOT SPECIFIED
                   |
                   v
       governed review if needed
```

Analysis outputs remain downstream and method-owned. They may expose missing project meaning; they do not become project authority automatically.

## 6. Boundaries retained

This microstep does not introduce or prescribe:

- certificates;
- signatures;
- device credentials;
- mTLS;
- attestation;
- keys or MACs;
- allow-lists;
- protocol or transport authentication;
- an origin vocabulary or device-instance model;
- a new Decision, Functional Requirement or Security Requirement;
- a new BA contract.

`SEC-3.4.2-P` and the other MR-0003 Security Requirements remain unchanged.

## 7. Candidate state after this disposition

```text
corpusKey
    facial-access-candidate-r3

corpusRevision
    R3-CANDIDATE-7

authorityStatus
    EXPERIMENTAL_NON_CANONICAL

primaryBASourceAllowed
    false
```

AUTH-P is no longer a blocker for the current demonstration-corpus promotion path.

## 8. Next bounded microstep

The next authorized bounded review is **DG-FA-006 only**:

```text
IF identity determination is successful
AND the required authorization condition is satisfied
THEN AccessDecision MUST ALLOW
```

Do not perform promotion, accepted BA rebuild, STRIDE/STRIDE-AI integration, or lifecycle/test/code traceability work in the same microstep.
