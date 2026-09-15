# MR-01 External Decision Validation R1

This directory preserves the two answer-blind external MR-01 Decision reconstructions and the three-way reconciliation checkpoint used before R7 authoring.

## Frozen internal reference

- repository baseline: `c91dd567564e4a7f61c2e4e11fb4a9495623aa01`
- internal ledger SHA-256 at closure: `9a8b925ad660c0aab52ff586447b58ce3c8b2cede01506eb0618471027f670f9`

## External artifacts

- `EXTERNAL_REVIEW_1.md`
  - SHA-256: `d1559043d9611a0fbbb7753c7f2a0cc7ed99d517815ec31e59fd0cfc5908faf3`
- `EXTERNAL_REVIEW_2_MISTRAL_MEDIUM_3_5.md`
  - SHA-256: `5a11bfcf24f5b11e91a8f75a1e4f4c8a75f56130f2c72515c8fcfca01405bb92`

## Blind-review package provenance

- package: `DDTA_MR01_EXTERNAL_BLIND_REVIEW_R1.zip`
- package SHA-256: `e25514e7fd78300bc4e1353aa85ab9bf11f148f078760f96fe1684e97c5ee5e8`
- operational six-PDF source subset SHA-256: `e9e54d3ba7c06a5a4c215d015bc741e99a254f7337900ad60b783420039a6fed`

The experiment is answer-blind but not example-blind because R5/R6 contain historical DermaTriage examples.

## Current reconciled state

- CDEC-01-01: KEEP
- CDEC-01-02: KEEP, narrow P1-P4 identity
- CDEC-01-03: KEEP, technology-neutral four-stage identity
- CDEC-01-04A: LOWER_LEVEL after reconciliation
- CDEC-01-05: HOLD / BOUNDARY_REVIEW
- CDEC-01-06: LOWER_LEVEL after reconciliation
- CDEC-01-07: LOWER_LEVEL after reconciliation
- CDEC-01-08: KEEP

See `DDTA_R25_MR01_EXTERNAL_VALIDATION_RECONCILIATION_CHECKPOINT_R1.md` for the full rationale.
