# DermaTriage Holdout Observations — R6

Observations are evidence and guide candidates, not BA0–BA6 changes.

# O-02 — SOURCE VERB != BA OPERATOR

Further strengthened:

```text
FR-16 source "classify image" != BA classify
FR-12 source "classify disposition" != automatic BA classify
```

# O-03 — DATA INTERACTION COMPLETENESS

For every materially relevant data interaction, consider when material:

```text
1. WHAT — data/artifact
2. WHO — producer/reader/writer/sender/receiver
3. FROM — logical source and/or source store
4. TO — logical destination and/or destination store
5. OPERATION — transfer/read/write/retrieval/write-back/etc.
6. INTERFACE / LOGICAL PATH — endpoint/API/queue/file/IPC/etc.
7. SERVICE / CAPABILITY — consumed service/capability
8. CONNECTION / CHANNEL — independently meaningful connection/session/channel
9. TRANSPORT / PROTOCOL — communication protocol
10. MEDIUM — materially relevant logical/physical medium/network path
11. BOUNDARY — boundary/boundaries crossed
12. SECURITY / TRUST QUALIFICATION — authentication/confidentiality/integrity/provenance/etc.
```

Independent meanings:

```text
API != service != connection != transport != medium != boundary != ownership
```

O-03 does not require every level to be documented. O-09 governs intentional detail.

# O-04 — LOGICAL DATA FLOW != PHYSICAL DATA EXCHANGE

A logical B4 API interaction does not by itself establish HTTPS, TLS, TCP, Internet,
private network, physical medium or specific trust-boundary route.

# O-05 — SERVICE CONSUMPTION != DATA TRANSFER != RESPONSIBILITY

DEC-15 further confirms:

```text
DermaTriage consumes B4
DermaTriage transfers data to/from B4
DermaTriage retains review-management responsibility
```

# O-06 — INTENTIONAL DECOMPOSITION STOP != DOCUMENTATION GAP

MR-02 is `STOP AT MR`. Absence of Decision/FR is intentional and must not be auto-filled.

# O-07 — SEMANTIC PRESERVATION != STORAGE IMPLEMENTATION

DEC-03 requires original outcome and review to remain distinguishable. It does not select
append-only storage, immutable rows, event sourcing, separate tables or write-once storage.

# O-08 — RECORDING != ORIGIN / AUTHORSHIP

```text
HealthcareProfessional originates clinical judgment
DermaTriage records/manages ClinicalReviewResult
```

Persistence does not transfer authorship, authority or semantic ownership.

# O-09 — DOCUMENTATION DETAIL MUST BE INTENTIONAL

**New R6 observation.**

> Documentation completeness is not the requirement to document everything. It is the
> requirement to make the chosen documentation boundary explicit and conscious.

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

Interpretation:

```text
UNKNOWN_REQUIRED -> documentation gap
CONSIDERED_NOT_REQUIRED / OUT_OF_SCOPE / NOT_APPLICABLE -> intentional non-completeness
DEFERRED -> acceptable if traceable
NOT_DOCUMENTED_UNASSESSED -> quality-risk state; omission may be accidental
```

The goal is not maximal detail. The goal is awareness, traceable choice, clear authority
boundary and no accidental semantic omission.

# Guide candidate

A future DDTA documentation guide should ask:

```text
Was this level considered?
Is it material?
Is it required for the analyses the project wants to support?
If omitted, is it intentional, deferred, out of scope, not applicable or accidental?
```
