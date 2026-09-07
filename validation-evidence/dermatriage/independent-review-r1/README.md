# DermaTriage independent review R1

Checkpoint: `DDTA-R25-DERMATRIAGE-INDEPENDENT-REVIEW-GOVERNANCE-R12`
Purpose: `EXPERT_EVIDENCE_GOVERNANCE_AND_PROTOCOL_DEVIATION_CHECKPOINT`
Repository predecessor baseline: `36a1e1897302a77d3ecef5866e011f7082d0b597`
Status: **EVIDENCE PRESERVED — CROSS-REVIEW PENDING**

## Scope

This directory preserves the first independent expert review evidence collected after the DermaTriage holdout consolidation. It also records a guide-selection protocol deviation discovered during review of the supplied package.

No file in this evidence set changes BA0–BA6, accepted DermaTriage BA meaning, governed project documentation, or a prior checkpoint.

## Contents

- `PROTOCOL.md` — review and evidence-handling protocol;
- `INPUT_MANIFEST.yml` — known input identities, evidence-copy hashes, and provenance limits;
- `PROTOCOL_DEVIATION_GUIDE_SELECTION.md` — guide-selection incident and impact boundary;
- `expert-01/ORIGINAL_REPORT.md` — immutable original report;
- `expert-01/METADATA.yml` — report metadata and admissibility classification;
- `expert-02/ORIGINAL_REPORT.md` — immutable original report;
- `expert-02/METADATA.yml` — report metadata and admissibility classification;
- `EXPERT_REVIEW_CLASSIFICATION.md` — evidence-level classification only;
- `COMPARISON_PLAN.md` — planned three-way comparison protocol;
- `CHECKSUMS.sha256` — checksums for the evidence-set files other than itself.

## Critical provenance note

The recovered copies of the input PDFs are sufficient to record the content/version candidates and their evidence-copy hashes, but this checkpoint does **not** establish byte-for-byte identity between those recovered copies and the exact bytes delivered to each expert. `INPUT_MANIFEST.yml` therefore records `delivery_byte_identity: NOT_VERIFIED` rather than making a stronger claim.

## Next gate

The next activity is the three-way cross-review. Method changes remain blocked until the evidence review gate defined by the active work plan is satisfied.
