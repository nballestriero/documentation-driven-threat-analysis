# DermaTriage Base Analysis — Working Snapshot R1

**Checkpoint status:** `ACCEPTED_FOR_CONTINUATION`  
**Formal BA3 review state:** `PENDING_REVIEW`  
**Freshness:** `CURRENT`  
**Governed authority:** `DERMATRIAGE-GOV-R1`  
**Pinned repository baseline:** `163ee6ed5b56e10002474eeac35ea4e159fb5a9e`  
**Source:** `governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`

---

## 1. Scope of this snapshot

This snapshot records the Base Analysis meaning discussed through:

1. `MR-01`
2. `DEC-12`
3. `DEC-13`
4. `DEC-14`

It is intentionally incomplete.

Names marked **PROVISIONAL / RECONCILIATION OPEN** are retained so later source
elements can confirm, merge, distinguish or replace their working identity without
silently rewriting this checkpoint.

---

## 2. Working BAReferents

| ID | Working canonical name | Status | First evidence | Notes |
|---|---|---|---|---|
| BAREF-DERMA-001 | `DermaTriage` | WORKING_ACCEPTED | MR-01 | Central participant/capability. |
| BAREF-DERMA-002 | `DermatologicalCase` | WORKING_ACCEPTED | MR-01 | Case identity and later correlation context. |
| BAREF-DERMA-003 | `AvailableDermatologicalCaseInformation` | WORKING_ACCEPTED | MR-01 | Available information used for triage. |
| BAREF-DERMA-004 | `TriageUrgencyAssessment` | WORKING_ACCEPTED | MR-01 | Macro-level triage urgency result. |
| BAREF-DERMA-005 | `OperationalPriority` | WORKING_ACCEPTED | MR-01 | Distinct from analytical urgency/synthesis; P1-P4 are currently values. |
| BAREF-DERMA-006 | `DefinitiveClinicalDiagnosis` | WORKING_ACCEPTED | MR-01 | Scope over which DermaTriage lacks definitive diagnostic authority. |
| BAREF-DERMA-007 | `CompleteSpecialistRoutingProcess` | PROVISIONAL_RECONCILIATION | MR-01 | Reconcile with MR-02. |
| BAREF-DERMA-008 | `SkinLesionImage` | WORKING_ACCEPTED | DEC-12 | Image input for image-based path. |
| BAREF-DERMA-009 | `EfficientNet-B4` | WORKING_ACCEPTED | DEC-12 | Concrete governed classifier technology. |
| BAREF-DERMA-010 | `ImageUrgencyClassification` | WORKING_ACCEPTED | DEC-12 | Stage-1 analytical output. |
| BAREF-DERMA-011 | `Qwen2-VL-7B-Instruct` | WORKING_ACCEPTED | DEC-12 | Concrete governed model. |
| BAREF-DERMA-012 | `ClinicalDescription` | WORKING_ACCEPTED | DEC-12 | Stage-2 output. |
| BAREF-DERMA-013 | `ChromaDB` | WORKING_ACCEPTED | DEC-12 | Concrete governed retrieval technology. |
| BAREF-DERMA-014 | `sentence-transformers/all-MiniLM-L6-v2` | WORKING_ACCEPTED | DEC-12 | Concrete governed embedding model; BA detail necessity remains under observation. |
| BAREF-DERMA-015 | `HistoricalCaseContext` | WORKING_ACCEPTED | DEC-12 | Retrieved historical context consumed by synthesis. |
| BAREF-DERMA-016 | `BioMistral-7B` | WORKING_ACCEPTED | DEC-12 | Concrete governed synthesis model. |
| BAREF-DERMA-017 | `AvailableSymptomInformation` | WORKING_ACCEPTED | DEC-12 | Symptom information available to synthesis. |
| BAREF-DERMA-018 | `AITriageSynthesis` | WORKING_ACCEPTED | DEC-12 | Final analytical synthesis of the image-based pipeline. |
| BAREF-DERMA-019 | `ImageBasedTriagePipeline` | PROVISIONAL_PRESSURE_TARGET | DEC-12 | Pipeline identity appears useful; composition/order representation is open. |
| BAREF-DERMA-020 | `BaselineTrainingProcess` | PROVISIONAL_PRESSURE_TARGET | DEC-13 | Independently meaningful process; exposes function/behavior-binding pressure. |
| BAREF-DERMA-021 | `EfficientNetBaseline` | WORKING_ACCEPTED | DEC-13 | Trained/selected baseline required before operational use. |
| BAREF-DERMA-022 | `TrainingDataset` | WORKING_ACCEPTED | DEC-13 | Training input; detailed parameters remain in documentation unless later justified. |
| BAREF-DERMA-023 | `ImageBasedUrgencyClassificationCapability` | PROVISIONAL_RECONCILIATION | DEC-13 | Used to represent the capability that depends on the trained baseline; reconcile with later FR semantics. |
| BAREF-DERMA-024 | `B4` | WORKING_ACCEPTED | DEC-14 | External system participating in data exchange; not triage owner. |
| BAREF-DERMA-025 | `B4Consultation` | WORKING_ACCEPTED | DEC-14 | B4-originating consultation information. |
| BAREF-DERMA-026 | `B4Documents` | PROVISIONAL_RECONCILIATION | DEC-14 | Content class transferred from B4. |
| BAREF-DERMA-027 | `B4Images` | PROVISIONAL_RECONCILIATION | DEC-14 | Content class transferred from B4; reconcile with `SkinLesionImage` where source permits. |
| BAREF-DERMA-028 | `TriageOutcome` | PROVISIONAL_RECONCILIATION | DEC-14 | Reconcile with `TriageUrgencyAssessment`, `AITriageSynthesis`, `OperationalPriority`; do not merge by name similarity. |
| BAREF-DERMA-029 | `DirectTriagePath` | PROVISIONAL_PRESSURE_TARGET | DEC-14 | Distinct direct interaction path. |
| BAREF-DERMA-030 | `B4IntegratedTriagePath` | PROVISIONAL_PRESSURE_TARGET | DEC-14 | Distinct B4-integrated interaction path. |
| BAREF-DERMA-031 | `POST /analyze` | PROVISIONAL_RECONCILIATION | DEC-14 | Concrete direct endpoint/interface identity candidate. |
| BAREF-DERMA-032 | `POST /diagnose` | PROVISIONAL_RECONCILIATION | DEC-14 | Concrete B4-integrated endpoint/interface identity candidate. |
| BAREF-DERMA-033 | `B4DermaTriageBoundary` | PROVISIONAL_PRESSURE_TARGET | DEC-14 | Explicit project boundary; relation to interaction/interface remains open. |

