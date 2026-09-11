# DDTA R25 — Review Coverage Matrix R1

## Status

`REALIGNMENT EVIDENCE / NON-NORMATIVE / SUPERSEDES NONE`

Repository baseline:

```text
6e6ec547d2def68833547cc7a5848835d6948b43
```

Purpose: account explicitly for stable authority, R25 control-cycle evidence, the complete governed
DermaTriage source and the post-R36 PR-13 reconstruction before any normative consolidation.

The previously generated condensed off-repository R4/R6/integration drafts are excluded from the
authority chain because they were not cumulative enough.

## 1. Stable authority coverage

| Artifact | Authority | R37 handling |
|---|---|---|
| `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5.tex` | current Documentation BA authoring authority | preserve; future successor must be cumulative |
| `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3.tex` | current BA operational authority | preserve; 14-operator basis remains frozen |
| `DDTA_METHODOLOGY_GUIDE_STYLE_R1.sty` | current shared methodology style | preserve formatting conventions when authoring later |
| `DDTA_DERMATRIAGE_GOVERNED_DOCUMENTATION_R1.tex` | current governed project source | source-complete review target |

## 2. Current R25 execution-state coverage

| Artifact / area | R37 use |
|---|---|
| Work Plan R8 | execution discipline; formal gates; next review lineage |
| Operator/Pressure Ledger R22 | frozen 14 operators; PR/CC/CL/CMD state |
| Candidate Construct Disposition Matrix R5 | current cross-pressure/candidate disposition |
| CC-04 question pack + PR-03/PR-10 reconciliation | initiation/invocation/trigger boundary |
| all operator-specific question packs | diagnostic/boundary evidence, not project truth |
| semantic-family/general discovery packs | source-complete routing discipline |
| accepted working findings | evidence for boundary/delta destination decisions |
| governed source gap table | documentation-remediation input; never silently filled |

## 3. Construct-specific review aids accounted

| Review aid | Core distinction to preserve | Gate destination |
|---|---|---|
| General semantic discovery | discover meaning before choosing operator | classify |
| `produce` | output/result vs create/read/transfer/store/select | classify |
| `create` | new semantic identity/occurrence | classify |
| `transfer` | governed content conveyance + optional governed interaction facets | classify |
| `observe` | explicit existing-state read/query | classify |
| `transition` | same-identity lifecycle/state change | classify |
| `correlate` | same-context binding | classify |
| `reference` | directional target identity, not generic fallback | classify |
| `dependOn` | prerequisite, not mere ordering | classify |
| `consumeService` | actual service/capability use | classify |
| `realize` | abstract-to-concrete materialization, not execution substitute | classify |
| `assignResponsibility` | governance relation, distinct from technical roles | classify |
| `constrain` | reusable/queryable restriction | classify |
| `classify` | semantic kind/category | classify |
| `decisionRule` | condition/input -> governed result | classify |
| PR-01 `perform?` | execution pressure; irreducibility not demonstrated | evidence/reopen decision |
| flow/consumption family | distinguish service/data/endpoint/store/flow | classify |
| CC-01 `consumeData` | redundant for current non-destructive data-use cases | evidence |
| CC-02 `provideService` | surviving provider/service relation | admission/destination decision |
| CC-03 `storedIn` | surviving at-rest association | admission/destination decision |
| CC-04 `initiate` | surviving directed initiation relation | admission/destination decision |
| PR-13 selection reconstruction | criterion/order/bound/membership/use decomposition | destination decision |

## 4. Pressure/candidate coverage

