# DermaTriage guided documentation review R2

R2 is the second immutable research checkpoint of the R25 DermaTriage documentation holdout.
It is cumulative with R1 and records the explicit Research / Validation mode review of the Decision family under `MR-01 - Valutazione di triage del caso dermatologico`.

## Repository baseline used

`127c8a1532a193184ce86dd4c95f7547ce3606b9`

## Source authority

Original source package remains external evidence and is not copied into this directory:

`DermaTriage-Docs-20260830T152637Z-1-001.zip`

SHA-256:

`E9ED2C507BEFB95F54A52084687CD1E8798863AE81CF69D09568864D8CBF280E`

Previous DDTA reconstructions and Base Analysis are not project authority.

## R2 milestone

R2 preserves R1 and adds the Decision-family review for MR-01:

- `DEC-01 - Continuita' del triage in assenza di immagine`: PASS, SELECTABLE.
- `DEC-02 - Adozione della P-scale per la priorita' operativa`: REWORK -> PASS, SELECTABLE.
- SLA candidate: `NOT SPECIFIED`, not promoted to Decision because temporal semantics and responsibility owner are insufficiently defined.
- specialist candidate: outside the current MR-01 Decision family; routed to Macro Project Map review rather than forced under MR-01.
- cumulative D2 for MR-01: PASS; Decision layer closed for MR-01.

R2 also records that FR authoring is locally permitted under DEC-01/DEC-02 but globally deferred while the Macro Project Map is reopened to stabilize ownership of specialist routing, doctor validation/correction, learning/retraining lifecycle, and diagnostic-support boundaries.

## Method observations

R2 preserves and extends the methodology observation register, including the distinction between validation-record verbosity and operational authoring overhead, cross-layer classification assistance, numeric precision vs semantic sufficiency, and controlled upstream reopen when semantic ownership changes.

No modification to the R4 methodology is promoted by this checkpoint.

## Files

- `DDTA_R25_DERMATRIAGE_GUIDED_DOCUMENTATION_REVIEW_R2.tex`
- `DDTA_R25_DERMATRIAGE_GUIDED_DOCUMENTATION_REVIEW_R2.pdf`
- `DDTA_DERMATRIAGE_GUIDED_REVIEW_STYLE_R1.sty`
- `SHA256SUMS.txt`

## Build

From this directory:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error DDTA_R25_DERMATRIAGE_GUIDED_DOCUMENTATION_REVIEW_R2.tex
```

R2 is a research / methodology-validation artifact. It is not the final governed DermaTriage project documentation and it is not Base Analysis.
