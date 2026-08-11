# DDTA - Working Metamodel - Decision

**NON-CANONICAL WORKING DRAFT - REVISION 7**

Revision 7 is a **layering correction**, not a new field-model correction. It keeps the local Decision core and the two hierarchy/corpus invariants from revision 6, while relocating representation, realization, semantic-authority and authoring-review rules to `00-foundations/01-model-layering/`.

Decision-specific semantic core:

```text
Decision
|- title
|- context
|- decision
`- consequences
```

All four are semantically required and non-null in the current candidate.

Closed Decision/hierarchy semantics retained:

- `D-CLOSED-01` - one significant choice narrowing one parent MR;
- `D-CLOSED-02` - minimal semantic core above;
- `D-CLOSED-03` - Context is decision-local;
- `D-CLOSED-04` - one coherent chosen position;
- `D-CLOSED-05` - material consequences/trade-offs are represented;
- `D-CLOSED-07` - no mandatory embedded Alternatives or separate Rationale field;
- `H-CLOSED-01` - exactly one natural MR semantic owner;
- `H-CLOSED-02` - each Decision contributes a non-redundant significant choice.

Relocated from Decision-specific semantics:

- `D-CLOSED-06` -> authoring/review heuristic;
- `D-CLOSED-08` -> cross-cutting governance boundary;
- `D-CLOSED-09` -> cross-cutting semantic-authority principle;
- `R-CLOSED-01..04` -> representation/realization layers.

The relocation preserves the conclusions but prevents realization principles such as executable projections from being used as if they were semantic invariants inherited by every governed project.

The three semantic validation levels remain:

```text
1. local Decision validity
2. MR -> Decision hierarchical coherence
3. Decision-corpus coherence
```

Large-corpus similarity/search remains tooling that can surface review candidates; it does not decide parentage or semantic duplication.

See `../../00-foundations/01-model-layering/DDTA_MODEL_LAYERING_WORKING.pdf` for the cross-cutting layering and semantic-authority contract.
