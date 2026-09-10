# DDTA R25 — Post-Operator-Audit Disposition and Completeness Work Plan R4

## 1. Status and lineage

`ACTIVE EXECUTION PLAN / NON-NORMATIVE UNTIL INDIVIDUAL DISPOSITIONS PASS G1-G8`

This R4 supersedes `methodology/DDTA_R25_POST_HOLDOUT_OPERATOR_COMPLETE_REVIEW_WORK_PLAN_R3.md`
for execution order after completion of the existing-operator audit. R3 remains immutable historical
evidence of the semantic-family review strategy that produced the current findings.

Exact planning baseline:

```text
ca99122b2f628f169bed85e04e731c8f3f89ca3c
```

The method remains frozen during this plan:

```text
BA0 R1
BA1 R1
BA2 R3
BA3 R1
BA4 R1
BA5 R1
```

No guide, BA contract or governed DermaTriage documentation is changed merely by adopting this work plan.

## 2. Why a new plan is required

R3 was written while OP-09, OP-10, OP-11, OP-12 and OP-14 still required individual review.

R31 closes that milestone:

```text
EXISTING_OPERATOR_AUDIT = COMPLETE_14_OF_14
METHODOLOGY_REVIEW      = NOT_COMPLETE
```

The remaining problem is no longer "which existing operator should be reviewed next?".
It is now:

```text
observed semantic gap
    -> identify minimum adequate semantic level
    -> exhaust existing operator / kind / local construct / composition / projection
    -> test candidate
    -> apply G1-G8
    -> disposition
```

The work therefore moves from operator-by-operator audit to integrated semantic disposition.

## 3. Research sufficiency statement

The R25 research record is sufficient to execute the current disposition cycle and, after the mandatory
completeness re-check, to drive an evidence-grounded revision of the BA method and BA guidance.

This means the repository already contains enough evidence to determine, case by case, whether the
observed DermaTriage/Facial Access pressures require:

- clarification of an existing construct;
- signature/cardinality change to an existing operator;
- controlled kind/value;
- condition/rule-language extension;
- cross-cutting qualifier or reusable structure;
- proposition composition/projection;
- new top-level operator candidate;
- or explicit deferral for insufficient evidence.

It does **not** mean that DDTA is proven universally complete. `NOT_TESTED` and
`INSUFFICIENT_EVIDENCE` remain valid final dispositions where the governed corpora cannot support a
stronger claim.

No new exploratory corpus is required before beginning this disposition plan.

## 4. Governing principles

```text
SOURCE MEANING BEFORE VOCABULARY
SEMANTIC LOSS BEFORE NEW CONSTRUCT
EXISTING OPERATOR BEFORE NEW OPERATOR
KIND / LOCAL STRUCTURE BEFORE LEXICAL SPECIALIZATION
COMPOSITION / PROJECTION BEFORE NEW PRIMITIVE
NO SYNTHETIC EXAMPLE SATISFIES G1
NOT_TESTED != REJECTED
14_OF_14_REVIEWED != METHOD_COMPLETE
```

A source verb is never sufficient evidence for a same-named operator.

## 5. Review namespaces

Retained:

```text
OP-*   admitted BA2 R3 top-level operators
CL-*   decisionRule condition-language constructs
PR-*   observed semantic pressure topics
CC-*   explicit candidate constructs
CMD-*  candidate method deltas to existing operators
SF-*   semantic-family review clusters
```

R4 adds no new semantic namespace. The disposition matrix is an execution artifact, not a metamodel.

## 6. Current admitted top-level basis

The admitted BA2 R3 operator basis remains:

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

All 14 have completed their required existing-operator audit. No OP-15 is admitted at plan start.

## 7. Current local condition/rule constructs

The frozen guide contains:

```text
CL-01 comparison
CL-02 satisfies
CL-03 allOf
CL-04 anyOf
CL-05 not
resultAssignment
```

These are not all equally validated. R4 requires their explicit audit before candidate pressure
disposition because some apparent top-level gaps may be absorbed by a correctly scoped local-language
extension.

## 8. Full retained pressure register

