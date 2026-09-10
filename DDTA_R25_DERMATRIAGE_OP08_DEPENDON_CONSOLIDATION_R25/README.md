# DDTA R25 — OP-08 `dependOn` Consolidation R25

## Purpose

R25 closes the source-complete review of OP-08 `dependOn` against the governed DermaTriage documentation while preserving the frozen BA method.

R25 makes **no normative BA0–BA5 mutation**.

## Immutable predecessor

`be4c142464db81677661a64890a6204798e0ecd0`

## Frozen BA2 R3 contract

```text
dependOn
    dependent    -> BAReferent [1]
    prerequisite -> BAReferent [1..*]
```

Frozen meaning:

```text
Assert that one project meaning requires another
meaning/result/capability/milestone as a prerequisite.
```

## Refined application discipline

```text
dependOn(A,B)

A requires B as a governed prerequisite.
```

Primary counterfactual test:

```text
If B were unavailable, absent, not completed or not established,
could A still satisfy the governed documentation?

YES -> ordinarily not dependOn
NO  -> candidate dependOn
```

This does not turn every input, guard, prior step, library use or service use into a `dependOn` proposition. More-specific semantics must be exhausted first.

## Strong positive evidence

### MR-04 -> MR-03

The governed documentation explicitly states `MR-04 dependsOn MR-03` and explains that the adaptation branch consumes the governed meaning of clinical review owned by MR-03 without creating co-ownership. This independently validates the operator core.

### FR-16 capability -> trained/selected baseline

The source states that the image-based capability of FR-16 depends on a trained and selected classification baseline before operational use. This proves that `prerequisite` may be a governed result/artifact/capability/milestone, not only another Requirement.

The exact final BAReferent remains a reconciliation question:

```text
TrainedClassificationBaseline?
BestBaselineCheckpoint?
OperationalEfficientNetBaseline?
```

No ungoverned identity is selected during OP-08.

## Boundary rules

```text
precedes != dependOn
source word "requires" != dependOn
trigger/guard != automatically dependOn
authentication credential != automatically dependOn
service use != automatically duplicate dependOn
input use != automatically duplicate dependOn
```

## More-specific relation first

Several DermaTriage cases contain true dependency semantics but do not necessarily need an additional `dependOn` proposition.

Examples:

```text
produce.input
consumeService
future consumeData semantics
```

When the dependency edge can be reproduced deterministically from a more-specific accepted proposition, do not duplicate `dependOn` merely to make a graph easier to draw.

## Derived-dependency cases

Candidate downstream dependency edges, without duplicate BA truth:

```text
FR-19 synthesis <- governed inputs
FR-18 historical retrieval <- ClinicalDescription
FR-01 symptom urgency <- symptom information
FR-02 P-scale <- urgency/confidence
FR-08 classifier target <- corrected P-scale priority
```

## Boundary rechecks

### FR-05 / FR-07

FR-05 consumes evidence qualified according to FR-07. The narrow prerequisite is likely the evidence/result, not the FR-07 Requirement identity itself. Final representation is deferred to PR-11 data/evidence consumption.

### FR-22 / FR-23

The B4-integrated branch materially uses B4, but B4 is explicitly a consumed external service/system. OP-09 `consumeService` must be exhausted before adding redundant dependency edges.

### Technical/library dependencies

A documented library/runtime may be a legitimate prerequisite when the source explicitly requires it. A technology choice is not automatically a dependency. CPU fallback falsifies an unconditional DermaTriage -> CUDA dependency. Realization/dependency boundaries are carried to OP-10.

## Supporting dependency candidates

```text
FR-03 ClinicalReviewResult -> OriginalDermaTriageOutcome
FR-10 RollbackCapability -> RestorablePreviousVersion
```

Both preserve plausible/strong prerequisite meaning, but final minimal BA composition/referent shape remains for reconciliation.

## Negative controls

```text
MR-02 -> MR-01
    no canonical macro dependency is governed

FR-21 direct workflow -> B4 workflow
    explicitly does not depend on B4 workflow

threshold -> adaptation cycle
    trigger semantics

credential -> protected operation
    authentication/authorization guard

candidate qualification -> reference/criteria
    comparison/applicability/condition semantics
```

## Branch scope

A dependency may apply only to one branch. Do not widen a B4-integrated dependency into a universal DermaTriage dependency when the direct `/analyze` path is explicitly decoupled from B4.

## Dependency graph projection hypothesis

R25 preserves a non-normative hypothesis:

```text
ASSERTED DEPENDENCIES
    accepted dependOn propositions

DERIVED DEPENDENCIES
    reproducible implications of more-specific accepted BA propositions
```

Potential uses:

```text
impact analysis
dependency traversal
prerequisite ordering
change propagation
critical-node analysis
cycle detection
```

Edge provenance (`ASSERTED` vs `DERIVED`) must remain distinguishable. No normative graph schema is admitted in R25.

## Cycles and deadlocks

```text
dependency cycle != runtime deadlock
```

A cycle may be reported as a dependency-cycle finding. A deadlock claim requires additional governed wait/block/resource/concurrency semantics.

## Transitivity

Given `A dependsOn B` and `B dependsOn C`, a graph may compute transitive reachability. Do not automatically materialize `A dependsOn C` as new project truth unless independently governed.

## Signature result

```text
dependent    -> BAReferent [1]    KEEP
prerequisite -> BAReferent [1..*] KEEP
```

## Local verdict

```text
reviewStatus: COMPLETE_GUIDE_CLARIFICATION
reviewClosure: COMPLETE
empiricalStatus: TESTED_POSITIVE_STRONG
operatorCoreDisposition: KEEP_NO_CHANGE
wholeOperatorRedundancy: FALSIFIED
signatureDisposition: KEEP_NO_CHANGE
candidateMethodDelta: NONE
normative BA mutation: NONE
next review: OP-09 consumeService
```
