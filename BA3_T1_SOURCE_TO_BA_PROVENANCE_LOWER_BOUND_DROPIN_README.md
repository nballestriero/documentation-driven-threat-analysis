# BA3-T1 source-to-Base-Analysis provenance lower-bound drop-in

**Expected repository baseline before application:** `97ad32fb427f808521f9fe13fb6901465ccfd715`

This package executes only `BA3-T1 - source-to-Base-Analysis derivation and provenance lower-bound pressure test`.

It does **not** close BA3 and does not execute BA3-T2, BA4, formal threat-method overlays, Common Finding or implementation work.

## Result

BA3-T1 derives the minimum origin/provenance structure required by the closed BA0 responsibilities and current corpora.

Key dispositions:

- provenance on `BAReferent`: **REQUIRED**;
- provenance on `BAProposition`: **REQUIRED**;
- independent provenance per BA1 identity: **REQUIRED**;
- source-to-BA lineage: **MANY-TO-MANY REQUIRED**;
- immutable governed baseline context: **REQUIRED**;
- logical document identity + exact source locator: **REQUIRED**;
- copied source prose as BA authority: **REJECTED**;
- `GROUNDED`, `DERIVED`, `DIAGNOSTIC_UNRESOLVED`: **REQUIRED**;
- derived basis distinct from source authority: **REQUIRED**;
- inspectable derivation rule/rationale reference: **REQUIRED CANDIDATE / EXACT REGISTRY OPEN**;
- origin state = acceptance/review lifecycle: **REJECTED**;
- new provenance BAE family: **NOT FORCED**;
- method finding / ThreatForge runtime state as governed source: **REJECTED**;
- BA1 / BA2 reopen: **NOT TRIGGERED**.

BA3 remains open for cross-baseline identity, staleness, lifecycle, diagnostic resolution and later change/feedback mechanics.

## Existing tracked file modified

- `README.md`

No other existing tracked file is replaced. BA0, BA1, BA2, research terminology, Chapters 2-4 and historical work plans remain unchanged.

## New methodology artifacts

- `methodology/BA3_PROVENANCE_DERIVATION_CANDIDATE_R1.md/.tex/.pdf`
- `methodology/BA3_T1_SOURCE_TO_BA_PROVENANCE_LOWER_BOUND_R1.md/.tex/.pdf`
- `methodology/BA3_T1_PROVISIONAL_LEDGER_R1.yml`
- `methodology/DDTA_CURRENT_RESEARCH_STATE_R10.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R13.md/.tex/.pdf`

## Post-package state

```text
BA0                 CLOSED
BA1                 CLOSED
BA2                 CLOSED
BA3-T1              COMPLETED / PROVISIONAL PASS WITH LOWER-BOUND CANDIDATE
BA3                 STARTED / NOT CLOSED
BA4                 NOT STARTED
```

## Next authorized microstep

Only after this package is reviewed, committed, pushed and remotely verified:

> `BA3-T2 - cross-baseline identity, staleness and lifecycle pressure test`

Do not start BA4, formal threat-method overlays, Common Finding schema or implementation work.

## Application rule

Before extraction, both `HEAD` and `origin/master` must equal the expected baseline and the worktree must be clean. Verify the ZIP SHA-256 supplied with the package. After extraction, expect exactly the one tracked modification listed above plus the thirteen new files in this README. Run `git diff --check` before staging and `git diff --cached --check` after staging; both must return no whitespace errors.
