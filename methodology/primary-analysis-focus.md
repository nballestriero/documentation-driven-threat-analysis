# Primary Base Analysis focus - historical working proposition

**Status: SUPERSEDED AS A GENERAL BASE-ANALYSIS RULE / RETAINED AS HISTORICAL STUDY INPUT.**

This file originated the `STUDY-0001` ThreatForge corpus experiment. The study may remain useful as evidence about that bounded corpus, but later DDTA research does **not** accept either of the following as general methodology invariants:

1. every Functional Requirement must identify exactly one primary Base Analysis focus; or
2. `actor`, `component`, `asset`, `boundary`, `data_flow` is the accepted or complete BAE taxonomy.

BA0-R and BA0-T1 instead require semantic responsibilities to be justified by the governed corpus and prior art, and explicitly reject promotion of a recurring concept to a first-class metaclass merely because it is useful or appears in an earlier study. BA1 remains not started.

The historical proposition is preserved below to keep the experiment reproducible.

---

## Historical working proposition

Every Functional Requirement should identify exactly one primary Base Analysis focus.

The primary focus must resolve to one of:

- `actor`
- `component`
- `asset`
- `boundary`
- `data_flow`

A Governance Requirement inherits the primary focus of its Functional Requirement parent and may add:

- governed targets;
- constraints;
- verification components;
- evidence;
- related elements;
- candidate flows and boundaries.

## Historical interpretation rules

1. Repeated noun phrases and pronouns may resolve to the same entity.
2. A noun does not automatically become an asset.
3. A component or process may be the primary focus when it performs the behavior.
4. An asset may be the primary focus when the requirement governs a registry, catalog, view, document corpus or other protected information resource.
5. A data flow may be the primary focus when the requirement is naturally about information crossing from one endpoint to another.
6. An aggregate focus is allowed only when its members form one governed lifecycle and the aggregate can receive a stable identity.
7. If a single focus can be obtained only through an artificial aggregation, the requirement should be reviewed for possible decomposition.
8. Candidate mappings do not become canonical Base Analysis entities without governed review.

## Historical confidence values

- `explicit`: the body introduces and repeatedly reuses one clear subject.
- `inferred`: the focus is natural but requires interpretation.
- `composite`: the requirement describes one coherent aggregate not explicitly named as a single entity.
