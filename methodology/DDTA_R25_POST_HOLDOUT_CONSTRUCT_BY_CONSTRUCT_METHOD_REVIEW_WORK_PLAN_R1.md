# DDTA R25 — Post-Holdout Construct-by-Construct Method Review Work Plan R1

Status: **ACTIVE**

Checkpoint: `DDTA-R25-DERMATRIAGE-CONSTRUCT-METHOD-REVIEW-PLAN-R13`
Purpose: `POST_HOLDOUT_CONSTRUCT_BY_CONSTRUCT_METHOD_REVIEW_PLAN`
Repository baseline before this additive checkpoint: `facd456ee256746a61a7f94c72a04b20886ca59e`
Predecessor plan: `DDTA_R25_POST_HOLDOUT_INDEPENDENT_REVIEW_WORK_PLAN_R1`

## 1. Decision and current phase

The DermaTriage first-pass holdout is complete through R11 and the independent-review evidence has been preserved and governed through R12.

The next phase is:

```text
POST_HOLDOUT_CONSTRUCT_BY_CONSTRUCT_METHOD_REVIEW
```

The corrected independent R3 replication is **DEFERRED**, not rejected. No strict independent R3 reproducibility claim is made from the two protocol-deviated expert reports.

The two expert reports remain bounded supporting evidence for semantic recovery, documentation gaps, analyst variance, non-inference behavior, and guide/package usability. Their observations are incorporated source-bounded into each construct review rather than treated as normative method authority.

The previously planned monolithic three-way comparison is replaced, for the present phase, by an **embedded three-way comparison inside each construct review**.

## 2. Frozen-method rule during review

The accepted pre-holdout BA contract remains the immutable reference while individual reviews are executed.

```text
BA0 R1
BA1 R1
BA2 R3
BA3 R1
BA4 R1
BA5 R1

review output
    -> evidence
    -> METHOD_DELTA_CANDIDATE if justified

review output
    -X-> immediate BA0–BA5 mutation
```

No operator, role, family, semantic-kind rule, comparison primitive, or other BA construct is changed during a single construct review.

Only after all scheduled reviews are complete may accepted candidate deltas be considered together for an integrated method revision.

This prevents an early change from altering the analytical baseline used to evaluate later constructs.

## 3. Core anti-overfitting principle

A method change must never be justified as:

```text
DermaTriage needs X
    -> add X to BA
```

The required reasoning order is:

```text
governed source meaning
    -> general semantic need
    -> all occurrences of that need
    -> existing BA representation attempts
    -> information preserved / lost / distorted
    -> composition test using existing constructs
    -> generalization and minimality test
    -> candidate method delta only if still necessary
```

Before a new construct or extension can be admitted as a candidate, the semantic need MUST be expressible without DermaTriage-specific names, technologies, file names, thresholds, actors, or domain labels.

A single source occurrence may be sufficient evidence of a real general need, but a single occurrence is never sufficient justification for corpus-specific method vocabulary.

## 4. Mandatory chat transparency rule

Every construct review is conducted interactively and visibly.

Before a verdict is discussed, the chat MUST show:

1. the governed documentation anchor;
2. the relevant documentation excerpt;
3. **highlighted words/clauses that create the evidence**;
4. the current frozen construct or capability being tested;
5. the current BA representation attempt;
6. the semantic relation between the source wording and the evidence claim.

The presentation pattern is:

```text
DOCUMENTATION
[source anchor]
"... source text with EVIDENCE-BEARING WORDS highlighted ..."

WHAT THE SOURCE GOVERNS
- source-supported semantic fact

CURRENT CONSTRUCT
- frozen BA2 R3 definition / role relevant to the case

EVIDENCE LINK
source wording
    -> governed semantic distinction
    -> construct succeeds / strains / fails / is not needed
```

No construct review may be closed on the basis of a hidden aggregate finding that the user has not seen source-bounded in chat.

The complete review artifact may summarize the evidence afterward, but the material evidence must first be visible in the conversation.

## 5. Unit of review

The review unit is a **general BA construct or semantic capability**, not a project document and not a single DermaTriage requirement.

For each review, all known source locations where the construct:

- was used;
- should plausibly have been used;
- was difficult to apply;
- produced a representation pressure;
- was rejected;
- or was proposed by an expert,

must be collected before the verdict.

The review may therefore span DEC, FR, SR, MR and prior corpus evidence.

## 6. Mandatory review questions

Each construct review answers, in order:

### A. Current construct / capability
What does the frozen BA contract currently provide?

### B. General semantic need
What project-semantic distinction are we trying to preserve, stated domain-neutrally?

### C. Complete evidence set
Where does that need occur in DermaTriage? Where applicable, what prior Facial Access evidence exists?

### D. Independent-review signal
Do Expert 01 or Expert 02 independently observe the same semantic difficulty, a conflicting interpretation, or no issue?

Their evidence remains bounded by the R12 protocol-deviation classification.

### E. Existing representation attempts
How did the accepted/provisional DermaTriage BA represent the source meaning?

### F. Preservation test
What information is preserved, lost, distorted, inferred without authority, or left unresolved?

