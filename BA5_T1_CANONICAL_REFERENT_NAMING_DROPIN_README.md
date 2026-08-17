# BA5-T1 canonical referent naming drop-in

**Expected repository baseline before application:** `aa4b785dc72c2fbcd20fd04976e77fca3d07bf25`

This package executes only `BA5-T1 - canonical referent naming and controlled-authoring boundary trial`, reflecting the stronger controlled-vocabulary hypothesis selected after BA4 closure.

It does **not** close BA5 and does not execute BA5-T2, BA6, formal STRIDE/STRIDE-AI schemas, AnalysisRecord/Common Finding or ThreatForge implementation work.

## Result

BA5-T1 pressure-tests whether a named shared project referent can use one exact canonical name across governed documentation, accepted BA and shared derived views without synonym normalization.

Key dispositions:

- one named referent -> one exact canonical name per governed baseline/naming scope: **REQUIRED**;
- same referent same name across governed semantic references: **REQUIRED**;
- same referent same name across shared derived views: **REQUIRED**;
- alias/synonym as a second normative entity identifier: **REJECTED**;
- case/format variants as implicit aliases: **REJECTED**;
- canonical-name collision within one naming scope: **REJECTED**;
- `canonicalName == BAReferent identity`: **REJECTED**;
- governed cross-baseline rename with BA3 `RETAIN`: **PASS**;
- projection-owned type/category labels: **ALLOWED**;
- method-owned non-referent interpretation/aggregation labels: **ALLOWED DOWNSTREAM**;
- tool exact validation/completion: **ALLOWED**;
- hidden synonym normalization by the tool: **REJECTED IN THE T1 CORE**;
- new BAE family or BA2 operator: **NOT FORCED**;
- BA1 / BA2 / BA3 / BA4 reopen: **NOT TRIGGERED**;
- BA5: **STARTED / NOT CLOSED**.

The decisive refinement is that canonical-name invariance is baseline-scoped. A governed rename such as `cameraIngresso -> cameraNord` may retain the same BAReferent identity when BA3 determines that the project meaning itself is unchanged.

## Existing tracked file modified

- `README.md`

No other existing tracked file is replaced. BA0-BA4 closure artifacts, Chapters 2-4 and historical work plans remain unchanged.

## New methodology artifacts

- `methodology/BA5_CANONICAL_REFERENT_NAMING_REGISTRY_CANDIDATE_R1.md/.tex/.pdf`
- `methodology/BA5_T1_CANONICAL_REFERENT_NAMING_CONTROLLED_AUTHORING_TRIAL_R1.md/.tex/.pdf`
- `methodology/BA5_T1_PROVISIONAL_LEDGER_R1.yml`
- `methodology/DDTA_CURRENT_RESEARCH_STATE_R17.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R20.md/.tex/.pdf`

## Post-package state

```text
BA0                 CLOSED
BA1                 CLOSED
BA2                 CLOSED
BA3                 CLOSED
BA4                 CLOSED
BA5-T1              COMPLETED / PROVISIONAL PASS WITH CANONICAL-REFERENT-NAMING LOWER-BOUND
BA5                 STARTED / NOT CLOSED
BA6                 NOT STARTED
```

## Next authorized microstep

Only after this package is reviewed, committed, pushed and remotely verified:

> `BA5-T2 - canonical semantic registry coverage and governed-extension pressure test`

Do not start BA6 before BA5 is explicitly closed.

## Application rule

Before extraction, both `HEAD` and `origin/master` must equal the expected baseline and the worktree must be clean. Verify the ZIP SHA-256 supplied with the package. After extraction, expect exactly the one tracked modification listed above plus the thirteen new files in this README. Run `git diff --check` before staging and `git diff --cached --check` after staging; both must return no whitespace errors.
