# DDTA R25 — `consumeService` Question Pack R1

**Status:** TESTED / CONSTRUCT-SPECIFIC / NON-NORMATIVE
**Operator:** OP-09 `consumeService`
**Semantic family:** SF-01 Flow / Consumption / Service

This pack does not modify BA2 and cannot create project truth.

## Core admission questions

1. **Consumed object**
   - What exactly is being consumed/used?
   - Is it a service/capability, data/information/evidence, endpoint, technology, component, store,
     protocol, medium or artifact?

2. **Service/capability identity**
   - Does the proposed `service` term carry independently identifiable governed service/capability
     meaning?
   - Or are we merely relabeling a technology/component/endpoint as a service?

3. **Actual use**
   - Does the source govern actual functional use/consumption?
   - `available`, `exists`, `deployed`, `exposed`, or `configured` do not by themselves mean
     consumed.

4. **Consumer identity**
   - Which governed BAReferent is the genuine consumer?
   - Is the consumer a system, component, process, capability, organization or external client?

5. **Narrowest governed service**
   - What is the narrowest service/capability identity the source actually governs?
   - Do not invent a more elegant abstraction.

6. **Provider**
   - Does the source govern a distinct provider for the service?
   - If not, omit `provider`; do not infer `provider = service` or `provider = owner`.

7. **Provider independence**
   - Would `Provider P provides Service S` remain meaningful even if no consumer were currently
     governed?
   - If yes, retain the `provideService?` candidate for later construct exhaustion.

8. **Data/evidence boundary**
   - Is the consumed object actually data/result/evidence?
   - If yes, reject `consumeService` and route to `produce.input`, `observe`, `transfer` or PR-11
     `consumeData?` as appropriate.

9. **`produce.input` boundary**
   - Is the consumed information already an explicit input to a governed production?
   - Does independent functional consumption meaning remain after that proposition is recorded?

10. **Endpoint boundary**
    - Is the source governing invocation of an endpoint/path/interface?
    - Endpoint/path is not automatically the service.

11. **Invocation independence**
    - If the endpoint/interface changed while the same service/capability remained, would the
      service-use fact remain true?
    - If yes, service consumption and invocation are distinct semantics.

12. **Technology/component boundary**
    - Is the proposed service merely a library, runtime, technology or component being used?
    - Technology use is not automatically service consumption.

13. **`realize` boundary**
    - Does the source distinguish an abstract service/capability from a concrete realization?
    - If yes, preserve the distinction and do not consume the realization unless source meaning
      requires it.

14. **Production composition**
    - Does the service/capability produce a governed result?
    - If yes, `produce` may coexist; neither operator absorbs the other.

15. **Transfer composition**
    - Is content conveyed between participants?
    - Service use does not imply transfer; record `transfer` separately when governed.

16. **Observe composition**
    - Is the meaning primarily inspection/read/query of existing state?
    - `observe` may coexist or be more specific for that facet.

17. **Dependency composition**
    - Does service use also create prerequisite meaning?
    - Prefer `consumeService` for service use and derive dependency downstream unless the source
      separately governs an irreducible prerequisite.

18. **Ownership/responsibility**
    - Does the source explicitly preserve ownership/responsibility outside the consumed service?
    - `consumeService` never transfers either by itself.

19. **Scope**
    - Is consumption universal or branch-/workflow-/condition-specific?
    - Preserve the narrowest governed consumer scope.

20. **Delete test**
    - If `consumeService(C,S)` is removed while all other accepted propositions remain, can an
      analyst still reconstruct that C functionally uses service/capability S?
    - If not, the proposition carries autonomous meaning.

21. **Multiple consumers**
    - Does the corpus test one service consumed by multiple independently governed consumers?
    - If not, retain the frozen plural cardinality as untested rather than changing it.

22. **Provider role necessity**
    - Does provider identity carry information not reconstructible from service identity,
      realization or responsibility?
    - If the corpus does not test this, retain the optional role and mark empirical coverage weak.

23. **Capability identity falsification**
    - Try to restate the candidate service as technology/component/endpoint/store/medium/protocol.
    - If that loses nothing, service identity may be artificial.

24. **Interface replacement test**
    - If a concrete endpoint/interface/technology changed, would the same governed service
      consumption survive?
    - Use this only as a diagnostic; replacement imagination does not create project truth.

25. **Genuine consumer relation**
    - Does the source govern genuine use between independently identifiable meanings?
    - Mere containment, ownership, implementation or participation is not enough.

## Strong positive control

FR-22:

```text
B4 is an external service/system consumed by DermaTriage
and does not become owner of triage evaluation
```

Expected:

```text
consumeService
    consumer -> DermaTriage
    service  -> B4
```

## Data negative control

FR-18:

```text
HistoricalCaseContext consumed by BioMistral
```

`HistoricalCaseContext` is information/result, therefore this is not `consumeService`.

Route to PR-11 / CC-01 `consumeData?`.

## Invocation boundary control

FR-21:

```text
DirectClient invokes POST /analyze
POST /analyze invokes DermaTriageTriageProcess
```

This strongly tests PR-03 invocation semantics and must not turn the endpoint itself into the
consumed service.

## Technology ambiguity control

FR-18:

```text
DermaTriage indexes and queries in ChromaDB
```

This proves technology use, but not automatically service consumption.

Recheck under OP-10 `realize` and PR-08 store/persistence.

## Synthetic queue stress case

```text
SYNTHETIC ONLY
NOT PROJECT TRUTH
NOT G1 SOURCE EVIDENCE

Producer produces Message.
Message is published to Queue.
Consumer consumes Message from Queue.
```

Questions:

```text
Does Consumer consume Message?       -> data semantics
Does Consumer consume QueueService?  -> service semantics, only if governed
Is Message transferred?              -> transfer
Is Message persisted?                -> PR-08
Does Queue impose ordering?          -> PR-02 / selection/order semantics
```

Do not create any of these facts unless the governed source states them.
