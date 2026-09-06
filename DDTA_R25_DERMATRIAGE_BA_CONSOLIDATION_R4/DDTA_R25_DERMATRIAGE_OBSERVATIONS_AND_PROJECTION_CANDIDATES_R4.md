# DermaTriage R4 — Observations and Projection Candidates

These are guide/research hypotheses, not BA0–BA6 authority.

## O-03 — DATA INTERACTION COMPLETENESS

**Status:** `STRONGLY_SUPPORTED_GUIDE_CANDIDATE`

For each material data interaction, determine where relevant:

```text
WHAT?
    data artifact
    fields/components
    required/optional
    semantic binding

FROM WHERE?
    producer/source system/source store/provenance

TO WHERE?
    consumer/destination system/destination store

WHAT OPERATION?
    produce/read/query/write/index/persist/transfer

HOW?
    interface/path/protocol/medium/serialization when governed

WITH WHICH LINEAGE?
    copied/derived/transformed/correlated/versioned
```

Missing facts remain explicit documentation gaps and are never completed by BA
inference.

O-03 is not a new BA operator.

## O-04 — LOGICAL DATA FLOW != PHYSICAL DATA EXCHANGE

```text
A produces DataX
B uses DataX
```

does not itself establish HTTP, network transfer, file transfer, message bus, trust
boundary, transport security or physical medium.

Physical exchange requires independent governed evidence.

## BA4 candidate — LOGICAL DATA FLOW VIEW

Show producer -> information -> consumer without inventing physical transport.

## BA4 candidate — DATA CONTRACT FLOW VIEW

Show data artifact plus governed field/component contract between producer/consumer.

Potential later uses:

- privacy review;
- minimization;
- interface consistency;
- data governance;
- threat-analysis preparation.

## BA4 candidate — DATA LOCATION / STORE VIEW

Show governed data-artifact placement plus readers/writers only when accepted BA can
preserve the store association.

## Privacy separation

BA preserves project meaning such as field identity, contract, store, producer,
consumer, transfer/path. A later privacy method may classify sensitivity and apply
handling rules. BA must not silently add privacy classification absent governed
project meaning.
