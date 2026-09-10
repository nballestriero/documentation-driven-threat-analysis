# Candidate Additions / Pressure Carry-Forward R8

## Status

`NON-NORMATIVE / RETAINED FOR CONCEPTUAL PR/CC DISPOSITION + CONDITION-LANGUAGE REVIEW + PRE-REWRITE COMPLETENESS RECHECK`

R8 supersedes R7 as active carry-forward register. R7 remains historical evidence.

No item in this file is admitted BA method.

## Existing operator milestone

```text
OP-01..OP-14 REVIEWED
EXISTING_OPERATOR_AUDIT COMPLETE_14_OF_14
TOP_LEVEL_OPERATOR_COUNT 14
NEW_TOP_LEVEL_OPERATOR_ADMITTED NONE
```

## Pressure register

```text
PR-01 function/process/behavior identity binding
PR-02 pipeline composition/order
PR-03 interface/path/invocation association
PR-04 boundary/interaction association
PR-05 ordered comparison vocabulary
PR-06 scalar/property-addressing comparison
PR-07 structured data/information contract
PR-08 artifact/store/persistence
PR-09 acquisition/refresh
PR-10 conditional trigger
PR-11 data/evidence consumption
PR-12 negative non-sufficiency
PR-13 bounded recency/collection selection
PR-14 applicability binding

CC-01 consumeData
CC-02 provideService
```

Do not mint PR-15 for operation-target/effect-scope. Retain `OBS-OT-01` until ownership and level are clear.

## First-group reconciliation

### PR-01

```text
PR-01
    SOURCE_RELEVANCE_PRESENT
    PERFORM_WORKING_HYPOTHESIS_TESTED
    IRREDUCIBILITY_NOT_DEMONSTRATED
    RETAIN_PRESSURE
    DO_NOT_ADMIT
```

Output-producing behavior may collapse to `produce`. Retraining does not automatically prove performer semantics after inputs, configuration and operation scope are represented.

### CC-01 consumeData

```text
CC-01
    NON_DESTRUCTIVE_USE_ABSORBABLE
    DESTRUCTIVE_CONSUMPTION_NOT_GOVERNED
    GENERIC_CONSUME_NOT_JUSTIFIED
    CANDIDATE_REJECTED_REDUNDANT
```

`observe` is appropriate only for independently governed read/query/inspection semantics.

### CC-02 provideService

```text
CC-02
    SEMANTIC_DISTINCTION_RETAINED
    CLEAN_AUTONOMOUS_POSITIVE_CONTROL_INSUFFICIENT
    CANDIDATE_INSUFFICIENT_EVIDENCE
    RETAIN_FOR_OTHER_CORPUS_AND_COMPLETENESS_RECHECK
```

Data provision and endpoint exposure do not automatically imply service provision.

## Rejected temporary hypothesis: modify

```text
operation execution != actual value change
x_after = f(x_before) != x_after != x_before
```

Therefore a generic `modify` operator is not justified.

## New non-normative observation

```text
OBS-OT-01 OPERATION_TARGET_EFFECT_SCOPE
    SOURCE_PRESSURE_VISIBLE_IN_FR27
    LEVEL_UNRESOLVED
    NO_PR_ALLOCATED
    NO_CC_ALLOCATED
    NO_OPERATOR_ADMITTED
```

Test against existing composition and local structures first.

## Model/version observation

```text
MODEL_VERSION_CONCEPT SOURCE_SUPPORTED
REFERENCE_VERSION_1_0_0 SOURCE_SUPPORTED
RECOVERABLE_VERSION_PLURALITY SOURCE_SUPPORTED
ACTIVE_MODEL_DISTINCTION SOURCE_SUPPORTED
NEW_VERSION_PER_RETRAINING NOT_GOVERNED
EXACT_ROLLBACK_TARGET NOT_SUFFICIENTLY_GOVERNED
```

## Condition-language pressures retained

```text
PR-05 SOURCE_EVIDENCE_STRONG ROUTE_TO_CL01
PR-06 SOURCE_EVIDENCE_STRONG ROUTE_TO_CL01
PR-10 SOURCE_EVIDENCE_STRONG NEXT_CONCEPTUAL_GROUP
PR-12 SOURCE_EVIDENCE_STRONG SURVIVES_OP12_OP14
PR-13 SOURCE_EVIDENCE_STRONG NEXT_CONCEPTUAL_GROUP
PR-14 SOURCE_EVIDENCE_STRONG SURVIVES_OP12_OP14
```

## Other pressures

```text
PR-02 PENDING_LATER_STRUCTURAL_GROUP
PR-03 NEXT_CONCEPTUAL_GROUP
PR-04 PENDING_LATER_STRUCTURAL_GROUP
PR-07 PENDING_LATER_STRUCTURAL_GROUP
PR-08 NEXT_CONCEPTUAL_GROUP
PR-09 PENDING_LATER_STATE_ACQUISITION_GROUP
PR-11 RECONCILED_VIA_CC01_REJECTION
```

PR-11 remains as regression evidence that lexical `consume` does not necessarily require a consumption operator.

## Candidate method deltas

```text
CMD-OP04-OBSERVE-RESULT-REMOVAL
    DEFERRED_PENDING_INTEGRATED_REVIEW

CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
    DEFERRED_PENDING_INTEGRATED_REVIEW
```

## Next conceptual group

```text
PR-08 persistence / storedIn
PR-03 invoke / expose
PR-10 conditional action trigger
PR-13 selection / ranking / bounded selection
```

Review together for corpus efficiency; present findings separately by construct.

## Mandatory later gate

Before guide or final BA rewrite, reconcile the complete governed corpus against all operator, CL, PR, CC, observation and deferred-delta findings and force an explicit disposition for every surviving semantic gap.

General Discovery remains deferred to the third complete analysis cycle.
