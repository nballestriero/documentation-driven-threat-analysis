# BA1-T2 - Split-or-collapse pressure test of the two-family candidate

**Revision:** R1

**Status:** COMPLETED / PROVISIONAL PASS WITH MINIMALITY REFINEMENT / BA1 NOT CLOSED

**Repository baseline reviewed:** `f05fbb7b253392e158a1062df2614b177c13d43e`

**Phase:** BA1 - Minimal BAE ontology

**BA0:** CLOSED

**BA2:** NOT STARTED

## 1. Question and test discipline

BA1-T2 asks only:

> Does the BA1-T1 candidate `BAReferent + BAProposition` survive deliberate pressure to split recurring semantic kinds into dedicated first-class types, and does it also survive the opposite pressure to collapse both families into one undifferentiated analytical element?

The test does not design the BA2 relation/action vocabulary, BA3 provenance schema, BA4 views, formal STRIDE overlay, Finding model or ThreatForge implementation.

The governing criterion remains:

```text
independent semantic identity
        +
reusable subtype-specific invariants
        -> possible first-class split

recurring usefulness alone
        !=
first-class metaclass
```

A pressure case may justify an independently identifiable `BAReferent` without justifying a dedicated subtype such as `Behavior`, `Information`, `State`, `Contract` or `Store`.

## 2. Starting candidate from BA1-T1

BA1-T1 proposed two identity families:

```text
BAReferent
BAProposition
```

`BAReferent` covered independently identifiable units of shared project meaning. `BAProposition` covered independently identifiable methodology-neutral analytical assertions with origin/change/diagnostic pressure.

BA1-T1 deliberately left domain splits open and allowed a proposition to be targeted by another proposition. BA1-T2 treats both choices as falsifiable rather than inherited truth.

## 3. Pressure A - behavior/event identity

### 3.1 Facial-access delivery

`FR-3.4` requires delivery of `RecognitionCapture` from `CameraSubsystem` to `RecognitionProcessor`, correlated to the correct `RecognitionRequest`, with incomplete delivery not represented as success. Specialized requirements independently constrain confidentiality, integrity and authorized provenance during that same delivery meaning.

The pressure question is whether this requires a dedicated `Behavior` or `DataFlow` metaclass.

It does not.

The delivery meaning can have independent analytical identity as a `BAReferent` when multiple propositions need to talk about the same behavior. Separate propositions can state its source, destination, information, correlation and failure semantics, together with the specialized security constraints that apply to it.

This preserves behavior identity without asserting that every behavior/event belongs to a dedicated root metaclass.

### 3.2 Physical handoff milestone

The order-fulfillment corpus gives stronger pressure. The physical handoff milestone is defined in the fulfillment branch and reused by inventory stock issue and payment capture. Reuse across branches makes the milestone a natural independently identifiable semantic object.

Again, the evidence forces **referent identity**, not a universal `Event` metaclass. The milestone can be a `BAReferent`; propositions state who confirms it, when it occurs, and which stock/payment behavior depends on it.

### 3.3 Disposition

```text
Behavior / Event dedicated first-class split: NOT FORCED
Behavior/Event referent identity when independently reused: SUPPORTED
```

The old historical `data_flow` focus is not revived.

## 4. Pressure B - information/resource identity and lifecycle

The two corpora contain strongly reusable informational/resource-like meanings:

- `RecognitionCapture`;
- `RecognitionRequest`;
- `OrderEvaluation`;
- `Order`;
- `Reservation`;
- `ReservationResult`;
- `PaymentAuthorizationResult`;
- `FulfillmentTask`.

Some carry lifecycle or correlation semantics. `Reservation`, for example, is bound to one `OrderEvaluation`, has an ACTIVE lifecycle state, can be released/expired/consumed and participates in idempotent handling.

Those facts require stable referent identity and propositions about lifecycle/correlation. They do not establish one reusable set of invariants that all information/resource referents share and that generic referents cannot preserve.

A subtype may later become useful, but current evidence does not make it necessary for correctness or method-neutral reuse.

### Disposition

```text
Information / Resource dedicated first-class split: NOT FORCED
Lifecycle-bearing informational referents: representable as BAReferent + propositions
```

## 5. Pressure C - responsibility, externality and boundaries

Facial access distinguishes project endpoints from underlying external transport responsibility. Order fulfillment distinguishes internal project-owned inventory authority from an alternative external WMS and places payment/carrier providers behind governed contracts.

The pressure question is whether this forces dedicated `Participant`, `Component`, `Capability`, `Boundary` or `ExternalSystem` roots.

It does not.

