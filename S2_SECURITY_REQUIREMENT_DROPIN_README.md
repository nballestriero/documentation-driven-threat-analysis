# DDTA S2 SecurityRequirement — commit drop-in

## Expected repository baseline

```text
b9bbe690ba9f73e38f75ff9e7d8d36a88a16f49a
```

This drop-in is additive. It creates:

```text
05-security-requirement/
  README.md
  SHA256SUMS.txt
  01-metamodel/
    DDTA_SECURITY_REQUIREMENT_S2_R1.tex
    DDTA_SECURITY_REQUIREMENT_S2_R1.pdf
    README.md

S2_SECURITY_REQUIREMENT_DROPIN_README.md
```

It does **not** modify Chapter 4, `04-specialized-requirement/`, or `INDEX.md`.

## Semantic status

S2 is CLOSED for the current baseline:

- `SecurityRequirement IS-A SpecializedRequirement`;
- `protectedSecurityProperty : SecurityProperty [1]`;
- security failure mode must be explicit in normative clauses;
- SecurityRequirement identity is cause-neutral;
- one coherent SecurityRequirement has one governing security property;
- attack description, ordinary functional correctness and realization/control are not SecurityRequirement semantics.

Still OPEN/DEFERRED:

- `SecurityProperty` taxonomy/refinement;
- possible future structural `SecurityFailureMode` identity;
- Base Analysis / BAE;
- AnalysisRun / Finding;
- STRIDE;
- Attack / ThreatEvent / Incident / Vulnerability / Risk / Control;
- analysis coverage;
- provenance/change-event and revision model;
- verification evidence.

## Suggested commit

```text
thesis: formalize SecurityRequirement S2
```
