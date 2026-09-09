# DDTA R25 — OP-07 `reference` Consolidation R24

## Purpose

R24 closes the source-complete OP-07 review while preserving the frozen BA method.

The review substantially narrows the practical admission boundary of `reference`:

```text
reference is not "A is somehow related to B"
reference is not a fallback for unknown relations
reference is not a placeholder for a missing BA operator

reference preserves a governed directional target identity
when that target is not already reconstructible from other accepted BA facts.
```

R24 makes **no normative BA2 R3 mutation**.

## Immutable predecessor

`508c02c2da8ae97771cad46a0abc896f00b9be39`

## Frozen BA2 R3 contract

```text
reference
    referencer -> BAReferent [1]
    referenced -> BAReferent [1..*]
```

Frozen meaning:

```text
Assert an explicit reference from one project meaning to another
without by itself implying correlation, dependency or ownership.
```

## Main positive evidence — FR-03

FR-03 requires DermaTriage to register a clinical-review result and associate it with the
**original DermaTriage outcome to which the review refers**.

The target identity cannot be reconstructed safely from context correlation alone because the
governed source does not establish that each consultation/case has exactly one possible original
outcome.

Therefore:

```text
reference
    referencer -> ClinicalReviewResult
    referenced -> OriginalDermaTriageOutcome
```

preserves information not guaranteed by:

```text
correlate(review, consultation)
correlate(outcome, consultation)
```

The core delete test is:

```text
After removing reference,
can the exact target B of A be reconstructed uniquely
from every other accepted BA fact?

YES -> do not emit redundant reference
NO  -> reference may preserve irreducible target identity
```

## Why `correlate` does not absorb FR-03

`correlate` answers:

```text
under which governed context identity must A/B remain bound?
```

`reference` answers:

```text
which specific B is the governed semantic target of A?
```

Do not turn the referenced object into `correlationContext` merely to encode a pairwise reference.

## Revised evidence set

### Retained

- **FR-03** — strong target-identity evidence.

### Withdrawn as OP-07 positive evidence

- **FR-01** — case/consultation binding can be expressed by `correlate`; no independent
  `reference` proposition is needed to justify OP-07.
- **MR-01 generic aboutness** — not required as evidence for the operator and too close to
  context-binding semantics to justify a separate proposition without stronger need.

This makes the proof smaller but cleaner.

## Specific-operator-first rule

Before admitting `reference`, exhaust any source-supported more-specific relation.

Examples:

```text
dependsOn      -> do not weaken to reference
invokes        -> route to PR-03, not reference
persistedIn    -> route to PR-08, not reference
appliesTo      -> route to PR-14, not reference
selectedInto   -> route to PR-13, not reference
comparison     -> comparison/condition semantics, not reference
```

A clear source meaning that BA2 cannot yet express is a **methodology pressure**, not a reason to
hide the meaning behind `reference`.

## Generic fallback rejected

The review rejects:

```text
unknown relation A -> B
    -> provisional reference
```

because this would convert analysis uncertainty into project truth and would hide either:

- a documentation gap;
- a method-vocabulary pressure; or
- an unresolved representation question.

Preferred handling outside normative BA truth:

```text
RELATION_UNRESOLVED
RECHECK_REQUIRED
```

These are analysis/reconciliation states, not new BA semantic operators.

## Signature result

```text
referencer -> BAReferent [1]     KEEP
referenced -> BAReferent [1..*]  KEEP
```

DermaTriage directly tests the lower bound `referenced >= 1`.

The need for multiple `referenced` targets in one proposition is **not specifically tested by this
corpus**, which is not evidence for reducing the frozen cardinality.

## Candidate additions / pressure carry-forward

R24 also preserves the semantic additions that must be tested after the frozen operator/condition
audit. They remain **candidates**, not admitted operators.

See:

`validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_ADDITIONS_PRESSURE_CARRY_FORWARD_R1.md`

High-level carried topics include:

```text
function/process/behavior identity binding
pipeline membership and ordering
interface/path invocation
boundary interaction/crossing
structured information contracts
artifact/store persistence
acquisition and refresh
conditional action triggers
data/evidence consumption
negative implication/non-sufficiency
bounded recency / collection selection
configuration applicability
```

Possible vocabulary such as `performs`, `precedes`, `invokes`, `persistedIn`, `consumeData`,
`appliesTo`, etc. is **provisional naming only** until the owning PR review satisfies G1-G8.

## OP-07 result

```text
reviewStatus: COMPLETE_GUIDE_CLARIFICATION
reviewClosure: COMPLETE
empiricalStatus: TESTED_POSITIVE
operatorCoreDisposition: KEEP_NO_CHANGE
wholeOperatorRedundancy: FALSIFIED_BY_FR03_TARGET_IDENTITY
signatureDisposition: KEEP_NO_CHANGE
candidateMethodDelta: NONE
normative BA mutation: NONE
next review: OP-08 dependOn
```
