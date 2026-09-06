# DermaTriage Base Analysis — Delta R2

**Working disposition:** `ACCEPTED_FOR_CONTINUATION`  
**Formal BA3 review state:** `PENDING_REVIEW`  
**Freshness:** `CURRENT`

## 1. New BAReferents

| ID | Name | Status | Evidence |
|---|---|---|---|
| BAREF-DERMA-034 | `SymptomOnlyTriageProcess` | PROVISIONAL_PRESSURE_TARGET | DEC-01, FR-01 |
| BAREF-DERMA-035 | `SymptomBasedUrgency` | PROVISIONAL_RECONCILIATION | FR-01 |
| BAREF-DERMA-036 | `B4ChatbotInteractionFields` | PROVISIONAL_RECONCILIATION | DEC-01, FR-01 |
| BAREF-DERMA-037 | `Confidence` | PROVISIONAL_RECONCILIATION | DEC-02, FR-02 |

Do not yet merge `SymptomBasedUrgency` with `TriageUrgencyAssessment`.
Do not yet assume whether `Confidence` should remain an independent referent or become
a governed property binding; FR-16 must test that choice.

Not promoted:

- individual symptom fields as a complete vocabulary;
- P1/P2/P3/P4 as independent referents;
- 24h/48h/72h/7d as normative SLA constraints.

## 2. FR-01 working propositions

### BAPROP-DERMA-FR01-001

```text
operator: produce
polarity: POSITIVE

actor  -> DermaTriage
input  -> AvailableSymptomInformation
result -> SymptomBasedUrgency

condition:
    SkinLesionImage unavailable for DermatologicalCase
```

### BAPROP-DERMA-FR01-002

```text
operator: correlate
polarity: POSITIVE

correlatedItem     -> B4ChatbotInteractionFields
correlatedItem     -> AvailableSymptomInformation
correlationContext -> B4Consultation

condition:
    B4IntegratedTriagePath applicable
```

### BAPROP-DERMA-FR01-003

```text
operator: produce
polarity: POSITIVE

actor  -> DermaTriage
input  -> B4ChatbotInteractionFields
result -> AvailableSymptomInformation

condition:
    B4IntegratedTriagePath applicable
```

Recheck the actor/process binding at FR-22. This strengthens P-01.

## 3. Image optionality

Current evidence is sufficient to represent image optionality without a negative
`dependOn`:

```text
image available
    -> image-based path

image unavailable
    -> symptom-based urgency still produced
```

`R-03 IMAGE OPTIONALITY` is therefore `RESOLVED_FOR_CURRENT_EVIDENCE`.

This does not resolve whether the no-image path supplies all FR-02 mapping inputs.

## 4. DEC-02 / FR-02 required decision rule

Governed mapping:

```text
HIGH AND confidence > 0.85      -> P1
HIGH in other applicable cases  -> P2
MEDIUM                          -> P3
LOW                             -> P4
```

Appropriate BA2 operator:

```text
decisionRule
```

Conceptual lower shape:

```text
actor  -> DermaTriage
input  -> TriageUrgencyAssessment
input  -> Confidence
result -> OperationalPriority
```

The complete rule is **not materialized as an accepted BAProposition** in R2 because
frozen BA2 R3 cannot represent it honestly:

1. `greaterThan` is not an admitted comparison key;
2. direct scalar comparison may require inventing an unsupported property such as
   `Confidence.value` or `Confidence.score`.

Disposition:

```text
semanticNeed: CONFIRMED
operatorNeed: decisionRule CONFIRMED
materializationStatus: BLOCKED_BY_FROZEN_BA2_PRESSURE
pressureRefs: P-05, P-06
```

## 5. Documentation gaps preserved

- `GAP-DERMA-NOIMAGE-INPUT-01`: complete required/optional symptom contract and missing-value semantics are not governed.
- `GAP-DERMA-PMAP-INPUT-01`: complete missing/invalid urgency/confidence semantics are not governed.
- `GAP-DERMA-NOIMAGE-PMAP-BINDING-01`: no guarantee that symptom-only output always supplies every P-scale input.
- `GAP-DERMA-SLA-01`: P-scale time associations lack sufficiently governed trigger/owner/normative semantics.
