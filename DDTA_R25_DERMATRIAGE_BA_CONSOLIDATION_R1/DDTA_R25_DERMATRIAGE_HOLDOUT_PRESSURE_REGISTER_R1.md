# DermaTriage Holdout Pressure Register — R1

**Purpose:** accumulate empirical evidence without changing the frozen methodology.  
**Default disposition:** `OPEN_FOR_EVIDENCE_COLLECTION`

A pressure entry is not proof that the methodology is wrong. It is a bounded record
of a place where current BA representation is awkward, incomplete, potentially
redundant, or awaiting reconciliation.

---

## P-01 — FUNCTION / PROCESS / BEHAVIOR IDENTITY BINDING

**Classification:** `OPEN_HOLDOUT_PRESSURE`  
**Evidence:** `DEC-12`, `DEC-13`, `DEC-14`  
**Disposition:** `OPEN_FOR_EVIDENCE_COLLECTION`

### Governed evidence

DermaTriage repeatedly exposes independently meaningful functions/processes/paths:

- image-based pipeline stages;
- historical-case retrieval;
- baseline training;
- direct and B4-integrated paths.

### Current BA capability

BA1 can represent a behavior, process or capability as a `BAReferent`.

BA2 can represent activity semantics with operators such as `produce` and `observe`.

### Pressure

Except for `transfer.behavior`, current BA2 does not provide a general operator role
that explicitly binds a reusable function/process/behavior identity to the proposition
that describes what that function does.

This produces awkward shapes such as:

```text
produce
  actor -> BaselineTrainingProcess
```

when the analytical intent may instead be:

```text
identified process/function
  has inputs
  has outputs
  is realized/performed by something
```

### Rejected shortcut

Do not invent a new BA1 family such as `FunctionalBlock`.
BA1 already permits such meanings to be BAReferents.

### What would confirm the pressure

Further governed examples where the same function/process must be:

- independently referenced;
- constrained;
- realized by a technology;
- placed in a pipeline/workflow;
- compared or changed across baselines.

### Method change now

`NONE`.

---

## P-02 — PIPELINE COMPOSITION AND ORDER

**Classification:** `OPEN_HOLDOUT_PRESSURE`  
**Evidence:** `DEC-12`  
**Disposition:** `OPEN_FOR_EVIDENCE_COLLECTION`  
**Importance:** HIGH

### Governed evidence

DEC-12 adopts a **sequential four-stage pipeline**.

### Required analytical distinctions

The BA may need to preserve:

- identity of the pipeline;
- membership of stages in that pipeline;
- stage composition;
- governed sequence/order.

### Current difficulty

No current BA2 operator cleanly means:

- `contains stage`;
- `precedes/follows`;
- `is next stage in`.

### Rejected shortcut

Do not encode sequencing as `dependOn` unless the source actually governs prerequisite
semantics.

```text
precedes != dependOn
```

### Why this matters

Pipelines and workflows are common system structures. If the holdout confirms that
their composition/order is material shared project meaning, this may be a genuine BA2
coverage gap.

### Method change now

`NONE`.

---

## P-03 — INTERFACE / PATH ASSOCIATION

**Classification:** `OPEN_HOLDOUT_PRESSURE`  
**Evidence:** `DEC-14`  
**Disposition:** `OPEN_FOR_EVIDENCE_COLLECTION`

### Governed evidence

DEC-14 distinguishes:

- direct path -> `POST /analyze`;
- B4-integrated path -> `POST /diagnose`.

### Pressure

BA1 can give identity to paths and endpoints, but current BA2 does not obviously
provide a precise method-neutral relation meaning:

```text
endpoint/interface exposes or belongs to this interaction path
```

`reference` may be too weak; `realize`, `dependOn`, `transfer`, and `classify` mean
different things.

### Method change now

`NONE`.

---

## P-04 — BOUNDARY / INTERACTION ASSOCIATION

**Classification:** `OPEN_HOLDOUT_PRESSURE`  
**Evidence:** `DEC-14`  
**Disposition:** `OPEN_FOR_EVIDENCE_COLLECTION`

### Governed evidence

The B4/DermaTriage boundary is explicitly required to remain distinguishable.

### Current BA capability

BA1 permits a boundary to have `BAReferent` identity.

### Pressure

It is not yet clear how to state, with current BA2 semantics, which interaction,
transfer, interface or path crosses/uses a particular boundary without inventing
meaning.

### Method change now

`NONE`.

---

# Reconciliation items — not methodology defects yet

## R-01 — RESPONSIBILITY KIND AND PROPERTY CANONICALIZATION

**Classification:** `RECONCILIATION`

Working keys currently include:

- `triageResponsibility`
- `diagnosticAuthority`
- `ownership`
- `operationalPriorityLevel`

These require BA5 canonical review. Their existence does not yet imply a methodology
problem.

---

## R-02 — SPECIALIST ROUTING IDENTITY

**Classification:** `RECONCILIATION`

`CompleteSpecialistRoutingProcess` must be reconciled against `MR-02`.

Do not assume that related wording means identical BAReferent identity.

---

## R-03 — IMAGE OPTIONALITY SEMANTICS

**Classification:** `RECONCILIATION`

MR-01 says image is not a universal triage precondition.

The preferred validation is to see whether:

- DEC-12 / image path; and
- DEC-01 / no-image fallback

jointly preserve this meaning without inventing a negative `dependOn`.

---

## R-04 — TRIAGE RESULT IDENTITY FAMILY

**Classification:** `RECONCILIATION`

Keep distinct until governed evidence proves equivalence or containment:

- `TriageUrgencyAssessment`
- `ImageUrgencyClassification`
- `AITriageSynthesis`
- `TriageOutcome`
- `OperationalPriority`

Similarity of names or downstream use is not enough to merge them.

---

# Observations — empirical lessons, not defects

## O-01 — DOCUMENTATION DETAIL PROMOTION BOUNDARY

Governed technical detail is not automatically BA material.

Examples encountered:

- `all-MiniLM-L6-v2`
- cosine similarity;
- top-5 retrieval;
- Adam;
- warmup;
- CosineAnnealing;
- hyperparameters;
- FastAPI/Uvicorn;
- Python/PyTorch/CUDA runtime details.

Such detail remains authoritative in documentation and should enter BA only when its
identity, reuse, constraint, comparison, projection, or change impact makes the shared
analysis materially depend on it.

---

## O-02 — SOURCE VERB IS NOT AN OPERATOR

DEC-14 says that the integrated path “consumes” consultation/documents/images from B4.

This does **not** automatically justify:

```text
consumeService
  consumer -> DermaTriage
  service  -> B4
```

because BA2 `consumeService` concerns actual service/capability use, not arbitrary
consumption of data.

This observation reinforces operator selection by semantic definition rather than
lexical matching.

---

# Global rule for the remaining holdout

No entry in this register authorizes a methodology change.

After all governed DermaTriage documents have been analyzed, perform a cross-corpus
pressure review and classify each entry as one of:

- application error;
- documentation gap;
- BA canonicalization/reconciliation issue;
- guide/example weakness;
- tested redundancy;
- confirmed methodology pressure;
- confirmed missing construct;
- resolved/no change.
