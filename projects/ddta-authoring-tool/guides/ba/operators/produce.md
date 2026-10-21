---
type: BAOperatorGuide
schemaVersion: '0.1'
id: BA2-OP-PRODUCE
title: 'Produce — structural rule candidate C5 R1'
methodStatus: candidate
reviewStatus: draft
sourceRefs:
  - methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex
---

# BA2-OP-PRODUCE — Produce — structural rule candidate C5 R1

> **CANDIDATE / NOT ACTIVE.** This operator sheet is authored from the R7
> working rebuild (chapter 8, described pages 32–38). Its structural contract
> is reviewable by the C4 BA Rule Loader but cannot execute while
> `reviewStatus: draft`. `methodStatus: candidate` is separate from executable
> rule review. A structurally valid assertion is not automatically supported
> by the project's governed evidence.

## Meaning

`produce` states the smallest governed fact that an identified actor or
capability **makes one or more identified results available**. An `input` may
participate when the same documentation explicitly governs its use in this
production. Neither the operation's computational method nor a subsequent
conveyance of the result is asserted by `produce` alone.

## When to use

Use `produce` when the source explicitly governs a production, generation,
calculation, return, emission, or other making-available of a result, and
identifies:

- Exactly one `actor`: the producer/capability to which the fact is attributed.
- One or more `result` BAReferents made available by that actor.
- Zero or more `input` BAReferents, **only** when the source connects their use
  to the same governed act of production.

Reuse existing BAReferent identities for unchanged meanings, particularly when
a result subsequently appears as `transfer.content` or as a later operation's
input. Multiple results or inputs belong in one proposition only when the
source ties them to one governed production fact.

## When not to use

Do not claim `produce` when the source establishes only that a datum exists,
that a component has access to it, or that a pipeline contains ordered stages.
Do not manufacture an actor or a result to satisfy formal cardinalities.
Do not add an `input` merely because the datum is available upstream or is
plausibly consumed by the implementation.

If the actor or every result cannot be identified from governed evidence,
report **INSUFFICIENT EVIDENCE / NOT SPECIFIED** and request human review.
An absent optional input is not, by itself, an evidence gap or a cardinality
violation.

## Disambiguation

<!-- R7 chapter 8 leaves its operator-comparison subsection unfinished.
Do not manufacture formal cross-operator distinctions. At minimum,
produce is not a claim of transfer, persistence, or ex-novo creation. -->

## Canonical contract

The `yaml ba-rule` block is a candidate structural encoding of the R7 chapter
8 signature. Its DSL names, cardinalities, and diagnostic contract use the
same generic grammar as the reviewed `transfer` rule. The rule is **not
executable** while this guide has `reviewStatus: draft`.

```yaml ba-rule
contractVersion: '0.1'
semanticOperatorKey: produce
roles:
  actor: {min: 1, max: 1}
  input: {min: 0, max: unbounded}
  result: {min: 1, max: unbounded}
constraints: []
diagnostics:
  missingRole:
    code: BA-ROLE-MISSING
    severity: error
    guideSection: Canonical contract
    message: 'Required produce role {role} is missing.'
    llmInstruction: >
      Read BA2-OP-PRODUCE, especially Canonical contract and When not to use.
      Inspect the proposition and the governed documentation. Identify the
      required actor or result only if the source supports it; otherwise report
      INSUFFICIENT EVIDENCE. Never invent a BAReferent or add an implicit input.
  cardinality:
    code: BA-ROLE-CARDINALITY
    severity: error
    guideSection: Canonical contract
    message: 'Role {role} violates the declared produce cardinality.'
    llmInstruction: >
      Read BA2-OP-PRODUCE and review the actor, inputs, and results as one
      governed production fact. Explain the mismatch. Propose a split only
      if the source establishes distinct production facts; do not silently
      merge producers or invent missing meaning.
  unknownRole:
    code: BA-ROLE-UNKNOWN
    severity: error
    guideSection: Canonical contract
    message: 'Role {role} is not part of the produce signature.'
    llmInstruction: >
      Read BA2-OP-PRODUCE and the recognized operator registry. Determine
      whether the author intended a different source-supported proposition.
      Do not reclassify a role or substitute operators automatically.
```

**Shared BAProposition attributes** are outside the operator's roles:
`polarity` is mandatory (`affirmative` or `negative`) and is never inferred.
`negative` means an expressly governed denial of the production assertion,
not a missing actor, result, or evidence. Proposition-level `temporalScope`
is optional; when used, the C4 engine recognizes its proposed syntax but
reports the temporal check as **INCOMPLETE**, pending a reviewed temporal
contract. `condition` is discussed by R7 but is not supported by the C4
shared parser/contract; no implicit support is claimed.

## Invariants

- A formally valid `produce` has **exactly one** `actor` and **at least one**
  `result`; `input` is optional and unbounded when source-supported.
