# DermaTriage Effective Working Base Analysis — R6

Effective state:

```text
R1 + R2 + R3 + R4 + R5 + R6
```

## Coverage

```text
MR-01
    CLOSED for selected-child first-pass evidence collection

MR-02
    analyzed
    STOP AT MR

MR-03
    analyzed: MR-03, DEC-03, FR-03, FR-12, DEC-15
    remaining: FR-23, DEC-16, FR-24, FR-25
```

## R6 identities

```text
BAREF-DERMA-048 SpecialistDestinationIndication WORKING_ACCEPTED
BAREF-DERMA-049 HealthcareProfessional WORKING_ACCEPTED
BAREF-DERMA-050 ClinicalReviewResult WORKING_ACCEPTED
BAREF-DERMA-051 OriginalDermaTriageOutcome PROVISIONAL_RECONCILIATION
BAREF-DERMA-052 DiagnosticOutputWriteBack WORKING_ACCEPTED
BAREF-DERMA-053 MedicalValidationWriteBack WORKING_ACCEPTED
BAREF-DERMA-054 ValidatedOutcomeRetrieval WORKING_ACCEPTED
BAREF-DERMA-055 ValidatedOutcome PROVISIONAL_RECONCILIATION
```

`CompleteSpecialistRoutingProcess` remains distinct from `SpecialistDestinationIndication`
and is a working project-semantic identity for current evidence.

## Accepted R6 proposition summary

```text
MR02-001 produce DermaTriage + DermatologicalCase -> SpecialistDestinationIndication
MR02-002 assignResponsibility DermaTriage -> SpecialistDestinationIndication

MR03-001 produce HealthcareProfessional + OriginalDermaTriageOutcome -> ClinicalReviewResult
MR03-002 / FR03-001 correlate ClinicalReviewResult -> OriginalDermaTriageOutcome
MR03-003 HealthcareProfessional owns clinicalJudgmentAuthority
MR03-004 DermaTriage owns clinicalReviewManagementResponsibility
MR03-005 DermaTriage does NOT own clinicalJudgmentAuthority

FR12-001 constrain ClinicalReviewResult.reviewDisposition -> CONFIRMATION | CORRECTION

DEC15-001 transfer behavior DiagnosticOutputWriteBack DermaTriage -> B4 OriginalDermaTriageOutcome
DEC15-002 transfer behavior MedicalValidationWriteBack DermaTriage -> B4 ClinicalReviewResult
DEC15-003 transfer behavior ValidatedOutcomeRetrieval B4 -> DermaTriage ValidatedOutcome
DEC15-004 correlate OriginalDermaTriageOutcome + ClinicalReviewResult under B4Consultation
```

## Blocked governed meanings

```text
DermaTriage records/persists ClinicalReviewResult -> P-08
exchange behavior -> interface/logical path -> P-03
exchange behavior -> crossed boundary -> P-04
required structured property/component presence/cardinality -> P-07
```

## Pressure inventory

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

## Construct highlights

```text
transfer.behavior TESTED_POSITIVE_CROSS_CORPUS
consumeService TESTED_POSITIVE_STRONG
correlate TESTED_POSITIVE_STRONG
constrain TESTED_POSITIVE_STRONG
classify NOT_TESTED_POSITIVE (FR-12 negative control)
create NOT_TESTED_POSITIVE
transition NOT_TESTED_POSITIVE
```

## Next

```text
FR-23 — Write-back e retrieval della validazione B4
```
