# DDTA R25 — Post-Holdout Complete BA Operator and Pressure Review Work Plan R2

## 1. Purpose

This work plan supersedes `DDTA_R25_POST_HOLDOUT_CONSTRUCT_BY_CONSTRUCT_METHOD_REVIEW_WORK_PLAN_R1.md` **for execution order only**. The R1 plan remains immutable historical evidence.

R2 exists because the earlier sequence mixed:

- frozen BA2 top-level operators;
- condition-language primitives;
- wider semantic pressure topics.

The new plan first exhausts the existing method, then reviews pressure evidence, and only then permits integrated method revision.

## 2. Scope and governance

### In scope

- construction/authoring of Base Analysis;
- BA2 R3 operator sufficiency and clarity;
- `decisionRule` condition language;
- carried DermaTriage holdout pressure evidence;
- human-readable BA authoring notation;
- reproducibility, traceability, projection and documentation-QA value.

### Out of scope during this cycle

- documentation-writing methodology changes;
- DermaTriage governed-documentation changes;
- downstream threat-method invention of project truth;
- normative BA0–BA5 mutation during an individual review.

Frozen method during review:

```text
BA0 R1
BA1 R1
BA2 R3
BA3 R1
BA4 R1
BA5 R1
```

## 3. Fundamental rule

```text
SOURCE MEANING
    -> TEST EXISTING BA CONSTRUCTS
    -> TEST COMPOSITION OF EXISTING CONSTRUCTS
    -> RECORD PRESERVED / LOST / DISTORTED MEANING
    -> ONLY THEN CONSIDER A METHOD DELTA
```

Never:

```text
source uses verb X -> add operator X
```

and never:

```text
DermaTriage needs X -> BA universally needs X
```

## 4. Review namespaces

### `OP-*` — frozen BA2 R3 top-level operators

```text
OP-01 transfer
OP-02 produce
OP-03 create
OP-04 observe
OP-05 transition
OP-06 correlate
OP-07 reference
OP-08 dependOn
OP-09 consumeService
OP-10 realize
OP-11 assignResponsibility
OP-12 constrain
OP-13 classify
OP-14 decisionRule
```

### `CL-*` — `decisionRule` condition language

```text
CL-01 comparison
CL-02 satisfies
CL-03 allOf
CL-04 anyOf
CL-05 not
```

### `PR-*` — carried empirical pressure topics

```text
PR-01 P-01 function/process/behavior identity binding
PR-02 P-02 pipeline composition/order
PR-03 P-03 interface/path/invocation association
PR-04 P-04 boundary/interaction association
PR-05 P-05 ordered comparison vocabulary
PR-06 P-06 scalar/property-addressing comparison
PR-07 P-07 structured data/information contract
PR-08 P-08 data artifact/store/persistence association
PR-09 acquisition/refresh action semantics
PR-10 conditional action trigger semantics
PR-11 data/evidence consumption semantics
PR-12 negative implication/non-sufficiency semantics
PR-13 bounded recency/collection selection semantics
PR-14 configuration applicability binding evidence
```

## 5. Phase 0 — consolidation and inherited evidence

Before new review work:

- preserve R11 holdout conclusions;
- preserve R12 independent-review protocol deviation and admissibility limits;
- preserve CR-01/R14 as complete;
- preserve CR-02 comparison findings as non-normative working evidence;
- preserve all R1→R11 pressure history;
- preserve all previous BA representations used during the holdout.

No review may rely on chat history as its only evidence store.

## 6. Phase 1 — complete top-level operator audit

Review `OP-01` through `OP-14` in order.

For each operator answer:

1. What is the frozen BA2 R3 definition and signature?
2. Which governed DermaTriage source elements could require this semantic relation/action?
3. Where was the operator used in the previous BA/holdout?
4. Which uses were clearly correct?
5. Which candidate uses were rejected, and why?
6. Was any source meaning awkwardly absorbed by a neighboring operator?
7. Does composition with other existing constructs preserve the meaning?
8. Is the operator redundant, underspecified, overloaded, or simply not tested?
9. What must be carried into the final BA reconstruction?
10. Is any documentation QA finding present, separate from method pressure?

Allowed review statuses include:

```text
COMPLETE_NO_CHANGE
COMPLETE_GUIDE_CLARIFICATION
COMPLETE_APPLICATION_CORRECTION
EXTENSION_CANDIDATE
NEW_CONSTRUCT_PRESSURE_RETAINED
NOT_TESTED
DEFERRED_WITH_REASON
```

`NOT_TESTED` does not mean useless or invalid.

### Inherited special cases

- `OP-13 classify` is already `COMPLETE_GUIDE_CLARIFICATION` via CR-01/R14 unless later evidence creates an explicit contradiction.
- `OP-14 decisionRule` inherits CR-02 evidence but remains open until the source-complete review is recorded under this plan.

## 7. Phase 2 — condition-language audit

Review `CL-01` through `CL-05` independently from top-level BA2 operators.

