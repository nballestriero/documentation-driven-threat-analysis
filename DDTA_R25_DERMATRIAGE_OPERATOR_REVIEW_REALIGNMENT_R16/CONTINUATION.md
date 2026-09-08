# Continuation from R16

## Required baseline

```text
c5845183dcc256140b9823a39a582a8830855911
```

R16 is an additive work-plan checkpoint applied on top of R15. After R16 is committed and pushed, the resulting commit becomes the next continuation baseline.

## Required reading order for the next review session

1. `DDTA_R25_DERMATRIAGE_OPERATOR_REVIEW_REALIGNMENT_R16/CONSOLIDATED_STATE.md`
2. `methodology/DDTA_R25_POST_HOLDOUT_OPERATOR_COMPLETE_REVIEW_WORK_PLAN_R2.md`
3. `validation-evidence/dermatriage/post-holdout-method-review-r1/OPERATOR_AND_PRESSURE_REVIEW_LEDGER_R2.yml`
4. `validation-evidence/dermatriage/post-holdout-method-review-r1/construct-reviews/CR-01_CLASSIFY.md`
5. `validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CR-02_DECISIONRULE_COMPARISON_CANDIDATE_R1.md`
6. `DDTA_R25_DERMATRIAGE_HOLDOUT_FINAL_CONSOLIDATION_R11/DDTA_R25_DERMATRIAGE_FINAL_PRESSURE_REGISTER_R11.md`
7. `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.md`
8. `governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`

The older R13 work plan remains historical evidence but is superseded **for execution order only** by R2 of the operator-complete review plan.

## Immediate next operation after R16

Start `OP-01 transfer` under the new operator audit protocol.

Do not skip directly to a pressure topic such as `consume`, pipeline composition, or persistence merely because the source contains that verb or concept. First audit the complete frozen BA2 vocabulary and record whether existing constructs already preserve the required meaning.

## Stop conditions

Do not create a new normative BA method revision until:

- all `OP-*` entries are closed;
- all `CL-*` entries are closed;
- all `PR-*` entries are closed or explicitly deferred with reason;
- cross-review contradictions are reconciled;
- G1–G8 are applied to every surviving method delta.

Do not construct the final DermaTriage BA until the integrated BA-method revision is available. Working BA fragments may be preserved only as reconstruction evidence.
