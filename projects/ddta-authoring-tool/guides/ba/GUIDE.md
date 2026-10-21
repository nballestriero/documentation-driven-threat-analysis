# Base Analysis — General Guide

> **PLACEHOLDER — TO BE AUTHORED AND REVIEWED.** This freeform Markdown guide
> is intended for authors and LLMs. It does not use the `BAOperatorGuide`
> schema and it does not contain executable BA operator rules.

## What is Base Analysis

*To be drafted and reviewed using the R7 rebuild and the explicit
methodological decisions made during this authoring process.*

## Semantic authority and the BA/documentation boundary

*To be drafted and reviewed.*

## BAReferent and BAProposition

*To be drafted and reviewed. Do not duplicate operator signatures here.*
The shared contract is `contracts/ba-proposition.yaml`. `polarity` is
required; `temporalScope` is optional and its value semantics are still under
review. Neither field is an operator role. The R7 authoring model discusses
`temporalScope` as a proposition-level scoped modifier.

## Identity, granularity, and continuity

*To be drafted and reviewed.*

## Construction and review method

*To be drafted and reviewed.*

## Operator catalog

Operator sheets reside in [`operators/`](operators/) and are executable
only when their `reviewStatus` is `reviewed`. This does not require
`methodStatus: current`: `transfer` (C4 R3) and `produce` (C5 R2) are
approved for **structural validation** while their broader methodological
status remains `candidate`.
Historical drafts are preserved in [`reviews/`](reviews/) for traceability,
not authority. Methodological recognition and executable rule coverage are
different states.

## Historical references

- `methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex` — working review source; no automatic promotion.

This general guide must not be checked against `BAOperatorGuide` fields. Generic
Markdown checks may be introduced separately.
