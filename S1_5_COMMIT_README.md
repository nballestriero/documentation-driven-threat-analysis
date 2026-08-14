# S1.5 commit drop-in

This package is designed to be extracted at the root of the repository:

`C:\Users\user\Documents\TESI`

It is **additive only**. It creates:

```text
04-specialized-requirement/
  04-s1-5-working/
    DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.md
    DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.tex
    DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.pdf
    README.md
    SHA256SUMS.txt
```

No existing thesis chapter or S1 artifact is replaced.

Expected baseline before extraction:

`9108917d1ca6dfa030df6625018520db0b05f6bf`

Suggested commit message:

`thesis: add S1.5 requirement abstraction working note`

`INDEX.md` is intentionally not modified. The working note can be indexed later if/when S1.5 is closed or promoted.
