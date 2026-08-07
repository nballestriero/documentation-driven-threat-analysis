# Research questions

The research scope is intentionally narrow. DDTA is evaluated as a documentation-primary,
methodology-neutral analysis core with pluggable threat-analysis overlays and a governed path
from accepted findings to security requirements. Cost, ROI and broad industrial-effort studies
are outside the primary thesis evaluation.

## RQ1 — Documentation to Base Analysis

To what extent can governed software documentation be transformed, before implementation,
into a methodology-neutral Base Analysis while preserving explicit provenance and review of
derived elements?

## RQ2 — Multi-method core

Can the same Base Analysis support distinct threat-analysis methodologies through isolated
plugins, preserving each method's specific semantics while producing comparable results
through a common finding model?

The thesis evaluates this question through the implementation and evaluation of two methodology
plugins: STRIDE and STRIDE-AI. They are demonstrators of the plugin and overlay boundary, not
evidence that every existing threat-analysis methodology is automatically supported.

## RQ3 — Findings to Security Requirements

Can accepted results produced by distinct methodologies be incorporated uniformly into governed
project documentation as Security Requirements while preserving provenance to the protected
Functional Requirement, Base Analysis, analysis record and originating methodology?

## RQ4 — Change and re-analysis

Can provenance relations and governed baselines identify which Base Analysis elements, analyses,
findings and Security Requirements require re-evaluation after relevant documentation or
methodology-configuration changes?

## Deliberate exclusions

The thesis does not make primary research questions about:

- economic cost, ROI or organizational adoption;
- universal superiority over manual threat modeling;
- support for every threat-modeling methodology;
- autonomous acceptance of generated findings or Security Requirements;
- legal or compliance analysis;
- universal LLM reproducibility.

These topics may appear as limitations or future work where supported by the literature.
