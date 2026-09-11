# CC-04 `initiate` Question Pack R1

## Status

`CANDIDATE_TESTED_POSITIVE / NON-NORMATIVE / NOT_ADMITTED`

```text
candidateId: CC-04
candidateName: initiate
owningPressures: PR-03, PR-10
empiricalStatus: CANDIDATE_TESTED_POSITIVE
admissionStatus: NOT_ADMITTED
formalGate: G1_G8_PENDING
```

## Minimum meaning and signature

```text
initiate
    initiator -> BAReferent [1]
    initiated -> BAReferent [1]
```

The candidate asserts that a governed initiator directly starts or requests execution/activation of
a governed target.

## Positive controls

FR-21:
```text
DirectClient -> POST /analyze
POST /analyze -> DermaTriageTriageProcess
```

FR-04:
```text
DermaTriage -> PromptEvolutionCycle
condition: PromptEvolutionThresholdReached
```

FR-05:
```text
DermaTriage -> ClassifierAdaptationCycle
condition: ClassifierAdaptationThresholdReached
```

## Existing-construct exhaustion

`transfer` fails when no governed content role exists.

`consumeService` fails for endpoint-to-process and actor-to-cycle initiation.

`produce` preserves output semantics but not initiator topology.

`dependOn` preserves prerequisite/dependency, not directed initiation.

`reference` is too weak.

`create` would invent new occurrence/identity for the cycles.

`transition` would invent lifecycle state change for FR-04/FR-05.

`decisionRule` would invent a result assignment where the consequent is action.

## Trigger reconciliation

A condition becoming true is not itself the initiator.

```text
threshold reached != caller
```

Represent the governed consequent directly and attach the condition to that proposition.

## Negative controls

FR-10: support for revocation/restoration does not establish automatic rollback initiation.

FR-25: calls toward B4 do not justify inventing a specific endpoint/operation target.

FR-16 / FR-01 / FR-03: existing operator + condition; no initiation required.

FR-27: already-activated cycle context; do not duplicate initiation.

## `initiationKind` experiment

Tested:

```text
REQUEST
START
```

After deleting the kind while retaining initiator, initiated, target identity/type, conditions and
adjacent propositions:

```text
independently governed information lost: NONE IDENTIFIED
```

Disposition:

```text
REJECT_REDUNDANT_OVER_SPECIFIC
```

## Non-implications

`initiate` does not imply success, completion, synchronous execution, transfer, service consumption,
creation, lifecycle transition, automatic trigger, authorization or responsibility.

## Delete test

Remove CC-04 while retaining the frozen 14 operators and current condition semantics.

Lost:
- FR-21 caller/endpoint/process topology;
- FR-04 / FR-05 actor-to-cycle initiation identity.

Current result:

```text
CC-04 SURVIVES DELETE TEST
```

## Projection value

Potential queries include:
- what initiates operation/process X?
- what does endpoint E initiate?
- which cycles can actor A initiate?
- which initiations are conditionally governed?
- which externally reachable initiation chains exist?

## G1-G8 readiness

```text
G1 Source evidence: STRONG CURRENT-CORPUS POSITIVE
G2 General formulation: PROVISIONAL
G3 Construct exhaustion: PASS_CURRENT_CORPUS
G4 No false semantics: PROVISIONAL_PASS_WITH_STRICT_BOUNDARIES
G5 Minimality: PASS_CURRENT_CORPUS / two roles only
G6 Non-redundancy: PROVISIONAL_PASS
G7 Backward compatibility: PENDING
G8 Projection/feedback value: POSITIVE / FORMAL REVIEW PENDING
```

No normative method delta is admitted by this pack.
