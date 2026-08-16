# BA2-T1 - BAProposition shape and participation-role lower-bound derivation

**Revision:** R1

**Status:** COMPLETED / PROVISIONAL CANDIDATE / BA2 NOT CLOSED

**Repository baseline reviewed:** `3d8251328c77177375cccf1c51caa54b7473e21e`

**Phase:** BA2 - Relations and canonical action vocabulary

**BA0:** CLOSED

**BA1:** CLOSED

**BA3:** NOT STARTED

## 1. Question and guardrail

BA2-T1 asks only:

> What is the minimum methodology-neutral structural shape required for one `BAProposition` to express reusable project facts over `BAReferent` identities without freezing an exhaustive predicate vocabulary or importing a domain/method taxonomy?

The test obeys the BA1 closure boundary:

```text
BAReferent     accepted identity family
BAProposition  accepted identity family
```

A failure that requires a third semantic identity family would reopen BA1. No such failure is found in this microstep.

BA2-T1 does not define provenance/source fields, views, ThreatForge classes, STRIDE/DFD semantics, Findings or a complete relation/action dictionary.

## 2. Evidence pressure

### 2.1 Documentation-layer constraint

The FunctionalRequirement metamodel makes normative prose semantically primary and explicitly states that SPO references do not carry all conditional, concurrency, lifecycle or failure semantics.

Its strong operational patterns include:

- condition -> required transition;
- request -> processing responsibility -> observable result;
- lifecycle event -> state change and failure behavior;
- interaction -> output/correlation behavior;
- concurrency condition -> atomicity/idempotency invariant.

Therefore BA2 cannot simply inherit documentation-layer SPO as the complete analytical proposition model.

### 2.2 Facial-access pressure

`FR-3.4` states one delivery meaning with at least these distinguishable semantic participants/conditions:

- `CameraSubsystem`;
- `RecognitionProcessor`;
- `RecognitionCapture`;
- `RecognitionRequest` correlation;
- incomplete delivery must not be represented as success.

The same delivery meaning is later constrained by confidentiality, integrity and authorized-origin requirements and survives some mutations while being retired by the local-recognition mutation.

### 2.3 Order-fulfillment pressure

The independent order corpus adds propositions that combine:

- executor/capability;
- request and result;
- `OrderEvaluation` correlation;
- `Reservation` lifecycle;
- all-lines atomicity;
- competing concurrency;
- idempotency;
- compensation;
- authorized/declined/indeterminate outcomes;
- physical handoff reuse across inventory and payment behavior.

The corpus explicitly says its actor/data/store/contract probe kinds are authoring substrate only and that final Base Analysis types are deferred.

## 3. Alternative A - universal binary SPO

Candidate:

```text
subject -- predicate --> object
```

### Test

Binary edges can represent simple facts, and they remain useful projections. The problem is using them as the **only** normative proposition shape.

For `FR-3.4`, four binary edges could encode source, destination, information and correlation only if there is a common semantic anchor that says they belong to the same delivery assertion. If the anchor is the `BAProposition`, the binary-only claim has already expanded into a role-bearing n-ary assertion. If the anchor is a synthetic `BAReferent` created for every relation occurrence, the model violates the BA1 distinction by using referent identity as a generic proposition proxy.

The order corpus makes the problem stronger: atomicity, concurrency and conditional result semantics apply to the joint configuration of multiple participants. Splitting them into unrelated triples requires a separate grouping/scope mechanism before the original claim can be reconstructed.

### Disposition

**REJECTED AS UNIVERSAL SHAPE.** Binary relations remain valid special cases or projections of a more general proposition structure.

## 4. Alternative B - one proposition with anonymous ordered participants

Candidate:

```text
operator(participant1, participant2, participant3, ...)
```

### Test

Positional ordering is insufficient because the same referent can occupy different semantic roles in different propositions, and method consumers should not depend on undocumented argument positions.

For example, `RecognitionCapture` may be transferred information in one assertion and the object of an acceptance/validity condition in another. `PaymentProvider` may be a destination/provider participant in one proposition and an external authority/context in another.

### Disposition

**REJECTED.** Participation roles must be explicit.

## 5. Alternative C - fixed domain-specific slots

