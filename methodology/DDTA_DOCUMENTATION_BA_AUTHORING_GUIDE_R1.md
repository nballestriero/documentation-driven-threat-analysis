# DDTA Documentation and Base Analysis Authoring Guide - R1

**Status:** R24 WORKING AUTHORING CONTRACT  
**Baseline:** `2be2c1749e2b29a3afa8c8040ce4c51be90b65d1`  
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

MRs normally govern:

- stable responsibility;
- intent/value;
- context;
- scope boundary;
- stakeholders;
- macro assumptions/constraints;
- direct MR dependencies.

MRs should not normally govern the detailed algorithm or branch logic used to construct a result.

### BA at MR level

Extract only the available macro semantics, for example:

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

Represent the policy/commitment that is explicitly governed.

Do not infer a complete operational `IF / THEN / ELSE` mapping unless the Decision itself explicitly governs that complete mapping and the documentation model intentionally places that detail there. In the current DDTA hierarchy, operational result construction is expected at FR level.

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

### 5.2 Testability check

For an FR containing a decision rule, a reviewer should be able to derive the relevant input combinations and expected outcomes without inventing project meaning.

If the FR leaves a branch unspecified, the test expectation for that branch is also unspecified. Do not silently complete it.

## 6. Base Analysis after FR

When an FR explicitly governs result construction, BA may add a `decisionRule` proposition in addition to the earlier macro proposition.

Example:

```text
produce
  actor  -> ControlledAreaAccess
  input  -> AccessAuthorizationState
  input  -> IdentityVerificationEvidence
  result -> AccessDecision
```

followed later by:

```text
decisionRule
  actor  -> ControlledAreaAccess
  input  -> AccessAuthorizationState
  input  -> IdentityVerificationEvidence
  result -> AccessDecision

  IF
    AccessAuthorizationState = VALID
    AND
    IdentityVerificationEvidence = POSITIVE
  THEN
    AccessDecision = ALLOW
  ELSE
    AccessDecision = NOT_ALLOW
```

The second proposition adds operational detail. It does not replace the first.

## 7. Do not misuse other BA semantics

### `condition`

Use for a proposition-local applicability/guard condition.

Do not use it to hide `IF / THEN / ELSE` result construction inside `produce`.

### `constrain`

Use for a real reusable/queryable restriction.

Do not use a free-text constraint blob merely because BA lacks a more specific representation.

### `dependOn`

Use for genuine prerequisites/dependencies.

Example:

```text
C dependOn A
C dependOn B
```

This is analytically useful because loss or compromise of B may propagate impact to C even when B looks non-critical in isolation.

`dependOn` therefore supports dependency paths, availability propagation and indirect criticality analysis. It is not a replacement for decision logic.

### `classify`

Keep classification as proposition semantics. Independent classification identity is useful because later method-neutral taxonomies can expand or project the same referent while retaining provenance and change history.

## 8. Documentation-to-BA detail rule

Use this review question at every step:

> Is this BA detail explicitly governed by the documentation at this level, or am I pulling a lower-level design/functional detail upward because the analysis model can express it?

If it is the second case, stop.

Expected progression:

```text
MR BA
  referents + macro relations

Decision BA
  explicit policy/commitment semantics

FR BA
  operational behavior, including decisionRule when governed

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

For the current R24 facial-access branch:

- MR-0001 already supports a `produce` proposition for `AccessDecision`;
- ADR-0001 governs a conjunctive access policy;
- the current FR wording must be reviewed before materializing a complete `decisionRule`, because BA must not infer `MUST ALLOW` on the positive branch unless that obligation is explicitly governed;
- the project document is therefore intentionally unchanged by this guide update.

## 12. Working acceptance rule

A documentation/BA representation is acceptable when it is:

1. easy for project authors and reviewers to read;
2. faithful to the governed abstraction level;
3. independently testable at FR level where applicable;
4. normalized enough for later analyses to consume without raw-prose reconstruction;
5. no more complex than the project meaning requires.
