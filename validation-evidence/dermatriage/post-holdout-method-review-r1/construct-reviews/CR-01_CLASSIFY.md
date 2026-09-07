# CR-01 — `classify`

Status: `COMPLETE`

Checkpoint: `DDTA-R25-DERMATRIAGE-CR01-CLASSIFY-CONSOLIDATION-R14`

Frozen method baseline:

`BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1`

Governed project source:

`governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`

Authority baseline:

`DERMATRIAGE-GOV-R1`

Primary verdict:

`GUIDE_CLARIFICATION`

## 0. Consolidated decision

CR-01 confirms that the existing `classify` operator is semantically useful and does not require a new BA1 family, a new BA2 operator, or a signature change.

The review identified a guide-level distinction that must be made explicit:

```text
SOURCE-SUPPORTED SEMANTIC KIND
    preserves an explicit kind stated or supported by governed documentation

is not the same thing as

OPERATIONAL MACRO-KIND
    a reusable method-neutral semantic kind that justifies common
    representation, questions, queries, documentation QA, or downstream treatment
```

A source-supported semantic kind may therefore remain valid even when it is too specific to become a methodology-wide macro-kind.

Example:

```text
classify(PromptEvolutionPath, Capability)
```

may preserve the explicit governed statement that prompt evolution is a capability.

For common structural treatment, the same referent may also be treated through the reusable macro-kind:

```text
classify(PromptEvolutionPath, Behavior)
```

when the source meaning supports that classification.

The operational macro-kind working set retained by this review is:

```text
Actor
Component
Behavior
Interface
Boundary
Store
Information
State
```

This set is the minimal set supported by the DermaTriage audit for reusable treatment. It is not declared to be a closed universal vocabulary. New macro-kinds require the same generalization, minimality, and reusable-treatment test.

## A. Current construct / capability

Frozen BA2 R3 form:

```text
classify
    classifiedReferent -> BAReferent [1]
    semanticKind       -> BAReferent [1..*]
```

Current semantic purpose:

- preserve a stable semantic kind without creating a new first-class BA1 family;
- keep identity separate from semantic classification;
- permit more than one source-supported semantic kind for the same referent.

Closest alternatives such as `realize`, `dependOn`, `constrain`, or naming conventions do not preserve the same `X IS OF SEMANTIC KIND Y` meaning.

## B. General semantic need

The general need is:

```text
IDENTITY
    what project meaning is this?

+

SEMANTIC KIND
    what reusable kind of thing is it?

+

OPERATIONAL TREATMENT
    does that kind justify common questions, projections, or documentation checks?
```

The review must avoid both failure modes:

```text
every noun in the source
    -> global semantic kind
```

and:

```text
only a small global taxonomy is allowed
    -> explicit source-supported kinds are discarded
```

The resulting rule is:

```text
preserve explicit source-supported kinds when they carry governed meaning;

promote a kind to operational macro-kind only when members share
useful method-neutral treatment.
```

## C. Source evidence inventory

The full governed DermaTriage R1 baseline was reviewed across project framing, MR-01..MR-04, DEC-01..DEC-18, active FRs, and the final documentation-gap register.

Material evidence groups are summarized below.

