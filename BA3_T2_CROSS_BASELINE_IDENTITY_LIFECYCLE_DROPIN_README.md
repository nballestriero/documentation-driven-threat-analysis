# BA3-T2 cross-baseline identity/lifecycle drop-in

**Expected repository baseline before application:** `52864d2ce177abdd694436306d8152db688effa0`

This package executes only `BA3-T2 - cross-baseline identity, staleness and lifecycle pressure test`.

It does **not** close BA3 and does not execute BA3-T3, BA4, formal threat-method overlays, Common Finding or implementation work.

## Result

BA3-T2 replays the BA3-T1 provenance lower bound across facial-access M1/M2/M3 and the order-fulfillment internal/external inventory-authority control.

Key dispositions:

- stable cross-baseline semantic identity: **REQUIRED CAPABILITY**;
- `BAReferent` continuity: **RETAIN WHEN THE SAME REUSABLE PROJECT MEANING SURVIVES**;
- `BAProposition` continuity: **RETAIN ONLY UNDER NORMALIZED ASSERTION EQUIVALENCE**;
- source document revision -> same BA identity: **REJECTED**;
- BA continuity dispositions: **`RETAIN | REPLACE | RETIRE`**;
- BA-level `REVISE` as fourth identity disposition: **NOT REQUIRED**;
- review state: **`PENDING_REVIEW | ACCEPTED | REJECTED` REQUIRED**;
- freshness: **`CURRENT | STALE` REQUIRED**;
- accepted `REPLACE`: prior element **SUPERSEDED**;
- accepted `RETIRE`: prior element **RETIRED**;
- resolved diagnostic rewritten from unresolved to grounded: **REJECTED**;
- historical provenance deletion after replacement/retirement: **REJECTED**;
- new lifecycle BAE family: **NOT FORCED**;
- BA1 / BA2 reopen: **NOT TRIGGERED**.

BA3 remains open for derivation-rule reproducibility, effective dependency/change-impact lineage and feedback provenance.

## Existing tracked file modified

- `README.md`

No other existing tracked file is replaced. BA0, BA1, BA2, BA3-T1, research terminology, Chapters 2-4 and historical work plans remain unchanged.

## New methodology artifacts

- `methodology/BA3_IDENTITY_LIFECYCLE_CANDIDATE_R1.md/.tex/.pdf`
- `methodology/BA3_T2_CROSS_BASELINE_IDENTITY_STALENESS_LIFECYCLE_R1.md/.tex/.pdf`
- `methodology/BA3_T2_PROVISIONAL_LEDGER_R1.yml`
- `methodology/DDTA_CURRENT_RESEARCH_STATE_R11.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R14.md/.tex/.pdf`

## Post-package state

```text
BA0                 CLOSED
BA1                 CLOSED
BA2                 CLOSED
BA3-T1              COMPLETED / PROVISIONAL PASS WITH LOWER-BOUND CANDIDATE
BA3-T2              COMPLETED / PROVISIONAL PASS WITH IDENTITY-LIFECYCLE REFINEMENT
BA3                 STARTED / NOT CLOSED
BA4                 NOT STARTED
```

## Next authorized microstep

Only after this package is reviewed, committed, pushed and remotely verified:

> `BA3-T3 - derivation-rule reproducibility and change-impact lineage pressure test`

Do not start BA4, formal threat-method overlays, Common Finding schema or implementation work.

## Application rule

Before extraction, both `HEAD` and `origin/master` must equal the expected baseline and the worktree must be clean. Verify the ZIP SHA-256 supplied with the package. After extraction, expect exactly the one tracked modification listed above plus the thirteen new files in this README. Run `git diff --check` before staging and `git diff --cached --check` after staging; both must return no whitespace errors.
