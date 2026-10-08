# MR-C6 graph levels G0/G1/G2/G3/G4/G5 - repository review R4

This folder preserves the deterministic MR-C6 projection through the FR-C6-01-03 split working review.

- `MRC6_G0_R2.mmd`: accepted top-level MR-C6 / DEC-C6-01 semantics.
- `MRC6_G1_R2.mmd`: G0 plus direct MR-C6 `hasPart` environment composition.
- `MRC6_G2_R2.mmd`: G1 plus accepted named hardware configuration `constrain`.
- `MRC6_G3_R6.mmd`: G2 plus FR-C6-01-02 named software-dependency `constrain` and accepted `realize` from `SCP-C6-01-02 / requirements.txt` to `RequiredSoftwareDependencies`.
- `MRC6_G4_R8.mmd`: G3 plus the reviewed FR-C6-01-03A ModelResources projection. Containment inside `ModelResources` renders the reviewed model-resource composition; the existing functional `realize` relations reach the current model realizations outside `DermaTriageEnvironment`.
- `MRC6_G5_R8.mmd`: G4 plus documentation-only placeholders for FR-C6-01-03B (`DermaTriage RAG Dataset`, `data/RAG_dataset.csv`) and FR-C6-01-03C (`Training images`, `data/images/`). The dashed amber cards are intentionally BA-pending and do not establish new `hasPart` propositions yet.
- `DDTA_R25_DERMATRIAGE_MRC6_GRAPH_LEVELS_G0_G1_G2_G3_G4_G5_MERMAID_R8.pdf`: reviewed six-page oversized projection.
- `MRC6_G0_R6_review_page.pdf` ... `MRC6_G3_R6_review_page.pdf`: unchanged accepted review pages reused from R6.
- `MRC6_G4_R8_review_page.pdf` and `MRC6_G5_R8_review_page.pdf`: reviewed page snapshots for the new levels.
- `...R8.tex`: LaTeX assembly wrapper for the six reviewed page snapshots.

The Mermaid files are the semantic/topological graph sources. Solid blue containment denotes the reviewed composition/`hasPart` view where BA is already established. Explicit arrows remain named BA operators such as `realize` or `constrain`. Amber dashed cards in G5 preserve documentation elements whose BA has deliberately not yet been performed.

G0-G3 are reused unchanged from the accepted R6 graph set. G4 adds the ModelResources work already reviewed in chat; G5 materializes the A/B/C documentation split so that the RAG dataset and training-image information is not lost before their dedicated BA pass.
