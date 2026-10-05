# DDTA DermaTriage - Source-to-Hierarchy Finding Register R1

**Execution baseline used to create this register:** `3d1cd23`
**Status:** WORKING AUDIT / NOT PROJECT AUTHORITY / NOT BA AUTHORITY
**Controlled by:** `methodology/DDTA_R25_BASE_ANALYSIS_GUIDE_REBUILD_WORK_PLAN_R7.md`

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
| `RC-001` | Automatic rollback >5% | OR2 Architecture §4.2; OR4 Training Cycles | MR-04 → DEC-08 → FR-10 | **CLOSED** | Source/hierarchy, corrected documentation and affected BA are closed for this checkpoint. Reopen only if upstream authority/evidence changes invalidate the disposition. |
| `RC-002` | Stage-4 JSON output contract: recommended_action + naming divergence | OR2 Architecture Stage 4; OR5 Stage 4 tests | Runtime owner hint: MR-01 → DEC-MR01-03 → FR-MR01-03-04; verification owner under RC-021 review | **SOURCE-CONFIRMED / OWNER-CHAIN TO REVALIDATE / PAUSED FOR RC-021** | Resume after the MR-family review; distinguish runtime Stage-4 semantics from the OR5 verification oracle before any documentation correction. |
| `RC-003` | P1-P4 SLA 24h/48h/72h/7d | OR2 Architecture adaptation mapping | MR/Decision/FR owner NOT YET CLOSED | **SOURCE-CONFIRMED / OWNER OPEN** | Determine macro responsibility first; do not attach SLA to nearest existing branch by convenience. |
| `RC-004` | Baseline classifier absolute quality gates | OR2 Model Test Report; OR5 acceptance criteria | Likely MR-01 / Stage-1 branch; exact Decision/FR owner open | **SOURCE-CONFIRMED / OWNER OPEN** | Keep distinct from MR-04 comparative retraining gate; decide exact hierarchy from source meaning. |
| `RC-005` | Classifier-retraining fine-tune parameters | OR2 Architecture §4.2; OR4 Training Cycles §3.3 | MR-04 classifier-adaptation branch; Decision/FR owner open | **SOURCE-CONFIRMED / OWNER OPEN** | Preserve within correct hierarchy as normative or current realization only after source-level classification. |
| `RC-006` | Case intake: image + age + sex + localization | OR2 Architecture pipeline flow step 1 | MR-01; Decision/FR owner open | **SOURCE-CONFIRMED / OWNER OPEN** | Reconstruct case/input contract; do not infer these are symptom-only scoring inputs. |
| `RC-007` | Baseline initial-training realization | OR2 Model Test Report; OR3; training documentation | MR-01; exact Decision/FR owner open | **SOURCE-CONFIRMED / OWNER OPEN** | Preserve baseline-training lineage separately from feedback retraining inside the correct MR/Decision/FR branch. |
| `RC-008` | Prompt trigger semantics: 'Every 10 corrections' vs 'reaches 10' | OR2 Architecture prompt evolution | MR-04 → DEC-04 → FR-04 | **SOURCE-CONFIRMED / OWNER-CHAIN TO REVALIDATE** | Resolve recurrence semantics from original wording before BA. |
| `RC-009` | Prompt-evidence qualifier 'pertinent' | OR2/OR4 prompt-evolution wording | MR-04 → DEC-09 → FR-06 | **SOURCE-OVERSTATEMENT CANDIDATE** | Verify whether any original establishes pertinence; otherwise remove/downgrade before selection review. |
| `RC-010` | HistoricalCaseRetrieval vs HistoricalCaseSimilarityRetrieval identity | Corrected MR-01/Stage-3 documentation after Phase A | MR-01 → DEC-MR01-03 → FR-MR01-03-03 | **BA IDENTITY REVIEW DEFERRED** | Do not merge/remove until source-closed Stage-3 documentation is available. |
| `RC-011` | ClinicalReviewDisposition independent BA identity | Corrected MR-03/FR-12 documentation after Phase A | MR-03 → DEC-03 → FR-12 | **BA IDENTITY REVIEW DEFERRED** | After FR-12 source closure, decide whether independent BAReferent identity is justified. |
| `RC-012` | ClinicianDisagreement vs agrees == False | OR4 retraining semantics + corrected MR-03/MR-04 branches | Cross-branch owner to revalidate; FR-07 currently involved | **SOURCE + BA IDENTITY RECHECK** | First establish governed documentation meaning; only then decide BA identity/granularity. |
| `RC-013` | B4 bearer-JWT endpoint/source binding | OR2 B4 endpoint table | MR-03 → DEC-16 → FR-25 | **SOURCE-CONFIRMED / BINDING OWNER-CHAIN TO REVALIDATE** | Preserve documented token endpoint in FR-25 branch; BA transfer source remains a later question. |
| `RC-014` | Accepted BA graph count/components | Accepted BA after all upstream corrections | Not a documentation owner | **POST-BA DIAGNOSTIC** | Current 19-component result at 3d1cd23 is diagnostic only; recompute deterministically after BA rerun. |
| `RC-015` | Information/data-contract construct sufficiency | Source-closed contract-bearing FRs | Method Phase C | **METHOD DEFERRED** | No generic contract operator; reassess only after corrected contracts and BA. |
| `RC-016` | selection construct pressure | Source-closed FR-06/FR-07 and other recurrent cases | Method Phase C | **METHOD DEFERRED** | Rebuild evidence set after RC-009/RC-012; do not freeze signature yet. |
| `RC-017` | decisionRule relocation | Source-closed mapping FRs plus C7 verification-pressure cases | Method Phase C | **METHOD DEFERRED / C7 REVIEW PRESSURE RECORDED** | P-scale and readiness remain positive local-structure regressions. C7-P02 adds `lt`, governed-domain criterion reuse and governed-fact occurrence reuse. C7-P03..P07 add domain-validity, qualitative non-empty, `eq 5`, structured-content, completeness/timing and criterion-local outcome pressure; P06 shows observation-only verification without a documented pass condition, while P07 exposes a `gt`/`ge` source conflict. No new syntax/operator is admitted. Keep candidate/not admitted pending BA review, Facial Access cross-corpus regression + explicit checkpoint. |
| `RC-018` | MR-02 specialist boundary vs SLA meaning | OR2/OR3/OR5 | MR-02 plus separate owner review for SLA | **SOURCE OWNER REVIEW** | Keep specialist destination distinct from SLA; do not invent routing/vocabulary/booking. |
| `RC-019` | Privacy / anonymization / in-memory upload facts | Original privacy/data sources | MR/Decision/FR owner NOT YET CLOSED | **SOURCE OWNER / CLASSIFICATION REVIEW** | First find hierarchy owner; only afterward decide whether security specialization is justified. |
| `RC-020` | FR-13/14/15 non-propagation family | Original adaptation-loop semantics | MR-04 → DEC-05 → FR-13/14/15 | **SOURCE-STRENGTH + DOWNSTREAM-UTILITY REVIEW** | Re-test source support and branch autonomy after primary source-preservation corrections. |
| `RC-021` | Environment preparation vs verification/test macro-responsibility split pressure | OR4 Training Environment Configuration §§1-9; OR5 Test Environment Setup §§1-9 | MR-C6 → DEC-C6-01 → FR-C6-01-01 / FR-C6-01-02 / FR-C6-01-03 / FR-C6-01-04 / FR-C6-01-05 / FR-C6-01-06 approved/current; C6 decomposition complete; MR-C7 → DEC-C7-01 → FR-C7-01-01 / FR-C7-02-01 / FR-C7-02-02 approved/current; FR-C7-03-01..04 / FR-C7-04-01 / FR-C7-05-01 / FR-C7-06-01 / FR-C7-07-01 materialized as candidate/non-current review; MR-03 rework candidate; initial-training lifecycle kept separate but not promoted to MR | **C6 COMPLETE / C7 P03-P07 REVIEW MATERIALIZED / RC-021 OPEN** | Jointly review candidate BA and lifecycle-owner Mermaid projections, then apply explicit promote/rework/split gates. Keep verification ownership distinct from runtime/adaptation/quality ownership. Resume RC-002 only after this RC-021 review checkpoint is stable. |


