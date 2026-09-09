# OP-05 — `transition` Review

## Review identity

```text
review_id: OP-05
reviewStatus: EXTENSION_CANDIDATE
reviewClosure: COMPLETE
empiricalStatus: TESTED_POSITIVE_STRONG
frozen_method: BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
baseline_commit: 20dd07f1bf856e0a1bbf218c5e3fb9837456c93a
```

## 1. Construct under review

BA2 R3 defines `transition` as a governed state/lifecycle change of a subject.

Frozen operator-scoped contract:

```text
transition
  subject   -> BAReferent [1]
  toState   -> BAReferent [1]
  actor     -> BAReferent [0..1]
  fromState -> BAReferent [0..1]
```

Inherited R11 status was `NOT_TESTED_POSITIVE_IN_DERMATRIAGE`.

## 2. Governed source evidence

### FR-10 — revocation after adoption

Source anchor: `MR-04 / DEC-08 / FR-10`.

Evidence-bearing meaning:

```text
an adaptation is already adopted
material post-adoption degradation may occur
DermaTriage must support revocation
revocation restores a previous acceptable version/state
rollback automaticity is not governed
```

Governed semantic claim relevant to OP-05:

```text
same classification-adaptation identity
    undergoes post-adoption lifecycle revocation
```

This is the strongest positive case.

### FR-09 — qualification for adoption

Source anchor: `MR-04 / DEC-06 / FR-09`.

Evidence-bearing meaning:

```text
CandidateUrgencyClassificationAdaptation
    is comparatively evaluated
    and may be considered qualified for adoption
    only if all governed criteria are satisfied
```

The wider MR-04/FR-15 material explicitly distinguishes lifecycle results including
qualification, acceptance and progression.

Disposition: secondary transition candidate requiring separation from the decision/evaluation
result itself.

### FR-04 / FR-05 — activation negative controls

Source anchors: `MR-04 / DEC-04 / FR-04` and `FR-05`.

The source governs threshold-triggered activation of adaptation cycles. It does not govern
`INACTIVE -> ACTIVE` state vocabularies for those cycles.

Disposition: transition rejected; route conditional action trigger semantics to PR-10.

### FR-26 — prompt versioning / reset

Source anchor: `MR-04 / DEC-17 / FR-26`.

The source governs version management, persistence, update, reset and history. It does not govern
a sufficiently explicit `fromState -> toState` lifecycle transition for a prompt/version subject.

Disposition: `INSUFFICIENT_EVIDENCE` for transition; documentation clarity opportunity retained.

### FR-27 — model update negative control

Source anchor: `MR-04 / DEC-18 / FR-27`.

Fine-tuning updates model parameters/blocks. Parameter mutation is not by itself a governed
lifecycle transition.

Disposition: transition rejected.

### FR-03 / FR-12 — review lifecycle QA

Source anchor: `MR-03 / DEC-03 / FR-03 / FR-12`.

Confirmation/correction is governed as review disposition/classification. The documentation
already records `GAP-DERMA-REVIEW-LIFECYCLE-01` for overwrite/history/retention/finality.

Disposition: do not invent a clinical-review lifecycle transition.

### Documentation lifecycle negative control

Metadata such as `Lifecycle: current` and the historical `FR-11 superseded` status describe
source/document governance unless project-semantic lifecycle is independently governed.

Disposition: `NOT_A_PROJECT_TRANSITION`.

## 3. Previous BA / holdout representation

R11 recorded:

```text
transition: NOT_TESTED_POSITIVE_IN_DERMATRIAGE
```

R11 correctly rejected transition for prompt update/reset and model parameter update. R22 retains
those negative decisions but identifies FR-10 as previously unexhausted positive lifecycle evidence.

## 4. Representation experiments

### Experiment A — delete `transition` from FR-10

Candidate reconstruction using neighboring constructs:

```text
constrain / decisionRule
    -> can preserve when revocation is allowed/required

version selection / applicability
    -> can preserve which existing version becomes active

classify
    -> can label an adaptation or result
```

