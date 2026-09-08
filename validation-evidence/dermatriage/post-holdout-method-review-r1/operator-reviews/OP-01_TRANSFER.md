# OP-01 — `transfer` Review

## Review identity

```text
review_id: OP-01
review_kind: OPERATOR
status: COMPLETE_GUIDE_CLARIFICATION
frozen_method: BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1
baseline_commit: c8902f6e2f4280dfe7543767c20910a79174b0e6
```

## 1. Construct under review

### Frozen BA2 R3 meaning

`transfer` asserts conveyance of content from a source to one or more destinations. When the transfer behavior itself requires reusable project-semantic identity, optional role `behavior` may bind that behavior to a `BAReferent`.

```text
transfer
  behavior    -> BAReferent [0..1]
  source      -> BAReferent [1]
  destination -> BAReferent [1..*]
  content     -> BAReferent [1..*]
```

Authority: `methodology/BA2_RELATION_ACTION_VOCABULARY_R3.md`.

## 2. Governed source evidence

### DEC-14 — B4 / DermaTriage exchange

Source: `governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`, `DEC-14`.

Evidence-bearing meaning:

- B4 participates in data exchange with DermaTriage;
- `POST /diagnose` consumes consultation/documents/images made available by B4;
- DermaTriage produces and returns the triage outcome;
- B4 does not acquire triage responsibility.

Governed semantic claims relevant to `transfer`:

```text
B4 -> DermaTriage : consultation / documents / images
DermaTriage -> B4 : triage outcome
```

The ownership/responsibility statement is separate and must not be absorbed by `transfer`.

### FR-22 — integrated B4 triage

Source anchor: `FR-22`.

Evidence-bearing clause:

> When `POST /diagnose` is invoked for a B4 consultation, DermaTriage must acquire the applicable information/documents from B4, execute triage, and retain association with the same consultation.

SPO support includes:

```text
B4 -- provides --> ConsultationData
B4 -- provides --> CaseDocuments
DermaTriage -- consumes --> ConsultationData
DermaTriage -- produces --> B4CorrelatedTriageOutcome
```

This distinguishes conveyance/provision, consumption, production, and correlation.

### FR-23 — validation write-back / retrieval

Source anchor: `FR-23`.

Evidence-bearing meaning:

- diagnostic-output write-back;
- medical-validation write-back;
- retrieval of validated outcomes;
- same consultation/case identity retained across those interactions.

SPO support:

```text
DermaTriage -- writes back --> B4TriageOutcome
ClinicianValidation -- written back to --> B4
B4 -- provides --> ValidatedOutcome
ValidatedOutcome -- correlatedWith --> OriginalDermaTriageOutcome
```

The conveyance parts are transfer-compatible. Same-case binding remains `correlate` semantics and must not be inferred from transfer direction.

### FR-21 / FR-25 — adjacent interaction evidence

`FR-21` states:

```text
DirectClient -- invokes --> POST /analyze
POST /analyze -- invokes --> DermaTriageTriageProcess
```

`FR-25` states that the DermaTriage B4 client obtains/refreshes and presents a bearer JWT for authenticated calls toward B4.

These are important counterexamples to overloading `transfer`: invocation/authentication direction is not the same thing as content-flow direction.

## 3. Previous BA / holdout representation

R1 working snapshot accepted:

```text
BAPROP-DERMA-DEC14-001
transfer
  source      -> B4
  destination -> DermaTriage
  content     -> B4Consultation
  content     -> B4Documents
  content     -> B4Images
```

and:

```text
BAPROP-DERMA-DEC14-002
transfer
  source      -> DermaTriage
  destination -> B4
  content     -> TriageOutcome
```

R11 final construct ledger records:

```text
transfer          TESTED_POSITIVE_STRONG
transfer.behavior TESTED_POSITIVE_CROSS_CORPUS_STRONG
```

No artificial positive case is needed.

## 4. Representation experiments

### A — simple transfer

