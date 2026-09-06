# Next bounded step — after R3 consolidation

Continue with BA0–BA6 frozen.

## Next element

`FR-18 — Retrieval di casi storici con ChromaDB e all-MiniLM-L6-v2`

## Specific tests

1. Re-evaluate `observe` from DEC-12 using the concrete FR-18 semantics.
2. Determine whether an independently reusable retrieval capability is required.
3. Test whether `ClinicalDescription` is concretely consumed as downstream input,
   adding evidence to P-02.
4. Inspect top-5 and cosine similarity:
   - BA-relevant constraint?
   - data/retrieval contract detail?
   - technical detail only?
5. Inspect ChromaDB and all-MiniLM-L6-v2 realization relationships.
6. Continue collecting P-07 data-contract evidence without adopting a new schema.

Stop after FR-18.
