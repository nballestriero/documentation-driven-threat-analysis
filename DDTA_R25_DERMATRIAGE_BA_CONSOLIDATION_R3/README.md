# DDTA R25 — DermaTriage Base Analysis Consolidation R3

This is an **additive successor checkpoint** to `DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R2`.

## Pinned continuation baseline

- Repository: `nballestriero/documentation-driven-threat-analysis`
- Exact baseline: `43af852f5faa4e4585a39b14ee5be46dcd09ca9d`
- Governed authority: `DERMATRIAGE-GOV-R1`
- Governed source: `governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`

## Newly consolidated source elements

- `FR-16` — image-based urgency classification with EfficientNet-B4
- `FR-17` — clinical-description production with Qwen2-VL-7B-Instruct

## Effective state

```text
R1
+
R2
+
R3 semantic delta
+
R3 pressure / gap / projection-candidate registers
```

Earlier checkpoints remain immutable.

## Main R3 conclusions

- `realize` receives its first positive DermaTriage test.
- `ImageBasedUrgencyClassificationCapability` is strengthened to working-accepted identity.
- `Confidence` is strengthened as an independently reusable BAReferent.
- the earlier `actor -> EfficientNet-B4` production shape is refined in the effective view to:
  - capability as `produce.actor`;
  - `EfficientNet-B4` as concrete realization of that capability.
- `P-01` is **narrowed**, not confirmed as a generic BA2 gap.
- `P-06` is strengthened by FR-16.
- `P-07 — STRUCTURED DATA / INFORMATION CONTRACT` becomes an open holdout pressure,
  supported by FR-16 and FR-17.
- no `correlate` workaround is accepted for literal `includes` / required-field semantics.
- a BA4 projection idea is recorded: `Data Contract Flow View`.
- the `0.25` HIGH threshold remains source-observed but semantically insufficient for a
  `decisionRule`.

## Methodology freeze

No file in this package modifies BA0–BA6.
No R3 pressure authorizes a methodology change.

## Next bounded source element

`FR-18 — Retrieval di casi storici con ChromaDB e all-MiniLM-L6-v2`
