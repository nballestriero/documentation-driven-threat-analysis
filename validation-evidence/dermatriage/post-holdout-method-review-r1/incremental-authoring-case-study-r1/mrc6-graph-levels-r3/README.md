# MR-C6 graph levels G0/G1/G2/G3/G4/G5/G6 - repository review R5

This folder preserves the deterministic MR-C6 projection through the FR-C6-01-03A1 model-acquisition review.

- `MRC6_G0_R2.mmd`: accepted top-level MR-C6 / DEC-C6-01 semantics.
- `MRC6_G1_R2.mmd`: G0 plus direct MR-C6 `hasPart` environment composition.
- `MRC6_G2_R2.mmd`: G1 plus accepted named hardware configuration `constrain`.
- `MRC6_G3_R6.mmd`: G2 plus FR-C6-01-02 named software-dependency `constrain` and accepted `realize` from `SCP-C6-01-02 / requirements.txt` to `RequiredSoftwareDependencies`.
- `MRC6_G4_R8.mmd`: G3 plus the reviewed FR-C6-01-03A ModelResources projection. Containment inside `ModelResources` renders the reviewed model-resource composition; the existing functional `realize` relations reach the current model realizations outside `DermaTriageEnvironment`.
- `MRC6_G5_R8.mmd`: G4 plus documentation-only placeholders for FR-C6-01-03B (`DermaTriage RAG Dataset`, `data/RAG_dataset.csv`) and FR-C6-01-03C (`Training images`, `data/images/`). The dashed amber cards are intentionally BA-pending and do not establish new `hasPart` propositions yet.
- `MRC6_G6_R9.mmd`: G5 plus the accepted FR-C6-01-03A1 acquisition slice. `GoogleDriveModelStore` is the external source Store; `EfficientNetB4WeightsArtifact` (`efficientnet_b4.pth`, EfficientNet-B4 weights, 72 MB) is the transferred content; `ActiveClassifierStore` is the local destination Store with locator `models/efficientnet_b4.pth` relative to `image_classifier/`. Its containment inside `ModelResources` maps to `BAP-FRC6-01-03A1-05`; the acquisition path maps to `BAP-FRC6-01-03A1-04`.
- `DDTA_R25_DERMATRIAGE_MRC6_GRAPH_LEVELS_G0_G1_G2_G3_G4_G5_G6_MERMAID_R9.pdf`: reviewed seven-page cumulative projection. G6 is vector/selectable; earlier accepted pages remain unchanged.
- `MRC6_G0_R6_review_page.pdf` ... `MRC6_G3_R6_review_page.pdf`: unchanged accepted review pages reused from R6.
- `MRC6_G4_R8_review_page.pdf` and `MRC6_G5_R8_review_page.pdf`: unchanged reviewed page snapshots from R8.
- `MRC6_G6_R9_review_page.pdf`: accepted vector review page for the A1 acquisition increment.
- `...R9.tex`: LaTeX assembly wrapper for the seven reviewed page snapshots.

The Mermaid files are retained as the semantic/topological graph sources and as the reproducible basis for subsequent incremental edits. Visual containment represents the accepted `hasPart` view; explicit labeled edges represent other BA operators. Dashed amber cards in G5/G6 remain documentation-only BA-pending elements for FR-C6-01-03B/C.

G6 deliberately does not add an intermediate landing Store for the Google Drive download, because the source does not specify it. The open relation between the model identity `EfficientNet-B4` and the weights artifact remains outside this graph pass, as do authority-boundary and integrity-verification analysis.
