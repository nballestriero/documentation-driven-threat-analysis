# Thesis representation

The thesis may derive prose, tables and figures from the research records in
this repository.

The thesis must not treat candidate mappings as accepted findings until their
study status is reviewed.

## Representations and authority

The Markdown chapter files and research registries preserve research structure,
claims, evidence and work still to be completed. They remain research-oriented
sources and scaffolding rather than final typesetting.

The current chapter-level Italian thesis projections are the standalone sources under
`thesis/latex/chapters/`. Their milestone PDFs are retained together with the corresponding
LaTeX so that each chapter can be reviewed independently.

`thesis/latex/DDTA_tesi.tex` predates the current standalone Chapter 2 and Chapter 3 workflow
and is not the current chapter-authority source. It will be rebuilt/integrated later from the
reviewed standalone LaTeX chapters. It must not be used to override newer research scope,
claims or chapter text.

All LaTeX projections may synthesize repository records into academic prose, tables and
figures, but they are not independent sources of research claims or evidence. Statements
about ThreatForge must remain traceable to an immutable ThreatForge baseline recorded in
this research repository.

Where the available evidence is incomplete, the LaTeX projection must preserve
an explicit editorial marker instead of presenting provisional material as an
established result.

## Version history

Git history preserves the evolution of the LaTeX source. Numbered copies of the
same working file are not maintained in parallel.

Meaningful thesis milestones may receive repository tags. Generated PDFs are not committed
for every edit. The current standalone Chapter 2 and Chapter 3 PDFs are explicit review
milestones retained beside their LaTeX sources; other working PDFs should normally remain
untracked unless another archival decision is made.

## Build

Standalone chapter sources under `thesis/latex/chapters/` are built independently during
chapter drafting and review. On Windows PowerShell, from the repository root:

```powershell
cd thesis\latex\chapters

pdflatex -interaction=nonstopmode -halt-on-error 02-background.tex
pdflatex -interaction=nonstopmode -halt-on-error 02-background.tex
pdflatex -interaction=nonstopmode -halt-on-error 02-background.tex

pdflatex -interaction=nonstopmode -halt-on-error 03-state-of-the-art-and-research-gap.tex
pdflatex -interaction=nonstopmode -halt-on-error 03-state-of-the-art-and-research-gap.tex
pdflatex -interaction=nonstopmode -halt-on-error 03-state-of-the-art-and-research-gap.tex

Remove-Item `
    .\02-background.aux, `
    .\02-background.log, `
    .\03-state-of-the-art-and-research-gap.aux, `
    .\03-state-of-the-art-and-research-gap.log `
    -Force -ErrorAction SilentlyContinue
```

Three passes are used deliberately so inline bibliography citations, labels and internal
references settle deterministically before a milestone PDF is reviewed. The final integrated
build procedure will be frozen when the reviewed standalone sources are assembled into the
thesis master.

## Planned evolution

- bibliography completion and source-specific notes;
- figures derived from study and ThreatForge baseline records;
- experiment descriptions, protocols and reviewed results;
- claim-to-evidence consolidation;
- assembly of reviewed standalone LaTeX chapters into the final thesis master;
- institution-specific front matter and final submission formatting.
