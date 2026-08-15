# DDTA BA0-R systems-modeling research-history drop-in

**Expected repository baseline:** `89e5486e02d07ff5b97082f73a2e22ac1b4319ae`

Purpose: record the BA0-R literature research and its evolving conclusions in Git **without closing BA0-R, modifying the closed documentation semantics, or promoting candidate source records into the canonical literature registries**.

## Important ISO edition distinction

The user-supplied file reviewed in this package is **ISO/IEC/IEEE 42010:2011(E), first edition**, not the 2022 edition. The 2022 edition remains the separate ACCESS-LIMITED candidate `SRC-0043`. The 2011 full-text historical source is recorded as `SRC-0048`. No equivalence of normative clauses across editions is assumed.

The copyrighted ISO PDF is **not included** in this ZIP and MUST NOT be committed. Its reviewed local SHA-256 is:

`0b53b9400cd590f9a89d767333ff6d80f2296892a76ab8e08225eae035edb64f`

## What the drop-in adds

- source notes and excerpt ledgers for SRC-0039 through SRC-0048;
- LaTeX + PDF reading worksheets for SRC-0039 through SRC-0048;
- Revision 2 synthesis/ledger preserved as the pre-ISO full-text analysis state;
- Revision 3 synthesis/ledger incorporating the 2011 full-text regression;
- `BA0_R_SYSTEMS_MODELING_RESEARCH_CHECKPOINT_R1` in Markdown/LaTeX/PDF;
- sidecar review registries (`*.BA0-R.REVIEW-R3.yml`) that intentionally do **not** replace canonical registries.

## Semantic state after application

`BA0-R semantic closure = OPEN`, `BA0 = PAUSED`, `BA1 = NOT STARTED`.

The most important correction preserved by Revision 3 is that ISO 42010 supports both synthetic and projective construction of views. A single canonical underlying repository is therefore **not** a universal prior-art requirement; if DDTA chooses a canonical projective Base Analysis, BA0/BA4 must justify it as a DDTA design choice.

## Apply

Extract this ZIP at the repository root only after checking the baseline and a clean working tree. The ZIP contains only new paths; it does not intentionally overwrite canonical repository files.
