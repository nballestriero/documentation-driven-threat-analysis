# DDTA Ontology Identifier Policy — candidate R1

DDTA is the ontology project. Filename, Markdown document ID, prefix abbreviation, ontology IRI and ontology term IRIs are distinct concepts.

- **DDTA Core ontology IRI:** `<https://w3id.org/ddta/core>`
- **DDTA Core term namespace:** `<https://w3id.org/ddta/core#>`
- **Prefix convention:** `@prefix ddta: <https://w3id.org/ddta/core#> .`
- **Example:** `ddta:hasInput` expands to `<https://w3id.org/ddta/core#hasInput>`.
- **File path:** `ontology/core.ttl` is a local serialization; it is **not** the identity.

The base ontology identifier does not include the fragment marker. Terms use `#`. OWL ontology version identifiers may be added in a separate versioning decision; version changes should not automatically rename stable core terms.

**Important publication prerequisite:** The `w3id.org/ddta` path is a **proposed**, not yet registered or verified, persistent identifier. `w3id.org` redirects need an approved registration with a target under the project's control. A local Turtle parser works without dereferencing the URL, but persistent Web resolution is not guaranteed until that registration is completed. Do not claim ownership or W3C endorsement.

## Migration from Protégé-generated IDs

- Old ontology IRI: `<http://www.semanticweb.org/user/ontologies/2026/10/untitled-ontology-16>`.
- Old term namespace: `<http://www.semanticweb.org/user/ontologies/2026/10/untitled-ontology-16/>`.
- New ontology IRI: `<https://w3id.org/ddta/core>`.
- New term namespace: `<https://w3id.org/ddta/core#>`.

Every old term `<http://www.semanticweb.org/user/ontologies/2026/10/untitled-ontology-16/Term>` now has the corresponding new term `<https://w3id.org/ddta/core#Term>`. This is an identity migration, **not** a new ontology axiom or assertion that old and new IDs are equivalent. Older files outside `ddta-semantic-workspace` are intentionally untouched. If they need to interoperate, their IRI references must be migrated or mapped explicitly later.

DermaTriage's `https://example.org/ddta/dermatriage#` currently remains a separate **experimental** project namespace. It is not an alias for Core. Proposed future modules `ai` and `security` would require their own namespaces under the registered project path.

## Invariants

1. One term uses the same IRI everywhere: core definition, MR Turtle, SPARQL, and visualization rules.
2. An RDF term's identity does not depend on its Markdown document, location, `rdfs:label`, or diagram ID.
3. The graph rendering rules remain outside Core; refactoring the IRI must not alter OWL semantics beyond renaming terms.
4. All generated Mermaid diagrams are checked after migration; do not edit generated files to repair an ontology mismatch.