| ID | Topic | Current state preserved by R37 |
|---|---|---|
| PR-01 | function/process/behavior identity / `perform?` | `PRESSURE_RETAINED` |
| PR-02 | pipeline composition/order | `OPEN` |
| PR-03 | interface/path/invocation | `RECONCILED / CC-04` |
| PR-04 | boundary/interaction association | `OPEN` |
| PR-05 | ordered comparison vocabulary | `ROUTE_CL01` |
| PR-06 | scalar/property comparison | `ROUTE_CL01` |
| PR-07 | structured information contract | `OPEN` |
| PR-08 | at-rest storage association | `RECONCILED / CC-03` |
| PR-09 | acquisition/refresh | `OPEN` |
| PR-10 | conditional action trigger | `RECONCILED / CC-04 + CONDITION` |
| PR-11 | data/evidence consumption | `RECONCILED` |
| PR-12 | negative implication/non-sufficiency | `OPEN` |
| PR-13 | bounded/ranked/recency selection | `REUSABLE_SELECTION_STRUCTURE / NON-NORMATIVE` |
| PR-14 | applicability/configuration binding | `OPEN` |
| CC-01 | `consumeData` | `REJECT_REDUNDANT` |
| CC-02 | `provideService` | `TESTED_POSITIVE / NOT_ADMITTED` |
| CC-03 | `storedIn` | `TESTED_POSITIVE / NOT_ADMITTED` |
| CC-04 | `initiate` | `TESTED_POSITIVE / NOT_ADMITTED` |
| CMD-OP04 | remove `observe.result` | `DEFERRED` |
| CMD-OP05 | transition state/value refinement | `DEFERRED` |
| OBS-OT-01 | operation-target/effect-scope | `LEVEL_UNRESOLVED` |

## 5. Condition-language coverage

| ID | Current R25 state |
|---|---|
| CL-01 `comparison` | strong ordered/scalar pressure; current equality-style vocabulary insufficient |
| CL-02 `satisfies` | source relevance positive; formal closure pending |
| CL-03 `allOf` | strong conjunction evidence; formal closure pending |
| CL-04 `anyOf` | not sufficiently tested |
| CL-05 `not` | clean positive control not established; avoid false positives from `agrees == False` and non-sufficiency |

## 6. DermaTriage source-element index

The source-complete gate must produce a semantic/disposition row for every active FR below.

| FR | Governed area | R37 review focus |
|---|---|---|
| FR-16 | image urgency classification | produce/classify/constrain/realize-vs-execute |
| FR-17 | clinical description | produce/realize-vs-execute |
| FR-18 | historical retrieval | produce/observe/selection/correlate/technology/store boundaries |
| FR-19 | multi-source synthesis | produce/correlate/input provenance |
| FR-20 | baseline training/checkpoint | produce/config constraint/selection/comparison |
| FR-21 | direct `/analyze` | provideService candidate/initiate/exposure boundaries |
| FR-22 | B4 integrated diagnosis | consumeService/transfer/correlate/responsibility boundary |
| FR-01 | no-image urgency | conditional behavior/produce/input contract gap |
| FR-02 | P-scale priority | decisionRule/comparison/domain constraint |
| FR-03 | clinical review registration | correlate/reference/record-storage boundary |
| FR-12 | confirmation vs correction | classify/review semantics |
| FR-23 | B4 validation exchange | transfer/correlate/write-back vs storage |
| FR-24 | X-API-Key admin operations | constrain/auth applicability |
| FR-25 | bearer JWT B4 interaction | constrain/auth/invocation target under-governance |
| FR-04 | prompt evolution threshold | initiate + condition; trigger distinction |
| FR-05 | classifier adaptation threshold | initiate + condition; trigger distinction |
| FR-13 | activation-path independence | negative non-sufficiency |
| FR-14 | evidence-path independence | negative non-sufficiency |
| FR-15 | lifecycle-result independence | negative non-sufficiency/lifecycle boundary |
| FR-09 | candidate qualification | decisionRule/comparison/allOf/applicability |
| FR-10 | revocation/restoration | transition/reference/version selection/automaticity gap |
| FR-06 | recent prompt evidence | selection/recency/bound/gap preservation |
| FR-07 | classifier qualifying evidence | classification/condition/applicability |
| FR-08 | supervision target | decisionRule/classify/input-gap preservation |
| FR-26 | prompt versioning/persistence | storedIn candidate/transition/realize boundaries |
| FR-27 | incremental retraining | produce/execute/constraint/operation-target pressure |

