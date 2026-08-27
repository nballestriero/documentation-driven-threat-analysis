---
title: "DDTA R24 Facial Access AUTH-C checkpoint - R1"
---

# DDTA R24 Facial Access AUTH-C checkpoint

**Status:** ACTIVE R24 EXECUTION REFINEMENT — BOUNDED AUTH-C DISPOSITION
**Prepared against repository baseline:** `1305b03301bf5790a5083e78526a9c24940587c0`

## 1. Purpose

This checkpoint records the bounded disposition of the Facial Access clarification question `AUTH-C`:

> quale evidenza governata determina chi è autorizzato a conoscere il contenuto di `RecognitionCapture`?

The purpose of the current validation corpus is to demonstrate the DDTA documentation-to-Base-Analysis process and later the controlled integration of multiple analysis methods. It is not to fully specify every project policy or implementation detail before that process is exercised.

## 2. Current governed meaning

`SEC-3.4.2-C` already governs:

```text
parent behavior
    FR-3.4.2 RecognitionCapture delivery

protectedSecurityProperty
    Confidentiality

normative obligation
    RecognitionCapture content MUST NOT become intelligible
    to subjects unauthorized to know it

failure mode
    RecognitionCapture content becomes intelligible
    to an unauthorized subject during delivery
```

The current corpus does **not** govern the complete authorization basis that determines which subjects are authorized to know that content.

## 3. Bounded disposition

`AUTH-C` is retained as:

**PRESERVED CLARIFICATION / ANALYSIS-RELEVANT PROJECT MEANING NOT SPECIFIED / NON-BLOCKING FOR THE CURRENT PROCESS-DEMONSTRATION CORPUS.**

This means:

```text
Confidentiality obligation
    -> GOVERNED

security-property anchor SEC-3.4.2-C
    -> GOVERNED

who is authorized to know RecognitionCapture content
    -> NOT SPECIFIED

silently infer authorized subjects
    -> FORBIDDEN

new authorization policy now
    -> NOT REQUIRED

new Decision / FR / SR now
    -> NOT JUSTIFIED

new BA contract now
    -> NOT JUSTIFIED

promotion blocker for this demonstration corpus
    -> NO
```

## 4. Why this is sufficient for the thesis process experiment

DDTA does not require project documentation to anticipate every question that every later analysis method may ask.

The documentation must instead preserve the distinction between:

```text
known governed fact
unknown / not-specified project fact
analysis-derived question
eventual governed correction if the project later chooses to answer it
```

`SEC-3.4.2-C` therefore remains a stable project-owned security obligation and a semantic bridge that future analysis results may address.

A later method-specific analysis may identify that its reasoning needs the authorization basis. That question can be traced back to the existing Security Requirement without allowing the analysis method to invent the project answer.

## 5. Boundaries retained

This microstep does not infer that:

- `CameraSubsystem` and `RecognitionProcessor` are the complete set of subjects authorized to know the capture;
- `MR-0002` access authorization is also authorization to know `RecognitionCapture`;
- any operator, administrator, service or other subject is authorized or unauthorized;
- TLS, mTLS, certificates, credentials, ACLs, roles or any other realization mechanism are required.

`MR-0002` remains about access authorization associated with `GovernedIdentity`; it is not reused as a confidentiality-disclosure policy.

## 6. SecurityRequirement role retained

The current Security Requirement structure is not reopened.

For the process-demonstration corpus:

```text
project documentation
      |
      v
SEC-3.4.2-C
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
          AUTH-C / NOT SPECIFIED
                   |
                   v
       governed review if needed
```

Analysis outputs remain downstream. They may expose missing project meaning; they do not become authority automatically.

## 7. Candidate state after this disposition

```text
corpusKey
    facial-access-candidate-r3

corpusRevision
    R3-CANDIDATE-6

authorityStatus
    EXPERIMENTAL_NON_CANONICAL

primaryBASourceAllowed
    false
```

AUTH-C is no longer a blocker for the current demonstration-corpus promotion path.

## 8. Editorial repair included

The previous DG-FA-005 apply accidentally left the literal prefix `6342` immediately before the heading `## Deliberately unresolved meaning` in `candidate-r3/README.md`.

This microstep repairs that heading to:

```text
## Deliberately unresolved meaning
```

This is an editorial repair only and carries no semantic change.

## 9. Next bounded microstep

The next authorized bounded review is **AUTH-P only**:

> quale evidenza governata determina quali origini sono autorizzate a fornire `RecognitionCapture` per una `IdentityDeterminationRequest`?

Do not review `DG-FA-006`, promotion, accepted BA rebuild, STRIDE/STRIDE-AI or lifecycle/test/code traceability in the same microstep.
