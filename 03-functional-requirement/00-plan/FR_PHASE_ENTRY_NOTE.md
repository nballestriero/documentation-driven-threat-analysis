# Functional Requirement phase entry note

**Non-canonical research checkpoint.**

Baseline research repository HEAD before this patch: `438254a4729ffc8c497a69b212ad3cf240e5af7e`.

## Why the study moves downward now

The Macro Requirement and Decision studies have accumulated sufficient horizontal evidence to act as a provisional upper-layer baseline. The current Decision core has survived the independent facial-access example, the ThreatForge construction regression, and the model-layering correction without requiring additional Decision fields. Remaining ThreatForge MR-0003/MR-0004/MR-0005 Decision holdouts are therefore preserved untouched rather than consumed immediately.

The next risk is vertical overfitting: continuing to refine MR and Decision without defining the Functional Requirement level could optimize the upper layers around historical ThreatForge documentation that may itself need to change once downstream obligations and realization are modeled.

The study therefore enters a **Functional Requirement semantic phase before the remaining Decision holdouts**.

This does not invalidate the frozen historical Decision-phase plan. That plan remains evidence of the earlier experimental design. This note records the later methodological correction and the reason for it.

## Provisional upper-layer status

The current status is:

```text
Macro Requirement model
    -> provisional upper-layer baseline

Decision model Revision 7
    -> provisional upper-layer baseline

Functional Requirement
    -> construction phase begins here
```

"Provisional" means that an FR counterexample may force a correction upward. Any such correction must be attributed to explicit vertical evidence and followed by regression over the already admitted MR/Decision evidence.

## Scope discipline

Construction evidence for the FR phase may use:

- ThreatForge MR-0001 and MR-0002 Functional Requirements as historical construction evidence;
- the already admitted revised MR/Decision interpretation for those construction concerns;
- a newly authored independent facial-access FR example.

The following remain outside construction evidence:

- ThreatForge MR-0003/MR-0004/MR-0005 Requirement bodies and registries;
- their still-unconsumed Decision holdouts;
- Security/Governance/Privacy specialized-requirement semantics except as boundary observations already known from the inventory.

The goal is to avoid learning the FR model from the same holdouts later used to challenge the combined hierarchy.

## Updated experimental direction

```text
MR provisional baseline
    +
Decision Revision 7 provisional baseline
    |
    v
Functional Requirement construction model
    |
    v
ThreatForge MR-0001/MR-0002 FR regression
    |
    v
independent facial-access FR authoring
    |
    v
vertical MR -> Decision -> FR regression
    |
    v
correction/regression if required
    |
    v
Specialized Requirement study
    |
    +--> Security derivation: Analysis Record -> Finding -> SEC
    |
    v
remaining ThreatForge holdouts with stronger vertical model
```

## Primary vertical question

The FR phase must not assume that the historical ThreatForge relation `FR -> exactly one Decision` is already correct merely because IDs and registries encode it.

The central structural experiment is:

> Does every independently meaningful Functional Requirement have one natural Decision parent, or can a Functional Requirement be directly owned by a Macro Requirement while being constrained/operationalized by zero or more Decisions?

A mandatory Decision parent is retained as a working hypothesis, not a closed invariant, until this question is tested on construction and independent evidence.

## Realization boundary

The FR phase also introduces, but does not yet fully model, two downstream relation families:

```text
FunctionalRequirement -- realizedBy --> RealizationArtifact
Requirement           -- verifiedBy --> VerificationEvidence
```

These relations must not make source-code paths, framework choices, implementation state, or test tooling part of the intrinsic FR semantics.

A file existing is not evidence that a requirement is satisfied. Realization and verification remain distinct.

## Specialized-requirement boundary

For this phase, "Requirement" means **Functional Requirement** unless explicitly qualified.

Security, Governance and Privacy are treated as later specialized requirements that enrich/constrain an FR. Their shared semantic superclass and exact relation vocabulary remain open.

Security has an additional derivation constraint to be studied later:

```text
AnalysisRecord
    -> CommonFinding
    -> accepted Finding
    -> SecurityRequirement
    -> FunctionalRequirement
```

The Functional Requirement model must therefore remain usable without embedding STRIDE, STRIDE-AI or other analysis-method semantics into the FR itself.
