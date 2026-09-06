# DermaTriage Holdout Pressure Register — R6

**Method changes authorized:** `NONE`

R6 preserves P-01..P-08. No new pressure ID is introduced during the frozen holdout.

# P-01 — FUNCTION / PROCESS / BEHAVIOR IDENTITY BINDING

**Status:** `OPEN — REPEATED PROCESS SUBCASE`

Carried from R5.

# P-02 — PIPELINE COMPOSITION AND ORDER

**Status:** `OPEN — PARTIALLY NARROWED`

Carried unchanged.

# P-03 — INTERFACE / PATH / INVOCATION ASSOCIATION

**Status:** `STRONG_REPEATED_HOLDOUT_PRESSURE — FURTHER STRENGTHENED`

Existing endpoint->process evidence remains. DEC-15 adds:

```text
DiagnosticOutputWriteBack
MedicalValidationWriteBack
ValidatedOutcomeRetrieval
    -> use B4 APIs
```

Current BA2 represents behavior/source/destination/content but cannot cleanly bind an
independently identified interaction behavior to its interface/logical path.

Rejected generic shortcuts: `reference`, `dependOn`, `realize`.

Analytical subdimensions, not new pressure IDs:

```text
P-03a endpoint -> invoked behavior
P-03b interaction behavior -> interface/logical path
P-03c interaction behavior -> service/channel/connection where governed
```

# P-04 — BOUNDARY / INTERACTION ASSOCIATION

**Status:** `STRONG_REPEATED_HOLDOUT_PRESSURE — FURTHER STRENGTHENED`

`B4DermaTriageBoundary` coexists with multiple bidirectional transfers, but BA2 still cannot
cleanly state that a specific transfer behavior crosses that boundary.

# P-05 — ORDERED COMPARISON VOCABULARY

Carried unchanged. `greaterThan` remains required by FR-02.

# P-06 — DIRECT SCALAR / PROPERTY-ADDRESSING COMPARISON

Carried unchanged.

# P-07 — STRUCTURED DATA / INFORMATION CONTRACT

**Status:** `OPEN — STRONGLY REINFORCED`

FR-12:

```text
ClinicalReviewResult.reviewDisposition
allowed vocabulary = CONFIRMATION | CORRECTION
required for every recorded review result
```

`constrain` represents the vocabulary but not cleanly mandatory presence / exactly-one
cardinality.

Analytical subdimensions:

```text
P-07a vocabulary/domain restriction -> largely representable
P-07b required property/component presence -> open
P-07c structural cardinality/nesting -> open
```

# P-08 — DATA ARTIFACT / STORE / PERSISTENCE ASSOCIATION

**Status:** `OPEN — STRONGLY REINFORCED`

FR-18 established artifact/store association pressure. FR-03 adds:

```text
DermaTriage records/persists ClinicalReviewResult
```

Rejected as persistence substitutes:

```text
create
produce
observe
transition
transfer
reference
correlate
```

Analytical subdimensions:

```text
P-08a artifact -> storage/location association
P-08b actor -> record/write/persist -> artifact
```

# Interaction-level evidence discipline

Consider when material:

```text
WHAT
WHO
FROM
TO
OPERATION
INTERFACE / LOGICAL PATH
SERVICE / CAPABILITY
CONNECTION / CHANNEL
TRANSPORT / PROTOCOL
MEDIUM
BOUNDARY / BOUNDARIES CROSSED
SECURITY / TRUST QUALIFICATION
```

Missing dimensions are not automatically gaps. Assess materiality and documentation intent.

# R6 pressure lesson

```text
1. source governs meaning + BA represents it -> accepted BA
2. source governs meaning + BA cannot preserve it -> methodology pressure
3. required meaning is not sufficiently governed -> documentation gap
4. level intentionally omitted after conscious assessment -> intentional documentation boundary
```
