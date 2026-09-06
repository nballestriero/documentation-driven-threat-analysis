# DermaTriage Holdout Pressure Register — R2

**Default:** `OPEN_FOR_EVIDENCE_COLLECTION`  
**Method changes authorized:** `NONE`

## P-01 — FUNCTION / PROCESS / BEHAVIOR IDENTITY BINDING

**Evidence:** DEC-12, DEC-13, DEC-14, DEC-01, FR-01  
**Strength:** REPEATED

R2 adds `SymptomOnlyTriageProcess`. The clean proposition remains:

```text
produce
  actor  -> DermaTriage
  input  -> AvailableSymptomInformation
  result -> SymptomBasedUrgency
```

Current BA2 still has no general role binding reusable process/function identity to
this proposition. Do not force `actor -> SymptomOnlyTriageProcess`.

## P-02 — PIPELINE COMPOSITION AND ORDER

Carried from R1. Still open.

DEC-01 introduces an alternative path, but current applicability conditions are
sufficient so far; no new branching operator is currently required.

## P-03 — INTERFACE / PATH ASSOCIATION

Carried from R1. No R2 change.

## P-04 — BOUNDARY / INTERACTION ASSOCIATION

Carried from R1. No R2 change.

## P-05 — ORDERED COMPARISON VOCABULARY

**Classification:** STRONG_HOLDOUT_METHODOLOGY_PRESSURE  
**Evidence:** DEC-02, FR-02

Concrete governed requirement:

```text
confidence > 0.85
```

Current BA2 R3 admits:

```text
equals
notEquals
```

Boolean composition is already available:

```text
allOf  = AND
anyOf  = OR
not    = NOT
notEquals = !=
```

Empirically confirmed missing comparison:

```text
greaterThan = >
```

Review candidates only, not yet empirically required:

```text
lessThan = <
greaterThanOrEqual = >=
lessThanOrEqual = <=
```

No methodology change now.

## P-06 — DIRECT SCALAR / PROPERTY-ADDRESSING COMPARISON

**Classification:** STRONG_HOLDOUT_METHODOLOGY_PRESSURE  
**Evidence:** FR-02

Governed meaning:

```text
confidence > 0.85
```

Current BA2 requires each comparison to contain:

```text
referent
property
comparisonKey
value
```

If `Confidence` is the compared semantic value, inventing:

```text
Confidence.value
Confidence.score
```

would add unsupported project meaning.

Alternative to test at FR-16:

- perhaps `confidence` is governed as a property of another existing referent;
- if that becomes explicit, P-06 may narrow or resolve.

Do not invent a `HighConfidenceCondition` solely to hide the threshold via `satisfies`.

# Reconciliation / resolution

## R-01 — RESPONSIBILITY / PROPERTY CANONICALIZATION

OPEN.

## R-02 — SPECIALIST ROUTING IDENTITY

OPEN. Reconcile at MR-02.

## R-03 — IMAGE OPTIONALITY

`RESOLVED_FOR_CURRENT_EVIDENCE`.

Positive conditional paths preserve the meaning; no negative dependency or new
optional-dependency operator is required.

## R-04 — TRIAGE RESULT IDENTITY FAMILY

OPEN. Keep distinct:

```text
TriageUrgencyAssessment
ImageUrgencyClassification
AITriageSynthesis
TriageOutcome
SymptomBasedUrgency
OperationalPriority
```

# Documentation gaps, not methodology defects

- D-01 / GAP-DERMA-NOIMAGE-INPUT-01
- D-02 / GAP-DERMA-PMAP-INPUT-01
- D-03 / GAP-DERMA-NOIMAGE-PMAP-BINDING-01
- D-04 / GAP-DERMA-SLA-01

# Guide-level candidate

Make the existing condition vocabulary explicit in examples:

```text
allOf      -> AND
anyOf      -> OR
not        -> NOT
notEquals  -> !=
```

This is currently a guide/readability candidate, not a metamodel extension.