### Intentionally not promoted to referent yet

- `P1`, `P2`, `P3`, `P4`: controlled local values of `OperationalPriority`.
- individual stakeholders listed by MR-01: not promoted merely because they are stakeholders.
- a universal symptom vocabulary: explicitly not reified.
- optimizer/scheduler/training hyperparameters: retained in governed documentation unless later BA use justifies promotion.
- `cosine similarity` and `top-5`: governed technical details, not automatically BA identities.

---

## 3. Working BAPropositions

All propositions below are:

- `discussionDisposition: ACCEPTED_FOR_CONTINUATION`
- `reviewState: PENDING_REVIEW`
- `freshness: CURRENT`
- `originState: GROUNDED`

unless explicitly noted.

### MR-01

#### BAPROP-DERMA-MR01-001 — Triage production

```text
operator: produce
polarity: POSITIVE

actor  -> DermaTriage
input  -> DermatologicalCase
input  -> AvailableDermatologicalCaseInformation
result -> TriageUrgencyAssessment
result -> OperationalPriority
```

Purpose: preserve the macro-level production meaning without inventing the
conditional mapping to P1-P4.

#### BAPROP-DERMA-MR01-002 — Operational-priority vocabulary

```text
operator: constrain
polarity: POSITIVE

constraintTarget -> OperationalPriority
constraintValue:
  property   -> operationalPriorityLevel   [BA5 candidate key]
  vocabulary -> P1 | P2 | P3 | P4
```

The property key remains a BA5 canonicalization candidate.

#### BAPROP-DERMA-MR01-003 — Triage responsibility

```text
operator: assignResponsibility
polarity: POSITIVE

responsibleParty    -> DermaTriage
responsibilityScope -> TriageUrgencyAssessment
responsibilityKind  -> triageResponsibility   [BA5 candidate]
```

`DEC-14` adds reinforcing source evidence that B4 does not acquire this responsibility.

#### BAPROP-DERMA-MR01-004 — No definitive diagnostic authority

```text
operator: assignResponsibility
polarity: NEGATIVE

responsibleParty    -> DermaTriage
responsibilityScope -> DefinitiveClinicalDiagnosis
responsibilityKind  -> diagnosticAuthority   [BA5 candidate]
```

#### BAPROP-DERMA-MR01-005 — No end-to-end specialist-routing ownership

```text
operator: assignResponsibility
polarity: NEGATIVE

responsibleParty    -> DermaTriage
responsibilityScope -> CompleteSpecialistRoutingProcess
responsibilityKind  -> ownership   [BA5 candidate]
```

This does not deny participation in specialist routing.

### DEC-12

#### BAPROP-DERMA-DEC12-001 — Image urgency classification

```text
operator: produce
polarity: POSITIVE

actor  -> EfficientNet-B4
input  -> SkinLesionImage
result -> ImageUrgencyClassification

scopedModifier.condition:
  image-based path applicable / SkinLesionImage available
```

#### BAPROP-DERMA-DEC12-002 — Clinical description

```text
operator: produce
polarity: POSITIVE

actor  -> Qwen2-VL-7B-Instruct
input  -> SkinLesionImage
result -> ClinicalDescription

scopedModifier.condition:
  image-based path applicable / SkinLesionImage available
```

