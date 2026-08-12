# DDTA - Working Metamodel - Decision

**DOCUMENTATION-LAYER CLOSURE CANDIDATE - REVISION 8**

Revision 8 preserves the Revision 7 local field core and layering separation, but refines the definition of Decision after the Functional Requirement experiments. The thesis baseline intentionally keeps a regular `MR -> Decision -> FR` authoring layer.

## 1. Definition

A Decision is a governed **significant commitment** that narrows exactly one parent Macro Requirement by fixing a meaningful position, responsibility boundary, policy, convention, strategy, technology/architecture choice or other project commitment whose consequences matter downstream.

Normally the commitment selects among plausible alternatives. In the rare case where no materially distinct alternative is practical or admissible, DDTA still permits an explicit **necessity/default Decision** so that the documentation layer remains regular and the commitment is not hidden.

### Fundamental question

> **Which significant commitment narrows this Macro Requirement, why must the project take that position, and which consequences do we accept?**

For an ordinary choice, Context should expose the unresolved alternatives/tension. For a necessity/default Decision, Context must explain why alternatives are absent, non-material or excluded by a governed constraint.

## 2. Semantic core

```text
Decision
|- title
|- context
|- decision
`- consequences
```

All four are semantically required and non-null.

Topology:

```text
MacroRequirement 1 ---- * Decision 1 ---- * FunctionalRequirement
```

- every Decision has exactly one natural MR semantic owner;
- every Functional Requirement has exactly one parent Decision;
- an authored Decision may temporarily have zero FR children;
- Decision is never a child of Functional Requirement.

## 3. Closed Decision semantics

- `D8-CLOSED-01` - one significant commitment narrowing one parent MR;
- `D8-CLOSED-02` - minimal semantic core is `title/context/decision/consequences`;
- `D8-CLOSED-03` - Context is Decision-local;
- `D8-CLOSED-04` - one coherent chosen/committed position;
- `D8-CLOSED-05` - material consequences/trade-offs/downstream effects are represented;
- `D8-CLOSED-06` - no mandatory embedded Alternatives or separate Rationale field;
- `D8-CLOSED-07` - exactly one natural MR semantic owner;
- `D8-CLOSED-08` - each Decision contributes non-redundant governed knowledge;
- `D8-CLOSED-09` - FRs descend from Decision; a Decision may own `0..*` FRs;
- `D8-CLOSED-10` - no Decision is hierarchically below an FR.

## 4. Genuine-choice Decision versus necessity/default Decision

The normal case remains a genuine project choice.

Use a **necessity/default Decision** only when a regular Decision layer is required but the author cannot identify a materially distinct admissible alternative after reasonable domain review, or when external constraints effectively reduce the admissible solution set to one position.

A necessity/default Decision is valid only if:

1. **Context names the reason** - e.g. regulatory constraint, contractual boundary, physical impossibility, fixed upstream dependency, or explicitly reviewed absence of material alternatives;
2. **Decision states an actual commitment** - not a tautology such as "the system will do what the MR says";
3. **Consequences remain material** - the commitment still creates downstream responsibilities/FRs or constrains later design;
4. **Reopen trigger is visible** - if the constraining condition changes or a material alternative appears, the Decision is reviewable/supersedable;
5. **No ignorance laundering** - "we did not think about alternatives" is insufficient evidence for this mode.

The metamodel does not require a `decision_kind` field at L1. The distinction can be expressed in Context/Decision/Consequences unless later representation evidence justifies a dedicated field.

## 5. Decision split/merge tests

Split commitments that can change independently and have distinct consequences/trade-offs. Do not merge choices merely because the same FR is affected by both.

Questions:

- What responsibility/solution space is still unresolved inside the MR?
- What changes if a different position is adopted?
- Does the Decision establish who owns the behavior (internal system vs external service/provider)?
- Does it choose a strategy/policy whose operational consequences appear in FRs?
- Could part of this Decision change without changing the rest? If yes, consider splitting.
- If the Decision is removed, is non-derivable governed commitment knowledge lost?

## 6. Historical and cross-cutting boundaries

Lifecycle/status, semantic authority, representation, executable projections and tool support remain cross-cutting L1/L2/L3/L4 concerns rather than Decision-specific fields.

Large-corpus similarity/search may surface review candidates but does not decide ownership, equivalence or parentage.

See `../../00-foundations/01-model-layering/DDTA_MODEL_LAYERING_WORKING.*` for the layering contract.
