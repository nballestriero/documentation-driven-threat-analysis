# DDTA metamodel working package

**Non-canonical research workspace.**

This package is intentionally separated from canonical thesis/repository material. It contains the current Macro Requirement study only.

## Contents

- `01-mr/01-metamodel/` - general MR metamodel, independent from ThreatForge.
- `01-mr/02-threatforge-comparison/` - ThreatForge as a case study: current MR versus successive rewrites.
- `01-mr/03-example-facial-access/` - independent example project using facial recognition, biometric data and ML.
- `01-mr/04-teachability-maps/` - non-canonical Macro Project Map study, saved facial-access/ThreatForge diagrams and DFD-renderer compatibility notes.
- `guidance/` - draft authoring guidance/anti-pattern notes for future LLM and programmer guidance.

The ThreatForge case study and the facial-access example are evidence and test material. They are not part of the general metamodel.

## Current MR boundary lesson

The ThreatForge MR-0003/MR-0005 case is retained as a worked example of why MR merge/split decisions must be checked against descendant Decision families and not inferred from rewritten prose alone. The comparison preserves original, first rewrite and second rewrite for both MRs.

## Current temporal-stability lesson

Macro Requirements describe stable project concerns, not temporary progress of solution design. Statements such as `not yet decided` or `currently evaluating` belong to working/Decision state when they would become obsolete merely because a lower-level choice is taken.

## Observation deferred to the analysis metamodel

The facial-access example shows that one project can contain concerns that later benefit from different analysis paradigms. The MR hierarchy must remain organized by project concerns rather than by methodology. The future analysis model should test method selection over explicit scopes/subjects and convergence of heterogeneous analysis feedback into one governed documentation lifecycle.

## Intent/Objective closure

The separate `Objective` concept is removed from the MR working model. `Intent` now owns macro purpose, value and desired outcome. The decision was tested on four facial-access MRs and on the five original/candidate ThreatForge MRs.

## Teachability lesson

Macro Requirements should not directly produce DFD/architecture semantics, but the MR set should be teachable as a simple Macro Project Map. The saved diagrams distinguish canonical MR relations from non-canonical didactic interpretation and provide accessible textual companions.

The current ThreatForge DFD implementation was inspected as a rendering reference: future MR maps may share its deterministic HTML/SVG visual/accessibility method while keeping a separate semantic projection contract.
