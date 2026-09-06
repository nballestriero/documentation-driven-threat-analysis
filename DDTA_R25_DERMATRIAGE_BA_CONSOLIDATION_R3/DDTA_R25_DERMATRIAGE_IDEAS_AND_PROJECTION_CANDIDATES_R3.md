# R3 Ideas and Projection Candidates

These are **research hypotheses / future design candidates**, not current BA0–BA6
authority.

# I-01 — Data contract as analysis-enabling project meaning

A structured information artifact may need a reusable method-neutral contract such as:

```text
ClinicalDescription

required:
    shape
    borders
    color
    texture
    suspiciousCharacteristics

optional:
    ...
```

Potential future contract dimensions:

- field/component identity;
- required / optional;
- cardinality;
- allowed value/domain;
- type;
- nested structure;
- conditional presence;
- concrete realization when separately governed.

Do not adopt this schema yet. Test it against further DermaTriage evidence.

---

# I-02 — Producer / consumer / transfer contract continuity

Potential analytical chain:

```text
Capability A
    produces
DataArtifact

DataArtifact
    governed by
DataContract

Capability B
    consumes / uses DataArtifact
```

and, when crossing participants:

```text
transfer.content -> DataArtifact
```

The value of this model is that `transfer.content` would no longer be an opaque box:
a projection could dereference the artifact's governed contract.

---

# I-03 — Privacy-oriented analysis benefit

A method-neutral BA should preserve project meaning such as:

```text
DataArtifact contains field X
field X is transferred from A to B
```

A later privacy-specific analysis may then classify that field according to its own
method / legal / organizational rules.

Important separation:

```text
governed documentation
        ↓
BA data identity + contract + flow
        ↓
privacy-specific projection / interpretation
```

The BA should not silently label a field privacy-sensitive unless that classification
is itself project-governed.

This permits later questions such as:

- is this field necessary in this flow?
- should it be blocked?
- should it be minimized?
- should it be transformed/pseudonymized?
- does a boundary expose it?
- do producer and consumer agree on optional/required semantics?

---

# I-04 — BA4 candidate: Data Contract Flow View

**Status:** `PROJECTION_CANDIDATE_ONLY`

Purpose:

Generate a shallow graph focused only on data exchange, for example:

```text
[Capability / Participant A]
        |
        | DataArtifact
        |   fieldA [required]
        |   fieldB [optional]
        |   fieldC [required]
        v
[Capability / Participant B]
```

Possible projection inputs:

- participant/capability BAReferents;
- information/data BAReferents;
- `produce`;
- `transfer`;
- downstream input/consumption semantics;
- data-contract structure if the final BA representation supports it.

Potential uses:

- manual architecture review;
- privacy-oriented review;
- data minimization;
- interface consistency;
- later threat-analysis preparation.

This view must not introduce project meaning absent from the accepted BA.

---

# I-05 — Future concrete realization of a data contract

If future documentation governs a concrete JSON/API/schema representation, `realize`
may potentially express:

```text
abstract:
    DataContract

realization:
    concrete JSON/API/schema representation
```

This is only a hypothesis to test. `realize` must not be used to mean that a data
artifact merely contains a field.