### RC-021 opening record

```text
Finding ID:
RC-021

Original source locators:
OR4_Training_Environment_Config.pdf §§1-9
OR5_Test_Environment_Setup.pdf §§1-9

Minimal source-supported meaning:
The original corpus exposes a pre-use environment lifecycle with at least two
separable responsibility candidates.

Candidate A - environment preparation:
OR4 documents the environment required to train and run DermaTriage, including
resource prerequisites, software stack, model/resource acquisition, environment
configuration, directory/storage structure, installation, ChromaDB
initialization, server start and deployment verification.

Candidate B - verification/test:
OR5 documents setup and verification of the DermaTriage test environment and
defines endpoint tests, per-stage pipeline tests, full-pipeline tests, B4
integration tests, retraining tests, known limitations and acceptance criteria
with expected results/pass conditions.

Cross-source ownership pressure:
OR4 also contains deployment verification/health checks, while OR5's stated
purpose includes setup as well as verification. Therefore source-document
boundaries MUST NOT be treated as semantic-owner boundaries.

MR-family separation/classification checkpoint:
MR-01 triage evaluation -> KEEP.
MR-02 specialist-destination indication -> KEEP / STOP AT MR.
MR-03 clinical-review management -> KEEP with REWORK candidate.
MR-04 controlled continuous adaptation -> KEEP.
Initial training / baseline establishment -> preserve as a distinct lifecycle
meaning, but LOWER LEVEL for this checkpoint; do not merge it into MR-04.
Aggregate "environment setup + verification" -> SPLIT.

MR-C6 environment-preparation branch:
  title -> Predisposizione e inizializzazione dell'ambiente DermaTriage
  classification -> KEEP / APPROVED / CURRENT_GOVERNED
  approved Decision -> DEC-C6-01 Predisposizione dell'ambiente mediante una
  procedura esplicita di setup
  approved FR -> FR-C6-01-01 Predisposizione delle risorse di calcolo e storage
  dell'ambiente
  approved FR -> FR-C6-01-02 Predisposizione dello stack software e delle dipendenze
  approved FR -> FR-C6-01-03 Disponibilita' delle risorse di modello e dei dati
  approved FR -> FR-C6-01-04 Configurazione dei binding dell'ambiente e delle integrazioni
  approved FR -> FR-C6-01-05 Inizializzazione della base vettoriale dei casi storici
  approved FR -> FR-C6-01-06 Avvio del servizio API DermaTriage; C6 decomposition closed.
  Stage-3 ownership review -> temporary FR-MR01-03-03A/B split closed;
  offline historical-vector-base preparation -> FR-C6-01-05;
  runtime retrieval -> canonical FR-MR01-03-03.

MR-C7 verification branch:
  title -> Verifica del sistema DermaTriage
  classification -> KEEP / APPROVED / CURRENT_GOVERNED
  approved Decision -> DEC-C7-01 Verifica mediante controlli espliciti e criteri applicabili
  approved FR -> FR-C7-01-01 Verifica della readiness operativa del servizio DermaTriage
  approved FR -> FR-C7-02-01 Verifica dell'endpoint di analisi diretta DermaTriage
  approved FR -> FR-C7-02-02 Verifica dell'endpoint integrato B4 di DermaTriage
  candidate/non-current review FR -> FR-C7-03-01 / FR-C7-03-02 / FR-C7-03-03 / FR-C7-03-04
  for per-stage pipeline verification;
  candidate/non-current review FR -> FR-C7-04-01 full-pipeline end-to-end verification;
  candidate/non-current review FR -> FR-C7-05-01 aggregated B4 integration verification;
  candidate/non-current review FR -> FR-C7-06-01 retraining-control observation;
  candidate/non-current review FR -> FR-C7-07-01 baseline absolute-quality-gate verification.
  BA checkpoint -> DermaTriageVerification and DermaTriageVerificationProcedure accepted;
  ServiceReadinessVerification, ServiceHealthCheckResult and ReadinessOutcome accepted;
  DirectAnalysisEndpoint, DirectAnalysisEndpointVerification, DirectAnalysisEndpointObservation
  and DirectAnalysisEndpointVerificationOutcome accepted;
  B4IntegratedDiagnosisEndpoint, B4IntegratedDiagnosisEndpointVerification,
  B4IntegratedDiagnosisEndpointObservation and B4IntegratedDiagnosisEndpointVerificationOutcome accepted;
  BAP-DECC7-01-01 realize, BAP-FRC7-01-01-01 produce,
  BAP-FRC7-02-01-01 produce and BAP-FRC7-02-02-01 produce accepted.
  New C7-P03..P07 verification identities and produce propositions remain candidate/non-accepted;
  nested operatorStructure.decisionRule material remains candidate/non-admitted. The review records
  additional criterion-shape and source-conflict pressure without admitting new criterion syntax.

Documentation + BA checkpoint:
The existing DermaTriage case-study file now contains:
- the MR-03 rework candidate and proposal pages for missing clinical-review tooling;
- MR-C6 promoted to CURRENT_GOVERNED;
- DEC-C6-01 and FR-C6-01-01 through FR-C6-01-06 promoted to CURRENT_GOVERNED;
- accepted/candidate BA material for the approved C6 branch;
- the temporary FR-MR01-03-03A/B review split closed by relocating offline preparation to FR-C6-01-05 and restoring runtime retrieval to canonical FR-MR01-03-03;
- FR-C6-01-06 replacing the final residual C6-P06 worklist and closing the C6 decomposition;
- MR-C7 and DEC-C7-01 promoted to CURRENT_GOVERNED with parallel BA checkpoint;
- FR-C7-01-01 promoted to CURRENT_GOVERNED, closing C7-P01;
- FR-C7-02-01 and FR-C7-02-02 promoted to CURRENT_GOVERNED, closing the C7-P02 endpoint-verification placeholder by split;
- readiness and endpoint-verification BA accepted at produce level; nested decisionRule material remains candidate/non-admitted method evidence;
- C7-P03..P07 source-first reconstruction materialized as candidate/non-current FR pages with candidate BA and lifecycle-owner consolidation; no new FR or BA promotion is performed by this review checkpoint.

The environment-preparation owner and the verification owner are therefore no longer provisional at MR level.
MR-C7, DEC-C7-01, FR-C7-01-01, FR-C7-02-01 and FR-C7-02-02 have passed their gates; residual verification FR ownership is now explicitly reconstructed but remains candidate/non-current pending joint BA/graph review and explicit promotion/rework gates.
BA is no longer globally blocked for RC-021: inside an approved documentation branch
it is run immediately as a diagnostic representation check while documentation remains
the sole project authority.

Important non-inferences:
- do not infer that every OR4 fact belongs to Candidate A;
- do not infer that every OR5 fact belongs to Candidate B;
- do not infer "test passed -> runtime contract authority";
- do not infer a mandatory production/deployment gate before operational use;
- do not infer separate training and runtime environments unless a source closes
  that distinction;
- do not infer an `ELSE -> FAIL` branch from a positive pass condition alone;
- do not treat `/stats` or `/docs` as readiness/pass-fail criteria without an explicit criterion;
- do not promote `/analyze` test values `45`, `male`, `back` or `/diagnose` value `consulto_id=1` to endpoint requirements;
- do not turn `/analyze` expected fields `specialist`, `SLA` and `confidence` into pass criteria when the source only governs `<30s` plus valid P-scale;
- do not expand `valid P-scale value` into duplicated P1/P2/P3/P4 equality branches under C7 merely to encode the test oracle;
- do not normalize B4 write-back verification into an invented boolean such as `b4Write=true`, and do not duplicate the governed runtime transfer only because verification observes its occurrence;
- do not turn current authentication bindings into pass criteria unless the verification source governs them as criteria;
- do not create an MR merely because a lifecycle phase is security-relevant.

Security-analysis relevance:
Preparation and verification are security-relevant because changes introduced
during those phases may affect later runtime behavior. This motivates preserving
the source-supported lifecycle for downstream threat analysis, but it is NOT the
authority for creating either MR.

Immediate next action:
C7-P01 is closed by FR-C7-01-01 and C7-P02 is closed by the approved split into
FR-C7-02-01 and FR-C7-02-02. The C7-P03..P07 source-first reconstruction is now
materialized as candidate/non-current FR documentation and candidate BA. Jointly review
the candidate BA identities/propositions and lifecycle-owner Mermaid projections; then
apply explicit promote/rework/split gates. Keep test-oracle meaning distinct from the
runtime, adaptation or quality owner being verified. MR-C7, DEC-C7-01, FR-C7-01-01,
FR-C7-02-01 and FR-C7-02-02 remain current; the new C7-P03..P07 FRs are not current.

After this RC-021 candidate BA/graph review checkpoint is stable, resume RC-002 with
OR2 runtime Stage-4 semantics and OR5 Stage-4 verification expectations kept distinct.

Documentation correction authorized:
YES - MR-C6, DEC-C6-01 and FR-C6-01-01 through FR-C6-01-06 are approved/current for this checkpoint; the C6 decomposition is complete.
NO - no residual C6-Pxx candidate remains.
YES - MR-C7, DEC-C7-01, FR-C7-01-01, FR-C7-02-01 and FR-C7-02-02 are approved/current for this checkpoint; C7-P01 and C7-P02 are closed.
YES - C7-P03..P07 are materialized as review-only candidate FR documentation for joint BA/graph validation; this does not authorize promotion.

BA status:
MR-03 affected BA: REVALIDATION REQUIRED AFTER DOCUMENTATION CLOSURE.
MR-C6 approved branch: ANALYZED IN PARALLEL / COMPLETE FOR CURRENT C6 SCOPE.
MR-C7 approved branch: ACCEPTED BA THROUGH FR-C7-02-02; C7-P03..P07 CANDIDATE BA MATERIALIZED / NOT ACCEPTED.
RC-017 note: readiness remains the second independent DermaTriage regression case for nested decisionRule. C7-P02 adds `lt` plus governed-domain/governed-fact reuse pressure; C7-P03..P07 add further candidate criterion-shape and `gt`/`ge` conflict pressure. The structure remains candidate/non-admitted pending joint BA review, Facial Access regression and checkpoint.
```


