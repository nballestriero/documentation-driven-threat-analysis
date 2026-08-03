# Literature corpus

This directory is the research index for Documentation-Driven Threat Analysis (DDTA).
It separates bibliographic facts, source-derived content, temporal assessment,
researcher interpretation and thesis claims.

## Workflow

1. Register a source in `literature.registry.yml`.
2. Record legal access metadata in `source-access.registry.yml`.
3. Create one source note from `templates/source-note.template.md`.
4. Answer the four reading questions and assess temporal validity.
5. Record citation-ready locations in `excerpts/<SOURCE-ID>.excerpts.yml`.
6. Keep verbatim quotation, faithful paraphrase and researcher interpretation separate.
7. Add cross-source conclusions only under `syntheses/`.
8. Cite stable publisher, DOI, standard or project URLs; do not commit copyrighted source PDFs.

## Four reading questions

1. What research problem does the source address and what contribution does it make?
2. Which artifacts does it start from and how does it assume, create, extract or derive a system representation?
3. How does it connect sources, requirements, evidence and change, and what is automated or human-reviewed?
4. What does it demonstrate, what are its limits, and what does it leave open for DDTA and the overlay method?

## Temporal validity

Every source note must distinguish conceptual durability from technological and empirical currency.
Record publication year, evidence window, time sensitivity, elements still applicable,
potentially obsolete elements, contemporary corroboration and permitted thesis use.

A foundational source may remain essential for definitions while being unsuitable as
standalone evidence of current tools or practice.

## Evidence notation

- `C`: verified verbatim quotation with exact location.
- `P`: faithful paraphrase with exact location.
- `I`: researcher interpretation, clearly separated from source-derived content.

## Repository and local PDFs

Generated DDTA worksheets may be committed under `worksheets/`.
Source PDFs are kept locally under `local-pdf/` and ignored by Git. The repository
stores only legal access links, retrieval metadata and optional local SHA-256 values.

## Evidence levels

- `primary_research`: peer-reviewed empirical or technical research.
- `secondary_review`: systematic review, mapping study, or survey.
- `standard_guidance`: standard, manifesto, official methodology, or maintained guidance.
- `book`: scholarly or practitioner monograph.
- `tool_project`: maintained tool or reference implementation documentation.
- `preprint`: scholarly manuscript not yet confirmed as peer reviewed.

## Verification states

- `verified`: title, authorship, year, venue and stable identifier checked against a primary source.
- `partially_verified`: core identity checked, but venue/version or metadata still needs review.
- `candidate`: relevant lead requiring full verification before thesis citation.
