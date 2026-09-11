# PR-03 / PR-10 Initiation Reconciliation R1

## Status

`SOURCE-COMPLETE CONCEPTUAL REVIEW / NON-NORMATIVE`

## Scope

The complete governed DermaTriage corpus was reviewed for invocation, calls, conditional activation,
generic `when` clauses, start/trigger wording, rollback/revocation, B4 calls, fallback and
already-activated cycle contexts.

## Result

A narrower directed-initiation candidate survives:

```text
CC-04 initiate
    initiator -> BAReferent
    initiated -> BAReferent
```

No normative operator is added.

## PR-03 invocation facet

FR-21 proves irreducible directed topology:

```text
DirectClient -> AnalyzeEndpoint
AnalyzeEndpoint -> DermaTriageTriageProcess
```

Existing frozen operators cannot reconstruct this topology without loss or false roles.

`invoke` is therefore retained as source evidence but absorbed into `initiate`.

## PR-10 trigger facet

FR-04 / FR-05 govern:

```text
condition satisfied
+
DermaTriage initiates adaptation cycle
```

The condition is not the caller/actor. The BA already supports proposition-local condition semantics.

```text
trigger primitive:
    NOT_JUSTIFIED

conditional initiation:
    initiate + condition

other conditional behavior:
    corresponding existing operator + condition
```

## Minimality test

`initiationKind = REQUEST | START` was explicitly tested and failed the delete test.

Target identity already preserves endpoint/process/cycle distinctions. Conditions preserve
conditional activation. `START` additionally risks unsupported creation/transition semantics.

```text
initiationKind:
    REJECT_REDUNDANT_OVER_SPECIFIC
```

## Boundary controls

FR-10:
- support for revocation/restoration;
- no automatic rollback initiation inference.

FR-25:
- authenticated calls to B4;
- no specific endpoint/operation target governed.

FR-16 / FR-01 / FR-03:
- conditional behavior;
- no initiation required.

FR-27:
- behavior for an already-activated retraining cycle;
- no duplicate start proposition.

## Candidate allocation

```text
CC-04 initiate
status: CANDIDATE_TESTED_POSITIVE
admission: NOT_ADMITTED
gate: G1-G8_PENDING
```

## Pressure reconciliation

```text
PR-03:
    exposure facet -> decomposed in R35
    invocation facet -> reconciled through CC-04

PR-10:
    generic trigger primitive -> not justified
    directed activation -> CC-04 + condition
```

Both pressures are locally reconciled for the current disposition phase, subject to final
completeness and integrated G1-G8 review.
