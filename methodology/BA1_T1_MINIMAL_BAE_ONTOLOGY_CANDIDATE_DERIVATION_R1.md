# BA1-T1 - Minimal BAE ontology candidate derivation

**Revision:** R1

**Status:** COMPLETED / PROVISIONAL CANDIDATE / BA1 NOT CLOSED

**Repository baseline reviewed:** `83af68cb1a02a6b1e76f591d4c1519f9496be3b3`

**Phase:** BA1 - Minimal BAE ontology

**BA0:** CLOSED

**BA2:** NOT STARTED

## 1. Question and guardrail

BA1-T1 asks only:

> What is the smallest falsifiable set of first-class analytical identity families needed to realize the closed BA0 responsibilities without importing document types, tool structures, threat-method categories or general systems-modeling taxonomies by default?

The governing rule is:

```text
semantic responsibility exists
        !=
first-class metaclass required
```

For every recurring semantic responsibility, BA1-T1 tests whether it can remain a relation, role, property/value, constraint/state, provenance or diagnostic record, or derived projection before proposing a first-class BAE identity.

This microstep does not define relation vocabulary, canonical action predicates, identity/equivalence lifecycle rules, provenance materialization, projection contracts, AnalysisRecord, Finding or a threat-method overlay.

## 2. Closed input boundary from BA0

BA0-T3 closed eight responsibilities:

- `BA0-C1` authority and provenance boundary;
- `BA0-C2` baseline-scoped shared semantic identity;
- `BA0-C3` method-neutral shared core;
- `BA0-C4` explicit uncertainty and diagnostic localization;
- `BA0-C5` projection readiness and source drill-down;
- `BA0-C6` change-impact traceability;
- `BA0-C7` source-localized feedback handoff;
- `BA0-C8` minimality and representation independence.

BA0 also closed that grounded, derived and diagnostic/unresolved are required **origin/state responsibilities**, not pre-approved domain metaclasses. A generic reviewed analytical-addition class is not required.

The BA0 boundary already speaks of stable analytical **referents and propositions**. BA1-T1 treats those words as responsibility-level evidence and tests whether they deserve distinct first-class identity families.

## 3. Evidence base

### 3.1 Facial-access branch inherited from BA0-T1/T2

The branch requires stable recognition of at least:

- `CameraSubsystem`;
- `RecognitionProcessor`;
- `RecognitionCapture`;
- `RecognitionRequest`;
- consumed transport responsibility/context;
- current Ethernet realization;
- the delivery/correlation/failure statements around `FR-3.4`;
- the confidentiality, integrity and authorized-origin conditions constraining that delivery.

BA0-T1 showed that the same referent can participate in grounded and derived assertions with different origin. It also showed that a plausible invented endpoint is not accepted merely because it is convenient to draw.

Mutation M1 (`Ethernet -> Wi-Fi`) changes one realization while preserving most other meaning. Mutation M3 (remote -> local recognition) retires/revises delivery meaning and proves that lexical equality alone cannot establish analytical identity.

### 3.2 Independent order-fulfillment corpus

The revision-3 complete order-fulfillment authoring probe is used as a structurally distinct pressure source. It explicitly states that its governed references are an authoring substrate and that their final Base Analysis types are deferred.

The corpus contains:

- human/external participants (`Customer`, `WarehouseOperator`, `PaymentProvider`);
- project capabilities/services such as `OrderService`, `InventoryService` and `PaymentAdapter`;
- further service referents such as `FulfillmentService` and `CarrierAdapter`;
- lifecycle-bearing concepts such as `OrderEvaluation`, `Order` and `Reservation`;
- result concepts such as `ReservationResult` and `PaymentAuthorizationResult`;
- task concepts such as `FulfillmentTask`;
- store candidates such as `InventoryLedger` and `ReservationStore`;
- contract candidates such as `PaymentProviderContract` and `CarrierContract`;
- state and result values (`ACCEPTED`, `authorized`, `declined`, `indeterminate`, reservation lifecycle state);
- cross-branch service consumption without ownership transfer;
- decisions that change responsibility boundaries (internal inventory authority versus external WMS);
- operational statements about correlation, atomicity, idempotency, compensation, concurrency, failure and physical handoff milestones.

The corpus deliberately leaves the exact formal object for cross-MR service consumption open for Base Analysis.

### 3.3 Documentation-layer constraints

The FunctionalRequirement baseline makes normative prose semantically primary and uses SPO references only to expose reusable participants. It explicitly states that SPO alone does not contain all conditional, concurrency, lifecycle or failure semantics.

The Decision layer records project commitments; it is not automatically an analytical type. The MR working evidence likewise warns that nouns in MR prose do not directly create BAEs. The layering work separates L1 semantics from material representation, tooling and projections.

Therefore BA1 must not copy the `MR -> Decision -> FR -> SR` document hierarchy into Base Analysis.

## 4. Lower-bound falsification: can one generic element type be enough?

### Candidate alternative A

```text
BAElement
```

with every project thing and every analytical claim represented as the same undifferentiated kind.

### Test