#### BAPROP-DERMA-DEC12-003 — Historical-case retrieval

```text
operator: observe
polarity: POSITIVE

actor    -> ChromaDB
observed -> historical case information
result   -> HistoricalCaseContext
```

Status note: the operator is a good current fit for querying existing historical
information without implying creation/change, but the identity of the retrieval
function itself exposes an open BA2 pressure.

#### BAPROP-DERMA-DEC12-004 — AI triage synthesis

```text
operator: produce
polarity: POSITIVE

actor  -> BioMistral-7B
input  -> ImageUrgencyClassification
input  -> ClinicalDescription
input  -> HistoricalCaseContext
input  -> AvailableSymptomInformation
result -> AITriageSynthesis
```

#### BAPROP-DERMA-DEC12-005 — Same-case correlation

```text
operator: correlate
polarity: POSITIVE

correlatedItem     -> ImageUrgencyClassification
correlatedItem     -> ClinicalDescription
correlatedItem     -> HistoricalCaseContext
correlatedItem     -> AITriageSynthesis
correlationContext -> DermatologicalCase
```

`AITriageSynthesis` and `OperationalPriority` remain distinct referents; no artificial
`distinctFrom` proposition is introduced.

### DEC-13

#### BAPROP-DERMA-DEC13-001 — Operational capability prerequisite

```text
operator: dependOn
polarity: POSITIVE

dependent    -> ImageBasedUrgencyClassificationCapability
prerequisite -> EfficientNetBaseline
```

This is a direct test of `dependOn` as prerequisite semantics.

#### BAPROP-DERMA-DEC13-002 — Baseline training output

```text
operator: produce
polarity: POSITIVE

actor  -> BaselineTrainingProcess
input  -> TrainingDataset
input  -> EfficientNet-B4
result -> EfficientNetBaseline
```

The `actor -> BaselineTrainingProcess` shape is intentionally retained as a pressure
observation rather than silently repaired.

`create` is not used: the current analytical need is production of a baseline result,
not explicit establishment semantics.

### DEC-14

#### BAPROP-DERMA-DEC14-001 — B4 to DermaTriage transfer

```text
operator: transfer
polarity: POSITIVE

source      -> B4
destination -> DermaTriage
content     -> B4Consultation
content     -> B4Documents
content     -> B4Images
```

#### BAPROP-DERMA-DEC14-002 — DermaTriage to B4 outcome transfer

```text
operator: transfer
polarity: POSITIVE

source      -> DermaTriage
destination -> B4
content     -> TriageOutcome
```

#### BAPROP-DERMA-DEC14-003 — Integrated-path triage production

```text
operator: produce
polarity: POSITIVE

actor  -> DermaTriage
input  -> B4Consultation
input  -> B4Documents
input  -> B4Images
result -> TriageOutcome

scopedModifier.condition:
  B4IntegratedTriagePath applicable
```

#### BAPROP-DERMA-DEC14-004 — B4 does not own triage responsibility

```text
operator: assignResponsibility
polarity: NEGATIVE

responsibleParty    -> B4
responsibilityScope -> TriageUrgencyAssessment
responsibilityKind  -> triageResponsibility   [BA5 candidate]
```

The positive DermaTriage triage-responsibility proposition remains
`BAPROP-DERMA-MR01-003`; DEC-14 is additional governed support, not a reason to mint a
semantically duplicate proposition.

---

## 4. Deliberate non-representations

The checkpoint intentionally does **not** assert:

- a negative `dependOn` from triage to image;
- that MR-01 has no dependencies merely because no macro canonical dependency is listed;
- complete SLA semantics;
- a universal closed symptom vocabulary;
- that `B4` is consumed as a service merely because information from B4 is “consumed”;
- that sequential pipeline order is equivalent to `dependOn`;
- that every technical configuration value needs a BA referent/proposition;
- a decision rule for P1-P4 before the source element governing the mapping is analyzed;
- a decision rule for checkpoint selection before the relevant FR is analyzed;
- equivalence among `TriageUrgencyAssessment`, `ImageUrgencyClassification`,
  `AITriageSynthesis`, `TriageOutcome` and `OperationalPriority`.

---

## 5. BA3 provenance posture

The material above is source-grounded to the governed documentation elements listed
for each entry.

At this checkpoint:

```text
originState: GROUNDED
reviewState: PENDING_REVIEW
freshness: CURRENT
discussionDisposition: ACCEPTED_FOR_CONTINUATION
```

No `DERIVED` element is accepted by this checkpoint and no derivation rule is introduced.

---

## 6. Checkpoint conclusion

The current BA is sufficient to continue the holdout, but it is not declared complete.

Open representation pressure is recorded separately and must **not** be repaired by
changing BA0–BA6 before the remainder of the governed DermaTriage corpus has been
analyzed.
