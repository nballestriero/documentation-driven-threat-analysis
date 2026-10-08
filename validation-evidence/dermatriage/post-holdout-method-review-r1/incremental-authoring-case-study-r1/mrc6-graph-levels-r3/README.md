# MR-C6 graph levels G0/G1/G2/G3 - repository review R3

This folder preserves the accepted deterministic BA projection through FR-C6-01-02.

- `MRC6_G0_R2.mmd`: accepted top-level MR-C6 / DEC-C6-01 semantics.
- `MRC6_G1_R2.mmd`: G0 plus direct MR-C6 `hasPart` environment composition.
- `MRC6_G2_R2.mmd`: G1 plus accepted named hardware configuration `constrain`.
- `MRC6_G3_R6.mmd`: G2 plus FR-C6-01-02 named software-dependency `constrain` and accepted `realize` from `SCP-C6-01-02 / requirements.txt` to `RequiredSoftwareDependencies`.
- `DDTA_R25_DERMATRIAGE_MRC6_GRAPH_LEVELS_G0_G1_G2_G3_MERMAID_R6.pdf`: reviewed four-page oversized vector projection (590 x 350 mm).
- `MRC6_G*_R6_review_page.pdf`: page snapshots extracted from that reviewed vector PDF.
- `...R6.tex`: LaTeX assembly wrapper for the reviewed vector page snapshots.

The Mermaid files are the semantic/topological graph sources. Every visible semantic edge in G3 is backed by an accepted BAProposition. The LaTeX wrapper is an assembly artifact for the reviewed rendering; it does not introduce graph semantics.

G0-G2 are intentionally reused unchanged from the previously accepted R2 source. The former candidate `EnvironmentSetupProcedure dependOn ComputeResources/StorageResources` edges remain absent. No `currentImplementationOf` or ad-hoc specialization operator is introduced: FR-C6-01-02 uses the existing BA operators `constrain` and `realize`.