| Source anchor | Evidence-bearing wording / meaning | Semantic need | CR-01 result |
|---|---|---|---|
| DEC-05 | prompt evolution and classifier adaptation are explicitly described as distinct **capability** | preserve explicit semantic kind | positive `classify` evidence; `Capability` need not become a global macro-kind |
| DEC-12 / FR-16..FR-19 | EfficientNet-B4, Qwen2-VL, ChromaDB and BioMistral perform distinct pipeline roles and produce/consume distinct outputs | executable elements, behaviors, information | supports `Component`, `Behavior`, `Information` |
| DEC-14 / FR-21 / FR-22 | FastAPI exposes `POST /analyze` and `POST /diagnose`; B4 remains external and the B4/DermaTriage boundary stays explicit | access path and separation | supports `Interface`, `Boundary` |
| MR-03 / DEC-03 / FR-03 / FR-12 | clinical judgement belongs to the healthcare professional; DermaTriage records and correlates review outcomes; confirmation and correction remain distinguishable | actor/authority, information, lifecycle condition | supports `Actor`, `Information`, `State` |
| DEC-15 / FR-23 | write-back and retrieval preserve consultation/case identity across B4 interaction | boundary crossing, interface, information correlation | supports `Boundary`, `Interface`, `Information` |
| DEC-16 / FR-24 / FR-25 | administrative operations and B4 interaction use distinct authentication mechanisms (`X-API-Key`, bearer JWT) | interface/boundary questions | reinforces `Interface`, `Boundary`, `Actor` |
| DEC-04 / FR-04 / FR-05 | adaptation processes activate only after path-specific accumulated evidence conditions are satisfied | action/trigger semantics | supports `Behavior`; `ActivationCondition` remains source meaning, not required as macro-kind |
| DEC-06 / FR-09 | a candidate is evaluated and may become qualified for adoption only after applicable criteria are satisfied | lifecycle condition | supports `State` |
| DEC-08 / FR-10 | adopted adaptation can be revoked; previous acceptable versions are maintained and an active model is identifiable | persistence and lifecycle state | supports `Store`, `State` |
| DEC-09 / FR-06 | a bounded recent evidence set is constructed for prompt evolution | information selection | supports `Information`; specific `EvidenceSet`/`EvidenceWindow` need not be global macro-kinds |
| DEC-10 / FR-07 | clinician disagreement qualifies as classifier-adaptation evidence | semantic information and qualification state | supports `Information` and state/rule treatment |
| DEC-11 / FR-08 | corrected P-scale priority is mapped to a classifier supervision target | derived information | supports `Information` |
| DEC-17 / FR-26 | PromptManager is a component; prompt versions are persisted in `db/prompts.json`; update/reset/history are supported | component, persistence, version state | supports `Component`, `Store`, `State` |
| DEC-18 / FR-27 | incremental retraining consumes qualified corrections and B4 images and updates selected EfficientNet-B4 blocks | behavior, component, information | supports `Behavior`, `Component`, `Information` |
| Final gap register | input contracts, history/retention, ordering, deduplication, authority, deployment, rollback binding and related meanings remain explicitly bounded | documentation QA | validates value of kind-specific question packs without converting unanswered questions into requirements |

No inference from absent documentation is used to populate these kinds.

## D. Chat evidence record

CR-01 was performed interactively.

The conversation established and accepted:

- the frozen `classify` signature;
- explicit positive evidence from DEC-05;
- the distinction between semantic identity and reusable semantic kind;
- the need to audit all BAReferents rather than only previously emitted `classify` propositions;
- the reusable-treatment criterion for macro-kind admission;
- the eight-kind operational set;
- kind-specific common questions;
- the four-way documentation finding classification:
  `ANSWERED`, `CLARITY_OPPORTUNITY`, `GOVERNED_GAP`, `NOT_APPLICABLE`.

The user explicitly accepted retaining this set and the associated questions before this consolidation.

## E. Prior-corpus evidence

No new cross-corpus admission claim is made in CR-01.

The DermaTriage audit is sufficient to justify a guide clarification and a working reusable macro-kind set, but not to declare the eight kinds a closed universal taxonomy.

Future corpora, including Facial Access reuse, may:

- confirm the same macro-kinds;
- show that one is unnecessary outside DermaTriage;
- provide evidence for an additional reusable macro-kind.

Any addition must pass the same reusable-treatment test.

## F. Independent expert signals

The R12 independent expert reports remain bounded supporting evidence because of the recorded protocol deviation.

For CR-01:

- expert disagreement on `classify` usefulness/application is treated as a guide/application calibration signal;
- no expert statement is used to create or remove a semantic kind;
- the macro-kind working set is admitted from governed source meaning plus the reusable-treatment test, not from expert preference.

Admissibility classification:

`SUPPORTING_DIVERGENCE`

Strict frozen-R3 reproducibility claim:

`NOT_MADE`

## G. Existing representation attempts

### Attempt 1 — source-specific classification

