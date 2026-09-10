# OP-08 Working Finding — `dependOn` Boundaries R1

## Status

`ACCEPTED_REVIEW_FINDING / NON-NORMATIVE`

## Core finding

The frozen `dependOn` core is necessary, but admission must be narrower than generic "uses", "comes after" or "requires".

```text
dependOn(A,B)
    A requires B as a governed prerequisite.
```

Primary counterfactual:

```text
without B, can A still satisfy the source?
YES -> ordinarily reject dependOn
NO  -> candidate
```

## Strong evidence

`MR-04 -> MR-03` is directly governed and explicitly explained as dependency on clinical-review meaning.

`FR-16 -> trained/selected classification baseline` is directly governed as an operational prerequisite. Final prerequisite referent must use the narrowest independently identifiable governed meaning.

## `precedes` boundary

```text
B before A != A dependsOn B
```

Pure ordering routes to PR-02.

## `produce.input` boundary

When B is a governed input used to produce A, `produce` may already preserve the exact source truth. If dependency can be deterministically projected, duplicate `dependOn` solely for graph construction is redundant.

## `consumeService` boundary

A service-consumption proposition may later support a derived dependency edge. OP-09 must decide service-consumption semantics before OP-08 duplicates those edges.

## `consumeData` boundary

FR-05/FR-07 demonstrates a strong dependency chain through qualified evidence. The narrow prerequisite is likely the evidence/result rather than the producing Requirement itself. PR-11 owns unresolved data/evidence-consumption semantics.

## Trigger / authentication boundaries

```text
trigger != automatically dependOn
ProtectedOperation requires credential != automatically dependOn
SOURCE WORD REQUIRES IS NOT OPERATOR dependOn
```

## Branch scope

FR-21 explicitly provides a direct path that does not depend on the B4 workflow. Any B4 dependency must remain scoped to the B4-integrated branch.

## Technical/runtime dependency

A library/runtime can be a valid prerequisite if governed documentation explicitly requires it. Technology selected/used is not automatically `dependOn`. CPU fallback falsifies an unconditional CUDA prerequisite. OP-10 retains the realization boundary.

## Recovery prerequisite

FR-10 is a supporting candidate:

```text
RollbackCapability dependsOn RestorablePreviousVersion
```

because restore-based rollback cannot satisfy the source without a restorable previous version. Final referent shape remains open.

## Reference composition

FR-03 may preserve both:

```text
reference(review, originalOutcome)
    -> which outcome is targeted?

dependOn(review, originalOutcome)
    -> can this review exist as governed without an outcome to review?
```

Final minimal composition remains a reconciliation item.

## Transitivity and cycles

Do not materialize transitive closure automatically as source truth.

```text
dependency cycle = valid future graph finding
dependency cycle != automatic deadlock
```

Deadlock requires richer runtime semantics.
