# Dependency Graph Projection Hypothesis R1

## Status

`CANDIDATE PROJECTION MECHANISM / NON-NORMATIVE / NOT ADMITTED`

This artifact records a downstream projection hypothesis discovered during OP-08. It does not modify BA0–BA5 and does not authorize new project truth.

## Motivation

A dependency graph can support:

```text
impact analysis
dependency traversal
prerequisite ordering
change propagation
critical-node analysis
cycle detection
```

The BA should not duplicate semantic propositions solely to make this graph convenient.

## Edge classes

```text
ASSERTED
    edge comes from an accepted dependOn BA proposition

DERIVED
    edge is reproducibly implied by a more-specific accepted BA proposition
```

Potential derived-edge sources must be validated construct by construct, including `produce.input`, `consumeService` if OP-09 confirms the implication, and future `consumeData` semantics if PR-11 admits them.

## Provenance

Every projected edge should retain:

```text
edgeKind: ASSERTED | DERIVED
source: originating BA proposition(s)
derivationRule: required for DERIVED edges
```

A graph must not present derived semantics as directly source-asserted.

## Transitive reachability

Given `A dependsOn B` and `B dependsOn C`, the graph may compute that A reaches C without creating a third asserted BA proposition. Distinguish direct asserted edge, direct derived edge and transitive reachability.

## Cycle detection

A graph may identify `A -> B -> C -> A` as a dependency cycle and use this for documentation QA or architecture review.

It must not automatically label the cycle a runtime deadlock.

## Deadlock boundary

A deadlock conclusion normally requires additional governed semantics such as wait-for relation, resource holding, blocking behavior, concurrency and release conditions. OP-08 alone does not provide these semantics.

## Conditional / branch-scoped edges

A projected dependency must preserve applicability scope. A B4-integrated dependency must not be widened to all DermaTriage workflows because the governed direct workflow explicitly avoids the B4 dependency.

## Future validation

Revisit after:

```text
OP-09 consumeService
OP-10 realize
PR-02 pipeline composition/order
PR-10 trigger semantics
PR-11 data/evidence consumption
```

and ultimately during integrated method/projection review. General Discovery Pack execution remains deferred to the third complete analysis cycle.
