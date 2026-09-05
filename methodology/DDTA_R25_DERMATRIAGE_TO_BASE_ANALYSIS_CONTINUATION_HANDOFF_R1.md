# DDTA R25 - DermaTriage to Base Analysis Continuation Handoff R1

**Status:** START NEXT BA SESSION HERE
**Promotion predecessor:** `bf2236cf921b73309b162c74af11e4edb6e95db9`
**Project authority:** `DERMATRIAGE-GOV-R1`
**Methodology authority:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5`

## Reading order

1. `methodology/DDTA_R25_DERMATRIAGE_DOCUMENTATION_AND_GUIDE_PROMOTION_CHECKPOINT_R1.md`
2. `methodology/DDTA_R25_BASE_ANALYSIS_WORK_PLAN_AFTER_DERMATRIAGE_PROMOTION_R1.md`
3. `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.pdf`
4. `governed-corpora/dermatriage/current-r1/corpus.manifest.yml`
5. `governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.pdf`
6. `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.pdf`
7. current BA0-BA5 contract files, with BA2 R3

## Session-start checks

- verify `master` is clean;
- resolve the exact current Git SHA;
- verify the authority registry marks `DERMATRIAGE-GOV-R1` as `CURRENT_GOVERNED` and `primaryBASourceAllowed: true`;
- pin that Git SHA as the concrete source revision for the BA session;
- do not use previous DermaTriage BA candidates as project authority.

## First action

Execute BA0 over the promoted DermaTriage baseline, then propose the minimum BAReferent/BAProposition set for one bounded branch before broadening coverage.

Do not create diagrams or start STRIDE before the relevant BA is accepted.
