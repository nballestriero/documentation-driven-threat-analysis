# Three-way independent review comparison plan

Status: **READY / NOT YET EXECUTED**

## 1. Comparison set

```text
INTERNAL DERMATRIAGE HOLDOUT
    vs
EXPERT-01
    vs
EXPERT-02
```

The internal holdout remains the accepted working analysis at its governed checkpoint. Expert reports remain independent evidence; they are not rewritten into the internal representation before comparison.

## 2. Comparison labels

Each source-bounded claim or analysis decision should receive one of:

- `3/3_CONVERGENCE` — all three analyses materially agree;
- `2/3_CONVERGENCE` — two materially agree and the third differs or omits;
- `OURS_ONLY` — only the internal holdout makes the claim;
- `EXPERT_ONLY` — one or both experts make a claim absent internally;
- `DIRECT_DISAGREEMENT` — analyses make incompatible positive claims;
- `NOT_COMPARABLE_DUE_TO_PROTOCOL` — meaningful comparison would require the frozen R3 execution contract that was not supplied.

Absence is not automatically disagreement. Different granularity is not automatically semantic conflict.

## 3. Comparison dimensions

At minimum compare:

1. BAReferent identity boundaries;
2. BAProposition meaning;
3. operator choice where comparable;
4. `classify` usage and semantic-kind decisions;
5. conditional/decision-rule interpretation;
6. rejected inferences and non-admitted semantics;
7. documentation gaps;
8. methodology-pressure hypotheses;
9. construct usefulness/difficulty;
10. guide usability under the package actually supplied;
11. projection readiness claims;
12. analyst confidence/reproducibility observations.

## 4. Source-bounded procedure

For every comparable bounded source element:

1. quote or identify the governed source anchor;
2. record the internal holdout result without changing it;
3. record Expert 01's result without normalization;
4. record Expert 02's result without normalization;
5. identify whether terminology differs but meaning converges;
6. classify convergence/disagreement;
7. identify whether the difference is likely source ambiguity, analyst variance, guide/package effect, method representational limit, or non-comparability;
8. defer all method changes to the later post-holdout review.

## 5. Protocol-aware questions

For every operator-level disagreement ask:

```text
Would this disagreement still be meaningful if both experts had received
DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3?
```

If the answer cannot be established from the evidence, use `NOT_COMPARABLE_DUE_TO_PROTOCOL` rather than attributing the divergence to BA itself.

## 6. Outputs of the future cross-review

The comparison should eventually produce a separate derived artifact containing:

- source-by-source matrix;
- convergence summary;
- disagreement register;
- protocol-dependent/non-comparable register;
- documentation-gap convergence register;
- candidate method-pressure evidence register;
- corrected-R3-replication recommendation.

That future artifact must not overwrite either original report.

## 7. Exit gate

The comparison phase is complete only when every material expert claim used downstream is traceable to its original report and is marked with an admissibility/comparability status.
