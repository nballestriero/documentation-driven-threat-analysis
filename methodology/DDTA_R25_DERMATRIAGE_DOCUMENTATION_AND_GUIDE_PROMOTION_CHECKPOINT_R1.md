# DDTA R25 - DermaTriage Documentation and Authoring Guide Promotion Checkpoint R1

**Status:** CURRENT PROMOTION CHECKPOINT / BA HANDOFF ENABLED
**Promotion prepared against repository commit:** `bf2236cf921b73309b162c74af11e4edb6e95db9`
**Methodology authority after this promotion:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5`
**DermaTriage project authority after this promotion:** `DERMATRIAGE-GOV-R1`
**Primary BA source allowed:** YES

## 1. Purpose

This checkpoint closes the controlled documentation rewrite that followed the DermaTriage holdout and records the authority transition needed to start Base Analysis from the resulting native-DDTA documentation.

The promotion is explicit. Chronological recency alone does not create authority.

## 2. Promoted methodology artifact

The following files become the current documentation-authoring methodology authority:

- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.tex`
- `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.pdf`

Revision 5 is the reviewed successor of Revision 4. R4 remains preserved as historical predecessor and regression evidence; it is not overwritten.

The R5 promotion preserves the existing L1 model and introduces no new metamodel class or cardinality. Its principal holdout-derived authoring refinements are:

- technical/architectural neutralization is a classification test, not a license to genericize final project documentation;
- material technology, component, algorithm, service, protocol and process choices may be governed through ordinary Decision/FunctionalRequirement authoring when the normal semantic gates justify them;
- project documentation uses the normal DDTA fields rather than parallel `Current realization`-style fields;
- `Consequences` describes consequences for the project/system, not DDTA review procedure;
- A10/A12 preserve materially governed concrete project information without moving BA normalization into documentation authoring;
- diagrams and other structured views remain downstream projections of Base Analysis.

## 3. Promoted DermaTriage project authority

The current governed DermaTriage baseline is rooted at:

`governed-corpora/dermatriage/current-r1/`

Authority key:

`DERMATRIAGE-GOV-R1`

The canonical authored source is:

`DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`

The PDF in the same directory is its governed human-readable rendering. The style file is presentation support and does not create a second semantic authority.

The corpus manifest marks the family `CURRENT_GOVERNED` and permits primary Base Analysis use.

## 4. Historical preservation

Earlier DermaTriage A5/A6 candidates, rewrite experiments and study checkpoints remain historical or experimental research evidence. They are not silently rewritten to look current.

The source package remains provenance/evidence for the holdout reconstruction:

`DermaTriage-Docs-20260830T152637Z-1-001.zip`

SHA-256:

`E9ED2C507BEFB95F54A52084687CD1E8798863AE81CF69D09568864D8CBF280E`

For new Base Analysis work, project meaning comes from the promoted governed documentation baseline, not by reopening the original package to invent or replace current project meaning.

## 5. Base Analysis authorization boundary

After this promotion is committed, an accepted DermaTriage BA run MUST pin both:

1. authority baseline `DERMATRIAGE-GOV-R1`;
2. the exact Git commit containing this promotion state.

The promotion source commit `bf2236cf921b73309b162c74af11e4edb6e95db9` is the predecessor used to prepare this change. It is not the future BA source commit. The BA source commit is the commit produced after this drop-in is reviewed and committed.

Base Analysis remains analytical representation, not project authority. Documentation gaps and `NOT SPECIFIED` meanings must remain unresolved in BA unless the governed documentation is changed through project governance.

## 6. What this promotion does not claim

This checkpoint does not:

- close BA6;
- create an accepted DermaTriage Base Analysis automatically;
- start STRIDE or STRIDE-AI;
- turn historical working candidates into authority;
- create new non-security SpecializedRequirement subclasses;
- permit BA or tool output to rewrite project meaning directly.

## 7. Forward pointer

Active work continues with:

`methodology/DDTA_R25_BASE_ANALYSIS_WORK_PLAN_AFTER_DERMATRIAGE_PROMOTION_R1.md`

and the continuation handoff:

`methodology/DDTA_R25_DERMATRIAGE_TO_BASE_ANALYSIS_CONTINUATION_HANDOFF_R1.md`
