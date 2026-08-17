# DDTA BA4-T1 projection boundary, traceability and semantic-preservation trial - R1

**Status:** COMPLETED / PROVISIONAL PASS WITH PROJECTION-BOUNDARY LOWER-BOUND

**Repository baseline reviewed:** `ac49f02ca37d47e872b3ce5194f6dd0e26574d75`

**Executed scope:** BA4-T1 only.

## 1. Trial question

Can one accepted Base Analysis materialization support a human-oriented projection and a bounded method-oriented projection while preserving shared project meaning, explicit traceability and the governed-document authority boundary?

The trial is adversarial rather than demonstrative: every proposed projection convenience is tested for whether it silently adds shared meaning, hides lossiness, bypasses BA provenance or creates a second lifecycle authority.

## 2. Fixed input contract

The trial assumes only already-closed Base Analysis semantics:

```text
BA1
  BAReferent
  BAProposition

BA2
  semantic operator
  role-bound participation
  polarity
  condition / temporalScope where admissible

BA3
  baseline-scoped provenance
  GROUNDED / DERIVED / DIAGNOSTIC_UNRESOLVED
  review/freshness
  RETAIN / REPLACE / RETIRE
  role-bound derivation
  revalidationContext
```

No method-specific category is added to those inputs.

## 3. Primary facial-access BA slice

The pressure slice uses the already-reviewed shared meaning around recognition delivery:

```text
BAReferents
  CameraSubsystem
  RecognitionProcessor
  RecognitionCapture
  RecognitionRequest
  LocalConnectivity
  WiredEthernet
  underlying transport responsibility scope

BAPropositions
  transfer(CameraSubsystem,
           RecognitionProcessor,
           RecognitionCapture)

  correlate(RecognitionCapture,
            RecognitionRequest)

  consumeService(project,
                 LocalConnectivity)

  assignResponsibility[negative](project,
                                 underlying transport,
                                 ownership/management)

  realize(LocalConnectivity,
          WiredEthernet)

  constrain(delivery behavior,
            incomplete delivery != successful completion)

  constrain(delivery behavior,
            confidentiality / integrity / authorized provenance)
```

The exact physical materialization is intentionally irrelevant. The trial operates over the closed semantic responsibilities.

## 4. Human-oriented projection trial

### 4.1 Projection purpose

Create a compact human view of the recognition-delivery branch without requiring the reader to navigate raw governed prose.

### 4.2 Allowed transformation

The trial allows:

- selection of the relevant BA slice;
- ordering by reading intent rather than source-document order;
- human display labels;
- grouping under `Recognition delivery`;
- aggregation of explicit constraints into an enumerated protection group.

### 4.3 Produced view

```text
Recognition delivery

CameraSubsystem delivers RecognitionCapture to RecognitionProcessor.
The capture is correlated to RecognitionRequest.
The project consumes LocalConnectivity but does not own/manage
its underlying transport infrastructure.
LocalConnectivity is realized by WiredEthernet.
Delivery has explicit completion, confidentiality, integrity
and authorized-provenance constraints.
```

Every meaning-bearing sentence/group is trace-bound to the underlying BA referents/propositions.

### 4.4 Semantic-preservation checks

`deliver` is used only as a human display rendering of BA `transfer` with the same source/destination/content bindings.

The negative responsibility proposition remains negative.

The constraint group enumerates the underlying obligations rather than concluding `secure channel` or `safe delivery`.

Result: **PASS**.

## 5. Negative human-view controls

### H-N1 - stronger aggregate

Input:

```text
confidentiality constraint
integrity constraint
authorized provenance constraint
```

Candidate rendering:

```text
"the transport is secure"
```

Disposition: **REJECTED**.

Reason: the phrase is a stronger and ambiguous project conclusion. It is not a mere grouping/rename.

### H-N2 - erased polarity

Input:

```text
assignResponsibility[negative](project, transport, ownership/management)
```

Candidate rendering:

```text
"the project manages transport"
```

Disposition: **REJECTED**.

### H-N3 - omitted scope interpreted as false

A view omits concurrency/idempotency because its purpose is only recognition delivery.

Inference:

```text
omitted -> project has no such constraints
```

Disposition: **REJECTED**.

This is the concrete pressure that forces `selectionCoverageContract`.

## 6. Bounded method-oriented projection trial

### 6.1 Projection purpose

Create a flow-oriented threat-analysis view that can reason about interaction structure while leaving method taxonomy downstream.

No STRIDE category or full DFD schema is defined.

### 6.2 Projection-owned constructs

```text
MethodNode
MethodInteraction
MethodAnnotation
```

These constructs are local to the consumer projection.

### 6.3 Shared mapping

