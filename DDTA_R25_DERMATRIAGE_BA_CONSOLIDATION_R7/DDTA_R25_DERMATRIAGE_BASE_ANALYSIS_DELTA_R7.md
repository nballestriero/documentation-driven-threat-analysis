# DermaTriage Base Analysis — Delta R7

**Disposition:** `ACCEPTED_FOR_CONTINUATION`  
**Formal BA3 review:** `PENDING_REVIEW`  
**Methodology:** `FROZEN`

R7 is additive after R6 and closes first-pass evidence collection for the MR-03 branch.

# 1. FR-23 — Write-back e retrieval della validazione B4

## New / refined identities

```text
BAREF-DERMA-056 B4TriageOutcome
    PROVISIONAL_RECONCILIATION

BAREF-DERMA-057 ClinicianValidation
    PROVISIONAL_RECONCILIATION

BAREF-DERMA-052 DiagnosticOutputWriteBack
    WORKING_ACCEPTED
BAREF-DERMA-053 MedicalValidationWriteBack
    WORKING_ACCEPTED
BAREF-DERMA-054 ValidatedOutcomeRetrieval
    WORKING_ACCEPTED
BAREF-DERMA-055 ValidatedOutcome
    PROVISIONAL_RECONCILIATION / STRONGLY_REINFORCED
```

Do not merge B4TriageOutcome with OriginalDermaTriageOutcome, ClinicianValidation with ClinicalReviewResult, or ValidatedOutcome with ClinicalReviewResult unless later governed evidence supports identity equivalence.

## Accepted propositions

```text
BAPROP-DERMA-FR23-001
transfer
behavior: DiagnosticOutputWriteBack
source: DermaTriage
destination: B4
content: B4TriageOutcome

BAPROP-DERMA-FR23-002
transfer
behavior: MedicalValidationWriteBack
source: DermaTriage
destination: B4
content: ClinicianValidation

BAPROP-DERMA-FR23-003
transfer
behavior: ValidatedOutcomeRetrieval
source: B4
destination: DermaTriage
content: ValidatedOutcome

BAPROP-DERMA-FR23-004
observe
actor: DermaTriage
observed: ValidatedOutcome

BAPROP-DERMA-FR23-005
correlate
correlatedItem: ValidatedOutcome
correlationContext: OriginalDermaTriageOutcome

BAPROP-DERMA-FR23-006
correlate
correlatedItem: [B4TriageOutcome, ClinicianValidation, ValidatedOutcome]
correlationContext: B4Consultation
```

`observe` represents read/retrieval of existing meaning; `transfer` represents B4 -> DermaTriage conveyance. They are distinct and can coexist.

# 2. DEC-16 — Authentication boundaries and mechanisms

Working identities, refined by FR-24/FR-25:

```text
BAREF-DERMA-058 XApiKeyAuthenticationMechanism
    WORKING_ACCEPTED
BAREF-DERMA-059 BearerJwtAuthenticationMechanism
    WORKING_ACCEPTED
BAREF-DERMA-060 ProtectedDermaTriageOperation
    WORKING_ACCEPTED
BAREF-DERMA-061 DermaTriageB4Client
    WORKING_ACCEPTED
BAREF-DERMA-062 B4BearerJwtTokenLifecycleManagement
    WORKING_ACCEPTED
BAREF-DERMA-063 DermaTriageAdministrativeOperationsBoundary
    PROVISIONAL_IDENTITY
```

`BAREF-DERMA-063` preserves only the governed distinction that the administrative interaction crosses a boundary different from the B4 interaction. It does not infer topology or deployment.

```text
BAPROP-DERMA-DEC16-001
constrain ProtectedDermaTriageOperation -> XApiKeyAuthenticationMechanism

BAPROP-DERMA-DEC16-002
constrain DiagnosticOutputWriteBack -> BearerJwtAuthenticationMechanism

BAPROP-DERMA-DEC16-003
constrain MedicalValidationWriteBack -> BearerJwtAuthenticationMechanism

BAPROP-DERMA-DEC16-004
constrain ValidatedOutcomeRetrieval -> BearerJwtAuthenticationMechanism

BAPROP-DERMA-DEC16-005
assignResponsibility
responsibleParty: DermaTriageB4Client
responsibilityScope: B4BearerJwtTokenLifecycleManagement
responsibilityKind: tokenAcquisitionAndRefreshResponsibility
```

