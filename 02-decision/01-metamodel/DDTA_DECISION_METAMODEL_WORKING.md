# DDTA - Working Metamodel - Decision

**NON CANONICAL WORKING DRAFT - REVISION 5**

Revision 5 retains the closed Decision semantics from revision 4 and adds cross-cutting representation decisions:

- every field declared by a governed document model is structurally present in every canonical instance representation;
- nullability is explicit and field-specific; omission is not equivalent to `null`;
- semantic meaning/type/cardinality/nullability/invariants are separated from physical order/headings/containers/mappings;
- executable validators, editor contracts, authoring/LLM guidance and machine schemas are deterministic projections of one governed canonical document model rather than parallel semantic authorities.

![Model to executable projections](../04-diagrams/MODEL_TO_EXECUTABLE_PROJECTIONS.svg)

The full revision-5 working text is typeset in `DDTA_DECISION_METAMODEL_WORKING.pdf` and its LaTeX source.