Historical source identity:

```text
FR-11
    SUPERSEDED
    must not be silently treated as active authority
```

## 7. Explicit documentation-gap coverage

Every row below must remain a project-documentation issue unless later source authority resolves it.

| Gap | Area | Preserved issue |
|---|---|---|
| Diagnostic authority boundary | framing / MR-01 | definitive diagnosis authority not established |
| `GAP-DERMA-NOIMAGE-INPUT-01` | FR-01 | required/optional symptom inputs and missing-value semantics |
| `GAP-DERMA-PMAP-INPUT-01` | FR-02 | complete urgency/confidence input semantics |
| `GAP-DERMA-NOIMAGE-PMAP-BINDING-01` | MR-01 | no-image output -> P-scale input completeness |
| `GAP-DERMA-SLA-01` | MR-01 downstream | SLA values lack sufficient trigger/outcome/owner/normative binding |
| `GAP-DERMA-PATH-01` | MR-01 downstream | `predicted_pathology` obligation/authority boundary |
| Specialist selection semantics | MR-02 | selection vocabulary/rule/input/fallback/booking unresolved |
| `GAP-DERMA-REVIEW-CONTENT-01` | FR-03/FR-12 | complete review/correction content model |
| `GAP-DERMA-REVIEW-LIFECYCLE-01` | FR-03/FR-12 | overwrite/history/retention/finality |
| `GAP-DERMA-REVIEW-DISAGREEMENT-BINDING-01` | MR-03/MR-04 | correction/disagreement/`agrees` normative binding |
| `GAP-DERMA-ADAPT-COUNTING-01` | FR-04/FR-05 | reset/dedup/reuse/persistence/multiple reviews/concurrency |
| `GAP-DERMA-ADAPT-THRESHOLD-AUTH-01` | FR-04/FR-05 | threshold authority and exact normative status |
| `GAP-DERMA-PROMPT-WINDOW-01` | FR-06 | ordering/membership/underfill/dedup/reuse/overlap/scope |
| `GAP-DERMA-SUPERVISION-INPUT-01` | FR-08 | missing/invalid/out-of-domain/conflicting corrected priority |
| `GAP-DERMA-DEPLOY-01` | FR-09 lifecycle | deployment authority and automaticity |
| `GAP-DERMA-ACCEPT-BINDING-01` | DEC-06/DEC-07 | quantitative acceptance/reference/population/5% binding |
| `GAP-DERMA-ROLLBACK-BINDING-01` | DEC-08/FR-10 | rollback unit/reference/population/window/timing/automaticity/authorization/target |
| `GAP-DERMA-EVAL-CONSISTENCY-01` | FR-09/DEC-07 | HIGH sensitivity/recall/correct-count relationship unexplained |

## 8. Missing step before guide authoring

Current coverage is **indexed**, not yet fully dispositioned.

The missing work is the R37 gate:

```text
for each row:
    source-grounded semantic reconstruction
    candidate/rejected routing
    documentation QA
    pressure classification
    primary destination
```

Only after those destination decisions can a cumulative guide rewrite be justified.

## 9. Current matrix state

```text
STABLE_AUTHORITY_INDEXED = YES
R25_EVIDENCE_INDEXED = YES
26_ACTIVE_FR_INDEXED = YES
FR11_SUPERSEDED_HANDLED = YES
SOURCE_GAPS_INDEXED = YES
PR13_RECONSTRUCTED = YES
PER_ROW_DESTINATION_CLASSIFICATION = PENDING
GUIDE_DELTA_DECISION = PENDING
READY_FOR_NORMATIVE_CONSOLIDATION = NO
```