### Current non-normative candidate for CL-01

Human-readable comparison authoring:

```text
Referent.property = value
Referent.property != value
Referent.property < value
Referent.property <= value
Referent.property > value
Referent.property >= value
ReferentA.property >= ReferentB.property
```

Conceptual structure may remain `comparison(left, operator, right)`, but the operational guide should prefer readable infix notation if the integrated review accepts it.

Do not introduce semantic comparison operators such as `notWorseThan` when a governed ordered comparison can express the meaning. Do not infer metric orientation when the source does not govern it.

Review `satisfies`, `allOf`, `anyOf`, and `not` for sufficiency, scope, readability, and non-overlap with generic action-trigger semantics.

## 8. Phase 3 — pressure review after construct exhaustion

Only after all relevant `OP-*` and `CL-*` entries have been tested may a `PR-*` topic be evaluated for a method delta.

For each pressure test these possibilities in order:

```text
A. existing operator already sufficient
B. composition of existing constructs sufficient
C. application correction sufficient
D. guide clarification sufficient
E. extension of existing construct required
F. genuinely new construct/operator required
G. pressure rejected / project-specific / not generalized
H. evidence insufficient -> retain/defer
```

Examples of required distinctions:

```text
precedes != dependOn
consume data != automatically consumeService
persistedIn != automatically reference
conditional action trigger != decisionRule
negative non-sufficiency != ordinary constraint
endpoint membership != invocation
boundary crossing != ordinary transfer unless the boundary role is preserved
```

## 9. Review artifact minimum content

No `OP-*`, `CL-*`, or `PR-*` review is closed unless its artifact contains enough information to contribute to the final BA and method consolidation without chat history.

Mandatory sections:

1. exact governed source anchor;
2. short evidence-bearing excerpt;
3. governed semantic claim;
4. frozen construct/signature under test;
5. previous BA representation(s);
6. representation experiments;
7. preserved/lost/distorted information;
8. rejected alternatives and non-inferences;
9. all-occurrences coverage statement;
10. local verdict;
11. generalization and minimality analysis;
12. G1–G8 assessment for any candidate delta;
13. `FINAL_BA_TRACE` section;
14. documentation QA section kept separate;
15. open/deferred questions.

Use `methodology/DDTA_R25_BA_OPERATOR_PRESSURE_REVIEW_ARTIFACT_TEMPLATE_R1.md`.

## 10. Method-delta gates G1–G8

A candidate method change must satisfy:

- **G1 Source evidence** — directly grounded in governed source evidence.
- **G2 General formulation** — method-neutral, not DermaTriage-specific.
- **G3 Construct exhaustion** — existing constructs/compositions were genuinely tested.
- **G4 No false semantics** — candidate does not add project truth.
- **G5 Minimality** — smallest adequate change.
- **G6 Non-redundancy** — not a synonym for an existing construct.
- **G7 Backward compatibility** — impact on existing BA contracts and artifacts is assessed.
- **G8 Projection/feedback value** — preserves information useful for reproducible analysis, projection, QA, or change impact.

Failure of a gate does not authorize silent relaxation; record the failure and disposition.

## 11. Phase 4 — integrated Base Analysis method revision

Only after Phases 1–3 are complete:

- reconcile surviving candidate deltas;
- eliminate redundant overlapping candidates;
- rerun G1–G8 at integrated level;
- decide whether BA2 R4 or another numbered BA contract revision is warranted;
- update the Base Analysis construction methodology;
- update the Base Analysis operational/authoring guide;
- publish backward-compatibility and migration notes.

The documentation-authoring methodology remains unchanged by this phase.

## 12. Phase 5 — complete DermaTriage BA re-run and reconciliation

Reconstruct the case-study BA using the consolidated method and all prior evidence:

```text
governed source
+ previous BA / holdout
+ pressure registers
+ independent review evidence
+ operator reviews
+ condition-language reviews
+ pressure reviews
+ integrated BA method
```

The final BA must be complete, human-reviewable, deterministic, source-traceable, and independent of downstream threat-analysis methods.

Produce both human-readable and machine-readable representations.

## 13. Phase 6 — publication and thesis update

Publish at minimum:

1. new normative BA methodology;
2. updated BA operational/authoring guide;
3. complete DermaTriage BA;
4. before/after BA comparison;
5. consolidated documentation-QA findings;
6. thesis-update-ready evidence pack covering method evolution, validation results, strengths, limitations, and documentation-improvement feedback.

## 14. Final closure criterion

The post-holdout BA-method review is complete only when:

- every frozen BA2 R3 operator has an explicit disposition;
- every condition-language primitive has an explicit disposition;
- every carried pressure has an explicit disposition;
- accepted deltas have been integrated into one coherent BA-method revision;
- the complete DermaTriage BA has been rerun under that revision;
- human-readable and machine-readable outputs agree semantically;
- the thesis update can be grounded in stable repository artifacts rather than conversational memory.
