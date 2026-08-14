# DDTA S1.5 working note

**Status:** temporary research material.

This directory records the S1.5 microstudy between SpecializedRequirement S1 and SecurityRequirement S2.
It is intentionally **not** a standalone thesis chapter and **not** a new canonical foundation.

The note studies two distinct questions:

1. whether `FunctionalRequirement` and `SpecializedRequirement` justify a common abstract `Requirement` contract;
2. which provenance capabilities a future DDTA analysis/history model must preserve without prematurely defining `AnalysisRecord`, `Finding`, revision or change-event machinery.

## Files

- `DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.md` - compact editable working source;
- `DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.tex` - standalone LaTeX formalization;
- `DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.pdf` - rendered study artifact;
- `SHA256SUMS.txt` - checksums for the three study files.

## Baseline

Repository: `nballestriero/documentation-driven-threat-analysis`

Baseline commit: `9108917d1ca6dfa030df6625018520db0b05f6bf`

## Epistemic boundary

`Requirement [abstract]` remains a **STRONG CANDIDATE** pending the final necessity test for an explicit L1 `NormativeObligation` metaclass.

Provenance separation and future lineage requirements are preserved as constraints; the structural provenance mechanism remains **OPEN**.
