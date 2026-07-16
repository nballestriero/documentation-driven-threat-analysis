# Preliminary findings

## Summary

The current ThreatForge corpus naturally supports the concept of a primary
Base Analysis focus for Functional Requirements.

| Focus type | Count |
|---|---:|
| Component | 17 |
| Asset | 6 |
| Data Flow | 1 |
| Actor | 0 |
| Boundary | 0 |

## Interpretation

The absence of Actor and Boundary as primary focus is not evidence that those
elements are absent from the system. The current corpus is dominated by
governance and tooling capabilities.

Candidate boundaries remain implicit in interactions such as:

- VS Code adapter to shared core;
- API to web UI;
- tool to repository filesystem;
- unsaved editor state to persisted repository state;
- canonical source to generated projection;
- repository runner to Git.

## Governance Requirements

Governance Requirements should not be forced to declare an independent primary
focus. They normally inherit the parent Functional Requirement focus and add:

- security or governance properties;
- constraints;
- verification behavior;
- negative fixtures;
- evidence expectations;
- additional related targets.

## Research value

This registry is useful for both:

1. thesis discussion, because it documents the origin of the proposed rule;
2. longitudinal study, because future ThreatForge baselines can be compared
   against the same mapping method.

A later study can measure:

- whether the ratio of direct to composite focus changes;
- when Actors and Boundaries begin to appear;
- whether new requirements become less or more analysis-ready;
- whether explicit focus annotations improve extraction quality;
- whether requirement decomposition changes after review.
