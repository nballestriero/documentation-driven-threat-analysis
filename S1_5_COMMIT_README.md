# S1.5 correction drop-in

Extract this package at the repository root:

`C:\Users\user\Documents\TESI`

## Expected baseline

`544ef14d92b50cf956cf6e8dd1000079d757c49c`

This correction **replaces only the already committed S1.5 working files** and the associated README/checksum material:

```text
04-specialized-requirement/
  04-s1-5-working/
    DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.md
    DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.tex
    DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.pdf
    README.md
    SHA256SUMS.txt

S1_5_COMMIT_README.md
```

No thesis chapter, S1 R2 artifact, authoring-rules artifact, facial-access corpus, or `INDEX.md` is modified.

## Semantic correction

- `Requirement [abstract]`: **CLOSED** as common superclass of FunctionalRequirement and SpecializedRequirement.
- `Requirement.normativeClause : NormativeClause [1..*]`: **CLOSED** with coherent-unit and split-on-independence invariants.
- `NormativeObligation` as a separate L1 metaclass: **REJECTED**.
- Provenance constraints: preserved; structural mechanism remains **OPEN**.
- Next research phase: S2 `SecurityRequirement IS-A SpecializedRequirement`.

Suggested commit message:

`thesis: close S1.5 requirement abstraction`