```text
PR-01 function/process/behavior identity binding
PR-02 pipeline composition/order
PR-03 interface/path/invocation association
PR-04 boundary/interaction association
PR-05 ordered comparison vocabulary
PR-06 scalar/property-addressing comparison
PR-07 structured data/information contract
PR-08 artifact/store/persistence association
PR-09 acquisition/refresh action semantics
PR-10 conditional action trigger semantics
PR-11 data/evidence consumption semantics
PR-12 negative implication/non-sufficiency semantics
PR-13 bounded recency/collection selection semantics
PR-14 configuration/applicability binding
```

Existing explicit candidates:

```text
CC-01 consumeData
CC-02 provideService
```

Deferred method deltas:

```text
CMD-OP04-OBSERVE-RESULT-REMOVAL
CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
```

## 9. Provisional solution classes

Every pressure/candidate must end in exactly one primary disposition class:

```text
ABSORBED_BY_EXISTING_OPERATOR
CONTROLLED_KIND_OR_VALUE
LOCAL_CONDITION_LANGUAGE_EXTENSION
REUSABLE_CROSS_CUTTING_STRUCTURE
COMPOSITION_OR_PROJECTION
APPLICATION_CORRECTION
METHOD_DELTA_TO_EXISTING_OPERATOR
NEW_TOP_LEVEL_OPERATOR
DEFER_NOT_TESTED
REJECT_REDUNDANT
REJECT_FALSE_SEMANTICS
NOT_GOVERNED
```

The chosen class must include source evidence and an explanation of why all lower-cost semantic
alternatives are insufficient.

## 10. Candidate hypotheses to test — not admitted constructs

R4 records the following **hypotheses**, without allocating new CC identities at plan adoption:

```text
PR-01 -> perform / execute relation ?
PR-03 -> invoke / interface-operation relation ?
PR-08 -> persist / storedIn relation ?
PR-10 -> trigger / conditional-action construct ?
PR-13 -> select / rank / bounded-selection construct ?
```

These names are diagnostic labels only.

A new `CC-*` identity is created only when the relevant pressure review shows an autonomous missing
semantic slot whose ownership is not already adequately represented by an existing PR/CC.

## 11. Phase A — condition-language audit

Review in this order:

```text
CL-01 comparison
CL-02 satisfies
CL-03 allOf
CL-04 anyOf
CL-05 not
```

### CL-01 mandatory source cases

At minimum:

```text
confidence > 0.85
accuracy degradation at most 5%
accuracy degradation > 5%
no-worse-than reference
typed scalar values
property addressing
same literal with different governed semantic roles
```

Questions:

- Is `equals | notEquals` sufficient? Expected pressure says no; prove exact minimum extension.
- Which ordered comparison keys are required by governed evidence?
- How are typed scalar values represented?
- How is the compared property identified without inventing a global object model?
- Is "no worse than" reducible to a controlled ordered comparator plus metric orientation, or does it
  require additional governed structure?

### CL-02 `satisfies`

Test named governed conditions where the source does not expose a property/value decomposition.
Do not invent an internal boolean merely to use `comparison`.

### CL-03 `allOf`

Use the DermaTriage qualification rule requiring all applicable acceptance criteria.

### CL-04 `anyOf`

Seek a clean source-grounded disjunction. If none exists, retain `NOT_SUFFICIENTLY_TESTED`; do not use
synthetic convenience as admission evidence.

### CL-05 `not`

Require a clean local-negation example. `agrees == False` is an encoding of a governed concept and
`A MUST NOT by itself imply B` is negative non-sufficiency; neither automatically proves `not`.

## 12. Phase B — candidate/pressure disposition by semantic family

### B1 — Execution / service / consumption / invocation

Review together:

```text
PR-01 performs/executes
PR-03 invocation/interface/path
PR-11 data/evidence consumption
CC-01 consumeData
CC-02 provideService
```

Must preserve distinctions:

```text
perform != realize
perform != produce
perform != assignResponsibility
provideService != realize
provideService != assignResponsibility
consumeData != consumeService
consumeData != observe automatically
invoke endpoint != consumeService automatically
endpoint/path != service/capability
```

Explicit candidate tests:

```text
perform(actor, behavior) ?
consumeData(consumer, data) ?
provideService(provider, service) ?
invoke(caller, operation/interface) ?
```

Do not admit any of these until composition and projection tests fail to preserve source meaning.

### B2 — State / persistence / acquisition / applicability

Review:

```text
PR-08 persistence/store
PR-09 acquire/refresh/renew
PR-14 applicability
CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
```

