# DDTA R25 — DermaTriage Base Analysis Consolidation R5

**Checkpoint role:** additive closure of the `MR-01` holdout branch.  
**Methodology state:** BA0–BA6 remain frozen.  
**Method changes authorized:** `NONE`.

## Continuation baseline

- Repository: `nballestriero/documentation-driven-threat-analysis`
- Exact predecessor commit: `7284c8ea7f9f5c4ef5e40527779fcc2fb81eaa9b`
- Immutable predecessor checkpoint: `DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R4`
- Governed authority: `DERMATRIAGE-GOV-R1`
- Governed source: `governed-corpora/dermatriage/current-r1/DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex`

## Newly consolidated source

- `FR-22 — Diagnosi integrata B4 tramite POST /diagnose`

With FR-22, all governed MR-01 child elements selected for the holdout have now been
analyzed:

```text
DEC-12 -> FR-16, FR-17, FR-18, FR-19
DEC-13 -> FR-20
DEC-14 -> FR-21, FR-22
DEC-01 -> FR-01
DEC-02 -> FR-02
```

## R5 main findings

- `consumeService` changes from `NOT_TESTED` to `TESTED_POSITIVE`.
- B4 service consumption and B4 -> DermaTriage data transfer are distinct accepted
  meanings.
- `B4IntegratedTriagePath` and `POST /diagnose` become `WORKING_ACCEPTED`.
- `B4DermaTriageBoundary` gains strong identity evidence.
- `P-03` remains open because endpoint -> invoked-process semantics repeat at both
  `/analyze` and `/diagnose`.
- `P-04` is strengthened because a governed transfer crosses a known B4/DermaTriage
  boundary but current BA2 cannot bind that boundary to the transfer.
- `P-07` remains important, but FR-22 contributes primarily a documentation gap
  because the detailed request/data contract is not governed.
- `D-12 — B4 Diagnose Data Contract Completeness` is added.
- `R-07 — B4 Exchange Data Identity Alignment` is added.
- `O-03 — Data Interaction Completeness` is further confirmed.
- No security/authentication semantics are inferred from FR-22; later dedicated
  documentation must be analyzed before such meaning is accepted.

## Effective state

```text
R1 + R2 + R3 + R4 + R5
```

## Next bounded source element

`MR-02 — Indirizzamento specialistico`

Stop after MR-02 for review.
