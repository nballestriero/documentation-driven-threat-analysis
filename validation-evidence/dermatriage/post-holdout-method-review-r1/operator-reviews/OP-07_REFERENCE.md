# DDTA R25 — OP-07 `reference` Review

## Review identity

```text
review_id: OP-07
review_kind: OPERATOR
status: COMPLETE_GUIDE_CLARIFICATION
frozen_method: BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
baseline_commit: 508c02c2da8ae97771cad46a0abc896f00b9be39
```

## 1. Construct under review

Frozen BA2 R3:

```text
reference
    referencer -> BAReferent [1]
    referenced -> BAReferent [1..*]
```

Meaning:

```text
Assert an explicit reference from one project meaning to another
without by itself implying correlation, dependency or ownership.
```

## 2. Governed source coverage

Semantic primary:

`governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`

The complete current governed baseline was reviewed across:

- MR-01 through MR-04;
- DEC-01 through DEC-18;
- all 26 active FRs in the manifest;
- FR-11 only as superseded historical context.

## 3. Main positive evidence — FR-03

FR-03 requires DermaTriage to record a clinical-review result by associating it with the original
DermaTriage outcome **to which the review refers**.

Source-supported relation:

```text
ClinicalReviewResult -> OriginalDermaTriageOutcome
```

DEC-03 additionally requires the original outcome and the review result to remain distinguishable.

### Target-identity test

The B4 workflow also preserves consultation/case identity, but the source does not establish that a
consultation has exactly one possible original DermaTriage outcome.

Therefore:

```text
correlate(ClinicalReviewResult, B4Consultation)
correlate(OriginalDermaTriageOutcome, B4Consultation)
```

does not guarantee that the exact review target is uniquely reconstructible.

`reference` preserves which exact original outcome is the target of the review.

Disposition:

```text
FR-03
    STRONG_POSITIVE_REFERENCE
```

## 4. Withdrawn candidate — FR-01

Earlier review exploration considered:

```text
AvailableSymptomInformation -> DermatologicalCase
```

as supporting reference evidence.

After OP-06 established that one-item context binding is valid for `correlate`, FR-01 no longer
provides independent evidence for OP-07.

Disposition:

```text
FR-01
    WITHDRAWN_AS_REFERENCE_EVIDENCE
    route: correlate / PR-07 interaction
```

## 5. Representation experiments

### Experiment A — correlate only

```text
Review R -> Consultation C
Outcome O -> Consultation C
```

Preserves same-context binding.

Does not preserve target identity when multiple O values remain source-compatible.

Verdict: insufficient replacement for FR-03.

### Experiment B — make O the correlation context

```text
correlate
    correlatedItem     -> Review R
    correlationContext -> Outcome O
```

Distorts roles: O is the referenced target, not a common context identity.

Verdict: reject.

### Experiment C — generic provisional reference

```text
unknown A -> B
reference(A,B)
status = provisional
```

Converts uncertainty into project truth and may hide documentation gaps or method pressure.

Verdict: reject.

### Experiment D — known missing semantic operator

Examples:

```text
POST /analyze invokes TriageProcess
PromptManager persists PromptVersion in store
PromptVersion applies to a model
```

Source semantics are clear; the problem is vocabulary coverage.

Verdict: route to PR-03 / PR-08 / PR-14, not `reference`.

## 6. Construct boundaries

```text
correlate:
    contextual identity binding

reference:
    directional target identity

dependOn:
    prerequisite

realize:
    abstract-to-concrete materialization

persistedIn:
    PR-08 pressure, not reference

appliesTo:
    PR-14 pressure, not reference

invokes:
    PR-03 pressure, not reference
```

## 7. Target-identity necessity test

Before admitting `reference(A,B)`:

```text
Can B be uniquely reconstructed from A
using all other accepted BA facts and governed cardinalities?
```

```text
YES -> do not emit redundant reference
NO  -> if A->B is explicitly source-grounded and no more-specific relation applies,
       reference preserves irreducible target identity
```

This is a guide/question-pack clarification, not a BA2 signature mutation.

## 8. Fallback handling

Rejected:

```text
reference as generic fallback
PROVISIONAL_REFERENCE as unresolved relationship placeholder
```

Preferred non-BA analysis state:

```text
RELATION_UNRESOLVED
RECHECK_REQUIRED
```

Routing:

```text
source incomplete
    -> documentation gap / unresolved source binding

source clear, BA cannot preserve semantics
    -> methodology pressure
```

## 9. Signature review

```text
referencer [1]
    KEEP

referenced [1..*]
    KEEP lower bound

referenced > 1
    NOT_TESTED_BY_DERMATRIAGE
```

Absence of a plural positive case in this corpus is not evidence for signature reduction.

## 10. Previous BA / holdout relation

The inherited ledger marked OP-07 as not previously tested positive in DermaTriage.

This review independently establishes a positive case from FR-03 rather than relying on inherited
representation.

The OP-06 reconciliation item for FR-03 can now be closed conceptually as:

```text
FR-03:
    correlation context and referential target are separate semantics
    target-identity relation routes to reference
```

Final BA materialization remains part of the final reconciliation cycle.

## 11. Rejected alternatives / non-inferences

- Source noun `reference` does not imply BA operator `reference`.
- Comparison against a reference version is comparison/applicability.
- Shared context does not automatically require a separate reference proposition.
- A referenced object must not be promoted to `correlationContext` merely to avoid `reference`.
- Unknown relation semantics do not authorize provisional `reference`.
- Clear but unsupported BA semantics must be carried as method pressure, not weakened to reference.
- Missing target cardinality must not be invented to make reference derivable.

## 12. Local verdict

```text
COMPLETE_GUIDE_CLARIFICATION
```

with:

```text
empiricalStatus: TESTED_POSITIVE
operatorCoreDisposition: KEEP_NO_CHANGE
wholeOperatorRedundancy: FALSIFIED_BY_FR03_TARGET_IDENTITY
signatureDisposition: KEEP_NO_CHANGE
candidateMethodDelta: NONE
normativeBAMutation: NONE
```

## 13. Generalization and minimality

General rule:

```text
reference preserves target identity only when:
    the target is source-grounded
    AND not uniquely reconstructible from other BA facts
    AND no more-specific semantic relation is adequate
```

This rule is method-neutral and not specific to clinical review.

## 14. G1–G8

Not applicable to a normative method delta: no BA2 mutation is proposed.

The guide/question-pack clarification is evidence-backed and does not change the frozen operator
contract.

## 15. FINAL_BA_TRACE

### FR-03

```text
meaning:
    ClinicalReviewResult targets the specific OriginalDermaTriageOutcome
    to which the review refers

representation:
    reference candidate / accepted OP-07 evidence
```

### FR-01

```text
meaning:
    symptom information belongs to the governed case/consultation context

reference:
    withdrawn

routing:
    correlate + PR-07 final materialization
```

### FR-21 / FR-26

```text
clear relation semantics:
    invocation / persistence / applicability

routing:
    pressure review
    NOT reference
```

## 16. Documentation QA

No new documentation gap is created merely by the OP-07 result.

Where target cardinality is absent, BA must not invent it. The absence becomes material only when a
downstream representation requires an ungoverned uniqueness assumption.

## 17. Candidate additions carried forward

R24 adds a non-normative pressure carry-forward artifact so previously identified possible additions
are not lost:

`validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_ADDITIONS_PRESSURE_CARRY_FORWARD_R1.md`

This does not admit any new operator.

## 18. Closure

```text
OP-07 reference
    COMPLETE

next:
    OP-08 dependOn
```
