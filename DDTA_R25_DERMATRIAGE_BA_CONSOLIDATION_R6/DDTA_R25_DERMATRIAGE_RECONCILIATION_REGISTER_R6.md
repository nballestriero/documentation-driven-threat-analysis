# DermaTriage Reconciliation Register — R6

# R-02 — SPECIALIST ROUTING IDENTITY

**Status:** `RESOLVED_FOR_CURRENT_EVIDENCE`

```text
SpecialistDestinationIndication != CompleteSpecialistRoutingProcess
```

No merge.

# R-05 — CONFIDENCE IDENTITY / BINDING

`OPEN` — carried.

# R-06 — TRIAGE PROCESS / PATH IDENTITY

`OPEN` — carried.

# R-07 — B4 EXCHANGE DATA IDENTITY ALIGNMENT

`OPEN` — carried:

```text
ConsultationData ? B4Consultation ? B4ChatbotInteractionFields
CaseDocuments ? B4Documents
B4CorrelatedTriageOutcome ? TriageOutcome + correlate(B4Consultation)
B4Images in DEC-14 but absent FR-22
```

# R-08 — SPECIALIST INDICATION / TRIAGE OUTPUT BINDING

**Status:** `OPEN`

```text
SpecialistDestinationIndication
    component of TriageOutcome?
    component of OperationalPriority?
    produced alongside OperationalPriority?
    derived from P-scale?
    independently determined?
```

# R-09 — ORIGINAL DERMATRIAGE OUTCOME IDENTITY

**Status:** `OPEN — STRONGLY REINFORCED`

```text
OriginalDermaTriageOutcome
    ? TriageOutcome
    ? AITriageSynthesis
    ? TriageUrgencyAssessment
    ? OperationalTriagePriorityPScale
    ? composite operational output
```

Important for review correlation and diagnostic-output write-back.

# R-10 — VALIDATED OUTCOME / CLINICAL REVIEW IDENTITY

**Status:** `OPEN — RECHECK FR-23`

```text
ValidatedOutcome ? ClinicalReviewResult
ValidatedOutcome ? B4-side representation of ClinicalReviewResult
ValidatedOutcome ? another review-derived result
```

# Discipline

```text
same words != same identity
related workflow position != same identity
merge only when governed meaning supports equivalence
```