Example:

```text
classify(PromptEvolutionPath, Capability)
```

Preserved:

- explicit source statement that the referent is a capability.

Problem:

- if every source noun becomes a global taxonomy entry, `classify` becomes an unbounded project ontology.

Resolution:

- retain source-supported semantic classification;
- do not automatically promote the kind to operational macro-kind.

### Attempt 2 — only broad macro-kind classification

Example:

```text
classify(PromptEvolutionPath, Behavior)
```

Preserved:

- common structural treatment of an executable/evolving behavior.

Potential loss:

- the explicit source statement that it is a `Capability`.

Resolution:

- multiple classifications are permitted when independently source-supported;
- macro-kind treatment does not replace source-specific meaning.

### Attempt 3 — over-specific macro-kind proliferation

Observed candidates included:

```text
ActivationCondition
AdaptationCandidate
LifecycleResult
ModelVersion
AcceptanceCriterion
Threshold
EvidenceWindow
EvidenceSet
EvidenceQualificationCondition
SupervisionTarget
Capability
```

These may be valid project meanings, but the DermaTriage audit does not show that each deserves its own reusable graphical treatment, common question family, or global methodology vocabulary.

Disposition:

`DO NOT PROMOTE AUTOMATICALLY TO OPERATIONAL MACRO-KIND`

## H. Composition test

The existing frozen construct is sufficient:

```text
classify(referent, sourceSpecificKind)
classify(referent, reusableMacroKind)
```

when both classifications are independently supported.

No new operator is necessary.

The question packs are guide-level analytical consumers of the reusable macro-kind and do not create project truth.

Result:

`PASS — existing construct composition is sufficient`

## I. Gap classification

Primary cause:

`GUIDE_CLARITY`

Secondary observation:

`APPLICATION_ERROR` may occur when analysts either under-apply a well-supported reusable kind or promote every nominal source concept into a global taxonomy.

No BA2 representation limit was demonstrated.

## J. Generalization test

Domain-neutral formulation:

> A semantic kind deserves standardized method treatment only when instances share useful method-neutral representation, questions, queries, documentation checks, or downstream analysis.

The eight retained kinds correspond to distinct structural questions:

```text
Actor       -> WHO ACTS / OWNS AUTHORITY?
Component   -> WHAT EXECUTES / PROVIDES?
Behavior    -> WHAT HAPPENS?
Interface   -> HOW IS IT ACCESSED?
Boundary    -> WHAT IS SEPARATED / CROSSED?
Store       -> WHAT PERSISTS?
Information -> WHAT MEANING IS PRODUCED / CONSUMED / TRANSFERRED?
State       -> WHAT CONDITION CAN AN IDENTIFIABLE THING BE IN?
```

Result:

`PASS`

## K. Minimality / redundancy test

No new BA1 family is required.

No new BA2 operator is required.

No closed ontology is required.

Smallest change:

1. clarify source-specific semantic kind versus operational macro-kind;
2. define the reusable-treatment admission criterion;
3. provide the eight-kind working catalog;
4. attach common question packs;
5. preserve an extension gate for future corpora.

Result:

`PASS`

## L. Backward-compatibility test

Existing accepted `classify` propositions remain semantically valid when source-supported.

Examples such as:

```text
classify(x, Capability)
classify(x, Threshold)
```

are not invalidated merely because `Capability` or `Threshold` are not in the operational macro-kind catalog.

The distinction affects standardized treatment, not historical source truth.

Immediate migration:

`NONE`

Later effective-BA rebuild may add missing reusable macro-kind classifications or remove unsupported classifications, but only through source-traceable reconciliation.

Result:

`PASS`

## M. Projection / feedback value

Operational macro-kinds provide deterministic consumers without reparsing project documentation.

Examples:

```text
Store
    -> persistence questions
    -> read/write queries
    -> version/history/retention coverage

Interface
    -> provider/consumer questions
    -> authentication and boundary queries

Actor
    -> responsibility and authority questions

Information
    -> producer/consumer/contract questions
```

This supports:

