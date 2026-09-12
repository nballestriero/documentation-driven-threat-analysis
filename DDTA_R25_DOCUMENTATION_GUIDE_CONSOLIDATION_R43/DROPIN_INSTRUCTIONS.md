# R43 drop-in instructions

R43 is applied to a working tree that may contain untracked R42 and R38-derived governance files. Do not require a globally clean working tree.

## Required HEAD

`bea1e6567d3f861294378b201648b0853b3c8a43`

## Obsolete untracked files replaced by R43

Verify exact SHA-256 before deleting:

```text
98e9d635cef606f16ed4c2cbaaba3654c1a10b3fa012b1f66d8dd92720a2877e  methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R6_CANDIDATE_R1.tex
d50bdd2c56a0b661206b2738f68feaa94fcc19c84468902816f77e9244aa2944  methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R6_CANDIDATE_R1.pdf
f22c10c43cac80c6c1b18658f1e2683c63a08c5f28cdbe3575749e9e19cebc17  methodology/DDTA_R25_GUIDE_CONSOLIDATION_MATRIX_R1.md
8e5893a528131fc0c81bda2b91e17c7edce93efecb3a040491ecb27e83dd5f19  methodology/DDTA_R25_GUIDE_CONSOLIDATION_REVIEW_CHECKLIST_R1.md
```

Copy R43 file-by-file with collision checks, verify `MANIFEST.sha256`, then remove the obsolete files only if their hashes still match the values above.