Meaning lost:

```text
the same adaptation identity underwent a governed lifecycle change
```

Result:

```text
TRANSITION_CORE_JUSTIFIED
```

### Experiment B — force `actor = subject`

Rejected.

General example:

```text
Administrator changes Account from ACTIVE to SUSPENDED
```

requires:

```text
actor   -> Administrator
subject -> Account
```

The operator must not be restricted to self-transition.

### Experiment C — remove `actor`

Rejected.

When the source governs who causes/performs a state change, that distinction is material and
method-neutral. FR-10 also demonstrates why the role must remain optional: the source governs
support for revocation but not the exact execution/authorization actor.

### Experiment D — force every state to be a BAReferent

Current frozen BA2 R3 contract does this at the transition role level.

BA2 R3's general proposition rule already allows a controlled typed local value when independent
identity is not required, while BA1 requires BAReferent identity when project meaning must be
independently reused.

For a simple governed state vocabulary such as:

```text
Order PENDING -> PAID
```

minting independent `PendingState` and `PaidState` BAReferents may add unnecessary identity.

For a state that is independently reused, constrained, correlated, compared or tracked across
propositions/baselines, BAReferent identity remains appropriate.

Result: candidate value-domain relaxation retained.

## 5. Existing-construct exhaustion and semantic boundaries

```text
transition != produce
transition != create
transition != classify
transition != decisionRule
transition != trigger
transition != property/parameter update
transition != persistence
transition != version selection/applicability
transition != documentation-governance lifecycle
```

`decisionRule` may coexist with `transition`: a rule can determine the condition/outcome while a
transition separately preserves the lifecycle change of the same subject.

## 6. All-occurrences coverage

Transition-oriented source exhaustion covered:

```text
MR-01 / MR-02 / MR-03 / MR-04
FR-03 / FR-04 / FR-05 / FR-09 / FR-10 / FR-12 / FR-13 / FR-14 / FR-15 / FR-26 / FR-27
source/document Lifecycle metadata
existing governed lifecycle/rollback/deployment/review gaps
```

No additional governed DermaTriage occurrence currently forces a different transition meaning.

## 7. Transition question pack outcome

`TRANSITION_QUESTION_PACK_R1` was useful for positive and negative discrimination.

Key retained questions:

```text
same subject identity before and after?
actual state/lifecycle meaning or generic mutation?
source-supported toState/fromState?
actor independently governed?
different version identity selected instead?
what lifecycle meaning is lost if transition is deleted?
```

The pack creates no project truth.

The separate General Discovery Pack introduced in R21 is **not executed in this cycle**; by project
decision it is deferred to a third complete analysis cycle after construct/method stabilization.

## 8. Rejected alternatives / non-inferences

Do not infer:

```text
activate cycle -> INACTIVE -> ACTIVE
update weights -> model lifecycle transition
prompt reset -> specific lifecycle transition
qualification -> automatic deployment
support revocation -> DermaTriage necessarily authorizes/performs revocation
VersionA restored instead of VersionB -> transition from VersionB identity to VersionA identity
current/superseded document status -> project transition
```

## 9. Local verdict

```text
reviewStatus: EXTENSION_CANDIDATE
reviewClosure: COMPLETE
transition core: KEEP_NO_CHANGE
empiricalStatus: TESTED_POSITIVE_STRONG
whole-operator redundancy: FALSIFIED
actor role: KEEP_NO_CHANGE
fromState optionality: KEEP_NO_CHANGE
toState required cardinality: KEEP_NO_CHANGE
candidate delta: CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
normative BA mutation: NONE
next review: OP-06 correlate
```

## 10. Generalization and minimality

The positive core finding is method-general: state/lifecycle change of the same semantic identity
is distinct from producing an output, classifying an item, evaluating a rule, mutating a property
or selecting a different existing version.

The actor/subject distinction is also method-general and must support all three cases:

```text
actor omitted
actor = subject
actor != subject
```

