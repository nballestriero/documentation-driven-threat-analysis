# CC-03 `storedIn` Question Pack R1

## Status

`CANDIDATE_TESTED_POSITIVE / NON-NORMATIVE / NOT_ADMITTED`

## Candidate identity

```text
candidateId: CC-03
candidateName: storedIn
owningPressure: PR-08
empiricalStatus: CANDIDATE_TESTED_POSITIVE
admissionStatus: NOT_ADMITTED
formalGate: G1-G8_PENDING
```

## A. Source meaning

Minimum candidate meaning:

```text
a governed stored item is maintained/resides as stored content
in a governed store/location
```

Source-positive controls:
- FR-26: prompt state persisted in `db/prompts.json`;
- FR-10: recoverable model versions maintained in `models/versions/`,
  model-version tracking in `db/model_versions.json`, active model in
  `models/efficientnet_b4.pth`.

Negative/boundary controls:
- FR-03 `record` with retention/history/finality explicitly under-governed;
- FR-23 write-back to B4 without governing B4 storage;
- FR-18 indexing/querying ChromaDB without complete persisted-representation identity;
- FR-20 best-checkpoint selection without persistence obligation;
- FR-04/FR-05 accumulated evidence with persistence/count lifecycle under-governed.

## B. Existing-construct exhaustion

`transfer` is sufficient only when a governed conveyance/write event exists.
Using it for FR-10 storage residence would invent a source/transfer event.

`constrain` can represent reusable storage/retention restrictions, but a fact that an
item resides in a location is not automatically a restriction.

`reference` preserves only reference identity and loses storage semantics.

`observe` represents read/query/inspection and loses at-rest residence.

Therefore the storage-association slot survives existing-construct exhaustion in the
current corpus.

## C. Independent semantic value

Delete test question:

```text
If storedIn is removed, can the BA still state where a recoverable version,
prompt state or active model is maintained without inventing transfer or
restriction semantics?
```

Current result:

```text
NO
```

Useful projections:
- data/artifact-at-rest view;
- store-content view;
- impact analysis by store;
- storage-without-retention-policy QA;
- change analysis for stored artifacts.

## D. Boundary rules

Do **not** infer `storedIn` from:
- `record`;
- `write-back`;
- `produce`;
- `select checkpoint`;
- `accumulate`;
- database/filename mention without governed residence;
- query/retrieval alone.

`storedIn` does **not** imply:
- retention duration;
- immutability;
- versioning;
- recoverability;
- backup;
- durability across all failures;
- who performed the write.

## E. Synthetic stress

```text
SYNTHETIC ONLY
NOT PROJECT TRUTH
NOT G1 SOURCE EVIDENCE

A message is sent to a transient socket and immediately consumed.
transfer exists; storedIn need not exist.

A configuration artifact is stated to reside in a configuration repository,
but the source does not govern who wrote it.
storedIn may exist; transfer need not exist.
```

## F. Minimal signature hypothesis

```text
storedIn
    storedItem -> BAReferent [1]
    store      -> BAReferent [1]
```

Cardinalities remain a working hypothesis until integrated admission.

No actor role is included: storage residence does not require the source to govern
the writer.

## G. Empirical disposition

```text
CURRENT CORPUS:
    TESTED_POSITIVE
    TESTED_NEGATIVE
    TESTED_BOUNDARY

GENERIC persist:
    REJECT AS CURRENT CANDIDATE FORMULATION

CC-03 storedIn:
    SURVIVES EXHAUSTION
    NOT_ADMITTED
    FORMAL G1-G8 PENDING
```

## H. G1-G8 readiness

```text
G1 Source evidence: STRONG
G2 General formulation: PROVISIONAL
G3 Construct exhaustion: PASS_CURRENT_CORPUS
G4 No false semantics: PROVISIONAL_PASS_WITH_NARROW_BOUNDARY
G5 Minimality: PROVISIONAL_PASS
G6 Non-redundancy: PROVISIONAL_PASS
G7 Backward compatibility: PENDING
G8 Projection/feedback value: POSITIVE / FORMAL REVIEW PENDING
```

No normative method delta is made by this pack.
