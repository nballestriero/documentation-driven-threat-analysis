# DDTA Authoring Tool — Guides

This directory holds authoring guides and candidate rules for the DDTA Authoring
Tool, not the project's MR, Decision, or FR documents (those remain in `docs/`).

## Areas

- [`ba/`](ba/README.md): a freeform general BA guide, an operator-sheet
  template, and individually reviewed operator drafts.
- [`mermaid/`](mermaid/README.md): a separate, currently placeholder guide
  for BA-to-Mermaid projection. Graphical conventions are not BA semantics.

## C2 R6 scope

This checkpoint introduces the candidate English format and review draft for
`transfer`, **without** adding executable operator rules or a BA Engine.
The current methodological authority of Operational Guide R3 is preserved;
Rebuild R7 is a source for reconciliation, not automatic promotion.

## Validation stages

The Document Engine validates Markdown field and section structure. A future
BA Rule Loader validates machine-readable operator contracts. A future
BA Engine evaluates BA occurrences in DDTA documents, while the Mermaid
projection engine consumes validated BA through its own separate guidance.
Passing an earlier stage does not imply that later stages have passed.
