# DermaTriage Effective Working Base Analysis — R8

```text
R1 + R2 + R3 + R4 + R5 + R6 + R7 + R8
```

Coverage:

```text
MR-01 complete
MR-02 complete / STOP AT MR
MR-03 branch complete
MR-04 IN PROGRESS
  DEC-04 branch complete
    FR-04 analyzed
    FR-05 analyzed
next: DEC-05
```

R8 referents: BAREF-DERMA-066..078.

R8 accepted propositions:

```text
MR04-001 dependOn ControlledDermaTriageAdaptation -> ClinicalReviewDerivedEvidence
MR04-002 realize ControlledDermaTriageAdaptation -> PromptEvolutionPath + EfficientNetB4AdaptationPath
DEC04-001 dependOn PromptEvolutionPath -> PromptEvolutionEvidenceAccumulationCondition
DEC04-002 dependOn EfficientNetB4AdaptationPath -> ClassifierAdaptationEvidenceAccumulationCondition
FR04-001 constrain PromptEvolutionThreshold -> 10
FR04-002 dependOn PromptEvolutionCycle -> PromptEvolutionEvidenceAccumulationCondition
FR04-003 assignResponsibility DermaTriage -> PromptEvolutionCycle / activation
FR05-001 constrain ClassifierAdaptationThreshold -> 50
FR05-002 dependOn ClassifierAdaptationCycle -> ClassifierAdaptationEvidenceAccumulationCondition
FR05-003 assignResponsibility DermaTriage -> ClassifierAdaptationCycle / activation
FR05-004 dependOn ClassifierAdaptationEvidenceAccumulationCondition -> QualifiedClassifierDisagreementEvidence
```

Pressure delta:

```text
P-05 FURTHER_STRENGTHENED
P-01,P-02,P-03,P-04,P-06,P-07,P-08 CARRIED

unnumbered carried:
  ACQUISITION_REFRESH_ACTION_SEMANTICS

unnumbered new:
  CONDITIONAL_ACTION_TRIGGER_SEMANTICS
  DATA_EVIDENCE_CONSUMPTION_SEMANTICS
```

Constructs:

```text
dependOn TESTED_POSITIVE_STRONG
realize TESTED_POSITIVE_STRONG
constrain TESTED_POSITIVE_STRONG
assignResponsibility TESTED_POSITIVE_STRONG
create NOT_TESTED_POSITIVE
transition NOT_TESTED_POSITIVE
classify NOT_TESTED_POSITIVE
decisionRule not generalized to conditional mandatory action
```
