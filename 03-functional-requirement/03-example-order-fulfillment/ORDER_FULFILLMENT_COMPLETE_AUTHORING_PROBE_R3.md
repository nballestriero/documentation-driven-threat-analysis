# Independent Validation Corpus - Order Fulfillment and Warehouse Management

**COMPLETE MR / DECISION / FR AUTHORING PROBE - REVISION 3**

> This corpus replaces the two earlier simplified order/inventory holdouts for validation purposes. It is written against the regular `MR -> Decision -> FR` hierarchy. It is evidence/test material, not a universal domain reference architecture.

## 1. Problem framing

**Problem / class of problems:** enable customers to place orders for physical products and progress them to fulfillment while preserving coherent commitments across finite stock, concurrent demand, payment authorization and physical dispatch.

**Meaningful boundary:** from checkout/order evaluation through order commitment, warehouse stock movement/reservation, payment authorization/settlement and handoff to dispatch.

**Out of scope:** procurement planning, supplier replenishment, long-term demand forecasting and carrier transport after governed handoff.

**Not assumed at framing level:** local vs external WMS/ERP, payment provider, carrier, database, API protocol, message broker, microservices, cloud, reservation algorithm, warehouse topology or persistence technology.

## 2. Operating scenario

- products are physical and stock is finite;
- concurrent checkout sessions may request the same SKU;
- stock changes through receipts, issues, returns, damage/quarantine and controlled adjustments;
- orders may contain multiple lines;
- payment authorization may be authorized, declined or indeterminate;
- retries must not create duplicate financial operations;
- stock reservations are temporary until commit, release or expiry;
- fulfillment may encounter short picks/damage despite a prior reservation;
- carrier interaction can be accepted, rejected or indeterminate.

## 3. Macro project map

![Order-fulfillment hierarchy and service dependencies](diagrams/ORDER_FULFILLMENT_HIERARCHY.png)

```text
MR-1 Order lifecycle and commitment
   | depends on services from
   +--> MR-2 Warehouse and inventory management
   +--> MR-3 Payment authorization and settlement
   |
   `--> MR-4 Fulfillment and dispatch (after acceptance)