Candidate examples:

```text
source / process / destination / data / store / trustBoundary
```

or another fixed architecture/threat-method slot set.

### Test

Facial access can be made to look DFD-like, but the order corpus needs request/result, correlation, reservation lifecycle, responsibility, atomicity, compensation and physical handoff semantics that do not fit one fixed DFD tuple without distortion.

A domain-specific slot set would also violate the closed method-neutral boundary.

### Disposition

**REJECTED AS UNIVERSAL CORE.** Domain/method projections may derive such slots later.

## 6. Lower bound 1 - explicit semantic operator

A set of participants and roles is still ambiguous unless the proposition says what semantic assertion connects them.

Therefore every proposition needs an explicit **method-neutral semantic operator key**.

This microstep does not accept a verb list. It accepts only the structural responsibility:

```text
BAProposition.semanticOperator = exactly 1 explicit semantic key
```

The key must eventually be stable enough for mechanical selection and comparison, but whether canonical operators are modeled as controlled symbols, registry entries or another representation remains later BA2 work.

No `Relation` or `Action` BAE identity family is created.

## 7. Lower bound 2 - role-bound n-ary participation

A BAProposition must support one or more role-bound semantic terms:

```text
participation 1..*
    role 1
    term 1
```

At least one term must be a `BAReferent`, preserving the BA1 definition that a proposition is an assertion about referent identities.

A term may be a typed local value when cross-proposition semantic identity is not required. If a condition/state/value must itself be reused, compared or constrained across propositions, BA1 already provides the promotion path: represent that project meaning as a `BAReferent`.

This form permits unary, binary and higher-arity propositions. N-ary support is therefore a **capability**, not a requirement that every proposition have more than two participants.

### Disposition

**FORCED CANDIDATE.**

## 8. Lower bound 3 - scoped semantic modifiers

The reviewed clauses show that the truth/meaning of an assertion may depend on:

- condition/applicability;
- state;
- failure/completion rule;
- realization;
- atomicity/concurrency;
- idempotency;
- polarity/negative outcome.

Treating this as an untyped prose suffix would defeat the purpose of Base Analysis. But forcing every local qualifier to become a `BAReferent` would over-reify project meaning.

BA2-T1 therefore accepts a weaker structural requirement:

> a BAProposition must support explicit, proposition-scoped semantic modifiers without requiring those modifiers to become BAE identities.

The exact modifier schema is intentionally **OPEN**. BA2-T2 must test whether modifiers are best represented through role-bound values/referents, normalized qualifier records, separate propositions about reusable referents, or a constrained combination.

### Disposition

**REQUIRED CAPABILITY / MATERIAL FORM OPEN.**

## 9. Referent classification versus participation role

The BA1 closure allowed method-neutral semantic classifications without creating subtype roots. BA2-T1 asks whether those classifications can instead be reconstructed from proposition roles.

They cannot reliably be collapsed.

Role is contextual; classification is reusable semantic characterization of the referent. `RecognitionCapture` does not cease to be information/resource-like project meaning because one proposition uses it as an acceptance object. `PaymentProviderContract` does not become a destination type merely because an interaction proposition points toward it/provider context.

If a method-neutral consumer must know reusable semantic kind but Base Analysis omits it, the consumer would have to reread raw prose or invent its own taxonomy, weakening shared semantics.

### Disposition

```text
classification derived only from roles         REJECTED
explicit reusable classification capability     SUPPORTED
exact classification vocabulary/cardinality     DEFERRED
```

This does not reopen BA1: classification remains cheaper than a first-class split.

## 10. Behavior/action identity test

BA1 already decided that a behavior/event may be a `BAReferent` when independently reused. BA2-T1 tests whether proposition structure now forces a dedicated `Action` family.

It does not.

A delivery behavior that must be referenced by multiple constraints may be a BAReferent. A proposition's semantic operator still expresses the assertion currently being made. These are different responsibilities:

```text
reusable project behavior meaning  -> BAReferent
asserted semantic relation/action  -> BAProposition operator + participation
```

### Disposition

**NO BA1 REOPEN.** No third identity family is forced.

## 11. Concrete facial-access rendering

The following labels are illustrative only:

