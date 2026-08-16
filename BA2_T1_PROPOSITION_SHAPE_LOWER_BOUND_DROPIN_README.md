# BA2-T1 proposition-shape lower-bound drop-in

**Expected repository baseline before application:** `3d8251328c77177375cccf1c51caa54b7473e21e`

This package executes only `BA2-T1 - minimal BAProposition structural shape and participation-role lower-bound derivation`. It does not close BA2 and does not execute BA3.

## Result

BA2-T1 derives the following provisional structural lower bound:

```text
BAProposition
|- semanticOperator   1
|- participation      1..*
|    |- role          1
|    `- term          1
`- scopedModifier     0..*  [capability required; exact form open]
```

Key dispositions:

- pure binary SPO as universal core: REJECTED;
- binary propositions as special cases: SUPPORTED;
- explicit role-bound n-ary participation: FORCED CANDIDATE;
- explicit method-neutral semantic operator key: FORCED CANDIDATE;
- fixed DFD/domain-specific slot taxonomy: REJECTED;
- scoped semantic modifier capability: REQUIRED, encoding OPEN;
- third BA1 identity family: NOT FORCED;
- exact operator/role/classification vocabulary: OPEN / NEXT PRESSURE TARGET.

BA1 remains closed. No new BAE first-class type is introduced.

## Existing tracked file modified

- `README.md`

No other existing tracked file is replaced. BA0, BA1, research terminology, Chapters 2-4 and historical work plans remain unchanged.

## New methodology artifacts

- `methodology/BA2_T1_PROPOSITION_SHAPE_PARTICIPATION_LOWER_BOUND_R1.md/.tex/.pdf`
- `methodology/BA2_PROPOSITION_STRUCTURE_CANDIDATE_R1.md/.tex/.pdf`
- `methodology/BA2_T1_PROVISIONAL_LEDGER_R1.yml`
- `methodology/DDTA_CURRENT_RESEARCH_STATE_R6.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R9.md/.tex/.pdf`

## Post-package state

```text
BA0                 CLOSED
BA1                 CLOSED
BA2-T1              COMPLETED / PROVISIONAL CANDIDATE
BA2                 STARTED / NOT CLOSED
BA3                 NOT STARTED
```

## Next authorized microstep

Only after this package is reviewed, committed, pushed and remotely verified:

> `BA2-T2 - semantic operator, participation-role and scoped-modifier vocabulary pressure test`

Do not start BA3, formal STRIDE overlay design, Common Finding schema or implementation work.

## Application rule

Before extraction, both `HEAD` and `origin/master` must equal the expected baseline and the worktree must be clean. Verify the ZIP SHA-256 supplied with the package. After extraction, expect exactly the one tracked modification listed above plus the new files in this README. Run `git diff --check` before staging and `git diff --cached --check` after staging; both must return no whitespace errors.
