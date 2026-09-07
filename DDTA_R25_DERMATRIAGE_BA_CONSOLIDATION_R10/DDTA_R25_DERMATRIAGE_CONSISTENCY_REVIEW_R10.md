# DermaTriage Pre-Consolidation Consistency Review — R10

## Scope

Working analyses reviewed before checkpointing:

```text
DEC-07
DEC-08
FR-10
DEC-09
FR-06
```

Methodology authority remains frozen BA0–BA6.

## Accepted correction — DEC-07 relation to concrete acceptance criteria

Working analysis had proposed:

```text
realize(
  abstract=ClassifierAcceptanceCriteria,
  realization=[
    SensitivityNonDegradationCriterion,
    FalseLowPerformanceNonDegradationCriterion,
    OverallAccuracyDegradationToleranceCriterion
  ]
)
```

Disposition:

```text
REJECTED_BEFORE_CONSOLIDATION
```

Reason:

`realize` asserts that a more concrete project meaning realizes/materializes an abstract
project meaning. Each individual metric-specific criterion does not independently realize
the whole `ClassifierAcceptanceCriteria` meaning.

R10 uses:

```text
classify(each concrete criterion, AcceptanceCriterion)

dependOn(
  dependent=ClassifierAdaptationQualificationCondition,
  prerequisite=[
    SensitivityNonDegradationCriterion,
    FalseLowPerformanceNonDegradationCriterion,
    OverallAccuracyDegradationToleranceCriterion
  ]
)
```

This preserves the source meaning that all applicable governed comparative criteria are
required for qualification without inventing collection-membership or realization semantics.

`BAREF-DERMA-088 ClassifierAcceptanceCriteria` and the R9 proposition that the qualification
condition depends on it remain carried. R10 adds the concrete currently governed prerequisites.

## Other working conclusions retained

```text
DEC-07:
    three metric-specific acceptance criteria accepted
    AcceptanceCriterion semantic kind accepted
    5% tolerance literal represented without inventing its arithmetic interpretation
    P-05 / P-06 strengthened
    GAP-DERMA-ACCEPT-BINDING-01 strengthened
    GAP-DERMA-EVAL-CONSISTENCY-01 strengthened

DEC-08:
    adopted adaptation, post-adoption threshold, post-adoption reference,
    rollback target and revocation condition accepted/provisionally reconciled
    Threshold semantic kind accepted
    R-15 opened
    transition not yet positive

FR-10:
    revocation/restoration behaviors accepted
    support responsibility accepted
    Store / Artifact classifications accepted
    persistence relationships remain partially representable -> P-08
    transition still not positive

DEC-09 / FR-06:
    evidence window/set and recent pertinent corrections accepted
    EvidenceWindow / EvidenceSet semantic kinds accepted
    production of PromptEvolutionEvidenceSet accepted at FR-06
    bounded top-N recency selection not fully representable
    -> BOUNDED_RECENCY_SELECTION_SEMANTICS
    GAP-DERMA-PROMPT-WINDOW-01 remains open
```

No other correction is required for R10.
