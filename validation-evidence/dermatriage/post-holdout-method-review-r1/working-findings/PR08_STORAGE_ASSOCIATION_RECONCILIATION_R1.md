# PR-08 Storage Association Reconciliation R1

## Status

`SOURCE-COMPLETE CONCEPTUAL REVIEW / NON-NORMATIVE`

## Scope

The complete governed DermaTriage baseline was reviewed for storage, persistence,
versioning, history, tracking, write/write-back, indexing/query, retrieval, restore,
retention and accumulated-evidence semantics.

## Main result

The original broad pressure:

```text
artifact/store/persistence
```

is refined to:

```text
PR-08 AT_REST_STORAGE_ASSOCIATION
```

The generic `persist` hypothesis is not retained.

A narrower candidate survives:

```text
CC-03 storedIn
```

## H1 — transfer + constrain

Result:

```text
PARTIAL
NOT UNIVERSALLY SUFFICIENT
```

Why:
- `transfer` requires conveyance semantics that FR-10 storage statements do not
  necessarily govern;
- `constrain` requires restriction semantics and cannot safely replace every factual
  storage association.

## H2 — storedIn + composition

Result:

```text
SURVIVES EXHAUSTION
```

Working meaning:

```text
stored item -> at-rest storage association -> store/location
```

Complementary constructs remain distinct:

```text
write/conveyance                -> transfer
storage residence               -> storedIn ?
retention/config restriction    -> constrain
read/query/retrieval            -> observe
version/result production       -> produce/create when source supports identity
restore/rollback                -> separate lifecycle/selection review
```

## H3 — generic persist

Result:

```text
NOT JUSTIFIED
```

It risks conflating:
- write;
- storage residence;
- durability;
- retention;
- history;
- versioning;
- recoverability.

## Positive controls

### FR-26
PromptManager maintains prompt versions, persists their state in `db/prompts.json`,
and supports update/reset/history.

### FR-10
Recoverable model versions are maintained in `models/versions/`; model-version tracking
is in `db/model_versions.json`; the active model is in `models/efficientnet_b4.pth`.

## Negative/boundary controls

### FR-03 / MR-03
Clinical review is recorded, but complete overwrite/history/retention/finality semantics
are explicitly not governed.

### FR-23
Write-back/retrieval with B4 governs exchange/correlation, not B4 internal persistence.

### FR-18
ChromaDB indexing/querying is governed; exact persisted-representation identity is not
sufficiently established merely from that fact.

### FR-20
Best checkpoint selection does not by itself govern persistence.

### FR-04 / FR-05
Evidence is accumulated, but count reset/reuse/persistence/concurrency semantics are
explicitly under-governed.

## Candidate allocation

```text
CC-03 storedIn
owner: PR-08
status: CANDIDATE_TESTED_POSITIVE
admission: NOT_ADMITTED
gate: G1-G8_PENDING
```

No top-level operator is added by this finding.
