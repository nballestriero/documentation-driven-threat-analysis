# DDTA metamodel working package

**Non-canonical research workspace.**

This package contains the current document-semantics studies for Macro Requirement and Decision. ThreatForge remains a case study/tool-support subject rather than the semantic owner of the general DDTA metamodel.

## Contents

### `00-foundations/`

- `00-foundations/01-model-layering/` - cross-cutting separation between conceptual metamodel, canonical representation contract, model-realization principles and tool support/conformance; includes the executable-projections diagram.

### `01-mr/`

- `01-mr/01-metamodel/` - general MR metamodel, independent from ThreatForge.
- `01-mr/02-threatforge-comparison/` - ThreatForge as a case study: current MR versus successive rewrites.
- `01-mr/03-example-facial-access/` - independent example project using facial recognition, biometric data and ML.
- `01-mr/04-teachability-maps/` - non-canonical Macro Project Map study, saved facial-access/ThreatForge diagrams and DFD-renderer compatibility notes.

### `02-decision/`

- `02-decision/01-metamodel/` - Decision-specific conceptual semantics plus MR->Decision hierarchy/corpus invariants. Cross-cutting representation/realization rules now live under `00-foundations/`.
- `02-decision/02-threatforge-comparison/` - 16 historical ThreatForge ADR bodies from MR-0001/MR-0002 versus their revised candidate Decisions; MR-0003/MR-0004/MR-0005 remain untouched holdouts.
- `02-decision/03-plan/` - frozen experimental work plan before authoring the independent facial-access Decision corpus.
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

A closed construction rule may be reopened only by a concrete counterexample from an independent example or sequential holdout, followed by regression over prior evidence. Revision 7 keeps this local field core unchanged and removes non-Decision layering rules from the Decision-specific closed set.

## Decision-set coherence after early facial-access D2

Early Phase D2 review of the frozen facial-access corpus exposed a limitation above single-document validity: individually plausible Decisions can still be redundant across different Macro Requirements or have ambiguous semantic ownership. Revision 6 therefore closes two additional hierarchy/corpus invariants:

1. **Unique semantic ownership** - each Decision has exactly one Macro Requirement that naturally owns the unresolved problem; if the same Decision can move unchanged to another MR, review the Decision or MR decomposition instead of duplicating ownership.
2. **Non-redundant Decision contribution** - each Decision contributes a significant choice not already governed by another applicable Decision and not completely derivable from its parent plus existing Decisions.

The Decision model now distinguishes three review levels:

```text
local Decision validity
    -> MR -> Decision hierarchical coherence
    -> Decision-corpus coherence
```

These invariants are part of the metamodel; similarity/search algorithms are not.

## Model layering and semantic authority

Revision 7 separates four concerns that had accumulated inside the Decision study:

```text
L1 conceptual metamodel
L2 canonical representation contract
L3 model realization principles
L4 tool support / conformance view
```

`H-CLOSED-01` and `H-CLOSED-02` remain conceptual metamodel invariants. `D-CLOSED-06`, `D-CLOSED-08`, `D-CLOSED-09` and `R-CLOSED-01..04` retain their conclusions but now live in the cross-cutting layering document at `00-foundations/01-model-layering/DDTA_MODEL_LAYERING_WORKING.*`.

In particular, `R-CLOSED-04` (executable projections from one governed model) is a **model-realization principle**, not a semantic invariant that every governed DDTA project inherits. It therefore cannot by itself make a ThreatForge product ADR redundant.

Semantic nullability and its material encoding are also separated: whether a value may be absent is semantic; how an allowed absence is serialized is representational.

The model-to-executable-projections diagram now lives under `00-foundations/01-model-layering/diagrams/`.

## Scalable tooling and controlled vocabulary boundary

Similarity/search algorithms remain tooling assistance for reviewing semantic invariants at scale. They may surface likely duplicate or cross-parent candidates but do not establish semantic equivalence or parent ownership.

A controlled vocabulary, if adopted, is governed knowledge independent from ThreatForge. Its universal/optional/profile-specific status remains open; stemming, normalization and ranking remain tooling unless explicitly promoted into governed semantics.

## ThreatForge support/conformance direction

ThreatForge should eventually make explicit which DDTA contracts it supports, validates, projects or assists with rather than re-declaring those semantics inside tool ADRs. The exact support/coverage relation model is deferred until Requirement and implementation-trace semantics are revisited.


## ThreatForge Decision regression after Revision 7

`02-decision/02-threatforge-comparison/THREATFORGE_DECISION_REGRESSION_REV7.*` records the complete regression of the sixteen construction candidates after correcting the model-layering error.

Key outcomes:

- L3 realization principles cannot by themselves make a ThreatForge Decision redundant;
- ownership-correct wording must still contain an autonomous choice;
- parentage must be re-evaluated after ownership/narrowing changes;
- support of one concrete model extension can be L4 conformance/coverage rather than a standalone Decision.

The regression specifically reopens the earlier negative reading of executable-contract ADR-0007 and retains `H-CLOSED-02` as the reason to challenge Security-support ADR-0009.


## Corrected ThreatForge Decision candidates after Revision 7

`02-decision/02-threatforge-comparison/THREATFORGE_ADR_CANDIDATES_REV7.*` rewrites the sixteen historical construction slots against the Revision 7 layering and corpus invariants.

The rewrite deliberately does not preserve a one-to-one ADR count:

- Diátaxis, controlled vocabulary and governed-reference grammar are relocated to DDTA method/L2 representation ownership candidates;
- implementation trace is rewritten as a ThreatForge product choice and proposed for MR-0002;
- handoff remains a meaningful ThreatForge project-operation Decision with parent unresolved;
- Security Requirement support is removed as a standalone Decision candidate and represented as an L4 support/conformance case;
- the remaining ThreatForge candidates are rewritten/cleaned so that each document states a tool/project choice rather than merely restating the DDTA contract it supports.

Study annotations for semantic owner, proposed parent and supported DDTA contract are not new canonical Decision fields.

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

Phase D1 is authored and frozen in `02-decision/05-example-facial-access/FACIAL_ACCESS_DECISION_DEMO.*`. The frozen D1 corpus remains unchanged. Revision 6 added hierarchy/corpus invariants; the subsequent independent-example review and ThreatForge construction regression exposed a layering error in the study itself. Revision 7 checkpoints the corrected separation. The ThreatForge construction regression is now finalized in `THREATFORGE_DECISION_REGRESSION_REV7.*`; no historical ThreatForge ADR has been migrated. The corrected candidate corpus is now written in `THREATFORGE_ADR_CANDIDATES_REV7.*`. The next step is to validate that rewritten corpus itself before touching the sequential ThreatForge MR-0003/MR-0004/MR-0005 holdouts.

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
