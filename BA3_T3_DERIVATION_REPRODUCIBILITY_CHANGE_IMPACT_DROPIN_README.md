# BA3-T3 derivation reproducibility/change-impact drop-in

**Expected repository baseline before application:** `5fc0b92809ece193deaba4206488d78f981f7855`

This package executes only `BA3-T3 - derivation-rule reproducibility and change-impact lineage pressure test`.

It does **not** close BA3 and does not execute BA3-T4, BA4, formal threat-method overlays, Common Finding or implementation work.

## Result

BA3-T3 pressure-tests the T1/T2 contracts against facial M4 effective-governed-context change, provider-state normalization and the analysis-to-governance feedback loop.

Key dispositions:

- plain untyped `derivationBasis`: **REJECTED**;
- role-bound `derivationBasisBinding`: **REQUIRED**;
- immutable inspectable derivation-rule revision: **REQUIRED**;
- universal executable derivation language: **REJECTED**;
- semantic replay/review reproducibility: **REQUIRED**;
- explicit `revalidationContext`: **REQUIRED**;
- `revalidationContext` as BA2 `dependOn`: **REJECTED**;
- M4 silent BA repair from sibling Decision: **REJECTED**;
- localized staleness propagation: **REQUIRED**;
- whole-BA invalidation on any file change: **REJECTED**;
- project-specific provider mapping hidden in tool: **REJECTED**;
- analysis result/corrective candidate as BA source authority: **REJECTED**;
- new BAE family: **NOT FORCED**;
- BA1 / BA2 / BA3-T1 / BA3-T2 reopen: **NOT TRIGGERED**.

BA3 remains open only for the integrated BA3-T4 closure review.

## Existing tracked file modified

- `README.md`

No other existing tracked file is replaced. BA0, BA1, BA2, BA3-T1, BA3-T2, research terminology, Chapters 2-4 and historical work plans remain unchanged.

## New methodology artifacts

- `methodology/BA3_DERIVATION_CHANGE_IMPACT_CANDIDATE_R1.md/.tex/.pdf`
- `methodology/BA3_T3_DERIVATION_REPRODUCIBILITY_CHANGE_IMPACT_R1.md/.tex/.pdf`
- `methodology/BA3_T3_PROVISIONAL_LEDGER_R1.yml`
- `methodology/DDTA_CURRENT_RESEARCH_STATE_R12.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R15.md/.tex/.pdf`

## Post-package state

```text
BA0                 CLOSED
BA1                 CLOSED
BA2                 CLOSED
BA3-T1              COMPLETED / PROVISIONAL PASS WITH LOWER-BOUND CANDIDATE
BA3-T2              COMPLETED / PROVISIONAL PASS WITH IDENTITY-LIFECYCLE REFINEMENT
BA3-T3              COMPLETED / PROVISIONAL PASS WITH DERIVATION-IMPACT REFINEMENT
BA3                 STARTED / NOT CLOSED
BA4                 NOT STARTED
```

## Next authorized microstep

Only after this package is reviewed, committed, pushed and remotely verified:

> `BA3-T4 - provenance, identity/lifecycle and derivation/change-impact closure review`

Do not start BA4, formal threat-method overlays, Common Finding schema or implementation work.

## Application rule

Before extraction, both `HEAD` and `origin/master` must equal the expected baseline and the worktree must be clean. Verify the ZIP SHA-256 supplied with the package. After extraction, expect exactly the one tracked modification listed above plus the thirteen new files in this README. Run `git diff --check` before staging and `git diff --cached --check` after staging; both must return no whitespace errors.
