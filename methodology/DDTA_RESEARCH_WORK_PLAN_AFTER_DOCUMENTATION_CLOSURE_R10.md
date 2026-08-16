# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 10**

**Status:** active BA2 execution plan after BA2-T2 operator/role/modifier vocabulary pressure testing.

**Supersedes:** Revision 9 only for forward execution state; R1-R9 remain historical research records.

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

BA2 must not introduce `Action`, `Relation`, `Participation`, `Role`, `Behavior`, `Information`, `Store`, `Contract`, `Boundary` or `State` as new first-class identity families unless a concrete BA1 reopen criterion is met.

## 3. BA2 objective

BA2 defines the smallest stable methodology-neutral proposition/relation/action semantics over the BA1 identities while preserving:

```text
semantic identity family
    !=
semantic operator / participation role / modifier
    !=
lexical label / authoring synonym
```

Base Analysis must support mechanical selection and projection without forcing consumers to reinterpret raw prose or import threat-method categories.

## 4. BA2-T1 - proposition structural lower bound

**Status: COMPLETED / PROVISIONAL CANDIDATE.**

BA2-T1 rejects pure binary SPO as the universal proposition shape and retains explicit n-ary role-bound participation with a stable semantic operator and scoped modifier capability.

```text
BAProposition
|- semanticOperator   1
|- participation      1..*
|    |- role          1
|    `- term          1
`- scopedModifier     0..*
```

## 5. BA2-T2 - operator, role and modifier vocabulary pressure test

**Status: COMPLETED / PROVISIONAL PASS WITH VOCABULARY-ARCHITECTURE REFINEMENT.**

BA2-T2 pressure-tested source-predicate copying, operator grouping, role scoping, modifier boundaries, polarity, classification and the bounded method consumer.

### Result

```text
Stable semantic operator key                 REQUIRED
Source predicate list as BA vocabulary       REJECTED
Lexical label as semantic identity            REJECTED
Operator-family facet                         PROVISIONAL ORGANIZING CANDIDATE
Seed operator key set                         PROVISIONAL CANDIDATE
Reusable role concepts                        SUPPORTED
Operator-scoped role compatibility/cardinality REQUIRED
Global context-free role contract             REJECTED
Untyped/free-text modifier bag                 REJECTED
Normalized local modifier capability           SUPPORTED / CANDIDATE
Explicit polarity                              STRONG CANDIDATE
Modifier promotion rule                        REQUIRED
Classification-as-BAProposition               STRONG CANDIDATE
Exact semantic-kind vocabulary                 OPEN
Third BA1 identity family                      NOT FORCED
```

The active vocabulary candidate is `BA2_SEMANTIC_VOCABULARY_CANDIDATE_R1.md`.

### Semantic boundaries retained

BA2-T2 explicitly preserves:

```text
correlation           != generic reference
service consumption   != ownership/management transfer
provider raw state    != governed project state
request acceptance    != physical handoff
realization           != generic local modifier when reusable
referent classification != participation role
```

### Modifier promotion rule

A modifier remains embedded only when it is local to one proposition/binding, has no new independent participant set, needs no independent assertion provenance/review identity, and is not reused as project meaning.

Otherwise model the meaning through explicit BAReferent/BAProposition semantics rather than a modifier mini-language.

## 6. BA2-T3 - cross-corpus regression and semantic-key/lexical separation

**NEXT / NOT EXECUTED BY THIS PLAN REVISION.**

BA2-T3 must replay the BA2-T2 candidate systematically against both current corpora rather than inventing more vocabulary for reassurance.

It must test:

1. whether every seed operator key is necessary or whether keys can merge without semantic loss;
2. whether any reviewed fact requires a missing method-neutral key or role distinction;
3. whether operator-scoped role contracts can assign compatible minimum/maximum cardinalities consistently;
4. whether the same semantic key remains stable across different source verbs and whether lexical synonyms can be separated cleanly from semantic identity;
5. whether explicit polarity avoids negative operator proliferation without weakening constraint semantics;
6. whether the modifier promotion rule keeps correlation, realization, responsibility and reusable constraints out of a generic modifier bag;
7. whether classification-as-proposition supplies the reusable semantic-kind distinctions needed by human/method consumers without reopening BA1;
8. whether the bounded STRIDE-oriented projection remains constructible without DFD/STRIDE leakage.

### Exit condition

Produce a regression disposition for each candidate key/role/modifier rule and identify the smallest unresolved set.

If the candidate survives but closure criteria still require a distinct review, schedule that review. Do not close BA2 merely because the current examples can be encoded, and do not invent additional microsteps without a concrete unresolved falsification target.

## 7. BA3 - derivation, provenance and authority

Only after BA2 closes, BA3 must close:

- document-to-BAReferent/BAProposition derivation rules;
- source locators;
- grounded, derived and diagnostic/unresolved materialization;
- identity/equivalence/lifecycle rules;
- acceptance/rejection/stale semantics;
- source-to-analysis and analysis-to-source traceability.

Governed documentation remains project authority.

## 8. BA4 - projections

Define derived human and method projections from the same accepted BA semantics. No view becomes source authority.

## 9. BA5 - lexical vocabulary and optional assistance

Only after semantic operator/role contracts are closed, define canonical display labels, authoring synonyms and optional assistance. NLP/LLM proposals remain candidate-producing support and cannot establish project semantics silently.

## 10. BA6 - Base Analysis closure and regression

Regress the complete Base Analysis design against closed corpora and at least one structurally different holdout. BA6 closes the complete Base Analysis design.

## 11. Analysis envelope remains downstream

Only after Base Analysis closure:

- A1 - AnalysisRecord / execution envelope;
- A2 - common reviewed Finding boundary;
- A3 - change/provenance integration;
- formal methodology overlays and STRIDE/STRIDE-AI evaluations.

The earlier STRIDE transfer probe remains only a bounded consumer probe.

## 12. Next authorized microstep

After the BA2-T2 package is reviewed, committed and remotely verified, execute only:

> **BA2-T3 - cross-corpus regression of the operator/role/modifier candidate and semantic-key/lexical separation.**

Do not start BA3, formal STRIDE overlay design, Common Finding schema or implementation work.
