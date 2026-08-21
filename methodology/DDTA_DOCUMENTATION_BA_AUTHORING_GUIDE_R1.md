# DDTA Documentation and Base Analysis Authoring Guide - R1

**Status:** R24 WORKING AUTHORING CONTRACT  
**Current refinement baseline:** `0fc9ea67eb13a47d0acd2ad36a174bcf6e6aa237`
**R24 checkpoint:** `DDTA_R24_DECISION_RULE_CHECKPOINT.md`
**Purpose:** keep project documentation simple to write/read while preserving enough normalized meaning in Base Analysis for test derivation and later analysis.

## 1. Core rule

Write only the detail appropriate to the current documentation level.

Base Analysis mirrors governed meaning; it must not invent detail earlier than the documentation.

```text
Problem framing
  -> what problem and boundary exist?

MacroRequirement
  -> what stable responsibility/result is needed?

Decision
  -> what significant policy/strategy/boundary choice narrows the MR?

FunctionalRequirement
  -> what operational behavior MUST occur and what observable result follows?

Base Analysis
  -> normalize only the meaning already governed at those levels

Tests / analyses
  -> consume the normalized FR/BA semantics
```

## 2. Keep project documentation readable

Project documentation is for project readers first.

Rules:

- use short domain-readable prose;
- do not expose BA implementation mechanics in project documentation;
- do not add research commentary to project documentation;
- do not force truth tables or graph syntax into an MR or Decision merely because tooling can consume them;
- use normative keywords in English (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`); do not translate keywords;
- prefer one clear operational rule over several equivalent explanatory paragraphs.

## 3. MacroRequirement authoring

Question:

> Which stable macro responsibility is governed, which result/value must it contribute, which inputs or other responsibilities are relevant, and what is outside its scope?

MRs normally govern stable responsibility, intent/value, context, scope boundary, stakeholders, macro assumptions/constraints and direct MR dependencies.

MRs should not normally govern the detailed algorithm or branch logic used to construct a result.

### BA at MR level

Extract only available macro semantics:

```text
produce
  actor  -> ControlledAreaAccess
  input  -> AccessAuthorizationState
  input  -> IdentityVerificationEvidence
  result -> AccessDecision
```

Do not add a `decisionRule` merely because the result will eventually require one.

## 4. Decision authoring

Question:

> Which significant project commitment narrows the MR, and what consequences follow from that choice?

A Decision can govern policy, strategy, responsibility boundary, convention or technology/architecture choice.

A Decision should not be inflated with implementation detail merely to make later BA easier.

### BA at Decision level

Represent the policy/commitment explicitly governed.

A Decision may also govern a semantic distinction or allowed domain that later FRs must preserve. BA may represent such a domain with `constrain` when the source actually governs it.

Do not infer a complete operational `IF / THEN / ELSE` mapping unless the documentation explicitly governs that mapping. In the current DDTA hierarchy, detailed result construction is normally expected at FR level.

## 5. FunctionalRequirement authoring

Question:

> Given the parent Decision and applicable inputs/conditions, what MUST the responsible capability do and what observable result MUST follow?

An FR should be independently assessable and should naturally support test-case derivation.

### 5.1 When the result depends on conditions

Use a direct decision form when it is the clearest way to state the behavior:

```text
IF <condition>
THEN <subject> MUST <observable result>
ELSE <subject> MUST <alternative observable result>
```

Conditions may use ordinary readable conjunction/disjunction:

```text
IF A AND B
THEN ...
ELSE ...
```

Do not split one coherent decision into one FR per truth-table row unless the behaviors are independently changeable responsibilities.

### 5.2 When the FR governs only the allowed semantic outcomes

An FR does not need to invent the algorithm that selects an outcome merely to be testable.

For example, it may govern:

```text
IdentityVerificationEvidence correspondence MUST be one of:
  TRUE
  FALSE
  UNKNOWN

TRUE means the evidence supports correspondence.
FALSE means the evidence supports non-correspondence.
UNKNOWN means the evidence supports neither conclusion sufficiently.
```

while leaving thresholds, model scores and technical selection rules to later governed detail.

This still supports useful tests: produced evidence must expose one governed outcome, and an unsupported fourth outcome is non-compliant.

### 5.3 Testability check

A reviewer should be able to derive expected observable obligations without inventing project meaning.

For a `decisionRule`, derive relevant input combinations and expected outcomes.

For an allowed vocabulary, verify that observed/produced semantic values belong to the governed domain and preserve the documented distinctions.

If documentation leaves a branch or selection algorithm unspecified, tests must not silently invent it.

## 6. Base Analysis after FR

Use the smallest construct matching the governed meaning.

### 6.1 Production

```text
produce
  actor  -> IdentityVerification
  result -> IdentityVerificationEvidence
```

says **what is produced**.

### 6.2 Allowed result domain

```text
constrain
  constraintTarget -> IdentityVerificationEvidence
  constraintValue
    property   -> correspondence
    vocabulary -> [TRUE, FALSE, UNKNOWN]
```

says **which governed values are allowed for a property**.

It does not say which value is present in a particular runtime occurrence and does not say how one value is selected.

### 6.3 Conditional result construction

`decisionRule` says **how governed conditions select or construct a result**, but only when the source FR actually governs the mapping represented by the rule.

The BA2 minimum shape is:

```text
decisionRule
  actor  -> <BAReferent>
  input  -> <BAReferent> [1..*]
  result -> <BAReferent>

  rule
    IF    <decisionCondition>
    THEN  <resultAssignment> [1..*]
    ELSE  <resultAssignment> [0..*]
```

An omitted `ELSE` has no implied meaning. BA must not invent a missing branch.

When a decision condition tests a governed property of a richer input referent, use the explicit property-addressed comparison shape. The current R24 verification-side pressure test uses:

```text
comparison
  referent      -> IdentityVerificationEvidence
  property      -> correspondence
  comparisonKey -> equals
  value         -> TRUE
```

This is semantically different from `IdentityVerificationEvidence = TRUE`, which would collapse the evidence object with the value of its `correspondence` property.

Do **not** use `AccessAuthorizationState.authorized = TRUE` as grounded facial-access meaning in the current R24 project. MR-0002 does not yet govern an `authorized` property, a `TRUE/FALSE` authorization vocabulary, or another normalized value structure sufficient to materialize that comparison.

The current R24 lower bound still requires `comparison.property`; the unresolved authorization representation is an open project-semantics pressure point, not a property-less counterexample.

The three constructs remain complementary:

```text
produce      -> what result exists/is made available
constrain    -> allowed governed semantic domain
decisionRule -> conditional selection/construction of a result
```
## 7. Do not misuse BA semantics

### `condition`

Use for a proposition-local applicability/guard condition.

Do not use it to hide `IF / THEN / ELSE` result construction inside `produce`.

### `constrain`

Use for a real reusable/queryable restriction.

For a finite allowed semantic domain, prefer the controlled structured form:

```text
constraintValue
  property   -> <controlled semantic key>
  vocabulary -> [<controlled typed values>]
```

Example:

```text
property   -> correspondence
vocabulary -> [TRUE, FALSE, UNKNOWN]
```

Do not repeat one `allowedValue` role for every vocabulary entry when one controlled vocabulary list preserves the meaning more clearly.

Do not use free-text `constraintValue` as a fallback for structured decision logic.

Do not infer that a vocabulary declaration assigns a runtime value or defines the algorithm selecting one.

If the vocabulary later needs independent reuse, provenance or change identity, promote it according to BA1 instead of hiding that identity inside the local list.

### `decisionRule`

Use when governed documentation states conditional result selection/construction.

When a condition tests a governed property of an input referent, state that property explicitly in `comparison`. In the current R24 lower bound `comparison.property` is required.

Do not use `IdentityVerificationEvidence = TRUE` when the governed meaning is `IdentityVerificationEvidence.correspondence = TRUE`.

Do not use `decisionRule` merely because a result has several possible values.

A vocabulary such as `[TRUE, FALSE, UNKNOWN]` does not by itself define three-valued logical operators or truth tables.

### `dependOn`

Use for genuine prerequisites/dependencies:

```text
C dependOn A
C dependOn B
```

This is analytically useful because loss or compromise of B may propagate impact to C even when B looks non-critical in isolation.

`dependOn` supports dependency paths, availability propagation and indirect criticality analysis. It is not a replacement for decision logic.

### `classify`

Keep classification as proposition semantics. Independent classification identity is useful because later method-neutral taxonomies can expand or project the same referent while retaining provenance and change history.

## 8. Documentation-to-BA detail rule

At every step ask:

> Is this BA detail explicitly governed by the documentation at this level, or am I pulling a lower-level design/functional detail upward because the analysis model can express it?

If it is the second case, stop.

Expected progression:

```text
MR BA
  referents + macro relations

Decision BA
  explicit policy/commitment/semantic-domain constraints

FR BA
  operational behavior
  allowed result domains when governed
  decisionRule only when conditional selection is governed

Specialized Requirement BA
  specialized constraints/obligations when governed
```

## 9. Analysis-value check

A BA construct is justified when it preserves meaning that an analysis can reuse without reconstructing raw prose.

Examples:

- `dependOn` -> dependency chain and propagated impact;
- `transfer` -> information movement;
- `correlate` -> binding/correlation integrity;
- `transition` -> lifecycle/state analysis;
- structured `constrain` vocabulary -> governed domain, unsupported-value detection and completeness checks;
- `decisionRule` -> decision paths, decision tables and functional test cases;
- `classify` -> later taxonomy projections.

Do not add BA structure only because it is possible to model it.

## 10. Authority and correction loop

```text
governed documentation
  -> BA reconstruction
  -> analysis / diagnostic
  -> documentation correction candidate
  -> governed review
  -> updated documentation
  -> updated BA
```

BA can expose ambiguity or missing branches. It must never silently repair project documentation.

## 11. Facial-access checkpoint

Current R24 findings:

- `MR-0001` supports the coarse `produce(... -> AccessDecision)` meaning;
- the conjunctive access-policy work and its exact operational mapping remain subject to the current project wording/FR pressure test before a complete access `decisionRule` is materialized;
- the authorization-side normalized comparison remains unresolved: current MR-0002 does not govern `AccessAuthorizationState.authorized`, a `TRUE/FALSE` authorization vocabulary, or an equivalent normalized value structure;
- the candidate verification Decision/FR under `MR-0003` preserves `IdentityVerificationEvidence.correspondence` with `[TRUE, FALSE, UNKNOWN]` without governing a selection algorithm;
- its BA candidate therefore uses `constrain` with `property -> correspondence` and `vocabulary -> [TRUE, FALSE, UNKNOWN]`;
- `UNKNOWN` is a local governed value where documented, not a general BA logical system;
- the verification-side comparison `IdentityVerificationEvidence.correspondence = TRUE` is property-addressed and semantically well-formed once the project source governs that meaning;
- the current R24 `comparison` lower bound requires `property`, while `resultAssignment` remains `target + value`;
- no property-less comparison has yet been justified by a concrete governed counterexample;
- no `valueOf`, verification `transition`, verification `classify` or verification-selection `decisionRule` is introduced merely to represent the allowed correspondence domain.
## 12. Working acceptance rule

A documentation/BA representation is acceptable when it is:

1. easy for project authors and reviewers to read;
2. faithful to the governed abstraction level;
3. independently testable at FR level where applicable;
4. normalized enough for later analyses to consume without raw-prose reconstruction;
5. no more complex than the project meaning requires.
