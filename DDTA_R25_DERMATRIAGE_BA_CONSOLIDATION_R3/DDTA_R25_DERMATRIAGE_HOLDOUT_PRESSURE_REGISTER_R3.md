# DermaTriage Holdout Pressure Register — R3

**Default disposition:** `OPEN_FOR_EVIDENCE_COLLECTION`  
**Method changes authorized:** `NONE`

---

# P-01 — FUNCTION / PROCESS / BEHAVIOR IDENTITY BINDING

**R3 status:** `OPEN — NARROWED`  
**Evidence:** DEC-12, DEC-13, DEC-14, DEC-01, FR-01, FR-16, FR-17

FR-16 provides a candidate existing-BA solution for capabilities:

```text
capability BAReferent
    as produce.actor

concrete technology
    realize
capability
```

This means the earlier awkwardness is not sufficient to claim a generic missing BA2
operator.

Still unresolved for:

- process identities;
- pipeline identities;
- workflow/path identities;
- cases where independently reusable behavior identity must be bound while another
  participant performs or owns the behavior.

FR-17 is a negative control against forced abstraction: no separate
`ClinicalDescriptionGenerationCapability` is minted merely to exercise `realize`.

---

# P-02 — PIPELINE COMPOSITION AND ORDER

**R3 status:** `OPEN — STRENGTHENED`  
**Evidence:** DEC-12, FR-17

FR-17 governs that `ClinicalDescription` is usable by later stages of the pipeline.

Do not encode:

```text
downstream / later
```

as `dependOn` unless prerequisite semantics are actually governed.

FR-18 should provide a concrete producer-consumer test for this output.

---

# P-03 — INTERFACE / PATH ASSOCIATION

Carried from R2. OPEN.

---

# P-04 — BOUNDARY / INTERACTION ASSOCIATION

Carried from R2. OPEN.

---

# P-05 — ORDERED COMPARISON VOCABULARY

**R3 status:** `STRONG_HOLDOUT_METHODOLOGY_PRESSURE`  
**Empirically confirmed:** `greaterThan (>)` from FR-02

FR-16 documents a HIGH threshold `0.25` but does **not** govern the comparison
operator. Therefore FR-16 does not add evidence for `>` / `>=`.

Still:

```text
>  empirically required
<  review candidate only
>= review candidate only
<= review candidate only
```

---

# P-06 — DIRECT SCALAR / PROPERTY-ADDRESSING COMPARISON

**R3 status:** `STRONG — STRENGTHENED`  
**Evidence:** FR-02, FR-16

FR-16 strengthens independent `Confidence` identity because:

- classification includes associated confidence;
- FR-02 reuses confidence in a separate decision mapping.

Therefore the workaround:

```text
Confidence.value
Confidence.score
```

remains unsupported by governed source and should not be invented merely to satisfy
the current comparison grammar.

---

# P-07 — STRUCTURED DATA / INFORMATION CONTRACT

**R3 status:** `OPEN_HOLDOUT_PRESSURE`  
**Evidence:** FR-16, FR-17  
**Importance:** HIGH

## Governed evidence

FR-16:

```text
ImageUrgencyClassification
    includes
Confidence
```

FR-17:

```text
ClinicalDescription
    MUST represent at least:
        shape
        borders
        color
        texture
        suspiciousCharacteristics
```

## Observed analytical need

The BA may need to preserve, in a queryable method-neutral form:

- independently identifiable data/information artifact;
- structured fields/components;
- required vs optional components;
- possibly cardinality;
- possibly value/domain constraints;
- possibly nested structures;
- producer/consumer relationship;
- transfer of the structured artifact across participants/capabilities.

## Why current shortcuts are rejected

```text
correlate
```

preserves shared context, not containment/contract.

```text
reference
```

is too weak.

```text
vocabulary constraint
```

means allowed values, not required fields/components.

Minting one BAReferent per field merely to satisfy the model may violate minimality.

## Candidate solution families for final review

### Candidate A — richer structured `constrain`

Example design hypothesis only:

```text
constrain
  constraintTarget -> ClinicalDescription
  dataStructure:
    requiredField -> shape
    requiredField -> borders
    requiredField -> color
    requiredField -> texture
    requiredField -> suspiciousCharacteristics
```

### Candidate B — identifiable contract referent

Example design hypothesis:

```text
ClinicalDescriptionContract
```

with an explicit relation between data artifact and contract.

This may require relation/operator support not currently present.

### Candidate C — combined approach

```text
contract BAReferent
+
structured constraint
+
realize concrete JSON/API/schema representation when governed
```

## Method change now

`NONE`.

Continue collecting real data-contract evidence before choosing a representation.

---

# Global R3 rule

P-07 is a pressure record, **not an authorization to introduce a new third BA family,
new operator, or schema grammar now**.
