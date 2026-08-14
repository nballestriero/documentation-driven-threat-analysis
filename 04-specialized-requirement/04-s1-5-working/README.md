# DDTA S1.5 working material

This directory contains the temporary S1.5 working formalization between SpecializedRequirement S1 and SecurityRequirement S2.

## Current correction

S1.5-A is now **CLOSED for the current thesis baseline**:

```text
Requirement [abstract]
    extends GovernedDocument
    normativeClause : NormativeClause [1..*]

FunctionalRequirement
    extends Requirement

SpecializedRequirement [abstract]
    extends Requirement
```

The previous candidate `NormativeObligation` metaclass is **REJECTED**. `Requirement` is itself the governed normative obligation. One Requirement may use one or more normative clauses, subject to the coherent-unit and split-on-independence invariants.

The provenance part of the working note remains intentionally incomplete: provenance/semantics separation is preserved, while `AnalysisRun`, `Finding`, `GovernedDocumentChangeEvent`, revision history and the acceptance workflow remain OPEN/DEFERRED for their owning later phases.

## Files

- `DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.md` - primary working note.
- `DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.tex` - typeset source.
- `DDTA_S1_5_REQUIREMENT_ABSTRACTION_PROVENANCE_WORKING.pdf` - rendered working artifact.
- `SHA256SUMS.txt` - checksums for the three working artifacts.

This is research material, not a standalone thesis chapter. Future consolidation belongs in Chapter 4 as common governed-document / Requirement structure, while provenance remains a separate cross-document concern.
