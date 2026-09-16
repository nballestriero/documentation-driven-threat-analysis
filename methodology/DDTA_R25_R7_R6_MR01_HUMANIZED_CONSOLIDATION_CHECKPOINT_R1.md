# DDTA R25 - R7 R6 / DermaTriage MR-01 Humanized Documentation Consolidation Checkpoint R1

**Status:** REVIEW CHECKPOINT / NON-NORMATIVE / NOT PROMOTED
**Input repository baseline:** `9aab0f2bc76682829e17651650ef6e2d7e74c4fb`
**Purpose:** consolidate the humanized Decision-authoring guide successor and the humanized DermaTriage MR-01 Decision documentation successor before further review.

## 1. Guide successor

`methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R6.tex` and PDF companion.

This successor preserves the previously consolidated guide lineage and rewrites the Decision-authoring section for direct human use. The Decision section keeps the source-first, discovery/promotion, MR-stability, neutralization, semantic-level, independent-governance, removal/replacement, decomposition, Decision-family regression and layer-specific closure method while reducing research-ledger language.

The Decision `Context` is explicitly framed as the project/domain situation needed to understand why a choice matters; it must not narrate the analysis process or use the documentation itself as the project context.

The guide also clarifies that an element inside an architectural Decision does not automatically become another Decision. An independently assessable operational behavior governed by the parent Decision may instead become a FunctionalRequirement candidate.

The canonical LLM execution prompt remains unchanged in this review successor.

## 2. DermaTriage documentation successor

`validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R5_MR01_DECISIONS.tex` and PDF companion.

The successor preserves the parallel layout:

- Documentation: left 2/3;
- Base Analysis: right 1/3;
- documentation questions/doubts: gray boxes below the relevant MR or Decision in the documentation column.

MR-01 is followed immediately by its four currently accepted Decisions, one Decision per page:

1. triage continuity without an image;
2. P1-P4 operational-priority scale;
3. sequential four-stage image-based analytical pipeline;
4. separation between analytical urgency evaluation and subsequent operational-priority determination.

The Decision prose is humanized so that Context, Decision and Consequences read as ordinary project documentation rather than as a reconstruction/research record.

## 3. Deliberate limits

This checkpoint does not:

- promote R7 R6 to methodology authority;
- replace or modify earlier R7 R4/R5 artifacts;
- replace or modify earlier DermaTriage R3/R4 artifacts;
- declare that MR-01 can never expose additional Decisions if new authoritative evidence appears;
- resolve source-limited ambiguity by preference;
- start FunctionalRequirement authoring;
- start Base Analysis;
- start threat analysis.

## 4. Current MR-01 Decision-family interpretation

The current source set supports four accepted Decision identities. Lower-level meanings remain available for subsequent FR/realization analysis. In particular, the four analytical stages are not lost: their operational behaviors are expected to be revisited as FunctionalRequirement candidates when FR authoring is explicitly opened.

## 5. Next action

Read the R7 R6 guide and the DermaTriage R5 documentation slowly. Apply any semantic or editorial corrections as successor revisions. Only after explicit review should a later checkpoint decide whether to promote or proceed to FunctionalRequirement authoring.
