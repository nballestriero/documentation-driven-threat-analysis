# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 20**

**Status:** active BA5 execution plan after BA5-T1 canonical referent naming and controlled-authoring pressure testing.

**Supersedes:** Revision 19 only for forward execution state; R1-R19 remain historical research records.

## 1. Fixed prior state

- Chapters 2-4: CLOSED / FINAL for current thesis scope.
- Documentation layer: CLOSED.
- BA0 responsibility/non-goals: CLOSED.
- BA1 minimal BAE identity ontology: CLOSED.
- BA2 relation/action vocabulary: CLOSED BY BA2-T4.
- BA3 provenance/derivation/identity/lifecycle/change-revalidation: CLOSED BY BA3-T4.
- BA4 projection boundary/traceability/coverage/interpretation: CLOSED BY BA4-T3.
- `BAReferent` and `BAProposition`: ACCEPTED first-class semantic identity families.
- ThreatForge remains a case study/tooling instrument, not DDTA semantic authority.

## 2. BA5 objective - canonical semantic registry and controlled authoring

BA5 now starts from the stronger hypothesis that semantic authoring should be canonical by construction rather than synonym-normalized after the fact.

For named project referents and, subject to later pressure, the wider operative BA vocabulary:

```text
registered canonical token
    -> normative semantic authoring

unregistered alias / synonym
    -> not silently equivalent
```

The purpose is to maximize cross-document and cross-view consistency before investing in lexical normalization machinery.

NLP/LLM assistance remains downstream candidate-producing help and is not required by the current core hypothesis.

## 3. BA5-T1 result

**Status: COMPLETED / PROVISIONAL PASS WITH CANONICAL-REFERENT-NAMING LOWER-BOUND.**

T1 establishes provisionally:

```text
one named referent -> one exact canonicalName per baseline/scope   REQUIRED
same referent same name across governed semantic references        REQUIRED
same referent same name across shared derived views                REQUIRED
alias/synonym as second normative entity identifier                REJECTED
case/format variant as implicit alias                              REJECTED
canonical-name collision in one naming scope                       REJECTED
canonicalName == BAReferent identity                                REJECTED
governed cross-baseline rename + BA3 RETAIN                         PASS
projection-owned type/category labels                              ALLOWED
method-owned non-referent labels                                   ALLOWED DOWNSTREAM
tool exact validation/completion                                   ALLOWED
tool hidden alias normalization                                    REJECTED IN CORE
```

The decisive refinement is that naming invariance is baseline-scoped. A governed rename does not itself force new `BAReferent` identity.

## 4. Why this does not reopen BA1-BA4

- BA1 identity remains semantic; canonical name is lexical metadata.
- BA2 already distinguishes stable semantic keys from lexical wording and needs no `nameOf` operator.
- BA3 already supports RETAIN under wording/name change when meaning survives.
- BA4 projection-local taxonomy remains free; only the shared referent name is constrained when a projection presents that referent.

No new BAE family or BA2 operator is forced.

## 5. Registry responsibility

BA5-T1 requires an auditable governed canonical-name registry responsibility for named referents, but does not mandate one physical implementation.

Minimum properties:

- baseline/scope binding;
- exact canonical token;
- unambiguous referent resolution;
- uniqueness within the active naming scope;
- no normative alias equivalence by default.

A tool may enforce the registry, but cannot become semantic authority by inventing equivalence or accepted terms.

## 6. BA5-T2 - canonical semantic registry coverage and governed-extension pressure test

**NEXT / NOT EXECUTED BY THIS PLAN REVISION.**

BA5-T2 must pressure-test whether the same controlled-registry discipline can cover the wider operative BA vocabulary already established by BA2 without introducing unnecessary lexical machinery.

It must test at least:

1. the thirteen accepted `semanticOperatorKey` values;
2. operator-scoped `roleKey` values;
3. method-neutral `semanticKind` keys, including current evidence such as `store` and `contract`;
4. controlled values such as responsibility kinds and other non-identifiable semantic values;
5. exact-token validation and registry lookup across documentation -> BA -> projections;
6. the minimum governed workflow for admitting a genuinely new canonical term;
7. attempted alias/synonym introduction as a negative control; and
8. whether tool completion/validation can operate without semantic-authority leakage.

### BA5-T2 guardrails

Do not:

- build a synonym ontology by default;
- perform arbitrary-narrative migration;
- authorize NLP/LLM output as semantic truth;
- convert method-specific projection taxonomy into BA vocabulary;
- create new BAE families merely to store lexical keys;
- reopen BA0-BA4 without a material semantic counterexample;
- start BA6.

### BA5-T2 exit condition

Produce the next smallest controlled-registry lower-bound refinement and identify whether any concrete evidence actually forces synonym/alias support.

Do not close BA5 unless the integrated lexical/registry responsibilities have survived sufficient pressure.

## 7. BA6 - complete Base Analysis regression and closure

Only after BA5 closes, regress the complete BA0-BA5 design against the closed corpora and at least one structurally different holdout.

BA6 should emphasize the complete integration path:

```text
governed documentation
 -> canonical registry-controlled authoring
 -> accepted BA
 -> provenance/change continuity
 -> multiple projections
 -> rebuild / cross-projection comparison
```

BA6 may reopen only the smallest earlier responsibility on a material counterexample.

Only BA6 may close the complete Base Analysis milestone for current thesis scope.

## 8. Analysis envelope remains downstream

Only after Base Analysis closure:

- A1 - AnalysisRecord / execution envelope;
- A2 - common reviewed Finding boundary;
- A3 - change/provenance integration;
- formal methodology overlays and STRIDE/STRIDE-AI evaluations.

## 9. Next authorized microstep

Only after the BA5-T1 package is reviewed, committed, pushed and remotely verified, execute:

> **BA5-T2 - canonical semantic registry coverage and governed-extension pressure test.**

Do not start BA6 or downstream analysis schemas before BA5 is explicitly closed.
