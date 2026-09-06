# DermaTriage Reconciliation Register — R5

# R-01 — Responsibility/property canonicalization

OPEN.

# R-02 — Specialist routing identity

OPEN. Next review begins at MR-02.

# R-03 — Image optionality

RESOLVED_FOR_CURRENT_EVIDENCE.

# R-04 — Triage result identity family

OPEN.

# R-05 — Confidence identity / binding

OPEN.

# R-06 — Triage process/path identity

OPEN and strengthened by FR-22.

Keep distinct until evidence proves otherwise:

```text
ImageBasedTriagePipeline
SymptomOnlyTriageProcess
DirectTriagePath
B4IntegratedTriagePath
DermaTriageTriageProcess
```

# R-07 — B4 EXCHANGE DATA IDENTITY ALIGNMENT

**R5 status:** `OPEN`

Reconcile:

```text
ConsultationData
    ?
B4Consultation
    ?
B4ChatbotInteractionFields
```

```text
CaseDocuments
    ?
B4Documents
```

```text
B4CorrelatedTriageOutcome
    ?
TriageOutcome + correlate(B4Consultation)
```

Also preserve the distinction:

```text
B4Images
```

is governed by DEC-14 but is not explicitly named by FR-22.

Do not infer either:

```text
B4Images definitely included in FR-22
```

or:

```text
B4Images definitely excluded from FR-22
```

without stronger source evidence.
