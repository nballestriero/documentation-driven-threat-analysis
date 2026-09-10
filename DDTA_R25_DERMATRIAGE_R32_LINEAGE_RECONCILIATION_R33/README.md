# DDTA R25 — R32 lineage reconciliation R33

This checkpoint repairs governance metadata after two different R32 checkpoints were committed sequentially.

Actual Git history:

```text
ca99122b2f628f169bed85e04e731c8f3f89ca3c  R31 — OP-14 decisionRule consolidation
  -> 666c192581dc58c0c464703807d36328bdbf4f7e  R32 — post-operator-audit disposition work plan
  -> 3cdd912e76ceeb19d2224efa6a506a793d35f26c  R32 — first candidate group consolidation
```

The second R32 was semantically useful, but its package had stale predecessor metadata. Its verifier correctly rejected application against `ca99122b2f628f169bed85e04e731c8f3f89ca3c` because the repository was already at `666c192581dc58c0c464703807d36328bdbf4f7e`. The files were nevertheless committed as a normal child of `666c192581dc58c0c464703807d36328bdbf4f7e`.

R33 does not amend, delete or force-rewrite either published R32 commit. It creates an unambiguous successor plan R5, ledger R19 and disposition matrix R2.

Semantic outcome preserved:

```text
PR-01 perform: pressure retained; irreducibility not demonstrated; not admitted
CC-01 consumeData: CANDIDATE_REJECTED_REDUNDANT
CC-02 provideService: CANDIDATE_INSUFFICIENT_EVIDENCE
generic consume: NOT_JUSTIFIED
generic modify: REJECTED_FALSE_SEMANTICS_AS_GENERIC_OPERATOR
OBS-OT-01 operation-target/effect-scope: RETAINED_LEVEL_UNRESOLVED
```

No BA0–BA5 construct changes. The top-level basis remains 14 operators.
