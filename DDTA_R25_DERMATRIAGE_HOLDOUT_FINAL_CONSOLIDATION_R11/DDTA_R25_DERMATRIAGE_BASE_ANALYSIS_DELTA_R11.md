# DermaTriage Base Analysis — Delta R11

**Disposition:** `FIRST_PASS_EVIDENCE_COLLECTION_COMPLETE`
**Methodology:** `BA0–BA6 FROZEN THROUGH HOLDOUT`
**New numbered pressure:** `NONE`

R11 consolidates the final four DermaTriage branches.

---

# 1. DEC-10 / FR-07 — Clinical disagreement as classifier-adaptation evidence

The source governs a normative semantic concept:

```text
ClinicianDisagreement
```

and explicitly distinguishes it from its current payload encoding:

```text
agrees == False
```

The encoding is state/data representation, not the identity of the governed concept.

New referents:

```text
BAREF-DERMA-114 ClinicianDisagreement
    WORKING_ACCEPTED

BAREF-DERMA-115 EvidenceQualificationCondition
    WORKING_ACCEPTED
    semantic kind
```

Forward classification:

```text
BAPROP-DERMA-FR07-001
classify(
  classifiedReferent=ClinicianDisagreement,
  semanticKind=EvidenceQualificationCondition
)
```

The previously provisional:

```text
BAREF-DERMA-078 QualifiedClassifierDisagreementEvidence
```

is now:

```text
WORKING_ACCEPTED
SPECIFIC_RECONCILIATION_RESOLVED
```

because FR-07 directly governs the disagreement-based qualification meaning.

Accepted prerequisite:

```text
BAPROP-DERMA-FR07-002
dependOn(
  dependent=QualifiedClassifierDisagreementEvidence,
  prerequisite=ClinicianDisagreement
)
```

Operational rule:

```text
BAPROP-DERMA-FR07-003

decisionRule

actor:
  DermaTriage

input:
  ClinicalReviewResult

result:
  QualifiedClassifierDisagreementEvidence

rule:
  IF
    satisfies(
      subject=ClinicalReviewResult,
      condition=ClinicianDisagreement
    )

  THEN
    resultAssignment(
      target=QualifiedClassifierDisagreementEvidence,
      value=QUALIFIED_FOR_CLASSIFIER_ADAPTATION
    )

  ELSE:
    OMITTED_NO_IMPLIED_MEANING
```

The BA intentionally does not replace the governed concept with a normalized
`ClinicalReviewResult.agrees = FALSE` ontology fact.

Cross-branch evidence:

```text
FR-07 qualifies the evidence
FR-05 consumes that qualified evidence for accumulation/activation
```

Therefore:

```text
DATA_EVIDENCE_CONSUMPTION_SEMANTICS
    FURTHER_STRENGTHENED
```

R-13 is partially resolved:

```text
QualifiedClassifierDisagreementEvidence:
    identity now accepted

broader clinical-review evidence lineage:
    remains open
```

Source-governed gap:

```text
GAP-DERMA-REVIEW-DISAGREEMENT-BINDING-01
    remains OPEN
```

because the full normative relationship among correction, disagreement and source-observed
state remains incomplete even though FR-07 clarifies the current disagreement encoding.

---

# 2. DEC-11 / FR-08 — Supervision target from clinically corrected P-scale priority

New referents:

```text
BAREF-DERMA-116 ClinicallyCorrectedPScalePriority
    WORKING_ACCEPTED

BAREF-DERMA-117 ClassifierSupervisionTarget
    WORKING_ACCEPTED

BAREF-DERMA-118 SupervisionTarget
    WORKING_ACCEPTED
    semantic kind
```

Accepted:

```text
BAPROP-DERMA-FR08-001
classify(
  classifiedReferent=ClassifierSupervisionTarget,
  semanticKind=SupervisionTarget
)

BAPROP-DERMA-FR08-002
produce(
  actor=DermaTriage,
  input=ClinicallyCorrectedPScalePriority,
  result=ClassifierSupervisionTarget
)
```

FR-08 provides four clean conditional result mappings:

```text
BAPROP-DERMA-FR08-003
IF priorityCode == P1
THEN ClassifierSupervisionTarget = HIGH

BAPROP-DERMA-FR08-004
IF priorityCode == P2
THEN ClassifierSupervisionTarget = HIGH

BAPROP-DERMA-FR08-005
IF priorityCode == P3
THEN ClassifierSupervisionTarget = MEDIUM

BAPROP-DERMA-FR08-006
IF priorityCode == P4
THEN ClassifierSupervisionTarget = LOW
```

Each is a `decisionRule` with:

