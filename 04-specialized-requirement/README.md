# Specialized Requirement - S1 research checkpoint

This directory preserves the S1 semantic study that closes the general `SpecializedRequirement` junction before the thesis specializes it as `SecurityRequirement`.

## Scope

The checkpoint is method-neutral. It formalizes the relation:

```text
MacroRequirement -> Decision -> FunctionalRequirement -> SpecializedRequirement
```

and deliberately does **not** formalize `SecurityRequirement`, Base Analysis/BAE, Finding, STRIDE/STRIDE-AI, controls, or ThreatForge-specific semantics.

## Contents

### `01-metamodel/`

- `DDTA_SPECIALIZED_REQUIREMENT_S1_R2.*` - formal S1 semantics, invariants, negative controls, cardinality and reopen rule.

### `02-authoring-guidance/`

- `DDTA_AUTHORING_RULES_THROUGH_SR_R3.*` - authoring contract through SpecializedRequirement, including the Macro Project Map review and the isolated-MR heuristic.

### `03-example-facial-access/`

- `DDTA_FACIAL_ACCESS_CAMERA_S1_STUDY_CORPUS_R2.*` - facial-access study corpus, camera/recognition mutations and regression of the historical isolated `MR-0004`.

## Key S1 closure

A `SpecializedRequirement` is a governed normative specialization of exactly one `FunctionalRequirement`. It strengthens the conditions under which the parent FR is satisfied, applies together with rather than instead of the functional obligation, and may require subordinate positive behavior without becoming an autonomous capability.

The conceptual core remains intentionally small:

```text
SpecializedRequirement [abstract]
    parentFunctionalRequirement : FunctionalRequirement [1]
    normativeObligation         : [1]
```

## Isolated-MR review

The S1 regression of the facial-access example introduced a candidate authoring heuristic:

> An isolated MacroRequirement is not invalid, but it requires explicit semantic review. If it mainly collects cross-cutting properties or constraints over behaviors owned by other branches, it may be a concern bucket classified too high in the hierarchy.

A graph/tool may therefore flag `degree(MR) = 0` as `REVIEW REQUIRED`, never as an automatic semantic error.

The facial-access regression removes historical `MR-0004` from the revised study corpus and redistributes its knowledge by semantics:

- biometric purpose limitation -> candidate local SpecializedRequirements on the FRs that actually process biometric material;
- contestability/review -> autonomous operational responsibility under the access-control branch when it requires an actual review process.

## Suggested INDEX.md entry

Add a root section similar to:

```markdown
### `04-specialized-requirement/`

- `04-specialized-requirement/01-metamodel/` - method-neutral S1 semantics for SpecializedRequirement.
- `04-specialized-requirement/02-authoring-guidance/` - authoring rules through SpecializedRequirement, including isolated-MR review.
- `04-specialized-requirement/03-example-facial-access/` - facial-access S1 study corpus and controlled regressions/mutations.
```

Do not treat this README or the study corpus as a SecurityRequirement metamodel. Security specialization is the next research step.
