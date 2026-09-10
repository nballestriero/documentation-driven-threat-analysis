# DDTA R25 — CC-03 `storedIn` consolidation R34

This checkpoint consolidates the source-complete PR-08 persistence/storage review at exact baseline:

```text
d5b39ee072e9cd489937bb171919de549e15a489
```

No BA0–BA5 method contract changes. The top-level BA2 basis remains 14 operators.

## Consolidated candidate

```text
CC-03 storedIn

working meaning:
    a governed information/artifact referent is maintained or resides
    as stored content in a governed store/location

working signature:
    storedItem -> BAReferent
    store      -> BAReferent

status:
    CANDIDATE_TESTED_POSITIVE
    NOT_ADMITTED
    G1-G8_PENDING
```

`storedIn` does **not** automatically assert:

```text
who wrote the item
when it was written
retention duration
immutability
versioning
recoverability
backup
survival of every failure
```

## Why `persist` is not retained as the candidate

The full DermaTriage corpus separates write, at-rest residence, retention/history,
versioning, recoverability, retrieval and rollback. A generic `persist` operator would
bundle meanings that are independently governed or intentionally unspecified.

## Existing-construct exhaustion

```text
transfer
    preserves conveyance/write-to-destination when source governs that event
    but cannot represent at-rest residence without inventing a transfer

constrain
    preserves governed storage/retention restrictions
    but cannot safely convert every storage fact into a restriction

reference
    too weak for storage residence

observe
    reads/queries stored content; it is not storage residence
```

## Source controls

Positive:
- FR-26 prompt version/state persisted in `db/prompts.json`;
- FR-10 recoverable model versions maintained in `models/versions/`,
  tracking in `db/model_versions.json`, active model in `models/efficientnet_b4.pth`.

Negative/boundary:
- FR-03 `record` does not establish complete history/retention/finality;
- FR-23 write-back does not establish persistence inside B4;
- FR-18 ChromaDB indexing/querying does not fully govern exact persisted representation;
- FR-20 checkpoint selection does not by itself establish persistence;
- accumulated evidence in FR-04/FR-05 does not establish persistence.

## Next review

Proceed to PR-03 `invoke / expose`.
