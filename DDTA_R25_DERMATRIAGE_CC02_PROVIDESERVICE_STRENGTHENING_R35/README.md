# DDTA R25 — CC-02 `provideService` strengthening R35

This checkpoint consolidates the full-corpus service/API/interface re-review performed at exact
baseline:

```text
68c8a387790c92c7f7e3859bfebd400fa29e242a
```

It makes no normative BA0–BA5 change. The BA2 top-level operator count remains 14.

## Main result

`CC-02 provideService` is strengthened from:

```text
CANDIDATE_INSUFFICIENT_EVIDENCE
```

to:

```text
CANDIDATE_TESTED_POSITIVE
NOT_ADMITTED
G1-G8_PENDING
```

The strongest current DermaTriage positive control is the DEC-14 / FR-21 combination:

- the documentation independently governs DermaTriage as the system/project actor;
- it explicitly governs a DermaTriage service;
- the service is made available through a governed interface;
- `POST /analyze` is governed as a reusable interface endpoint and is separately invoked;
- provision remains meaningful independently of actual service consumption.

## Working minimum meaning

```text
provideService(provider, service)
    = provider makes/offers a governed service/capability as a service
```

Minimum working signature:

```text
provider -> BAReferent [1]
service  -> BAReferent [1]
```

Plurality and final cardinality remain pending integrated review.

`provideService` does **not** automatically mean:

```text
consumer exists
service is currently consumed
provider owns the service
provider bears all responsibility for the service
provider realizes/implements the service
a specific endpoint exists
the service is reachable/healthy at runtime
```

## Why `consumeService` does not absorb provision

`consumeService` asserts actual functional use/consumption.

A service may be governed as offered/provided even when no particular consumption occurrence is
being asserted. Therefore:

```text
provideService != consumeService
```

When a consumer is explicitly governed, both propositions may coexist if both meanings matter.

## Why `assignResponsibility` does not absorb provision

Responsibility/authority and provision remain independent:

```text
provides service
    !=
is responsible for service
```

The existing OP-11 review had already established this boundary.

## Why `realize` does not absorb provision

Implementation/materialization and service provision remain independent:

```text
realizes capability
    !=
provides service
```

DEC-14 / FR-21 exposure through FastAPI/Uvicorn does not by itself establish an
abstract-to-concrete realization relation.

## Exposure result

The source wording `expose` is retained as evidence but does not justify an autonomous operator.

In the current corpus the material meaning can be decomposed into:

```text
service offering
    -> provideService

reusable endpoint identity
    -> BAReferent when independently reused/qualified

normatively governed endpoint/interface properties
    -> constrain

actual service use
    -> consumeService

content flow
    -> transfer

caller/callee relation
    -> invoke ?   [still open]
```

Therefore:

```text
generic expose operator
    NOT_JUSTIFIED
```

No `CC-04 expose` is allocated.

## Endpoint discipline

`POST /analyze` is a strong reusable-identity case because it is independently qualified and
participates in the governed call chain.

`POST /diagnose` is likewise a governed endpoint identity in the B4-integrated path.

The current documentation does **not** authorize treating `/analyze` and `/diagnose` as a closed,
complete vocabulary of all DermaTriage endpoints.

FR-24 governs protected administrative operations and their X-API-Key requirement, but does not
govern concrete paths for every operation. Do not invent those paths.

DEC-15 / FR-23 govern use of B4 APIs, but do not govern exact B4 endpoint paths. Do not invent them.

## Next review

Do not consolidate the remaining PR-03 invocation facet yet.

Next:

```text
PR-03 invoke
    versus
PR-10 trigger
```

The purpose is to determine whether invocation is an independently necessary caller-to-operation
relation or a specialized case of a more general activation/trigger semantics.
