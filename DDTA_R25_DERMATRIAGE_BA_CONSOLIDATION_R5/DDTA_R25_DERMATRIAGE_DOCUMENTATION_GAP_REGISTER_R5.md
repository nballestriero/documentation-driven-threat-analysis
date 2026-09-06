# DermaTriage Documentation Gap Register — R5 additions

R5 carries all previous gaps and adds D-12.

# D-12 — B4 DIAGNOSE DATA CONTRACT COMPLETENESS

**Source:** FR-22

Known:

```text
interface:
    POST /diagnose

external source/service:
    B4

consumer:
    DermaTriage

input categories:
    ConsultationData
    CaseDocuments

result:
    TriageOutcome

correlation:
    same B4Consultation
```

Not sufficiently governed in FR-22:

- complete `ConsultationData` schema;
- complete `CaseDocuments` schema;
- required vs optional fields;
- document types;
- document/cardinality constraints;
- exact relationship between FR-22 input contract and `B4Images` from DEC-14;
- consultation identifier contract;
- concrete request serialization;
- exact response body/schema;
- endpoint error contract.

Disposition:

```text
DOCUMENTATION GAP
```

## Authentication / transport note

R5 does **not** classify missing authentication or transport-security detail in FR-22
as a final project-level documentation defect because dedicated later governed
elements exist for B4 authentication/review interfaces and have not yet been analyzed.

Current status:

```text
NOT GOVERNED BY FR-22
RECHECK LATER
```

This applies the rule:

```text
missing from one FR
    !=
globally absent from project documentation
```
