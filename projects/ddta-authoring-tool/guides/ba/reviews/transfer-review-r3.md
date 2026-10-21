---
type: BAOperatorGuide
schemaVersion: '0.1'
id: BA2-OP-TRANSFER
title: 'Transfer — operator review draft R3'
methodStatus: historical
reviewStatus: draft
sourceRefs:
  - methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex
  - methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex
---

# BA2-OP-TRANSFER — Transfer — operator review draft R3

> **OBSOLETE HISTORICAL REVIEW / NOT EXECUTABLE.** R3 is superseded
> and MUST NOT be used as semantic authority for BA operator decisions.
> **REVIEW DRAFT / NOT EXECUTABLE.** This document belongs to `reviews/`, not
> `operators/`. Its Markdown format can be checked against `BAOperatorGuide`,
> but its semantic rules and machine-readable contract require explicit review
> before they can become active BA validation rules. `methodStatus: historical`
> is retained only for historical traceability and does not approve this
> draft or imply executable validation coverage.

## Meaning

`transfer` represents a **governed conveyance** of one or more identified
contents from one identified source to one or more identified destinations.
Its smallest governed semantic fact is that *content X is conveyed from A to B*.
A transfer is not merely an architectural connection, an execution sequence,
or an inferred dependency between adjacent components.

## When to use

Use `transfer` only when the documentation supports each required participant:

- Exactly one `source`, the governed origin of the conveyance.
- At least one `destination`, the governed receiver of the content.
- At least one `content`, the meaning-bearing item being conveyed.

Reuse an existing BAReferent for content that retains the same governed meaning
between production, transfer, and consumption. Introduce an optional `behavior`
BAReferent only if the transfer segment itself must be independently referenced,
constrained, realized, reviewed, or compared. Use multiple destinations or
contents in one proposition only when the same governed assertion supports them.

## When not to use

Do not infer a transfer solely from a component receiving an input, from a
mentioned API, from two components shown together, or from the ordering of
processing stages. If a source, destination, or content cannot be established,
record **INSUFFICIENT EVIDENCE / NOT SPECIFIED** for human review rather than
inventing a role assignment.

Do not infer transport protocol, medium, network hops, synchronization,
delivery success, encryption, retries, acknowledgment, persistence, ownership,
storage, service consumption, or failure semantics from the transfer assertion.

## Disambiguation

<!-- Optional. R7 contains an unfinished subsection on comparisons with other
operators. Do not introduce unreviewed distinctions simply to fill this field. -->

## Canonical contract

The following block is a **candidate machine-readable encoding** of the
source-supported signature. The future BA Rule Loader must check this grammar
and its diagnostics before enabling the operator. In particular, `unbounded`
and the diagnostic keys are proposed DSL syntax, not methodological terms.

```yaml ba-rule
contractVersion: '0.1'
semanticOperatorKey: transfer
roles:
  behavior: {min: 0, max: 1}
  source: {min: 1, max: 1}
  destination: {min: 1, max: unbounded}
  content: {min: 1, max: unbounded}
constraints: []
diagnostics:
  missingRole:
    code: BA-ROLE-MISSING
    severity: error
    guideSection: Canonical contract
    message: 'Required transfer role {role} is missing.'
    llmInstruction: >
      Read BA2-OP-TRANSFER, especially Canonical contract and When not to use.
      Inspect the affected BAProposition and its governed source evidence.
      Suggest a role assignment only when the evidence supports it. Otherwise
      report INSUFFICIENT EVIDENCE. Do not invent BAReferents.
  cardinality:
    code: BA-ROLE-CARDINALITY
    severity: error
    guideSection: Canonical contract
    message: 'Role {role} violates the declared transfer cardinality.'
    llmInstruction: >
      Read BA2-OP-TRANSFER and examine the proposition and its evidence.
      Explain the cardinality mismatch. Suggest splitting or changing a
      proposition only when the source warrants a semantic distinction.
  unknownRole:
    code: BA-ROLE-UNKNOWN
    severity: error
    guideSection: Canonical contract
    message: 'Role {role} is not part of the transfer signature.'
    llmInstruction: >
      Read BA2-OP-TRANSFER and the valid-operator registry. Check the intended
      meaning and suggest only a source-supported, canonically defined role.
      Do not invent an operator or silently rename the role.
```

**Shared BAProposition contract (not an operator role).** `polarity` applies to
all BAPropositions and is not repeated in the `roles` mapping. The agreed
values are `affirmative` and `negative`: the latter requires an explicitly
governed negation of this exact transfer claim. Missing evidence is **not**
a negative transfer. No implicit polarity default is authorized; the precise
shared machine rule remains a separate authoring/validation step.

