# DermaTriage Holdout Observations — R7

Observations are evidence / candidate documentation-quality lessons, not BA0–BA6 changes.

# O-02 — SOURCE VERB != BA OPERATOR
Carried and reinforced. `obtains token` is not automatically `create`, `produce`, or `observe`.

# O-03 — DATA / INTERACTION COMPLETENESS
Continue to assess, where material: WHAT, WHO, FROM, TO, OPERATION, INTERFACE/PATH, SERVICE, CONNECTION/CHANNEL, TRANSPORT/PROTOCOL, MEDIUM, BOUNDARY, SECURITY/TRUST QUALIFICATION, CREDENTIAL/AUTHENTICATION DETAIL.

# O-04 — LOGICAL DATA FLOW != PHYSICAL DATA EXCHANGE
`B4 APIs` does not establish HTTP/TLS/TCP/network/physical-medium details.

# O-05 — SERVICE CONSUMPTION != DATA TRANSFER != RESPONSIBILITY
Carried and reinforced.

# O-06 — INTENTIONAL DECOMPOSITION STOP != DOCUMENTATION GAP
Carried.

# O-07 — SEMANTIC PRESERVATION != STORAGE IMPLEMENTATION
Carried.

# O-08 — RECORDING != ORIGIN / AUTHORSHIP
Carried.

# O-09 — DOCUMENTATION DETAIL MUST BE INTENTIONAL
Use `DOCUMENTED`, `NOT_DOCUMENTED_UNASSESSED`, `CONSIDERED_NOT_REQUIRED`, `DEFERRED`, `OUT_OF_SCOPE`, `UNKNOWN_REQUIRED`, `NOT_APPLICABLE`. Absence is first assessed, then classified.

# O-10 — AUTHENTICATION != TRANSPORT PROTECTION

Known authentication mechanisms (`X-API-Key`, bearer JWT) do not authorize inference of HTTPS, TLS, confidentiality, integrity, server authentication, mutual authentication, private network, or encrypted medium.

# O-11 — AUTHENTICATION MECHANISM != CREDENTIAL INSTANCE / LIFECYCLE

```text
BearerJwtAuthenticationMechanism -> authentication policy/mechanism
B4BearerJWT -> credential/token project meaning
B4BearerJwtTokenLifecycleManagement -> acquisition/refresh responsibility scope
```

Therefore:

```text
mechanism != credential
credential != acquisition
acquisition != refresh
refresh != token creation
authentication != transport protection
```

# MR-03 documentation-quality lesson

MR-03 demonstrates a layered review:

```text
clinical authority
review meaning
persistence
correlation
service exchange
interface
boundary
authentication mechanism
credential
credential lifecycle
transport/channel detail
```

DDTA should make these layers visible so omitted levels can be consciously accepted, deferred, scoped out, or identified as required gaps instead of remaining accidental blind spots.
