# Protocol deviation — guide selection

Deviation ID: `DDTA-VAL-DERMA-R1-GUIDE-SELECTION-01`
Status: **OPEN / RECORDED**
Checkpoint: `DDTA-R25-DERMATRIAGE-INDEPENDENT-REVIEW-GOVERNANCE-R12`

## 1. Incident

The independent DermaTriage reviews were intended to exercise the frozen Base Analysis execution method. The intended execution guide was:

```text
DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.pdf
```

The package actually supplied the documentation BA authoring guide:

```text
DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.pdf
```

The original expert reports are not altered retrospectively.

## 2. Evidence

The recovered expert reports themselves are consistent with use of the supplied documentation-authoring guide:

- Expert 01 repeatedly refers to the documentation BA guide and cites its sections/examples;
- Expert 02 explicitly states that the analysis applies the Base Analysis methodology from the DDTA R5 guide.

The package manifest records the SHA-256 of currently recovered evidence copies of the relevant PDFs. Byte-for-byte identity between those recovered PDF copies and the precise files delivered to each expert is not independently established and is therefore recorded as `NOT_VERIFIED`.

## 3. Impact boundary

The deviation does **not** make the reports worthless.

They remain admissible for:

- independent recovery of governed semantics;
- documentation-gap and ambiguity discovery;
- analyst-decision variance;
- observations on the guide/package actually used;
- convergence in refusal to invent unsupported meaning;
- generation of hypotheses for subsequent method review.

They are not strict evidence, on their own, for:

- BA2 R3 operator-coverage completeness;
- frozen-R3 construct sufficiency;
- exact quantitative R3 reproducibility;
- an integrated BA6 pass/fail result;
- automatic promotion of a method pressure.

## 4. Root-cause classification

Current process-level root cause:

`AUTHORITY_ROLE_SELECTION_FAILURE`

Contributing conditions:

1. naming ambiguity around a generic request for the "BA guide";
2. absence of an explicit `INPUT_AUTHORITY_GATE` before delivery;
3. absence of a sealed input manifest binding file names, roles, versions, and hashes to the review package;
4. insufficient separation between documentation-authoring guidance and BA-execution guidance at the package handoff boundary.

These are validation-protocol findings. They do not alter governed DermaTriage meaning.

## 5. Corrective controls

For a corrected replication:

- use an explicit package ID;
- assign one authority role to every supplied artifact;
- require a pre-delivery authority-role check;
- record SHA-256 before delivery;
- preserve the delivered package or archive as immutable evidence;
- record analyst/report identity separately from input authority;
- prohibit substitution of a similarly named guide without a new package version.

## 6. Research implication

DDTA authority discipline is required at two distinct levels:

```text
PROJECT AUTHORITY DISCIPLINE
    governs what project meaning may enter BA

VALIDATION AUTHORITY DISCIPLINE
    governs what methodological/input package a validation result actually tests
```

A validation result can only support claims about the method version and source package that were actually supplied.
