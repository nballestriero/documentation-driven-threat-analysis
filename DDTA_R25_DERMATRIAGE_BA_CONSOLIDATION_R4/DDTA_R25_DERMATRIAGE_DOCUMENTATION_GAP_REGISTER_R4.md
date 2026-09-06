# DermaTriage Documentation Gap Register — R4 additions

## D-07 — HISTORICAL CASE CONTEXT CONTRACT COMPLETENESS

FR-18 tells us that five similar historical cases are retrieved, but not exactly
which fields/components are returned, whether full cases or selected attributes are
returned, or the complete historical/index schema.

Classification: `DOCUMENTATION GAP`.

## D-08 — AI TRIAGE SYNTHESIS CONTRACT / FIELD LINEAGE

Known minimum:

```text
urgency
confidence
reasoning
recommendedAction
```

Also produced:

```text
predicted_pathology
```

Unknown:

- full schema / nullability / domains;
- whether urgency/confidence are copied, newly computed or derived;
- lineage of reasoning/recommendedAction;
- exact contract status of predicted_pathology.

Classification: `DOCUMENTATION GAP`.

## D-09 — TRAINING DATA CONTRACT / PROVENANCE

FR-20 governs counts/configuration but not:

- row/feature schema;
- label field/domain;
- original data provenance;
- relationship original -> SMOTE-balanced training data;
- storage/loading location;
- train/validation/test schema relationship;
- unambiguous allocation semantics for the documented 345 rows.

Classification: `DOCUMENTATION GAP`.

## D-10 — BASELINE CHECKPOINT PERSISTENCE / LINEAGE

Known:

```text
BestBaselineCheckpoint selected by validation Macro F1
```

Unknown:

- persistence destination;
- version/identifier;
- overwrite/retention;
- metadata linking checkpoint to training run/data/config;
- exact tie/selection semantics where deterministic reproduction requires them.

Classification: `DOCUMENTATION GAP`.

## D-11 — DIRECT ANALYZE INTERFACE / DATA CONTRACT COMPLETENESS

Known:

```text
DirectClient invokes POST /analyze
a DermatologicalCase is submitted directly
POST /analyze invokes DermaTriageTriageProcess
FastAPI exposes the service
```

Not governed in FR-21:

- complete request schema;
- required/optional fields;
- serialization/content type;
- exact response schema/result;
- error contract;
- authentication/authorization;
- secure transport semantics;
- physical/network medium beyond endpoint/interface evidence.

Do not infer HTTPS/TLS/trust boundary/auth policy from `POST /analyze`.

Classification: `DOCUMENTATION GAP`.
