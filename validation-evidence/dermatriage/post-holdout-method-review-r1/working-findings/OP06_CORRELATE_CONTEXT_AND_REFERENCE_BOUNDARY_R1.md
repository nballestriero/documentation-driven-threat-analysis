# OP-06 Working Finding — Correlation Context and `reference` Boundary R1

## Status

`ACCEPTED_REVIEW_FINDING / NON-NORMATIVE`

## Problem

A weak distinction such as `reference = association without context` and `correlate = association
with context` would make the operators structurally overlapping and would invite `correlate` to
become a generic `relatedTo`.

## Retained distinction

```text
reference
    = explicit directional reference
      A -> B

correlate
    = identity binding under a governed context C
      required to prevent incorrect cross-matching
```

The two may coexist when both facts are governed.

## FR-03 boundary

FR-03 governs that `ClinicalReviewResult` is associated with the `OriginalDermaTriageOutcome` to
which the review refers.

Minimum representation candidate:

```text
reference
    referencer -> ClinicalReviewResult
    referenced -> OriginalDermaTriageOutcome
```

Do not use the original outcome itself as `correlationContext` merely to encode that pairwise
reference.

## FR-23 positive correlation

FR-23 separately governs preservation of the same consultation/case identity across B4 write-back
and retrieval. The exact final participating referents remain subject to final BA reconstruction.

## Narrowest governed context

When several shared identities exist, prefer the narrowest source-grounded identity needed to
prevent cross-match.

Generic example:

```text
Patient P
    |
  Exam E
   /  \
  D   D1
```

If D and D1 must remain tied to the same Exam E, `Exam E` is the preferred correlation context;
`Patient P` is too broad if the same patient may have multiple exams.

## Derived context

A context need not be named by the source as "correlation context", but it must be either directly
governed or necessarily derivable. A plausible transitive inference is not enough.

## Signature conclusion

DermaTriage does not justify changing BA2 R3:

```text
correlatedItem     [1..*]  KEEP
correlationContext [1]     KEEP
```

FR-22 is positive evidence that a one-item context binding can be meaningful. Making
`correlationContext` optional is rejected because it would weaken the operator boundary.
