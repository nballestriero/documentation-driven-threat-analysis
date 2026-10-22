---
type: BAOperatorGuide
schemaVersion: '0.1'
id: BA2-OP-TRANSFER
title: 'Transfer'
reviewStatus: reviewed
---

# BA2-OP-TRANSFER — Transfer

## Meaning

`transfer` asserts that one or more identified contents are conveyed from one identified source to one or more identified destinations. It is a governed conveyance, not merely a structural connection or an execution sequence.

## When to use

- Identify exactly one source, at least one destination, and at least one content.
- Reuse the same BAReferent for content whose governed meaning remains unchanged across production, transfer, and consumption.
- Add optional `behavior` only when the transfer segment has an independently governed identity.
- Combine contents or destinations only when the same governed assertion supports them.

## When not to use

- Do not infer a transfer from component adjacency, input usage, an API mention, or processing order alone.
- If source, destination, or content is not established, record insufficient evidence instead of inventing a role.
- Do not infer protocol, medium, persistence, encryption, successful delivery, retries, ownership, or storage.

## Disambiguation

<!-- -->

## Canonical contract

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
    llmInstruction: 'Read BA2-OP-TRANSFER. Verify the required role against documented evidence; never invent referents or roles.'
  cardinality:
    code: BA-ROLE-CARDINALITY
    severity: error
    guideSection: Canonical contract
    message: 'Role {role} violates the declared transfer cardinality.'
    llmInstruction: 'Read BA2-OP-TRANSFER. Check whether the governed assertion requires a split; do not guess.'
  unknownRole:
    code: BA-ROLE-UNKNOWN
    severity: error
    guideSection: Canonical contract
    message: 'Role {role} is not part of the transfer signature.'
    llmInstruction: 'Read BA2-OP-TRANSFER. Use only the declared role keys; do not silently change the operator.'
```

## Valid examples

**Valid — governed conveyance:**

```text
BAP-EX-TRANSFER-01 - transfer
  source      -> Acquisition
  destination -> Evaluation
  content     -> Measurement
  polarity    = affirmative
```

**Valid — explicitly prohibited conveyance:**

```text
BAP-EX-TRANSFER-02 - transfer
  source      -> SystemA
  destination -> SystemB
  content     -> SensitiveData
  polarity    = negative
```

## Invalid examples

**Missing content:**

```text
BAP-EX-TRANSFER-BAD-01 - transfer
  source      -> SystemA
  destination -> SystemB
  polarity    = affirmative
```

**Unjustified source:** a downstream component's use of data does not identify the source of transfer.
