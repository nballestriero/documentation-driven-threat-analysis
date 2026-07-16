# Documentation-Driven Threat Analysis

Research companion repository for the ThreatForge project.

## Purpose

This repository preserves structured research data, methodological decisions,
project baselines, longitudinal observations and thesis evidence related to
Documentation-Driven Threat Analysis.

It is intentionally separate from the ThreatForge software repository:

- ThreatForge governs and implements the software product.
- This repository governs research observations and thesis-relevant evidence.
- Records in this repository do not create product obligations for ThreatForge.
- Claims about ThreatForge must reference a stable repository baseline.

## Initial study

The first study evaluates the proposition:

> Every Functional Requirement should identify one primary Base Analysis focus.

The initial candidate mapping covers the 24 Functional Requirements present in
ThreatForge baseline `TF-BL-0001`, commit
`b8ffdbc5c6b6ae68ff5afefe2ab44116362d15e3`.

## Repository layout

```text
baselines/
  threat-forge-baselines.registry.yml

governance/
  decisions/
    TADR-0001_separate_research_repository.md

methodology/
  primary-analysis-focus.md

studies/
  requirement-primary-focus/
    STUDY-0001.md
    requirement-primary-focus.registry.yml
    findings.md

thesis/
  README.md
```

## Status

This is an experimental research corpus. The initial records are candidates
requiring review. They are not canonical ThreatForge Base Analysis records.