```text
actor:
    DermaTriage

input:
    ClinicallyCorrectedPScalePriority

result:
    ClassifierSupervisionTarget

comparison:
    property = priorityCode
    comparisonKey = equals

ELSE:
    omitted
```

This is a strong positive validation of the existing BA2 `comparison equals` lower bound and
of the rule:

```text
omitted ELSE
    -> no inferred fallback
```

Source-governed documentation gap:

```text
GAP-DERMA-SUPERVISION-INPUT-01
```

remains open for missing, invalid, out-of-domain or conflicting corrected priority.

No new methodology pressure is created by FR-08.

---

# 3. DEC-17 / FR-26 — PromptManager, prompt versioning and persistence

New referents:

```text
BAREF-DERMA-119 PromptManager
    WORKING_ACCEPTED

BAREF-DERMA-120 Component
    WORKING_ACCEPTED
    semantic kind

BAREF-DERMA-121 PromptVersion
    WORKING_ACCEPTED

BAREF-DERMA-122 PromptPersistenceArtifact
    WORKING_ACCEPTED
    source binding = db/prompts.json

BAREF-DERMA-123 PromptVersionManagementResponsibility
    WORKING_ACCEPTED

BAREF-DERMA-124 PromptUpdateOperation
    WORKING_ACCEPTED

BAREF-DERMA-125 PromptResetOperation
    WORKING_ACCEPTED

BAREF-DERMA-126 PromptHistoryOperation
    WORKING_ACCEPTED

BAREF-DERMA-127 PromptVersionSelectionOperation
    WORKING_ACCEPTED
```

Accepted:

```text
BAPROP-DERMA-DEC17-001
classify(PromptManager, Component)

BAPROP-DERMA-DEC17-002
dependOn(
  dependent=PromptEvolutionPath,
  prerequisite=PromptManager
)

BAPROP-DERMA-FR26-001
classify(PromptPersistenceArtifact, Artifact)

BAPROP-DERMA-FR26-002
classify(PromptUpdateOperation, Behavior)

BAPROP-DERMA-FR26-003
classify(PromptResetOperation, Behavior)

BAPROP-DERMA-FR26-004
classify(PromptHistoryOperation, Behavior)

BAPROP-DERMA-DEC17-003
classify(PromptVersionSelectionOperation, Behavior)

BAPROP-DERMA-FR26-005
assignResponsibility(
  responsibleParty=PromptManager,
  responsibilityScope=PromptVersion,
  responsibilityKind=PromptVersionManagementResponsibility
)

BAPROP-DERMA-FR26-006
assignResponsibility(
  responsibleParty=PromptManager,
  responsibilityScope=PromptUpdateOperation,
  responsibilityKind=PromptVersionManagementResponsibility
)

BAPROP-DERMA-FR26-007
assignResponsibility(
  responsibleParty=PromptManager,
  responsibilityScope=PromptResetOperation,
  responsibilityKind=PromptVersionManagementResponsibility
)

BAPROP-DERMA-FR26-008
assignResponsibility(
  responsibleParty=PromptManager,
  responsibilityScope=PromptHistoryOperation,
  responsibilityKind=PromptVersionManagementResponsibility
)

BAPROP-DERMA-DEC17-004
assignResponsibility(
  responsibleParty=PromptManager,
  responsibilityScope=PromptVersionSelectionOperation,
  responsibilityKind=PromptVersionManagementResponsibility
)
```

Governed but partially representable:

```text
PromptManager
    persists prompt state to
db/prompts.json

PromptVersion
    is used by
Qwen2-VL / BioMistral
```

Persistence strengthens:

```text
P-08 DATA ARTIFACT / STORE / PERSISTENCE ASSOCIATION
```

The model-applicability/use binding is preserved as:

```text
CONFIGURATION_APPLICABILITY_BINDING_EVIDENCE
    SINGLE_HOLDOUT_EVIDENCE
    NOT YET A SEPARATE NUMBERED OR UNNUMBERED PRESSURE
```

It must be reviewed post-holdout against existing relation pressure before creating any new
operator topic.

`transition` is not admitted merely because prompt versions may be updated/reset.

---

# 4. DEC-18 / FR-27 — Incremental EfficientNet-B4 retraining

New referents:

