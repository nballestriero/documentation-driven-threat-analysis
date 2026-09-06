# DermaTriage Base Analysis — Delta R6

**Disposition:** `ACCEPTED_FOR_CONTINUATION`  
**Formal BA3 review:** `PENDING_REVIEW`  
**Methodology:** `FROZEN`

R6 is the additive semantic delta after R5. It covers MR-02 and MR-03 through DEC-15.

# 1. MR-02 — Indirizzamento specialistico

Governed meaning:

```text
DermaTriage determines / produces-supports
SpecialistDestinationIndication
for DermatologicalCase
to support subsequent specialist routing.
```

Explicitly not established here:

```text
actual specialist assignment
booking
complete specialty taxonomy
fallback rule
complete P-scale -> specialist rule
complete routing ownership
```

MR-02 is intentionally `STOP AT MR`; no Decision or FR is invented.

```text
BAREF-DERMA-048 SpecialistDestinationIndication
    WORKING_ACCEPTED
```

`SpecialistDestinationIndication != CompleteSpecialistRoutingProcess`.

Accepted:

```text
BAPROP-DERMA-MR02-001
produce
actor: DermaTriage
input: DermatologicalCase
result: SpecialistDestinationIndication
```

```text
BAPROP-DERMA-MR02-002
assignResponsibility POSITIVE
responsibleParty: DermaTriage
responsibilityScope: SpecialistDestinationIndication
responsibilityKind: specialistDestinationIndicationResponsibility
```

Do not infer a canonical MR-02 dependency on MR-01, a P-scale specialist rule, booking,
or a `SpecialistPerson` identity from the source field label `specialist`.

# 2. MR-03 — Gestione della validazione clinica

```text
BAREF-DERMA-049 HealthcareProfessional
    WORKING_ACCEPTED
BAREF-DERMA-050 ClinicalReviewResult
    WORKING_ACCEPTED
BAREF-DERMA-051 OriginalDermaTriageOutcome
    PROVISIONAL_RECONCILIATION
```

Responsibility boundary:

```text
clinical judgment authority -> HealthcareProfessional
review management/registration/correlation -> DermaTriage
```

Accepted macro propositions:

```text
BAPROP-DERMA-MR03-001
produce
actor: HealthcareProfessional
input: OriginalDermaTriageOutcome
result: ClinicalReviewResult
```

This represents origin of the clinical judgment, not physical transport.

```text
BAPROP-DERMA-MR03-002
correlate
correlatedItem: ClinicalReviewResult
correlationContext: OriginalDermaTriageOutcome
```

```text
BAPROP-DERMA-MR03-003
assignResponsibility POSITIVE
HealthcareProfessional -> ClinicalReviewResult
kind: clinicalJudgmentAuthority
```

```text
BAPROP-DERMA-MR03-004
assignResponsibility POSITIVE
DermaTriage -> ClinicalReviewResult
kind: clinicalReviewManagementResponsibility
```

```text
BAPROP-DERMA-MR03-005
assignResponsibility NEGATIVE
DermaTriage -> ClinicalReviewResult
kind: clinicalJudgmentAuthority
```

Do not infer direct HealthcareProfessional -> DermaTriage transfer at MR level.

# 3. DEC-03 — Original outcome vs clinical review

DEC-03 reinforces:

```text
OriginalDermaTriageOutcome
    != semantic replacement by
ClinicalReviewResult
```

Separate BAReferent identities preserve the distinction; no `distinctFrom` operator is required.

Rejected:

```text
transition(OriginalDermaTriageOutcome -> ReviewedOutcome)
create(ClinicalReviewResult) by DermaTriage
physical immutability / append-only storage inference
```

Semantic preservation does not select a storage implementation.

# 4. FR-03 — Registrazione correlata

Accepted:

```text
BAPROP-DERMA-FR03-001
correlate
correlatedItem: ClinicalReviewResult
correlationContext: OriginalDermaTriageOutcome
```

FR-03 also supports DermaTriage review-management responsibility.

Blocked governed meaning:

