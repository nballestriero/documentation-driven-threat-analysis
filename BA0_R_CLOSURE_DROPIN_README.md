# DDTA BA0-R closure drop-in

Expected repository baseline:

`7acd2fb297f9e83049409268c18dac629cec5fcd`

Purpose: close the bounded BA0-R systems-modeling prior-art gate, promote SRC-0039 through SRC-0048 into the canonical literature/access registries, and preserve an explicit closure record without starting BA1 or modifying Chapters 2-4.

## Important constraints

- The helper verifies the exact baseline and refuses to run if either canonical registry already has local changes.
- SRC-0043 (ISO 42010:2022) and SRC-0045 (ArchiMate 3.2) are canonicalized as `partially_verified`, not as full-text verified evidence.
- SRC-0048 remains the separate full-text 2011 ISO 42010 edition; no equivalence with SRC-0043 is assumed.
- The helper normalizes new source `type` and `verification_state` fields to the vocabulary already documented in `literature/README.md`.
- The helper is temporary and should be deleted before staging.

## Persistent changes after application

Modified:
- `literature/literature.registry.yml`
- `literature/source-access.registry.yml`

Added:
- `literature/syntheses/BA0_R_CLOSURE_R1.md`
- `literature/syntheses/BA0_R_CLOSURE_R1.tex`
- `literature/syntheses/BA0_R_CLOSURE_R1.pdf`
- `BA0_R_CLOSURE_DROPIN_README.md`
- `BA0_R_CLOSURE_SHA256SUMS.txt`

Semantic state after commit:

`BA0-R = CLOSED`, `BA0 responsibility/non-goals = CURRENT`, `BA1 = NOT STARTED`.
