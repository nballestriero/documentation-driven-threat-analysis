# DEC-C6-01 — contextual use of reusable processes (experimental R1)

**Status:** `EXPERIMENTAL_NON_CANONICAL`. No original documentation, Core axioms, or
previous C6 composition pilot is overwritten by this experiment.

## Semantics tested

- `ddta:Process` is a reusable process definition. The process has the same IRI
  regardless of which workflow refers to it.
- `proc:ProcessStep` is a *planned placement* of that process within a workflow.
  It is NOT an execution, a function, or a subclass of `ddta:Process`.
- `ddta:hasPart` from workflow to its placement identifies membership/structure.
- `proc:referencesProcess` identifies the reusable process designated for that placement.
- Neither relation implies actual invocation, execution, success, prerequisites,
  or ordering. An ordered SPARQL result is not a process execution order.

## Sources vs hypothetical example

`DEC-C6-01-workflow-steps.ttl` encodes the six process definitions identified in
DEC-C6-01 (source page 48) as six separate *workflow-specific placements*. In
contrast, the earlier composition pilot placed the process IRIs directly under
`ddta:hasPart`. Both are **alternative candidate projections** of the same
workflow and should not be indiscriminately merged until that choice is approved.

`hypothetical-refresh.ttl` describes a **hypothetical**, second workflow that
references both the model-acquisition and repository-acquisition processes. It
is a reuse test, not a documented DermaTriage requirement or implemented
maintenance workflow.

We want eventually to express two *possible* ordered configurations:

| Context | Intended order (not RDF-encoded in this increment) |
|---|---|
| Installation C6 | Repository acquisition, then model acquisition (with other processes between) |
| Hypothetical model refresh | Model acquisition, then repository acquisition |

The tests prove that the **same process identities** can be referenced by
*different step identities in separate workflows*, with no global precedence.
They do NOT yet assert, query, or validate either order. That is the next,
separately reviewed semantic increment.

## Tests

From `projects/ddta-semantic-workspace`:

```powershell
python -m unittest discover -s tests -p test_process_ontology.py -v
python -m unittest discover -s tests -p test_c6_process_context.py -v
```

Example SPARQL: `step-placements.rq` selects eight workflow-step-process rows,
without asserting any sequence. Do not infer `ProcessStep -> ddta:Process`
subclassing, or an implementation/execution, from the example.

## Reference designs (not imported)

- P-Plan: distinction between plan and individual step, and between plan and
  execution. https://purl.org/net/p-plan
- OWL-S: composite process/control-flow ideas; no OWL-S import.
- DDTA Core (`ontology/core.ttl`) remains the source of truth for `Process`,
  `Function`, `hasPart`, and `realizesFunction`.
