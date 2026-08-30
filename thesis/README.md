# Thesis representation

The thesis derives prose, tables and figures from the reviewed research records in this repository.

It must not treat candidate mappings, study-local observations, single-case validation evidence, or provisional closure attempts as broader accepted findings than their evidence scope supports.

## Representations and authority

The Markdown chapter files and research registries preserve research structure, claims, evidence and work still to be completed. They remain research-oriented sources and scaffolding rather than final typesetting.

The current reviewed standalone Italian thesis sources are under:

`thesis/latex/chapters/`

Current reviewed chapter authority is:

```text
Chapter 2
    02-background.tex
    02-background.pdf
    CLOSED / FINAL for current scope

Chapter 3
    03-state-of-the-art-and-research-gap.tex
    03-state-of-the-art-and-research-gap.pdf
    CLOSED / FINAL for current scope

Chapter 4
    04-documentation-authoring-metamodel.tex
    04-documentation-authoring-metamodel.pdf
    CLOSED / FINAL for current scope
```

Closure record:

- `thesis/latex/chapters/CHAPTERS_2_4_CLOSURE_R1.md`

`thesis/latex/DDTA_tesi.tex` predates the current standalone Chapter 2-4 workflow and is not the current chapter-authority source.

It must not be incrementally patched as though it were the current master and must not override newer research scope, claims, evidence, or reviewed standalone chapter text.

The integrated thesis master will be rebuilt later from reviewed standalone sources.

## Claim and evidence authority

Canonical thesis claims:

- `thesis/claims/claims.registry.yml`

Current evidence registry:

- `thesis/evidence/evidence.registry.yml`

Current evidence-consolidation checkpoint:

- `methodology/DDTA_R25_THESIS_READY_EVIDENCE_CONSOLIDATION_CHECKPOINT_R1.md`

R25 Phase 3 preserves the six canonical claims without promotion and indexes reviewed evidence through `EVD-0017`.

The evidence registry distinguishes bounded method/case evidence from later empirical evidence.

Current Facial Access evidence may support carefully scoped prose about:

```text
method construction
case feasibility
documentation validation for Facial Access
Base Analysis feasibility for Facial Access
counterexample-driven BA2 refinement
Facial Access post-BA regression
```

It must not be presented as:

```text
universal effectiveness
cross-domain validation
integrated BA6 success
STRIDE / STRIDE-AI success
final RQ answers
```

Where evidence is incomplete, thesis prose must preserve an explicit editorial/evidence boundary instead of presenting provisional material as an established result.

## Current thesis structure

The current forward chapter map is:

- `thesis/outline.md`

The reviewed structure that must be preserved is:

```text
Chapter 2
    Background

Chapter 3
    State of the Art / Research Gap

Chapter 4
    Documentation metamodel and authoring rules
```

Chapter 4 is not the current Research Method chapter.

Later chapters remain working orientation until separately reviewed.

## Current writable-state boundary

After R25 Phase 3 and Phase 4 orientation synchronization:

```text
Chapter 1
    motivation / problem / RQs / scope
    writable with evidence-qualified contribution wording

Chapter 2
    CLOSED

Chapter 3
    CLOSED

Chapter 4
    CLOSED
    semantic reopen only under its recorded criteria

DDTA / BA methodology material
    WRITABLE through frozen documentation method,
    BA0-BA5 contract,
    and Facial Access case regression

BA6 integrated result
    NOT WRITABLE AS CLOSED

ThreatForge implementation chapter
    DEFER

evaluation protocol/design
    PARTLY WRITABLE

empirical evaluation results
    DEFER

final RQ answers
    DEFER
```

## Version history

Git history preserves the evolution of the LaTeX sources.

Numbered copies of the same working chapter are not maintained in parallel unless a specific archival decision requires one.

Meaningful thesis milestones may receive repository tags.

The retained Chapter 2-4 PDFs are explicit review milestones beside their corresponding LaTeX sources.

## Build

Standalone reviewed sources are built independently from:

`thesis/latex/chapters/`

On Windows PowerShell:

```powershell
cd thesis\latex\chapters

pdflatex -interaction=nonstopmode -halt-on-error 02-background.tex
pdflatex -interaction=nonstopmode -halt-on-error 02-background.tex
pdflatex -interaction=nonstopmode -halt-on-error 02-background.tex

pdflatex -interaction=nonstopmode -halt-on-error 03-state-of-the-art-and-research-gap.tex
pdflatex -interaction=nonstopmode -halt-on-error 03-state-of-the-art-and-research-gap.tex
pdflatex -interaction=nonstopmode -halt-on-error 03-state-of-the-art-and-research-gap.tex

pdflatex -interaction=nonstopmode -halt-on-error 04-documentation-authoring-metamodel.tex
pdflatex -interaction=nonstopmode -halt-on-error 04-documentation-authoring-metamodel.tex
pdflatex -interaction=nonstopmode -halt-on-error 04-documentation-authoring-metamodel.tex

Remove-Item `
    .\02-background.aux, `
    .\02-background.log, `
    .\03-state-of-the-art-and-research-gap.aux, `
    .\03-state-of-the-art-and-research-gap.log, `
    .\04-documentation-authoring-metamodel.aux, `
    .\04-documentation-authoring-metamodel.log `
    -Force -ErrorAction SilentlyContinue
```

Three passes are used deliberately so citations, labels and internal references settle deterministically before a milestone PDF is reviewed.

The final integrated build procedure will be frozen when reviewed standalone sources are assembled into the thesis master.

## Planned evolution

- bibliography completion and source-specific notes;
- evidence-qualified DDTA / Base Analysis methodology chapter authoring;
- formal holdout protocol and later holdout evidence;
- experiment descriptions, protocols and reviewed results;
- direct claim-to-evidence links only when evidence scope is commensurate with claim scope;
- later ThreatForge reference-implementation material after methodology stabilization;
- assembly of reviewed standalone LaTeX chapters into the final thesis master;
- institution-specific front matter and final submission formatting.
