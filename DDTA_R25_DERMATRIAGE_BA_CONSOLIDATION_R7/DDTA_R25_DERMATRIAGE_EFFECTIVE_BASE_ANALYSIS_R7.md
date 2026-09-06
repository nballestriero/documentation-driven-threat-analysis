# DermaTriage Effective Working Base Analysis — R7

Effective state:

```text
R1 + R2 + R3 + R4 + R5 + R6 + R7
```

## Coverage state

```text
MR-01: first-pass selected-child branch complete
MR-02: first-pass analyzed / STOP AT MR
MR-03: FIRST-PASS BRANCH COMPLETE

MR-03
    DEC-03
        FR-03
        FR-12
    DEC-15
        FR-23
    DEC-16
        FR-24
        FR-25
```

Next bounded source:

```text
MR-04 — Adattamento controllato sulla base della revisione clinica
```

## R7 effective identity delta

```text
BAREF-DERMA-052 DiagnosticOutputWriteBack WORKING_ACCEPTED
BAREF-DERMA-053 MedicalValidationWriteBack WORKING_ACCEPTED
BAREF-DERMA-054 ValidatedOutcomeRetrieval WORKING_ACCEPTED
BAREF-DERMA-055 ValidatedOutcome PROVISIONAL_RECONCILIATION
BAREF-DERMA-056 B4TriageOutcome PROVISIONAL_RECONCILIATION
BAREF-DERMA-057 ClinicianValidation PROVISIONAL_RECONCILIATION
BAREF-DERMA-058 XApiKeyAuthenticationMechanism WORKING_ACCEPTED
BAREF-DERMA-059 BearerJwtAuthenticationMechanism WORKING_ACCEPTED
BAREF-DERMA-060 ProtectedDermaTriageOperation WORKING_ACCEPTED
BAREF-DERMA-061 DermaTriageB4Client WORKING_ACCEPTED
BAREF-DERMA-062 B4BearerJwtTokenLifecycleManagement WORKING_ACCEPTED
BAREF-DERMA-063 DermaTriageAdministrativeOperationsBoundary PROVISIONAL_IDENTITY
BAREF-DERMA-064 AdministrativeClient WORKING_ACCEPTED
BAREF-DERMA-065 B4BearerJWT WORKING_ACCEPTED
```

## Accepted proposition delta

```text
FR23-001 transfer DiagnosticOutputWriteBack DermaTriage -> B4 / B4TriageOutcome
FR23-002 transfer MedicalValidationWriteBack DermaTriage -> B4 / ClinicianValidation
FR23-003 transfer ValidatedOutcomeRetrieval B4 -> DermaTriage / ValidatedOutcome
FR23-004 observe DermaTriage -> ValidatedOutcome
FR23-005 correlate ValidatedOutcome / OriginalDermaTriageOutcome
FR23-006 correlate B4TriageOutcome + ClinicianValidation + ValidatedOutcome / B4Consultation
DEC16-001 constrain ProtectedDermaTriageOperation -> XApiKeyAuthenticationMechanism
DEC16-002..004 constrain each B4 validation exchange behavior -> BearerJwtAuthenticationMechanism
DEC16-005 assignResponsibility DermaTriageB4Client -> B4BearerJwtTokenLifecycleManagement
FR24-001 constrain ProtectedDermaTriageOperation -> XApiKeyAuthenticationMechanism
FR25-001 transfer DermaTriageB4Client -> B4 / B4BearerJWT
```

## Governed-but-blocked / partial meanings

```text
AdministrativeClient presents X-API-Key to protected interaction/interface -> P-03
identified interaction crosses specific boundary -> P-04
DermaTriageB4Client obtains / refreshes B4BearerJWT -> UNNUMBERED_HOLDOUT_PRESSURE_EVIDENCE
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
P-08 DATA ARTIFACT / STORE / PERSISTENCE ASSOCIATION
```

No P-09 is created during holdout.

## Construct highlights

```text
transfer: TESTED_POSITIVE_STRONG
transfer.behavior: TESTED_POSITIVE_CROSS_CORPUS_STRONG
observe: TESTED_POSITIVE_STRONG
correlate: TESTED_POSITIVE_STRONG
consumeService: TESTED_POSITIVE_STRONG
assignResponsibility: TESTED_POSITIVE_STRONG
constrain: TESTED_POSITIVE_STRONG
create: NOT_TESTED_POSITIVE
transition: NOT_TESTED_POSITIVE
classify: NOT_TESTED_POSITIVE
decisionRule: TESTED_NECESSARY_BUT_BLOCKED
```
