# DermaTriage Holdout Pressure Register — R5

**Method changes authorized:** `NONE`

---

# P-01 — FUNCTION / PROCESS / BEHAVIOR IDENTITY BINDING

**R5 status:** `OPEN — REPEATED PROCESS SUBCASE`

Capability subcase remains largely representable.

Repeated process/behavior evidence now includes:

```text
BaselineTrainingProcess
DermaTriageTriageProcess
```

FR-21 and FR-22 both require a concrete endpoint to invoke the same independently
meaningful triage process.

No generalized role/operator is added during holdout.

---

# P-02 — PIPELINE COMPOSITION AND ORDER

**R5 status:** `OPEN — PARTIALLY NARROWED`

Carried from R4.

Producer/input chains recover important logical ordering, but not every explicit
pipeline membership/order fact.

---

# P-03 — INTERFACE / PATH / INVOCATION ASSOCIATION

**R5 status:** `STRONG_REPEATED_HOLDOUT_PRESSURE`

Existing BA2 successfully represents:

```text
DirectTriagePath
    realize
POST /analyze

B4IntegratedTriagePath
    realize
POST /diagnose
```

But repeated governed meaning remains blocked:

```text
POST /analyze
    invokes
DermaTriageTriageProcess

POST /diagnose
    invokes
DermaTriageTriageProcess
```

Rejected shortcuts:

```text
reference
dependOn
consumeService
realize(endpoint, process)
```

The path->endpoint subcase is largely narrowed. The endpoint->invoked-behavior
subcase is now strongly evidenced.

---

# P-04 — BOUNDARY / INTERACTION ASSOCIATION

**R5 status:** `STRONG_REPEATED_HOLDOUT_PRESSURE`

Known:

```text
B4DermaTriageBoundary

transfer
    B4 -> DermaTriage
    ConsultationData
    CaseDocuments
```

Current BA2 cannot explicitly bind:

```text
transfer
    crosses
B4DermaTriageBoundary
```

This distinction is material for:

- data-flow projections;
- privacy analysis;
- trust-boundary-aware threat analysis;
- interface review.

No new operator/role is authorized yet.

---

# P-05 — ORDERED COMPARISON VOCABULARY

Carried unchanged.

`greaterThan` remains empirically required by FR-02.

---

# P-06 — DIRECT SCALAR / PROPERTY-ADDRESSING COMPARISON

Carried unchanged.

R-05 confidence binding remains open.

---

# P-07 — STRUCTURED DATA / INFORMATION CONTRACT

**R5 status:** `OPEN — IMPORTANT, NO NEW METHOD COUNTEREXAMPLE FROM FR-22`

FR-22 makes complete interface/data contracts highly useful, but the detailed contract
is not governed in the source.

Therefore:

```text
missing request/data schema
    -> D-12 documentation gap

not automatically
    -> BA2 defect
```

Existing P-07 evidence remains FR-16, FR-17, FR-19.

---

# P-08 — DATA ARTIFACT / STORE ASSOCIATION

Carried unchanged.

FR-22 does not govern a B4 or DermaTriage store, so no storage relation is invented.

---

# R5 pressure lesson

The holdout now distinguishes three failure modes:

```text
1. source has meaning and BA can represent it
       -> accepted proposition

2. source has meaning but BA cannot represent it cleanly
       -> methodology pressure

3. source does not govern enough meaning
       -> documentation gap
```

FR-22 exercises all three categories and confirms the value of keeping them separate.