Candidate hypotheses:

```text
persist(content, store) ?
acquire/refresh as behavior/relation ?
applicability as cross-cutting qualifier/structure ?
```

Required boundary tests:

```text
persist != produce
persist != reference
persist != transition
refresh != observe automatically
refresh != create automatically
applicability != ordinary reference
same literal != same semantic role
```

Prefer cross-cutting applicability structure over a generic top-level `apply` operator unless evidence
shows autonomous project meaning and projection value.

### B3 — Pipeline / ordering / boundary

Review:

```text
PR-02 pipeline composition/order
PR-03 interface/path/invocation
PR-04 boundary/interaction
```

Test small orthogonal relations before a monolithic pipeline operator:

```text
memberOf / contains ?
precedes ?
interactsThrough ?
invoke ?
```

Required distinctions:

```text
precedes != dependOn
contains != realize
boundary crossing != transfer unless boundary meaning is preserved
endpoint membership != invocation
```

### B4 — Structured information

Review PR-07.

Test whether source meaning requires:

- structured typed value;
- information-contract structure;
- field membership;
- required/optional field semantics;
- value-domain constraints;
- or a top-level relation.

Do not create a dynamic operator for a static information schema merely for symmetry.

### B5 — Trigger semantics

Review PR-10 after CL audit.

Core source shapes:

```text
reaches 10 -> activate prompt evolution
reaches 50 -> activate classifier adaptation
```

Test in order:

1. `decisionRule` + existing result assignment;
2. extension of local rule language with action consequence;
3. reusable trigger structure;
4. only then top-level `trigger`.

A conditional capability requirement or conditional action is not automatically a result-selection
decision rule.

### B6 — Negative non-sufficiency

Review PR-12 after CL-03..CL-05.

Core meaning:

```text
A MUST NOT by itself imply B
```

This means `A alone is insufficient to infer B`; it is not equivalent to `IF A THEN NOT B`.

Test logical/governance representation before any top-level operator.

### B7 — Bounded / ranked selection

Review PR-13.

Core source cases:

```text
top-5 most similar historical cases
20 most recent pertinent corrections
best checkpoint according to validation Macro F1
```

The representation must preserve, when governed:

```text
candidate/source set
selection criterion
ranking or recency
limit/cardinality
selected result/subset
```

Test:

1. existing operator composition;
2. CL-01/local rule extension;
3. reusable selection structure;
4. top-level `select` only if autonomous proposition semantics and projection value remain lost.

## 13. Mandatory Candidate Construct Disposition Matrix

`validation-evidence/dermatriage/post-holdout-method-review-r1/working-findings/CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R1.md`
is the controlling working matrix for this plan.

Every PR, CC and CMD must record:

```text
SOURCE MEANING
SOURCE CASES
CURRENT REPRESENTATION
PRESERVED MEANING
LOST / DISTORTED MEANING
NEAREST EXISTING CONSTRUCT
ABSORPTION TEST
COMPOSITION TEST
PROJECTION TEST
DELETE TEST
PROVISIONAL SOLUTION
SEMANTIC LEVEL
EVIDENCE STATUS
G1-G8 STATUS
FINAL DISPOSITION
```

No item is closed by omission.

## 14. G1-G8 admission gate

Retain the existing gate:

```text
G1 Source evidence
G2 General formulation
G3 Construct exhaustion
G4 No false semantics
G5 Minimality
G6 Non-redundancy
G7 Backward compatibility
G8 Projection / feedback value
```

A proposed new top-level operator must pass all eight before admission.

### Additional R4 top-level operator test

Before `NEW_TOP_LEVEL_OPERATOR`, answer all:

```text
1. Is the meaning independently governed?
2. Does it survive every nearby existing operator?
3. Does proposition composition still lose material meaning?
4. Is a kind/value/local construct insufficient?
5. Is the proposition independently queryable?
6. Does removing it damage deterministic projections or feedback?
7. Is the signature stable and method-neutral?
8. Does the operator avoid encoding project-specific technology?
```

If any answer is unsupported, do not admit the operator.

## 15. Cross-candidate reconciliation

After individual reviews, compare surviving solutions to prevent duplicate primitives.

Mandatory comparisons include:

