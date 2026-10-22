---
type: BAOperatorGuide
schemaVersion: '0.1'
id: BA2-OP-PRODUCE
title: 'Produce'
reviewStatus: reviewed
---

# BA2-OP-PRODUCE — Produce

## Meaning

`produce` asserts that an identified actor or capability makes at least one identified result available. An input belongs to the same assertion only when its use is explicitly governed. The assertion does not describe how the result is computed or what happens to it afterward.

## When to use

- Identify one actor/capability responsible for making the result available.
- Identify at least one result; input is optional.
- Reuse the same BAReferent where the governed meaning of a result or input is unchanged.
- Group multiple inputs or results only when they belong to the same governed production fact.

## When not to use

- Do not infer `produce` from mere data availability, component adjacency, or pipeline order.
- Do not invent an actor, result, or optional input to satisfy the signature.
- Do not infer creation, transfer, storage, algorithm, success, or failure semantics.
- If evidence cannot identify an actor and a result, record insufficient evidence instead of asserting production.

## Disambiguation

<!-- -->

## Canonical contract

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
    llmInstruction: 'Read BA2-OP-PRODUCE. Verify the required role against documented evidence; never invent referents or roles.'
  cardinality:
    code: BA-ROLE-CARDINALITY
    severity: error
    guideSection: Canonical contract
    message: 'Role {role} violates the declared produce cardinality.'
    llmInstruction: 'Read BA2-OP-PRODUCE. Check whether the governed assertion requires a split; do not guess.'
  unknownRole:
    code: BA-ROLE-UNKNOWN
    severity: error
    guideSection: Canonical contract
    message: 'Role {role} is not part of the produce signature.'
    llmInstruction: 'Read BA2-OP-PRODUCE. Use only the declared role keys; do not silently change the operator.'
```

## Valid examples

**Valid — result without governed input:**

```text
BAP-EX-PRODUCE-01 - produce
  actor    -> DocumentAuthoring
  result   -> Document
  polarity = affirmative
```

**Valid — multiple results in one governed production:**

```text
BAP-EX-PRODUCE-02 - produce
  actor    -> RiskAssessment
  input    -> Measurement
  result   -> RiskScore
  result   -> RiskConfidence
  polarity = affirmative
```

## Invalid examples

**Missing actor:**

```text
BAP-EX-PRODUCE-BAD-01 - produce
  result   -> RiskScore
  polarity = affirmative
```

**Missing result:** an actor alone does not establish a production.
