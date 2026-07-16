# STUDY-0001 — Natural primary focus in ThreatForge Functional Requirements

## Status

In review

## Research question

Do the current ThreatForge Functional Requirements naturally identify one
primary element suitable for later Base Analysis?

## Source baseline

`TF-BL-0001`

## Corpus

- 24 Functional Requirements
- 37 Governance Requirements inspected for inheritance behavior
- 61 total Requirements

## Method

For each Functional Requirement:

1. inspect the Intent and Functional obligation sections;
2. identify the natural grammatical and semantic focus;
3. classify it as Actor, Component, Asset, Boundary or Data Flow;
4. record whether the identification is explicit, inferred or composite;
5. record the source body path;
6. avoid inventing a focus from the title alone.

Governance Requirements are evaluated separately to determine whether they
inherit the parent focus or introduce an independent domain focus.

## Preliminary result

All 24 Functional Requirements expose a recognizable primary focus:

- 17 Component
- 6 Asset
- 1 Data Flow
- 0 Actor
- 0 Boundary

Twenty are direct, three require a coherent aggregate, and one is naturally
centered on an API-to-UI data flow.

The result supports the working proposition for the current corpus, but does
not yet prove that the rule generalizes to future product-domain requirements.
