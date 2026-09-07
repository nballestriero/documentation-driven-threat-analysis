# DermaTriage Holdout Pressure Register — R8

Method changes: `NONE`. New numbered pressure IDs: `NONE`.

```text
P-01 carried
P-02 carried
P-03 strong / carried
P-04 strong / carried
P-05 STRONG_REPEATED_HOLDOUT_PRESSURE / FURTHER_STRENGTHENED
P-06 carried
P-07 strong / carried
P-08 strong / carried
```

## P-05

Evidence:

```text
FR-02 confidence > 0.85
FR-04 accumulated prompt evidence reaches threshold 10
FR-05 accumulated classifier evidence reaches threshold 50
```

Current `equals|notEquals` vocabulary does not preserve all ordered/threshold meanings.

Do not infer:

```text
reaches 10 == >= 10
reaches 50 == >= 50
```

## Unnumbered carried — TOKEN ACQUISITION / REFRESH

`ACQUISITION_REFRESH_ACTION_SEMANTICS` carried from R7.

## Unnumbered new — CONDITIONAL ACTION / TRIGGER SEMANTICS

Repeated:

```text
WHEN prompt condition THEN DermaTriage MUST activate PromptEvolutionCycle
WHEN classifier condition THEN DermaTriage MUST activate ClassifierAdaptationCycle
```

Current BA represents threshold, prerequisite and responsibility separately, but not a direct `WHEN condition THEN mandatory action` structure without inventing a decision result.

## Unnumbered new — DATA / EVIDENCE CONSUMPTION SEMANTICS

FR-05 consumes disagreement evidence qualified by FR-07.

Representable as prerequisite/dependency, but explicit non-service evidence consumption is not directly represented.

Rejected shortcuts:

```text
consumeService -> evidence is not service
transfer -> no governed source/destination
observe -> consumption != read/query
```