- common diagram treatment;
- repeatable queries;
- documentation coverage and clarity observations;
- later threat-analysis projections;
- source-localized feedback to documentation authors.

Important guardrail:

```text
unanswered question
    -X-> automatically missing requirement
```

Each answer is classified as:

```text
ANSWERED
CLARITY_OPPORTUNITY
GOVERNED_GAP
NOT_APPLICABLE
```

## N. Verdict

Primary verdict:

`GUIDE_CLARIFICATION`

Rationale:

`classify` already preserves the required semantic distinction. The empirical problem is how analysts decide which source-supported kinds deserve reusable standardized treatment. DermaTriage supports a minimal working set of eight operational macro-kinds and shows that attaching common questions to those kinds adds documentation-QA value without inventing project truth.

Method delta candidate:

```text
semantic need:
    distinguish source-supported semantic classification from reusable
    operational macro-kind treatment.

minimal proposed delta:
    clarify the authoring/operational guide so that:
      1. classify remains open to source-supported semantic kinds;
      2. operational macro-kinds require reusable method-neutral treatment;
      3. the observed working catalog is
         Actor, Component, Behavior, Interface, Boundary, Store, Information, State;
      4. each operational macro-kind has a standard question pack;
      5. the catalog is extensible only through evidence/generalization/minimality gates;
      6. unanswered questions are classified as
         ANSWERED / CLARITY_OPPORTUNITY / GOVERNED_GAP / NOT_APPLICABLE.

evidence basis:
    complete governed DermaTriage R1 semantic baseline audit.

open risks:
    - overfitting the eight-kind catalog to one corpus;
    - confusing source-specific semantic kinds with macro-kind membership;
    - converting common questions into inferred requirements;
    - applying graphical/downstream semantics that exceed governed meaning.
```

No candidate becomes normative BA methodology in this checkpoint.

---

# Appendix A — Operational macro-kind question packs

## Actor

Primary question:

`WHO ACTS, DECIDES, PROVIDES AUTHORITY OR PARTICIPATES?`

Questions:

- Who is the actor?
- Is it a person, role, organization, or external system?
- What responsibilities does it own?
- What activities does it perform?
- What does it produce?
- What does it consume?
- Over which decisions does it have authority?
- Which decisions does it explicitly not own?
- Is authority distinguishable from participation?
- With which Components does it interact?
- Through which Interfaces?
- Across which Boundaries?
- What Information does it provide, receive, or modify?
- Is the owner of each material action governed?
- Are proposal, decision, authorization, and execution distinguishable where material?

## Component

Primary question:

`WHAT EXECUTES, PROVIDES OR REALIZES BEHAVIOR?`

Questions:

- What component is it?
- What is its role?
- Which Behaviors does it realize?
- Which responsibilities are assigned to it?
- Which Information does it receive?
- Which Information does it produce?
- Which Components does it depend on?
- Which external services/components does it consume?
- Which Interfaces does it expose?
- Which Interfaces does it consume?
- Does it maintain State?
- Which configuration/version applies?
- Which Stores does it read?
- Which Stores does it write?
- On which side of a Boundary does it operate?

## Behavior

Primary question:

`WHAT HAPPENS?`

Questions:

- Who or what performs the Behavior?
- What triggers it?
- Is there an activation condition?
- Which Information does it consume?
- Where do inputs originate?
- What does it produce?
- Who consumes the result?
- Which preconditions apply?
- Which decision rules, thresholds, or constraints apply?
- Does it modify State?
- Does it create persistent side effects?
- Which Behavior occurs before it?
- Which Behavior follows it?
- Which dependencies or ordering constraints apply?
- Is an alternative/fallback path governed?
- What happens when expected input is unavailable?
- Does execution imply authority, or is authority separately governed?

## Interface

Primary question:

`HOW IS SOMETHING ACCESSED OR INVOKED?`

Questions:

- What is the Interface for?
- Who exposes it?
- Who invokes or consumes it?
- Which operations are available?
- Which Information does it accept?
- Which inputs are required or optional?
- What does it return or emit?
- Does it require authentication?
- Which authentication mechanism applies?
- Who is authorized to use it?
- Are authentication and authority distinct?
- Which Boundary does it cross?
- Which errors or fallbacks are governed?
- How is request/case/entity correlation preserved?

