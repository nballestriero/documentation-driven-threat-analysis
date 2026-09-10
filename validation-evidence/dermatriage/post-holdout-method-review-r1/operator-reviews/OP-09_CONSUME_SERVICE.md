# DDTA R25 — OP-09 `consumeService` Review

## Review identity

```text
review_id: OP-09
review_kind: OPERATOR_WITHIN_SEMANTIC_FAMILY
semantic_family: SF-01 FLOW_CONSUMPTION_SERVICE
status: COMPLETE_GUIDE_CLARIFICATION
frozen_method: BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
baseline_commit: 89da80e0459ba2a3578c961fb8f6e71b213bb99c
```

## 1. Frozen construct

```text
consumeService
    consumer -> BAReferent [1..*]
    service  -> BAReferent [1]
    provider -> BAReferent [0..1]
```

Frozen meaning:

```text
Assert actual consumption/use of a capability/service
without transferring ownership/responsibility.
```

## 2. Source-complete review framing

The complete governed DermaTriage source was reviewed for:

```text
explicit service/system consumption
data/evidence consumption
service exposure
endpoint/path invocation
technology/component use
query/read behavior
production/input flow
authentication gates
service ownership/responsibility boundaries
```

The search was not limited to the source word `consume`.

## 3. Strong positive evidence — FR-22

FR-22 governs that, when the B4-integrated path is invoked, DermaTriage obtains applicable
information/documents from B4, executes triage and keeps the outcome associated to the same
consultation.

Crucially, the source explicitly states that B4 remains an external service/system consumed by
DermaTriage and is not the owner of the triage evaluation.

This is direct positive evidence for:

```text
consumeService
    consumer -> DermaTriage
    service  -> B4
```

No distinct provider identity is invented.

## 4. Why `produce` is not enough

The source also supports production semantics:

```text
produce
    actor  -> DermaTriage
    input  -> ConsultationData
    input  -> CaseDocuments
    result -> B4CorrelatedTriageOutcome
```

Removing `consumeService` loses the independent fact that B4 itself is a consumed external
service/system.

Therefore:

```text
produce != consumeService
```

## 5. Why `transfer` is not enough

B4 provides data/documents to DermaTriage.

A transfer proposition can preserve content conveyance, but not the autonomous service-use meaning.

Therefore:

```text
transfer != consumeService
```

## 6. Why `correlate` is not enough

Correlation preserves same-consultation/case binding.

It does not preserve service use.

Therefore:

```text
correlate != consumeService
```

## 7. Data/evidence boundary — FR-18 / FR-19

FR-18 explicitly states:

```text
HistoricalCaseContext consumed by BioMistral-7B
```

FR-19 governs multi-source use of image classification, clinical description, historical context and
symptom information.

These are data/result/evidence consumption cases.

They are not `consumeService`.

Disposition:

```text
PR-11 / CC-01 consumeData
    source evidence STRONG
    construct admission NOT_AUTHORIZED
```

The PR-11 review must still test whether existing composition preserves all required meaning.

## 8. ChromaDB boundary

FR-18 governs indexing/querying in ChromaDB and retrieval by cosine similarity.

This demonstrates actual technology/system use but does not independently prove that the correct BA
meaning is service consumption.

Existing/adjacent meanings include:

```text
observe/query
produce input/result
realize capability with ChromaDB
store/persistence
```

Disposition:

```text
TECHNOLOGY_USE_POSITIVE
CONSUMESERVICE_NOT_ESTABLISHED
ROUTE_OP10_REALIZE_AND_PR08
```

This is a strong control against overloading `consumeService`.

## 9. Endpoint / invocation boundary — FR-21

FR-21 governs:

```text
DirectClient invokes POST /analyze
POST /analyze invokes DermaTriageTriageProcess
```

DEC-14 separately states that the DermaTriage service is exposed through FastAPI/Uvicorn.

The source therefore exposes distinct semantic targets:

```text
service/capability
endpoint/path
invoked process
realization/exposure technology
```

Disposition:

```text
SERVICE_USE_SEMANTICS_SUPPORTED
INDEPENDENT_CONSUMESERVICE_PROPOSITION_RECONCILE_WITH_PR03
ENDPOINT_IS_NOT_SERVICE
```

The strong positive control remains FR-22.

## 10. Authentication controls

FR-24 and FR-25 govern API-key/JWT authentication behavior.

Credentials and auth guards are not the consumed service itself.

```text
authentication requirement
    != consumeService
```

## 11. Internal model/component controls

EfficientNet-B4, Qwen, BioMistral and other internal technologies participate in processing and may
produce/consume data.

