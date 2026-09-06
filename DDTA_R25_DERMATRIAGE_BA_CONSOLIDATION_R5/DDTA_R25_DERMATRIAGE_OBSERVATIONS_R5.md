# DermaTriage R5 — Research / Documentation Observations

These observations are not BA0–BA6 authority.

# O-03 — DATA INTERACTION COMPLETENESS

FR-22 further supports the guide candidate.

For the B4 integration we can answer:

```text
WHAT?
    ConsultationData
    CaseDocuments
    TriageOutcome

FROM WHERE?
    B4

TO WHERE?
    DermaTriage

SERVICE CONSUMED?
    B4

INTERFACE?
    POST /diagnose

CORRELATION?
    same B4Consultation

BOUNDARY?
    B4DermaTriageBoundary exists
```

But important contract detail remains unknown and becomes D-12.

The documentation-review lesson remains:

```text
For each material read/write/produce/transfer,
record enough governed meaning to know, where relevant:

what data
where it comes from
where it goes
who reads/writes/produces it
which interface/path is used
which medium/boundary is involved
and which semantic/data contract applies
```

# O-04 — LOGICAL FLOW != PHYSICAL EXCHANGE

Carried.

# O-05 — SERVICE CONSUMPTION != DATA TRANSFER != RESPONSIBILITY

FR-22 gives a clean three-way distinction:

```text
DermaTriage consumes B4 as an external service/system

B4 transfers/provides data to DermaTriage

B4 does not own the triage evaluation
```

All three meanings may coexist and require different BA constructs.

This is strong evidence that `consumeService`, `transfer`, and
`assignResponsibility` are not redundant.