### RC-001 closure record

```text
Finding ID:
RC-001

Original source locator:
OR2_Architecture_Document.pdf §4.2; OR4_Training_Cycles_Report.pdf

Minimal source-supported meaning:
An already-adopted classifier adaptation that exceeds the governed post-adoption
accuracy-degradation threshold requires automatic rollback/restore of a previous
acceptable classifier version/state. The rollback branch uses maintained version
payloads and maintained version-tracking information to identify and restore the
previous acceptable version/state.

Source ambiguity / conflict:
The 5% threshold is source-supported, but the source does not close whether this
means relative percent or percentage points. It does not name the concrete actor
that computes the post-adoption degradation, does not govern a complete ordering
or tie-break among multiple acceptable stored versions, and does not specify the
concrete filesystem restore mechanism or the fate of the replaced active model.

Candidate MR owner:
MR-04

MR ownership rationale:
Rollback is part of controlled adaptation lifecycle/recovery after adoption and
therefore belongs to the macro-responsibility for controlled adaptation rather
than baseline triage execution.

MR action:
REUSE

Candidate Decision owner:
DEC-08

Decision rationale:
DEC-08 owns the distinct post-adoption policy choice that material degradation
above the governed threshold activates the rollback/restore branch. The corrected
Decision keeps this post-adoption threshold semantically distinct from the
pre-adoption comparative-qualification tolerance.

Decision action:
REWORK

Candidate FR owner:
FR-10

Operational behavior:
When post-adoption accuracy degradation exceeds the governed threshold, execute
automatic rollback; use maintained version-tracking information to identify a
previous acceptable version/state, retrieve it from the maintained classifier
versions, and restore it as the active classifier.

FR action:
REWORK

Placement of realization/evidence/binding inside the branch:
models/versions/ -> ClassifierVersionStore / maintained restorable versions
db/model_versions.json -> ModelVersionTrackingStore / ModelVersionTrackingArtifact
models/efficientnet_b4.pth -> ActiveClassifierStore / active classifier binding

Remaining NOT SPECIFIED / source gaps:
- concrete identity of the actor that produces PostAdoptionAccuracyDegradation;
- any additional inputs of that evaluation;
- relative-percent vs percentage-point interpretation of the 5% threshold;
- exact ordering/tie-break/choice among multiple acceptable versions;
- concrete restore mechanics (copy/move/overwrite/load/reference switch/etc.);
- fate of the previously active model after rollback.

Documentation correction authorized:
YES - applied and reviewed in the DEC-08 -> FR-10 branch before the affected BA
was rebuilt.

BA status:
REBUILT FROM THE CORRECTED DOCUMENTATION / RC-001 CHECKPOINT COMPLETE.
Accepted affected propositions are BAP-DEC08-01 and BAP-FR10-01..05. Store,
selection and response-only retrieval/transfer semantics were reviewed through
C0.1/C0.2/C0.3. The BA-to-Mermaid rollback example is regression evidence only
and is not part of the finding's project or BA authority.
```


## 4. Execution sequence

### A. Source-to-hierarchy reconstruction

Analyze `RC-021` first as a family-wide MR-owner gate because it can change the macro ownership used by subsequent source findings. Then resume `RC-002` through `RC-009`, followed by `RC-013`, `RC-018`, `RC-019`, `RC-020`.

These rows can change MR/Decision/FR meaning and therefore must be resolved before BA identity or graph corrections. `RC-021` does not authorize new MR authoring by itself: the complete MR family must first pass the active Documentation Authoring Guide separation/classification gates.

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
