# DermaTriage Reconciliation Register — R10

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

R-14 Classifier Reference Model Identity / Lineage
    OPEN / CARRIED
```

## R-13 — Clinical Review Evidence Identity / Lineage

R10 adds prompt-side selection identities:

```text
ClinicalReviewDerivedEvidence
    ?
AccumulatedPromptCorrectionEvidence
    ?
RecentPertinentClinicalCorrections
    ?
PromptEvolutionEvidenceWindow
    ?
PromptEvolutionEvidenceSet
    ?
QualifiedClassifierDisagreementEvidence
    ?
AccumulatedClassifierEvidence
```

Do not merge:

```text
activation accumulation
    with
current-cycle evidence selection
```

even when the same underlying clinical correction could participate in both analytical roles.

`BAREF-DERMA-078 QualifiedClassifierDisagreementEvidence` remains
`PROVISIONAL_RECONCILIATION` and is still scheduled for recheck at FR-07.

## R-14 — Classifier Reference Model Identity / Lineage

Carried open:

```text
EfficientNetB4ReferenceModelVersion1_0_0
    ?
EfficientNetBaseline
    ?
BestBaselineCheckpoint
```

## R-15 — Post-Adoption Reference Identity / Lineage

**Status:** `OPEN — ADDED IN R10`

```text
ApplicablePostAdoptionReference
    ?
EfficientNetB4ReferenceModelVersion1_0_0
    ?
EfficientNetBaseline
    ?
BestBaselineCheckpoint
```

Pre-adoption and post-adoption reference roles must not be merged by inference.

## Active classifier artifact reconciliation

`BAREF-DERMA-105 ActiveClassifierModelArtifact` is `PROVISIONAL_RECONCILIATION`.

It must remain distinct until source evidence resolves relationships among:

```text
ActiveClassifierModelArtifact
EfficientNet-B4 capability/model meaning
BestBaselineCheckpoint
reference model version
adopted classifier adaptation
future fine-tuned model versions
```

No identity merge is authorized in R10.
