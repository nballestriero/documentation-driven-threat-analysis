# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 12**

**Status:** active execution plan after BA2 relation/action vocabulary closure.

**Supersedes:** Revision 11 only for forward execution state; R1-R11 remain historical research records.

## 1. Fixed prior state

- Chapters 2-4: CLOSED / FINAL for current thesis scope.
- Documentation layer: CLOSED.
- BA0-R systems-modeling prior-art research: CLOSED.
- BA0 responsibility/non-goals: CLOSED.
- BA1 minimal BAE identity ontology: CLOSED.
- BA2 relation/action vocabulary: **CLOSED BY BA2-T4**.
- `BAReferent` and `BAProposition`: ACCEPTED first-class semantic identity families.
- ThreatForge is a case study/tooling instrument, not DDTA semantic authority.

## 2. Closed BA2 contract

BA2 closes:

```text
BAProposition
|- semanticOperatorKey   1
|- participation         1..*
|    |- roleKey          1
|    `- term             1
|- polarity              1
`- scopedModifier        0..*    [condition / temporalScope only]
```

Accepted current-scope operator registry:

```text
transfer
produce
create
observe
transition
correlate
reference
dependOn
consumeService
realize
assignResponsibility
constrain
classify
```

The registry is an accepted current-scope minimum with explicit reopen criteria. It is not a universal systems-modeling taxonomy or exhaustive verb dictionary.

BA2 also closes:

- operator-scoped role/cardinality contracts;
- explicit polarity;
- responsibility/ownership represented through `assignResponsibility + responsibilityKind + polarity`;
- modifier promotion rule and local `condition`/`temporalScope` lower bound;
- governed reusable completion/failure/atomicity/concurrency/idempotency rules as explicit `constrain` semantics;
- classification-as-proposition plus controlled semantic-kind registry contract;
- semantic-key versus lexical-label separation;
- no STRIDE/DFD categories and no third BA1 identity family in the common core.

## 3. BA3 objective

BA3 must define the smallest provenance/authority/derivation mechanics that connect governed documentation to the closed BA1/BA2 semantics without making Base Analysis a second project authority.

The core question is:

> How can each accepted BAReferent/BAProposition be reproducibly connected to the governed baseline and its derivation status so that consumers can drill down, diagnose uncertainty, reason about change and return corrective feedback to the right source without silently inventing project truth?

BA3 must preserve:

```text
governed documentation = project authority
Base Analysis          = accepted analytical representation
analysis result         = method-owned / reviewable
corrective candidate    = proposed documentation change
```

## 4. BA3-T1 - source-to-Base-Analysis derivation and provenance lower-bound pressure test

**NEXT / NOT EXECUTED BY THIS PLAN REVISION.**

BA3-T1 must derive only the minimum provenance/origin structure forced by the closed BA0 responsibilities and the current corpora.

It must pressure-test at least:

1. whether provenance attaches independently to `BAReferent`, `BAProposition`, or both;
2. many-to-many source-to-BA derivation (one clause -> multiple propositions; one meaning -> multiple source clauses);
3. governed source locator granularity sufficient for exact drill-down without copying source prose as authority into BA;
4. baseline identity/version context so the same source locator across revisions is not silently conflated;
5. the minimum distinction among `grounded`, `derived` and `diagnostic/unresolved` analytical materialization already required by BA0;
6. whether a derived proposition must record its derivation basis separately from the source authority it ultimately traces to;
7. how provenance behaves when a reusable BAReferent is supported by several document branches;
8. whether current evidence forces assertion acceptance/review state now or whether that belongs to a later BA3 microstep;
9. how to avoid encoding analysis-method findings or ThreatForge runtime state as source provenance.

### BA3-T1 guardrails

Do not:

- redefine the closed BA2 operator/role vocabulary;
- create new BAE identity families merely for provenance records;
- make Base Analysis project authority;
- design BA4 projections;
- define STRIDE/STRIDE-AI overlay schemas;
- define AnalysisRecord/Common Finding;
- design ThreatForge implementation classes or database tables;
- solve arbitrary legacy-document extraction.

### BA3-T1 exit condition

Produce a falsifiable provenance/derivation lower-bound candidate and an explicit unresolved set. Do not close BA3 in T1 unless the evidence unexpectedly shows no remaining distinct provenance/lifecycle question; default expectation is that later BA3 pressure will still be required.

## 5. BA4 - projections

Only after BA3 closes, define derived human and method projections from the same accepted BA semantics. No view becomes project authority.

## 6. BA5 - lexical vocabulary and optional assistance

Only after BA3/BA4 boundaries are stable, define canonical display labels, authoring synonyms and optional assistance. NLP/LLM proposals remain candidate-producing support and cannot establish project semantics silently.

## 7. BA6 - complete Base Analysis regression and closure

Regress the complete BA0-BA5 design against the closed corpora and at least one structurally different holdout. BA6 may reopen the smallest earlier phase only on a material counterexample.

## 8. Analysis envelope remains downstream

Only after Base Analysis closure:

- A1 - AnalysisRecord / execution envelope;
- A2 - common reviewed Finding boundary;
- A3 - change/provenance integration;
- formal methodology overlays and STRIDE/STRIDE-AI evaluations.

The earlier STRIDE transfer probe remains only a bounded consumer probe.

## 9. Next authorized microstep

After the BA2-T4 closure package is reviewed, committed, pushed and remotely verified, execute only:

> **BA3-T1 - source-to-Base-Analysis derivation and provenance lower-bound pressure test.**

Do not start BA4, formal threat-method overlays, Common Finding schema or implementation work.