The candidate state-value relaxation is not DermaTriage-specific. It aligns transition with BA1's
independent-identity criterion and BA2's existing controlled-local-value principle while retaining
BAReferent state identity when materially required.

## 11. G1–G8 — CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION

Candidate:

```text
transition
  subject   -> BAReferent [1]
  toState   -> BAReferent | controlled typed local state value [1]
  actor     -> BAReferent [0..1]
  fromState -> BAReferent | controlled typed local state value [0..1]
```

- **G1 Source evidence — PASS.** FR-10 supplies governed adoption/revocation lifecycle meaning
  without independently requiring state-object identity.
- **G2 General formulation — PASS.** The rule applies to any governed state transition.
- **G3 Construct exhaustion — PASS.** Neighboring constructs and version-selection semantics were
  tested; none resolves unnecessary state identity while preserving transition meaning.
- **G4 No false semantics — PASS.** Local values remain source-grounded; promotion to BAReferent is
  required when independent identity is needed.
- **G5 Minimality — PASS.** No role or cardinality changes; only the state-term value domain widens.
- **G6 Non-redundancy — PASS.** This is not a synonym/new operator; it is a signature alignment.
- **G7 Backward compatibility — PASS_WITH_SCHEMA_UPDATE.** Existing BAReferent-valued transitions
  remain valid; validators/serializers would need to admit the additional local-value form.
- **G8 Projection/feedback value — PASS.** Avoids artificial referents while preserving explicit
  lifecycle meaning and deterministic projection.

Disposition:

```text
DEFERRED_PENDING_INTEGRATED_REVIEW
```

No individual-review BA2 mutation is authorized.

## 12. FINAL_BA_TRACE

### FR-10

Carry:

```text
referent:
    ClassificationAdaptation identity (final canonical identity to reconcile)

meaning:
    same adopted adaptation may undergo governed revocation lifecycle change

source:
    MR-04 / DEC-08 / FR-10

representation:
    transition core ACCEPTED
    exact state materialization DEFERRED pending integrated state-value decision
    actor OMIT unless independently governed
```

Keep separate:

```text
restoration/selection of a previous acceptable existing model version
    -> PR-14 / version-selection applicability review
```

### FR-09

Carry as application recheck:

```text
candidate adaptation qualification progression
    transition + decisionRule composition POSSIBLE
    do not duplicate qualification result and lifecycle state accidentally
```

### Explicit non-inferences

Do not carry transition propositions for FR-04, FR-05, FR-26, FR-27, FR-03/12 or document
lifecycle metadata without additional governed evidence.

## 13. Documentation QA

```text
GOVERNED_GAP:
    GAP-DERMA-REVIEW-LIFECYCLE-01 (FR-03 / FR-12)
    GAP-DERMA-DEPLOY-01 (FR-09 lifecycle/deployment)
    GAP-DERMA-ROLLBACK-BINDING-01 (DEC-08 / FR-10)

CLARITY_OPPORTUNITY:
    FR-26 prompt update/reset/version lifecycle semantics

NOT_APPLICABLE:
    document current/superseded metadata as project transition
```

Documentation QA does not create BA truth and does not mutate the documentation-authoring method.

## 14. Open/deferred questions and ownership

```text
CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
    -> Phase 4 integrated BA method revision

BAPROP-DERMA-FR09-TRANSITION
    -> Phase 5 final DermaTriage BA reconciliation after OP-14 / CL / integrated method

BAPROP-DERMA-FR10-TRANSITION-STATE-REPRESENTATION
    -> Phase 5 after integrated state-value decision

FR-10 active-version restoration
    -> PR-14 configuration applicability / version-selection review

General Discovery Pack full-document execution
    -> third complete analysis cycle, not current operator audit
```

## 15. Per-construct consolidation result

```text
OP-05 transition: COMPLETE
core: KEEP_NO_CHANGE
empirical: TESTED_POSITIVE_STRONG
candidate signature delta: RETAIN_DEFERRED
next: OP-06 correlate
```
