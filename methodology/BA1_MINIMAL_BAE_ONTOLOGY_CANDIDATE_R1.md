# DDTA minimal BAE ontology candidate - R1

**Status:** CANDIDATE / NOT ACCEPTED / BA1 OPEN

**Derived by:** BA1-T1

**Repository baseline reviewed:** `83af68cb1a02a6b1e76f591d4c1519f9496be3b3`

## Candidate ontology

BA1-T1 proposes two first-class analytical identity families and no domain-specific subtype split yet.

### `BAReferent`

An independently identifiable unit of methodology-neutral shared project meaning that must be recognizable across one or more analytical propositions, projections or governed baselines.

A `BAReferent` may carry a semantic kind/role such as structural participant, external participant, capability, information/resource, behavior/event, store, contract or other project meaning. BA1-T1 does not promote those kinds to separate metaclasses.

### `BAProposition`

An independently identifiable methodology-neutral analytical assertion about shared project meaning. It references one or more `BAReferent` identities, may itself be targeted by other propositions, and has enough identity to support origin/provenance, review, diagnosis, reuse and change disposition.

Its content may express behavior, relation, dependency, responsibility, correlation, state/condition, applicability, constraint, lifecycle or failure semantics. BA2 will define the minimal relation/action vocabulary; BA3 will define provenance and diagnostic materialization.

## Minimal picture

```text
BAReferent *
     ^
     | referenced by
     |
BAProposition *

BAProposition may also be the target of another BAProposition.
```

`BAE` is an umbrella term, not an additional required metaclass in this candidate.

## Explicitly not accepted by R1

No first-class split is accepted yet for:

- Participant / Actor;
- Component / Capability;
- Asset;
- Information / Resource;
- Behavior / Event / Transition;
- Interface / Connection / Channel;
- Store / Persistence;
- Contract;
- Boundary;
- State / Mode / Context;
- Dependency / Allocation;
- Property / Constraint;
- DataFlow / Interaction.

Document types (`MacroRequirement`, `Decision`, `FunctionalRequirement`, `SpecializedRequirement`, `SecurityRequirement`) remain source-layer governed concepts and are not copied into Base Analysis as BAE types.

Diagnostic/unresolved, provenance/source locators and views are required responsibilities but are deferred to BA3/BA4 material contracts rather than proposed as domain BAE metaclasses.

## Falsification rule

This candidate fails if a concrete governed corpus or method-neutral consumer requires a deferred semantic kind to have independent subtype-specific identity/invariants that cannot be represented honestly with `BAReferent + BAProposition` without reconstructing meaning outside the shared core.

## Next step

`BA1-T2 - split-or-collapse pressure test of the two-family candidate`.

BA1 remains open. BA2 remains not started.
