# Functional Requirement semantic study

**Documentation-layer closure checkpoint.**

This directory now records the consolidated DDTA document-authoring baseline through Functional Requirement. The initial Revision 1 topology experiment is superseded by Revision 2 after more realistic access-control and order/warehouse review.

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

## Contents

- `00-plan/FR_PHASE_ENTRY_NOTE.md` - historical phase-entry checkpoint; retained as study history.
- `01-metamodel/DDTA_FUNCTIONAL_REQUIREMENT_METAMODEL_WORKING.*` - Revision 2 FR conceptual baseline.
- `02-authoring-guidance/DDTA_AUTHORING_RULES_THROUGH_FR_R2.*` - thesis authoring questions/invariants through FR.
- `03-example-order-fulfillment/ORDER_FULFILLMENT_COMPLETE_AUTHORING_PROBE_R3.*` - realistic independent warehouse/order/payment/fulfillment validation corpus using the regular hierarchy.
- `04-closure/DDTA_DOCUMENT_METAMODEL_THROUGH_FR_CLOSURE_R2.*` - closure checkpoint, excluded evidence, open boundaries and reopen conditions.

## Important evidence correction

Two earlier simplified order/inventory examples and the earlier facial direct-MR FR probes are **not used as closure evidence**. Deeper modeling exposed hidden responsibility/solution Decisions in those cases.

The current thesis baseline favors a constant hierarchy because responsibility-boundary Decisions materially change downstream FRs. If no genuine alternative exists, the necessity/default Decision rule keeps the layer explicit rather than silently removing it.

## Base Analysis boundary

The exact BAE taxonomy, service/capability representation, SPO predicate type compatibility and cross-MR consumption target remain for the next Base Analysis phase. The documentation layer fixes what an author must say without prematurely deciding how every referenced subject/object/service is represented analytically.

## Tool boundary

ThreatForge may later assist with hierarchy creation, governed-reference lookup, predicate suggestions and validation. It remains tool support, not semantic authority.
