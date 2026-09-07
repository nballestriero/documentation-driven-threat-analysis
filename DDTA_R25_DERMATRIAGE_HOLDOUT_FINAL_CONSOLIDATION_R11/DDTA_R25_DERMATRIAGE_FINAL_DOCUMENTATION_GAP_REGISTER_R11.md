# DermaTriage Final Documentation Gap Register — R11

## Source-governed open gaps

```text
Diagnostic authority boundary
GAP-DERMA-NOIMAGE-INPUT-01
GAP-DERMA-PMAP-INPUT-01
GAP-DERMA-NOIMAGE-PMAP-BINDING-01
GAP-DERMA-SLA-01
GAP-DERMA-PATH-01
Specialist selection semantics
GAP-DERMA-REVIEW-CONTENT-01
GAP-DERMA-REVIEW-LIFECYCLE-01
GAP-DERMA-REVIEW-DISAGREEMENT-BINDING-01
GAP-DERMA-ADAPT-COUNTING-01
GAP-DERMA-ADAPT-THRESHOLD-AUTH-01
GAP-DERMA-PROMPT-WINDOW-01
GAP-DERMA-SUPERVISION-INPUT-01
GAP-DERMA-DEPLOY-01
GAP-DERMA-ACCEPT-BINDING-01
GAP-DERMA-ROLLBACK-BINDING-01
GAP-DERMA-EVAL-CONSISTENCY-01
```

## Final holdout principles

```text
intentional decomposition stop
    != gap

out of scope
    != gap

not governed
    != negative truth

methodology representation failure
    != documentation gap

numeric literal
    != complete governed rule
```

## Final-source materiality updates

```text
GAP-DERMA-REVIEW-DISAGREEMENT-BINDING-01:
    FR-07 clarifies ClinicianDisagreement and current agrees==False encoding,
    but full correction/disagreement/state binding remains open.

GAP-DERMA-SUPERVISION-INPUT-01:
    FR-08 gives complete P1-P4 valid-domain mapping,
    but invalid/missing/conflicting input behavior remains open.

GAP-DERMA-PROMPT-WINDOW-01:
    remains open for tie/ordering/dedup/underfill/reuse semantics.

GAP-DERMA-ROLLBACK-BINDING-01:
    remains open for authorization/automaticity/timing/exact target.

GAP-DERMA-DEPLOY-01:
    remains open; qualification/adoption evidence does not assign final deployment authority.
```
