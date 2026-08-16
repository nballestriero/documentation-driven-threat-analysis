# DDTA Base Analysis responsibility boundary - R1

**Status:** CLOSED BY BA0-T3

**Repository baseline reviewed:** `ced13f9329c89c759b3608d66c3f81ac79b9469b`

**Activation:** applies when the BA0-T3 closure package is accepted and committed.

**Authority note:** this artifact defines the analysis-layer responsibility boundary; governed project documentation remains project authority.

## Responsibility statement

For a governed documentation baseline, **Base Analysis is the accepted methodology-neutral analytical representation of the shared project meaning required by DDTA**. It preserves baseline-scoped semantic identity, source/origin provenance and explicit unresolved state sufficiently to support reproducible reuse, progressive human and method-specific projections, source drill-down, change-impact reasoning and source-localized feedback handoff.

Base Analysis may normalize and derive analytical structure from governed meaning, but it must not silently create project commitments. Method-specific interpretation and analysis output remain outside the shared core. The representation may be reused or reproducibly rebuilt; semantic canonicality does not require one permanently materialized graph or implementation technology.

## Closed responsibilities

- **BA0-C1 Authority and provenance boundary:** project facts remain grounded in governed documentation; derivation and origin remain traceable.
- **BA0-C2 Baseline-scoped shared semantic identity:** accepted referents/propositions remain stable enough for reuse, comparison and revalidation.
- **BA0-C3 Method-neutral shared core:** method-owned semantics stay outside the common project-meaning layer.
- **BA0-C4 Explicit uncertainty and diagnostic localization:** encountered conflict, ambiguity, missing information or insufficiency is preserved rather than silently resolved.
- **BA0-C5 Projection readiness and source drill-down:** the same semantics support bounded human/method projections and navigation back to governed sources.
- **BA0-C6 Change-impact traceability:** source/semantic/dependency links support identification of potentially impacted analytical artifacts after change.
- **BA0-C7 Source-localized feedback handoff:** analysis outputs can identify the governed source area needing review without BA choosing or governing the correction.
- **BA0-C8 Minimality and representation independence:** only justified shared semantics belong in BA; no storage, notation, graph or general-purpose modeling language is mandated.

## Required origin-state responsibilities

At responsibility level BA must distinguish:

- grounded;
- derived;
- diagnostic / unresolved.

A general `reviewed analytical addition` class is **not required by BA0**. Any later proposal for such a shared-core construct must remain explicitly non-project-authoritative and may reopen BA0 if it changes the responsibility boundary.

## Closed non-goals

Base Analysis is not:

- project documentation authority or the document-governance workflow;
- an automatic arbitrary-narrative extraction/migration engine;
- a mechanism for silently promoting LLM/NLP/tool inference;
- a universal contradiction detector;
- a pre-approved BAE taxonomy or relation vocabulary;
- a SysML/KerML/ArchiMate/AADL replacement;
- a STRIDE/STRIDE-AI model or universal threat ontology;
- AnalysisRecord, Common Finding or Finding acceptance;
- the owner of corrective project decisions;
- a mandatory persisted graph/database/serialization/diagram;
- a proof of visualization usability;
- a downstream re-analysis scheduler.

## Deferred representation questions

BA1-BA6 decide how the closed responsibilities are represented, materialized, projected and regressed. BA0 closure accepts no BAE type or relation.

## Reopen rule

BA0 is reopened only by a material responsibility-level counterexample, not by ordinary ontology, relation, storage or rendering choices.