The independently identifiable parties/capabilities are referents. Project ownership, externality, service consumption and responsibility placement are propositions or roles over those referents. A named responsibility boundary may itself receive referent identity if the project needs to reuse that boundary explicitly, but no subtype-specific invariant is yet forced.

The critical semantic point is preserved without type proliferation:

```text
service/capability consumption
        !=
ownership transfer
```

### Disposition

```text
Participant / Component / Capability split: NOT FORCED
Boundary / ExternalSystem split: NOT FORCED
Responsibility and externality: proposition/role pressure supported
```

## 6. Pressure D - Store and Contract candidates

The order corpus names the following candidates:

- stores: `InventoryLedger`, `ReservationStore`;
- contracts: `PaymentProviderContract`, `CarrierContract`.

All require independent identity if they participate in analysis. But the corpus does not establish universal subtype invariants that cannot be stated over generic referents:

- a store may be project-owned or merely a candidate realization;
- a contract may define a governed interaction boundary while provider-specific raw states remain outside project semantics;
- replacement of a provider/contract does not imply that all contracts or stores require a dedicated root type for every consumer.

Their semantic kind must not be lost, but classification is not equivalent to a first-class metaclass.

### Disposition

```text
Store dedicated first-class split: NOT FORCED
Contract dedicated first-class split: NOT FORCED
```

## 7. Pressure E - state, context and indeterminate outcomes

The order corpus uses values/states such as:

- `Order=ACCEPTED`;
- payment `authorized`, `declined`, `indeterminate`;
- reservation ACTIVE and terminal lifecycle states;
- availability/result states such as sufficient/insufficient/indeterminate.

Current evidence supports three honest representations depending on semantic need:

1. scalar/enumerated value or qualifier when only local value semantics are needed;
2. proposition when a state condition or transition must be asserted;
3. `BAReferent` when a named state/mode/context has independent reusable identity across propositions.

No current case forces a universal `State` or `Context` metaclass.

### Disposition

```text
State / Mode / Context dedicated first-class split: NOT FORCED
```

## 8. Pressure F - proposition-as-target

BA1-T1 allowed a `BAProposition` to be targeted by another proposition. The pressure cases show that this is not required by the minimal ontology and can blur two different meanings:

```text
project meaning being constrained
        !=
analytical assertion record describing that meaning
```

For example, `SR-3.4-C`, `SR-3.4-I` and `SR-3.4-P` constrain the delivery behavior itself. They do not semantically constrain the existence of the analytical proposition record used to describe the delivery.

The cleaner minimal rule is:

- if project meaning needs independent reuse/qualification, give that meaning `BAReferent` identity;
- `BAProposition` asserts methodology-neutral meaning about referents;
- provenance, diagnostic and change-state metadata may target proposition identity in BA3, but that is analytical metadata rather than a project-semantic proposition.

BA1-T2 therefore removes proposition-as-project-target as a required feature of the minimal candidate.

### Disposition

```text
BAProposition as target of project-semantic BAProposition: NOT REQUIRED / REMOVED FROM MINIMAL CANDIDATE
Proposition identity for provenance/change/diagnostic handling: STILL REQUIRED
```

This is a reduction of R1, not a new type.

## 9. Pressure G - bounded method-consumer projection

The BA0-T2 bounded STRIDE transfer consumer requires a projection containing:

- behavior;
- source;
- destination;
- information;
- correlation;
- responsibility/externality;
- current realization;
- failure semantics;
- confidentiality/integrity/authorized-origin constraints.

The two-family ontology can supply the needed identities without importing STRIDE or DFD types:

- independently reused project meanings are `BAReferent` identities;
- methodology-neutral assertions connecting and qualifying those referents are `BAProposition` identities;
- BA2 will define the minimal shared relation/action roles needed to make those propositions mechanically selectable;
- the STRIDE consumer adds its own categories and dispositions outside Base Analysis.

The consumer therefore does not need a dedicated `Actor`, `Process`, `DataStore`, `DataFlow` or `TrustBoundary` root in BA1.

This is an ontology-level pass, not yet a proof of the final BA2/BA4 material projection contract.

### Disposition

```text
Bounded method consumer: PASS AT BA1 IDENTITY-ONTOLOGY LEVEL
Method-specific type contamination: NOT REQUIRED
```

## 10. Collapse pressure - can the two families become one?

### 10.1 Strong collapse candidate

The genuine collapse hypothesis is:

```text
BAElement
```

with no normative semantic distinction between project referent identity and analytical assertion identity.

This fails.

The same referent can remain stable while propositions about it are introduced, revised, superseded, invalidated or diagnosed. In facial access, `CameraSubsystem` can persist while delivery/realization statements change under mutations. In order fulfillment, one `OrderEvaluation` participates in independently evolving propositions about reservation, payment, compensation and commitment.

