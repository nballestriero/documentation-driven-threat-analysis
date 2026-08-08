# Research-gap map

## Source-derived observations

Threat-modeling guidance generally starts by establishing scope and a system
representation, then identifies what can go wrong, selects responses, and reviews
the work. DFDs, assets, components, entry points, and trust boundaries are common
inputs, but no single representation is mandatory.

Security requirements research provides systematic ways to derive security needs
from misuse, anti-goals, and attacker-oriented scenarios. Requirements traceability
research establishes the importance and difficulty of preserving links to origins,
rationale, implementation, and verification.

Model-driven security approaches generate or verify security artifacts from formal
or semi-formal models. Tool-supported threat modeling often treats a diagram, DSL,
or explicitly authored architecture model as its primary input.

## Working inference

The candidate DDTA gap is not “automated STRIDE.” For the current thesis it is the
definition and evaluation of a methodology-neutral portability / analysis-readiness
contract for governed project documentation, followed by construction and maintenance
of a reviewed common analysis model, methodology-specific analysis, and governed
incorporation of reviewed results.

The transformation of arbitrary or legacy project documentation into this portable form
is a separate problem and is reserved for future work.

## Claims not yet established

- Portable-by-construction governed documentation satisfying the DDTA input contract is
  sufficient to derive a useful reviewed Base Analysis model.
- The derived model is more complete or cheaper to maintain than a manually authored one.
- Change detection reliably identifies stale threat-analysis results.
- Security requirements derived through DDTA are superior to conventional practice.
- The approach generalizes beyond ThreatForge and documentation-rich repositories.

These are research questions or hypotheses, not conclusions.
