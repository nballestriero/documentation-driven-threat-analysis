# DermaTriage Base Analysis — Delta R8

## MR-04

New referents:

```text
BAREF-DERMA-066 ControlledDermaTriageAdaptation WORKING_ACCEPTED
BAREF-DERMA-067 ClinicalReviewDerivedEvidence PROVISIONAL_RECONCILIATION
BAREF-DERMA-068 PromptEvolutionPath WORKING_ACCEPTED
BAREF-DERMA-069 EfficientNetB4AdaptationPath WORKING_ACCEPTED
```

Accepted:

```text
BAPROP-DERMA-MR04-001
dependOn
dependent: ControlledDermaTriageAdaptation
prerequisite: ClinicalReviewDerivedEvidence

BAPROP-DERMA-MR04-002
realize
abstract: ControlledDermaTriageAdaptation
realization: PromptEvolutionPath, EfficientNetB4AdaptationPath
```

Negative controls: accumulated evidence != `create`; lifecycle wording != `transition` without governed states; out-of-scope authority != negative responsibility.

## DEC-04

```text
BAREF-DERMA-070 PromptEvolutionEvidenceAccumulationCondition WORKING_ACCEPTED
BAREF-DERMA-071 ClassifierAdaptationEvidenceAccumulationCondition WORKING_ACCEPTED
```

```text
BAPROP-DERMA-DEC04-001
dependOn PromptEvolutionPath
  -> PromptEvolutionEvidenceAccumulationCondition

BAPROP-DERMA-DEC04-002
dependOn EfficientNetB4AdaptationPath
  -> ClassifierAdaptationEvidenceAccumulationCondition
```

DEC-04 governs 10 relevant prompt corrections and 50 qualifying classifier corrections but delegates exact triggers to FR-04/FR-05.

## FR-04

```text
BAREF-DERMA-072 AccumulatedPromptCorrectionEvidence WORKING_ACCEPTED
BAREF-DERMA-073 PromptEvolutionThreshold WORKING_ACCEPTED
BAREF-DERMA-074 PromptEvolutionCycle WORKING_ACCEPTED
```

```text
BAPROP-DERMA-FR04-001
constrain PromptEvolutionThreshold -> 10
source meaning: accumulated prompt-correction evidence elements

BAPROP-DERMA-FR04-002
dependOn PromptEvolutionCycle
  -> PromptEvolutionEvidenceAccumulationCondition

BAPROP-DERMA-FR04-003
assignResponsibility
responsibleParty: DermaTriage
responsibilityScope: PromptEvolutionCycle
responsibilityKind: promptEvolutionCycleActivationResponsibility
condition: PromptEvolutionEvidenceAccumulationCondition
```

Blocked/partial:

```text
BAREQ-DERMA-FR04-THRESHOLD-001
AccumulatedPromptCorrectionEvidence reaches PromptEvolutionThreshold
status: PARTIALLY_REPRESENTABLE
pressure: P-05

BAREQ-DERMA-FR04-TRIGGER-001
WHEN condition satisfied THEN DermaTriage MUST activate PromptEvolutionCycle
status: PARTIALLY_REPRESENTABLE
unnumbered: CONDITIONAL_ACTION_TRIGGER_SEMANTICS
```

Do not infer `>= 10`, INACTIVE->ACTIVE, or cycle creation.

## FR-05

```text
BAREF-DERMA-075 AccumulatedClassifierEvidence WORKING_ACCEPTED
BAREF-DERMA-076 ClassifierAdaptationThreshold WORKING_ACCEPTED
BAREF-DERMA-077 ClassifierAdaptationCycle WORKING_ACCEPTED
BAREF-DERMA-078 QualifiedClassifierDisagreementEvidence PROVISIONAL_RECONCILIATION
recheck: FR-07
```

```text
BAPROP-DERMA-FR05-001
constrain ClassifierAdaptationThreshold -> 50
source meaning: qualifying corrections

BAPROP-DERMA-FR05-002
dependOn ClassifierAdaptationCycle
  -> ClassifierAdaptationEvidenceAccumulationCondition

BAPROP-DERMA-FR05-003
assignResponsibility
responsibleParty: DermaTriage
responsibilityScope: ClassifierAdaptationCycle
responsibilityKind: classifierAdaptationCycleActivationResponsibility
condition: ClassifierAdaptationEvidenceAccumulationCondition

BAPROP-DERMA-FR05-004
dependOn ClassifierAdaptationEvidenceAccumulationCondition
  -> QualifiedClassifierDisagreementEvidence
```

Blocked/partial:

```text
BAREQ-DERMA-FR05-THRESHOLD-001
AccumulatedClassifierEvidence reaches ClassifierAdaptationThreshold
status: PARTIALLY_REPRESENTABLE
pressure: P-05

BAREQ-DERMA-FR05-TRIGGER-001
WHEN condition satisfied THEN DermaTriage MUST activate ClassifierAdaptationCycle
status: PARTIALLY_REPRESENTABLE
repeated unnumbered: CONDITIONAL_ACTION_TRIGGER_SEMANTICS

BAREQ-DERMA-FR05-EVIDENCE-CONSUMPTION-001
classifier accumulation consumes FR-07-qualified disagreement evidence
status: PARTIALLY_REPRESENTABLE
unnumbered: DATA_EVIDENCE_CONSUMPTION_SEMANTICS
```

`consumeService` rejected: evidence is not a service. `transfer` rejected: no governed source/destination. `observe` rejected: consumption != read/query.

No BA0–BA6 change.
