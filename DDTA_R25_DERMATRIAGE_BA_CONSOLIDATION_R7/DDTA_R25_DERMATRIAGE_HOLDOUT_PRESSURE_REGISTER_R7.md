# DermaTriage Holdout Pressure Register — R7

**Method changes authorized:** `NONE`  
**New numbered pressure IDs:** `NONE`

# P-01 — FUNCTION / PROCESS / BEHAVIOR IDENTITY BINDING
**R7 status:** `OPEN — REPEATED PROCESS SUBCASE` — carried unchanged.

# P-02 — PIPELINE COMPOSITION AND ORDER
**R7 status:** `OPEN — PARTIALLY NARROWED` — carried unchanged.

# P-03 — INTERFACE / PATH / INVOCATION ASSOCIATION
**R7 status:** `STRONG_REPEATED_HOLDOUT_PRESSURE — FURTHER STRENGTHENED / PARTIALLY NARROWED`

FR-24 adds:

```text
AdministrativeClient presents X-API-Key to protected DermaTriage interaction/interface
```

The operation-side requirement is representable with `constrain`, but current BA cannot preserve the presenter-to-protected-interface binding with equal precision without inventing a credential instance or exact interface/destination detail.

FR-25 narrows the problem: when source + destination + content are governed, `transfer` is sufficient for credential conveyance.

# P-04 — BOUNDARY / INTERACTION ASSOCIATION
**R7 status:** `STRONG_REPEATED_HOLDOUT_PRESSURE — FURTHER STRENGTHENED`

DEC-16 explicitly states that administrative and B4 interactions cross different boundaries. Current BA preserves boundary identities but cannot cleanly bind an independently identified interaction to the boundary it crosses.

# P-05 — ORDERED COMPARISON VOCABULARY
Carried unchanged; `greaterThan` remains confirmed missing evidence from FR-02.

# P-06 — DIRECT SCALAR / PROPERTY-ADDRESSING COMPARISON
Carried unchanged.

# P-07 — STRUCTURED DATA / INFORMATION CONTRACT
**R7 status:** `OPEN — STRONG` — no new structural counterexample from FR-23/24/25.

# P-08 — DATA ARTIFACT / STORE / PERSISTENCE ASSOCIATION
**R7 status:** `OPEN — STRONG` — carried from R6. Token storage is `NOT_DOCUMENTED_UNASSESSED`, not new P-08 evidence.

# Unnumbered holdout pressure evidence — TOKEN ACQUISITION / REFRESH

**Status:** `GOVERNED COUNTEREXAMPLE — POST-HOLDOUT REVIEW REQUIRED`

```text
DermaTriageB4Client MUST obtain B4BearerJWT
DermaTriageB4Client MUST refresh / renew B4BearerJWT
```

Rejected approximations:

```text
create -> would assert issuance by client
produce -> would assert token origin at client
observe -> obtain != mere read/query
transition -> token states not governed
consumeService -> no auth/token service identity governed
transfer -> acquisition issuer/source not governed
```

Discipline:

```text
counterexample != automatic new acquire operator
counterexample != automatic new pressure ID during frozen holdout
```

Post-holdout review must compare possible minimal solutions after full corpus analysis.