```text
BAREQ-DERMA-FR03-RECORD-001
DermaTriage records/persists ClinicalReviewResult
pressureRef: P-08
```

Rejected substitutes:

```text
create: recording != semantic establishment of clinical judgment
produce: recording != authorship/output origin
observe: write != read/query
transition: no governed UNRECORDED -> RECORDED lifecycle
transfer: FR-03 does not assert source/destination conveyance
reference: too weak
correlate: association != persistence
```

# 5. FR-12 — Conferma vs correzione

Governed review-disposition domain:

```text
ClinicalReviewResult.reviewDisposition
    CONFIRMATION | CORRECTION
```

Accepted:

```text
BAPROP-DERMA-FR12-001
constrain
constraintTarget: ClinicalReviewResult
constraintValue:
    property: reviewDisposition
    vocabulary: [CONFIRMATION, CORRECTION]
```

`reviewDisposition` is a BA5 canonicalization candidate, not automatically a BAReferent.

Source wording includes “classify disposition”, but BA `classify` is rejected for this case.
Two unconditional classify propositions would wrongly assign both semantic kinds; no circular
conditional classification is introduced.

```text
classify:
    DIRECTLY_CONSIDERED_AND_REJECTED_FOR_FR12
    positive empirical status remains NOT_TESTED
```

P-07 is strengthened because vocabulary is representable but mandatory presence / exactly-one
cardinality is not cleanly preserved by current BA2.

# 6. DEC-15 — Validation exchange with B4

Three independently meaningful exchange behaviors are governed:

```text
BAREF-DERMA-052 DiagnosticOutputWriteBack WORKING_ACCEPTED
BAREF-DERMA-053 MedicalValidationWriteBack WORKING_ACCEPTED
BAREF-DERMA-054 ValidatedOutcomeRetrieval WORKING_ACCEPTED
BAREF-DERMA-055 ValidatedOutcome PROVISIONAL_RECONCILIATION
```

No specific B4 validation endpoint/API identity is minted at DEC-15 level.

```text
BAPROP-DERMA-DEC15-001
transfer
behavior: DiagnosticOutputWriteBack
source: DermaTriage
destination: B4
content: OriginalDermaTriageOutcome
```

```text
BAPROP-DERMA-DEC15-002
transfer
behavior: MedicalValidationWriteBack
source: DermaTriage
destination: B4
content: ClinicalReviewResult
```

```text
BAPROP-DERMA-DEC15-003
transfer
behavior: ValidatedOutcomeRetrieval
source: B4
destination: DermaTriage
content: ValidatedOutcome
```

```text
BAPROP-DERMA-DEC15-004
correlate
correlatedItem: [OriginalDermaTriageOutcome, ClinicalReviewResult]
correlationContext: B4Consultation
```

DEC-15 also adds source support to `consumeService(DermaTriage, B4)` and DermaTriage
review-management responsibility.

`observe` for retrieval remains a positive candidate for FR-23 rather than being silently
accepted from the Decision alone.

# 7. Interaction-detail refinement

For every materially relevant data interaction, consider:

```text
WHAT
WHO
FROM
TO
OPERATION
INTERFACE / LOGICAL PATH
SERVICE / CAPABILITY
CONNECTION / CHANNEL
TRANSPORT / PROTOCOL
MEDIUM
BOUNDARY / BOUNDARIES CROSSED
SECURITY / TRUST QUALIFICATION
```

These dimensions are not synonyms:

```text
API != service != connection != transport != medium != boundary != ownership
```

R6 does not require every dimension to be documented. It requires the chosen documentation
boundary to be intentional and reviewable.

Assessment states:

```text
DOCUMENTED
NOT_DOCUMENTED_UNASSESSED
CONSIDERED_NOT_REQUIRED
DEFERRED
OUT_OF_SCOPE
UNKNOWN_REQUIRED
NOT_APPLICABLE
```

`UNKNOWN_REQUIRED` is a documentation gap. Intentional non-completeness is not automatically a gap.

# 8. Methodology disposition

```text
BA0–BA6: FROZEN
new BA operator: NONE
new BA role: NONE
new first-class BAE family: NONE
```
