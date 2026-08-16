# BA1-T2 split-or-collapse pressure-test drop-in

**Expected repository baseline before application:** `f05fbb7b253392e158a1062df2614b177c13d43e`

This package executes only `BA1-T2 - split-or-collapse pressure test of the two-family candidate`. It does not close BA1 and does not execute BA2.

## Result

BA1-T2 retains a refined two-family candidate:

```text
BAReferent     STRONG CANDIDATE / NOT ACCEPTED
BAProposition  STRONG CANDIDATE / NOT ACCEPTED
```

No tested semantic kind forces a dedicated first-class split. The pressure test covers behavior/event identity, information/resource lifecycle, responsibility/externality, store/contract identity, state/context semantics and one bounded method-consumer projection.

The opposite semantic collapse into one undifferentiated analytical family is rejected.

One BA1-T1 feature is reduced: `BAProposition` is no longer required to serve as a project-semantic target for another proposition. Reusable or constrained project meaning receives `BAReferent` identity; proposition identity remains for assertion-level provenance, diagnosis and change disposition.

No relation/action vocabulary is closed.

## Existing tracked file modified

- `README.md`

No other existing tracked file is replaced. BA0 artifacts, BA1-T1 artifacts, research terminology, Chapters 2-4 and historical work plans remain unchanged.

## New methodology artifacts

- `methodology/BA1_T2_SPLIT_OR_COLLAPSE_PRESSURE_TEST_R1.md/.tex/.pdf`
- `methodology/BA1_MINIMAL_BAE_ONTOLOGY_CANDIDATE_R2.md/.tex/.pdf`
- `methodology/BA1_T2_PROVISIONAL_LEDGER_R1.yml`
- `methodology/DDTA_CURRENT_RESEARCH_STATE_R4.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R7.md/.tex/.pdf`

## Post-package state

```text
BA0 responsibility/non-goals  CLOSED
BA1-T1                        COMPLETED / PROVISIONAL CANDIDATE
BA1-T2                        COMPLETED / PROVISIONAL PASS WITH REFINEMENT
BA1 ontology                  OPEN / READY FOR DISTINCT CLOSURE REVIEW
BA2                           NOT STARTED
```

## Next authorized microstep

Only after this package is reviewed and committed:

> `BA1-T3 - minimal BAE ontology closure review`

Do not start BA2, formal STRIDE overlay design, Common Finding schema or implementation work.

## Application rule

Before extraction, both `HEAD` and `origin/master` must equal the expected baseline and the worktree must be clean. Verify the ZIP SHA-256 supplied with the package. After extraction, expect exactly the one tracked modification listed above plus the new files in this README. Run `git diff --check` before staging and `git diff --cached --check` after staging; both must return no whitespace errors.
