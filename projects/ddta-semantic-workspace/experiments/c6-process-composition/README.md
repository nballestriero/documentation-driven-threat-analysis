# DEC-C6-01: experimental process composition pilot R1

**Status:** EXPERIMENTAL_NON_CANONICAL. This is a test of the existing Core,
**not** an accepted RDF replacement for DEC-C6-01.

## Source and question

The DermaTriage parallel case study R25, DEC-C6-01 (page 48), describes
`EnvironmentSetupProcedure` as realizing `EnvironmentPreparation` and identifies
six named stages. The original `OR4_Training_Environment_Config.pdf`, page 3,
documents six operational setup steps and a subsequent deployment-verification step.

We are testing whether the six stages can each have the identity of an autonomous
`ddta:Process` while `EnvironmentSetupProcedure` composes them using `ddta:hasPart`.
We deliberately retain the original names ending in `Stage` for traceability.
Typing those stages as `ddta:Process` is a **candidate interpretation**, not a
claim already settled by the historical BA or a statement that each is executable
standalone without additional prerequisites.

### Six documented stages (documentation order; NOT RDF order)

1. `RepositoryAcquisitionStage`: acquire application code.
2. `SoftwareDependencyInstallationStage`: install software dependencies.
3. `ModelResourceAcquisitionStage`: acquire required model resources.
4. `EnvironmentConfigurationStage`: configure environment/bindings.
5. `LocalResourceInitializationStage`: initialize local resources.
6. `ServiceStartupStage`: start services.

The original OR4 commands are implementation evidence at lower level, not the
definitions of the six process identities. In particular, the explicitly listed
model-download step concerns EfficientNet weights; other models may be acquired
automatically (see original OR4 section 4).

## Result of the pilot

Existing Core concepts suffice for **structural composition**:
`ddta:Process`, `ddta:Function`, `ddta:hasPart`, `ddta:realizesFunction`.
None of these implies execution order, data transfer, runtime occurrence,
actual dependency, success, or exclusivity to this parent workflow.

This pilot does **not** assert that `RepositoryAcquisitionStage` and
`ModelResourceAcquisitionStage` are independent in their technical preconditions.
Different duties need not mean the absence of prerequisites.

**Outstanding modeling questions, for later review:**
- How to encode an ordered placement of a reusable process within a workflow?
- Can the same process appear twice in one workflow or once in two workflows
  without conflating its reusable definition and its contextual occurrence?
- `ddta:hasPart` models composition, not invocation. If we later need distinct
  occurrences, an explicit `ProcessStep` or equivalent contextual role may be needed.
- The current Mermaid renderer rejects shared children with multiple `hasPart`
  parents; that is a **rendering** limitation, not an OWL prohibition.

No `ProcessStep`, `Workflow`, `precedes`, transition, guard, or new ontology term
is declared; `ontology/process.ttl`, `ontology/core.ttl`, and the authored MR
documents remain unchanged.

## Run the isolated test

From `projects/ddta-semantic-workspace` in PowerShell:

```powershell
python -m unittest discover -s tests -p test_c6_process_composition.py -v
```

## Generate Mermaid using the existing renderer (on demand)

From the same workspace directory:

```powershell
$Pilot = 'experiments/c6-process-composition'
$Out = Join-Path $env:TEMP 'DDTA-C6-process-composition'
python -m tools.rdf_mermaid.render `
  --source "$Pilot/DEC-C6-01-process-composition.ttl" `
  --config "$Pilot/visualization.yaml" `
  --view "$Pilot/composition-view.rq" `
  --out $Out
code "$Out.graph.md"
```

This generates both `$Out.graph.md` and `$Out.mmd` outside the repository.
It intentionally shows only containment and realization, never arrows of
invented precedence. Open Markdown Preview in VS Code (`Ctrl+Shift+V`).

The ordinary project `build_views.ps1` and `check.ps1` are not changed.