```text
CameraSubsystem
  -> MethodNode(camera)

RecognitionProcessor
  -> MethodNode(recognition)

transfer(CameraSubsystem,
         RecognitionProcessor,
         RecognitionCapture)
  -> MethodInteraction(camera -> recognition)
     payload = RecognitionCapture
```

Trace bindings preserve the source/destination/content BA meaning.

Result: **PASS** as projection mapping.

The method node and method interaction are not promoted into BA families.

## 7. Method-owned interpretation pressure

The method projection wants an exposure annotation associated with externally supplied transport.

Its BA basis is:

```text
serviceUse
  -> consumeService(project, LocalConnectivity)

responsibilityBoundary
  -> assignResponsibility[negative](project,
                                    underlying transport,
                                    ownership/management)
```

The projection may produce:

```text
MethodAnnotation:
  externally-provided-transport-exposure
```

Disposition: **ALLOWED AS METHOD-OWNED INTERPRETATION**.

It must remain:

- explicitly owned by the method/projection;
- trace-bound to the BA basis;
- outside BA1/BA2 shared semantics;
- unable to become a grounded BA source.

The same mapping promoted to a new BA proposition is **REJECTED** by this trial.

## 8. Why direct source extraction inside projection fails

Negative pattern:

```text
projection engine
  reads D-3.4 prose directly
  invents method node/edge/shared labels
  records only source locator
```

This bypasses the accepted shared BA representation and can reconstruct project meaning differently for each consumer.

Disposition: **REJECTED for shared DDTA projection semantics**.

A view may follow BA3 provenance to show source context, but the shared semantic basis must remain BA when BA already represents the needed project meaning.

This preserves the DDTA purpose that each method should not rediscover the same project facts from documentation independently.

## 9. Projection trace shape trial

### 9.1 Flat list pressure

A simple method interaction can trace to one `transfer` proposition plus participant referents.

A flat BA reference list is reviewable when every reference has obvious contribution.

### 9.2 Multi-input interpretation pressure

The exposure annotation uses service use and responsibility boundary for different purposes.

If the trace is only:

```text
[BA-P1, BA-P2]
```

an independent reviewer cannot know which input satisfies which part of the projection mapping contract.

Role-bound trace is therefore required **where contribution roles differ**:

```text
serviceUse             -> BA-P1
responsibilityBoundary -> BA-P2
```

Disposition: **PASS / REQUIRED WHEN ROLES DIFFER**.

The role keys remain projection-contract scoped and do not reopen BA2.

## 10. Projection-local identity pressure

### 10.1 Meaning-bearing item

A method interaction must be independently selectable and traceable in the view.

Without a projection-local address/key, trace inspection can only point to an unstable render position.

Disposition: **projection-local identity/address REQUIRED for meaning-bearing items**.

### 10.2 Layout primitive

A line segment or table cell has no independent semantic trace requirement.

Disposition: **no semantic identity required**.

### 10.3 Cross-baseline identity

T1 finds no evidence that projection items need BA-like semantic continuity across baselines.

A deterministic local key may be useful operationally, but `RETAIN | REPLACE | RETIRE` is not copied into projection semantics.

Disposition: **NOT REQUIRED BY T1**.

## 11. Coverage and completeness pressure

The bounded method projection selects interaction-oriented facts.

It may intentionally omit:

- some realization detail;
- unrelated fulfillment semantics;
- diagnostic records outside its purpose;
- constraints not consumed by this projection revision.

The consumer must be able to determine that the projection is selective.

Therefore the descriptor must expose sufficient selection/coverage semantics to answer:

```text
What BA elements are eligible for this projection?
What states are admissible?
Does absence mean out-of-scope or evaluated-not-matched?
```

BA4-T1 does not force a universal completeness metric or query language.

## 12. Diagnostic pressure

Consider an accepted BA diagnostic created by M4 because sibling representation context conflicts with an unchanged FR.

Negative projection:

```text
DIAGNOSTIC_UNRESOLVED transfer meaning
  -> current flow item without warning
```

Disposition: **REJECTED**.

A normal accepted/current projection excludes or visibly qualifies it according to the descriptor. A review-oriented projection may include the diagnostic explicitly.

This uses BA3 state rather than creating a projection-owned truth state.

## 13. M1 change replay - Ethernet to Wi-Fi

B0 projection contains:

```text
realization item -> WiredEthernet
```

BA3 B1 continuity says the old realization proposition is replaced by the Wi-Fi proposition, while the transfer proposition may be retained.

T1 projection rule:

```text
keep projection@B0 as historical
build projection@B1 from accepted BA@B1
```

Consequences:

- flow interaction remains materially equivalent if its traced `transfer` meaning is retained;
- realization display/method annotation uses Wi-Fi if selected by the projection;
- no projection item is semantically rewritten in B0;
- no second `REPLACE` state machine is required.

Result: **PASS**.

## 14. M3 change replay - remote to local recognition

BA3 retires the remote capture-transfer proposition.

Negative behavior:

```text
projection item existed in B0
  -> preserve it in B1 regardless of BA
```

Disposition: **REJECTED**.

Correct behavior:

```text
rebuild from BA@B1
  -> no remote interaction unless another accepted BA proposition supports it
```

Result: **PASS**.

## 15. M4 change replay - representation conflict

When the representation Decision changes while the old FR remains inconsistent, BA3 marks affected meaning stale/unresolved rather than silently rewriting it.

A method projection that bypasses BA and reads the Decision alone could fabricate a new interaction payload while governance remains inconsistent.

Disposition: **REJECTED**.

A projection must consume the accepted BA state. Review projections may expose the unresolved condition; normal current projections may not present stale meaning as current project truth.

This directly supports the projection->BA trace boundary.

## 16. Order/provider control

### 16.1 Human gate view

A human order-evaluation view selects:

```text
reservation result
payment authorization result
full-order gate/atomicity meaning
```

It may omit inventory-concurrency implementation detail under its coverage contract.

Omission is not absence. **PASS**.

### 16.2 Provider normalization

A method projection needs `PaymentAuthorizationResult`.

Correct:

```text
consume accepted BA normalized result
```

Rejected:

```text
read raw provider status
apply projection-private project mapping
present result as shared project meaning
```

The latter would recreate exactly the hidden mapping authority rejected by BA3-T3.

## 17. BAE-family pressure

Candidate additions considered:

```text
BAProjection
BAViewItem
DFDNode
MethodInteraction
```

None is forced as a BA1 family.

Reason:

- projection descriptor/materialization/item identity is consumer-artifact identity;
- method node/interaction identity belongs to the method-owned projection;
- shared project meanings remain traced BAReferents/BAPropositions;
- no subtype-specific shared invariant requires a third BAE family.

Disposition: **BA1 REOPEN NOT TRIGGERED**.

## 18. BA2/BA3 reopen pressure

The human and method projections obtain the needed shared project meaning from the closed BA2 operators/roles and BA3 provenance/lifecycle metadata.

No new methodology-neutral operator is needed.

No missing provenance or change mechanism appears.

Projection-specific mapping/trace roles are not BA2 roles, and method annotations are downstream.

Disposition:

```text
BA2 reopen  NOT TRIGGERED
BA3 reopen  NOT TRIGGERED
```

## 19. Minimal accepted T1 candidate

```text
Projection definition
  immutable revision
  consumer purpose
  selection/coverage contract
  mapping contract
  interpretation boundary

Projection materialization
  source BA baseline
  meaning-bearing items

Meaning-bearing item
  projection-local key/address
  projection-owned kind
  1..* trace bindings to BA
  role-bound trace where contributions differ
  shared rendering and/or explicit method-owned interpretation
```

No stronger structure is justified by T1.

## 20. T1 provisional ledger summary

```text
Human projection from same BA                     PASS
Bounded method projection from same BA             PASS
Selection without coverage semantics               FAIL
Omission == negation                               FAIL
Display rename preserving BA meaning               PASS
Stronger human aggregation                         FAIL
Grouping with preserved member trace               PASS
Method-owned interpretation with BA trace          PASS
Method interpretation promoted into BA             FAIL
Meaning-bearing item without BA trace               FAIL
Mandatory duplicate GovernedSourceRef in view       NOT REQUIRED
Role-bound multi-input trace                        REQUIRED
Projection-local item identity                      REQUIRED WHEN MEANING-BEARING
Projection cross-baseline lifecycle                 NOT REQUIRED
Rebuild after BA change                             PASS / REQUIRED
New BAE family                                      NOT FORCED
New BA2 operator                                    NOT FORCED
BA1/BA2/BA3 reopen                                  NOT TRIGGERED
BA4                                                 STARTED / NOT CLOSED
```

## 21. Next pressure target

BA4-T1 is insufficient to close BA4.

The next smallest falsification target is:

> **BA4-T2 - method-owned interpretation, coverage loss and cross-projection consistency pressure test.**

T2 should use at least two incompatible method-oriented projections over the same BA, exercise diagnostics/stale views and aggressive selection/aggregation, and test whether the revisioned descriptor plus role-bound BA trace is sufficient for reproducible method-owned interpretation without introducing shared projection ontology.

Do not start BA5, BA6, AnalysisRecord/Common Finding or a complete STRIDE/STRIDE-AI schema.
