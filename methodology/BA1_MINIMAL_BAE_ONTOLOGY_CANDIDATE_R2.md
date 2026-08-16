# DDTA minimal BAE ontology candidate - R2

**Status:** STRONG CANDIDATE / NOT ACCEPTED / BA1 OPEN

**Derived by:** BA1-T1 + BA1-T2

**Repository baseline reviewed:** `f05fbb7b253392e158a1062df2614b177c13d43e`

**Supersedes for active BA1 reasoning:** `BA1_MINIMAL_BAE_ONTOLOGY_CANDIDATE_R1.md`

R1 remains immutable research history.

## Candidate ontology

The current minimal candidate contains exactly two semantic identity families:

```text
BAReferent
BAProposition
```

No domain-specific subtype split is accepted yet.

## `BAReferent`

A `BAReferent` is an independently identifiable unit of methodology-neutral shared project meaning that must be reusable across one or more analytical propositions, projections or governed baselines.

A referent may denote structural or human/external meaning, information or resources, behavior or events, contracts, storage, boundaries, states or contexts, or other project meaning.

Those semantic kinds may be important classifications, but BA1-T2 does not promote them to dedicated first-class metaclasses.

When a behavior, event, milestone, state or other meaning must be independently reused or constrained, that meaning can itself receive `BAReferent` identity.

## `BAProposition`

A `BAProposition` is an independently identifiable methodology-neutral analytical assertion about one or more `BAReferent` identities, with enough identity to support origin/provenance, diagnosis, reuse and change disposition.

A proposition may express project meaning such as:

- relation/dependency;
- behavior/action/transition semantics;
- responsibility/externality;
- correlation;
- state/condition/result semantics;
- applicability;
- constraint/property;
- lifecycle/failure/concurrency semantics.

The exact proposition structure, predicate/action vocabulary, role vocabulary and cardinalities remain BA2 questions.

## Refined family boundary

A `BAProposition` is not itself the project meaning that it describes.

If project meaning must be independently reused or qualified, that meaning receives `BAReferent` identity and propositions state its semantics.

Therefore proposition-as-project-target is **not required by the minimal candidate**.

Proposition identity still exists so that BA3 can attach origin/provenance, diagnostic state and change disposition to the assertion itself without confusing those concerns with referent identity.

## Minimal picture

```text
Base Analysis for one governed baseline

BAReferent *
    ^
    | referenced by
    |
BAProposition *

project-semantic reuse/qualification -> BAReferent
assertion provenance/diagnostic state -> BAProposition metadata in BA3
```

`BAE` remains an umbrella term, not an additional required metaclass.

## Split-or-collapse result

BA1-T2 did not force dedicated first-class roots for:

- Participant / Actor;
- Component / Capability;
- Information / Resource;
- Behavior / Event / Transition;
- Interface / Connection / Channel;
- Store / Persistence;
- Contract;
- Boundary / Externality;
- State / Mode / Context;
- Dependency / Allocation;
- Property / Constraint;
- DataFlow / Interaction.

A concrete instance of any of those meanings may still be a `BAReferent` when independent identity is needed.

The opposite collapse into one undifferentiated semantic family is rejected because referent identity and assertion identity/origin/evolution are independently required.

A single programming class, table or serialization container with a mandatory semantic discriminator would be only a representation choice and would not collapse the two semantic families.

## Document-layer boundary

Document types remain source-layer governed concepts and are not copied into Base Analysis as BAE types:

- `MacroRequirement`;
- `Decision`;
- `Requirement`;
- `FunctionalRequirement`;
- `SpecializedRequirement`;
- `SecurityRequirement`;
- `NormativeClause`.

Governed documentation remains project authority.

## Deferred rather than promoted

The following remain required later responsibilities but are not domain BAE metaclasses in this candidate:

- source locator and provenance materialization -> BA3;
- grounded/derived/diagnostic materialization -> BA3;
- identity/equivalence/lifecycle mechanics -> BA3;
- views/projections -> BA4;
- controlled vocabulary and lexical assistance -> BA5;
- Base Analysis regression/closure -> BA6;
- AnalysisRecord, Finding and method-specific outputs -> later analysis envelope.

## First-class split criterion

A new first-class BAE type/family is justified only if concrete evidence shows both:

1. independent semantic identity is required across propositions/projections/change; and
2. reusable subtype-specific invariants cannot be represented honestly as classifications, roles, values or propositions over the existing families.

Recurring usefulness, diagram convenience, implementation classes and method-specific categories are insufficient.

## Falsification rule

The two-family candidate fails if a concrete governed corpus or method-neutral consumer requires a deferred semantic kind to have independent subtype-specific identity/invariants that cannot be represented honestly with `BAReferent + BAProposition`, or if proposition identity can be removed without losing claim-level provenance/change/diagnostic semantics.

## Next step

`BA1-T3 - minimal BAE ontology closure review`.

BA1 remains open. BA2 remains not started.
