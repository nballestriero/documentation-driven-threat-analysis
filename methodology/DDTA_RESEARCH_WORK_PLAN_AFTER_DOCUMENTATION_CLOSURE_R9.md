# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 9**

**Status:** active BA2 execution plan after BA2-T1 proposition-structure lower-bound derivation.

**Supersedes:** Revision 8 only for forward execution state; R1-R8 remain historical research records.

## 1. Fixed prior state

- Chapters 2-4: CLOSED / FINAL for current thesis scope.
- Documentation layer: CLOSED.
- BA0-R systems-modeling prior-art research: CLOSED.
- BA0 responsibility/non-goals: CLOSED.
- BA1 minimal BAE identity ontology: CLOSED.
- `BAReferent` and `BAProposition`: ACCEPTED first-class semantic identity families.
- ThreatForge is a case study/tooling instrument, not DDTA semantic authority.

## 2. Closed BA1 identity boundary

BA1 accepts exactly:

```text
BAReferent
BAProposition
```

No `Action`, `Relation`, `Participation`, `Role`, `Behavior`, `Information`, `Store`, `Contract`, `Boundary` or `State` identity family may be added by BA2 unless a concrete counterexample satisfies the BA1 reopen criteria.

## 3. BA2 objective

BA2 defines the smallest stable methodology-neutral proposition/relation/action semantics over the BA1 identities while preserving:

```text
semantic identity family
    !=
semantic operator / participation role / modifier
    !=
lexical label / authoring synonym
```

BA2 must support mechanical selection/projection without importing threat-method categories or requiring consumers to reinterpret raw prose.

## 4. BA2-T1 - proposition shape and participation-role lower bound

**Status: COMPLETED / PROVISIONAL CANDIDATE.**

BA2-T1 tested universal binary SPO, positional n-ary tuples and fixed domain/method slots against facial-access and order-fulfillment evidence.

### Result

```text
Pure binary SPO as universal core       REJECTED
Binary propositions as special cases   SUPPORTED
Anonymous positional participation      REJECTED
Role-bound n-ary participation          FORCED CANDIDATE
Explicit semantic operator              FORCED CANDIDATE
Scoped semantic modifier capability     REQUIRED / ENCODING OPEN
Third BA1 identity family               NOT FORCED
```

Active lower-bound candidate:

```text
BAProposition
|- semanticOperator                  1
|- participation                     1..*
|    |- role                         1
|    `- term                         1
`- scopedModifier                    0..*
```

At least one participant term is a BAReferent. Typed local values may appear when independent semantic identity is not required.

Referent classification remains separate from contextual proposition role. BA2-T1 supports explicit method-neutral classification capability but does not freeze its vocabulary or cardinality.

## 5. BA2-T2 - operator, role and modifier vocabulary pressure test

**NEXT / NOT EXECUTED BY THIS PLAN REVISION.**

BA2-T2 must attempt to derive the smallest reusable methodology-neutral vocabulary needed to instantiate the T1 structure.

Pressure areas:

1. operator families needed by both corpora without copying document predicate labels mechanically;
2. role semantics for actor/executor, source/destination, information/object, request/result, correlation/context, provider/consumer/responsibility and affected state;
3. whether roles are globally canonical or operator-scoped;
4. operator-role compatibility/cardinality constraints;
5. representation boundary between role-bound participants and scoped modifiers;
6. condition, state, failure, applicability, realization, atomicity/concurrency and negation/polarity pressure;
7. reusable referent classification needed for mechanical human/method projections;
8. bounded method-consumer mapping without STRIDE/DFD leakage.

### Exit condition

Produce a falsifiable vocabulary candidate and explicit rejected/deferred alternatives. Do not close BA2 if important operator/role/modifier ambiguity remains.

## 6. Later BA2 closure sequence - provisional only

If BA2-T2 yields a stable vocabulary candidate, later microsteps should pressure-test:

- cross-corpus regression;
- lexical canonical label versus synonym separation;
- role/cardinality consistency;
- whether any relation/action semantic identity needs a registry-level stable key;
- BA2 closure and reopen criteria.

The exact number of later microsteps is evidence-driven, not precommitted.

## 7. BA3 - derivation, provenance and authority

Only after BA2 closure, BA3 must close:

- document-to-BAReferent/BAProposition derivation rules;
- source locators;
- grounded, derived and diagnostic/unresolved materialization;
- identity/equivalence/lifecycle rules;
- acceptance/rejection/stale semantics;
- source-to-analysis and analysis-to-source traceability.

Governed documentation remains project authority.

## 8. BA4 - projections

Define derived human and method projections from the same accepted BA semantics. No view becomes source authority.

## 9. BA5 - vocabulary and optional assistance

Define lexical controlled vocabulary, authoring synonyms and optional assistance only after semantic operator/role contracts are closed. NLP/LLM proposals remain candidate-producing support and cannot establish project semantics silently.

## 10. BA6 - Base Analysis closure and regression

Regress the implemented Base Analysis design against closed corpora and at least one structurally different holdout. BA6 closes the complete Base Analysis design.

## 11. Analysis envelope remains downstream

Only after Base Analysis closure:

- A1 - AnalysisRecord / execution envelope;
- A2 - common reviewed Finding boundary;
- A3 - change/provenance integration;
- formal methodology overlays and STRIDE/STRIDE-AI evaluations.

The earlier STRIDE transfer probe remains only a bounded consumer probe.

## 12. Next authorized microstep

After the BA2-T1 package is reviewed, committed and remotely verified, execute only:

> **BA2-T2 - semantic operator, participation-role and scoped-modifier vocabulary pressure test.**

Do not start BA3, formal STRIDE overlay design, Common Finding schema or implementation work.
