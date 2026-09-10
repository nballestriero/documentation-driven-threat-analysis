# DDTA R25 — Post-Operator-Audit Candidate Disposition Work Plan R4

## 1. Purpose

R4 supersedes `DDTA_R25_POST_HOLDOUT_OPERATOR_COMPLETE_REVIEW_WORK_PLAN_R3.md` for execution order after the 14/14 existing-operator audit. R3 remains immutable historical evidence.

R4 incorporates the first conceptual pressure/candidate-group reconciliation. It explicitly separates:

```text
natural-language verb
semantic relation/effect
candidate construct
normative BA operator
```

A familiar verb does not create a BA operator.

## 2. Frozen method

The normative method remains:

```text
BA0 R1
BA1 R1
BA2 R3
BA3 R1
BA4 R1
BA5 R1
```

Forbidden during conceptual review:

- normative BA0–BA5 mutation;
- documentation-authoring-method mutation;
- adding a top-level operator because source prose uses a verb;
- inventing output, state, identity, mutation, actor, role or condition;
- treating a plausible implementation as project truth.

## 3. Existing-operator state

```text
OP-01..OP-14 REVIEW COMPLETE 14_OF_14
```

No top-level operator is added or removed by R4.

Open existing-operator method deltas remain:

```text
CMD-OP04-OBSERVE-RESULT-REMOVAL
CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
```

`decisionRule` remains stable while CL-01..CL-05 are still pending formal review.

## 4. Strengthened delete/exhaustion rule

For every candidate or pressure ask:

> If the candidate proposition is deleted, what governed information can no longer be reconstructed deterministically?

Before a new construct survives, test:

1. existing operator instance;
2. existing role/kind/controlled value;
3. local reusable structure;
4. composition of existing propositions;
5. deterministic projection;
6. documentation/application correction;
7. only then a new method construct.

Lexical difference is insufficient. The semantic distinction must be useful and irreducible.

## 5. Function/mutation discipline

Do not infer value/state change merely because the source says `update`, `modify`, `fine-tune`, `train` or `execute`.

```text
x_after = f(x_before)
    does not imply
x_after != x_before
```

Keep distinct unless the source binds them:

```text
operation execution
operation target/effect scope
write/update eligibility
actual value change
new semantic identity
lifecycle transition
```

## 6. First candidate group

### PR-01 function/process/behavior identity binding

The working `perform(actor, behavior)` hypothesis was tested but irreducibility is not demonstrated.

- Output-producing classification may be represented by `produce`.
- Retraining wording does not by itself require `perform`.
- `perform` must not merely mirror the source verb `execute`.
- FR-27 exposes operation-target/effect-scope questions more strongly than performer semantics.

```text
PR-01
    PRESSURE_RETAINED
    PERFORM_WORKING_HYPOTHESIS_NOT_ADMITTED
    IRREDUCIBILITY_NOT_DEMONSTRATED
```

### CC-01 consumeData

Non-destructive data use does not require a separate primitive when the governed meaning is already preserved by, as applicable:

```text
produce.input
decisionRule.input
observe
transfer
other exact composition
```

Use `observe` only when reading/querying/inspection itself is governed; do not infer it from every input relation.

Destructive consumption such as dequeue/remove/claim/acknowledge is semantically different, but is not governed by current DermaTriage evidence and must first be tested against existing composition.

```text
CC-01 consumeData
    CANDIDATE_REJECTED_REDUNDANT
```

A generic `consume` operator is not justified.

### CC-02 provideService

Service provision remains distinguishable from:

```text
realize
assignResponsibility
consumeService
data provision
endpoint exposure
```

Current DermaTriage evidence still lacks a sufficiently clean autonomous `Provider P provides Service S` positive control independent of a specific consumer/projection.

```text
CC-02 provideService
    CANDIDATE_INSUFFICIENT_EVIDENCE
    RETAIN FOR OTHER CORPUS / COMPLETENESS RECHECK
```

## 7. FR-27 model-evolution reconciliation

Current evidence supports:

```text
logical model identity
model-version concept
reference version 1.0.0
recoverable version plurality
active-model distinction
```

Current evidence does not establish:

```text
one new ModelVersion per retraining cycle
actual value inequality for every trained parameter
new identity merely because weights may be recomputed
lifecycle transition merely because parameters are in training scope
exact rollback target
```

Neither `perform` nor `modify` is therefore admitted from FR-27.

Retain:

```text
OBS-OT-01 OPERATION_TARGET_EFFECT_SCOPE
```

This asks how a governed operation's target/effect scope should be represented without asserting a stronger postcondition.

## 8. Candidate-specific question packs

The first-group questions are preserved in:

```text
PR01_PERFORM_QUESTION_PACK_R1.md
CC01_CONSUMEDATA_QUESTION_PACK_R1.md
CC02_PROVIDESERVICE_QUESTION_PACK_R1.md
```

They are review tools, not project truth.

## 9. Next conceptual discussion group

Review together for corpus efficiency but present findings separately:

```text
PR-08 persistence / storedIn
PR-03 invoke / expose
PR-10 conditional action trigger
PR-13 selection / ranking / bounded selection
```

For each:

1. define the smallest source-grounded meaning;
2. state what it must not imply;
3. enumerate source anchors;
4. test existing operators and composition;
5. identify negative controls;
6. apply the delete test;
7. identify independent queries/projections;
8. only then hypothesize signature and level.

Do not allocate new `CC-*` identifiers for naming convenience.

## 10. Remaining pressures after group 2

```text
PR-02 pipeline composition/order
PR-04 boundary/interaction
PR-07 structured data/information contract
PR-09 acquisition/refresh
PR-12 negative non-sufficiency
PR-14 applicability
OBS-OT-01 operation-target/effect-scope
```

Potential names such as `memberOf`, `precedes`, `interactsThrough`, `acquire`, `refresh` or `appliesTo` remain hypotheses only.

## 11. Condition-language audit

Still required:

```text
CL-01 comparison
CL-02 satisfies
CL-03 allOf
CL-04 anyOf
CL-05 not
```

Current evidence strongly pressures CL-01 beyond `equals | notEquals`; no extension is normative until consolidated.

## 12. G1–G8 gate

Any surviving method delta must pass:

- G1 Source evidence
- G2 General formulation
- G3 Construct exhaustion
- G4 No false semantics
- G5 Minimality
- G6 Non-redundancy
- G7 Backward compatibility
- G8 Projection/feedback value

A construct can be intelligible and still fail G3–G6.

## 13. Mandatory completeness re-check

Before guide or final BA rewrite, reconcile the complete governed corpus against:

- all 14 operator reviews;
- CL-01..CL-05;
- PR-01..PR-14;
- all CC candidates;
- `OBS-OT-01`;
- deferred method deltas;
- application-reconciliation findings;
- independent-review provenance limits.

Every surviving gap must receive an explicit disposition.

## 14. Integrated revision and rerun

Only after the completeness gate:

```text
1. decide surviving method deltas
2. decide whether BA2 R4 is warranted
3. update operational/authoring guidance
4. publish compatibility/migration notes
5. rebuild the complete DermaTriage BA
6. assess documentation improvements, strengths and limitations
```

General Discovery remains deferred to the third complete analysis cycle.

## 15. Immediate next action

```text
DISCUSS GROUP 2:
    PR-08 persistence / storedIn
    PR-03 invoke / expose
    PR-10 trigger
    PR-13 select / rank
```

Do not execute normative method changes during that discussion.
