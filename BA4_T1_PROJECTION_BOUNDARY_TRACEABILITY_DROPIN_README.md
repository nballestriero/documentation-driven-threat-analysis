# BA4-T1 projection boundary/traceability drop-in

**Expected repository baseline before application:** `ac49f02ca37d47e872b3ce5194f6dd0e26574d75`

This package executes only `BA4-T1 - projection boundary, traceability and semantic-preservation lower-bound trial`.

It does **not** close BA4 and does not execute BA4-T2, BA5, BA6, formal STRIDE/STRIDE-AI schemas, AnalysisRecord/Common Finding or ThreatForge implementation work.

## Result

BA4-T1 pressure-tests one human-oriented projection and one bounded method-oriented projection over the same accepted Base Analysis materialization, then replays facial M1/M3/M4 and order/provider controls.

Key dispositions:

- projection derived from accepted BA: **REQUIRED**;
- immutable projection revision: **REQUIRED**;
- explicit selection/coverage contract: **REQUIRED**;
- omission as project negation/absence: **REJECTED**;
- meaning-bearing projection item trace to BA: **REQUIRED**;
- duplicate governed-source provenance in every projection item: **NOT REQUIRED**;
- projection-local identity for meaning-bearing items: **REQUIRED**;
- role-bound trace when input contributions differ: **REQUIRED**;
- human selection/rename/grouping/aggregation: **PASS when semantic-preserving**;
- stronger shared aggregation: **REJECTED**;
- explicit method-owned interpretation: **ALLOWED DOWNSTREAM**;
- method interpretation promoted into BA: **REJECTED**;
- BA replacement/retirement handled by projection rebuild: **REQUIRED**;
- second project lifecycle model in projection: **REJECTED**;
- new BAE family or BA2 operator: **NOT FORCED**;
- BA1 / BA2 / BA3 reopen: **NOT TRIGGERED**;
- BA4: **STARTED / NOT CLOSED**.

## Existing tracked file modified

- `README.md`

No other existing tracked file is replaced. BA0-BA3 closure artifacts, Chapters 2-4 and historical work plans remain unchanged.

## New methodology artifacts

- `methodology/BA4_PROJECTION_BOUNDARY_TRACEABILITY_CANDIDATE_R1.md/.tex/.pdf`
- `methodology/BA4_T1_PROJECTION_BOUNDARY_TRACEABILITY_SEMANTIC_PRESERVATION_R1.md/.tex/.pdf`
- `methodology/BA4_T1_PROVISIONAL_LEDGER_R1.yml`
- `methodology/DDTA_CURRENT_RESEARCH_STATE_R14.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R17.md/.tex/.pdf`

## Post-package state

```text
BA0                 CLOSED
BA1                 CLOSED
BA2                 CLOSED
BA3                 CLOSED
BA4-T1              COMPLETED / PROVISIONAL PASS WITH PROJECTION-BOUNDARY LOWER-BOUND
BA4                 STARTED / NOT CLOSED
BA5                 NOT STARTED
BA6                 NOT STARTED
```

## Next authorized microstep

Only after this package is reviewed, committed, pushed and remotely verified:

> `BA4-T2 - method-owned interpretation, coverage loss and cross-projection consistency pressure test`

Do not start BA5, BA6 or downstream analysis schemas.

## Application rule

Before extraction, both `HEAD` and `origin/master` must equal the expected baseline and the worktree must be clean. Verify the ZIP SHA-256 supplied with the package. After extraction, expect exactly the one tracked modification listed above plus the thirteen new files in this README. Run `git diff --check` before staging and `git diff --cached --check` after staging; both must return no whitespace errors.
