# CC-02 `provideService` Question Pack R2

## Status

`CANDIDATE_TESTED_POSITIVE / NON-NORMATIVE / NOT_ADMITTED`

R2 supersedes R1 for current empirical disposition. R1 remains historical evidence.

```text
candidateId: CC-02
candidateName: provideService
empiricalStatus: CANDIDATE_TESTED_POSITIVE
admissionStatus: NOT_ADMITTED
formalGate: G1_G8_PENDING
```

## A. Minimum source meaning

```text
Provider P makes/offers independently governed Service S as a service.
```

The proposition must not be created from data provision, endpoint exposure, responsibility,
realization or actual consumption alone.

## B. Strong positive control — DEC-14 / FR-21

The current DermaTriage corpus independently governs:

```text
DermaTriage
DermaTriage service
service/interface availability
POST /analyze
direct invocation through that endpoint
```

This resolves the previous R1 problem that no sufficiently clean provider/service case had been
identified.

Working proposition:

```text
provideService
    provider -> DermaTriage
    service  -> DermaTriageService
```

Final canonical referent naming remains for integrated BA reconstruction.

## C. Existing-construct exhaustion

### `consumeService`

Actual service use is not standing provision.

```text
consumeService != provideService
```

A provider/service relation can be meaningful even when no consumer occurrence is currently being
asserted.

### `assignResponsibility`

Provision does not establish governance responsibility or authority.

```text
assignResponsibility != provideService
```

### `realize`

Implementation/materialization does not establish service provision.

```text
realize != provideService
```

### `transfer`

Content conveyance does not establish service provision.

```text
transfer != provideService
```

### `produce`

Producing a result does not establish that the actor offers an independently governed service.

```text
produce != provideService
```

### PR-03 exposure

Endpoint/interface exposure is a technical/service-access facet. In the current corpus it can be
decomposed without replacing provider-to-service meaning.

## D. Exposure boundary

Do not infer `provideService` merely from:

```text
FastAPI exposes endpoint E
```

unless provider and service identities and their offering relation are independently source-grounded.

For DermaTriage, the broader DEC-14 / FR-21 context supplies the necessary service-level meaning.
The positive control is the complete governed context, not the word `expose` alone.

## E. Endpoint representation

An endpoint may be promoted to BAReferent when it is independently reused or qualified.

Example current-corpus case:

```text
POST /analyze
    independently constrained
    invoked by DirectClient
    invokes DermaTriageTriageProcess
```

Governed method/path/framework/authentication restrictions may be represented with `constrain`
when the source actually establishes a reusable/queryable restriction.

Do not infer a closed endpoint inventory from a partial list.

Do not invent endpoint paths for FR-24 administrative operations or B4 API interactions where the
source does not govern them.

## F. Negative controls

```text
B4 provides ConsultationData
    != provideService automatically

FastAPI exposes an endpoint
    != provideService automatically

component realizes capability
    != provideService

party is responsible for a service
    != provideService

client consumes service
    != provider-service relation automatically

actor produces output
    != provideService
```

## G. Delete test

Remove the provider-to-service relation while keeping:

```text
endpoint identities
endpoint constraints
actual service consumption
content transfers
responsibility
realization
invocation
```

Current result:

```text
provider-to-service standing relation is no longer deterministically recoverable
without adding assumptions
```

Therefore CC-02 survives the current delete test.

## H. Projection value

Potential deterministic queries:

```text
who provides service S?
which services are provided by P?
which offered services have no governed consumer?
which provided services have endpoint/authentication constraints?
which service-provider changes affect interface or threat projections?
```

## I. Working signature

```text
provideService
    provider -> BAReferent [1]
    service  -> BAReferent [1]
```

This is a minimum current-corpus hypothesis only.

Plurality, alternative provider multiplicity, delegation and shared provision remain untested.

## J. G1–G8 readiness

```text
G1 Source evidence:
    STRONG CURRENT-CORPUS POSITIVE

G2 General formulation:
    PROVISIONAL

G3 Construct exhaustion:
    PASS_CURRENT_CORPUS

G4 No false semantics:
    PROVISIONAL_PASS_WITH_STRICT_BOUNDARIES

G5 Minimality:
    PROVISIONAL_PASS

G6 Non-redundancy:
    PROVISIONAL_PASS

G7 Backward compatibility:
    PENDING

G8 Projection/feedback value:
    POSITIVE / FORMAL REVIEW PENDING
```

No normative method delta is admitted by this pack.
