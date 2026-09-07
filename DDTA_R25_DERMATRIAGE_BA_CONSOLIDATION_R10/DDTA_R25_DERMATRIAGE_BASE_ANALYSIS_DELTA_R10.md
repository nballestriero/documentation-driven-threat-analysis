# DermaTriage Base Analysis — Delta R10

**Disposition:** `ACCEPTED_FOR_CONTINUATION`
**Methodology:** `BA0–BA6 FROZEN`
**New numbered pressure:** `NONE`

R10 is additive after R9 and consolidates:

```text
DEC-07
DEC-08
FR-10
DEC-09
FR-06
```

---

# 1. DEC-07 — Asymmetric prioritization of quality metrics

New referents:

```text
BAREF-DERMA-089 SensitivityNonDegradationCriterion
    WORKING_ACCEPTED

BAREF-DERMA-090 FalseLowPerformanceNonDegradationCriterion
    WORKING_ACCEPTED

BAREF-DERMA-091 OverallAccuracyDegradationToleranceCriterion
    WORKING_ACCEPTED

BAREF-DERMA-092 AcceptanceCriterion
    WORKING_ACCEPTED
    semantic kind
```

Accepted:

```text
BAPROP-DERMA-DEC07-001
classify(
  classifiedReferent=SensitivityNonDegradationCriterion,
  semanticKind=AcceptanceCriterion
)

BAPROP-DERMA-DEC07-002
classify(
  classifiedReferent=FalseLowPerformanceNonDegradationCriterion,
  semanticKind=AcceptanceCriterion
)

BAPROP-DERMA-DEC07-003
classify(
  classifiedReferent=OverallAccuracyDegradationToleranceCriterion,
  semanticKind=AcceptanceCriterion
)

BAPROP-DERMA-DEC07-004
dependOn(
  dependent=ClassifierAdaptationQualificationCondition,
  prerequisite=[
    SensitivityNonDegradationCriterion,
    FalseLowPerformanceNonDegradationCriterion,
    OverallAccuracyDegradationToleranceCriterion
  ]
)

BAPROP-DERMA-DEC07-005
constrain(
  constraintTarget=OverallAccuracyDegradationToleranceCriterion,
  constraintValue=5%
)
```

The provisional working `realize(ClassifierAcceptanceCriteria, concrete criteria)` is rejected
before consolidation. See `DDTA_R25_DERMATRIAGE_CONSISTENCY_REVIEW_R10.md`.

Governed but partially representable:

```text
BAREQ-DERMA-DEC07-SENSITIVITY-001
    candidate sensitivity must not worsen relative to applicable reference sensitivity
    pressureRefs = [P-05, P-06]

BAREQ-DERMA-DEC07-FALSELOW-001
    candidate false-low performance must not worsen relative to applicable reference
    pressureRefs = [P-05, P-06]

BAREQ-DERMA-DEC07-ACCURACY-001
    candidate overall-accuracy degradation must remain within documented 5% tolerance
    pressureRefs = [P-05, P-06]
    gapRef = GAP-DERMA-ACCEPT-BINDING-01
```

Negative control:

```text
NON-DEGRADATION != EQUALITY
```

The governed 5% literal is not normalized to relative percentage, percentage points or another
arithmetic formula because the source does not fully bind that interpretation.

---

# 2. DEC-08 — Reversibility after post-adoption degradation

New referents:

```text
BAREF-DERMA-093 AdoptedClassifierAdaptation
    WORKING_ACCEPTED

BAREF-DERMA-094 PostAdoptionAccuracyDegradationThreshold
    WORKING_ACCEPTED

BAREF-DERMA-095 Threshold
    WORKING_ACCEPTED
    semantic kind

BAREF-DERMA-096 ApplicablePostAdoptionReference
    PROVISIONAL_RECONCILIATION
    R-15

BAREF-DERMA-097 PreviousAcceptableVersionOrState
    PROVISIONAL_RECONCILIATION
    recheck FR-10 / later lineage review

BAREF-DERMA-098 ClassifierAdaptationRevocationCondition
    WORKING_ACCEPTED
```