```text
transfer
  source      -> B4
  destination -> DermaTriage
  content     -> ConsultationData
```

Preserves: conveyance direction and content identity.

Does not assert: who initiated the interaction, invocation path, authentication order, boundary crossing, consumption, persistence, success, retry, rate limits, or responsibility.

Result: **accepted default form**.

### B — mechanical `behavior` on every transfer

```text
transfer
  behavior    -> B4ConsultationDelivery
  source      -> B4
  destination -> DermaTriage
  content     -> ConsultationData
```

If no other governed fact needs to target `B4ConsultationDelivery`, the extra referent adds identity without analytical need.

Result: **rejected as default authoring practice**.

### C — `behavior` when the transfer itself is independently qualified

Cross-corpus Facial Access evidence requires reusable identity for a delivery because service, medium and security properties target that exact delivery segment.

```text
transfer
  behavior    -> RecognitionCaptureDelivery
  source      -> CameraSubsystem
  destination -> RecognitionProcessor
  content     -> RecognitionCapture
```

Result: **accepted admission case**. `behavior` remains optional and valid.

### D — add `initiator` directly to `transfer`

Rejected during OP-01.

Reason: `source/destination` describe the direction of conveyed content. Interaction initiation may differ in request/response, push, subscription/notification, callback, or event-driven patterns. A single `initiator` role would be ambiguous between interaction initiator, request sender, response sender, or causal trigger.

Route the need to `PR-03 INTERFACE_PATH_INVOCATION_ASSOCIATION` rather than overloading `transfer`.

## 5. Existing-construct exhaustion and semantic boundaries

```text
transfer != produce
transfer != consumeService
transfer != data/evidence consumption
transfer != invoke/request
transfer != dependOn
transfer != persist/store association
transfer != boundary crossing
transfer != correlate
transfer != assignResponsibility
```

Two propositions may coexist when both meanings are governed. Example:

```text
DermaTriage produces TriageOutcome
DermaTriage transfers TriageOutcome to B4
```

Similarly, receipt/conveyance does not automatically establish semantic consumption.

## 6. All-occurrences coverage

Material transfer-like DermaTriage evidence checked in the governed R1 corpus:

- DEC-14 data exchange and outcome return;
- FR-21 direct invocation as a negative/adjacent case;
- FR-22 B4-provided data and correlated outcome production;
- FR-23 write-back/retrieval flows;
- FR-25 authenticated calls toward B4 as interaction-direction evidence;
- previous R1 BA transfer propositions;
- R11 final construct-test status;
- Facial Access cross-corpus `transfer.behavior` counterexample embedded in BA2 R3.

No source evidence reviewed requires a change to core `transfer` semantics.

## 7. Transfer question-pack evaluation

The full candidate pack is stored in `question-packs/TRANSFER_QUESTION_PACK_R1.md`.

Important observed results on DermaTriage:

| Question | Result | Disposition |
|---|---|---|
| What content moves, from where to where? | DEC-14 / FR-22 / FR-23 provide material answers. | ANSWERED |
| Who initiates the interaction? | Direct path explicitly names `DirectClient`; B4-related flows have different call directions and FR-22 does not reduce them to one universal initiator. | CLARITY_OPPORTUNITY / route PR-03 |
| Push, pull, request/response, notification? | Not uniformly governed for all transfer cases. | CLARITY_OPPORTUNITY / route PR-03 |
| Which interface/path is used? | `/analyze`, `/diagnose` and B4 calls are governed in relevant scopes. | ANSWERED, but relation semantics belong PR-03 |
| Does it cross a governed boundary? | B4/DermaTriage boundary is explicit. | ANSWERED, relation semantics belong PR-04 |
| Authentication mechanism? | B4 interaction uses bearer JWT in governed scope. | ANSWERED |
| Authentication before material resource allocation? | Not governed by the reviewed source. | CLARITY_OPPORTUNITY, not a requirement |
| Rate/frequency bounds, queue, timeout, retry, backpressure? | No general governed answer found for the reviewed transfer cases. | CLARITY_OPPORTUNITY unless later scope makes NOT_APPLICABLE/GOVERNED_GAP |
| Same-request/case correlation required? | Explicitly required in B4 validation/integrated flows. | ANSWERED; represent separately with `correlate` |

