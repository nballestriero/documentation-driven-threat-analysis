# BA2-T3 cross-corpus regression drop-in

**Expected repository baseline before application:** `4d832bcf90109106d543029cb517be32a6fe7ea7`

This package executes only `BA2-T3 - cross-corpus regression of the operator/role/modifier candidate and semantic-key/lexical separation`. It does not close BA2 and does not execute BA3.

## Result

BA2-T3 replays the BA2-T2 candidate across the facial-access and order-fulfillment corpora and reduces the candidate before closure review.

Key dispositions:

- operator-family facet as normative semantics: **REMOVED**;
- operator seed: **REDUCED 14 -> 13**;
- `ownOrManage`: **MERGED INTO `assignResponsibility`** using `responsibilityKind` and polarity;
- missing method-neutral operator: **NONE FORCED**;
- `input` role under `produce`: **ADDED / FORCED BY REGRESSION**;
- `responsibilityKind`: **ADDED / FORCED BY MERGE**;
- semantic-key/source-lexical separation: **PASS**;
- explicit polarity: **RETAINED**;
- modifier lower bound: **REDUCED TO `condition` + `temporalScope`**;
- completion/failure, atomicity, concurrency and idempotency: **PROMOTED TO `constrain`** when governed/analytically relevant;
- classification-as-proposition: **RETAINED**;
- fixed universal semantic-kind taxonomy: **NOT REQUIRED**;
- bounded STRIDE consumer: **PASS WITHOUT DFD/STRIDE LEAKAGE**;
- third BA1 identity family: **NOT FORCED**.

BA2 remains open only for a dedicated closure review over the regressed R2 candidate.

## Existing tracked file modified

- `README.md`

No other existing tracked file is replaced. BA0, BA1, BA2-T1, BA2-T2, research terminology, Chapters 2-4 and historical work plans remain unchanged.

## New methodology artifacts

- `methodology/BA2_T3_CROSS_CORPUS_REGRESSION_R1.md/.tex/.pdf`
- `methodology/BA2_SEMANTIC_VOCABULARY_CANDIDATE_R2.md/.tex/.pdf`
- `methodology/BA2_T3_REGRESSION_LEDGER_R1.yml`
- `methodology/DDTA_CURRENT_RESEARCH_STATE_R8.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R11.md/.tex/.pdf`

## Post-package state

```text
BA0                 CLOSED
BA1                 CLOSED
BA2-T1              COMPLETED / PROVISIONAL CANDIDATE
BA2-T2              COMPLETED / PROVISIONAL PASS WITH REFINEMENT
BA2-T3              COMPLETED / PROVISIONAL PASS WITH REDUCTION
BA2                 STARTED / NOT CLOSED
BA3                 NOT STARTED
```

## Next authorized microstep

Only after this package is reviewed, committed, pushed and remotely verified:

> `BA2-T4 - relation/action vocabulary closure review over the regressed R2 candidate`

Do not start BA3, formal STRIDE overlay design, Common Finding schema or implementation work.

## Application rule

Before extraction, both `HEAD` and `origin/master` must equal the expected baseline and the worktree must be clean. Verify the ZIP SHA-256 supplied with the package. After extraction, expect exactly the one tracked modification listed above plus the new files in this README. Run `git diff --check` before staging and `git diff --cached --check` after staging; both must return no whitespace errors.
