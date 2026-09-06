# DermaTriage Documentation Gap Register — R6

R6 distinguishes documentation gaps from intentional non-completeness.

## Assessment states

```text
DOCUMENTED
NOT_DOCUMENTED_UNASSESSED
CONSIDERED_NOT_REQUIRED
DEFERRED
OUT_OF_SCOPE
UNKNOWN_REQUIRED
NOT_APPLICABLE
```

Rules:

```text
UNKNOWN_REQUIRED -> documentation gap
CONSIDERED_NOT_REQUIRED / OUT_OF_SCOPE / NOT_APPLICABLE -> not automatic gaps
DEFERRED -> acceptable when traceable
NOT_DOCUMENTED_UNASSESSED -> documentation-quality risk requiring assessment
```

Prior `D-01..D-12` are carried from predecessor checkpoints and are not rewritten.

# D-13 — SPECIALIST DESTINATION SELECTION / CONTRACT COMPLETENESS

**Status:** `OPEN`

Known:

```text
DermaTriage produces/supports SpecialistDestinationIndication
operational output includes specialist-oriented information
purpose is downstream specialist routing support
```

Not sufficiently governed:

```text
selection rule
complete destination vocabulary
fallback rule
exact semantic type of `specialist`
complete relation to P-scale
derivation source of destination indication
complete output binding
```

Explicitly out of scope, not gaps at MR-02 level:

```text
booking
actual specialist assignment
complete routing ownership
```

# D-14 — CLINICAL REVIEW REGISTRATION / PERSISTENCE COMPLETENESS

**Status:** `OPEN — BOUNDED`

Known:

```text
WHAT: ClinicalReviewResult
WHO RECORDS/MANAGES: DermaTriage
CORRELATED WITH: OriginalDermaTriageOutcome
```

Not sufficiently governed by FR-03:

```text
storage/repository
write target
registration identifier
persisted association representation
write interface/path
```

Not automatically gaps because MR-03 places them out of scope at this authority level:

```text
full retention policy
full history policy
finality policy
```

# DEC-15 interaction detail — assessment, not automatic gaps

Known:

```text
interface/logical path: B4 APIs
service/system: B4
boundary identity: B4DermaTriageBoundary
exchange behaviors: DiagnosticOutputWriteBack, MedicalValidationWriteBack, ValidatedOutcomeRetrieval
```

Assessment before FR-23 / DEC-16:

```text
specific API endpoint: DEFERRED -> FR-23
authentication: DEFERRED -> DEC-16 / FR-24 / FR-25
connection/channel: NOT_DOCUMENTED_UNASSESSED
transport/protocol: NOT_DOCUMENTED_UNASSESSED
medium/network path: NOT_DOCUMENTED_UNASSESSED
boundary-to-specific-transfer binding: METHODOLOGY PRESSURE P-04
```

The purpose is conscious assessment, not maximal documentation.
