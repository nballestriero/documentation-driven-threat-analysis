# DDTA Chapter 4 + post-documentation work-plan drop-in

Target repository baseline:

`9a04bc5b98b7f4a2b8400f2b210e7cea6b04d1a9`

This drop-in is **additive**. It does not modify the current MR/Decision/FR closure files and it does not yet integrate the new chapter into `thesis/latex/DDTA_tesi.tex`.

## Added thesis artifact

- `thesis/latex/chapters/04-documentation-authoring-metamodel.tex`
- `thesis/latex/chapters/04-documentation-authoring-metamodel.pdf`
- supporting chapter figures under `thesis/latex/chapters/figures/04_*`

The standalone PDF is a review candidate for Chapter 4. Integration/renumbering of the master thesis is deferred until human review.

## Added work plan

- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R1.md`
- matching `.tex` and `.pdf`

The plan explicitly supersedes the earlier *sequence* that placed Base Analysis before SecurityRequirement design. It does **not** reopen the closed MR/Decision/FR semantics.

The next research order is:

```text
Chapter 4 review
 -> minimal SpecializedRequirement semantics
 -> method-neutral SecurityRequirement semantics
 -> independent SEC corpus
 -> formal Base Analysis / BAE
 -> common AnalysisRecord / Finding
 -> method-neutral overlay/plugin contract
 -> STRIDE
 -> Finding -> SEC provenance / effective obligation
 -> design change -> re-analysis
 -> STRIDE-AI
```

LINDDUN and an optional additional method remain later neutrality challenges, not primary implementation/evaluation methods.