```text
BAREF-DERMA-128 EfficientNetB4Retraining
    WORKING_ACCEPTED

BAREF-DERMA-129 EfficientNetB4RetrainingResponsibility
    WORKING_ACCEPTED

BAREF-DERMA-130 CNNTrainingInput
    WORKING_ACCEPTED

BAREF-DERMA-131 B4CaseImages
    WORKING_ACCEPTED

BAREF-DERMA-132 LastTwoFeatureBlocks
    WORKING_ACCEPTED

BAREF-DERMA-133 ClassifierHead
    WORKING_ACCEPTED

BAREF-DERMA-134 EarlierFeatureLayers
    WORKING_ACCEPTED

BAREF-DERMA-135 BackboneLearningRate
    WORKING_ACCEPTED

BAREF-DERMA-136 ClassifierLearningRate
    WORKING_ACCEPTED

BAREF-DERMA-137 RetrainingEpochCount
    WORKING_ACCEPTED

BAREF-DERMA-138 RetrainingClassWeights
    WORKING_ACCEPTED

BAREF-DERMA-139 ApplicableJpegPngInclusionConstraint
    WORKING_ACCEPTED

BAREF-DERMA-140 PdfExclusionConstraint
    WORKING_ACCEPTED

BAREF-DERMA-141 QualifiedClinicalCorrections
    PROVISIONAL_RECONCILIATION
```

Accepted:

```text
BAPROP-DERMA-FR27-001
classify(EfficientNetB4Retraining, Behavior)

BAPROP-DERMA-FR27-002
assignResponsibility(
  responsibleParty=DermaTriage,
  responsibilityScope=EfficientNetB4Retraining,
  responsibilityKind=EfficientNetB4RetrainingResponsibility
)

BAPROP-DERMA-FR27-003
dependOn(
  dependent=EfficientNetB4Retraining,
  prerequisite=[
    QualifiedClinicalCorrections,
    CNNTrainingInput,
    ClassifierSupervisionTarget
  ]
)

BAPROP-DERMA-FR27-004
dependOn(
  dependent=CNNTrainingInput,
  prerequisite=B4CaseImages
)

BAPROP-DERMA-FR27-005
constrain(BackboneLearningRate, 5e-6)

BAPROP-DERMA-FR27-006
constrain(ClassifierLearningRate, 3e-5)

BAPROP-DERMA-FR27-007
constrain(RetrainingEpochCount, 10)

BAPROP-DERMA-FR27-008
constrain(RetrainingClassWeights, [3.0, 2.0, 1.0])

BAPROP-DERMA-FR27-009
dependOn(
  dependent=EfficientNetB4Retraining,
  prerequisite=[
    BackboneLearningRate,
    ClassifierLearningRate,
    RetrainingEpochCount,
    RetrainingClassWeights
  ]
)
```

Structured property-vocabulary constraints:

```text
BAPROP-DERMA-FR27-010
constrain(
  constraintTarget=EfficientNetB4Retraining,
  constraintValue={
    property: trainableScope,
    vocabulary: [LastTwoFeatureBlocks, ClassifierHead]
  }
)

BAPROP-DERMA-FR27-011
constrain(
  constraintTarget=EfficientNetB4Retraining,
  constraintValue={
    property: frozenScope,
    vocabulary: [EarlierFeatureLayers]
  }
)
```

Input-policy constraints:

```text
BAPROP-DERMA-FR27-012
constrain(
  constraintTarget=CNNTrainingInput,
  constraintValue=ApplicableJpegPngInclusionConstraint
)

BAPROP-DERMA-FR27-013
constrain(
  constraintTarget=CNNTrainingInput,
  constraintValue=PdfExclusionConstraint
)
```

The source also states that retraining acquires qualified corrections and applicable documents
from B4 cases.

Therefore:

```text
ACQUISITION_REFRESH_ACTION_SEMANTICS
    FURTHER_STRENGTHENED

DATA_EVIDENCE_CONSUMPTION_SEMANTICS
    FURTHER_STRENGTHENED
```

`BAREF-DERMA-141 QualifiedClinicalCorrections` is not merged automatically with
`BAREF-DERMA-078 QualifiedClassifierDisagreementEvidence`.

New reconciliation:

```text
R-16 TRAINING QUALIFIED-CORRECTION EVIDENCE IDENTITY
    OPEN
```

No `create` is inferred: the source governs fine-tuning/update behavior but does not explicitly
establish a newly created project-semantic model artifact.

No `transition` is inferred: updating model parameters is not a governed lifecycle state
transition.

---

# 5. Final branch closure

```text
DEC-10 -> FR-07:
    FIRST-PASS COMPLETE

DEC-11 -> FR-08:
    FIRST-PASS COMPLETE

DEC-17 -> FR-26:
    FIRST-PASS COMPLETE

DEC-18 -> FR-27:
    FIRST-PASS COMPLETE

MR-04:
    FIRST-PASS COMPLETE
```

DermaTriage first-pass bounded source evidence collection is complete.
