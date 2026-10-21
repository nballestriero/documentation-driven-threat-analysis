# DDTA Authoring Tool — Guides

This directory holds authoring guides and candidate rules for the DDTA Authoring
Tool, not the project's MR, Decision, or FR documents (those remain in `docs/`).

## Areas

- [`ba/`](ba/README.md): a freeform general BA guide, an operator-sheet
  template, and operator sheets with explicit structural review status.
- [`mermaid/`](mermaid/README.md): a separate, currently placeholder guide
  for BA-to-Mermaid projection. Graphical conventions are not BA semantics.

## C2 R6 scope

This checkpoint introduces the candidate English format and review draft for
`transfer`, **without** adding executable operator rules or a BA Engine.
Operational Guide R3 is obsolete and MUST NOT be used as methodological
authority. The R7 rebuild is the working review source; each proposed rule
still requires explicit methodological approval before activation.

## Validation stages

The Document Engine validates Markdown field and section structure. A future
BA Rule Loader validates machine-readable operator contracts. A future
BA Engine evaluates BA occurrences in DDTA documents, while the Mermaid
projection engine consumes validated BA through its own separate guidance.
Passing an earlier stage does not imply that later stages have passed.

## C4 R3 current BA rule status

The generic BA Rule Loader is implemented in the candidate prototype.
`ba/operators/transfer.md` is structurally executable after `reviewStatus`
was set to `reviewed`; `methodStatus: candidate` is unchanged. The general
BA guide and Mermaid guide are still separate workstreams.

## C5 R2 current BA rule status

`ba/operators/transfer.md` and `ba/operators/produce.md` are both
structurally executable (`reviewStatus: reviewed`, `methodStatus: candidate`).
The machine rules come from their English Markdown guides. Source-evidence
review, identity resolution, and temporal semantics are not implied by PASS.
