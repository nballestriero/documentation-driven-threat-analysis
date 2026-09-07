# DermaTriage Reconciliation Register — R9

Carried:

```text
R-09 Original DermaTriage Outcome identity
    OPEN

R-10 Validation / ValidatedOutcome / ClinicalReviewResult identity
    OPEN

R-11 B4 Client identity / logical placement
    RESOLVED_FOR_CURRENT_EVIDENCE

R-12 Administrative Client identity / placement
    OPEN

R-13 Clinical Review Evidence Identity / Lineage
    OPEN / FURTHER STRENGTHENED
```

## R-13 — Clinical Review Evidence Identity / Lineage

R9 reinforces path specificity:

```text
ClinicalReviewDerivedEvidence
    ?
AccumulatedPromptCorrectionEvidence
    ?
QualifiedClassifierDisagreementEvidence
    ?
AccumulatedClassifierEvidence
```

FR-14 explicitly prevents qualification for one adaptation path from being automatically
treated as qualification for another path.

`BAREF-DERMA-078 QualifiedClassifierDisagreementEvidence` remains
`PROVISIONAL_RECONCILIATION` and must be rechecked at FR-07.

## R-14 — Classifier Reference Model Identity / Lineage

**Status:** `OPEN — ADDED IN R9`

```text
EfficientNetB4ReferenceModelVersion1_0_0
    ?
EfficientNetBaseline
    ?
BestBaselineCheckpoint
```

Potential relationships:

```text
same identity
realization
selected checkpoint
versioned model
derived artifact
reference designation
```

No relationship is selected by inference.

FR-09 confirms that an applicable reference version participates in classifier-adaptation
qualification, but does not resolve its lineage relative to the earlier baseline/checkpoint
identities.
