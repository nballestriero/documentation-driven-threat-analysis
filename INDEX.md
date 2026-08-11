# DDTA metamodel working package

**Non-canonical research workspace.**

This package contains the current document-semantics studies for Macro Requirement and Decision. ThreatForge remains a case study/tool-support subject rather than the semantic owner of the general DDTA metamodel.

## Contents

### `01-mr/`

- `01-mr/01-metamodel/` - general MR metamodel, independent from ThreatForge.
- `01-mr/02-threatforge-comparison/` - ThreatForge as a case study: current MR versus successive rewrites.
- `01-mr/03-example-facial-access/` - independent example project using facial recognition, biometric data and ML.
- `01-mr/04-teachability-maps/` - non-canonical Macro Project Map study, saved facial-access/ThreatForge diagrams and DFD-renderer compatibility notes.

### `02-decision/`

- `02-decision/01-metamodel/` - Decision construction-candidate semantics and closed cross-cutting representation decisions.
- `02-decision/02-threatforge-comparison/` - 16 historical ThreatForge ADR bodies from MR-0001/MR-0002 versus their revised candidate Decisions; MR-0003/MR-0004/MR-0005 remain untouched holdouts.
- `02-decision/03-plan/` - frozen experimental work plan before authoring the independent facial-access Decision corpus.
- `02-decision/04-diagrams/` - reusable model-to-executable-projections diagram and sources.
- `02-decision/05-example-facial-access/` - Phase D1 independent facial-access Decision authoring corpus; intentionally frozen before D2 analysis.

### `guidance/`

- draft authoring guidance/anti-pattern notes currently focused on MR; Decision guidance remains deferred until the Decision holdout sequence is complete.

The ThreatForge case study and the facial-access example are evidence/test material. They are not themselves the general metamodel.

## Current MR boundary lesson

The ThreatForge MR-0003/MR-0005 case is retained as a worked example of why MR merge/split decisions must be checked against descendant Decision families and not inferred from rewritten prose alone. The comparison preserves original, first rewrite and second rewrite for both MRs.

## Current MR temporal-stability lesson

Macro Requirements describe stable project concerns, not temporary progress of solution design. Statements such as `not yet decided` or `currently evaluating` belong to working/Decision state when they would become obsolete merely because a lower-level choice is taken.

## MR analysis boundary

Macro Requirements provide analysis-enabling project context but do not directly instantiate canonical analytical elements, topology, flows, trust boundaries or method-specific interpretation. Any analytical representation derived from MR prose requires a later governed interpretation/review step.

## Intent/Objective closure

The separate `Objective` concept is removed from the MR working model. `Intent` owns macro purpose, value and desired outcome. The decision was tested on four facial-access MRs and on the five original/candidate ThreatForge MRs.

## Teachability lesson

Macro Requirements should not directly produce DFD/architecture semantics, but the MR set should be teachable as a simple Macro Project Map. Saved diagrams distinguish canonical MR relations from explicitly non-canonical didactic interpretation and provide accessible textual companions.

The current ThreatForge DFD implementation was inspected as a rendering reference: future MR maps may share deterministic HTML/SVG visual/accessibility utilities while keeping a separate semantic projection contract.

## Decision construction-candidate closure

The Decision-specific semantic core is currently closed for the construction candidate:

```text
Decision
|- title
|- context
|- decision
`- consequences
```

The four fields are semantically required and non-null. Context is decision-local; one Decision expresses one coherent chosen position; Consequences records material effects/trade-offs. `Non-goals`, mandatory embedded Alternatives and a separate mandatory Rationale field are not part of the current core. Lifecycle/status remains a later cross-cutting governance concern.

A closed construction rule may be reopened only by a concrete counterexample from an independent example or sequential holdout, followed by regression over prior evidence.

## Semantic-owner separation

Historical ThreatForge ADRs frequently mix choices about the DDTA method/metamodel, governed-project instances, ThreatForge tool support and ThreatForge project operations because model and tool evolved together.

Current rule:

```text
DDTA method / metamodel
    owns portable general semantics

Governed project
    owns concrete governed instances and project-specific choices

ThreatForge tool
    supports authoring/resolution/validation/projection/workflow
    without becoming owner of general semantics

ThreatForge project operations
    govern development of ThreatForge itself
    without becoming universal DDTA rules
```

Review test: if ThreatForge were replaced by another tool, a statement that should remain true is probably owned by DDTA/model/method rather than by a ThreatForge product ADR.

## Cross-cutting representation decisions

The working package now also closes the following representation properties for the construction candidate:

1. **Complete canonical shape** - every field declared by a governed document model is structurally present in every canonical instance representation.
2. **Explicit nullability / empty values** - omission is not equivalent to `null`; nullability and canonical empty values are field-specific.
3. **Semantic / representation separation** - meaning, types, cardinalities, nullability and invariants are semantic; order, headings, containers, mirrors and serialization mapping belong to governed representation profiles.
4. **Executable projections from one model** - validators, editor contracts, authoring/LLM assistance and machine-readable schemas should be deterministic projections of one governed canonical document model rather than parallel semantic authorities.

See `02-decision/04-diagrams/MODEL_TO_EXECUTABLE_PROJECTIONS.svg` for the explanatory structure.

## Cross-document problems deliberately left open

The construction corpus demonstrates that persistent choices can be forgotten or lose explicit downstream coverage even while artifacts survive. The working constraints retained for later combined MR -> Decision -> Requirement modeling are:

- no orphan normative decision;
- single-source governed knowledge;
- effective governed context;
- Decision survivability and recoverability;
- coverage awareness for pervasive/cross-cutting obligations;
- no inheritance-by-copy.

These are not new Decision fields. Their minimal relation/propagation mechanism remains open until Requirement semantics is studied.

## Current Decision validation state

Phase D1 is now authored and frozen in `02-decision/05-example-facial-access/FACIAL_ACCESS_DECISION_DEMO.*`. The eight Decisions have **not yet been analyzed** against the construction candidate. The next empirical step is Phase D2; the D1 corpus must remain unchanged while it is evaluated so that any counterexample remains attributable to the independent authoring evidence.

## Next experimental sequence

The sequence is frozen in `02-decision/03-plan/DECISION_PHASE_WORK_PLAN.md`:

```text
Decision construction candidate checkpoint
    -> independent facial-access Decision authoring
    -> facial-access Decision analysis / possible regression
    -> candidate closure after independent example
    -> ThreatForge MR-0003 holdout
    -> ThreatForge MR-0004 holdout
    -> ThreatForge MR-0005 holdout
    -> Decision-phase synthesis
    -> Requirement semantic study
```

The holdouts must remain sequential and uncontaminated. Any model correction must be attributable to concrete evidence and followed by regression on all prior cases.
