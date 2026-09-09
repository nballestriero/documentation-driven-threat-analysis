# OP-05 Transition State Representation Candidate R1

## Status

```text
candidateId: CMD-OP05-TRANSITION-STATE-VALUE-ADMISSION
kind: SIGNATURE_VALUE_DOMAIN_RELAXATION
normativeStatus: DEFERRED_PENDING_INTEGRATED_REVIEW
BA2MutationNow: FORBIDDEN
```

## Frozen BA2 R3

```text
transition
    subject   -> BAReferent [1]
    toState   -> BAReferent [1]
    actor     -> BAReferent [0..1]
    fromState -> BAReferent [0..1]
```

## Candidate integrated shape

```text
transition
    subject   -> BAReferent [1]
    toState   -> BAReferent | controlled typed local state value [1]
    actor     -> BAReferent [0..1]
    fromState -> BAReferent | controlled typed local state value [0..1]
```

No role removal and no cardinality change is proposed.

## Semantic roles

```text
subject
    identity whose state/lifecycle changes

actor
    independently governed identity that causes/performs the change
    may equal subject
    may differ from subject
    may be omitted
```

## State identity admission rule candidate

```text
independent state meaning reused/qualified/correlated/compared/tracked across propositions or baselines
    -> BAReferent

otherwise, when source meaning is preserved without independent identity
    -> controlled typed local state value
```

## Why this is minimal

BA1 already requires referent identity only for independently reusable project meaning. BA2 R3
already permits controlled typed local participation values generally when independent identity is
not required. The transition operator-scoped role contract is therefore a candidate for alignment
with those existing principles rather than a new ontology family.

## Positive pressure case

FR-10 supplies lifecycle meaning equivalent to:

```text
same ClassificationAdaptation
    adopted -> revoked
```

without independently forcing artificial `AdoptedState` and `RevokedState` referent identities.

## Counterexample where BAReferent remains appropriate

If a governed state is independently targeted by multiple propositions, constrained, correlated,
compared across baselines, or otherwise requires stable identity, it remains a BAReferent.

## G1–G8

```text
G1 PASS
G2 PASS
G3 PASS
G4 PASS
G5 PASS
G6 PASS
G7 PASS_WITH_SCHEMA_UPDATE
G8 PASS
```

## Integrated-review questions

1. exact schema notation for controlled state values;
2. canonicalization rules and BA5 impact;
3. projection serialization of referent-vs-local state terms;
4. migration guidance for existing transitions;
5. cross-corpus regression before BA2 R4 acceptance.
