# OP-07 Working Finding — Target Identity and `reference` Boundary R1

## Status

`ACCEPTED_REVIEW_FINDING / NON-NORMATIVE`

## Core finding

`reference` survives the DermaTriage delete test only after a stricter derivability check.

```text
reference(A,B)
```

is useful when all of the following hold:

1. A directional A->B target relation is source-grounded.
2. B cannot be reconstructed uniquely from the other accepted BA propositions.
3. No more-specific semantic relation already preserves the governed meaning.

## FR-03

FR-03 governs that the `ClinicalReviewResult` is associated with the specific
`OriginalDermaTriageOutcome` to which the review refers.

Correlation under a consultation/case does not prove that the target is uniquely recoverable because
the source does not establish a global one-original-outcome-per-consultation cardinality.

Therefore `reference` preserves:

```text
which exact OriginalDermaTriageOutcome is the target of this ClinicalReviewResult?
```

## Boundary with `correlate`

```text
correlate:
    under which contextual identity must the item(s) remain bound?

reference:
    which specific semantic target does A refer to?
```

A common context is not enough to recover a target unless governed cardinality makes the target
unique.

## Withdrawn candidate — FR-01

`AvailableSymptomInformation concerns DermatologicalCase` no longer serves as independent evidence
for OP-07 because a one-item `correlate` binding can preserve case/consultation identity.

This withdrawal strengthens rather than weakens the review by removing a potentially overlapping
use.

## No generic fallback

Do not use `reference` for:

```text
source meaning unknown
method operator missing
relation pending review
```

Preferred analysis/reconciliation state:

```text
RELATION_UNRESOLVED
RECHECK_REQUIRED
```

This is not a BA proposition and does not create project truth.

## Pressure routing examples

```text
invokes      -> PR-03
persistedIn  -> PR-08
appliesTo    -> PR-14
selectedInto -> PR-13
consumeData  -> PR-11
triggers     -> PR-10
```

Clear semantics plus missing vocabulary is method pressure, not `reference`.

## Signature conclusion

No DermaTriage evidence justifies a BA2 signature mutation:

```text
referencer [1]      KEEP
referenced [1..*]   KEEP
```

Plural referenced cardinality remains untested by this corpus rather than disproved.