The pack is diagnostically useful because it exposes security-analysis-relevant distinctions without turning them into BA facts when the source is silent.

## 8. Rejected alternatives / non-inferences

Do not infer from a transfer alone:

- interaction initiator;
- request/response causality;
- synchronous/asynchronous semantics;
- push/pull mode;
- protocol or medium;
- authentication or authorization ordering;
- queue, timeout, retry, rate limit, backpressure;
- transfer success or acknowledgement;
- boundary crossing;
- semantic consumption of received data;
- persistence;
- ownership/responsibility;
- correlation with a prior request/case.

## 9. Local verdict

```text
COMPLETE_GUIDE_CLARIFICATION
```

Operator disposition:

```text
transfer core       KEEP / NO_CHANGE
transfer.behavior   KEEP / OPTIONAL REIFICATION ROLE
normative BA change NONE
```

Candidate future guide improvements:

1. present `source / destination / content` as the default human-facing form;
2. explain `behavior` only through the independent-reusable-identity admission test;
3. include a transfer-specific diagnostic question pack;
4. explicitly state `content-flow direction != interaction initiation`.

## 10. Generalization and minimality

The distinction is method-general: any system may have request/response, push, subscription, callback, event-driven or asynchronous flows where conveyed-content direction differs from interaction initiation.

Minimality favors leaving `transfer` unchanged and routing interaction semantics to a separate review.

## 11. G1–G8

No normative BA delta is proposed by OP-01, so G1–G8 admission is not required for a BA contract change.

The guide-only candidate is source/cross-corpus supported, minimal, backward compatible, and improves reproducibility/non-inference behavior.

## 12. FINAL_BA_TRACE

Later DermaTriage BA reconstruction must be able to recover at minimum:

```text
DEC-14 / FR-22
B4 -> DermaTriage : applicable consultation/data/documents/images

DEC-14
DermaTriage -> B4 : triage outcome

FR-23
DermaTriage / clinician-validation write-back toward B4
B4 -> DermaTriage : validated outcome where source supports the direction
```

Preserve separately:

- production of outcomes;
- semantic consumption of received data;
- same-consultation/case correlation;
- interface/path invocation;
- boundary relation;
- authentication;
- any later accepted initiation/push-pull semantics.

Explicit non-inference: no transfer proposition alone establishes requester/initiator, rate limit, queue, timeout, retry, or authentication order.

Dependencies: `PR-03`, `PR-04`, `PR-11`; persistence only if later content/store evidence requires `PR-08`.

## 13. Documentation QA

The transfer question pack demonstrates useful documentation feedback without changing project truth.

- exchange direction/content: generally `ANSWERED` in B4 flows;
- direct-path invocation: `ANSWERED`;
- universal interaction-initiation semantics across B4 flows: `CLARITY_OPPORTUNITY`;
- rate/queue/timeout/retry/backpressure: `CLARITY_OPPORTUNITY` unless a later project scope establishes necessity;
- B4 authentication mechanism: `ANSWERED`;
- authentication-vs-resource-allocation ordering: `CLARITY_OPPORTUNITY`.

No unanswered question is automatically promoted to a requirement or documentation-method change.

## 14. Open/deferred questions

- interaction initiation / request-response / push-pull: `PR-03`;
- relation of transfer to interface/path: `PR-03`;
- explicit boundary crossing relation: `PR-04`;
- data/evidence consumption after receipt: `PR-11`;
- persistence after receipt: `PR-08` only where source evidence requires it.

## 15. Per-construct consolidation result

OP-01 is closed for the operator-audit phase.

```text
next review: OP-02 produce
```