## Boundary

Primary question:

`WHAT IS SEPARATED OR CROSSED?`

Questions:

- What does the Boundary separate?
- Which Actors/Components are on each side?
- Which Information crosses it?
- Which Behaviors cause crossings?
- Through which Interfaces?
- Which controls apply at the crossing?
- How is the crossing authenticated?
- Does authority change across the Boundary?
- Which responsibilities remain on each side?
- Which trust assumptions or policies are governed?
- Which assumptions are explicitly not governed?
- How is identity/correlation preserved across the Boundary?

## Store

Primary question:

`WHAT PERSISTS?`

Questions:

- What does the Store retain?
- Who writes or updates it?
- Who reads it?
- Do persisted elements have stable identity?
- How are elements correlated?
- Are versions retained?
- Which version/state is active?
- When is an element created?
- When is it updated?
- When is it replaced?
- When is it deleted?
- Is history retained?
- Is retention governed?
- Is temporal ordering relevant and governed?
- Is deduplication governed?
- Are concurrent updates possible and defined?
- Which Actors/Components can access the Store?
- Does access cross a Boundary?

## Information

Primary question:

`WHAT MEANING IS PRODUCED, CONSUMED OR TRANSFERRED?`

Questions:

- What does the Information represent?
- Who produces it?
- Who consumes it?
- From which source does it originate?
- What structure does it have?
- Which fields/elements are material?
- Which values are allowed?
- Is it required or optional?
- Can it be absent?
- What does absence mean?
- What does an invalid value mean?
- To which case/entity does it refer?
- How is correlation preserved?
- Is it derived from other Information?
- Which rule governs that derivation?
- Is it persisted?
- In which Store?
- Does it cross a Boundary?
- Who has authority over its meaning?

## State

Primary question:

`WHAT CONDITION CAN AN IDENTIFIABLE THING BE IN?`

Questions:

- State of what subject?
- Which states are possible?
- What is the initial state?
- Which transitions are allowed?
- What triggers each transition?
- Who or what performs the transition?
- Which conditions must hold?
- Is State persisted?
- Where?
- Is transition history retained?
- Are terminal/final states defined?
- Can a state be revoked or rolled back?
- Who has authority to cause or approve the transition?
- Is qualification distinct from adoption, deployment, activation, or finality where applicable?

---

# Appendix B — Disposition of non-macro kinds observed in DermaTriage

| Kind / family | Operational disposition | Source meaning |
|---|---|---|
| `Capability` | common treatment folds into `Behavior` | may remain a valid source-supported semantic kind |
| `Service` | common treatment folds into `Component` + `Interface` | may remain valid when explicitly governed |
| `Artifact` | common treatment normally folds into `Information`, `Store`, or `State` | preserve specific source meaning when material |
| `Message` | `NOT_REQUIRED_BY_DERMATRIAGE_R1`; not globally rejected | future message/event-driven corpus may validate it |
| `ActivationCondition` | no separate standard question pack | preserve explicit condition meaning and relation to `Behavior` |
| `AdaptationCandidate` | no separate standard question pack | preserve identity/state meaning |
| `LifecycleResult` | no separate standard question pack | normally treated through `State` |
| `ModelVersion` | no separate standard question pack | normally `Information` + `State` + `Store` |
| `AcceptanceCriterion` | no separate standard question pack | preserve through rule/constraint semantics |
| `Threshold` | no separate standard question pack | preserve through constraint/rule semantics |
| `EvidenceWindow` | no separate standard question pack | normally `Information` plus selection behavior |
| `EvidenceSet` | no separate standard question pack | normally `Information` |
| `EvidenceQualificationCondition` | no separate standard question pack | preserve through decision/condition semantics |
| `SupervisionTarget` | no separate standard question pack | normally `Information` |

The table does not delete or invalidate source-supported classifications. It only denies automatic promotion to methodology-wide operational macro-kind.