This collapses two responsibilities that current evidence needs to distinguish:

1. **identity of what the project statement is about**; and
2. **identity, origin and evolution of the statement itself**.

In T1, `CameraSubsystem` can remain the same referent while the statements involving it are retained, revised or retired. The normalized delivery tuple is derived even though its referenced participants are grounded. In the order corpus, the same `OrderEvaluation` identity participates in multiple independently governed claims about reservation, payment, compensation and commitment.

If referent and proposition are one undifferentiated kind, provenance and change review can still be implemented with extra flags, but the semantic distinction has merely been hidden in properties. That does not reduce the required ontology; it obscures it.

### Disposition

**REJECTED AS THE MINIMAL BA1-T1 CANDIDATE.** A single undifferentiated analytical element does not preserve the observed distinction between identity of a referent and identity/origin of claims about it.

## 5. Upper-bound falsification: are domain-specific roots already forced?

The reviewed evidence repeatedly uses structural participants, behavior, information, state, interfaces/contracts, stores and boundaries. BA0-R also established their recurring semantic relevance.

However, recurring relevance is not sufficient for first-class split.

Current cases can be represented without yet declaring separate root metaclasses:

- `CameraSubsystem`, `RecognitionProcessor`, `OrderService`, `PaymentProvider`, `InventoryLedger` and `PaymentProviderContract` can all be independently identified referents whose more specific semantic role remains explicit but not yet a metaclass split;
- `RecognitionCapture`, `RecognitionRequest`, `OrderEvaluation`, `Reservation` and result objects can be referents with information/resource/lifecycle roles;
- delivery, correlation, dependency, ownership, state transition, atomicity, idempotency, applicability and security conditions can be propositions;
- a behavior/event that later needs independent cross-statement identity may itself become a referent, without proving today that all behaviors require a separate `Behavior` metaclass;
- state values can remain values/qualifiers or propositions until an independently governed state identity is forced;
- a boundary, channel, store or contract can remain a referent role/kind until evidence requires subtype-specific invariants that cannot be expressed without a first-class split.

### Disposition

**NOT YET FORCED.** `Behavior`, `Information`, `Participant`, `Component/Capability`, `Boundary`, `Channel`, `Store`, `Contract`, `State/Mode/Context`, `Interface/Connection`, `Dependency` and similar families remain split hypotheses for later pressure testing.

## 6. Minimal ontology candidate

BA1-T1 therefore proposes exactly two first-class analytical identity families.

### BA1-C1 - `BAReferent`

**Status:** CANDIDATE / FIRST-CLASS IDENTITY PRESSURE SUPPORTED / NOT ACCEPTED

A `BAReferent` is an independently identifiable unit of methodology-neutral shared project meaning that must be recognizable across one or more analytical propositions, projections or governed baselines.

A referent may denote structural, human/external, informational/resource, behavioral/event, contractual, storage or other project meaning. Those semantic kinds are not first-class subtype decisions in BA1-T1.

Examples from the evidence include, when independent identity is needed by analysis:

- `CameraSubsystem`, `RecognitionProcessor`;
- `RecognitionCapture`, `RecognitionRequest`;
- `OrderEvaluation`, `Reservation`;
- `InventoryService`, `PaymentProvider`;
- `PaymentProviderContract`, `InventoryLedger`.

A governed document is not automatically a `BAReferent`. The project meaning expressed by a document may justify one or more referents, while the document remains source authority and provenance evidence.

### BA1-C2 - `BAProposition`

**Status:** CANDIDATE / FIRST-CLASS IDENTITY PRESSURE SUPPORTED / NOT ACCEPTED

A `BAProposition` is an independently identifiable methodology-neutral analytical assertion expressing shared project meaning about one or more referents, with enough identity to carry source/origin distinction, be retained/revised/retired or diagnosed, and be reused by multiple projections or consumers.

A proposition may express, without pre-closing the later vocabulary:

- relation or dependency;
- behavior/action/transfer/transition;
- responsibility or ownership context;
- correlation;
- state/condition/result semantics;
- applicability;
- constraint/property;
- lifecycle/failure/concurrency semantics.

A proposition may itself need to be the target of another proposition. For example, a specialized condition may constrain the same delivery meaning without forcing a separate `Behavior` metaclass at this stage.

The exact predicate/action vocabulary and structural shape of propositions belong to BA2. Exact origin/provenance/source-locator materialization belongs to BA3.

### Candidate picture

```text
Base Analysis for one governed baseline

    BAReferent *
        ^
        | referenced by
        |
    BAProposition *

BAProposition has identity and may also be targeted by other propositions.
```

`BAE` is used as the umbrella term for Base Analysis elements. BA1-T1 does **not** require an additional concrete or abstract `BAElement` metaclass unless a later shared-field/invariant analysis justifies it.

## 7. Why proposition identity is not just a relation table

The evidence requires more than binary edges.

`FR-3.4` includes source, destination, delivered information, request correlation and failure semantics. The order corpus includes conditions, atomicity, concurrency, idempotency, lifecycle and indeterminate outcomes that cannot be reduced faithfully to one subject-predicate-object edge.

