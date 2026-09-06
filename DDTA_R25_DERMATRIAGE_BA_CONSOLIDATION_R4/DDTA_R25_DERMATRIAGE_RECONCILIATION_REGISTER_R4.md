# DermaTriage Reconciliation Register — R4

## R-01 Responsibility/property canonicalization
OPEN.

## R-02 Specialist routing identity
OPEN; reconcile at MR-02.

## R-03 Image optionality
`RESOLVED_FOR_CURRENT_EVIDENCE`.

## R-04 Triage result identity family
OPEN:

```text
TriageUrgencyAssessment
ImageUrgencyClassification
SymptomBasedUrgency
AITriageSynthesis
TriageOutcome
OperationalPriority
```

FR-19 strengthens the review because AITriageSynthesis contains `urgency`.

## R-05 Confidence identity / binding
OPEN.

Need to reconcile:

```text
FR-16 classification Confidence
FR-19 AITriageSynthesis.confidence
FR-02 applicable confidence
```

Same lexical name does not prove identical semantic value.

## R-06 Triage process/path identity
OPEN.

Reconcile:

```text
ImageBasedTriagePipeline
SymptomOnlyTriageProcess
DirectTriagePath
B4IntegratedTriagePath
DermaTriageTriageProcess
```

Do not merge process/path/pipeline identities by name similarity. Recheck FR-22.
