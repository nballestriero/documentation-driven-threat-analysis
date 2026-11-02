# DDTA Semantic Workspace

**Working project (bootstrap R1)** inside the existing `TESI` Git repository. This directory is the intended **active location** for ongoing DDTA ontology and DermaTriage semantic reconstruction. It is **not** a separate Git repository. The older DDTA documents and tools are **not deleted or superseded automatically**.

## Contents

| Directory | Role |
|---|---|
| `ontology/` | Generic ontology source of truth; `core.ttl` is an **exact copy** of the uploaded `core(2).ttl` (2026-11-02) |
| `dermatriage/mr/` | New concise authored MR documents with inline Turtle (currently MR-01 candidate only) |
| `dermatriage/views/` | SPARQL CONSTRUCT queries defining what to show |
| `dermatriage/diagrams/` | **Generated** Mermaid `.mmd` and GitHub/VS Code-ready `.graph.md` |
| `tools/` | Deterministic renderer, independent YAML graphical conventions, PowerShell commands and dependency pins |
| `tests/` | Regression and source-compatibility tests |
| `references/` | Read-only snapshots of existing documentation to support the rewrite |
| `WORKING_PLAN.md` | Phases, next decisions, migration and deferred clean-up |

**Normative layers:** Turtle/OWL defines semantic identities and relations; SPARQL selects a view; YAML controls rendering; Mermaid is generated output. Changing arrow orientation or visual containment does not change RDF semantics.

## One-time setup (PowerShell, from this directory)

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\tools\requirements.txt
.\tools\check.ps1
```

Alternatively use a configured `python` command and install the requirements without a virtual environment. `check.ps1` prefers `.venv\Scripts\python.exe` if present.

## Daily commands

```powershell
.\tools\build_views.ps1            # regenerate output only when necessary
.\tools\build_views.ps1 -Check     # verify checked-in outputs without modifying files
.\tools\check.ps1                 # tests + generated file freshness
code .\dermatriage\diagrams\MR-01-structure.graph.md
```

In VS Code, open Markdown Preview (`Ctrl+Shift+V`). GitHub also renders Mermaid in fenced Markdown. The `.mmd` file is kept for Mermaid tooling.

## Workflow

1. Update a **source** file, e.g., `dermatriage/mr/MR-01.md` or `ontology/core.ttl`.
2. Modify a SPARQL view or `tools/visualization.yaml` only if the desired **view** or rendering convention changes.
3. Run `tools/build_views.ps1`; check the generated diagram.
4. Run `tools/check.ps1`, inspect `git diff` / `git status`, and commit changes to the existing TESI Git repository when approved.

Do **not** manually edit files in `dermatriage/diagrams/`.

## Status and deliberate limits

- `ontology/core.ttl` uses the DDTA Core namespace `https://w3id.org/ddta/core#` (term IRIs use `#`). The proposed `w3id.org/ddta` identifier must still be registered before public publication.
- The copy of `MR-01.md` and its graph are **candidate**, not promoted to governed documentation.
- The existing MacroRequirement authoring schema requires sections removed in this experiment; the old strict validator has **not** been updated.
- The current renderer rejects `hasPart` cycles or shared children with multiple parents, rather than guessing a graphical containment.
- `hasPart` is represented by nesting in diagrams, but is **not** changed in OWL.
- Detailed contract validation, agentic/AI and security ontologies, and definitive authoring guides are deferred.
- Generated Protégé `###` IRI comments have been normalized to the current `#` namespace. Those comments are descriptive, not RDF triples. See [ontology/IRI_POLICY.md](ontology/IRI_POLICY.md).

See [WORKING_PLAN.md](WORKING_PLAN.md) before extending the model.