SPO remains useful as one structured projection, but the full analytical claim is the semantic unit that needs provenance and change review.

Therefore BA1-T1 does not define `Relation` as a first-class BAE. A relation/action may be part of the content of a `BAProposition`; BA2 will decide the minimal relation and action vocabulary.

## 8. Mapping the BA0 responsibilities to the candidate

- **C1 authority/provenance:** referents and especially propositions remain source-aligned; exact provenance records are BA3, not new domain BAEs.
- **C2 shared semantic identity:** `BAReferent` and `BAProposition` provide the two identity-bearing families forced by current evidence.
- **C3 method-neutral core:** neither family contains STRIDE/STRIDE-AI or tool-owned categories.
- **C4 diagnostic localization:** diagnostic/unresolved remains status/record over affected identities; no `Diagnostic` domain BAE is required.
- **C5 projection readiness:** views select/project referents and propositions; `View` is BA4, not a core BAE type.
- **C6 change-impact traceability:** referent/proposition identity allows selective retain/revise/retire review; exact dependency relations are BA2/BA3.
- **C7 feedback handoff:** source-aligned propositions localize the governed area to review; governance workflow remains outside BA.
- **C8 minimality/independence:** no notation, storage technology, document hierarchy or domain-specific subtype is accepted without separate pressure.

## 9. Explicit non-first-class dispositions in BA1-T1

### Not copied from documentation

The following are **not BAE metaclasses by inheritance**:

- `MacroRequirement`;
- `Decision`;
- `Requirement`;
- `FunctionalRequirement`;
- `SpecializedRequirement`;
- `SecurityRequirement`;
- `NormativeClause`.

They remain governed-document concepts/source identities. BA3 will later define document-to-Base-Analysis derivation and provenance.

### Not promoted from historical/tool studies

The following are **not accepted roots**:

- `actor`;
- `component`;
- `asset`;
- `boundary`;
- `data_flow`;
- ThreatForge-native objects;
- STRIDE DFD categories.

### Deferred semantic-kind splits

The following remain **OPEN / DEFERRED AS FIRST-CLASS SPLITS**:

- Participant / actor-like role;
- structural element / component / capability;
- information / resource;
- behavior / event / transition;
- interface / connection / channel;
- store / persistence;
- contract;
- boundary / scope boundary;
- state / mode / context;
- dependency / allocation;
- property / constraint as an autonomous element.

They may remain classifications/roles/propositions, or later evidence may force a subtype/metaclass split.

### Deferred to later phases rather than domain ontology

- source locator, provenance record and origin materialization -> BA3;
- diagnostic record/status schema -> BA3;
- view/projection -> BA4;
- controlled vocabulary and lexical assistance -> BA5;
- AnalysisRecord, Finding and methodology output -> post-BA6 analysis envelope.

## 10. Candidate falsification criteria

The two-family candidate must be weakened or split if a concrete corpus or consumer demonstrates any of the following:

1. two referents with the same generic representation require subtype-specific invariants that cannot be expressed without losing reusable semantics;
2. behavior/event identity cannot be represented honestly as referent plus propositions without ambiguity or unstable reification;
3. information/resource identity requires distinct lifecycle/typing rules that generic referents cannot preserve;
4. state/context must be independently identified and related across multiple claims in a way that values/qualifiers/propositions cannot represent cleanly;
5. boundary/interface/contract/store semantics require independent first-class identity and subtype invariants for multiple analysis consumers;
6. proposition-as-target becomes ambiguous or creates circular semantics that a dedicated behavior/constraint element would resolve materially;
7. a method-neutral consumer cannot build its required projection without reconstructing domain kinds independently from raw prose;
8. a structurally different governed corpus cannot be represented without adding method/tool/document-specific meaning to either family.

Ordinary requests for a nicer diagram or convenient implementation class are not sufficient evidence.

## 11. Result

BA1-T1 produces a **minimal falsifiable ontology candidate**, not an accepted ontology:

```text
CANDIDATE
    BAReferent
    BAProposition

NOT ACCEPTED YET
    any domain-specific subtype/metaclass split
```

This candidate is smaller than the historical five-focus study and smaller than a general-purpose systems model. It is also stronger than an untyped node graph because it preserves the distinction between project referent identity and provenance-bearing analytical claim identity.

No relation vocabulary is closed by BA1-T1.

## 12. Next authorized microstep

Execute only:

> **BA1-T2 - split-or-collapse pressure test of the two-family candidate.**

BA1-T2 must deliberately stress `BAReferent + BAProposition` against at least:

- behavior/event identity and specialized constraints in the facial-access branch;
- information/resource lifecycle and correlation in order fulfillment;
- internal/external responsibility boundaries plus contract/store candidates;
- state/indeterminate semantics and physical handoff event reuse;
- one bounded method-consumer projection.

Its purpose is to decide whether any deferred semantic kind is forced to become a first-class split, whether the two-family candidate can be simplified further, or whether it survives unchanged.

Do not start BA2 unless BA1 is explicitly closed after pressure testing and closure review.
