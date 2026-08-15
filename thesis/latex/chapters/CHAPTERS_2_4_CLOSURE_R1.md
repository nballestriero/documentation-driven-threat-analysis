# DDTA thesis Chapters 2-4 closure record

**Status:** CLOSED / FINALIZATION RECORD  
**Baseline before finalization:** `ec6c0107e0d5c0460d2afcbe12dae6f40bc5e6c5`  
**Date:** 15 August 2026

## Purpose

This record establishes a research freeze for the thesis block that motivates and defines the governed documentation layer before Base Analysis work starts. `FINAL` means stable for the current thesis scope, not immutable. A chapter may be reopened only under the explicit criteria below.

## Chapter 2 - Background

**Status: CLOSED / FINAL.**

The chapter already supports the downstream research direction without requiring conceptual revision. In particular it preserves the distinctions that:

- threat analysis can begin before implementation when adequate knowledge is available;
- documentation and an analyzable model are not synonyms;
- different analysis methods may require different viewpoints;
- Finding, threat/mitigation and SecurityRequirement are distinct artifacts;
- automated or LLM-produced artifacts remain candidates until semantically reviewed;
- traceability, provenance and change awareness affect analytical validity.

Normal Base Analysis refinement does not reopen Chapter 2.

### Reopen clause

Reopen only for a material literature/factual error, a materially unsupported claim, or falsification of a foundational distinction used by the thesis.

## Chapter 3 - State of the art and research gap

**Status: CLOSED / FINAL after editorial coherence correction.**

The G1-G4 research gap remains valid for the current thesis scope:

1. governed portable-by-construction documentation to a reviewed analyzable representation;
2. a common methodology-neutral core supporting different analysis viewpoints;
3. method-specific results through reviewed findings to governed security requirements;
4. change-aware traceability and re-analysis.

The finalization patch changes only a stale forward reference so that Chapter 3 no longer assigns the research-design role to the now-established documentation-metamodel Chapter 4. It does not change the research gap, RQs or evidence synthesis.

### Reopen clause

Reopen only if the research gap or evaluated thesis scope is materially falsified or materially changed, or if prior work is found to already solve a claimed discontinuity in the evaluated end-to-end sense.

## Chapter 4 - Documentation metamodel and authoring rules

**Status: CLOSED / FINAL after S1.5 + S2 consolidation.**

The final chapter consolidates the documentation semantics reached through the repository work up to SecurityRequirement:

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

with the concrete authoring/ownership path:

```text
Project problem framing [method precondition]
    -> MacroRequirement
    -> Decision
    -> FunctionalRequirement
    -> SecurityRequirement
       (concrete SpecializedRequirement)
```

### Consolidated closed results

- MR semantics and single macro responsibility;
- Decision as significant commitment under exactly one MR;
- FR as independently assessable operational Requirement under exactly one Decision;
- `Requirement [abstract]` as the common governed normative obligation;
- `Requirement.normativeClause : NormativeClause [1..*]`;
- coherent-unit and split-on-independence rule;
- `NormativeObligation` as a separate L1 metaclass REJECTED;
- SpecializedRequirement as a normative strengthening of exactly one FR;
- conjunctive composition and removal test;
- realization separation and no ordinary functional-correctness duplication;
- `SecurityRequirement IS-A SpecializedRequirement`;
- `protectedSecurityProperty : SecurityProperty [1]`;
- failure-mode explicitness in normative clauses;
- cause neutrality;
- one governing security property per coherent SecurityRequirement;
- Attack/Finding/Risk/Control/verification evidence excluded from SecurityRequirement core semantics.

### Still intentionally open outside the Chapter 4 closure

- complete lifecycle/history/change-event mechanism;
- exact L2 representation of `NormativeClause`;
- `SecurityProperty` taxonomy/refinement;
- possible future structural identity for `SecurityFailureMode`;
- Base Analysis / BAE;
- AnalysisRecord / Finding;
- STRIDE / STRIDE-AI overlays;
- Risk / Control / verification evidence;
- exact analytical provenance/change-event model.

These open items do not make Chapter 4 provisional because they belong to later owning layers unless a concrete counterexample demonstrates otherwise.

### Reopen clause

Reopen Chapter 4 only if a later phase produces a concrete recurring semantic failure that cannot be represented without changing the governed documentation contract. The counterexample must identify the minimum owning layer to change and must trigger regression of previously accepted corpora.

Examples that do **not** by themselves reopen Chapter 4:

- adding a BAE type or relation;
- adding a graphical Base Analysis projection;
- a method plugin needing private taxonomy fields;
- a tool proposing a new vocabulary synonym;
- an LLM producing a candidate BAE or finding;
- a new implementation/control technique.

## Freeze rule

After the finalization commit:

```text
Chapter 2  CLOSED / FINAL
Chapter 3  CLOSED / FINAL
Chapter 4  CLOSED / FINAL
```

Later thesis work should reference these chapters rather than continuously retrofitting them. Editorial correction remains possible, but semantic reopening requires the criteria above.

## Next research boundary

The next authorized research block is Base Analysis. The first microstep is to define the responsibility and boundary of the methodology-neutral analyzable representation before fixing a BAE taxonomy or applying a threat method.
