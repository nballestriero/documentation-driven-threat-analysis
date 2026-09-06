# DermaTriage Base Analysis — Delta R3

**Working disposition:** `ACCEPTED_FOR_CONTINUATION`  
**Formal BA3 review state:** `PENDING_REVIEW`  
**Freshness:** `CURRENT`

This file records the R3 semantic delta only.

---

# 1. Source elements consolidated

- `FR-16`
- `FR-17`

---

# 2. Identity refinements

## BAREF-DERMA-023 — ImageBasedUrgencyClassificationCapability

Previous status:

```text
PROVISIONAL_RECONCILIATION
```

R3 effective status:

```text
WORKING_ACCEPTED
```

Rationale:

- DEC-13 already requires an operational image-classification capability to depend on
  the trained baseline;
- FR-16 explicitly governs the image-based classification function;
- the identity is reused across dependency, production and realization semantics.

## BAREF-DERMA-037 — Confidence

Previous status:

```text
PROVISIONAL_RECONCILIATION
```

R3 effective status:

```text
WORKING_ACCEPTED
```

Rationale:

- FR-16 says the image urgency classification includes / produces associated confidence;
- FR-02 independently reuses confidence as an input to the P-scale mapping;
- independent reuse justifies stable BA identity.

This does not resolve P-06: the source supports `Confidence` as reusable meaning but
does not govern an artificial `Confidence.value` / `Confidence.score` property.

---

# 3. FR-16 accepted working propositions

## BAPROP-DERMA-FR16-001 — Concrete realization of image-classification capability

```text
operator: realize
polarity: POSITIVE

abstract    -> ImageBasedUrgencyClassificationCapability
realization -> EfficientNet-B4
```

This is the first positive DermaTriage exercise of `realize`.

## BAPROP-DERMA-FR16-002 — Image urgency production

```text
operator: produce
polarity: POSITIVE

actor  -> ImageBasedUrgencyClassificationCapability
input  -> SkinLesionImage
result -> ImageUrgencyClassification
result -> Confidence

scopedModifier.condition:
    SkinLesionImage available for DermatologicalCase
```

This is the preferred R3 effective shape.

### Refinement of earlier R1 representation

R1 historically recorded:

```text
BAPROP-DERMA-DEC12-001

produce
  actor  -> EfficientNet-B4
  input  -> SkinLesionImage
  result -> ImageUrgencyClassification
```

R3 does not rewrite R1.

For the **effective BA**, FR-16 evidence supports the more explicit pattern:

```text
capability
    produces result
+
technology
    realizes capability
```

Classification:

```text
APPLICATION REFINEMENT USING EXISTING BA2
not methodology change
```

## BAPROP-DERMA-FR16-003 — Image urgency result domain

```text
operator: constrain
polarity: POSITIVE

constraintTarget -> ImageUrgencyClassification

constraintValue:
    property   -> urgencyLevel   [BA5 candidate]
    vocabulary -> HIGH | MEDIUM | LOW
```

The source governs the result domain. The canonical property key remains open to BA5
review.

---

# 4. FR-16 structured-result association is intentionally not approximated

Governed source meaning:

```text
ImageUrgencyClassification
    includes
Confidence
```

R3 does **not** accept:

```text
correlate
    Confidence
    with ImageUrgencyClassification
```

as a substitute for literal structural/contract semantics.

Reason:

```text
same-context binding
    !=
contains / includes / required data component
```

The unresolved semantic need is carried by P-07.

---

# 5. FR-16 technical details deliberately not over-normalized

## RGB 380x380

Source-observed baseline input format:

```text
RGB 380x380
```

R3 does not globally constrain `SkinLesionImage` to this shape because the source says
it is the baseline input, not necessarily the intrinsic format of every project image.

Disposition:

```text
GOVERNED TECHNICAL DETAIL
BA promotion not yet justified
```

## HIGH threshold 0.25

Known:

```text
documented HIGH threshold = 0.25
```

Not sufficiently governed:

- compared quantity;
- comparison operator;
- full HIGH/MEDIUM/LOW decision semantics;
- MEDIUM/LOW boundaries.

Therefore no `decisionRule` is materialized from `0.25`.

---

# 6. FR-17 behavioral meaning mostly reinforces existing BA

Existing proposition:

```text
BAPROP-DERMA-DEC12-002

produce
  actor  -> Qwen2-VL-7B-Instruct
  input  -> SkinLesionImage
  result -> ClinicalDescription
```

R3 adds FR-17 as reinforcing governed source support rather than minting a duplicate
semantic proposition.

The existing same-case correlation from DEC-12 also remains sufficient for case
association.

---

# 7. FR-17 minimum structured-content contract

FR-17 governs that `ClinicalDescription` must represent **at least**:

```text
shape
borders
color
texture
suspiciousCharacteristics
```

The word `at least` is significant:

```text
minimum required content
!=
closed complete schema
```

R3 does not encode this using:

- `vocabulary`, because allowed values are not required components;
- `reference`, because reference-only semantics are too weak;
- artificial BAReferents for every field;
- prose hidden inside an unconstrained `constrain`;
- `correlate`, because same-context relation is not containment/contract.

The requirement is preserved as a blocked semantic need under P-07.

---

# 8. P-01 refinement

FR-16 demonstrates that one class of P-01 cases may already be representable:

```text
BAReferent capability
+
capability as produce.actor
+
realize(capability, concrete technology)
```

Therefore P-01 is narrowed.

Still open:

- independently meaningful processes;
- pipeline identities;
- workflow/path identities;
- cases where a process must be constrained/reused while a different party performs it.

FR-17 also demonstrates that a concrete technology may legitimately remain
`produce.actor` when no independently reusable abstract capability is required.

---

# 9. R3 conclusion

```text
FR-16:
    essential meaning largely representable
    realize first positive test
    P-01 narrowed
    P-06 strengthened
    P-07 evidence added
    threshold semantics gap preserved

FR-17:
    core production already represented
    duplicate BA proposition not required
    structured minimum data/content contract required
    P-07 strengthened to open holdout pressure
```
