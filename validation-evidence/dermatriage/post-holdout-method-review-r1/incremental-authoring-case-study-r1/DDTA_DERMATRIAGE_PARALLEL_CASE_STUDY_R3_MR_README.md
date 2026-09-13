# DermaTriage Parallel Case Study - R3 MR checkpoint

**Status:** FROZEN BOUNDED DOCUMENTATION CHECKPOINT / NOT CURRENT PROJECT AUTHORITY  
**Scope:** Project Problem Framing + MacroRequirement layer only  
**Method used:** `DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R3`  
**Project source authority for reconstruction:** exact original `OR2_Architecture_Document.pdf` extracted from `DermaTriage-Docs-20260830T152637Z-1-001.zip`

This artifact continues the established parallel case-study layout:

- left 2/3: DDTA project documentation;
- right 1/3: Base Analysis lane;
- the BA lane is intentionally not populated for the MR pages in this checkpoint;
- BA remains downstream and will be added only after the documentation slice is frozen.

## Frozen MR result

- `MR-01 - Valutazione di triage del caso dermatologico` - `PROCEED TO DECISIONS`;
- `MR-02 - Indicazione della destinazione specialistica` - `STOP AT MR`;
- `MR-03 - Validazione e correzione medica degli esiti` - `PROCEED TO DECISIONS`;
- `MR-04 - Adattamento controllato sulla base della revisione clinica` - `PROCEED TO DECISIONS`, with `dependsOn MR-03`.

No semantic `dependsOn MR-01` is asserted for MR-02 or MR-03 in this checkpoint. The source clearly shows operational consumption/flow, but the distinction between dataflow/output consumption and a true macro semantic dependency remains a guide-level point to be reviewed before promotion.

## Integrity

The first two pages preserve the previously approved case-study content and hashes:

- page 1: `ccabe4bed7cca4d2f68a2005e42f36e3`;
- page 2: `0fb76dc0491da2793823b20571e5268b`.

The complete page index is stored in `DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R3_MR_PAGE_MD5_INDEX.txt`.

This checkpoint does not alter `DERMATRIAGE-GOV-R1`, the current documentation-method authority, the current BA authority, or the canonical methodology style.
