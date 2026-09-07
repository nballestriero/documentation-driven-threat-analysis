# DermaTriage MR-04 / DEC-07 / DEC-08 / DEC-09 Progress Checkpoint — R10

## Branch state

```text
MR-04:
    FIRST-PASS IN PROGRESS

DEC-04:
    FIRST-PASS BRANCH COMPLETE

DEC-05:
    FIRST-PASS BRANCH COMPLETE

DEC-06:
    FIRST-PASS BRANCH COMPLETE

DEC-07:
    FIRST-PASS BRANCH COMPLETE
    no active concrete SpecializedRequirement

DEC-08:
    FIRST-PASS BRANCH COMPLETE
    FR-10 ANALYZED

DEC-09:
    FIRST-PASS BRANCH COMPLETE
    FR-06 ANALYZED

next:
    DEC-10
```

## DEC-07 result

```text
SensitivityNonDegradationCriterion
    classify -> AcceptanceCriterion

FalseLowPerformanceNonDegradationCriterion
    classify -> AcceptanceCriterion

OverallAccuracyDegradationToleranceCriterion
    classify -> AcceptanceCriterion
    constraint literal -> 5%

ClassifierAdaptationQualificationCondition
    dependOn ->
      SensitivityNonDegradationCriterion
      FalseLowPerformanceNonDegradationCriterion
      OverallAccuracyDegradationToleranceCriterion
```

P-05 / P-06 are further strengthened.

## DEC-08 / FR-10 result

```text
PostAdoptionAccuracyDegradationThreshold
    classify -> Threshold
    constraint literal -> 5%

ClassifierAdaptationRevocationCondition
    dependOn ->
      AdoptedClassifierAdaptation
      PostAdoptionAccuracyDegradationThreshold
      ApplicablePostAdoptionReference

ClassifierAdaptationRevocation
    classify -> Behavior

ClassifierAdaptationRestoration
    classify -> Behavior
    realize -> ClassifierAdaptationRevocation

DermaTriage
    assignResponsibility ->
      ClassifierAdaptationRevocationSupportResponsibility

ModelVersionsStore
    classify -> Store

ModelVersionTrackingArtifact
    classify -> Artifact

ActiveClassifierModelArtifact
    classify -> Artifact
```

P-08 is strongly strengthened by governed persistence bindings.

`transition` remains not positively tested.

## DEC-09 / FR-06 result

```text
PromptEvolutionEvidenceWindow
    classify -> EvidenceWindow

PromptEvolutionEvidenceSet
    classify -> EvidenceSet

PromptEvolutionEvidenceWindowSize
    constrain -> 20

PromptEvolutionEvidenceSet
    dependOn -> PromptEvolutionEvidenceWindow

DermaTriage
    produce ->
      PromptEvolutionEvidenceSet
    input ->
      RecentPertinentClinicalCorrections
```

New unnumbered pressure:

```text
BOUNDED_RECENCY_SELECTION_SEMANTICS
```

because current BA cannot structurally preserve the governed top-N recency membership rule.

## Documentation gaps materially exercised

```text
GAP-DERMA-ACCEPT-BINDING-01
GAP-DERMA-EVAL-CONSISTENCY-01
GAP-DERMA-ROLLBACK-BINDING-01
GAP-DERMA-PROMPT-WINDOW-01
```

## Reconciliation

```text
R-13:
    OPEN / further strengthened

R-14:
    OPEN / carried

R-15:
    OPEN / new
```

## Closure

```text
DEC-07:
    CLOSED FOR FIRST-PASS EVIDENCE COLLECTION

DEC-08:
    CLOSED FOR FIRST-PASS EVIDENCE COLLECTION

DEC-09:
    CLOSED FOR FIRST-PASS EVIDENCE COLLECTION

MR-04:
    REMAINS OPEN
```

Next bounded source:

```text
DEC-10
```

Remaining active bounded source elements:

```text
8
```