- The role key `result` identifies a participant in this production; it is
  not an intrinsic global type of its BAReferent.
- Multiple results describe one production only when the documentation
  binds them to the same actor and same governed assertion.
- An unchanged output keeps its BAReferent identity across later transfer or
  consumption; neither file placement nor a variable name creates a new one.
- Explicit negative polarity requires evidence of a negated production.
- No computational algorithm, model, threshold, storage, ownership, network
  transfer, destination, protocol, serialization, success, failure, retry, or
  ex-novo creation is entailed by this operator alone.
- The engine can validate declared roles and cardinalities, but not source
  sufficiency, referent identity resolution, or semantic acceptance.

## Diagnostics

`BA-ROLE-MISSING`, `BA-ROLE-CARDINALITY`, and `BA-ROLE-UNKNOWN` are structural
errors, with their human messages and LLM correction instructions declared
inside this guide's `yaml ba-rule` block. When eventually activated, the
validator must link each error to the affected proposition and the
`Canonical contract` guide section.

Shared errors including `BA-POLARITY-MISSING` and local proposition ID
collisions are controlled by the common BAProposition contract, not by
`produce`'s roles. A recognized `produce` proposition currently yields
`BA-OP-UNCOVERED` and an INCOMPLETE result because this guide is still draft.
A time-qualified proposition additionally requires an unfinished temporal
validation; neither condition permits a false BA PASS.

## Valid examples

**Production without explicitly governed input:**

```text
BAP-EX-PRODUCE-01 - produce
  actor    -> DDTADocumentAuthoring # BAR-EX-AUTHOR
  result   -> DDTADocument          # BAR-EX-DOCUMENT
  polarity = affirmative
```

Evidence assumption: the DDTA authoring capability makes the DDTA document
available. No additional input may be added solely to complete the shape.

**One production with two governed results and one governed input:**

```text
BAP-EX-PRODUCE-02 - produce
  actor    -> RiskAssessmentComputation # BAR-EX-RISK-ACTOR
  input    -> MeasurementRecord         # BAR-EX-MEASUREMENT
  result   -> RiskAssessment            # BAR-EX-ASSESSMENT
  result   -> AssessmentConfidence      # BAR-EX-CONFIDENCE
  polarity = affirmative
```

Evidence assumption: the same governing statement requires the capability
to use the measurement record and make both results available. Merely
mentioning multiple results in different contexts would not justify merging.

**Explicitly prohibited production:**

```text
BAP-EX-PRODUCE-03 - produce
  actor    -> ExportService    # BAR-EX-EXPORT
  result   -> SensitiveReport  # BAR-EX-REPORT
  polarity = negative
```

Evidence assumption: an explicit rule prohibits that service from producing
that report. This is not a representation of unavailable evidence.

## Invalid examples

**Missing producer:**

```text
BAP-EX-PRODUCE-BAD-01 - produce
  result   -> RiskAssessment
  polarity = affirmative
```

Expected structural diagnostic after rule activation: `BA-ROLE-MISSING`
for `actor`.

**Missing result:**

```text
BAP-EX-PRODUCE-BAD-02 - produce
  actor    -> RiskAssessmentComputation
  polarity = affirmative
```

Expected structural diagnostic: `BA-ROLE-MISSING` for `result`.

**Two producers in one proposition:**

```text
BAP-EX-PRODUCE-BAD-03 - produce
  actor    -> StageA
  actor    -> StageB
  result   -> ResultX
  polarity = affirmative
```

Expected structural diagnostic: `BA-ROLE-CARDINALITY` for `actor`.

**Unsupported inference:** the statement “Stage B has DataX available” does
not establish that Stage B produced DataX. Likewise, the availability of
DataX upstream is insufficient to assert its use as a `produce.input`.

## Source reconciliation

- **Working methodological source: R7, chapter 8, described pages 32–38.**
  These pages specify the smallest governed production fact, actor/input/result
  cardinalities, referent continuity, evidence boundaries, extraction checks,
  LLM guidance, and the authoring examples.
- **R7 page 36, DermaTriage Stage 3:** `HistoricalCaseRetrieval` produces
  `RetrievedHistoricalCaseContext`, using `ClinicalDescription` only where
  source-supported. These identities are an example, not a new universal role
  or algorithmic requirement.
- **R7 page 38:** the comparison section is unfinished; `Disambiguation`
  is deliberately left without new unsupported cross-operator rules.
- **Common BAProposition rule:** `polarity` is required, while `temporalScope`
  is optional with currently unverified semantics. `condition` support is not
  introduced by this operator sheet.
- **Scope boundary:** Mermaid shapes and projection rules are excluded from
  this semantic operator guide.

**Activation gate:** review this sheet's semantics and its executable DSL,
then explicitly set `reviewStatus: reviewed` in a separate checkpoint.
Do not promote `methodStatus: candidate` automatically. A document-format
PASS alone does not activate the guide.
