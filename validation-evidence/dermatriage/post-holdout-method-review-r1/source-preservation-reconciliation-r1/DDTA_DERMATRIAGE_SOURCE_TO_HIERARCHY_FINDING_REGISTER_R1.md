# DDTA DermaTriage - Source-to-Hierarchy Finding Register R1

**Execution baseline used to create this register:** `3d1cd23`
**Status:** WORKING AUDIT / NOT PROJECT AUTHORITY / NOT BA AUTHORITY
**Controlled by:** `methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R6.md`

## 1. Purpose

This register gives stable working IDs to findings raised by the two independent audits and the internal source-first audit. It does not accept a finding by majority vote and it does not authorize a documentation or Base Analysis correction by itself.

For project facts, the six authorized original DermaTriage documents remain the sole authority. Every source-supported finding must be reconstructed through the governed DDTA hierarchy before BA is re-run:

```text
ORIGINAL SOURCE
    -> MacroRequirement owner
        -> Decision owner, only when justified
            -> FunctionalRequirement owner, only when justified
                -> Base Analysis, only after documentation closure
```

There is no direct `SOURCE -> BA` correction path.

A technical/configuration/test fact may remain non-normative, but it must still be anchored inside the correct MR / Decision / FR branch as current realization, evidence/reference material, or an explicit source gap. A separate evidence label does not replace hierarchical ownership.

## 2. Per-finding analysis record

Each finding is closed one at a time using this exact record:

```text
Finding ID:
Original source locator:
Minimal source-supported meaning:
Source ambiguity / conflict:

Candidate MR owner:
MR ownership rationale:
MR action: REUSE | REWORK | SPLIT | MERGE | NEW CANDIDATE | HOLD

Candidate Decision owner:
Decision rationale:
Decision action: REUSE | REWORK | MERGE | SPLIT | NEW CANDIDATE | NOT REQUIRED | HOLD

Candidate FR owner:
Operational behavior:
FR action: REUSE | REWORK | MERGE | SPLIT | NEW CANDIDATE | NOT REQUIRED | HOLD

Placement of realization/evidence/binding inside the branch:
Remaining NOT SPECIFIED / source gaps:
Documentation correction authorized: YES | NO

BA status: NOT ANALYZED UNTIL DOCUMENTATION CLOSED
```

## 3. Finding inventory and order

