# DermaTriage guided documentation review - R3

This directory preserves the immutable R25 guided-review checkpoint that closes A2 / Macro Project Map after the controlled reopen triggered during the MR-01 Decision-family review.

## Milestone scope

R3 is cumulative with R2. It preserves the previously accepted authority gate, project framing, MR-01, DEC-01, DEC-02, SLA disposition, and local D2 closure, then adds:

- MR-02 - specialist routing, D1 PASS and STOP AT MR;
- MR-03 - management of clinical validation of outputs, D1 PASS / NON STOP;
- MR-04 - controlled adaptation based on clinical review, D1 PASS / NON STOP;
- `MR-04 dependsOn MR-03`;
- review of `predicted_pathology / diagnosis`, with the candidate diagnostic MR not promoted;
- routing of `predicted_pathology` to MR-01 downstream classification;
- cumulative Macro Project Map review and D1 cumulative PASS;
- holdout observations through `OBS-DDTA-DERMA-10`.

## Status

- Research / validation artifact, not the final DermaTriage governed-documentation baseline.
- Base Analysis remains blocked.
- FunctionalRequirement authoring remains deferred until active Decision branches are closed.
- Once committed, this R3 directory is immutable. Subsequent milestones must use a new revision directory.

## Build

From this directory, with a LaTeX environment containing the packages required by the preserved style:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error DDTA_R25_DERMATRIAGE_GUIDED_DOCUMENTATION_REVIEW_R3.tex
```
