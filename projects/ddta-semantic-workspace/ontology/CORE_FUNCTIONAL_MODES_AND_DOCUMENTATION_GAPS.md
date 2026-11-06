# DDTA Core — Functional Modes and Documentation Gaps

**Integration scope:** `ontology/core.ttl` and generic RDF-to-graph validation/visualization.
**Status:** integrated Core vocabulary; MR-01 is now canonical and Graph L3 general is available.
**Non-goals:** no inference that undocumented statements are false, and no automatic derivation of a FunctionalMode from a changing input.

## FunctionalMode

- `ddta:FunctionalMode`: a declared applicability variant of a stable `ddta:Function`; disjoint with Function and Process. It is not a subfunction, execution, or implementing pipeline.
- `ddta:hasMode`: Function -> FunctionalMode; the renderer may draw graphical containment, but this is **not** semantic `hasPart`.
- `ddta:hasInput` / `ddta:hasOutput`: the same functional interface relations are used on a `Function` and a `FunctionalMode`; the subject's RDF type distinguishes them. They do not describe a transfer or assert successful execution.
- The former mode-specific predicates have been **retired**: `modeHasInput`, `guaranteesOutput`, `requiresPresent`, `requiresAbsent`. Do not assert or use them in gap predicates. Missing `hasInput` statements are **not negative facts** (OWL Open World semantics); `hasOutput` does not formalize a per-element guarantee.
- `ddta:constrainsInformation` links ContractElement to the Information it constrains; `minOccurs` and `maxOccurs` state occurrence bounds in the contract context, not on the Information entity.

A Function may use varying input without any FunctionalMode (e.g. the DDTA graph generator with or without DEC sources). Declare modes only when their distinction is documented as meaningful.

## DocumentationGap

- `ddta:DocumentationGap`: identified insufficiency of documentation.
- `ddta:EntityDocumentationGap` + `ddta:concernsEntity`: insufficient description concerning an entity.
- `ddta:RelationDocumentationGap` + `ddta:gapSource`, `ddta:gapPredicate`, `ddta:gapTarget`: a relation whose truth is not established.
- All gaps require **exactly one nonempty `rdfs:label`** in the selected RDF/Turtle. Optional `rdfs:comment` can provide extended explanation. A generalized custom subclass is also checked. The validator implements this check; OWL alone does not.
- The three `gap*` assertions **do not assert** the questioned relation. The validator rejects a gap for a relation already asserted in the selected RDF graph, duplicate descriptions of a relation, and incomplete endpoints.

Example:

```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <https://example.org/case#> .

ex:MissingBinding a ddta:RelationDocumentationGap ;
    rdfs:label "Non specificato se la modalità garantisce la priorità"@it ;
    rdfs:comment "Output da verificare rispetto al contratto di valutazione."@it ;
    ddta:gapSource ex:ModeWithoutImage ;
    ddta:gapPredicate ddta:hasOutput ;
    ddta:gapTarget ex:Priority .
```

## Rendering

`tools/visualization.yaml` is the single graphical style authority. For a gap, the renderer creates a **yellow circle with black ?**, and shows its source `rdfs:label` as a separate caption with a subtle dotted leader. The caption is *presentation-only*.

In the default Graph L3, Contract and ContractElement are not drawn: their occurrence constraints are displayed on the Information nodes as view-only cardinalities. The contract identities and links remain in the canonical RDF. An explicit contract-specific view may still display the full contract structure.

For a relation gap, the source and target are connected through the circle by yellow dashed segments; no RDF domain relation is fabricated. An optional Information element (`minOccurs = 0`) uses a dashed **border**, which is independent of the yellow DocumentationGap convention.

## Regression and reproduction

From `projects/ddta-semantic-workspace`:

```powershell
python experiments/graph-l3-functional-modes/run_experiment.py --out "$env:TEMP\DDTA-L3-FOCUS"
python -m unittest discover -s tests -p test_l3_functional_modes.py -v
code "$env:TEMP\DDTA-L3-FOCUS.graph.md"
```

The L3 pilot uses `ontology/core.ttl` directly: the old `core-extension-candidate.ttl` is retired and deliberately empty. The selected L3 source is the canonical `dermatriage/mr/MR-01.md`. The general six-MR Graph L3 is available as `--view l3`. A focus selector remains future work.
