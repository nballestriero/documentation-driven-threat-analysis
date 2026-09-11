# DDTA R25 — Source-Complete Reconstruction and Consolidation Gate R1

## Status

`ACTIVE REALIGNMENT GATE / NON-NORMATIVE`

Repository baseline:

```text
6e6ec547d2def68833547cc7a5848835d6948b43
```

This gate is deliberately placed **before** any candidate successor revision of the Documentation
BA Authoring Guide or Base Analysis Operational Guide.

Its purpose is to decide what, if anything, belongs in normative methodology after the R25
DermaTriage control cycle.

## 1. Gate principle

R25 is a second/control cycle. A finding produced during this cycle is evidence until a separate
authority decision makes it normative.

Therefore:

```text
finding exists
    !=
guide must change

candidate survives delete test
    !=
candidate is admitted

source is unclear
    !=
BA may complete the source

question pack asks a question
    !=
project requirement exists
```

## 2. Required evidence sets

The gate is incomplete unless all of the following are reconciled:

### 2.1 Stable methodology

- Documentation BA Authoring Guide R5;
- Base Analysis Operational Guide R3;
- BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1;
- current methodology style conventions.

### 2.2 R25 control-cycle evidence

- Work Plan R8;
- Operator and Pressure Review Ledger R22;
- Candidate Construct Disposition Matrix R5;
- construct-specific question packs;
- semantic-family question packs;
- accepted/non-normative working findings;
- deferred CMD observations;
- PR-01..PR-14;
- CC-01..CC-04;
- condition-language findings CL-01..CL-05;
- OBS-OT-01.

### 2.3 Governed project source

- all four active MacroRequirement branches;
- every active Decision;
- all 26 active FunctionalRequirements;
- FR-11 as superseded historical identity;
- project framing and scope boundaries;
- explicit documentation-gap register.

### 2.4 Post-R36 continuity

- PR-13 source-complete selection reconstruction over FR-18, FR-06 and FR-20.

## 3. Per-source-element reconstruction record

For every governed source element that materially participates in BA, capture at least:

```text
sourceAnchor
sourceExcerptOrClauseIdentity
candidateSemanticFact[]
candidateRouting[]
rejectedRouting[]
requiredConditionsOrModifiers[]
identityDecisions[]
documentationQA[]
methodPressure[]
openInterpretation[]
```

The record must be source-grounded. Absence of an answer is not permission to invent one.

## 4. Documentation QA vocabulary

Use these outcomes consistently:

```text
ANSWERED
NOT_APPLICABLE
CLARITY_OPPORTUNITY
GOVERNED_GAP
```

Then independently classify unresolved review material as:

```text
SOURCE_DOCUMENT_GAP
METHODOLOGY_PRESSURE
INTERPRETIVE_UNCERTAINTY
VALIDATION_TARGET
```

The two classifications answer different questions and must not be collapsed.

## 5. Normative preservation gate

Before any R3->successor or R5->successor authoring:

1. enumerate every major normative section in the predecessor;
2. assign one preservation decision:
   - `PRESERVE_VERBATIM_OR_SEMANTIC_EQUIVALENT`;
   - `EXPAND_WITH_EVIDENCE`;
   - `CHANGE_REQUIRES_EXPLICIT_DELTA`;
3. prohibit silent deletion;
4. prohibit shortening merely for readability when normative information is lost;
5. require an explicit change rationale for every changed rule/signature/cardinality/boundary.

A cumulative successor is not valid merely because it is clearer or shorter.

## 6. Operator and semantic-boundary gate

At minimum, verify the following retained distinctions.

### 6.1 `produce` / `create`

```text
produce = result/output made available
create  = new project-semantic identity/occurrence
```

Do not infer creation from a factory name, output production, retrieval or persistence.

### 6.2 `transfer`

Preserve content, source and destination. Treat interaction mode, boundary, channel, retries,
timeouts, queueing and failure semantics only when governed.

### 6.3 `observe`

Preserve explicit read/query/inspection of existing state. Do not infer observation from every input
or every transferred object. Keep query-selection semantics distinct.

### 6.4 `transition`

Require same project-semantic subject identity plus governed lifecycle/state change. Do not equate
version selection, qualification result, property update or supported rollback with a transition.

### 6.5 `correlate` / `reference`

`correlate` preserves same-context binding; `reference` preserves a directional target identity.
Neither is a generic fallback for unclear relations.

### 6.6 `dependOn`

Require prerequisite semantics. Temporal order alone is not dependency; transitive closure may be a
projection rather than stored BA truth.

### 6.7 `consumeService`

Require actual service/capability use. Endpoint, component, technology and information/evidence are
not automatically services.

### 6.8 `realize`

Require concrete materialization of independently governed abstract meaning. Do not use `realize` as
a substitute for unadmitted `perform/execute` semantics.

### 6.9 `assignResponsibility`

Keep responsibility/authority distinct from provider, performer, producer, consumer, realization
and mere participation.

