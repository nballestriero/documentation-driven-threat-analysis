# DDTA Semantic Workspace — Graph L1 / Graph L2

This is the reproducible operating procedure for the graph views used in the DermaTriage MR pilot.
The documentation levels historically called L1/L2 are **independent** of *Graph L1* and *Graph L2*.
This file records the current experimental graphical views; it does not approve additional MR/DEC/FR content.

## Source of truth

- Source: the Turtle fenced blocks in **selected** `dermatriage/mr/*.md` documents.
- Identity: resource URIs; do not duplicate entities on the basis of file names or labels.
- Query implementation: `.rq` files below, versioned in the repository.
- Renderer: `python -m tools.visualize` (single generic tool).
- Graphical style: `tools/visualization.yaml` (one shared YAML file).
- Output: generated `.mmd` and `.graph.md`; **do not edit the output as source**.

Run all commands below **from** `projects/ddta-semantic-workspace`.

## Graph L1 — General functional overview

Saved ordered SPARQL chain:

1. `views/pipeline/01-information-links.rq`: derive the synthetic functional information links.
2. `views/pipeline/02-l1-projection.rq`: select the L1 projection.

The generic CLI registers this chain as `--view l1`:

```powershell
python -m tools.visualize `
  --view l1 `
  --mr 'MR-01,MR-02,MR-03,MR-04,MR-C6,MR-C7' `
  --out "$env:TEMP\DDTA-Generic-Graph\L1_ALL"

code "$env:TEMP\DDTA-Generic-Graph\L1_ALL.graph.md"
```

## Graph L2 — Primary-function interface (current candidate)

Saved ordered SPARQL chain:

1. `views/pipeline/01-information-links.rq`: derive the same information links as L1.
2. `views/pipeline/02-l2-primary-interface.rq`: retain the functional/architectural overview; expand `hasInput`/`hasOutput` for explicitly declared `hasPrimaryFunction` functions; connect other functions only when they use/produce those *same* information URIs; hide `informationLink` edges fully represented by these explicit relations. Keep remaining synthetic links (including `informationCompositionLink`).

**Important:** as of the generic pipeline R1, there is **no** `--view l2` preset. Pass the two saved queries explicitly; do not write SPARQL at execution time.

```powershell
python -m tools.visualize `
  --mr 'MR-01,MR-02,MR-03,MR-04,MR-C6,MR-C7' `
  --query 'views/pipeline/01-information-links.rq' `
  --query 'views/pipeline/02-l2-primary-interface.rq' `
  --out "$env:TEMP\DDTA-Generic-Graph\L2_ALL"

code "$env:TEMP\DDTA-Generic-Graph\L2_ALL.graph.md"
```

To inspect the selected RDF without changing query logic, append `--emit-query-result`. This writes `.result.ttl` only on successful validation/rendering.

## Select another source subset — same query, same renderer, same YAML

To analyze just MR-01 and MR-02, keep the **same L2 query chain** and change only `--mr` / `--out`:

```powershell
python -m tools.visualize `
  --mr 'MR-01,MR-02' `
  --query 'views/pipeline/01-information-links.rq' `
  --query 'views/pipeline/02-l2-primary-interface.rq' `
  --out "$env:TEMP\DDTA-Generic-Graph\L2_MR01_02"
```

For a more general document selection, `tools.visualize` also supports repeated `--source` arguments. Avoid loading a companion standalone `.ttl` alongside its Markdown Turtle by default.

## Determinism / checks

- Identical input documents, selection, ordered queries, schema, YAML and tool versions yield identical generated content.
- A different `--mr` selection changes the *input RDF graph* and may legitimately change the output.
- On validation or query errors, output files must not be created or overwritten (pipeline contract).
- To check that **previously generated outputs** still match without overwriting them, rerun the exact same command with `--check`; the files must already exist.
- The graphical direction of `hasInput` can be inverted by the shared YAML presentation rule; it does not change the RDF subject/predicate/object.
- Do not infer data transfers, execution order, new functions, or missing architectural relationships.
- Graph L2 presently expands the *primary* interface, not all functions' interfaces or the internals of information/contract structures.

## Repository locations

```
tools/visualize.py
tools/visualization.yaml
views/pipeline/01-information-links.rq
views/pipeline/02-l1-projection.rq
views/pipeline/02-l2-primary-interface.rq
views/pipeline/explicit-relationships.rq
```

Graph L2 is a working hypothesis for the first macro-level documentation-analysis phase. Review it with different MR selections before freezing any methodological guide rule.
