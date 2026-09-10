# Candidate Additions / Pressure Carry-Forward R7

## Status

`NON-NORMATIVE / RETAINED FOR CONDITION-LANGUAGE + PR/CC DISPOSITION + PRE-REWRITE COMPLETENESS RECHECK`

R7 carries forward the complete R6 register and adds findings from OP-14 `decisionRule`.

No candidate in this file is admitted BA method.

## Existing pressure register retained

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

## Existing-operator audit milestone

```text
OP-01..OP-14 REVIEWED
EXISTING_OPERATOR_AUDIT COMPLETE_14_OF_14
```

This is an exhaustion milestone, not a completeness proof.

## OP-14 updates

### PR-05 — ordered comparison vocabulary

DermaTriage requires ordered forms such as:

```text
confidence > 0.85
accuracy degradation at most 5%
accuracy degradation > 5%
no-worse-than reference
```

```text
PR-05
    SOURCE_EVIDENCE_STRONG
    OP12_BOUNDARY_CONFIRMED
    OP14_PRESSURE_CONFIRMED
    ROUTE_TO_CL01
    NOT_ADMITTED
```

### PR-06 — scalar/property-addressing comparison

Typed scalar/property comparison remains required beyond categorical vocabulary.

```text
PR-06
    SOURCE_EVIDENCE_STRONG
    OP14_PRESSURE_CONFIRMED
    ROUTE_TO_CL01
    NOT_ADMITTED
```

### PR-10 — conditional action trigger

```text
reaches 10 -> activate prompt evolution
reaches 50 -> activate classifier adaptation
```

OP-14 exhaustion shows these are not automatically result-selection rules.

```text
PR-10
    SOURCE_EVIDENCE_STRONG
    SURVIVES_OP12
    SURVIVES_OP14
    AUTONOMOUS_ACTION_TRIGGER_MEANING_REMAINS
    NOT_ADMITTED
```

### PR-12 — negative non-sufficiency

`A MUST NOT by itself imply B` is not equivalent to `IF A THEN NOT B`.

```text
PR-12
    SOURCE_EVIDENCE_STRONG
    SURVIVES_OP12
    SURVIVES_OP14
    ROUTE_TO_CL03_CL04_CL05_AND_INTEGRATED_REVIEW
    NOT_ADMITTED
```

### PR-13 — bounded recency/collection selection

Top-5 similarity retrieval and recent-20 pertinent corrections retain ranking/recency/membership/selection meaning not captured by scalar constraint or simple decision rule.

```text
PR-13
    SOURCE_EVIDENCE_STRONG
    SURVIVES_OP12
    SURVIVES_OP14
    NOT_ADMITTED
```

### PR-14 — applicability binding

Rules, comparisons, triggers and restrictions can be scoped to path/phase/reference/operation/population.

```text
PR-14
    SOURCE_EVIDENCE_STRONG
    SURVIVES_OP12
    SURVIVES_OP14
    ROUTE_TO_CL_AUDIT_SF05_INTEGRATED_REVIEW
    NOT_ADMITTED
```

## Other retained pressures remain open

```text
PR-01 SOURCE_EVIDENCE_STRONG_PENDING_PRESSURE_REVIEW
PR-02 PENDING_SF06
PR-03 STRENGTHENED_PENDING_SF02_SF06
PR-04 PENDING_SF06
PR-07 PENDING
PR-08 PENDING_SF05
PR-09 PENDING_SF05
PR-11 SOURCE_EVIDENCE_STRENGTHENED_PENDING
```

None is closed merely because OP-14 completed the existing-operator audit.

## Candidate constructs

```text
CC-01 consumeData
    CHARACTERIZED
    SOURCE_EVIDENCE_STRONG
    NOT_ADMITTED

CC-02 provideService
    CHARACTERIZED
    REALIZE_EXHAUSTION_COMPLETE
    ASSIGN_RESPONSIBILITY_EXHAUSTION_COMPLETE
    AUTONOMOUS_MEANING_SURVIVES
    REMAINING_EXHAUSTION: PR-01, PR-03
    NOT_ADMITTED
```

## Deferred candidate method deltas

The following already-existing method deltas remain open for integrated review:

```text
CMD-OP04-OBSERVE-RESULT-REMOVAL
    DEFERRED_PENDING_INTEGRATED_REVIEW

CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
    DEFERRED_PENDING_INTEGRATED_REVIEW
```

## Ranked-selection observation

FR-20 best-checkpoint selection by validation Macro F1 exposes decision-like ranked/argmax semantics not demonstrated by the current local rule vocabulary.

This is retained as a completeness observation rather than immediately minting a new PR or operator. During the pre-rewrite re-check it must be tested against PR-13, CL-01/local rule extension and composition before any new construct is considered.

## Mandatory pre-rewrite completeness re-check

Before rewriting the BA guide or final DermaTriage BA, perform a source-complete reconciliation of the entire governed corpus against all operator, CL, PR, CC and CMD findings.

For every surviving semantic gap, force one disposition:

```text
ABSORBED_BY_EXISTING_OPERATOR
CONTROLLED_KIND_OR_VALUE
LOCAL_CONDITION_LANGUAGE_EXTENSION
COMPOSITION_OR_PROJECTION
APPLICATION_CORRECTION
METHOD_DELTA_TO_EXISTING_OPERATOR
NEW_TOP_LEVEL_OPERATOR_CANDIDATE
NOT_GOVERNED_OR_INSUFFICIENT_EVIDENCE
```

No final guide rewrite should begin while an observed gap has no explicit disposition.

## General Discovery

The General Discovery Pack remains deferred to the third complete analysis cycle. The mandatory pre-rewrite completeness re-check is a focused reconciliation/control pass and does not replace the later General Discovery execution.