Authentication requirement is representable with current `constrain`. No authentication operator is introduced.

# 3. FR-24 — X-API-Key per operazioni amministrative

The protected operation scope includes, where exposed as protected:

```text
review
validation/correction
prompt management
classifier retraining
```

The earlier working name `DermaTriageAdministrativeReviewOperations` is therefore refined before checkpoint acceptance to:

```text
BAREF-DERMA-060 ProtectedDermaTriageOperation
```

FR-24 introduces:

```text
BAREF-DERMA-064 AdministrativeClient
    WORKING_ACCEPTED
```

Accepted:

```text
BAPROP-DERMA-FR24-001
constrain
constraintTarget: ProtectedDermaTriageOperation
constraintValue: XApiKeyAuthenticationMechanism
```

Partially representable governed meaning:

```text
BAREQ-DERMA-FR24-PRESENT-001
AdministrativeClient presents X-API-Key to protected DermaTriage interaction/interface
status: PARTIALLY_REPRESENTABLE
pressureRef: P-03
```

Current BA represents that the operation requires the mechanism, but cannot preserve the presenter-to-protected-interface binding with equal precision without inventing credential instance or exact interface/destination detail.

# 4. FR-25 — Bearer JWT per interazione B4

FR-25 resolves the logical B4 client identity and introduces the credential/token:

```text
BAREF-DERMA-061 DermaTriageB4Client
    WORKING_ACCEPTED
BAREF-DERMA-065 B4BearerJWT
    WORKING_ACCEPTED
```

Important distinction:

```text
BearerJwtAuthenticationMechanism
    != B4BearerJWT
    != B4BearerJwtTokenLifecycleManagement
```

Bearer credential presentation:

```text
BAPROP-DERMA-FR25-001
transfer
source: DermaTriageB4Client
destination: B4
content: B4BearerJWT
```

No separate transfer-behavior referent is minted because current evidence does not require independent qualification of this credential conveyance.

## Token obtain / refresh counterexample

Governed:

```text
DermaTriageB4Client MUST obtain / refresh B4BearerJWT
```

Rejected current approximations:

```text
create -> would imply client creates/issues token
produce -> would imply token origin at client
observe -> obtain is not mere read/query
transition -> no governed token states/lifecycle transitions
consumeService -> no governed token/authorization service identity
transfer -> issuer/source of acquisition is not governed
```

Record:

```text
BAREQ-DERMA-FR25-TOKEN-LIFECYCLE-001
status: GOVERNED_BUT_NOT_FULLY_REPRESENTABLE
pressureDisposition: UNNUMBERED_HOLDOUT_PRESSURE_EVIDENCE
candidateTopic: ACQUISITION / REFRESH ACTION SEMANTICS
```

No new pressure ID is created while BA0–BA6 are frozen.

# 5. Interaction completeness / intentional detail

R7 preserves O-03 and O-09. For JWT interaction:

```text
DermaTriageB4Client: DOCUMENTED
B4: DOCUMENTED
Bearer JWT mechanism: DOCUMENTED
B4BearerJWT credential: DOCUMENTED
client obtains token: DOCUMENTED
client refreshes token: DOCUMENTED
client presents token to B4: DOCUMENTED

token issuer: NOT_DOCUMENTED_UNASSESSED
token acquisition interface: NOT_DOCUMENTED_UNASSESSED
refresh interface / trigger: NOT_DOCUMENTED_UNASSESSED
token storage: NOT_DOCUMENTED_UNASSESSED
exact wire/header representation: NOT_DOCUMENTED_UNASSESSED
transport/protocol: NOT_DOCUMENTED_UNASSESSED
medium/network path: NOT_DOCUMENTED_UNASSESSED
channel confidentiality/integrity: NOT ESTABLISHED BY AUTHENTICATION REQUIREMENT
```

These are assessment states, not automatic gaps.

# 6. Methodology disposition

```text
BA0–BA6: FROZEN
new top-level operator: NONE
new first-class BAE family: NONE
new numbered pressure: NONE
unresolved governed counterexample added: token obtain / refresh action semantics
```