Accepted:

```text
BAPROP-DERMA-DEC08-001
classify(
  classifiedReferent=PostAdoptionAccuracyDegradationThreshold,
  semanticKind=Threshold
)

BAPROP-DERMA-DEC08-002
constrain(
  constraintTarget=PostAdoptionAccuracyDegradationThreshold,
  constraintValue=5%
)

BAPROP-DERMA-DEC08-003
dependOn(
  dependent=ClassifierAdaptationRevocationCondition,
  prerequisite=[
    AdoptedClassifierAdaptation,
    PostAdoptionAccuracyDegradationThreshold,
    ApplicablePostAdoptionReference
  ]
)
```

Governed but partially representable:

```text
BAREQ-DERMA-DEC08-DEGRADATION-001

post-adoption accuracy degradation
    > PostAdoptionAccuracyDegradationThreshold
relative to
    ApplicablePostAdoptionReference

pressureRefs:
    P-05
    P-06

gapRef:
    GAP-DERMA-ROLLBACK-BINDING-01
```

Identity control:

```text
pre-adoption tolerance T = 5%
post-adoption threshold R = 5%

same literal
    !=
same semantic identity
```

`transition` is considered but not accepted at DEC-08.

---

# 3. FR-10 — Revocation and restoration support

New referents:

```text
BAREF-DERMA-099 ClassifierAdaptationRevocation
    WORKING_ACCEPTED

BAREF-DERMA-100 ClassifierAdaptationRestoration
    WORKING_ACCEPTED

BAREF-DERMA-101 Behavior
    WORKING_ACCEPTED
    semantic kind

BAREF-DERMA-102 ClassifierAdaptationRevocationSupportResponsibility
    WORKING_ACCEPTED

BAREF-DERMA-103 ModelVersionsStore
    WORKING_ACCEPTED
    source binding = models/versions/

BAREF-DERMA-104 ModelVersionTrackingArtifact
    WORKING_ACCEPTED
    source binding = db/model_versions.json

BAREF-DERMA-105 ActiveClassifierModelArtifact
    PROVISIONAL_RECONCILIATION
    source binding = models/efficientnet_b4.pth

BAREF-DERMA-106 Store
    WORKING_ACCEPTED
    semantic kind

BAREF-DERMA-107 Artifact
    WORKING_ACCEPTED
    semantic kind
```

Accepted:

```text
BAPROP-DERMA-FR10-001
classify(ClassifierAdaptationRevocation, Behavior)

BAPROP-DERMA-FR10-002
classify(ClassifierAdaptationRestoration, Behavior)

BAPROP-DERMA-FR10-003
realize(
  abstract=ClassifierAdaptationRevocation,
  realization=ClassifierAdaptationRestoration
)

BAPROP-DERMA-FR10-004
assignResponsibility(
  responsibleParty=DermaTriage,
  responsibilityScope=ClassifierAdaptationRevocation,
  responsibilityKind=ClassifierAdaptationRevocationSupportResponsibility
)

BAPROP-DERMA-FR10-005
dependOn(
  dependent=ClassifierAdaptationRestoration,
  prerequisite=PreviousAcceptableVersionOrState
)

BAPROP-DERMA-FR10-006
classify(ModelVersionsStore, Store)

BAPROP-DERMA-FR10-007
classify(ModelVersionTrackingArtifact, Artifact)

BAPROP-DERMA-FR10-008
classify(ActiveClassifierModelArtifact, Artifact)
```

Governed persistence meaning:

```text
restorable model versions
    maintained in models/versions/

model-version tracking
    maintained in db/model_versions.json

active classifier model
    represented by models/efficientnet_b4.pth
```

Current status:

```text
BAREQ-DERMA-FR10-PERSISTENCE-001
    PARTIALLY_REPRESENTABLE
    pressureRef = P-08
```

Current BA2 has no specific persistence/store association sufficient to preserve these bindings
without changing them into dependency, generic reference or prose constraint semantics.

`transition` remains `NOT_TESTED_POSITIVE`: the source governs support for revocation through
restoration but does not establish canonical fromState/toState values or automatic execution.

---

# 4. DEC-09 — Recent bounded prompt evidence

New referents:

```text
BAREF-DERMA-108 PromptEvolutionEvidenceWindow
    WORKING_ACCEPTED

BAREF-DERMA-109 PromptEvolutionEvidenceSet
    WORKING_ACCEPTED

BAREF-DERMA-110 EvidenceWindow
    WORKING_ACCEPTED
    semantic kind

BAREF-DERMA-111 EvidenceSet
    WORKING_ACCEPTED
    semantic kind

BAREF-DERMA-112 PromptEvolutionEvidenceWindowSize
    WORKING_ACCEPTED
```

Accepted:

```text
BAPROP-DERMA-DEC09-001
classify(PromptEvolutionEvidenceWindow, EvidenceWindow)

BAPROP-DERMA-DEC09-002
classify(PromptEvolutionEvidenceSet, EvidenceSet)

BAPROP-DERMA-DEC09-003
constrain(
  constraintTarget=PromptEvolutionEvidenceWindowSize,
  constraintValue=20
)

BAPROP-DERMA-DEC09-004
dependOn(
  dependent=PromptEvolutionEvidenceWindow,
  prerequisite=PromptEvolutionEvidenceWindowSize
)

BAPROP-DERMA-DEC09-005
dependOn(
  dependent=PromptEvolutionEvidenceSet,
  prerequisite=PromptEvolutionEvidenceWindow
)
```

Working selection meaning is carried to FR-06.

---

# 5. FR-06 — Construction of the current-cycle prompt evidence set

New referent:

```text
BAREF-DERMA-113 RecentPertinentClinicalCorrections
    WORKING_ACCEPTED
```

Accepted:

```text
BAPROP-DERMA-FR06-001
produce(
  actor=DermaTriage,
  input=RecentPertinentClinicalCorrections,
  result=PromptEvolutionEvidenceSet
)
```

`BAPROP-DERMA-DEC09-005` is strongly reinforced.

The source explicitly governs:

```text
for each prompt-evolution cycle
select/use
the 20 most recent
pertinent clinical corrections
to construct
PromptEvolutionEvidenceSet
```

Current BA can preserve actor, input, result, set/window identity and numeric bound, but it
cannot structurally preserve bounded top-N recency selection.

Therefore:

```text
BAREQ-DERMA-DEC09-RECENCY-SELECTION-001

status:
    GOVERNED_BUT_NOT_FULLY_REPRESENTABLE

pressure:
    BOUNDED_RECENCY_SELECTION_SEMANTICS
```

This is distinct from P-05: ordered comparison alone does not encode ranking plus bounded
collection membership.

The source simultaneously leaves ordering edge cases, deduplication, underfill and cross-cycle
reuse/overlap insufficiently specified. That remains documentation gap
`GAP-DERMA-PROMPT-WINDOW-01`.

---

# 6. R10 observations

```text
O-20
NON-DEGRADATION != EQUALITY
    STRONGLY_SUPPORTED

O-21
SAME LITERAL != SAME SEMANTIC IDENTITY
    STRONGLY_REINFORCED

O-22
SUPPORT RESPONSIBILITY
    !=
DECISION / AUTHORIZATION RESPONSIBILITY
    CANDIDATE / STRONG EVIDENCE

O-23
SELECTION WINDOW != SELECTED EVIDENCE SET
    STRONGLY_REINFORCED

O-24
BOUND SIZE != MEMBERSHIP RULE
    CANDIDATE / STRONG EVIDENCE
```

No BA0–BA6 change is authorized.
