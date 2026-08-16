# BA1-T3 - Minimal BAE ontology closure review

**Revision:** R1

**Status:** CLOSED / BA1 COMPLETE

**Repository baseline reviewed:** `e88d7e220536863d564f9e3b9fac7f1592a8c440`

**Phase:** BA1 - Minimal BAE ontology

**BA0:** CLOSED

**BA2:** NOT STARTED BY THIS REVIEW

## 1. Closure question

BA1-T3 asks only:

> Is the refined `BAReferent + BAProposition` identity boundary necessary, sufficient and correctly phased to close BA1 without importing relation vocabulary, domain taxonomies, document types, threat-method categories or implementation structure?

This is a closure and falsification review. It is not another ontology invention exercise.

The test uses the exit criteria from Work Plan R7: necessity, sufficiency, no leakage, correct phase placement, the T2 minimality refinement and a stop criterion against unnecessary BA1-T4 work.

## 2. What "base entities" means in BA1

The phrase "base entities that describe the project" is directionally useful but needs one distinction.

`BAReferent` is the family for **what shared project meaning is being talked about**. That meaning may be structural, informational, behavioral, contractual, stateful or otherwise conceptual; it is not necessarily one runtime object instance.

`BAProposition` is the family for **what Base Analysis asserts about those referents**.

For example, a bounded facial-access projection can distinguish referents such as:

- CameraSubsystem;
- RecognitionProcessor;
- RecognitionCapture;
- RecognitionRequest;
- the delivery behavior itself when it needs reusable identity;
- the current Ethernet realization if analysis needs to identify it independently.

Separate propositions can then state source, destination, information carried, correlation, failure semantics, responsibility/externality and applicable security constraints.

This avoids forcing every useful noun or behavior into its own metaclass while preserving enough identity for later relations, provenance and projections.

## 3. Evidence inherited from BA1-T1 and BA1-T2

BA1-T1 established the lower-bound distinction between referent identity and assertion identity. It rejected one fully undifferentiated analytical element and deliberately left conventional domain roots unaccepted.

BA1-T2 then attacked the candidate in both directions:

- split pressure across behavior/event, information/resource and participant/capability;
- separate split pressure across boundary/externality, store, contract and state/context;
- bounded method-consumer pressure using the earlier STRIDE transfer probe;
- collapse pressure attempting to remove the semantic distinction between BAReferent and BAProposition.

No tested semantic kind forced a dedicated first-class split. The semantic one-family collapse failed. T2 also removed an R1 overextension: project-semantic qualification should target the underlying BAReferent, not treat a BAProposition record as the project meaning being constrained.

## 4. Necessity test A - remove `BAReferent`

### Hypothesis

Represent only analytical assertions, using source strings, document identifiers or assertion-local values for the things those assertions mention.

### Failure

The same project meaning is reused across multiple assertions, projections and baselines. Facial access needs stable recognition of CameraSubsystem, RecognitionProcessor, RecognitionCapture and RecognitionRequest across delivery, security and mutation reasoning. Order fulfillment reuses OrderEvaluation, Reservation, provider/contract meanings and the physical handoff milestone across branches.

Without referent identity, each proposition or projection must reconstruct equivalence independently or rely on document syntax as semantic identity. That breaks or weakens:

- BA0-C2 baseline-scoped shared semantic identity;
- BA0-C5 projection reuse and source drill-down;
- BA0-C6 change-impact traceability;
- the method-neutral reuse required by the T2 consumer probe.

### Disposition

```text
Remove BAReferent: FAIL
BAReferent necessity: SUPPORTED
```

## 5. Necessity test B - remove `BAProposition`

### Hypothesis

Keep only BAReferent and attach every fact as anonymous properties/edges, or reify each assertion as another generic referent.

### Failure

Current evidence requires claim-level origin and evolution distinct from referent identity. A CameraSubsystem referent may remain stable while a delivery or realization assertion is retained, revised or retired. One OrderEvaluation participates in independently evolving claims about reservation, payment, compensation and commitment.

Anonymous properties/edges can be given IDs and metadata, but once they have independent assertion identity, origin, diagnosis and change disposition they implement proposition semantics under another representation. Reifying every assertion as an undifferentiated referent likewise hides rather than removes the distinction.

Removing BAProposition therefore undermines:

- BA0-C1 origin/provenance boundary;
- BA0-C4 diagnostic localization;
- BA0-C6 change-impact traceability;
- BA0-C7 source-localized feedback handoff.

### Disposition

```text
Remove BAProposition: FAIL
BAProposition necessity: SUPPORTED
```

## 6. Sufficiency test - does a third family remain hidden?

The closure review rechecks every split pressure raised by R2.

### Behavior / event

The facial-access delivery and order-fulfillment physical handoff need reusable semantic identity in some projections. That is sufficient pressure for BAReferent identity, but not for a universal Behavior/Event root with closed subtype-specific invariants.

**Disposition:** NOT FORCED AS FIRST-CLASS SPLIT.

### Information / resource

RecognitionCapture, RecognitionRequest, OrderEvaluation, Reservation and result concepts need stable identity and lifecycle/correlation assertions. Current evidence does not establish a common invariant set that requires a separate Information/Resource identity family.

**Disposition:** NOT FORCED AS FIRST-CLASS SPLIT.

### Participant / component / capability / boundary

Internal and external responsibility placement must be explicit, but it can be expressed through referent identities plus method-neutral roles/propositions. Service consumption does not transfer ownership.