### 6.10 `constrain`

Keep reusable/queryable restrictions distinct from local conditions, trigger thresholds, decision
mappings, bounded selection and `NOT_GOVERNED`.

### 6.11 `classify`

Preserve semantic kind/category meaning. Do not use it to encode criterion-based selection,
lifecycle transition or generic property assignment without source support.

### 6.12 `decisionRule`

Require a governed mapping from conditions/inputs to a governed result. A conditional action,
non-sufficiency statement, ranking query or support/capability clause is not automatically a
`decisionRule`.

### 6.13 `perform?`

PR-01 remains pressure only. Execution evidence exists, but irreducibility has not been demonstrated.

## 7. Candidate-construct gate

Preserve current status exactly until formal admission work is performed:

| ID | Candidate | Current status | R37 authority |
|---|---|---|---|
| CC-01 | `consumeData` | `REJECT_REDUNDANT` | evidence |
| CC-02 | `provideService` | `TESTED_POSITIVE / NOT_ADMITTED` | evidence |
| CC-03 | `storedIn` | `TESTED_POSITIVE / NOT_ADMITTED` | evidence |
| CC-04 | `initiate` | `TESTED_POSITIVE / NOT_ADMITTED` | evidence |

A future guide may explain these as validation findings, but must not list CC-02/03/04 as official
operators unless the formal admission gate is separately completed.

## 8. PR-13 gate

Check FR-18, FR-06 and FR-20 separately.

Required distinctions:

```text
candidate population
criterion
ordering/ranking when governed
bound when governed
selected membership/result
later retrieval/use
```

Do not reduce all of these to `topK`.

Current R37 working conclusion:

```text
selection semantics are reusable and non-deletable in the tested cases
a new top-level operator is not yet justified
a reusable selection structure is the preferred working representation
CL-01 ordered-comparison pressure remains separate
```

This result is evidence, not a BA2 mutation.

## 9. DermaTriage source-completeness gate

The coverage matrix must account for all 26 active FRs:

```text
FR-01 FR-02 FR-03 FR-04 FR-05 FR-06 FR-07 FR-08 FR-09 FR-10
FR-12 FR-13 FR-14 FR-15 FR-16 FR-17 FR-18 FR-19 FR-20 FR-21
FR-22 FR-23 FR-24 FR-25 FR-26 FR-27
```

FR-11 must be explicitly treated as superseded, not silently ignored or reactivated.

The review must also cover every explicit documentation gap already present in the governed source.

## 10. Destination decision

After reconstruction, assign every material result exactly one primary destination:

### `GUIDE_DELTA_REQUIRED`

Use only when the stable normative guide is materially incomplete, ambiguous or incorrect and the
R25 evidence supports a normative procedure/semantic change.

### `COMPANION_ONLY`

Use for pedagogical explanations, worked examples, operator-choice reasoning, negative examples and
diagnostic question sequences that improve usability without changing method authority.

### `EVIDENCE_ONLY`

Use for empirical controls, rejected hypotheses, corpus-specific observations and historical
validation evidence that should not become general method rules.

### `DOCUMENTATION_REMEDIATION`

Use when the source project is under-governed or internally unclear. Do not “fix” such issues by
changing BA semantics.

### `TARGETED_REOPEN_REQUIRED`

Use when governed meaning is clear but the frozen method cannot preserve it without demonstrated
loss and the issue cannot yet pass an admission/delta gate.

### `NO_CHANGE`

Use when the control cycle confirms the current guide and no additional normative text is needed.

## 11. Guide decision rule

Only after the per-item destination table is complete:

```text
if any item == GUIDE_DELTA_REQUIRED:
    author candidate cumulative guide successor
else:
    do not revise the normative guide merely to record the review
```

A companion may still be justified even when no normative guide delta exists.

## 12. Consolidation pass criteria

The R37 gate may be marked `READY_FOR_CONSOLIDATION` only when:

- predecessor normative content is accounted for;
- all governed source elements are covered;
- every explicit source gap is preserved/classified;
- every R25 PR/CC/CMD/CL/OBS item has a disposition/destination;
- PR-13 is captured without premature operator admission;
- evidence and authority are visibly separated;
- no source gap has been silently completed;
- no candidate has been silently promoted;
- open targeted questions have explicit owners/next tests.

## 13. Expected decision after this gate

The gate should answer two separate questions:

```text
Q1. Does the normative method need a cumulative guide revision?
Q2. Does usability need a worked/pedagogical companion even if Q1 = NO?
```

This separation is intentional. It avoids rewriting stable authority simply because the validation
cycle produced useful teaching material.

## 14. Current gate state

```text
SOURCE_COVERAGE_INDEXED
PR13_RECONSTRUCTED
DESTINATION_CLASSIFICATION_PENDING
NORMATIVE_GUIDE_DELTA_DECISION_PENDING
READY_FOR_CONSOLIDATION = NO
```
