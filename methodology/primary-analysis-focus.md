# Primary Base Analysis focus

Status: research working proposition under the literature-to-model neutrality audit.
It is not a frozen DDTA portability-contract rule and must not be treated as evidence
that one primary focus or the current five focus types are universally neutral.

## Working proposition

Every Functional Requirement should identify exactly one primary Base Analysis
focus.

The primary focus must resolve to one of:

- `actor`
- `component`
- `asset`
- `boundary`
- `data_flow`

A Governance Requirement inherits the primary focus of its Functional
Requirement parent and may add:

- governed targets;
- constraints;
- verification components;
- evidence;
- related elements;
- candidate flows and boundaries.

## Interpretation rules

1. Repeated noun phrases and pronouns may resolve to the same entity.
2. A noun does not automatically become an asset.
3. A component or process may be the primary focus when it performs the behavior.
4. An asset may be the primary focus when the requirement governs a registry,
   catalog, view, document corpus or other protected information resource.
5. A data flow may be the primary focus when the requirement is naturally about
   information crossing from one endpoint to another.
6. An aggregate focus is allowed only when its members form one governed
   lifecycle and the aggregate can receive a stable identity.
7. If a single focus can be obtained only through an artificial aggregation,
   the requirement should be reviewed for possible decomposition.
8. Candidate mappings do not become canonical Base Analysis entities without
   governed review.

## Confidence values

- `explicit`: the body introduces and repeatedly reuses one clear subject.
- `inferred`: the focus is natural but requires interpretation.
- `composite`: the requirement describes one coherent aggregate not explicitly
  named as a single entity.