| ID | Finding | Original-source anchor | Current/candidate hierarchy | Working status | Immediate next check |
|---|---|---|---|---|---|
| `RC-001` | Automatic rollback >5% | OR2 Architecture §4.2; OR4 Training Cycles | MR-04 → DEC-08 → FR-10 | **SOURCE-CONFIRMED / OWNER-CHAIN TO REVALIDATE** | Re-read source in context; confirm/rework existing branch before any BA. |
| `RC-002` | Stage-4 JSON output contract: recommended_action + naming divergence | OR2 Architecture Stage 4; OR5 Stage 4 tests | MR-01 → DEC-MR01-03 → FR-MR01-03-04 | **SOURCE-CONFIRMED / OWNER-CHAIN TO REVALIDATE** | Reconstruct complete Stage-4 contract from both originals; preserve source disagreement explicitly. |
| `RC-003` | P1-P4 SLA 24h/48h/72h/7d | OR2 Architecture adaptation mapping | MR/Decision/FR owner NOT YET CLOSED | **SOURCE-CONFIRMED / OWNER OPEN** | Determine macro responsibility first; do not attach SLA to nearest existing branch by convenience. |
| `RC-004` | Baseline classifier absolute quality gates | OR2 Model Test Report; OR5 acceptance criteria | Likely MR-01 / Stage-1 branch; exact Decision/FR owner open | **SOURCE-CONFIRMED / OWNER OPEN** | Keep distinct from MR-04 comparative retraining gate; decide exact hierarchy from source meaning. |
| `RC-005` | Classifier-retraining fine-tune parameters | OR2 Architecture §4.2; OR4 Training Cycles §3.3 | MR-04 classifier-adaptation branch; Decision/FR owner open | **SOURCE-CONFIRMED / OWNER OPEN** | Preserve within correct hierarchy as normative or current realization only after source-level classification. |
| `RC-006` | Case intake: image + age + sex + localization | OR2 Architecture pipeline flow step 1 | MR-01; Decision/FR owner open | **SOURCE-CONFIRMED / OWNER OPEN** | Reconstruct case/input contract; do not infer these are symptom-only scoring inputs. |
| `RC-007` | Baseline initial-training realization | OR2 Model Test Report; OR3; training documentation | MR-01; exact Decision/FR owner open | **SOURCE-CONFIRMED / OWNER OPEN** | Preserve baseline-training lineage separately from feedback retraining inside the correct MR/Decision/FR branch. |
| `RC-008` | Prompt trigger semantics: 'Every 10 corrections' vs 'reaches 10' | OR2 Architecture prompt evolution | MR-04 → DEC-04 → FR-04 | **SOURCE-CONFIRMED / OWNER-CHAIN TO REVALIDATE** | Resolve recurrence semantics from original wording before BA. |
| `RC-009` | Prompt-evidence qualifier 'pertinent' | OR2/OR4 prompt-evolution wording | MR-04 → DEC-09 → FR-06 | **SOURCE-OVERSTATEMENT CANDIDATE** | Verify whether any original establishes pertinence; otherwise remove/downgrade before selection review. |
| `RC-010` | HistoricalCaseRetrieval vs HistoricalCaseSimilarityRetrieval identity | Corrected MR-01/Stage-3 documentation after Phase A | MR-01 → DEC-MR01-03 → FR-MR01-03-03B | **BA IDENTITY REVIEW DEFERRED** | Do not merge/remove until source-closed Stage-3 documentation is available. |
| `RC-011` | ClinicalReviewDisposition independent BA identity | Corrected MR-03/FR-12 documentation after Phase A | MR-03 → DEC-03 → FR-12 | **BA IDENTITY REVIEW DEFERRED** | After FR-12 source closure, decide whether independent BAReferent identity is justified. |
| `RC-012` | ClinicianDisagreement vs agrees == False | OR4 retraining semantics + corrected MR-03/MR-04 branches | Cross-branch owner to revalidate; FR-07 currently involved | **SOURCE + BA IDENTITY RECHECK** | First establish governed documentation meaning; only then decide BA identity/granularity. |
| `RC-013` | B4 bearer-JWT endpoint/source binding | OR2 B4 endpoint table | MR-03 → DEC-16 → FR-25 | **SOURCE-CONFIRMED / BINDING OWNER-CHAIN TO REVALIDATE** | Preserve documented token endpoint in FR-25 branch; BA transfer source remains a later question. |
| `RC-014` | Accepted BA graph count/components | Accepted BA after all upstream corrections | Not a documentation owner | **POST-BA DIAGNOSTIC** | Current 19-component result at 3d1cd23 is diagnostic only; recompute deterministically after BA rerun. |
| `RC-015` | Information/data-contract construct sufficiency | Source-closed contract-bearing FRs | Method Phase C | **METHOD DEFERRED** | No generic contract operator; reassess only after corrected contracts and BA. |
| `RC-016` | selection construct pressure | Source-closed FR-06/FR-07 and other recurrent cases | Method Phase C | **METHOD DEFERRED** | Rebuild evidence set after RC-009/RC-012; do not freeze signature yet. |
| `RC-017` | decisionRule relocation | Source-closed mapping FRs | Method Phase C | **METHOD DEFERRED** | Keep candidate/not admitted until corrections + cross-corpus regression. |
| `RC-018` | MR-02 specialist boundary vs SLA meaning | OR2/OR3/OR5 | MR-02 plus separate owner review for SLA | **SOURCE OWNER REVIEW** | Keep specialist destination distinct from SLA; do not invent routing/vocabulary/booking. |
| `RC-019` | Privacy / anonymization / in-memory upload facts | Original privacy/data sources | MR/Decision/FR owner NOT YET CLOSED | **SOURCE OWNER / CLASSIFICATION REVIEW** | First find hierarchy owner; only afterward decide whether security specialization is justified. |
| `RC-020` | FR-13/14/15 non-propagation family | Original adaptation-loop semantics | MR-04 → DEC-05 → FR-13/14/15 | **SOURCE-STRENGTH + DOWNSTREAM-UTILITY REVIEW** | Re-test source support and branch autonomy after primary source-preservation corrections. |

## 4. Execution sequence

### A. Source-to-hierarchy reconstruction

Analyze first: `RC-001` through `RC-009`, then `RC-013`, `RC-018`, `RC-019`, `RC-020`.

These rows can change MR/Decision/FR meaning and therefore must be resolved before BA identity or graph corrections.

### B. BA identity and graph

After the affected documentation branches are source-closed, analyze `RC-010`, `RC-011`, `RC-012` and then recompute `RC-014` from the accepted BA register.

The current graph result at execution baseline `3d1cd23` is only a diagnostic checkpoint and must not be treated as a target topology.

### C. Method consolidation

Only after A and B: `RC-015`, `RC-016`, `RC-017`.

No new operator/construct may be admitted merely to connect the graph or preserve a finding that belongs upstream in documentation.

## 5. Analyst reports

The independent/internal audit reports are discovery and regression evidence only. Agreement between reports increases review priority but does not establish project truth. Disagreement is resolved by reopening the original source and reconstructing the semantic owner.

## 6. Closure rule

A finding may be marked `CLOSED` only when:

- its original-source meaning has been re-read in context;
- its MR owner is decided;
- any Decision/FR ownership is decided without structural filling;
- realization/evidence details are preserved inside that branch without accidental normative promotion;
- open source gaps remain explicit;
- the corrected documentation branch has passed its family regression;
- affected BA has been reconstructed from that corrected documentation.
