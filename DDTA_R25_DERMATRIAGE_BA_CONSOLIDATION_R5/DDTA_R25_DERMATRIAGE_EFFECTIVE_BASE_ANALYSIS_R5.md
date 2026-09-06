# DermaTriage Effective Working Base Analysis — R5

Effective state:

```text
R1 + R2 + R3 + R4 + R5
```

## MR-01 analyzed coverage

```text
MR-01

DEC-12
    FR-16
    FR-17
    FR-18
    FR-19

DEC-13
    FR-20

DEC-14
    FR-21
    FR-22

DEC-01
    FR-01

DEC-02
    FR-02
```

R5 therefore closes the planned MR-01 child evidence-collection branch.

## R5 identity changes

```text
B4IntegratedTriagePath
    -> WORKING_ACCEPTED

POST /diagnose
    -> WORKING_ACCEPTED

B4DermaTriageBoundary
    -> WORKING_ACCEPTED_IDENTITY

ConsultationData
    -> PROVISIONAL_RECONCILIATION

CaseDocuments
    -> PROVISIONAL_RECONCILIATION
```

## R5 accepted propositions

```text
FR22-001 realize(B4IntegratedTriagePath, POST /diagnose)

FR22-002 consumeService(
    consumer = DermaTriage,
    service = B4)

FR22-003 transfer(
    B4 -> DermaTriage,
    ConsultationData,
    CaseDocuments)

FR22-004 produce(
    DermaTriage,
    inputs = ConsultationData + CaseDocuments,
    result = TriageOutcome,
    condition = B4IntegratedTriagePath)

FR22-005 correlate(
    TriageOutcome,
    context = B4Consultation)
```

## Repeated unresolved meanings

```text
endpoint -> invoked process
    P-03 / P-01

transfer -> crossed boundary
    P-04

structured request/data contract
    D-12, with P-07 only where actual governed structure later exists
```

## Current pressure inventory

```text
P-01 FUNCTION / PROCESS / BEHAVIOR IDENTITY BINDING
P-02 PIPELINE COMPOSITION AND ORDER
P-03 INTERFACE / PATH / INVOCATION ASSOCIATION
P-04 BOUNDARY / INTERACTION ASSOCIATION
P-05 ORDERED COMPARISON VOCABULARY
P-06 DIRECT SCALAR / PROPERTY-ADDRESSING COMPARISON
P-07 STRUCTURED DATA / INFORMATION CONTRACT
P-08 DATA ARTIFACT / STORE ASSOCIATION
```

## Next

```text
MR-02 — Indirizzamento specialistico
```
