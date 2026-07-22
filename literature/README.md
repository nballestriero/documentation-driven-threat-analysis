# Literature corpus

This directory is the research index for Documentation-Driven Threat Analysis (DDTA).
It separates bibliographic facts from interpretation and from thesis claims.

## Workflow

1. Register a source in `literature.registry.yml`.
2. Create one note from `templates/source-note.template.md`.
3. Record claims supported, contradicted, or left open by the source.
4. Add cross-source conclusions only under `syntheses/`.
5. Cite stable publisher, DOI, standard, or project URLs; do not commit copyrighted PDFs.

## Evidence levels

- `primary_research`: peer-reviewed empirical or technical research.
- `secondary_review`: systematic review, mapping study, or survey.
- `standard_guidance`: standard, manifesto, official methodology, or maintained guidance.
- `book`: scholarly or practitioner monograph.
- `tool_project`: maintained tool or reference implementation documentation.
- `preprint`: scholarly manuscript not yet confirmed as peer reviewed.

## Verification states

- `verified`: title, authorship, year, and stable identifier checked against a primary source.
- `partially_verified`: core identity checked, but venue/version or metadata still needs review.
- `candidate`: relevant lead requiring full verification before thesis citation.