Claim-level origin/change/diagnostic handling therefore cannot be reduced to referent identity without losing a real semantic distinction.

### 10.2 Physical single-class implementation is not semantic collapse

A storage implementation could materialize both families in one table/class with a mandatory discriminator. That does **not** falsify the two-family ontology: the semantic distinction would still exist as a normative partition with different invariants.

BA1 concerns semantic identity families, not the number of programming classes or database tables.

### Disposition

```text
Semantic collapse to one undifferentiated family: REJECTED
Single physical implementation class/table: REPRESENTATION CHOICE / IRRELEVANT TO BA1
```

## 11. Split-pressure summary

- Behavior/Event: **NOT FORCED** as dedicated type; independent event/behavior identity can be `BAReferent`.
- Information/Resource: **NOT FORCED**.
- Participant/Component/Capability: **NOT FORCED**.
- Boundary/Externality: **NOT FORCED**.
- Store: **NOT FORCED**.
- Contract: **NOT FORCED**.
- State/Mode/Context: **NOT FORCED**.
- Method-specific DFD/STRIDE roots: **REJECTED AS BA1 NECESSITY**.
- Proposition-as-project-target: **NOT REQUIRED / REMOVED FROM MINIMAL CANDIDATE**.
- Semantic one-family collapse: **REJECTED**.

No tested case reaches `FORCED CANDIDATE SPLIT`.

## 12. Refined two-family candidate

BA1-T2 therefore retains exactly two candidate identity families, with a sharper boundary.

### BA1-C1 - `BAReferent`

**Status:** STRONG CANDIDATE / NOT ACCEPTED

An independently identifiable unit of methodology-neutral shared project meaning that must be reusable across one or more propositions, projections or governed baselines.

Its semantic kind may matter and must not be lost, but BA1 does not yet require dedicated metaclasses for participant, information, behavior/event, store, contract, boundary, state or similar kinds.

When behavior/event/state/context meaning needs independent project-semantic reuse, it can itself be represented as a `BAReferent`.

### BA1-C2 - `BAProposition`

**Status:** STRONG CANDIDATE / NOT ACCEPTED

An independently identifiable methodology-neutral analytical assertion about one or more `BAReferent` identities, with enough identity for origin/provenance, diagnosis, reuse and change disposition.

A proposition is not itself the project meaning it describes. Project-semantic qualification should target referents, while proposition provenance/diagnostic state is handled as analytical metadata in BA3.

The exact proposition structure, predicates, roles, n-ary representation and action vocabulary remain BA2 questions.

## 13. What BA1-T2 does not decide

BA1-T2 does not decide:

- whether `BAReferent` and `BAProposition` share an abstract implementation superclass;
- the canonical semantic-kind/classification vocabulary;
- relation cardinalities or n-ary proposition encoding;
- action/predicate vocabulary;
- identity/equivalence/lifecycle mechanics;
- source locators and provenance records;
- diagnostic record schema;
- view/projection contracts;
- lexical controlled vocabulary;
- AnalysisRecord, Finding or method-specific schemas.

These remain in BA2-BA6 or the later analysis envelope.

## 14. Falsification assessment

The two-family candidate would have failed if any tested recurring kind required independent subtype-specific invariants that generic referent identity could not preserve, or if the bounded method consumer needed method-specific roots in the shared core.

No such counterexample was found in the two current corpora.

The candidate would also have been reducible if proposition identity could be eliminated without losing independent origin/change/diagnostic handling. The collapse test failed.

One R1 feature was weakened: proposition-as-project-target is unnecessary and risks confusing assertion records with project meaning. Removing it improves minimality.

## 15. Trial disposition

```text
BA1-T2                         COMPLETED / PROVISIONAL PASS WITH REFINEMENT
BAReferent                     STRONG CANDIDATE / NOT ACCEPTED
BAProposition                  STRONG CANDIDATE / NOT ACCEPTED
Dedicated domain-type splits   NOT FORCED BY TESTED EVIDENCE
Semantic one-family collapse   REJECTED
BA1                            OPEN / READY FOR DISTINCT CLOSURE REVIEW
BA2                            NOT STARTED
```

BA1 is **not closed by this trial**. The evidence is now stable enough to perform a distinct closure review rather than inventing another ontology experiment for reassurance.

## 16. Next authorized microstep

Execute only:

> **BA1-T3 - minimal BAE ontology closure review.**

BA1-T3 must test whether the refined two-family boundary is necessary, sufficient and correctly phased, and whether every remaining unresolved design question genuinely belongs to BA2-BA6.

If no material counterexample remains, BA1-T3 may close BA1 and authorize BA2. It must not begin relation/action vocabulary design inside the closure review.
