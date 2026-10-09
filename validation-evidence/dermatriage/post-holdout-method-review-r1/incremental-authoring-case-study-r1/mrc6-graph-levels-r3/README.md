# MR-C6 graph levels G0/G1/G2/G3/G4/G5/G6/G7 - repository review R6

This folder preserves the deterministic MR-C6 projection through the FR-C6-01-03A2/A3/A4 model-acquisition review.

- `MRC6_G0_R2.mmd`: accepted top-level MR-C6 / DEC-C6-01 semantics.
- `MRC6_G1_R2.mmd`: G0 plus direct MR-C6 `hasPart` environment composition.
- `MRC6_G2_R2.mmd`: G1 plus accepted named hardware configuration `constrain`.
- `MRC6_G3_R6.mmd`: G2 plus FR-C6-01-02 named software-dependency `constrain` and accepted `realize` from `SCP-C6-01-02 / requirements.txt` to `RequiredSoftwareDependencies`.
- `MRC6_G4_R8.mmd`: G3 plus the reviewed FR-C6-01-03A ModelResources projection. Containment inside `ModelResources` renders the reviewed model-resource composition; the existing functional `realize` relations reach the current model realizations outside `DermaTriageEnvironment`.
- `MRC6_G5_R8.mmd`: G4 plus documentation-only placeholders for FR-C6-01-03B (`DermaTriage RAG Dataset`, `data/RAG_dataset.csv`) and FR-C6-01-03C (`Training images`, `data/images/`). The dashed amber cards are intentionally BA-pending and do not establish new `hasPart` propositions yet.
- `MRC6_G6_R9.mmd`: G5 plus the accepted FR-C6-01-03A1 acquisition slice. `GoogleDriveModelStore` is the external source Store; `EfficientNetB4WeightsArtifact` is transferred to `ActiveClassifierStore`, whose locator is `models/efficientnet_b4.pth` relative to `image_classifier/`.
- `MRC6_G7_R10.mmd`: G6 plus the accepted A2/A3/A4 HuggingFace acquisition slices. `HuggingFaceModelStore` is the reused source Store; `Qwen2VL7BModelArtifact`, `AllMiniLML6V2ModelArtifact`, and `BioMistral7BModelArtifact` are transferred to their respective local destination Stores. The three local Stores are contained in `ModelResources`; the current model identities are connected to their downloaded artifacts through the reviewed `realize` propositions `BAP-FRC6-01-03A2-06`, `BAP-FRC6-01-03A3-06`, and `BAP-FRC6-01-03A4-06`.
- `DDTA_R25_DERMATRIAGE_MRC6_GRAPH_LEVELS_G0_G1_G2_G3_G4_G5_G6_G7_MERMAID_R10.pdf`: reviewed eight-page cumulative projection. Pages G0-G6 are reused unchanged from R9; G7 is the new vector/selectable page.
- `MRC6_G7_R10_review_page.pdf`: reviewed vector page for the A2/A3/A4 increment.
- `...R10.tex`: LaTeX assembly wrapper that reuses the complete R9 cumulative PDF and appends G7.

The Mermaid files remain the semantic/topological graph sources and the reproducible basis for subsequent incremental edits. Visual containment represents the accepted `hasPart` view; explicit labeled edges represent other BA operators. Dashed amber cards remain documentation-only BA-pending elements for FR-C6-01-03B/C.

G7 does not invent concrete local cache paths for Qwen2, MiniLM or BioMistral: all three destination locators remain `NOT SPECIFIED`. Authority-boundary and integrity-verification analysis remain open. The A1 relation between `EfficientNet-B4` and `EfficientNetB4WeightsArtifact` also remains outside this graph pass.
