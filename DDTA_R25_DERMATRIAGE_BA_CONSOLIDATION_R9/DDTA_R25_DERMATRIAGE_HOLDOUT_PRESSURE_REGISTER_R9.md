# DermaTriage Holdout Pressure Register — R9

**Method changes:** `NONE`  
**New numbered pressure IDs:** `NONE`

## Numbered pressures

```text
P-01 FUNCTION / PROCESS / BEHAVIOR IDENTITY BINDING
    CARRIED

P-02 PIPELINE COMPOSITION / ORDER
    CARRIED

P-03 INTERFACE / PATH / INVOCATION ASSOCIATION
    STRONG / CARRIED

P-04 BOUNDARY / INTERACTION ASSOCIATION
    STRONG / CARRIED

P-05 ORDERED COMPARISON VOCABULARY
    STRONG REPEATED / CARRIED
    no additional FR-09 comparator is inferred before DEC-07

P-06 SCALAR / PROPERTY-ADDRESSING COMPARISON
    STRONG / CARRIED

P-07 STRUCTURED DATA / INFORMATION CONTRACT
    STRONG / CARRIED

P-08 DATA ARTIFACT / STORE / PERSISTENCE ASSOCIATION
    STRONG / CARRIED
```

## Unnumbered carried — acquisition / refresh action semantics

Carried from R7.

## Unnumbered carried — conditional action / trigger semantics

Carried from FR-04 / FR-05.

FR-09 is deliberately distinguished:

```text
FR-04 / FR-05:
    WHEN condition
    THEN actor MUST perform action
    -> conditional-action pressure

FR-09:
    IF governed qualification condition satisfied
    THEN governed result = QUALIFIED_FOR_ADOPTION
    -> clean decisionRule use
```

## Unnumbered carried — data / evidence consumption semantics

Carried from FR-05.

## Unnumbered strong repeated — negative implication / non-sufficiency semantics

FR-13:

```text
ActivationConditionOfPathA
    MUST NOT imply
ActivationConditionOfPathB
```

FR-14:

```text
EvidenceQualifiedForPathA
    MUST NOT imply
EvidenceQualifiedForPathB
```

FR-15:

```text
LifecycleResultOfPathA
    MUST NOT imply
EquivalentLifecycleResultOfPathB
```

Status:

```text
STRONG_REPEATED_UNNUMBERED_HOLDOUT_PRESSURE_EVIDENCE
```

Current operators cannot directly preserve the general meaning:

```text
fact scoped to A
    does not by itself establish
corresponding fact scoped to B
```

without changing the meaning into negative dependency, mutual exclusion or negative
outcome.

No numbered pressure is introduced during the frozen holdout.

## FR-09 disposition

FR-09 does not create a new pressure.

It provides a positive counterpoint:

```text
decisionRule:
    actor + input + result
    IF candidate satisfies governed qualification condition
    THEN result = QUALIFIED_FOR_ADOPTION
    ELSE omitted
```

This supports the current BA2 boundary between conditional result selection and conditional
mandatory action.
