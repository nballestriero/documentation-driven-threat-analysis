# DermaTriage — new candidate documentation

`mr/MR-01.md` is the editable source (YAML + concise Intent/Context + Turtle). `diagrams/*` is generated.

- [MR-01 source](mr/MR-01.md)
- [MR-01 summary graph](diagrams/MR-01-overview.graph.md)
- [MR-01 composition and contract graph](diagrams/MR-01-structure.graph.md)

Older governed documentation remains a historical/reference input in `../references/dermatriage/` and in the existing TESI repository. **Do not treat historical references as hidden dependencies of the newly authored MR.** The current MR-01 is candidate, not approved as a replacement for the original.

## MR-01 + MR-02 RDF composition (experimental)

`mr/MR-02.md` intentionally reuses the exact `derma:TriageOutcome` IRI from MR-01. This is a plausible test assumption, **not a verified claim about the historical implementation**. The renderer reads both Markdown Turtle blocks into one RDF graph; `views/mr-aggregate-{overview,structure}.rq` select two generated Mermaid views under `diagrams/MR-01-02-*`.

The functional overview does not yet assert an owning System or a runtime order; those are separate propositions. The CLI takes one `--source` argument per Markdown/Turtle document.


## MR-03 and on-demand aggregate views (candidate)

- [MR-03 — clinical review management](mr/MR-03.md): its Turtle reuses the same `TriageOutcome` IRI and models `ClinicalReviewRecord hasPart (TriageOutcome, ClinicalReview)`.
- `views/mr-functions-overview.rq` and `views/mr-functions-structure.rq` select **every `ddta:Function` in the supplied MR source set**, without listing MR names explicitly.
- Generate *temporary* cross-MR diagrams by giving the renderer repeated `--source` arguments and an `--out` path under `$env:TEMP`. These previews are **not committed by default**; the editable sources remain Markdown/Turtle, SPARQL and visualization YAML.
- `hasPart` is projected as containment; an RDF IRI is drawn only once even if used by several MR and as both an input and an output part. This is a logical composition, not a claim of physical data copying or temporal execution order.

## MR-04 controlled adaptation (candidate)

- [MR-04 — controlled adaptation](mr/MR-04.md) reuses `derma:ClinicalReviewRecord` from MR-03.
- `AccumulatedClinicalReviewRecords hasPart ClinicalReviewRecord` is a **logical collection structure at MR level**, not a count, set of actual record instances, or an assertion that every review qualifies for a given adaptation route. The latter is DEC/FR territory.
- `ControlledAdaptation` has the accumulated records as input; its outputs are an `AdaptationCandidate` (`Artifact`) and `AdaptationQualificationResult` (`Information`). Neither states that a candidate has been adopted or deployed.
- Artifact node recognition is a **visualization-only** addition in `tools/visualization.yaml`, reusing an existing palette class. Core is unchanged.
- Generate MR-01…MR-04 overview/structure previews on demand using `dermatriage/views/mr-functions-{overview,structure}.rq` and repeated `--source` arguments. No generated four-MR diagrams are stored in Git by default.

## Generating a combined view on demand (all MR)

From the workspace root, use `./tools/build_views.ps1 -AllMR` in PowerShell to
load **all** `dermatriage/mr/MR-*.md` files, union their RDF by IRI and open the
**structure** view in VS Code (`Ctrl+Shift+V` for Markdown preview). The output
is written to `%TEMP%/DDTA-All-MR-structure.graph.md` and `.mmd`, **not** to
Git. Run `./tools/build_views.ps1 -AllMR -View overview` for the simpler flow;
`-NoOpen` generates the files without opening VS Code. The source count and
names are printed to make omissions visible.

The ordinary `./tools/build_views.ps1` and `./tools/check.ps1` still generate
or verify only the intentionally tracked MR-01 and MR-01+MR-02 diagrams.
