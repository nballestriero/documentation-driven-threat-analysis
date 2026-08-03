# Thesis representation

The thesis may derive prose, tables and figures from the research records in
this repository.

The thesis must not treat candidate mappings as accepted findings until their
study status is reviewed.

## Representations and authority

The Markdown chapter files and research registries preserve research structure,
claims, evidence and work still to be completed. They remain research-oriented
sources and scaffolding rather than final typesetting.

`thesis/latex/DDTA_tesi.tex` is the editable Italian thesis projection. It may
synthesize repository records into academic prose, tables and figures, but it
is not an independent source of research claims or evidence. Statements about
ThreatForge must remain traceable to an immutable ThreatForge baseline recorded
in this research repository.

Where the available evidence is incomplete, the LaTeX projection must preserve
an explicit editorial marker instead of presenting provisional material as an
established result.

## Version history

Git history preserves the evolution of the LaTeX source. Numbered copies of the
same working file are not maintained in parallel.

Meaningful thesis milestones may receive repository tags. Generated PDFs are
not committed for every edit; milestone PDFs should normally be attached to the
corresponding release or retained only when an explicit archival decision is
made.

## Build

From `thesis/latex` run:

```text
pdflatex -interaction=nonstopmode -halt-on-error DDTA_tesi.tex
pdflatex -interaction=nonstopmode -halt-on-error DDTA_tesi.tex
```

The second pass resolves the table of contents and internal references. LaTeX
auxiliary files and the ordinary working PDF are ignored by Git.

## Planned evolution

- bibliography completion and source-specific notes;
- figures derived from study and ThreatForge baseline records;
- experiment descriptions, protocols and reviewed results;
- claim-to-evidence consolidation;
- institution-specific front matter and final submission formatting.
