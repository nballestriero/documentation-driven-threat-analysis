# DEC-C6-01 — first-class control-flow transitions (pilot R1)

**Status:** `EXPERIMENTAL_NON_CANONICAL` — no change to historical/governed DermaTriage documentation. The structural source for this exercise is DEC-C6-01 p.48 in the parallel case study; OR4 Training Environment Configuration p.3 documents its operational counterparts.

## The decision being tested

A workflow is represented by **the existing** `ddta:Process`. In the prior context pilot, it contains six placements (`proc:ProcessStep`) and each placement references one reusable `ddta:Process` by `proc:referencesProcess`.

This increment adds **directed first-class control-flow transitions**. For the documented six-step linear flow, the workflow contains five transitions, each with `proc:fromNode` and `proc:toNode`. The transition is an identified object, so later conditions, events, forks and joins can be represented without converting process definitions themselves into ordered activities.

Minimal example:

```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix proc: <https://w3id.org/ddta/process#> .
@prefix derma: <https://example.org/ddta/dermatriage#> .

derma:EnvironmentSetupProcedure ddta:hasPart derma:RepositoryToDependencies .
derma:RepositoryToDependencies a proc:ControlFlowTransition ;
    proc:fromNode derma:SetupRepositoryStep ;
    proc:toNode derma:SetupDependenciesStep .
```

In the current ontology, `proc:ProcessStep rdfs:subClassOf proc:FlowNode`. `ControlFlowTransition` itself is **not** a `FlowNode`. The `FlowNode` generalization permits future gateway/synchronization nodes. It does not define gateway semantics today.

## Data sources: load them together

- Prior contextual placement: `experiments/c6-process-context/DEC-C6-01-workflow-steps.ttl` (unchanged).
- New planned flow: `experiments/c6-process-control-flow/DEC-C6-01-control-flow.ttl`.
- Optional, **hypothetical and not source-supported**: prior `hypothetical-refresh.ttl` plus new `hypothetical-refresh-control-flow.ttl` for a second workflow with different local ordering.

Do **not** union the older `experiments/c6-process-composition/DEC-C6-01-process-composition.ttl` into the new contextual design: it is an **alternative historical experiment** with `hasPart` directly to process definitions, not to placements. It is deliberately left untouched for regression.

## Scope of the semantic commitments

- `ddta:Process` means a process pattern/definition; a workflow is a process that orchestrates placements. We have **not** introduced `proc:Workflow`.
- A `ProcessStep` denotes a placement; a process definition can be reused in different workflows. A step does **not** denote an execution.
- A transition denotes a **planned control-flow path**. It does not assert execution, completion, success, a data transfer, a runtime dependency, or that a particular condition was satisfied.
- Order is captured locally by the transition graph. It does not assert global ordering between the referenced process definitions.
- `ddta:hasPart` is structural only; it does not imply ordering by itself.
- `rdfs:domain` and `rdfs:range` generate typing consequences, **not validation errors**. Endpoint counts, common workflow membership and this pilot's linear sequence are checked explicitly in Python.
- The linear validator **does not define the general ontology**: loops, branches and concurrency can be added later with dedicated semantics and tests.

## Queries, deterministic diagram, tests

From `projects/ddta-semantic-workspace`:

```powershell
python -m unittest discover -s tests -p test_process_ontology.py -v
python -m unittest discover -s tests -p test_c6_process_context.py -v
python -m unittest discover -s tests -p test_c6_process_composition.py -v
python -m unittest discover -s tests -p test_c6_control_flow.py -v
python .\experiments\c6-process-control-flow\render_workflow.py --check
```

`workflow-transitions.rq` selects workflow, transition, endpoints and the referenced processes. It returns five C6 edges; including the hypothetical data yields one additional edge in the separate workflow. `workflow-structure.rq` constructs a C6-only structural subgraph.

`render_workflow.py` is a **focused pilot-only renderer** that reads RDF plus `workflow-transitions.rq` and uses the separate `visualization.yaml` to produce the two stable files under `diagrams/`:

- `DEC-C6-01-control-flow.mmd`
- `DEC-C6-01-control-flow.graph.md` (VS Code / GitHub Mermaid preview)

Do not edit generated diagrams manually. To regenerate:

```powershell
python .\experiments\c6-process-control-flow\render_workflow.py
```

The existing shared `tools/rdf_mermaid/render.py` remains untouched: its current rendering rules are keyed only to the Core namespace and do not yet cover `proc:` relations. Integration is an explicit future renderer task, not an implicit change here.

## Architecture / future work

- `ddta-core` remains independent. This module reuses Core IRIs for `Process`, `Function`, `hasPart`, and `realizesFunction`; no `owl:imports` is asserted until IRI resolution/import behavior is approved.
- An optional **ontology module catalog** is planned for authoring suggestions: encountering `ddta:Process` may suggest `ddta-process`; it is guidance, not OWL reasoning or an automatic classification. No catalog schema or VS Code functionality is implemented by this pilot.
- Joint review still needed: `Process`, workflow role, `ProcessStep`, `FlowNode`, `ControlFlowTransition`, endpoint cardinality, ownership and how conditional/parallel transitions will differ from simple sequencing.
- No model-training, STRIDE, server or Hugging Face classes/properties have been introduced in Process.
- Ontology IRIs under `w3id.org/ddta` remain proposed and not yet publicly registered.
