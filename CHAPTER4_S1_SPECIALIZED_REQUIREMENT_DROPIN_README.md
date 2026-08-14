# Chapter 4 + SpecializedRequirement S1 drop-in

Baseline used for the research regression:

`3eeac1fc972d89282cd2ffd8700e9af0f5b69610`

## What this package changes

### Replaces existing canonical thesis chapter

```text
thesis/latex/chapters/04-documentation-authoring-metamodel.tex
thesis/latex/chapters/04-documentation-authoring-metamodel.pdf
```

The filenames are intentionally unchanged so the existing thesis include path continues to work.

### Adds new research package

```text
04-specialized-requirement/
  01-metamodel/
  02-authoring-guidance/
  03-example-facial-access/
  README.md
  SHA256SUMS.txt
```

## Semantic change carried by the chapter revision

The chapter now includes the candidate `Isolated-MR review` heuristic discovered by regressing the facial-access corpus after S1:

- an MR with no canonical MR relation is not automatically invalid;
- graph isolation is a review signal;
- the reviewer checks whether the node is a valid autonomous macro responsibility, a missing dependency, or a cross-cutting concern bucket classified too high;
- specialized concerns such as security, privacy, performance or regulatory constraints should not be promoted to MR merely to give an analysis methodology a home.

The revised facial-access study removes historical `MR-0004` from the revised corpus and redistributes its two main commitments according to their semantics rather than their former container.

## Intentionally not changed by this drop-in

- no SecurityRequirement metamodel yet;
- no Base Analysis/BAE;
- no STRIDE/STRIDE-AI formalization;
- no ThreatForge semantic changes;
- no automatic overwrite of `INDEX.md` or root checksum files.

A suggested INDEX entry is included in `04-specialized-requirement/README.md` so it can be merged without overwriting unrelated local edits.
