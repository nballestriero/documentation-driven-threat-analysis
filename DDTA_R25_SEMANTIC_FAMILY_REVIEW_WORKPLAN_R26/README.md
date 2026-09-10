# DDTA R25 — Semantic-Family Review Work Plan R26

## Purpose

R26 changes **review execution strategy only**. It does not modify the frozen BA method or governed DermaTriage documentation.

Prepared against exact baseline:

`f40741a64e0a9494702572b50c8ce1fe6a583e0c`

## Why R3 is needed

OP-01..OP-08 showed that semantic sufficiency often depends on composition across neighboring constructs. The clearest current example is the flow/service family:

```text
produce data
consume data ?
transfer data
observe data
store/queue data ?
consume service
provide service ?
invoke endpoint ?
depend on service/data ?
```

Reviewing these only as isolated words risks either duplication or hiding genuine gaps.

## What R26 introduces

- `DDTA_R25_POST_HOLDOUT_OPERATOR_COMPLETE_REVIEW_WORK_PLAN_R3.md`;
- semantic-family execution map `SF-01..SF-06`;
- a generic Candidate Construct Question-Pack template;
- an SF-01 Flow/Consumption/Service question pack;
- carry-forward R2 with `consumeData?` and newly characterized `provideService?`;
- ledger R12 pointing OP-09 into SF-01.

## What R26 does not do

```text
NO BA2 R4
NO new operator admission
NO consumeData admission
NO provideService admission
NO documentation-authoring method mutation
NO General Discovery execution
```

## Immediate next work

```text
SF-01 Flow / Consumption / Service
    -> OP-09 consumeService source-complete review
    -> characterize PR-11 consumeData
    -> test provideService candidate
    -> test endpoint/store/queue boundaries where the governed source permits
```

If DermaTriage cannot test a candidate, it remains `CANDIDATE_NOT_TESTED` with its question pack for a future corpus.
