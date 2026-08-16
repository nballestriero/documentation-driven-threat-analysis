# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 6**

**Status:** active BA1 execution plan after BA1-T1 candidate derivation.

**Supersedes:** Revision 5 only for forward execution state; R1-R5 remain historical research records.

## 1. Fixed prior state

- Chapters 2-4: CLOSED / FINAL for current thesis scope.
- Documentation layer: CLOSED.
- BA0-R systems-modeling prior-art research: CLOSED.
- BA0 responsibility/non-goals: CLOSED by BA0-T3.
- ThreatForge is a case study/tooling instrument, not DDTA semantic authority.
- No historical focus set, systems-modeling metaclass or threat-method element is inherited automatically into BA1.

## 2. BA0 boundary carried forward

Base Analysis must preserve baseline-scoped shared semantic identity, source/origin provenance and explicit unresolved state sufficiently for reusable human/method projections, source drill-down, change-impact reasoning and source-localized feedback handoff.

The representation remains methodology-neutral and implementation-independent. Grounded, derived and diagnostic/unresolved are responsibility-level origin/state distinctions; a generic reviewed analytical-addition class is not required.

## 3. BA1 objective

BA1 decides the **minimal first-class identity ontology** needed to realize the BA0 boundary.

For every recurring semantic responsibility, test first whether it can remain:

- relation;
- role/classification;
- property/value;
- constraint/state;
- provenance/diagnostic record;
- derived/projection construct.

Only independent semantic identity plus reusable subtype-specific invariants justify a first-class split.

```text
semantic responsibility exists
        !=
first-class metaclass required
```

## 4. BA1-T1 - minimal ontology candidate derivation

**Status: COMPLETED / PROVISIONAL CANDIDATE.**

BA1-T1 rejects both extremes:

1. one undifferentiated analytical element type is too weak because it hides the distinction between identity of a project referent and identity/origin/evolution of analytical claims;
2. domain-specific root taxonomies are premature because current evidence does not yet force separate `Behavior`, `Information`, `Participant`, `Store`, `Contract`, `Boundary`, `State`, etc. metaclasses.

The resulting falsifiable candidate is:

```text
BAReferent     CANDIDATE / NOT ACCEPTED
BAProposition  CANDIDATE / NOT ACCEPTED
```

`BAReferent` provides independent identity for shared project meaning. `BAProposition` provides independent identity for provenance-bearing shared analytical claims. Specific semantic kinds remain open split hypotheses.

No relation vocabulary is closed by T1.

## 5. BA1-T2 - split-or-collapse pressure test

**NEXT / NOT EXECUTED BY THIS PLAN REVISION.**

Pressure-test the two-family candidate against deliberately difficult cases:

1. **Behavior/event identity:** can FR-3.4 delivery and the physical handoff milestone be represented without a dedicated Behavior/Event type while preserving specialized constraints and cross-branch reuse?
2. **Information/resource lifecycle:** do `RecognitionCapture`, `OrderEvaluation`, `Reservation`, result objects and their correlation/lifecycle semantics require a separate Information/Resource type?
3. **Responsibility and externality:** can internal/external ownership, provider boundaries and capability/service consumption remain propositions/roles over referents without dedicated Participant/Component/Boundary roots?
4. **Store and contract identity:** do the store candidate `InventoryLedger` and the contract candidates `PaymentProviderContract` / `CarrierContract` require subtype-specific first-class invariants?
5. **State/context:** can `ACCEPTED`, `authorized/declined/indeterminate`, reservation lifecycle and failure states remain values/qualifiers/propositions?
6. **Method consumer:** can one bounded method-specific projection select what it needs without reconstructing missing domain kinds independently from raw prose?
7. **Collapse test:** can `BAReferent` and `BAProposition` be merged without losing assertion-level provenance/change semantics?

### BA1-T2 exit

Record for every deferred split one of:

- `NOT FORCED`;
- `FORCED CANDIDATE SPLIT`;
- `REQUIRES MORE EVIDENCE`;
- `REJECTED`.

Do not close BA1 merely because the two-family candidate survives one corpus fragment.

## 6. BA1 closure review

After BA1-T2, execute a distinct closure review only if the candidate is stable enough to define a minimal ontology without embedding relation vocabulary or provenance mechanics.

Closure must state:

- accepted first-class BAE types/families;
- explicit non-types/roles/properties/deferred constructs;
- first-class identity criterion;
- reopen criteria;
- what remains for BA2-BA6.

Only explicit BA1 closure authorizes BA2.

## 7. Sequence after BA1 closure

Do not skip phases:

```text
BA2 - Relations and canonical action vocabulary
BA3 - Document-to-BAE derivation, provenance and authority
BA4 - Multi-level human and method projections
BA5 - Controlled vocabulary and optional authoring/extraction assistance
BA6 - Base Analysis closure and regression
```

### BA2

Define the smallest stable relation/action vocabulary over the accepted BA1 identity ontology. Keep semantic relation, canonical lexical label and authoring synonym assistance separate.

### BA3

Close identity/equivalence/lifecycle rules, source locators, grounded/derived/diagnostic materialization, acceptance/rejection, stale state and document-to-analysis traceability.

### BA4

Define derived human and method projections. No view is source authority.

### BA5

Define controlled vocabulary and optional assistance. LLM/NLP proposals remain candidate-producing support and cannot establish authority silently.

### BA6

Regress the Base Analysis against closed corpora and at least one structurally different holdout before formal overlay work.

## 8. Analysis envelope remains downstream

Only after Base Analysis closure:

- A1 - AnalysisRecord / execution envelope;
- A2 - common reviewed Finding boundary;
- A3 - change/provenance integration;
- formal methodology overlays and STRIDE/STRIDE-AI evaluations.

The BA0-T2 STRIDE probe remains only a pre-overlay consumer probe.

## 9. Next authorized microstep

Execute only:

> **BA1-T2 - split-or-collapse pressure test of the two-family candidate.**

Do not start BA2, formal STRIDE overlay design, Common Finding schema or implementation work until BA1 closes explicitly.