## Invariants

- Each formally valid `transfer` proposition has exactly one `source`, at
  least one `destination`, and at least one `content`.
- A role key is scoped to this operator: `source` means an origin in the
  transfer assertion, not an intrinsic global type of the BAReferent.
- An optional `behavior` identifies the transfer segment, not its content or
  either endpoint; it does not replace any required role.
- Different syntactic locations do not, by themselves, create distinct
  BAReferent identities for semantically unchanged content.
- Explicit negation (`polarity = negative`) differs from lack of evidence.
- Role names and cardinalities are automatically checkable. Whether the
  documentation truly supports a conveyance, an optional `behavior`, or an
  identity reuse remains subject to semantic review.

## Diagnostics

The candidate codes `BA-ROLE-MISSING`, `BA-ROLE-CARDINALITY`, and
`BA-ROLE-UNKNOWN` are declared within the rule block above; their diagnostic
messages and LLM instructions must be read from the guide rather than
hard-coded separately into the Python engine. A future diagnostic must link
to the relevant rule ID and section, identify the affected source location
when available, and distinguish a formal violation from unresolved evidence.

Shared diagnostics, such as an unrecognized `semanticOperatorKey` or missing
BAProposition-level `polarity`, belong to the common BA engine and operator
registry, not to the `transfer` rule definition.

## Valid examples

**Affirmative transfer (example only; referent identities must be established):**

```text
BAP-EX-TRANSFER-01 - transfer
  source      -> MeasurementAcquisition  # BAR-EX-ACQUISITION
  destination -> EvaluationEngine        # BAR-EX-EVALUATION
  content     -> MeasurementRecord       # BAR-EX-RECORD
  polarity    = affirmative
```

Evidence assumption: the source states that the acquisition subsystem
conveys the measurement record to the evaluation engine.

**Explicitly prohibited transfer:**

```text
BAP-EX-TRANSFER-02 - transfer
  source      -> SystemA   # BAR-EX-A
  destination -> SystemB   # BAR-EX-B
  content     -> DataX     # BAR-EX-X
  polarity    = negative
```

Evidence assumption: the governed documentation explicitly states that
SystemA must not convey DataX to SystemB. This is not an example of unknown
or absent evidence.

## Invalid examples

**Missing required content:**

```text
BAP-EX-TRANSFER-BAD-01 - transfer
  source      -> SystemA
  destination -> SystemB
  polarity    = affirmative
```

Expected candidate diagnostic: `BA-ROLE-MISSING` (`content`).

**Two sources in a single proposition:**

```text
BAP-EX-TRANSFER-BAD-02 - transfer
  source      -> SystemA
  source      -> SystemC
  destination -> SystemB
  content     -> DataX
  polarity    = affirmative
```

Expected candidate diagnostic: `BA-ROLE-CARDINALITY` (`source`).

**Source evidence states only “Stage B uses X”:** an upstream `source`
cannot be inferred from that statement alone. This is a semantic evidence
gap, not permission to fill the role with a plausible upstream stage.

**Unjustified `behavior`:** providing a syntactically valid behavior role
does not establish the independent transfer identity's semantic necessity.

## Source reconciliation

- **Historical R3 text (OBSOLETE, NOT AUTHORITY):** the operator's signature is `behavior [0..1]`,
  `source [1]`, `destination [1..*]`, and `content [1..*]`; its `behavior`
  refinement is explicitly limited to transfer. Relevant parts include
  “transfer — qualcosa viene trasferito …”, “Ruoli e cardinalità principali”,
  and “Il delta BA2 R3 / transfer.behavior”. These source titles are retained
  as literal locators, not as the language of the new guide.
- **Rebuild R7, chapter 7, described pages 23–29:** confirms that signature
  and expands on governed evidence, content identity continuity, negative
  assertions, and controlled LLM-assisted authoring. The rebuild is a
  review source and does not automatically promote new rules.
- **Identified R7 unfinished text:** “Discriminazioni con altri costrutti”
  contains a placeholder; the new `Disambiguation` section remains optional.
- **Excluded R7 content:** graphical rendering and projection rules
  belong to a separate guide. None are part of the BA operator contract.
- **Items requiring future review:** formal grammar of the YAML DSL;
  supported `constraints`; shared proposition fields including `polarity`;
  links to operator registries; and the authority/revision workflow.

**Activation gate:** after joint review and explicit approval, produce
`guides/ba/operators/transfer.md` from this draft, validate its complete rule
contract, and enable it through the generic BA Rule Loader. Passing the
Markdown document schema alone does not activate or approve the operator.
