# DermaTriage Reconciliation Register — R7

# R-02 — SPECIALIST ROUTING IDENTITY
**Status:** `RESOLVED_FOR_CURRENT_EVIDENCE` — carried from R6.

# R-05 / R-06 / R-07 / R-08
Carried according to predecessor state.

# R-09 — ORIGINAL DERMATRIAGE OUTCOME IDENTITY
**R7 status:** `OPEN — FURTHER STRENGTHENED`

```text
OriginalDermaTriageOutcome
    ? TriageOutcome
    ? AITriageSynthesis
    ? TriageUrgencyAssessment
    ? OperationalTriagePriorityPScale
    ? B4TriageOutcome
```

FR-23 does not authorize a merge.

# R-10 — VALIDATION / VALIDATED OUTCOME / CLINICAL REVIEW IDENTITY
**R7 status:** `OPEN — FURTHER STRENGTHENED`

```text
ClinicalReviewResult ? ClinicianValidation ? ValidatedOutcome
```

FR-23 gives correlation evidence, not equivalence evidence.

# R-11 — B4 CLIENT IDENTITY / LOGICAL PLACEMENT
**R7 status:** `RESOLVED_FOR_CURRENT_EVIDENCE`

```text
B4Client -> DermaTriageB4Client
logical project placement: DermaTriage-side B4 client
```

Not resolved or implied: process, container, host, network zone, physical deployment, credential storage location.

# R-12 — ADMINISTRATIVE CLIENT IDENTITY / PLACEMENT
**R7 status:** `OPEN`

Known:

```text
AdministrativeClient presents X-API-Key
```

Not governed: human vs software client, realizing UI/service/component, logical ownership, deployment placement, side of administrative boundary, credential-holder implementation.

## R7 reconciliation discipline

```text
more concrete child terminology may refine canonicalName
but must not silently create duplicate identities
correlation != equivalence
logical ownership/placement != deployment placement
```
