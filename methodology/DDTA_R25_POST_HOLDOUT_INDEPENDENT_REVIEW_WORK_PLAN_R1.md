# DDTA R25 — Post-Holdout Independent Review Work Plan R1

Status: **ACTIVE**

Checkpoint: `DDTA-R25-DERMATRIAGE-INDEPENDENT-REVIEW-GOVERNANCE-R12`
Purpose: `EXPERT_EVIDENCE_GOVERNANCE_AND_PROTOCOL_DEVIATION_CHECKPOINT`
Repository baseline before this additive checkpoint: `36a1e1897302a77d3ecef5866e011f7082d0b597`
Predecessor plan: `DDTA_R25_BASE_ANALYSIS_WORK_PLAN_AFTER_DERMATRIAGE_PROMOTION_R1`

## 1. Current phase

`INDEPENDENT_REVIEW_EVIDENCE_RECONCILIATION`

The DermaTriage holdout first-pass consolidation has completed through R11. Before post-holdout method changes are admitted, the independent expert evidence must be preserved, classified for admissibility, and compared against the internal holdout analysis.

This plan is additive. It does not rewrite, supersede, or reinterpret predecessor checkpoints.

## 2. Frozen method boundary

During this phase the accepted BA method remains frozen. The following are blocked until the independent-review evidence gate is completed:

- BA0–BA6 method changes;
- promotion, merging, renaming, or retirement of method pressures;
- retrospective classification-coverage corrections to the accepted DermaTriage BA;
- reconciliation changes that alter accepted BA meaning;
- integrated DermaTriage BA6 verdict;
- deterministic projection verdict;
- claims of strict independent reproducibility against BA2 R3 based only on the protocol-deviated reviews.

No construct is to be added, removed, or redefined merely to fit expert output.

## 3. Independent-review evidence currently available

Two independent expert reports have been completed. They are preserved under:

```text
validation-evidence/dermatriage/independent-review-r1/
```

Both are retained as evidence even though the review package contains a protocol deviation: the documentation-authoring BA guide R5 was supplied where the frozen Base Analysis Operational Guide R3 was intended for strict BA execution replication.

The reports therefore remain admissible for bounded questions such as semantic recovery, documentation-gap discovery, analyst variance, non-inference behavior, and guide/package usability. They are not, by themselves, strict evidence of BA2 R3 operator coverage, construct sufficiency, or R3 reproducibility.

## 4. Required work sequence

```text
EXPERT EVIDENCE PRESERVATION
        ↓
PROTOCOL DEVIATION CLASSIFICATION
        ↓
THREE-WAY CROSS-REVIEW
        ↓
CORRECTED-R3-REPLICATION DECISION
        ↓
POST-HOLDOUT PRESSURE REVIEW
        ↓
CLASSIFICATION COVERAGE AUDIT
        ↓
RECONCILIATION
        ↓
EFFECTIVE BA REBUILD
        ↓
INTEGRATED DERMATRIAGE BA6
        ↓
PROJECTION TEST
```

## 5. Work items

### W1 — Preserve evidence

- preserve each original expert report byte-for-byte;
- record report SHA-256 and byte size;
- record the names and evidence-copy hashes of the methodological/source inputs currently available;
- do not modify expert wording to align it with the internal BA.

### W2 — Register protocol deviation

Record:

```text
intended BA execution guide:
    DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3

actually supplied guide:
    DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5

status:
    PROTOCOL_DEVIATION
```

The deviation must remain visible in all subsequent claims based on this review set.

### W3 — Classify evidence admissibility

For every expert finding, distinguish whether it can support:

- independent semantic recovery evidence;
- documentation-gap convergence/divergence;
- analyst-decision variance;
- guide/package usability;
- rejected-inference convergence;
- method pressure hypothesis;
- strict frozen-R3 reproducibility.

The last category remains `NOT_ESTABLISHED_BY_THIS_REVIEW_SET` unless independently replicated with the intended R3 execution guide.

### W4 — Execute three-way comparison

Compare:

```text
INTERNAL DERMATRIAGE HOLDOUT
    vs
EXPERT-01
    vs
EXPERT-02
```

using the categories and dimensions defined in `COMPARISON_PLAN.md`.

No disagreement is automatically a method defect. No agreement is automatically method validation.

### W5 — Decide corrected R3 replication

Before making strict claims about independent R3 reproducibility, record an explicit decision on whether to execute a corrected independent replication using the intended package.

At least one corrected R3 replication is recommended before making strict reproducibility claims. A second corrected independent replication would provide stronger analyst-variance evidence but is not made a prerequisite by this work plan.

The corrected package should contain, at minimum:

1. `DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.pdf`;
2. `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.pdf`;
3. the independent-review protocol;
4. an exact input manifest including file role, SHA-256, and package version.

### W6 — Resume post-holdout method review

Only after the evidence gate closes may the post-holdout pressure review, classification audit, reconciliation, BA6, and projection tests resume.

## 6. Exit criteria for this phase

This phase can close only when:

- both original expert reports are preserved and checksummed;
- the guide-selection deviation is documented;
- admissibility boundaries are explicit;
- the three-way comparison is complete;
- protocol-dependent disagreements are marked `NOT_COMPARABLE_DUE_TO_PROTOCOL` where appropriate;
- a corrected-R3-replication decision is recorded;
- no BA0–BA6 change has been silently introduced during evidence review.

## 7. Research interpretation

The protocol deviation itself is evidence about DDTA validation governance. Authority discipline must apply not only to governed project documentation, but also to methodological artifacts supplied to independent reviewers. A validation result is interpretable only relative to the exact authority package used to produce it.