```text
P-FR34-DELIVERY
semanticOperator: transfer
participation:
  source              -> CameraSubsystem
  destination         -> RecognitionProcessor
  information         -> RecognitionCapture
  correlationContext  -> RecognitionRequest
scopedModifier:
  completion          -> incomplete delivery != successful completion
```

This is already richer than SPO but still smaller than a domain-specific DFD ontology.

If `FR-3.4 delivery` is independently reused by specialized constraints, its project meaning may additionally be represented as a BAReferent and participate explicitly in those propositions. The assertion identity `P-FR34-DELIVERY` does not become the project-semantic target.

## 12. Concrete order-fulfillment rendering

Consider the atomic reservation requirement. One proposition must be able to expose, without synthetic document/tool types:

```text
semanticOperator: reserve / allocate   [illustrative]
participation:
  executor     -> InventoryService
  request      -> ReservationRequest
  correlation  -> OrderEvaluation
  created      -> Reservation
  result       -> ReservationResult
  affected     -> InventoryBalance
scopedModifier:
  atomicity    -> all requested lines or none
  concurrency  -> competing reservation cannot consume frozen quantity
```

The exact canonical roles and operator names are not accepted here. The example demonstrates only why the structure must be role-bound and able to carry scoped semantics.

## 13. Bounded consumer check

The prior bounded STRIDE-oriented consumer needs behavior, source, destination, information, correlation, responsibility/externality, realization, failure and constraints.

BA2-T1's candidate can expose those semantics without importing STRIDE categories:

- referents carry stable project-semantic identity and reusable classification where needed;
- propositions carry explicit operator semantics;
- role bindings expose participation mechanically;
- scoped modifiers preserve conditions/failure semantics;
- method-specific categories remain in the consumer.

### Result

**STRUCTURAL PASS / VOCABULARY NOT YET CLOSED.**

## 14. Falsification summary

- Pure binary SPO as universal core: **REJECTED**.
- Binary proposition as a valid special case: **SUPPORTED**.
- Anonymous positional n-ary tuple: **REJECTED**.
- Explicit role-bound n-ary participation: **FORCED CANDIDATE**.
- Fixed domain/method slot model: **REJECTED**.
- Explicit semantic operator key: **FORCED CANDIDATE**.
- Exhaustive operator list: **DEFERRED**.
- Scoped modifier capability: **REQUIRED / ENCODING OPEN**.
- Free-text modifier bag: **REJECTED**.
- Participation/Role/Qualifier as BAE identity families: **NOT FORCED**.
- Referent classification reconstructed only from roles: **REJECTED**.
- Explicit method-neutral classification capability: **SUPPORTED / VOCABULARY OPEN**.
- Dedicated Action/Event/Relation identity family: **NOT FORCED**.
- BA1 reopen: **NOT TRIGGERED**.

## 15. Provisional candidate

```text
BAProposition
|- identity                         [BA1 CLOSED]
|- semanticOperator                1
|- participation                   1..*
|    |- role                       1
|    `- term                       1
`- scopedModifier                  0..* [capability required; exact shape open]
```

Additional constraints:

1. at least one participation term is a `BAReferent`;
2. n-ary participation is supported but not mandatory for every proposition;
3. role semantics are explicit, not positional;
4. semantic operator and role vocabularies are method-neutral and still open;
5. reusable referent classification is separate from contextual participation role;
6. no new BAE identity family is introduced.

## 16. What BA2-T1 does not decide

BA2-T1 does not decide:

- final operator vocabulary;
- final participation-role vocabulary;
- operator-role compatibility matrix;
- role cardinalities;
- exact qualifier/modifier representation;
- logical composition/negation expression language;
- canonical classification vocabulary;
- provenance/source fields;
- views/projections;
- lexical synonyms;
- threat-method mappings.

## 17. Next authorized microstep

Execute only:

> **BA2-T2 - semantic operator, participation-role and scoped-modifier vocabulary pressure test.**

BA2-T2 must attempt to derive the smallest reusable method-neutral semantic vocabulary from the two corpora and bounded consumer while keeping lexical synonyms, method-specific categories and provenance out of scope.

Do not close BA2 merely because the structural lower bound survives this trial.