MR-4 consumes stock-allocation/issue services from MR-2
MR-3 capture timing consumes a governed handoff milestone from MR-4
```

Service consumption does not transfer ownership.

## 4. Governed references used by FR clauses

These references are an authoring substrate only. Their final Base Analysis types are deliberately deferred.

| Ref | Name | Probe kind | Meaning |
|---|---|---|---|
| `ACT-Customer` | Customer | actor | person submitting checkout |
| `ACT-WarehouseOperator` | WarehouseOperator | actor | receives/picks/packs physical stock |
| `ACT-InventoryManager` | InventoryManager | actor | approves controlled adjustments |
| `CMP-OrderService` | OrderService | capability | owns order evaluation/commit state |
| `CMP-InventoryService` | InventoryService | capability | project-side inventory authority in chosen internal-WMS Decision |
| `CMP-PaymentAdapter` | PaymentAdapter | capability | project-side PSP integration |
| `CMP-PaymentProvider` | PaymentProvider | external capability | selected PSP |
| `CMP-FulfillmentService` | FulfillmentService | capability | pick/pack/handoff lifecycle |
| `CMP-CarrierAdapter` | CarrierAdapter | capability | project-side carrier integration |
| `DAT-OrderEvaluation` | OrderEvaluation | data | correlated checkout evaluation |
| `DAT-Order` | Order | data | governed committed/rejected/cancelled state |
| `DAT-InventoryBalance` | InventoryBalance | data | on-hand/reserved/blocked accountable state |
| `DAT-StockMovement` | StockMovement | data | receipt/issue/return/adjustment event |
| `DAT-AvailabilityResult` | AvailabilityResult | data | sufficient/insufficient/indeterminate observation |
| `DAT-Reservation` | Reservation | data | temporary allocation/hold for one evaluation |
| `DAT-ReservationRequest` | ReservationRequest | data | full-order stock hold request correlated to OrderEvaluation |
| `DAT-ReservationResult` | ReservationResult | data | reserved/unavailable/indeterminate outcome |
| `DAT-PaymentAuthRequest` | PaymentAuthorizationRequest | data | amount/currency authorization request correlated to OrderEvaluation |
| `DAT-PaymentAuthResult` | PaymentAuthorizationResult | data | authorized/declined/indeterminate project result |
| `DAT-PaymentSettlementResult` | PaymentSettlementResult | data | capture/void/refund result |
| `DAT-FulfillmentTask` | FulfillmentTask | data | pick/pack work for accepted order/reservation |
| `DAT-DispatchRequest` | DispatchRequest | data | governed carrier handoff request for prepared fulfillment |
| `DAT-DispatchAcceptance` | DispatchAcceptance | data | carrier accepted/rejected/indeterminate result |
| `STORE-InventoryLedger` | InventoryLedger | store candidate | chosen project-owned stock authority |
| `STORE-ReservationStore` | ReservationStore | store candidate | chosen persistence for reservation lifecycle |
| `CON-PaymentContract` | PaymentProviderContract | contract candidate | governed PSP interface |
| `CON-CarrierContract` | CarrierContract | contract candidate | governed carrier interface |

# 5. MR-1 - Order lifecycle and commitment

## Intent

Manage a coherent order lifecycle and determine when the project is allowed to make a customer commitment, using inventory and payment capabilities without absorbing their internal responsibilities.

## Context

Checkout can fail because stock cannot be reserved, payment cannot be authorized or a dependent capability returns an indeterminate result. Commitment must not leave hidden stock/payment side effects.

## Stakeholders

Customers, customer support, commercial/order operations, downstream inventory/payment/fulfillment owners.

## Scope

Order evaluation/session, commitment decision, accepted/rejected/cancelled state and coordination/compensation of dependent capabilities. Warehouse accounting, PSP internals and carrier execution remain in their own branches.

## ADR-1.1 - Explicit correlated OrderEvaluation before commitment

**Context.** The project could mutate a draft Order directly, keep checkout state externally/statelessly, or create an explicit evaluation context used to correlate stock/payment outcomes before commitment.

**Decision.** Use one explicit `OrderEvaluation` identity for each checkout evaluation. All reservation, payment and compensation results used for that attempt are correlated to it before an Order becomes committed.

**Consequences.** Correlation and idempotency become explicit project semantics; stale/superseded evaluations can be distinguished from the current attempt.

### FR-1.1 - Create and preserve one correlated order evaluation

When Customer submits checkout with one or more product lines and quantities, OrderService MUST create exactly one active `OrderEvaluation` with stable correlation identity and MUST preserve the evaluated product/quantity set until the evaluation is terminal or superseded.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| Customer | submits | OrderEvaluation |
| OrderService | creates | OrderEvaluation |
| OrderService | maintains | OrderEvaluation |

## ADR-1.2 - Reservation and payment authorization are both commitment gates

**Context.** The project could confirm before payment, confirm before stock allocation, or require both results. Execution may be sequential or concurrent, but customer commitment must not exist without both prerequisites.

**Decision.** An Order may become accepted only after one valid full-order `ReservationResult=reserved` and one `PaymentAuthorizationResult=authorized` are correlated to the same active OrderEvaluation. The acquisition order/concurrency of the two results is not fixed here.

**Consequences.** MR-1 consumes capabilities from MR-2 and MR-3. Indeterminate results keep the evaluation non-committed. Side effects require compensation if the other gate fails.

### FR-1.2 - Obtain governed inventory and payment results for the active evaluation

For an active OrderEvaluation, OrderService MUST request the required stock-reservation and payment-authorization services and MUST associate each returned governed result with the same evaluation before commitment is decided. A result correlated to another/superseded evaluation MUST NOT satisfy the current gate.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| OrderService | requests | InventoryService |
| OrderService | requests | PaymentAdapter |
| OrderService | receives | ReservationResult |
| OrderService | receives | PaymentAuthorizationResult |

**Service consumption:** reservation is provided by the MR-2 branch; payment authorization by MR-3.

## ADR-1.3 - All-or-nothing customer commitment for requested lines

**Context.** A multi-line order could accept available lines and backorder/reject others, or require the whole requested set before commitment.

**Decision.** The probe uses all-or-nothing customer commitment: every requested line/quantity must be covered by the reservation used for acceptance.

**Consequences.** Partial warehouse allocations cannot silently become a partially accepted customer order under this project policy.

### FR-1.3 - Commit or reject the full evaluated order from correlated results

When both governed gate results are available for the same active OrderEvaluation, OrderService MUST transition/create `Order=ACCEPTED` only if payment is authorized and reservation covers the full evaluated line set. A negative result MUST prevent acceptance. An indeterminate result MUST keep the order non-committed until resolved or the evaluation is terminated by applicable recovery policy.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| OrderService | reads | ReservationResult |
| OrderService | reads | PaymentAuthorizationResult |
| OrderService | transitions | Order |

## ADR-1.4 - Explicit compensation of pre-commit side effects

**Context.** Reservation or payment authorization can succeed while the other gate later fails/cancels. Ignoring the successful side effect would leak stock holds or financial authorizations.

**Decision.** A non-accepted evaluation with created pre-commit side effects must explicitly invoke the corresponding release/void service and track unresolved compensation.

**Consequences.** Order failure is not treated as a single local calculation; compensation is a governed cross-MR interaction.

### FR-1.4 - Compensate failed/cancelled commitment

When an OrderEvaluation terminates without acceptance after a stock Reservation or Payment Authorization side effect exists, OrderService MUST request the corresponding release/void capability and MUST retain enough correlation to determine the compensation outcome. It MUST NOT treat the evaluation as cleanly compensated while a required compensation result remains indeterminate.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| OrderService | requestsRelease | InventoryService |
| OrderService | requestsVoid | PaymentAdapter |

# 6. MR-2 - Warehouse and inventory management

## Intent

Maintain trustworthy operational stock and provide availability/reservation/issue behavior that prevents the project from promising the same finite quantity to incompatible commitments.

## Context

Stock enters/leaves the warehouse, may be damaged/blocked, may be temporarily reserved by concurrent sessions and must eventually be consumed or released. Availability is not equivalent to the last counted on-hand quantity.

## Stakeholders

Warehouse operators, inventory managers, order operations, fulfillment operations, finance/audit roles affected by stock discrepancies.

## Scope

Accountable stock movements, stock-state semantics, availability, reservation lifecycle, concurrency and issue. Procurement/supplier planning is outside this probe.

## ADR-2.1 - Project-owned internal inventory authority

**Context.** The project could manage stock internally, delegate stock/reservation to an external WMS/ERP, or consume a black-box reservation service. These alternatives move the responsibility boundary and materially change downstream FRs.

**Decision.** This concrete probe implements inventory management internally: `InventoryService + InventoryLedger` are the authoritative project-managed source for on-hand/reserved/blocked stock state used by ordering and fulfillment.

**Consequences.** The project owns receipt/adjustment/availability/reservation/concurrency/release/issue FRs. A future external-WMS Decision would replace many of these with integration/API/contract FRs rather than being a transparent implementation swap.

### FR-2.1 - Record inbound stock receipt exactly once

When WarehouseOperator confirms receipt of a product quantity at a governed stock location, InventoryService MUST create an attributable inbound `StockMovement` and MUST increase corresponding on-hand `InventoryBalance` exactly once. Reprocessing the same governed receipt identity MUST NOT increase stock a second time.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| WarehouseOperator | confirmsReceipt | StockMovement |
| InventoryService | records | StockMovement |
| InventoryService | increases | InventoryBalance |

## ADR-2.2 - Accountable stock changes are recorded as movements, not destructive balance rewrites

**Context.** Inventory corrections could overwrite current balance with little history, or preserve attributable movements from which current accountable state is updated/reconciled.

**Decision.** Receipt, issue, return and controlled adjustment are recorded as attributable `StockMovement` events; historical accountable movements are not silently rewritten/deleted to hide previous state.

**Consequences.** Reconciliation/auditability improve; corrections are additional governed movements. Future GovernanceRequirements may add approval/evidence constraints.

### FR-2.2 - Record controlled stock adjustment

When a physical count, damage/quarantine event or approved correction requires an accountable change, InventoryService MUST create an adjustment StockMovement linked to the applicable reason/approval context and MUST update the affected InventoryBalance without deleting or rewriting the prior accountable movement history.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| InventoryManager | approves | StockMovement |
| InventoryService | records | StockMovement |
| InventoryService | updates | InventoryBalance |

## ADR-2.3 - Separate on-hand, reserved and blocked stock semantics

**Context.** One quantity cannot distinguish physically present stock from stock already promised to orders or present but unusable due to damage/quarantine.

**Decision.** Govern distinct on-hand, active-reserved and blocked quantities. Allocatable availability excludes active reservations and blocked quantity.

**Consequences.** Every movement/reservation/release/issue must preserve these semantics; exact persistence schema remains implementation.

### FR-2.3 - Produce attributable current availability without freezing stock

When an availability query identifies product, location scope and requested quantity, InventoryService MUST derive `AvailabilityResult` from current accountable InventoryBalance, distinguish sufficient/insufficient/indeterminate and make the result attributable to its observation/state context. The availability query MUST NOT itself freeze quantity.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| InventoryService | reads | InventoryBalance |
| InventoryService | produces | AvailabilityResult |

## ADR-2.4 - Temporary expiring reservation hold bound to one OrderEvaluation

**Context.** The project could decrement stock immediately at checkout, use non-expiring allocations, perform best-effort availability checks without holds, or use temporary reservation/lease semantics.

**Decision.** Use a temporary `Reservation` bound to one OrderEvaluation. ACTIVE reservation freezes allocatable quantity without representing physical stock issue. It remains until commit/consumption, explicit release or governed expiry.

**Consequences.** Reservation identity/lifecycle/correlation become operational semantics. The expiry duration itself is not hard-coded into this FR corpus.

### FR-2.4 - Maintain reservation identity and lifecycle correlation

For every ACTIVE Reservation, InventoryService MUST preserve exactly one originating OrderEvaluation reference, reserved line quantities, lifecycle state and applicable expiry context. Release, expiry or consumption commands MUST target that Reservation identity and MUST be idempotent for repeated delivery of the same governed command.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| InventoryService | maintains | Reservation |
| Reservation | references | OrderEvaluation |

## ADR-2.5 - Atomic all-lines reservation under concurrency

**Context.** Concurrent checkouts can observe the same apparent availability and oversell if read/check and reservation are independent. Multi-line orders also risk partial holds that violate MR-1 all-or-nothing commitment.

**Decision.** Allocation for one full-order ReservationRequest is atomic with respect to competing reservations and stock-changing operations: either the complete requested set becomes reserved or no line becomes ACTIVE for that request.

**Consequences.** Implementation must provide concurrency control but the Decision does not prescribe locks, isolation level, CAS, queue or storage engine.

### FR-2.5 - Create one atomic temporary reservation for the full evaluated set

When a ReservationRequest identifies an active OrderEvaluation and its full product/quantity set, InventoryService MUST atomically determine allocatability against current on-hand/reserved/blocked state. If fully allocatable, it MUST create exactly one ACTIVE Reservation, increase reserved quantity for each line exactly once and return `ReservationResult=reserved`. If not fully allocatable, it MUST create no active partial reservation for that request and return unavailable. A concurrent request MUST NOT reserve quantity already frozen by the first active Reservation.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| InventoryService | creates | Reservation |
| InventoryService | updates | InventoryBalance |
| InventoryService | produces | ReservationResult |

## ADR-2.6 - Reservation release/expiry restores allocatable quantity idempotently

**Context.** A temporary hold can be released explicitly, expire, or be consumed. Replayed lifecycle events must not double-release quantity.

**Decision.** Release and expiry transition an ACTIVE Reservation out of commitment eligibility exactly once and restore reserved quantity to allocatable state unless another stock constraint blocks it.

**Consequences.** Reservation lifecycle commands/results must be correlated and idempotent. The policy determining expiry time remains separately governed.

### FR-2.6 - Release reserved quantity after cancellation, failure or expiry

When an ACTIVE Reservation is explicitly released because its order evaluation is cancelled/rejected, or when the governed expiry condition occurs, InventoryService MUST transition it so it can no longer support commitment and MUST decrease corresponding reserved quantities exactly once. Replayed release/expiry handling MUST NOT free the same quantity twice.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| InventoryService | releases | Reservation |
| InventoryService | decreasesReserved | InventoryBalance |

## ADR-2.7 - Physical handoff is the stock-issue milestone

**Context.** Accountable stock issue could be recorded at pick completion, packing, carrier request, carrier acceptance or physical handoff. Recording too early can reduce on-hand stock when goods remain controlled by the warehouse.

**Decision.** For this probe, accountable outbound issue occurs at the governed **physical handoff milestone** for the picked quantities, not merely at dispatch-request preparation or raw carrier acceptance.

**Consequences.** Fulfillment must emit/confirm the handoff milestone. Inventory consumes only quantities covered by the valid Reservation. Payment capture policy can reference the same governed milestone.

### FR-2.7 - Convert reserved quantities into accountable stock issue at handoff

When FulfillmentService confirms the governed physical handoff milestone for an accepted order under a valid Reservation, InventoryService MUST create the attributable outbound StockMovement and MUST atomically reduce on-hand and reserved quantities for the consumed reservation lines exactly once. It MUST NOT issue quantities beyond the Reservation or silently consume unrelated unreserved stock.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| InventoryService | records | StockMovement |
| InventoryService | decreases | InventoryBalance |
| InventoryService | consumes | Reservation |

## 6.1 Counterfactual: if ADR-2.1 chose an external WMS

This is not the chosen branch, but it demonstrates why ADR-2.1 is a real responsibility-boundary Decision.

With an external authoritative WMS, project-owned FRs would shift toward integration semantics such as:

- submit governed receipt/adjustment requests through the WMS contract;
- request full-order reservation and correlate the WMS result to OrderEvaluation;
- map provider-specific reservation statuses to governed project semantics;
- resolve indeterminate/time-out outcomes before semantically new retries;
- request release of the exact reservation identity;
- confirm/consume stock issue through the external contract.

The WMS's internal ledger schema, lock/isolation mechanism and internal concurrency algorithm would normally fall outside project FR ownership unless exposed as contractual properties.

Therefore "internal vs external inventory authority" is not an implementation detail: it changes the FR responsibility boundary.

# 7. MR-3 - Payment authorization and settlement

## Intent

Provide governed payment authorization/settlement state that order commitment can consume without adopting provider-specific status as project semantics.

## Context

External operations can time out after processing; blind retry can duplicate financial effects. Authorization, capture and void/refund are distinct lifecycle operations.

## Stakeholders

Customers, finance, customer support, fraud/payment operations, order operations.

## Scope

Authorization request/result, ambiguous outcome resolution, void/capture and provider integration. Card-network/provider internals remain outside project boundary.

## ADR-3.1 - External PSP behind a governed project contract

**Context.** Payment could be processed internally or delegated to different providers with different APIs and state vocabularies.

**Decision.** Delegate payment operations to external `PaymentProvider` through `PaymentProviderContract`, with `PaymentAdapter` owning project-side integration.

**Consequences.** API interaction, correlation and failure handling are project FRs; provider internals are not.

### FR-3.1 - Submit idempotently identifiable authorization request

When `PaymentAuthorizationRequest` is issued for an active OrderEvaluation, PaymentAdapter MUST submit an idempotently identifiable provider operation through PaymentProviderContract and preserve correlation to the evaluation.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| PaymentAdapter | sends | PaymentAuthorizationRequest |
| PaymentAdapter | communicatesWith | PaymentProvider |

## ADR-3.2 - Normalize provider-specific authorization states into project semantics

**Context.** Provider-specific status vocabularies should not leak into order commitment semantics.

**Decision.** Project payment authorization result is governed as `authorized`, `declined` or `indeterminate`; raw provider states are mapped behind PaymentAdapter.

**Consequences.** Provider replacement does not require MR-1 to understand provider-specific status codes.

### FR-3.2 - Produce correlated governed authorization result

PaymentAdapter MUST map the provider response/outcome to `PaymentAuthorizationResult` in project semantics and MUST correlate it to the originating OrderEvaluation. A provider-specific raw status MUST NOT directly become the order commitment result.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| PaymentAdapter | maps | PaymentAuthorizationResult |
| PaymentAdapter | produces | PaymentAuthorizationResult |

## ADR-3.3 - Resolve indeterminate operation before semantically new retry

**Context.** A timeout can occur after the provider accepted/processed a request. A blind new authorization can duplicate financial effects.

**Decision.** For an indeterminate submitted operation, resolve the same idempotent operation status before starting a semantically new authorization unless the contract proves it was not accepted.

**Consequences.** Recovery queries/idempotency keys become operational contract; retry policy is not a naive loop.

### FR-3.3 - Resolve indeterminate authorization safely

When authorization outcome is indeterminate after submission, PaymentAdapter MUST query/resolve the same provider operation before initiating a semantically new authorization attempt for that OrderEvaluation, unless the governed contract proves the original operation was not accepted.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| PaymentAdapter | queries | PaymentProvider |
| PaymentAdapter | updates | PaymentAuthorizationResult |

## ADR-3.4 - Capture only after governed physical handoff

**Context.** Payment could be captured at checkout, after picking, after carrier acceptance or after physical handoff.

**Decision.** Authorize before order acceptance, but capture only after MR-4 confirms the governed physical handoff milestone for the order.

**Consequences.** Accepted-but-not-handed-off orders hold authorization without capture; failed pre-handoff commitment requires void/release.

### FR-3.4 - Capture authorized payment after handoff

When the governed physical handoff milestone is confirmed for an accepted order with still-valid authorization, PaymentAdapter MUST request capture exactly once for the governed payable amount and MUST produce a correlated PaymentSettlementResult. It MUST NOT capture solely because Order is ACCEPTED.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| PaymentAdapter | requestsCapture | PaymentSettlementResult |
| PaymentAdapter | produces | PaymentSettlementResult |

## ADR-3.5 - Void open authorization when pre-capture commitment is abandoned

**Context.** A reservation/payment gate can fail after authorization succeeds, or an accepted order can be cancelled before capture.

**Decision.** Open authorization is explicitly voided/released when commitment is abandoned before capture.

**Consequences.** Compensation is observable and correlated rather than left to provider expiration as hidden behavior.

### FR-3.5 - Void pre-capture authorization

When an OrderEvaluation terminates without acceptance, or an accepted order is cancelled before capture while valid authorization remains open, PaymentAdapter MUST request the governed void/release operation and MUST produce a correlated PaymentSettlementResult.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| PaymentAdapter | requestsVoid | PaymentSettlementResult |
| PaymentAdapter | produces | PaymentSettlementResult |

# 8. MR-4 - Fulfillment and dispatch

## Intent

Transform an accepted order backed by valid stock allocation into controlled physical fulfillment and dispatch while preserving correlation between order, reservation, picked quantity, stock issue and carrier handoff.

## Context

Picking can encounter shortage/damage despite reservation. Carrier request can fail/timeout. Physical stock must not be issued merely because a dispatch request exists.

## Stakeholders

Warehouse/fulfillment operators, customers, carrier operations, customer support.

## Scope

Fulfillment task, pick/pack confirmation, fulfillment exceptions, carrier request/acceptance and physical handoff confirmation. Carrier transport after handoff is outside scope.

## ADR-4.1 - Fulfillment task requires accepted order plus valid reservation

**Context.** Warehouse execution could pick directly from order lines or require the exact stock allocation created during commitment.

**Decision.** Each FulfillmentTask references one accepted Order and the valid Reservation covering quantities to pick.

**Consequences.** Warehouse discrepancies can be detected against the committed allocation; inventory issue traces to reservation lifecycle.

### FR-4.1 - Create fulfillment task from accepted order and reservation

When Order is ACCEPTED and its Reservation is valid for the committed line set, FulfillmentService MUST create exactly one active FulfillmentTask referencing both and containing quantities to pick. It MUST NOT create a normal pick task for rejected/non-committed evaluation.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| FulfillmentService | creates | FulfillmentTask |
| FulfillmentTask | references | Order |
| FulfillmentTask | references | Reservation |

## ADR-4.2 - Short pick/damage is an explicit exception, not silent substitution

**Context.** Physical execution may find missing/damaged quantity despite prior logical reservation.

**Decision.** Short pick/damage/missing allocated quantity produces an explicit fulfillment exception; normal completion cannot silently substitute unrelated stock commitment or mark full completion.

**Consequences.** Recovery/backorder/customer handling can be governed separately; stock/accounting is not silently corrupted.

### FR-4.2 - Confirm picked quantities and surface reservation discrepancy

When WarehouseOperator confirms picking for a FulfillmentTask, FulfillmentService MUST record picked quantities by order line and compare them with the referenced Reservation. A short pick/damaged/missing allocated quantity MUST produce an explicit blocking fulfillment exception and MUST NOT be silently treated as complete fulfillment.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| WarehouseOperator | confirmsPick | FulfillmentTask |
| FulfillmentService | updates | FulfillmentTask |

## ADR-4.3 - External carrier handoff behind governed contract

**Context.** Dispatch could be performed internally or delegated to an external carrier/fulfillment provider.

**Decision.** Delegate carrier request through CarrierAdapter + CarrierContract; expose governed DispatchAcceptance rather than raw provider status.

**Consequences.** Provider mapping/correlation/recovery are project concerns; carrier transport internals remain external.

### FR-4.3 - Submit complete dispatch request and produce governed acceptance

When FulfillmentTask has required picked/packed quantities and no blocking exception, CarrierAdapter MUST create/submit the governed `DispatchRequest` through CarrierContract and MUST produce DispatchAcceptance correlated to Order and FulfillmentTask. Raw carrier status MUST NOT directly become project dispatch state.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| CarrierAdapter | sends | DispatchRequest |
| CarrierAdapter | produces | DispatchAcceptance |

## ADR-4.4 - Explicit physical handoff milestone closes warehouse custody

**Context.** Carrier acceptance of a request does not necessarily mean goods physically left warehouse control. Stock issue/payment capture need a stable project milestone.

**Decision.** Define a governed physical handoff milestone after successful prepared dispatch, distinct from mere request acceptance. This milestone is the event consumed by MR-2 stock issue and MR-3 capture policies.

**Consequences.** MR-2 and MR-3 can depend on one governed business event without adopting raw carrier semantics.

### FR-4.4 - Confirm physical handoff and invoke downstream services

When picked/packed goods for the accepted order physically cross the governed handoff milestone, FulfillmentService MUST record/emit that handoff correlated to Order, FulfillmentTask and Reservation, and MUST request the MR-2 stock-issue capability. The MR-3 capture branch may consume the same handoff result under ADR-3.4. A rejected/indeterminate carrier request alone MUST NOT count as physical handoff.

SPO:

| Subject | Predicate | Object |
|---|---|---|
| FulfillmentService | confirmsHandoff | FulfillmentTask |
| FulfillmentService | requestsStockIssue | InventoryService |

# 9. Hierarchy view

```text
MR-1 Order lifecycle
  ADR-1.1 explicit evaluation
    FR-1.1 create evaluation
  ADR-1.2 commit gates
    FR-1.2 obtain/correlate stock+payment results
  ADR-1.3 all-or-nothing commitment
    FR-1.3 commit/reject full order
  ADR-1.4 compensation
    FR-1.4 release/void side effects

