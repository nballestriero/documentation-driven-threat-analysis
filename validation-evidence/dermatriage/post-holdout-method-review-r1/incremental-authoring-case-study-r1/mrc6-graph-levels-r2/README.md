# MR-C6 graph levels G0/G1/G2 - Mermaid R2

Review artifact for the deterministic MR-C6 projection.

- `MRC6_G0_R2.mmd`: top-level accepted BA (`produce`, `realize`, `dependOn`).
- `MRC6_G1_R2.mmd`: G0 + direct MR-level `hasPart` composition.
- `MRC6_G2_R2.mmd`: G1 + accepted named hardware configuration `constrain`.
- `*_mermaid_render.pdf`: deterministic vector render used by the LaTeX wrapper.
- `DDTA_R25_DERMATRIAGE_MRC6_GRAPH_LEVELS_G0_G1_G2_MERMAID_R2.tex/.pdf`: one oversized page per graph (590 x 350 mm), intended to remain extensible.

The two former working candidate `dependOn` edges from `EnvironmentSetupProcedure` to compute/storage resources are intentionally absent. No `apply` or `load` relation is inferred between the setup procedure and `HardwareConfigurationProfile`.
