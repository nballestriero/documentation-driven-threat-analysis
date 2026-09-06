# DermaTriage Base Analysis — Delta R5

**Disposition:** `ACCEPTED_FOR_CONTINUATION`  
**Formal BA3 review:** `PENDING_REVIEW`  
**Freshness:** `CURRENT`

R5 closes the analyzed MR-01 child branch and records only the semantic delta from
FR-22.

---

# 1. Source element

```text
FR-22 — Diagnosi integrata B4 tramite POST /diagnose
```

Governed source meaning:

```text
when POST /diagnose is invoked for a B4 consultation:
    DermaTriage acquires applicable information/documents from B4
    DermaTriage executes triage
    result remains associated with the same B4 consultation
    B4 remains an external consumed service/system
    B4 does not own the triage assessment
```

Source SPO support:

```text
B4 -- provides --> ConsultationData
B4 -- provides --> CaseDocuments
DermaTriage -- consumes --> ConsultationData
DermaTriage -- produces --> B4CorrelatedTriageOutcome
```

---

# 2. Identity refinements

## BAREF-DERMA-030 — B4IntegratedTriagePath

```text
previous:
    PROVISIONAL_PRESSURE_TARGET

R5 effective:
    WORKING_ACCEPTED
```

FR-22 concretely exercises the B4-integrated path.

## BAREF-DERMA-032 — POST /diagnose

```text
previous:
    PROVISIONAL_RECONCILIATION

R5 effective:
    WORKING_ACCEPTED
```

FR-22 directly governs this endpoint as the integration entry point.

## BAREF-DERMA-033 — B4DermaTriageBoundary

```text
previous:
    PROVISIONAL_PRESSURE_TARGET

R5 effective:
    WORKING_ACCEPTED_IDENTITY
```

The boundary is explicit in DEC-14 and FR-22 provides a concrete cross-system
interaction. The identity is accepted, while P-04 remains open because the boundary
cannot yet be bound cleanly to a specific transfer proposition.

## New provisional exchange-data identities

```text
BAREF-DERMA-046 ConsultationData
    PROVISIONAL_RECONCILIATION

BAREF-DERMA-047 CaseDocuments
    PROVISIONAL_RECONCILIATION
```

They must be reconciled with existing B4-side information identities. No merge is
performed by lexical similarity.

---

# 3. Accepted working propositions

## BAPROP-DERMA-FR22-001 — B4 integrated path realization

```text
operator: realize
polarity: POSITIVE

abstract    -> B4IntegratedTriagePath
realization -> POST /diagnose
```

This parallels the accepted FR-21 direct path realization:

```text
DirectTriagePath -> POST /analyze
B4IntegratedTriagePath -> POST /diagnose
```

## BAPROP-DERMA-FR22-002 — B4 service consumption

```text
operator: consumeService
polarity: POSITIVE

consumer -> DermaTriage
service  -> B4
```

This is the first positive DermaTriage holdout test of `consumeService`.

Do not mint `B4Service` merely to satisfy the operator. The governed source itself
identifies B4 as the external service/system consumed.

## BAPROP-DERMA-FR22-003 — B4 to DermaTriage input transfer

```text
operator: transfer
polarity: POSITIVE

source      -> B4
destination -> DermaTriage
content     -> ConsultationData
content     -> CaseDocuments

scopedModifier.condition:
    B4IntegratedTriagePath applicable
```

This is intentionally distinct from service consumption:

```text
consumeService(B4)
    !=
transfer(data from B4)
```

## BAPROP-DERMA-FR22-004 — Integrated triage production refinement

```text
operator: produce
polarity: POSITIVE

actor  -> DermaTriage
input  -> ConsultationData
input  -> CaseDocuments
result -> TriageOutcome

scopedModifier.condition:
    B4IntegratedTriagePath applicable
```

R5 treats this as a Functional-Requirement-level refinement of the earlier DEC-14
integrated-path production meaning.

R5 does not silently add `B4Images` to this FR-level input set. DEC-14 evidence remains
valid separately.

## BAPROP-DERMA-FR22-005 — Same B4 consultation correlation

```text
operator: correlate
polarity: POSITIVE

correlatedItem     -> TriageOutcome
correlationContext -> B4Consultation
```

The compound documentation phrase `B4CorrelatedTriageOutcome` does not force a new BA
referent because its governed meaning is sufficiently represented as:

```text
TriageOutcome
+
correlate(..., B4Consultation)
```

---

# 4. Source-support addition

Add FR-22 source support to the existing negative responsibility proposition:

```text
BAPROP-DERMA-DEC14-004

assignResponsibility
polarity: NEGATIVE

responsibleParty    -> B4
responsibilityScope -> TriageUrgencyAssessment
responsibilityKind  -> triageResponsibility
```

FR-22 explicitly states that B4 is not the subject that owns the triage evaluation.

---

# 5. Repeated blocked endpoint-invocation meaning

FR-21 already established:

```text
POST /analyze
    invokes
DermaTriageTriageProcess
```

FR-22 now supplies the parallel integrated case:

```text
POST /diagnose
    invokes / causes execution of
DermaTriageTriageProcess
```

Record:

```text
BAREQ-DERMA-FR22-INVOKE-001
status: BLOCKED_BY_CURRENT_RELATION_PRESSURE
pressureRefs: [P-01, P-03]
```

Rejected approximations remain:

```text
reference
    too weak

dependOn
    prerequisite != invocation

consumeService
    endpoint is not the external service being consumed

realize(endpoint, process)
    endpoint realization != invoked behavior
```

This is now repeated evidence, not a one-off wording problem.

---

# 6. Boundary binding pressure

Known:

```text
B4DermaTriageBoundary exists

transfer:
    B4 -> DermaTriage
    ConsultationData
    CaseDocuments
```

Blocked semantic need:

```text
this transfer crosses B4DermaTriageBoundary
```

Current BA2 has no accepted role/relation for this association.

Do not replace it with `correlate`, `reference`, `dependOn`, or `realize`.

This strengthens P-04.

---

# 7. Data-contract boundary

FR-22 does not govern the complete request/data contract.

Known:

```text
ConsultationData
CaseDocuments
TriageOutcome
POST /diagnose
same B4 consultation correlation
```

Not sufficiently governed:

```text
complete field schema
required/optional fields
document cardinality/types
exact relationship to B4Images
request serialization
exact response contract
error contract
```

Therefore this is recorded as D-12, not silently repaired as a P-07 methodology
extension.

Authentication/security is not inferred here because dedicated later documentation
exists and has not yet been analyzed.

---

# 8. MR-01 branch closure status

All selected children under MR-01 have now been analyzed.

This is an evidence-collection branch closure only:

```text
BA6 integrated DermaTriage validation:
    NOT EXECUTED

methodology review:
    NOT EXECUTED

method change:
    NONE
```

Next bounded source element:

```text
MR-02
```
