# DDTA R25 — Documentation Guide Consolidation R43

## Status

`CANDIDATE DOCUMENTATION-METHOD CONSOLIDATION / NON-NORMATIVE / NO AUTHORITY CHANGE`

Exact repository baseline:

`bea1e6567d3f861294378b201648b0853b3c8a43`

R43 consolidates the documentation-method candidate after the BA guide set was separated into its own Core/Complete artifacts.

## Purpose

R43 produces one candidate successor surface for documentation authoring:

`methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R6_CANDIDATE_R2.{tex,pdf}`

The rename from the historical `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_*` naming is intentional. It clarifies that documentation authoring and Base Analysis are separate methodologies. R5 is not renamed retroactively and remains current authority.

## Separation contract

R6 R2 owns:

- governed-document authoring;
- L1/L2 meaning and representation;
- L3/L4 boundary;
- MR -> Decision -> FR -> specialization authoring;
- authority, lifecycle, provenance and source gaps;
- downstream handoff and governed feedback.

R6 R2 does not own:

- BA operators/signatures/roleKey/cardinalities;
- BAReferent/BAProposition construction;
- BA operator discrimination;
- threat/DFD projection mechanics.

Those belong to the separate BA Core/Complete guide set.

## Local cleanup expected

The user working tree currently contains four obsolete untracked R38-era files. After exact-hash verification, R43 replaces/removes them:

- `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R6_CANDIDATE_R1.{tex,pdf}`
- `DDTA_R25_GUIDE_CONSOLIDATION_MATRIX_R1.md`
- `DDTA_R25_GUIDE_CONSOLIDATION_REVIEW_CHECKLIST_R1.md`

`DDTA_ARTIFACT_EVOLUTION_AND_AUTHORITY_PROTOCOL_R1.md` is retained.
