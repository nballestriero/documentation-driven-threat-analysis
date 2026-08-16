# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 8**

**Status:** active execution plan after BA1 minimal identity-ontology closure.

**Supersedes:** Revision 7 only for forward execution state; R1-R7 remain historical research records.

## 1. Fixed prior state

- Chapters 2-4: CLOSED / FINAL for current thesis scope.
- Documentation layer: CLOSED.
- BA0-R systems-modeling prior-art research: CLOSED.
- BA0 responsibility/non-goals: CLOSED by BA0-T3.
- BA1 minimal BAE identity ontology: CLOSED by BA1-T3.
- ThreatForge is a case study/tooling instrument, not DDTA semantic authority.

## 2. Closed BA1 identity ontology

BA1 accepts exactly:

```text
BAReferent
BAProposition
```

`BAReferent` is the identity family for independently reusable methodology-neutral shared project meaning.

`BAProposition` is the identity family for independently reviewable methodology-neutral analytical assertions about BAReferents.

`BAE` is an umbrella term, not an additional required metaclass.

A BAReferent may denote structural, human/external, informational/resource, behavioral/event, contractual, storage, boundary, state/context or other project meaning. Current evidence does not require dedicated first-class roots for those categories.

## 3. Closed specialization rule

A new dedicated BAE type/family is justified only if evidence shows both:

1. independent semantic identity across propositions/projections/change; and
2. reusable subtype-specific invariants that cannot be represented honestly as classifications, roles, values or propositions over the closed families.

This prevents future BA phases from turning every useful semantic category into a metaclass by convenience.

## 4. Phase sequence after BA1

Do not skip phases:

```text
BA2 - Relations and canonical action vocabulary
BA3 - Document-to-BAE derivation, provenance and authority
BA4 - Multi-level human and method projections
BA5 - Controlled vocabulary and optional authoring/extraction assistance
BA6 - Base Analysis closure and regression
```

Formal analysis-envelope and threat-method work remains after BA6.

## 5. BA2 objective

BA2 decides the smallest stable methodology-neutral proposition/relation/action structure over the closed BA1 identity ontology.

BA2 must preserve three separations:

```text
semantic identity family
    !=
semantic relation / participation role
    !=
lexical label / authoring synonym
```

It must also keep method-owned threat semantics outside Base Analysis.

BA2 may define how reusable semantic classifications are represented, but it may not silently introduce new BA1 first-class identity families. A genuine third-family requirement reopens BA1.

## 6. BA2-T1 - proposition shape and participation-role lower bound

**NEXT / NOT EXECUTED BY THIS PLAN REVISION.**

BA2-T1 asks:

> What is the minimum methodology-neutral structural shape required for one BAProposition to express reusable project facts over BAReferents without freezing an exhaustive predicate vocabulary or importing a domain/method taxonomy?

### Pressure questions

BA2-T1 must test at least:

1. whether binary subject-predicate-object is sufficient or n-ary participation is required;
2. how one proposition can represent roles such as source, destination, information, correlation or responsibility without turning each role into a BA1 type;
3. whether action/behavior identity belongs to BAReferent while action semantics belong to proposition structure;
4. how qualifiers such as condition, state, failure, applicability or realization attach without creating assertion ambiguity;
5. how the same project meaning can participate in different semantic roles across propositions;
6. whether method-neutral classification must be explicit for mechanical projection or can be derived from proposition roles without raw-prose reconstruction.

### Guardrails

BA2-T1 must not:

- invent an exhaustive verb list;
- import STRIDE/DFD categories;
- define BA3 provenance fields;
- define BA4 views;
- create ThreatForge implementation classes;
- reopen BA1 unless a concrete identity counterexample is found.

### Exit condition

Produce a falsifiable lower-bound proposition structure with explicit alternatives rejected/deferred. Do not yet claim a complete canonical relation/action vocabulary unless the evidence genuinely forces it.

## 7. Later BA2 work - provisional sequence only

Only after BA2-T1 is reviewed should later BA2 microsteps pressure-test and close the actual relation/action vocabulary.

Likely concerns include:

- stable relation/action semantic identities;
- role cardinalities and n-ary propositions;
- dependency, responsibility, correlation, realization and constraint semantics;
- classification versus relation boundaries;
- lexical canonical labels versus authoring synonyms.

This section is planning only, not semantic acceptance.

## 8. BA3 - derivation, provenance and authority

After BA2 closure, BA3 must close:

- document-to-BAReferent/BAProposition derivation rules;
- source locators;
- grounded, derived and diagnostic/unresolved materialization;
- identity/equivalence/lifecycle rules;
- acceptance/rejection/stale semantics;
- source-to-analysis and analysis-to-source traceability.

Governed documentation remains project authority.

## 9. BA4 - projections

Define derived human and method projections from the same accepted BA semantics. No view becomes source authority.

## 10. BA5 - vocabulary and optional assistance

Define controlled vocabulary and optional assistance only after the semantic contracts exist. Lexical normalization, NLP/LLM proposals and authoring suggestions remain support mechanisms and cannot establish project semantics silently.

## 11. BA6 - Base Analysis closure and regression

Regress the implemented Base Analysis design against closed corpora and at least one structurally different holdout. BA6, not BA1, closes the complete Base Analysis design.

## 12. Analysis envelope remains downstream

Only after Base Analysis closure:

- A1 - AnalysisRecord / execution envelope;
- A2 - common reviewed Finding boundary;
- A3 - change/provenance integration;
- formal methodology overlays and STRIDE/STRIDE-AI evaluations.

The BA0-T2 STRIDE probe remains only a pre-overlay consumer probe.

## 13. Next authorized microstep

After the BA1-T3 closure package is committed and remotely verified, execute only:

> **BA2-T1 - minimal BAProposition structural shape and participation-role lower-bound derivation.**

Do not start formal STRIDE overlay design, Common Finding schema or implementation work.