MR-2 Warehouse/inventory
  ADR-2.1 internal inventory authority
    FR-2.1 inbound receipt
  ADR-2.2 accountable movement history
    FR-2.2 controlled adjustment
  ADR-2.3 stock-state semantics
    FR-2.3 availability
  ADR-2.4 temporary reservation lifecycle
    FR-2.4 reservation identity/lifecycle
  ADR-2.5 atomic all-line allocation
    FR-2.5 concurrent reservation
  ADR-2.6 release/expiry semantics
    FR-2.6 release quantity
  ADR-2.7 physical handoff -> stock issue
    FR-2.7 outbound issue

MR-3 Payment
  ADR-3.1 external PSP
    FR-3.1 submit authorization
  ADR-3.2 normalized payment semantics
    FR-3.2 governed result
  ADR-3.3 indeterminate retry semantics
    FR-3.3 resolve before retry
  ADR-3.4 capture after handoff
    FR-3.4 capture
  ADR-3.5 void abandoned authorization
    FR-3.5 void

MR-4 Fulfillment
  ADR-4.1 accepted order + reservation
    FR-4.1 fulfillment task
  ADR-4.2 explicit pick exception
    FR-4.2 pick/discrepancy
  ADR-4.3 external carrier contract
    FR-4.3 dispatch acceptance
  ADR-4.4 physical handoff milestone
    FR-4.4 confirm handoff
```

No necessity/default Decision is required in this particular corpus because material alternatives exist for every parent commitment. The rule remains available for rare singleton-solution branches.

# 10. Validation observations

This corpus supports the regular hierarchy without requiring Decisions below FR:

- responsibility-boundary choices (internal WMS vs external WMS, external PSP, external carrier) sit naturally at Decision level;
- strategy/policy choices (reservation semantics, atomic all-line allocation, handoff milestone, capture timing) sit naturally at Decision level;
- operational obligations become concrete FRs under those commitments;
- cross-MR composition appears as service/capability consumption rather than multiple FR owners;
- no FR needs to own a Decision child;
- mutable values such as reservation duration remain outside FR unless later classified by a specialized/policy/interface contract.

The exact formal object used to represent cross-MR service consumption remains deliberately open for the Base Analysis phase.
