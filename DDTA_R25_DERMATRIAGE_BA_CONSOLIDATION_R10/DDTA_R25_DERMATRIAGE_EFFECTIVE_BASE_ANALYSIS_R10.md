# DermaTriage Effective Working Base Analysis — R10

Effective state:

```text
R1 + R2 + R3 + R4 + R5 + R6 + R7 + R8 + R9 + R10
```

## Coverage

```text
MR-01:
    FIRST-PASS COMPLETE

MR-02:
    FIRST-PASS COMPLETE
    STOP AT MR

MR-03:
    FIRST-PASS BRANCH COMPLETE

MR-04:
    FIRST-PASS IN PROGRESS

    DEC-04:
        branch complete
        FR-04 analyzed
        FR-05 analyzed

    DEC-05:
        branch complete
        FR-13 analyzed
        FR-14 analyzed
        FR-15 analyzed

    DEC-06:
        branch complete
        FR-09 analyzed

    DEC-07:
        branch complete
        no active concrete SpecializedRequirement

    DEC-08:
        branch complete
        FR-10 analyzed

    DEC-09:
        branch complete
        FR-06 analyzed

next:
    DEC-10
```

Remaining active bounded source elements after R10:

```text
DEC-10
FR-07

DEC-11
FR-08

DEC-17
FR-26

DEC-18
FR-27

TOTAL = 8
```

## R10 referent delta

```text
089 SensitivityNonDegradationCriterion
090 FalseLowPerformanceNonDegradationCriterion
091 OverallAccuracyDegradationToleranceCriterion
092 AcceptanceCriterion
093 AdoptedClassifierAdaptation
094 PostAdoptionAccuracyDegradationThreshold
095 Threshold
096 ApplicablePostAdoptionReference
097 PreviousAcceptableVersionOrState
098 ClassifierAdaptationRevocationCondition
099 ClassifierAdaptationRevocation
100 ClassifierAdaptationRestoration
101 Behavior
102 ClassifierAdaptationRevocationSupportResponsibility
103 ModelVersionsStore
104 ModelVersionTrackingArtifact
105 ActiveClassifierModelArtifact
106 Store
107 Artifact
108 PromptEvolutionEvidenceWindow
109 PromptEvolutionEvidenceSet
110 EvidenceWindow
111 EvidenceSet
112 PromptEvolutionEvidenceWindowSize
113 RecentPertinentClinicalCorrections
```

## R10 proposition highlights

```text
DEC-07:
    classify three concrete criteria -> AcceptanceCriterion
    qualification condition depends on the three concrete criteria
    constrain accuracy tolerance criterion -> 5%

DEC-08:
    classify post-adoption degradation threshold -> Threshold
    constrain post-adoption threshold -> 5%
    revocation condition depends on adopted adaptation + threshold + post-adoption reference

FR-10:
    classify revocation/restoration -> Behavior
    restoration realizes revocation
    assign DermaTriage revocation-support responsibility
    restoration depends on previous acceptable version/state
    classify rollback storage -> Store
    classify tracking + active-model paths -> Artifact

DEC-09:
    classify prompt evidence window -> EvidenceWindow
    classify prompt evidence set -> EvidenceSet
    constrain window-size parameter -> 20
    evidence set depends on window

FR-06:
    DermaTriage produces PromptEvolutionEvidenceSet
    from RecentPertinentClinicalCorrections
```

## Construct status

```text
BAReferent:
    TESTED_POSITIVE_STRONG

BAProposition:
    TESTED_POSITIVE_STRONG

classify:
    TESTED_POSITIVE_IN_DERMATRIAGE
    repeated forward applications
    classification coverage audit still deferred

decisionRule:
    TESTED_POSITIVE_IN_DERMATRIAGE
    carried from FR-09

transition:
    NOT_TESTED_POSITIVE
    DEC-08 / FR-10 considered but do not govern canonical fromState/toState

dependOn:
    TESTED_POSITIVE_STRONG

realize:
    TESTED_POSITIVE_STRONG
    FR-10 restoration realizes revocation

assignResponsibility:
    TESTED_POSITIVE_STRONG
    support responsibility does not imply authorization authority

constrain:
    TESTED_POSITIVE_STRONG
    threshold/bound literals preserved without inventing complete formulas

produce:
    TESTED_POSITIVE_STRONG
    FR-06 current-cycle evidence set

create:
    NOT_TESTED_POSITIVE

reference:
    NOT_TESTED_POSITIVE

P-08 persistence association:
    STRONG_REPEATED_PRESSURE
```

## Application-completeness evidence

```text
CLASSIFICATION_COVERAGE_REVIEW_EVIDENCE

status:
    OPEN / CARRY_FORWARD

new forward evidence:
    AcceptanceCriterion
    Threshold
    Behavior
    Store
    Artifact
    EvidenceWindow
    EvidenceSet

disposition:
    NOT_A_METHOD_PRESSURE

review:
    after current DermaTriage evidence cycle
    after post-holdout methodology review
    before integrated DermaTriage BA6
```

## Pressure state

```text
P-01 carried
P-02 carried
P-03 strong / carried
P-04 strong / carried
P-05 strong repeated / further strengthened
P-06 strong repeated / further strengthened
P-07 strong / carried
P-08 strong repeated / further strengthened

UNNUMBERED:
  ACQUISITION_REFRESH_ACTION_SEMANTICS
      carried

  CONDITIONAL_ACTION_TRIGGER_SEMANTICS
      repeated / carried

  DATA_EVIDENCE_CONSUMPTION_SEMANTICS
      carried

  NEGATIVE_IMPLICATION_NON_SUFFICIENCY_SEMANTICS
      strong repeated / carried

  BOUNDED_RECENCY_SELECTION_SEMANTICS
      NEW IN R10
```

DermaTriage BA6 remains not executed.
