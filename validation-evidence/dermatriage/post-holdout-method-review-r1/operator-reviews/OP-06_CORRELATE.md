# DDTA R25 — OP-06 `correlate` Review

## Review identity

```text
review_id: OP-06
review_kind: OPERATOR
status: COMPLETE_GUIDE_CLARIFICATION
frozen_method: BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
baseline_commit: 9e5176e49845c9184814a17aee550c0afb02fce8
```

## 1. Construct under review

- name: `correlate`
- frozen definition: assert same-request/evaluation/operation/context identity matching required to
  bind items correctly.
- frozen signature:

```text
correlate
    correlatedItem     -> BAReferent [1..*]
    correlationContext -> BAReferent [1]
```

## 2. Governed source evidence

Semantic primary:
`governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`

- **DEC-12:** outputs of the four pipeline stages must remain correlated to the same case. Strong positive.
- **FR-19:** multi-source BioMistral inputs are combined for the same case. Strong positive.
- **FR-22:** B4 triage outcome remains associated with the same B4 consultation. Strong positive.
- **FR-01:** symptom information comes from fields associated with the same B4 consultation.
  Positive correlation semantics; final representation deferred to PR-07 interaction.
- **DEC-15 / FR-23:** review/outcome exchange preserves same consultation/case identity. Very strong positive.
- **FR-03:** review refers to original outcome. Boundary case routed to OP-07 `reference`.

## 3. Previous BA / holdout representation

The inherited ledger signal for OP-06 was `TESTED_POSITIVE_STRONG`. This review does not accept that
signal as proof; the operator was re-tested source-first against the complete governed semantic primary.

## 4. Representation experiments

### Delete `correlate` from DEC-12 / FR-19

Individual stage behaviors remain representable, but the same-case binding is lost. Deletion rejected.

### Replace FR-23 correlation with direct `reference`

A direct referential edge can preserve which outcome points to which other outcome, but it cannot by
itself preserve same consultation/case identity across the workflow. Replacement rejected.

### Force FR-03 into `correlate`

Using `OriginalDermaTriageOutcome` as `correlationContext` distorts the source: it is the referenced
object, not an independently governed common context. Route to `reference`.

## 5. Existing-construct exhaustion and semantic boundaries

```text
reference              = directional explicit reference, not context binding
dependOn               = prerequisite, not correlation
transfer                = conveyance, not same-context matching
produce                 = actor/result/input, not same-context matching
selection / membership = collection inclusion, not correlation
comparison/applicability = evaluation relation, not correlation
similarity              = similar case, not same case identity
```

## 6. All-occurrences coverage

The complete governed semantic primary was inspected across MR-01 through MR-04, DEC-01 through
DEC-18, all 26 active FRs listed by the current manifest, and superseded FR-11 only as historical
non-active context. No additional active occurrence forces a different `correlate` signature.

## 7. Construct-specific question pack

`validation-evidence/dermatriage/post-holdout-method-review-r1/question-packs/CORRELATE_QUESTION_PACK_R1.md`

The retained questions cover context grounding, narrowest context, cross-match violation,
`reference` boundary, fake-context rejection, single-item context binding and delete/merge-first.

## 8. Rejected alternatives / non-inferences

- API existence does not imply request/response correlation.
- Cosine similarity is not BA correlation.
- Collection membership is not automatically correlation.
- Shared project membership is not correlation.
- Applicable comparison reference is not a correlation context.
- FR-27 per-case correction/image pairing is not inferred from technical expectations.
- Referenced item is not promoted to context merely to encode a pairwise reference.
- Synthetic request/evaluation/session contexts are not invented when source-grounding is absent.

## 9. Local verdict

```text
COMPLETE_GUIDE_CLARIFICATION
empiricalStatus: TESTED_POSITIVE_STRONG
operatorCoreDisposition: KEEP_NO_CHANGE
wholeOperatorRedundancy: FALSIFIED
signatureDisposition: KEEP_NO_CHANGE
normativeBAMutation: NONE
```

## 10. Generalization and minimality

The finding is method-general: `reference` is a directional referential edge; `correlate` is
context-identity binding needed to prevent cross-match. The context may be a case, consultation,
exam, request, transaction, evaluation, operation, or another governed identity.

## 11. G1–G8 evaluation

Not applicable: R23 proposes no normative method delta.

## 12. FINAL_BA_TRACE

```text
DEC-12 / FR-19
    same DermatologicalCase -> correlate accepted operator evidence

FR-22
    same B4Consultation -> correlate accepted operator evidence

DEC-15 / FR-23
    same B4Consultation/case identity -> correlate accepted operator evidence

FR-03
    review refers to original outcome -> route OP-07 reference

FR-01
    same B4Consultation semantics -> positive; materialization deferred PR-07

FR-27
    per-case correction/image correlation -> INSUFFICIENT_EVIDENCE
```

## 13. Documentation QA

```text
FR-27 per-case correction/image binding: CLARITY_OPPORTUNITY
FR-01 structured field contract: existing governed gap / PR-07 interaction
```

No documentation gap is created merely because BA chooses not to infer a correlation.

## 14. Open/deferred questions and owning review

```text
FR-03 exact reference representation -> OP-07 reference
FR-01 structured information/correlate composition -> PR-07 + final BA reconciliation
FR-27 per-case pairing -> documentation QA / final source validation; do not infer now
```

## 15. Per-construct consolidation result

```text
OP-06 correlate
    COMPLETE
core: KEEP_NO_CHANGE
signature: KEEP_NO_CHANGE
whole-operator redundancy: FALSIFIED
method delta: NONE
next: OP-07 reference
```

## Closure check

Another analyst can reconstruct the finding from this artifact, the question pack, the boundary
finding, BA2 R3, and the governed semantic primary without conversation history.
