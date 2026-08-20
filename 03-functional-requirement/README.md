# Functional Requirement semantic study

**Documentation-layer closure checkpoint, with active R24 authoring refinement.**

This directory records the consolidated DDTA document-authoring baseline through Functional Requirement. Revision 2 remains the historical closure artifact; active R24 co-authoring additionally uses the unified documentation/BA guide introduced after the facial-access decision-rule pressure test.

## Current hierarchy

```text
Project problem framing  [method precondition]
        -> MacroRequirement
        -> Decision
        -> FunctionalRequirement
        -> SpecializedRequirement
```

For thesis scope, the next specialization to formalize is `SecurityRequirement`.

Every FR has exactly one Decision parent. The rare case where no material alternative exists is represented by an explicit necessity/default Decision whose Context explains why the admissible alternative space is singleton or constrained. No Decision is a child of FR.

## Current authoring guidance

Read together:

- `02-authoring-guidance/DDTA_AUTHORING_RULES_THROUGH_FR_R2.md` - historical Revision 2 documentation-layer closure contract;
- `../methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R1.md` - active R24 documentation/BA co-authoring rules, including FR testability, abstraction-level discipline and `IF / THEN / ELSE` decision-rule guidance;
- `../methodology/BA2_RELATION_ACTION_VOCABULARY_R2.md` - active R24 BA2 working revision adding FR-level `decisionRule` semantics while retaining the existing operator meanings.

R24 does not rewrite historical R2 evidence in place. The new guide and BA2 revision are explicit continuation artifacts.

## Contents

- `00-plan/FR_PHASE_ENTRY_NOTE.md` - historical phase-entry checkpoint; retained as study history.
- `01-metamodel/DDTA_FUNCTIONAL_REQUIREMENT_METAMODEL_WORKING.*` - Revision 2 FR conceptual baseline.
- `02-authoring-guidance/DDTA_AUTHORING_RULES_THROUGH_FR_R2.*` - historical thesis authoring questions/invariants through FR.
- `03-example-order-fulfillment/ORDER_FULFILLMENT_COMPLETE_AUTHORING_PROBE_R3.*` - realistic independent warehouse/order/payment/fulfillment validation corpus using the regular hierarchy.
- `04-closure/DDTA_DOCUMENT_METAMODEL_THROUGH_FR_CLOSURE_R2.*` - closure checkpoint, excluded evidence, open boundaries and reopen conditions.

## R24 decision-rule refinement

A Functional Requirement should remain readable and independently testable.

When an FR governs how a result is constructed from conditions, ordinary normative prose may use a direct form such as:

```text
IF <condition>
THEN <subject> MUST <result>
ELSE <subject> MUST <alternative result>
```

The corresponding BA detail is introduced only at the level where that behavior is governed. MR-level `produce` semantics remain coarse and are not silently specialized with lower-level branch logic.

`dependOn` remains distinct prerequisite semantics and is intentionally retained because later analyses can use dependency chains for impact propagation and indirect criticality discovery.

## Important evidence correction

Two earlier simplified order/inventory examples and the earlier facial direct-MR FR probes are **not used as closure evidence**. Deeper modeling exposed hidden responsibility/solution Decisions in those cases.

The current thesis baseline favors a constant hierarchy because responsibility-boundary Decisions materially change downstream FRs. If no genuine alternative exists, the necessity/default Decision rule keeps the layer explicit rather than silently removing it.

## Base Analysis boundary

Governed project documentation remains project authority. BA reconstructs reusable method-neutral meaning at the detail actually governed by each documentation level.

R24 specifically rejects pulling a complete result-construction rule into MR-level BA merely because the analytical model can express it.

## Tool boundary

ThreatForge may later assist with hierarchy creation, governed-reference lookup, predicate suggestions, decision-rule projection and validation. It remains tool support, not semantic authority.
