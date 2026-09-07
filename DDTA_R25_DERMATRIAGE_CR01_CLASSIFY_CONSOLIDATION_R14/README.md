# DDTA R25 — DermaTriage CR-01 `classify` Consolidation R14

Checkpoint:

`DDTA-R25-DERMATRIAGE-CR01-CLASSIFY-CONSOLIDATION-R14`

Required predecessor HEAD:

`81b94f5dd0fba9eaf6ba22f9b8c263158d62e55d`

## Purpose

Additively consolidate the completed CR-01 `classify` review while preserving the R13 construct-by-construct governance model and keeping BA0–BA5 frozen.

## Consolidated CR-01 result

Primary verdict:

`GUIDE_CLARIFICATION`

The existing `classify` operator remains sufficient.

CR-01 distinguishes:

- source-supported semantic kinds, which preserve governed project meaning;
- operational macro-kinds, which additionally justify reusable method-neutral treatment.

The retained operational macro-kind working set is:

```text
Actor
Component
Behavior
Interface
Boundary
Store
Information
State
```

Each macro-kind has a standard question pack for representation, query, documentation QA, and downstream analysis.

The set is not declared a closed universal taxonomy.

## Important non-loss rule

A project-specific or source-specific kind is not invalid merely because it is not in the operational macro-kind set.

For example, the explicit DermaTriage statement that two adaptation paths are `Capability` can remain source-supported classification meaning, while common structural treatment is provided by `Behavior`.

## Files introduced or updated

Added:

- `validation-evidence/dermatriage/post-holdout-method-review-r1/construct-reviews/CR-01_CLASSIFY.md`
- `DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/`

Updated:

- `validation-evidence/dermatriage/post-holdout-method-review-r1/CONSTRUCT_REVIEW_LEDGER.yml`
- `validation-evidence/dermatriage/post-holdout-method-review-r1/NEXT_STEP.md`

## Forbidden changes

This checkpoint does not modify:

- governed DermaTriage documentation;
- BA0–BA5 normative artifacts;
- R11 holdout evidence;
- R12 independent expert reports;
- the R13 work plan or historical checkpoint.

## Next review

`CR-02 — decisionRule + comparison condition language`
