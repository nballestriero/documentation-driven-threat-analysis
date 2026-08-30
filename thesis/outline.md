# Thesis outline

## Status and authority

This is the current forward thesis-structure map after R25 Phase 4 orientation synchronization.

Reviewed standalone chapter authority currently exists for Chapters 2-4.

```text
Chapter 2
    Background
    CLOSED / FINAL for current scope

Chapter 3
    State of the Art / Research Gap
    CLOSED / FINAL for current scope

Chapter 4
    Documentation metamodel and authoring rules
    CLOSED / FINAL for current scope
```

Chapters 1 and 5 onward remain forward structure / authoring orientation until separately reviewed.

The outline does not make deferred empirical results writable merely by naming their future chapter.

## 1. Introduction

Problem, motivation, focused research questions, candidate contributions, scope and thesis structure.

The contribution must be stated with evidence-qualified wording.

Primary evaluation scope remains RQ1-RQ4.

Economic cost, ROI, broad adoption studies and reliable migration from arbitrary legacy documentation into DDTA-portable form remain outside the primary thesis claim.

## 2. Background — CLOSED / FINAL

Current reviewed source:

- `thesis/latex/chapters/02-background.tex`

The chapter provides the conceptual background required for later DDTA work, including:

- early threat analysis and system understanding;
- distinctions among documentation, analyzable representations, findings, mitigations and Security Requirements;
- method-dependent analysis viewpoints;
- traceability, provenance and change awareness;
- automation / LLM candidate generation versus governed acceptance.

Semantic reopening follows only the criteria recorded in `CHAPTERS_2_4_CLOSURE_R1.md`.

## 3. State of the Art / Research Gap — CLOSED / FINAL

Current reviewed source:

- `thesis/latex/chapters/03-state-of-the-art-and-research-gap.tex`

The current research gap remains organized around:

```text
G1
    governed portable-by-construction documentation
    -> reviewed analyzable representation

G2
    methodology-neutral common core
    -> multiple analysis viewpoints

G3
    method-specific results
    -> reviewed findings
    -> governed Security Requirements

G4
    change-aware traceability
    -> re-analysis
```

The chapter does not assign the Research Method role to Chapter 4.

Semantic reopening follows only the criteria recorded in `CHAPTERS_2_4_CLOSURE_R1.md`.

## 4. Documentation metamodel and authoring rules — CLOSED / FINAL

Current reviewed source:

- `thesis/latex/chapters/04-documentation-authoring-metamodel.tex`

This chapter owns the governed documentation layer and its reviewed authoring semantics.

Current closed structural baseline:

```text
GovernedDocument
    |
    +-- MacroRequirement
    +-- Decision
    `-- Requirement [abstract]
            normativeClause : NormativeClause [1..*]
            |
            +-- FunctionalRequirement
            `-- SpecializedRequirement [abstract]
                    `-- SecurityRequirement
```

The chapter covers the reviewed documentation hierarchy and authoring rules through SecurityRequirement.

Later Base Analysis, projections, threat methods, Findings, implementation controls, and BA-specific vocabulary are downstream and do not become Chapter 4 semantics merely because they consume the documentation.

Semantic reopening requires the explicit counterexample/reopen criteria recorded in `CHAPTERS_2_4_CLOSURE_R1.md`.

## 5. Documentation-Driven Threat Analysis and Base Analysis methodology

Working forward chapter.

This chapter should explain the stable DDTA method downstream of the governed documentation contract.

Expected evidence-qualified content:

### 5.1 Documentation-to-BA boundary

- frozen documentation authoring/review protocol R4;
- documentation authority over Base Analysis;
- `NOT SPECIFIED` as valid traceable meaning;
- handoff from governed project documentation to source-first Base Analysis.

### 5.2 BA0 — responsibility boundary

What Base Analysis is and is not.

### 5.3 BA1 — identity ontology

`BAReferent` and `BAProposition`.

### 5.4 BA2 — relation/action vocabulary

Current pre-holdout BA2 R3 semantics, including only the validated local refinements:

```text
transfer.behavior
decisionRule.satisfies
```

### 5.5 BA3 — provenance, derivation, lifecycle and change

Source provenance and later impact/revalidation semantics.

### 5.6 BA4 — projection boundary

Methodology-specific projections consume the shared BA without redefining canonical BA semantics.

### 5.7 BA5 — canonical semantic registry and controlled authoring

Canonical token / registry discipline and controlled extension.

### 5.8 Facial Access worked example

Writable through:

```text
FACIAL-ACCESS-GOV-R2
source-first BA
representation-pressure review
BA2 R3
complete Facial Access BA
post-BA regression PASS
```

The worked example must retain its single-case evidence boundary.

### 5.9 BA6 integrated validation boundary

BA6 remains OPEN.

Do not write BA6 as closed before the holdout, multiple projections, governed change, BA3 revalidation and rebuild/re-analysis complete the inherited gate.

## 6. Research method and evaluation protocol

Working forward chapter.

This chapter owns the experimental and validation design, not Chapter 4.

Expected content includes:

- research questions and hypotheses;
- R25 pre-holdout freeze rationale;
- anti-contamination protocol;
- selection criteria for a structurally different holdout after Phase 5;
- project source / authority baseline pinning;
- documentation B0 construction and semantic regression;
- governance promotion;
- source-first BA B0;
- representation-pressure review;
- multiple BA4 projections;
- governed B0 -> B1 change;
- BA3 impact / revalidation;
- BA and projection rebuild / re-analysis;
- comparison/evaluation criteria;
- validity threats and reproducibility.

The protocol may be written before empirical results exist.

The holdout must not be selected or authored before the immutable PRE-HOLDOUT FREEZE closes.

## 7. ThreatForge reference implementation

Deferred until methodology stabilization and the later authorization point.

ThreatForge is a downstream reference implementation / experimental harness.

It must consume DDTA semantics rather than define them.

Future material may cover architecture, implementation mechanisms and methodology-plugin execution only when the stable contracts and evaluation sequence authorize that work.

Historical ThreatForge evidence remains research history and is not the new holdout.

## 8. Evaluation

Empirical results remain deferred until the required executions exist.

Expected later evaluation areas include:

- holdout documentation-method replication;
- holdout BA construction and representation pressure;
- multiple projections from the same canonical BA;
- STRIDE / STRIDE-AI or other authorized threat-method evaluation;
- Common Finding boundary behavior;
- provenance and Security Requirement feedback;
- governed change and stale/re-analysis behavior;
- BA6 integrated verdict.

No result should be prewritten as successful.

## 9. Discussion

Interpret results against literature and the declared evidence boundaries.

Expected themes include:

- transferability beyond Facial Access;
- limits of the portability contract;
- human-review dependence;
- method-neutral versus method-specific semantics;
- under-specification and `NOT SPECIFIED`;
- counterexample-driven refinement;
- limits of the evaluated methodology set;
- automation risks;
- validity threats;
- future legacy-document migration research.

## 10. Conclusions

Answer RQ1-RQ4 only from evidence actually available at thesis completion.

State demonstrated contributions and explicit non-claims.

Do not present untested generality, open BA6 requirements, or deferred evaluation as established results.
