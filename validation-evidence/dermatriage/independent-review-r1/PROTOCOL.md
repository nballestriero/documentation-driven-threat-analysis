# Independent review evidence protocol

## 1. Purpose

The independent review is used to measure how another analyst recovers governed meaning, applies BA concepts, rejects unsupported inference, identifies documentation gaps, and experiences the supplied guidance.

It is not a mechanism for allowing expert output to override governed documentation or silently redefine the DDTA method.

## 2. Authority order

The review must preserve the DDTA authority invariant:

```text
governed documentation
    -> Base Analysis
    -> deterministic/reproducible projections
    -> optional method-specific interpretation
```

Expert observations are validation evidence. They are not an upstream source of project truth.

## 3. Original-evidence preservation

Each `ORIGINAL_REPORT.md` is immutable evidence.

Rules:

- preserve bytes as received/recovered;
- record SHA-256 and byte size;
- never edit the original to normalize terminology or repair method usage;
- place any classification, reconciliation, or comparison in separate derived files;
- keep protocol limitations attached to claims derived from the report.

## 4. Protocol-deviation rule

The intended execution guide for a strict frozen-BA replication was `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.pdf`.

The review package instead supplied `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.pdf`.

Therefore these reviews are classified as `PROTOCOL_DEVIATED_WRONG_EXECUTION_GUIDE` for strict R3 replication purposes.

The reports remain usable for bounded evidence that does not require proving execution against the exact R3 operator contract.

## 5. Admissible evidence questions

This review set may be used to study:

- independent semantic recovery;
- discovery of documentation gaps and ambiguities;
- analyst identity/classification variance;
- rejected or resisted inference;
- usability and clarity of the package actually supplied;
- hypotheses for later method review;
- cross-review convergence and disagreement.

It must not alone be used to establish:

- strict BA2 R3 operator coverage;
- complete frozen-R3 construct sufficiency;
- exact R3 reproducibility percentages;
- an integrated BA6 verdict;
- a method change.

## 6. Cross-review discipline

The comparison is evidence classification, not method repair.

For each comparable claim, record source-local support and classify it as one of:

```text
3/3_CONVERGENCE
2/3_CONVERGENCE
OURS_ONLY
EXPERT_ONLY
DIRECT_DISAGREEMENT
NOT_COMPARABLE_DUE_TO_PROTOCOL
```

Do not collapse disagreement into a single synthesized answer before preserving each analyst's original position.

## 7. Corrected replication package

A future corrected replication intended to test frozen R3 should pin the exact package before delivery and include:

- governed DermaTriage documentation R1;
- Base Analysis Operational Guide R3;
- this or a successor independent-review protocol;
- a package manifest with exact role, filename, SHA-256, and delivery identifier.

An input-authority gate should verify that every supplied artifact matches the intended authority role before the package is released.
