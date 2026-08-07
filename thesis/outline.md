# Thesis outline

## 1. Introduction

Problem, motivation, focused research questions, candidate contributions, scope and thesis
structure. The central contribution is not a new threat-analysis method: it is a
documentation-primary, methodology-neutral core that supports multiple method overlays and
returns accepted results to governed documentation as Security Requirements.

Primary evaluation scope: RQ1-RQ4. Economic cost, ROI and broad adoption studies are excluded.

## 2. Background

### 2.1 Threat modeling and early analysis
System understanding before code, scope, threat/finding/mitigation/security-requirement
distinctions, and repeated analysis across system evolution.

### 2.2 Representations used by threat-analysis methods
Components and data flows, assets, attacker/scenario views, goals and anti-goals, requirements,
architectural views and other method-dependent representations. Do not assume one universal
representation.

### 2.3 Security Requirements Engineering
From security problems and accepted analytical results to testable product obligations;
distinction between product Security Requirements and analysis-method vocabulary.

### 2.4 Traceability and provenance
Source identity, rationale, relations, verification evidence, baseline identity and evolution.

### 2.5 Model-driven and documentation-driven analysis
Explicit models, derived representations, candidate artifacts, deterministic transformations
and human review boundaries.

### 2.6 Automation and LLM-assisted transformations
Candidate generation versus acceptance; syntax, semantic fidelity, source coverage,
grounding, execution provenance and staleness.

### 2.7 Methodological viewpoints over system knowledge
Software/component-centered, attack/scenario-centered, goal-oriented,
requirements-oriented and asset-centered viewpoints. STRIDE-AI is used as a targeted
asset-centered AI/ML methodology reference; STRIDE is discussed only where needed.

### 2.8 Background synthesis
Conceptual requirements that motivate a methodology-neutral, documentation-derived core.

## 3. State of the art and research gap

### 3.1 Comparison dimensions
Starting artifact, canonical representation, analytical focus, method-specific semantics,
output, automation, human review, traceability and change handling.

### 3.2 Requirements-first and security-requirements approaches
### 3.3 Scenario, misuse and anti-goal approaches
### 3.4 Model-driven security
### 3.5 Automated threat modeling
### 3.6 Threat-model-as-code and tool-supported approaches
### 3.7 Automated requirements engineering and LLM-derived candidate models
### 3.8 Maintenance, provenance and reproducibility
### 3.9 Cross-source comparison
Replace generalized families with source-specific evidence and explicit unknowns.
### 3.10 Research gap
Derive, rather than assert, the gap:
governed documentation -> neutral analyzable model -> multiple methodology overlays ->
common reviewed findings -> governed Security Requirements -> change-aware re-analysis.

## 4. Research method

Research design, case selection, baselines, corpus protocol, reference models, expected-result
oracles, data collection, metrics, validity threats and reproducibility.

Primary evaluation is case-based and functional. Use published reference cases or independently
prepared expected results where an explicit oracle can be justified. Precision, recall and F1 are
used only where TP/FP/FN classification is genuinely defined. Cost and ROI are not primary metrics.

## 5. Documentation-Driven Threat Analysis

Definitions, input contract, Base Analysis metamodel, documentary candidate lifecycle, provenance,
review states, methodology plugin/overlay contract, Common Finding boundary, Security Requirement
feedback path and change-impact semantics.

The common core must not contain STRIDE, STRIDE-AI or other methodology-specific classifications.

## 6. ThreatForge reference implementation

Architecture and implemented mechanisms, described only as evidence that the method can be
operationalized. Demonstrate the plugin boundary with two real methodology implementations:
STRIDE and STRIDE-AI, both consuming the same Base Analysis and returning candidates through the
same Common Finding contract.

Do not generalize from two plugins to universal methodology support.

## 7. Evaluation

Evaluate:

- documentation-to-Base-Analysis derivability against explicit reference models;
- invariance of the canonical Base Analysis across STRIDE and STRIDE-AI runs;
- preservation of method-specific semantics inside each plugin boundary;
- expected, missing and unexpected finding candidates when a defensible oracle exists;
- common Finding normalization and review outcomes;
- Finding-to-Security-Requirement provenance completeness;
- stale propagation after controlled documentation and methodology changes.

No primary economic-cost comparison is required.

## 8. Discussion

Interpretation against the literature, limits of the two-plugin demonstration, transferability,
human-review dependence, incomplete documentation, automation risks, validity of reference cases,
and future extension to additional methodologies.

## 9. Conclusions

Answer RQ1-RQ4, state demonstrated contributions and explicit non-claims, and identify future
research without presenting untested generality as established.