```text
perform vs invoke
perform vs provideService
consumeData vs observe vs produce.input
persist vs produce/reference/transition
trigger vs local rule action consequence
select vs CL-01/ranking structure
pipeline ordering vs dependOn
applicability vs reference/constraint/rule-local scope
structured information vs constrain/classify
```

One observed source sentence may legitimately generate multiple orthogonal propositions; avoid forcing
all facets into one operator.

## 16. Candidate method-delta reconciliation

Revisit:

```text
CMD-OP04-OBSERVE-RESULT-REMOVAL
CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
```

For each, determine whether the accumulated corpus confirms:

- signature simplification/extension;
- application-only correction;
- or deferral.

A method delta to an existing operator is preferable to a new operator when it restores the intended
semantic nucleus without overloading the operator.

## 17. Phase C — mandatory source-complete pre-rewrite completeness re-check

After CL and PR/CC/CMD disposition, re-read the **entire current governed DermaTriage documentation**.

Reconcile every governed source meaning against:

```text
all OP-01..OP-14 reviews
all CL-01..CL-05 outcomes
all PR-01..PR-14 outcomes
all CC outcomes
all CMD outcomes
application reconciliation findings
independent-review provenance limits
```

For each materially relevant source meaning, verify that it has an explicit path to:

```text
existing operator
newly admitted operator
kind/value
local construct
cross-cutting structure
composition/projection
application correction
NOT_GOVERNED
DEFER_NOT_TESTED / INSUFFICIENT_EVIDENCE
```

No materially observed gap may remain unclassified.

This is a focused completeness/control pass. It does not prove universal semantic completeness and does
not replace the later General Discovery Pack.

## 18. Phase D — integrated method revision

Only after Phase C passes may the method be unfrozen for integrated revision.

Decide, as one coherent change set:

- whether BA2 R4 is required;
- final operator list and signatures;
- final CL vocabulary/structures;
- cross-cutting reusable structures;
- compatibility/migration rules from BA2 R3;
- any admitted OP-04/OP-05 method deltas;
- explicit deferred/not-tested limitations.

Do not mutate one guide first and infer the method from prose later.

## 19. Phase E — guidance revision

After the integrated method contract is fixed, update guidance in dependency order:

```text
1. normative BA contract(s)
2. DDTA Base Analysis Operational Guide
3. DDTA Documentation BA Authoring Guide
4. examples and migration notes
5. validators/tooling only after L1/L2 meaning is stable
```

The new guide must explain every admitted construct word-by-word and demonstrate extraction from
complete governed source fragments, including both positive and boundary examples.

## 20. Phase F — full DermaTriage BA reconstruction

Reconstruct the complete DermaTriage BA from the full governed baseline using only the newly frozen
method.

The rerun must expose:

- preserved meaning;
- newly representable meaning;
- remaining `NOT_SPECIFIED` / `NOT_GOVERNED`;
- any application defects;
- projection improvements attributable to the method change.

The rerun cannot create project authority absent from source documentation.

## 21. Phase G — later General Discovery

The General BA Semantic Discovery Pack remains deferred to the third complete analysis cycle.

Its purpose remains independent:

```text
no operator-specific prompt
    -> inspect full governed documentation
    -> detect semantic meaning not suggested by the stabilized vocabulary
```

This later cycle is the stronger challenge against vocabulary anchoring and is not replaced by the
R25 pre-rewrite completeness re-check.

## 22. Completion criteria for this plan

R4 is complete only when:

```text
CL-01..CL-05 have dispositions
PR-01..PR-14 have dispositions
CC-01..CC-02 and any newly justified CC have dispositions
CMD-OP04 and CMD-OP05 have dispositions
cross-candidate reconciliation is complete
G1-G8 has been applied to every proposed method delta
source-complete pre-rewrite completeness re-check passes
integrated method revision is explicitly authorized
```

Until then:

```text
GUIDE_REWRITE = BLOCKED
FINAL_DERMATRIAGE_BA = BLOCKED
```

## 23. Immediate next action

```text
ACTIVE BASELINE:
ca99122b2f628f169bed85e04e731c8f3f89ca3c

FIRST REVIEW:
CL-01 comparison

CONTROLLING WORKING ARTIFACT:
CANDIDATE_CONSTRUCT_DISPOSITION_MATRIX_R1.md
```

Start CL-01 with the current governed corpus and route its outcome back into PR-05 and PR-06 before
moving to CL-02.
