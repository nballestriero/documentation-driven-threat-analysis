# DDTA R25 — OP-05 `transition` Discovery Checkpoint R21

R21 is an **intermediate checkpoint**, not closure of OP-05.

## Baseline

`ed403c248e0f7f61a49f16b74d2a40847acef41a`

## Frozen construct

```text
transition
    subject   -> BAReferent [1]
    toState   -> BAReferent [1]
    actor     -> BAReferent [0..1]
    fromState -> BAReferent [0..1]
```

Meaning: governed state/lifecycle change of a subject.

## General interpretation under test

A valid transition candidate requires the **same project-semantic identity before and after** plus a source-governed state/lifecycle change.

Do not equate generic mutation, production, activation, qualification, persistence, version selection, documentation governance, or property change with `transition`.

## Two-stage validation pattern

```text
ENTIRE GOVERNED DOCUMENTATION
    -> GENERAL SEMANTIC DISCOVERY PACK
    -> candidate semantic facts / routing
    -> CONSTRUCT-SPECIFIC QUESTION PACK
    -> admit / reject / reroute / documentation QA
```

## Current candidates

- **FR-10**: already-adopted adaptation -> revocation. Strongest positive candidate. Keep adaptation lifecycle separate from active-version restoration.
- **FR-09**: candidate adaptation -> qualified for adoption. Open boundary between lifecycle transition and decision/evaluation result.

## Negative controls

- FR-04/FR-05 activation: likely trigger semantics; do not invent `INACTIVE -> ACTIVE`.
- FR-27 parameter update: mutation/update is not automatically lifecycle transition.
- documentation metadata `current/superseded`: governance lifecycle is not automatically project-semantic lifecycle.

## Documentation QA

- FR-03/FR-12: review overwrite/history/retention/finality not sufficiently governed.
- FR-26: update/reset/history/version state exists, but `fromState -> toState` semantics are unclear.

## State representation hypothesis

BA2 R3 currently requires state roles to bind BAReferents. R21 only opens the question whether simple governed local state values could sometimes be more minimal. No contract change is authorized.

## Closure rule

OP-05 remains open until whole-document discovery and transition-specific falsification are recorded, including positive, negative, ambiguous and QA outcomes plus delete/merge-first redundancy testing.