Do not infer:

```text
DermaTriage consumeService each internal component
```

from containment/participation alone.

## 12. Prompt/configuration controls

PromptVersion use is configuration/data applicability, not automatically service consumption.

Route to PR-14 / persistence/selection semantics as appropriate.

## 13. Refined application rule

Use `consumeService` only when all are source-grounded:

```text
1. a genuine consumer identity;
2. an independently identifiable service/capability identity;
3. actual functional use/consumption;
4. source scope of that use.
```

Do not require the service to be abstract. A concrete system may serve as the term if the source
governs that system itself as the service/capability being consumed.

## 14. Non-inferences

Do not infer `consumeService` from:

```text
data is consumed
endpoint is invoked
technology is used
component is contained
service is merely exposed
credential is required
content is transferred
state is queried
result is produced
dependency exists
```

Any of those meanings may coexist only when separately governed.

## 15. Question-pack result

The final OP-09 pack contains 25 questions.

Most decisive:

```text
Q1  what is consumed?
Q2  does the service/capability have independent governed identity?
Q3  is there actual use rather than availability/exposure?
Q10 endpoint/invocation boundary
Q12 technology/component boundary
Q13 realize boundary
Q20 delete test
Q23 capability identity falsification
Q24 interface replacement diagnostic
Q25 genuine consumer relation
```

## 16. Signature review

### `consumer [1..*]`

Lower bound is supported.

Plural cardinality is not sufficiently exercised by current DermaTriage evidence.

Disposition:

```text
KEEP_FROZEN
PLURAL_BEHAVIOR_NOT_SUFFICIENTLY_TESTED
```

### `service [1]`

Direct positive evidence supports exactly one service per proposition in the current strong case.

Disposition:

```text
KEEP_FROZEN
```

### `provider [0..1]`

A distinct provider is plausible and method-general, but DermaTriage does not sufficiently test an
independently governed provider distinct from service/owner/responsible party.

Disposition:

```text
KEEP_FROZEN
ROLE_EMPIRICALLY_NOT_SUFFICIENTLY_TESTED
```

No absence-of-evidence deletion is authorized.

## 17. `provideService?` candidate

R26 characterized `CC-02 provideService`.

OP-09 does not prove that a new operator is required.

The candidate remains:

```text
CANDIDATE_CHARACTERIZED
NOT_ADMITTED
```

Required construct exhaustion:

```text
consumeService.provider
OP-10 realize
OP-11 assignResponsibility
PR-01 performs/executes
PR-03 invocation/exposure
```

## 18. `consumeData?` candidate

R27 strengthens the source evidence for the semantic slot:

```text
HistoricalCaseContext consumed by BioMistral
multi-source synthesis inputs are functionally used
clinical/evidence inputs are consumed downstream
```

But source-supported semantic slot does not equal a required top-level operator.

Disposition:

```text
CC-01 consumeData
    CANDIDATE_CHARACTERIZED
    sourceEvidence STRONG
    NOT_ADMITTED
    owner PR-11
```

## 19. Whole-operator redundancy

Falsified by FR-22.

No frozen existing operator or tested composition preserves the service-use fact itself without
loss.

## 20. Documentation QA

The source is unusually clear for B4 because it explicitly states service/system consumption and
ownership separation.

Potential clarity opportunities in other projects:

```text
distinguish service/capability from endpoint
distinguish provider from owner/responsible party
distinguish data consumption from service consumption
distinguish concrete technology from stable capability
```

These are authoring observations, not automatic governed gaps.

## 21. G1–G8

No OP-09 method delta is proposed, so no new-construct G1–G8 admission is performed.

Adjacent candidates remain blocked.

## 22. FINAL_BA_TRACE

```text
FR-22
    preserve consumeService(DermaTriage, B4)

FR-18 HistoricalCaseContext -> BioMistral
    do not encode as consumeService
    carry to PR-11 / CC-01

FR-21 DirectClient -> /analyze
    preserve invocation pressure
    reconcile stable service use with PR-03

FR-18 ChromaDB
    do not automatically encode consumeService
    carry to OP-10 / PR-08

FR-24/25
    authentication semantics, not service consumption itself
```

## 23. Local verdict

```text
COMPLETE_GUIDE_CLARIFICATION
TESTED_POSITIVE_STRONG
operator core KEEP_NO_CHANGE
whole-operator redundancy FALSIFIED
signature KEEP_NO_CHANGE
candidate method delta NONE
```

## 24. Next review

`OP-10 realize` within `SF-02 CAPABILITY_REALIZATION_EXECUTION`.
