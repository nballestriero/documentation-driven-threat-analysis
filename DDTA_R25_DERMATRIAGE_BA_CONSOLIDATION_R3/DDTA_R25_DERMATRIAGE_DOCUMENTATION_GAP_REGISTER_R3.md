# DermaTriage Documentation Gap Register — R3 additions

This file records documentation insufficiency separately from methodology pressure.

## D-05 — FR-16 HIGH THRESHOLD SEMANTICS

**Source-observed fact:**

```text
HIGH threshold = 0.25
```

**Not sufficiently governed:**

- exact compared quantity;
- comparison operator (`>`, `>=`, etc.);
- complete HIGH/MEDIUM/LOW branching semantics;
- MEDIUM/LOW boundaries.

**BA consequence:**

No `decisionRule` may be materialized from the `0.25` fact alone.

**Classification:**

```text
DOCUMENTATION GAP
not methodology defect
```

---

## D-06 — FR-17 CLINICAL DESCRIPTION FORMAT COMPLETENESS

**Governed minimum:**

```text
shape
borders
color
texture
suspiciousCharacteristics
```

The source says **at least**, therefore the set is a minimum, not a closed schema.

**Not established by current evidence:**

- complete schema;
- all optional fields;
- field cardinalities;
- detailed value domains;
- nested representation;
- concrete serialization contract.

**BA consequence:**

Preserve the minimum governed content without inventing the complete format.

**Classification:**

```text
DOCUMENTATION DETAIL / POSSIBLE GAP
```

This entry may later be narrowed if downstream documentation provides the full
contract.
