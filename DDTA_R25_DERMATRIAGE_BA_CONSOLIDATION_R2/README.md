# DDTA R25 — DermaTriage Base Analysis Consolidation R2

This is an **additive successor checkpoint** to `DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R1`.

## Pinned continuation baseline

- Repository: `nballestriero/documentation-driven-threat-analysis`
- Exact baseline: `9fd218803abdd812245b8ac27116a9fa2fa08ecb`
- Governed authority: `DERMATRIAGE-GOV-R1`
- Governed source: `governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`

## Newly consolidated source elements

- `DEC-01`
- `FR-01`
- `DEC-02`
- `FR-02`

## Effective state

```text
R1 working snapshot
+
R2 semantic delta
+
R2 pressure/documentation-gap register
```

R1 remains immutable. R2 does not rewrite it.

## New empirical conclusions

- no-image triage is representable with positive condition-scoped propositions;
- a negative `dependOn` on image is not required;
- `decisionRule` is empirically necessary for the P-scale mapping;
- `allOf` / `anyOf` / `not` already provide AND / OR / NOT;
- `notEquals` already covers `!=`;
- `greaterThan (>)` is empirically required but missing from BA2 R3;
- `<`, `>=`, `<=` are review candidates only, not yet empirically required;
- mandatory `comparison.property` may be too restrictive for direct scalar comparison such as `confidence > 0.85`.

## Frozen-method rule

No finding in this checkpoint authorizes a BA0–BA6 modification. Methodology changes
remain deferred until the governed DermaTriage corpus has been analyzed.

## Next bounded element

`FR-16 — Classificazione image-based di urgenza con EfficientNet-B4`
