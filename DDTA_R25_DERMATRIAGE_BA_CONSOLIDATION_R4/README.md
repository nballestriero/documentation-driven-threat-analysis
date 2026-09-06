# DDTA R25 — DermaTriage Base Analysis Consolidation R4

Additive successor to `DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R3`.

- Repository: `nballestriero/documentation-driven-threat-analysis`
- Exact continuation baseline: `caf02332900997f7081d8426b3999a50e2d80638`
- Governed authority: `DERMATRIAGE-GOV-R1`
- Governed source: `governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`
- Newly consolidated: `FR-18`, `FR-19`, `FR-20`, `FR-21`
- Next bounded source element: `FR-22`

Effective state:

```text
R1 + R2 + R3 + R4 semantic delta + R4 pressure/gap/observation registers
```

Previous checkpoints remain immutable. BA0–BA6 remain frozen.

Main R4 findings:

- `observe` is positively tested by FR-18 but exposes parameterized-query role pressure.
- `realize` gains additional positive evidence at FR-18, FR-20 and FR-21.
- P-01 is decomposed: capability subcase mostly representable; process subcase remains open.
- P-02 is partially narrowed by producer/input data dependency.
- P-03 is partially narrowed by `realize(DirectTriagePath, POST /analyze)`.
- P-07 remains open for field/component contracts but narrows for scalar/cardinality/config constraints.
- P-08 `DATA ARTIFACT / STORE ASSOCIATION` is added.
- O-03 `DATA INTERACTION COMPLETENESS` is strongly supported as a documentation-guide candidate.
- D-07 through D-11 are added.
