# R42 drop-in instructions

This package is additive and targets exact Git HEAD:

`bea1e6567d3f861294378b201648b0853b3c8a43`

It intentionally does **not** require a clean working tree because the earlier R38 candidate package may already exist locally as untracked review material. Safety is provided by exact-HEAD verification plus a collision check for every R42 destination path.

Recommended application:

1. extract the ZIP to a temporary directory;
2. run `DDTA_R25_BASE_ANALYSIS_GUIDES_CONSOLIDATION_R42/APPLY_DROPIN.ps1 -Repo C:\Users\user\Documents\TESI`;
3. verify `R42 MANIFEST: ALL FILES OK`;
4. run `git status --short` and `git diff --check`;
5. review both PDFs before staging or committing.

Do not apply R39, R40 or R41 after R42. Their useful content is consolidated here.
