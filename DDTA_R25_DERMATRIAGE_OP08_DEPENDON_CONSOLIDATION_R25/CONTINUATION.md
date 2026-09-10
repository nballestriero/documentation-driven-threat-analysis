# Continuation after R25

## Baseline discipline

R25 was prepared against:

`be4c142464db81677661a64890a6204798e0ecd0`

After applying, committing and pushing R25, use the resulting R25 commit SHA as the next exact baseline.

## OP-08 closure

```text
OP-08 dependOn
    COMPLETE
    local verdict: COMPLETE_GUIDE_CLARIFICATION
    empirical: TESTED_POSITIVE_STRONG
    core: KEEP_NO_CHANGE
    signature: KEEP_NO_CHANGE
    whole-operator redundancy: FALSIFIED
```

Core application rule:

```text
dependOn(A,B)
    only when B is a governed prerequisite for A

not merely:
    B precedes A
    A uses B as data
    A invokes B
    A is guarded by B
    A references B
```

## Completed operator reviews after R25

```text
OP-01 transfer                 COMPLETE
OP-02 produce                  COMPLETE
OP-03 create                   COMPLETE_DEFERRED_WITH_REASON / NOT_TESTED
OP-04 observe                  COMPLETE
OP-05 transition               COMPLETE / EXTENSION_CANDIDATE
OP-06 correlate                COMPLETE
OP-07 reference                COMPLETE
OP-08 dependOn                 COMPLETE
OP-13 classify                 COMPLETE
```

## Operators still requiring review

```text
OP-09 consumeService
OP-10 realize
OP-11 assignResponsibility
OP-12 constrain
OP-14 decisionRule
```

OP-14 retains prior candidate work but remains unclosed.

## Strong OP-08 evidence

```text
MR-04 -> MR-03
    explicit macro prerequisite

FR-16 image-based capability -> trained/selected classification baseline
    explicit operational prerequisite
    final prerequisite referent granularity remains open
```

## Reconciliation / adjacent-review carry-forward

```text
AR-OP08-01  FR-16 prerequisite referent granularity -> final BA reconciliation
AR-OP08-02  FR-03 reference vs prerequisite composition -> final BA reconstruction
AR-OP08-03  FR-10 rollback -> restorable previous version -> final BA reconciliation
AR-OP08-04  FR-05 / FR-07 evidence dependency -> PR-11 data/evidence consumption
AR-OP08-05  FR-22 / FR-23 B4 service dependency -> OP-09 consumeService
AR-OP08-06  technical/library/runtime dependencies -> OP-10 realize boundary
```

## Dependency graph hypothesis

Non-normative carry-forward:

```text
dependency projection
    asserted edges = accepted dependOn propositions
    derived edges  = reproducible implications of more-specific accepted propositions

edge provenance MUST remain distinguishable
```

Do not duplicate BA facts solely for visualization.

```text
dependency cycle != automatic runtime deadlock
```

## Existing deferred method-delta candidates

Unchanged:

```text
CMD-OP04-OBSERVE-RESULT-REMOVAL
CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
```

## Candidate additions / pressure carry-forward

Unchanged R24 register:

`validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_ADDITIONS_PRESSURE_CARRY_FORWARD_R1.md`

Particularly relevant after OP-08:

```text
PR-02 pipeline composition/order
    precedes != dependOn

PR-10 trigger semantics
    trigger != dependOn

PR-11 data/evidence consumption
    consumeData boundary with dependOn
```

## General Discovery Pack

Still deferred:

```text
GENERAL_BA_SEMANTIC_DISCOVERY_PACK_R1
    execution: DEFERRED_TO_THIRD_COMPLETE_ANALYSIS_CYCLE
```

## Next review

`OP-09 consumeService`

Important inherited boundary from OP-08:

```text
actual service consumption
    may imply a derived dependency

but:
    do not automatically duplicate consumeService + dependOn

and:
    consuming data from a system != automatically consuming the service itself
```
