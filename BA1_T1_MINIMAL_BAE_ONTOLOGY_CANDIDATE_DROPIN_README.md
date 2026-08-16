# BA1-T1 minimal BAE ontology candidate drop-in

**Expected repository baseline before application:** `83af68cb1a02a6b1e76f591d4c1519f9496be3b3`

This package executes only `BA1-T1 - minimal BAE ontology candidate derivation from the closed BA0 responsibilities`. It does not close BA1 and does not execute BA2.

## Result

BA1-T1 derives a falsifiable two-family candidate:

```text
BAReferent     CANDIDATE / NOT ACCEPTED
BAProposition  CANDIDATE / NOT ACCEPTED
```

The candidate is a lower bound, not a final taxonomy. It rejects one undifferentiated analytical element as too weak, but does not yet promote `Behavior`, `Information`, `Participant`, `Store`, `Contract`, `Boundary`, `State` or other recurring semantic kinds to first-class metaclasses.

No relation vocabulary is closed.

## Evidence pressure used

The derivation combines:

- `methodology/BA0_BASE_ANALYSIS_RESPONSIBILITY_BOUNDARY_R1.md`;
- BA0-T1/T2 facial-access evidence and mutations;
- `03-functional-requirement/03-example-order-fulfillment/ORDER_FULFILLMENT_COMPLETE_AUTHORING_PROBE_R3.md` as a structurally distinct corpus;
- documentation-layer layering, Decision and FR constraints;
- BA0-R prior-art conclusions without inheriting any prior-art metaclass by default.

## Existing tracked file modified

- `README.md`

No other existing tracked file is replaced. BA0 artifacts, research terminology, Chapters 2-4 and historical work plans remain unchanged.

## New methodology artifacts

- `methodology/BA1_T1_MINIMAL_BAE_ONTOLOGY_CANDIDATE_DERIVATION_R1.md/.tex/.pdf`
- `methodology/BA1_MINIMAL_BAE_ONTOLOGY_CANDIDATE_R1.md/.tex/.pdf`
- `methodology/BA1_T1_PROVISIONAL_LEDGER_R1.yml`
- `methodology/DDTA_CURRENT_RESEARCH_STATE_R3.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R6.md/.tex/.pdf`

## Post-package state

```text
BA0 responsibility/non-goals  CLOSED
BA1-T1                        COMPLETED / PROVISIONAL CANDIDATE
BA1 ontology                  STARTED / NOT CLOSED
BA2                           NOT STARTED
```

## Next authorized microstep

Only after this package is reviewed and committed:

> `BA1-T2 - split-or-collapse pressure test of the two-family candidate`

Do not start BA2, formal STRIDE overlay design, Common Finding schema or implementation work.

## Application rule

Before extraction, both `HEAD` and `origin/master` must equal the expected baseline and the worktree must be clean. Verify the ZIP SHA-256 supplied with the package. After extraction, expect exactly the one tracked modification listed above plus the new files in this README. Run `git diff --check` before staging and `git diff --cached --check` after staging; both must return no whitespace errors.