**Disposition:** NOT FORCED AS FIRST-CLASS SPLIT.

### Store / contract

InventoryLedger, ReservationStore, PaymentProviderContract and CarrierContract can have stable BAReferent identity and distinct classifications. The reviewed evidence does not require separate root invariants for all stores or contracts.

**Disposition:** NOT FORCED AS FIRST-CLASS SPLIT.

### State / context

Local states may remain values; asserted conditions/transitions may be propositions; independently reusable named states or contexts may receive BAReferent identity. No universal State/Context root is required.

**Disposition:** NOT FORCED AS FIRST-CLASS SPLIT.

### Diagnostic / provenance / view

These are real BA0 responsibilities but their independent representation belongs to BA3/BA4 metadata and projection contracts. Promoting them to domain BAE roots would confuse ontology with analytical administration.

**Disposition:** CORRECTLY DEFERRED.

### Sufficiency result

No material identity responsibility remains unrepresented. The two families are sufficient at the BA1 abstraction level.

## 7. No-leakage review

The closure boundary does not require:

- MR/Decision/FR/SR document kinds as BAE types;
- STRIDE, STRIDE-AI or DFD roots;
- actor/component/asset/boundary/data_flow historical taxonomy;
- SysML/KerML/ArchiMate/AADL metaclasses;
- ThreatForge classes;
- one graph, database, programming class hierarchy or diagram notation;
- a fixed semantic-kind vocabulary.

This preserves BA0-C3 method neutrality and BA0-C8 representation independence.

## 8. Specialization review - types versus classifications

BA1 closure explicitly distinguishes three levels:

```text
first-class identity family
    BAReferent / BAProposition

method-neutral semantic kind or role
    behavior, information, capability, contract, store, state, ...

method-specific interpretation
    STRIDE/DFD/etc. categories owned by the analysis method
```

The middle level is important: the project can distinguish a delivery behavior from information or a contract without requiring three independent ontology roots.

BA2 may define how proposition participation roles, relation/action semantics and reusable semantic classifications are represented. BA5 may later address controlled lexical vocabulary and authoring assistance. Neither phase may silently promote a category into a new BA1 root without a concrete reopen trigger.

## 9. Correct phase-placement review

The unresolved questions after BA1 are real, but they do not block identity-ontology closure.

- proposition arity, participant roles, relation/action semantics -> **BA2**;
- identity/equivalence mechanics, source locators, grounded/derived/diagnostic materialization, stale/change state -> **BA3**;
- human/method views and projection contracts -> **BA4**;
- controlled vocabulary, lexical normalization and optional assistance -> **BA5**;
- full Base Analysis regression and implementation-independent closure -> **BA6**;
- AnalysisRecord, Finding and formal method overlays -> **after BA6**.

No unresolved BA1 identity question is being hidden inside BA2-BA6.

## 10. Minimality refinement review

T2 removed proposition-as-project-target from the required core. BA1-T3 confirms that reduction.

If a delivery, milestone, policy-like meaning or named state must be qualified by multiple project-semantic assertions, that meaning receives BAReferent identity. BAProposition remains the assertion record carrying claim-level provenance/diagnostic/change pressure.

This avoids confusing "the thing being constrained" with "the analytical statement describing the constraint".

## 11. First-class split criterion

BA1-T3 closes the following criterion:

> A new dedicated BAE type/family requires both independent semantic identity across propositions/projections/change and reusable subtype-specific invariants that cannot be represented honestly as classifications, roles, values or propositions over the accepted families.

This criterion is deliberately stronger than "the concept appears often" or "a tool/method has a class for it".

## 12. Reopen review

Future specialization is allowed, but not by silent ontology growth.

BA1 must be reopened if later concrete evidence proves, for example, that a behavior/event, information, state, boundary, contract or other semantic kind needs subtype-specific invariants that generic BAReferent plus BAProposition cannot preserve for method-neutral consumers.

Ordinary implementation convenience, prettier diagrams or one analysis method's preferred taxonomy do not reopen BA1.

## 13. Stop criterion

The closure review found:

- both accepted families are necessary;
- no tested third identity family is necessary;
- the two-family boundary is method-neutral and representation-independent;
- residual questions have valid owners in BA2-BA6;
- the T2 reduction removes rather than adds ontology surface.

A BA1-T4 experiment would therefore be reassurance work without a specific unresolved falsification target.

### Disposition

```text
BA1-T4: NOT REQUIRED
```

## 14. BA1 closure decision

BA1 is closed for the current thesis scope.

```text
BA1                             CLOSED
BAReferent                      ACCEPTED
BAProposition                   ACCEPTED
BAE umbrella metaclass          NOT REQUIRED
Dedicated domain root splits    NOT REQUIRED BY CURRENT EVIDENCE
Proposition-as-project-target   NOT REQUIRED
BA2                             NOT STARTED / NEXT AUTHORIZED PHASE
```

The accepted boundary is recorded canonically in `BA1_MINIMAL_BAE_IDENTITY_ONTOLOGY_R1.md`.

## 15. Next authorized microstep

After this closure package is reviewed, committed and remotely verified, execute only:

> **BA2-T1 - minimal BAProposition structural shape and participation-role lower-bound derivation.**

BA2-T1 must ask what minimum methodology-neutral structure allows a BAProposition to state reusable facts over BAReferents without yet freezing an exhaustive relation/action vocabulary or importing method-specific semantics.
