# DDTA R25 — DermaTriage source-complete realignment R37

## Status

`REALIGNMENT CHECKPOINT / NON-NORMATIVE / NO METHOD AUTHORITY CHANGE`

Repository packaging baseline:

```text
6e6ec547d2def68833547cc7a5848835d6948b43
```

Lineage predecessor:

```text
DDTA_R25_DERMATRIAGE_CC04_INITIATE_CONSOLIDATION_R36
```

This checkpoint exists because a later documentation-generation attempt compressed the stable
methodology and the DermaTriage review evidence too aggressively. Those off-repository condensed
drafts are not accepted as cumulative successors of the current guides.

R37 restores a safe execution boundary before any normative consolidation.

## Stable authority preserved

R37 does **not** replace, shorten, rewrite, or supersede:

```text
methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.tex
methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex
methodology/DDTA_METHODOLOGY_GUIDE_STYLE_R1.sty
governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex
```

The frozen BA method remains:

```text
BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
top-level operator count = 14
```

No R37 artifact is a current methodology authority.

## Why R37 exists

The R25 DermaTriage work is a **second/control cycle** over an already validated operator basis.
Its purpose is to search for:

- redundancy;
- semantic boundary failures;
- under-modelled project meaning;
- documentation gaps;
- operator/condition pressure;
- corner cases;
- candidate constructs that survive delete/merge-first testing.

It must not be rewritten as if R25 were the original operator-discovery cycle.

The realignment also restores source-complete coverage. The governed DermaTriage baseline contains
26 active FunctionalRequirements, one superseded FR identity, four MacroRequirements, their
decisions, and an explicit documentation-gap register. A handful of illustrative FRs is not a
substitute for this coverage.

## R36 state preserved

At R36:

```text
CC-01 consumeData
    REJECTED_REDUNDANT

CC-02 provideService
    CANDIDATE_TESTED_POSITIVE
    NOT_ADMITTED

CC-03 storedIn
    CANDIDATE_TESTED_POSITIVE
    NOT_ADMITTED

CC-04 initiate
    CANDIDATE_TESTED_POSITIVE
    NOT_ADMITTED
```

No candidate above is promoted by R37.

## Post-R36 reconstruction captured by R37

R36 explicitly routed the next review to PR-13 bounded/ranked/recency selection.

The subsequent analysis is now captured in:

```text
validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/
    PR13_SELECTION_RECONSTRUCTION_R1.md
```

Its status is deliberately non-normative. The current working disposition is:

```text
REUSABLE_SELECTION_STRUCTURE
NO NEW TOP-LEVEL OPERATOR
NO BA2 R3 MUTATION
```

This finding preserves the distinction among criterion, ordering/ranking, bound, selected
membership and later retrieval.

## Required intermediate step before consolidation

R37 introduces exactly one new execution gate:

```text
methodology/
    DDTA_R25_SOURCE_COMPLETE_RECONSTRUCTION_AND_CONSOLIDATION_GATE_R1.md
```

The gate must be completed before deciding whether to:

1. author cumulative successor revisions of the normative guides;
2. keep a finding only in a worked/pedagogical companion;
3. keep it only as validation evidence;
4. correct/improve project documentation;
5. reopen a narrow targeted methodology question.

This prevents evidence from silently becoming normative method text.

## Deliverables in this drop-in

```text
DDTA_R25_DERMATRIAGE_REALIGNMENT_R37/
    README.md
    CONTINUATION.md
    REALIGNMENT_SCOPE.yml
    DROPIN_INSTRUCTIONS.md
    MANIFEST.sha256

methodology/
    DDTA_R25_SOURCE_COMPLETE_RECONSTRUCTION_AND_CONSOLIDATION_GATE_R1.md

validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/
    DDTA_R25_REVIEW_COVERAGE_MATRIX_R1.md
    PR13_SELECTION_RECONSTRUCTION_R1.md
```

## Explicit exclusions

This checkpoint intentionally does not contain:

- a new Documentation BA Authoring Guide;
- a new Base Analysis Operational Guide;
- a new governed DermaTriage documentation revision;
- an admitted fifteenth BA operator;
- a rewritten complete DermaTriage BA;
- the previously generated condensed R4/R6/integration drafts.

Those outputs are premature until the source-complete consolidation gate has been executed.

## Stopping rule

Do not label a future guide revision as current methodology authority merely because R25 generated
new evidence.

First complete the R37 gate. Then classify every proposed delta by destination and authority.
Only `GUIDE_DELTA_REQUIRED` items may enter a candidate cumulative guide revision, and even that
candidate remains non-authoritative until separately reviewed and approved.