### G. Composition test
Can existing constructs be composed without creating false project meaning?

### H. Gap classification
Is the issue source/documentation incompleteness, BA application error, guide clarity problem, representation limit, or merely analyst preference?

### I. Generalization test
Can the need be stated without DermaTriage vocabulary and plausibly recur across domains?

### J. Minimality / redundancy test
Would a proposed extension overlap an existing construct or be expressible through an existing combination?

### K. Backward-compatibility test
Would the candidate change alter accepted meaning in Facial Access or earlier BA artifacts?

### L. Projection-value test
Does the additional semantic distinction materially support deterministic/reproducible projections or source-localized feedback?

### M. Verdict
Exactly one primary verdict:

```text
NO_CHANGE
APPLICATION_CORRECTION
GUIDE_CLARIFICATION
EXISTING_CONSTRUCT_EXTENSION_CANDIDATE
NEW_CONSTRUCT_CANDIDATE
PRESSURE_RETAINED
REJECTED
```

A review may record secondary notes, but it must not silently convert a candidate into normative method.

## 7. Admission gate for a method delta

A candidate extension or new construct must satisfy ALL applicable gates:

```text
G1 SOURCE EVIDENCE
    At least one explicit governed meaning cannot be adequately preserved.

G2 GENERAL SEMANTIC FORMULATION
    The need can be stated without corpus-specific vocabulary.

G3 EXISTING-CONSTRUCT EXHAUSTION
    Existing operators/roles/modifiers/composition have been tried.

G4 NO FALSE SEMANTICS
    The workaround would otherwise add or distort project meaning.

G5 MINIMALITY
    The candidate adds only the smallest missing distinction.

G6 NON-REDUNDANCY
    The candidate does not duplicate another construct.

G7 BACKWARD COMPATIBILITY
    Existing accepted BA can remain semantically valid or migration impact is explicit.

G8 PROJECTION / FEEDBACK VALUE
    The distinction has a justified analytical consumer or improves authority-preserving feedback.
```

Failure of any mandatory gate prevents immediate method promotion.

## 8. Review order

The initial ledger is:

```text
CR-01  classify
CR-02  decisionRule + comparison condition language (P-05 / P-06)
CR-03  constrain
CR-04  persistence / store association (P-08)
CR-05  interface / path / invocation association (P-03)
CR-06  boundary / interaction association (P-04)
CR-07  structured data / information contract (P-07)
CR-08  conditional action trigger semantics
CR-09  data / evidence consumption semantics
CR-10  bounded recency / collection selection semantics
CR-11  acquisition / refresh action semantics
CR-12  negative implication / non-sufficiency semantics
CR-13  function / process / behavior identity binding (P-01)
CR-14  pipeline composition / order (P-02)
CR-15  configuration applicability binding evidence
```

The order after CR-03 may be changed if an earlier review proves that two topics share the same underlying general need. Such a change must be recorded in the ledger; topics may not disappear silently.

## 9. Why CR-01 is `classify`

`classify` is used as a calibration review because:

- it already exists in BA2 R3;
- DermaTriage produced strong positive classification evidence;
- the R11 classification review records the hypothesis that earlier extraction may have under-applied it;
- Expert 01 and Expert 02 differ materially on its usefulness/application;
- therefore the first review can test whether the real issue is method insufficiency, guide clarity, or application consistency without inventing a new construct.

The question is not simply whether `classify` should exist. The operational question is:

```text
Across every source-supported semantic kind in the corpus,
was classify needed, correctly bounded, and consistently applied?
```

## 10. Evidence preservation and expert comparison

For each construct review, evidence is recorded separately from conclusions.

Expert findings are labelled as:

```text
SUPPORTING_CONVERGENCE
SUPPORTING_DIVERGENCE
EXPERT_ONLY_SIGNAL
NOT_COMPARABLE_DUE_TO_PROTOCOL
NOT_RELEVANT_TO_THIS_CONSTRUCT
```

No expert statement can directly create or remove a BA construct.

## 11. Review artifacts

Derived construct-review artifacts live under:

```text
validation-evidence/
  dermatriage/
    post-holdout-method-review-r1/
```

They are validation evidence, not governed project authority and not normative BA methodology.

Each completed review receives:

```text
construct-reviews/
    CR-##_NAME.md
```

and updates:

```text
CONSTRUCT_REVIEW_LEDGER.yml
```

Only a later integrated consolidation may produce a candidate new BA contract revision.

## 12. Exit criteria

This phase is complete only when:

- every ledger item has a recorded verdict;
- every material verdict is traceable to source excerpts;
- all method-delta candidates pass the generalization and minimality gates;
- all expert evidence used downstream is bounded by its admissibility status;
- no BA0–BA5 artifact has been modified during individual reviews;
- candidate deltas have been compared for overlap and interaction;
- an explicit integrated method-revision decision is recorded.

## 13. Next operational step

```text
CR-01 CLASSIFY
```

The review begins source-first by collecting every DermaTriage location that provides evidence for a stable reusable semantic kind, then showing each material source excerpt and its evidence-bearing wording in chat before determining the verdict.
