# DermaTriage Holdout Pressure Register — R10

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
    STRONG_REPEATED
    FURTHER_STRENGTHENED_BY_DEC07_DEC08_FR10

    R10 counterexamples include:
      sensitivity NOT_WORSE_THAN applicable-reference sensitivity
      false-low performance NOT_WORSE_THAN applicable reference
      overall-accuracy degradation AT_MOST pre-adoption tolerance
      post-adoption accuracy degradation GREATER_THAN rollback threshold

P-06 SCALAR / PROPERTY-ADDRESSING COMPARISON
    STRONG_REPEATED
    FURTHER_STRENGTHENED_BY_DEC07_DEC08_FR10

    Required meaning compares properties/derived scalars of candidate/adopted adaptations
    against properties/derived scalars of applicable reference versions.

P-07 STRUCTURED DATA / INFORMATION CONTRACT
    STRONG / CARRIED

P-08 DATA ARTIFACT / STORE / PERSISTENCE ASSOCIATION
    STRONG_REPEATED
    FURTHER_STRENGTHENED_BY_FR10

    Governed persistence meanings include:
      restorable versions maintained in models/versions/
      model-version tracking in db/model_versions.json
      active classifier model in models/efficientnet_b4.pth

    Current BA2 cannot preserve these as explicit store/persistence bindings without
    changing them into dependency, generic reference or prose constraint semantics.
```

## Unnumbered carried — acquisition / refresh action semantics

Carried.

## Unnumbered carried — conditional action / trigger semantics

Carried from FR-04 / FR-05.

## Unnumbered carried — data / evidence consumption semantics

Carried from FR-05.

## Unnumbered strong repeated — negative implication / non-sufficiency semantics

Carried from FR-13 / FR-14 / FR-15.

## New unnumbered — bounded recency selection semantics

Source counterexample from DEC-09 / FR-06:

```text
for each prompt-evolution cycle

select/use
    the 20 most recent
    pertinent clinical corrections

to construct
    PromptEvolutionEvidenceSet
```

Current BA can represent:

```text
actor
input
result
window identity
set identity
numeric bound
```

but not structurally:

```text
eligibility filter
+
recency ranking
+
bounded top-N membership selection
```

Status:

```text
BOUNDED_RECENCY_SELECTION_SEMANTICS
    UNNUMBERED_HOLDOUT_PRESSURE_EVIDENCE
```

Relationship to P-05:

```text
P-05 ordered comparison
    may help express recency ordering

but

ordered comparison alone
    !=
top-N collection membership selection
```

No numbered pressure is introduced during the frozen holdout.
