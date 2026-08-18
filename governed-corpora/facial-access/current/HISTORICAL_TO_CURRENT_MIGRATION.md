# Facial-access historical → current migration provenance

## Why a new corpus exists

The historical material is intentionally preserved unchanged because it records the evolution of the DDTA documentation model. It must not be rewritten in place.

The current corpus applies the later documentation-layer closure to the same study domain so that the effect on Base Analysis can be measured.

## MR-0003

Historical:

```text
MR-0003
Riconoscimento facciale per la verifica della persona
```

Current R1:

```text
MR-0003
Verifica dell'identità al punto di accesso
```

The current MR removes the chosen verification mechanism from the macro identity. This package treats the change as a governed documentation migration for the validation corpus. It does **not** pre-decide BA cross-baseline continuity; the later BA comparison must determine which shared meanings are retained, replaced or newly materialized.

## Facial recognition moves down

Historical MR-level commitment:

```text
facial recognition
camera
ML model
```

Current:

```text
MR-0003 identity verification
    |
    `-- D-3.1 choose facial recognition
```

Camera/recognition placement is still lower:

```text
D-3.4 separate CameraSubsystem and RecognitionProcessor
```

Transport ownership and medium remain separate Decisions:

```text
D-3.5 consume external/local connectivity
D-3.6 wired Ethernet
```

## Historical Decision mapping

| Historical source | Current R1 | Treatment |
|---|---|---|
| MR-0003/ADR-0001 — recognition produces identity evidence, not access decision | D-3.2 | semantic responsibility preserved and re-parented under generalized MR |
| MR-0003/ADR-0002 — stable outcome semantics vs ML model | D-3.3 | semantic responsibility preserved |
| S1 D-3.3 — remote recognition placement | D-3.4 | re-authorized in current branch |
| S1 D-3.4 — transport responsibility boundary | D-3.5 | re-authorized in current branch |
| S1 D-3.5 — Ethernet medium | D-3.6 | re-authorized in current branch |

## Historical FR mapping

| Historical source | Current R1 |
|---|---|
| S1 FR-3.3 Acquire RecognitionCapture | FR-3.4.1 |
| S1 FR-3.4 Deliver RecognitionCapture | FR-3.4.2 |

R1 additionally materializes operational FRs for the already-governed semantics of D-3.2 and D-3.3:

- `FR-3.2.1 Produce identity-verification evidence`
- `FR-3.3.1 Expose governed recognition outcome`

These are new current-corpus authoring decisions and must be tested by the later BA comparison rather than assumed to improve the method.

## Historical SpecializedRequirement mapping

The S1 examples for Confidentiality, Integrity and Authorized Provenance predated/served the S2 closure. In current R1 they are written explicitly as SecurityRequirements:

- `SEC-3.4.2-C`
- `SEC-3.4.2-I`
- `SEC-3.4.2-P`

Each has one `protectedSecurityProperty` and an explicit failure mode.

## What is deliberately not migrated yet

- MR-0001 branch and the exact access-decision consumer target;
- MR-0002 branch;
- the historical MR-0004 decomposition;
- complete topology;
- test/code trace model;
- Base Analysis;
- threat-method overlays.

Those omissions are explicit so that "not yet migrated" is never silently interpreted as "project does not contain".
