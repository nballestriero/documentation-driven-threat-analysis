# DDTA R25 DermaTriage MR Consolidation R46 - Continuation

## Exact baseline

Repository: `nballestriero/documentation-driven-threat-analysis`  
Branch: `master`  
Apply-on baseline: `ed2e9dc89515e9f578af1776cafdb7b42c49636c`

No commit or push is performed by this package.

## Consolidated state

- R5 remains documentation-method authority.
- BA R3 remains Base Analysis authority.
- R7 Rebuild R3 is frozen as the documentation-guide experiment baseline.
- DermaTriage Project Problem Framing + four-MR documentation is frozen in the R3 parallel case-study artifact.
- MR-02 intentionally stops at MR.
- MR-04 depends semantically on MR-03.
- MR-02 -> MR-01 and MR-03 -> MR-01 are not promoted to `dependsOn` in the frozen candidate; they remain explicit guide-review cases.
- The right-hand BA lane remains unpopulated on MR pages.

## Next sequence

1. Apply and review this R46 drop-in.
2. Preserve R7 R3 unchanged.
3. Review the six guide pressures G1-G6 recorded in the MR checkpoint.
4. Draft the smallest successor guide refinements as a new candidate revision.
5. Regression-test those refinements against the frozen DermaTriage MR case and non-DermaTriage examples.
6. Decide together which guide changes to keep.
7. Then populate the BA lane for the stable MR slice and continue the BA-guide rewrite.

## STOP conditions

STOP if:

- repository baseline differs from the expected SHA;
- working tree is dirty before the drop-in;
- canonical style blob differs before or after application;
- R7 R3 is modified in place;
- existing R1 case-study files are overwritten;
- frozen R3 MR artifact hashes differ from the expected hashes after copying;
- a guide change is introduced in this consolidation package;
- BA is populated before the guide-review decision or used to invent project meaning.
