# DDTA Semantic Workspace — Working Plan

Updated: 2026-11-02. This plan covers a **candidate experimental workspace**, not a promotion of legacy guide authority.

## 0. Baseline (bootstrap R1) — prepared

- [x] Establish project tree within `TESI/projects/ddta-semantic-workspace/`.
- [x] Preserve the most recent user-supplied `core(2).ttl` **byte for byte** as `ontology/core.ttl`; parse and check required vocabulary.
- [x] Re-home the tested RDF → Mermaid pilot into `tools/`, `dermatriage/`, and `tests/`.
- [x] Store graphical conventions separately in YAML, and graph scope in SPARQL CONSTRUCT.
- [x] Include MR-01 candidate, source PDF reference and two generated views.
- [x] Provide a non-destructive installation with preflight hash/collision checks.
- [ ] Apply package to Windows TESI repository; confirm generated graphs visually in VS Code and GitHub.
- [ ] Inspect and commit bootstrap diff on explicit review.

## 1. Core ontology and working semantics

- Continue one general concept at a time; no DermaTriage-specific entities in `ontology/core.ttl`.
- Check adequacy of generic contracts, cardinality, function, transfer, part-whole and boundary, reusing focused tests.
- Separate RDF semantics from generated diagram notation. Do not infer facts from presentation layout.

## 2. DermaTriage new documentation

- Review MR-01 concise `Intent`/`Context` and Turtle; keep metadata.
- Discuss and approve MR-02, MR-03 etc. one document at a time.
- Add Decision/FR documents gradually without copying implementation details into MR.
- Only then reconcile the documentation authoring schema; legacy strict validator may not accept this experimental MR format.

## 3. Visualization and validation

- Audit rules for additional operators and containment corner cases.
- Add SPARQL views for System/Environment, Transfer/Boundary, and Contract as their semantics stabilize.
- Keep `.graph.md` and `.mmd` generated, stable, diffable, checked by tests.
- When required, evaluate SHACL and scope-completeness controls as separate validation layers.

<!-- DDTA-SEMANTIC-WORKSPACE-GRAPH-PIPELINE-R1 BEGIN -->
### 3.1 Generic RDF composition and graphical pipeline (decision 2026-11-05)

**Architecture decision — accepted for implementation planning (not yet implemented).**

- **Document inputs:** DDTA authoring documents (MR, DEC, FR, and future document types) contain YAML front matter, natural-language description, and fenced Turtle blocks. Extract the Turtle from each *selected document*, regardless of document type. Do not require separate `.ttl` copies of Markdown-embedded Turtle; if standalone RDF sources are supported, their inclusion must be explicit and never double-count a companion copy by default.
- **Independent source selector:** select explicitly which documents contribute to the aggregate RDF graph. The same L1 query must work both for MR-01 + MR-02 and for all six MR documents, without changing the SPARQL query. Later selectors may use branches, document types or relations; these are deferred refinements.
- **RDF merge by identity:** resource identity is determined by the complete URI/IRI, not by label, file name or document ID. RDF triples are set-like: identical triples are deduplicated, while compatible statements about the same URI are merged. Different IRIs are not automatically equated. Do not add invented links to make a graph appear connected.
- **Blocking conflict policy:** a conflict established by the explicitly defined validation rules (e.g., violation of a declared disjointness or a constrained single-valued role) is a **hard error**. Validation is required **before** emitting any generated graph or report. On any detected incompatibility, parse error or failed required validation, **emit a clear error and create or overwrite NO output file** (`.mmd`, `.graph.md`, result/report, or other generated artifact). Existing outputs remain unchanged; no partial outputs are left behind. Compatible multiple assertions for the same URI are not conflicts merely because they appear in different documents. Document the conflict rules and test them; do not assume unrestricted OWL open-world reasoning flags every apparent discrepancy.
- **No per-edge provenance requirement:** the merged graph and rendered edges need not retain a source-document provenance record. A validation error may identify relevant input files for diagnosis; this is not an obligation to store persistent provenance per triple or per diagram edge.
- **One SPARQL query per requested view, independently of source selection:** the query selects graph entities/relations, not source files. Keep the existing CONSTRUCT approach as the first generic contract; examine SELECT-result mapping only if needed later.
- **One shared graphical configuration:** reuse and extend `tools/visualization.yaml`; do not create YAML styles for L1, L2, individual MR, DEC, FR or projects. Document front matter is metadata, not graphical configuration.
- **One generic renderer:** reuse/refactor `tools/rdf_mermaid/render.py` to render the query result with the shared YAML. Do not proliferate dedicated Python renderers per view. `tools/build_l1.py` may become a thin compatibility wrapper, but must not contain L1-specific Mermaid rendering logic.
- **Truthful topology:** the renderer must preserve selected RDF subjects and objects. In particular, draw `DermaTriageEnvironment` as a distinct Environment node: `EnvironmentPreparation prepares DermaTriageEnvironment`, and `DermaTriageVerification verifies` both DermaTriage and DermaTriageEnvironment. The `DermaTriage hasOperationalEnvironment DermaTriageEnvironment` relation is distinct from containment; never redirect edges to the System for layout convenience.
- **Primary capability and view simplification:** the previously tested `hasPrimaryFunction` keeps the system-to-primary link, while L1 can hide redundant `providesFunction` arrows *in the view only*. Preserve other functions, information links, preparation and verification semantics. Keep RDF statements unchanged by rendering rules.

**Implementation order / acceptance tests (pending):**

1. [ ] Inventory existing `tools/rdf_mermaid/render.py`, `tools/visualization.yaml`, `tools/build_l1.py`, SPARQL queries and tests; identify generic behavior to retain before refactoring.
2. [ ] Implement a generic DDTA Turtle extractor and source selector; allow MR-01 + MR-02 and all-six-MR inputs against the same L1 query, sharing the same graphical YAML.
3. [ ] Define explicit URI/type/property consistency rules and a fail-fast validator. Test compatible repeated URI, duplicate triple, distinct-URI resources, incompatible declarations, invalid Turtle, and zero-output-on-error (including preservation of previously generated files).
4. [ ] Separate query execution and generic Mermaid rendering without weakening determinism; produce `.mmd` and `.graph.md` from one renderer and one YAML for L1 and a second, unrelated SPARQL query.
5. [ ] Correct Environment/System topology for MR-C6 and MR-C7 through faithful RDF results and general renderer behavior, not project-specific Python logic.
6. [ ] Run regression tests for the existing L1 pilot (32 tests reported PASS on 2026-11-05), plus old RDF/Mermaid rendering tests. Visually review in VS Code before accepting the replacement pipeline.

**Scope:** this section records the architecture and test plan only. It does not claim that composition, conflict detection or renderer refactoring have already been implemented, and does not authorize changes to MR/DEC/FR authoring guides.
<!-- DDTA-SEMANTIC-WORKSPACE-GRAPH-PIPELINE-R1 END -->

## 4. Additional ontology modules

- When Core is stable, define AI (models, training/inference, agentic systems) separately from Core.
- Subsequently define security (STRIDE, STRIDE-AI, threats, controls, vulnerabilities, attack prerequisites) and appropriate bridging relationships.
- Avoid cyclic dependencies or implementing domain-specific concepts in Core.

## 5. Documentation guides — **last**

- After ontology and renderer converge, revise MR/DEC/FR authoring guides, Core/AI/Security ontology guides and visual conventions.
- Do not modify or replace existing governed guide files during the bootstrap.

## 6. Historical consolidation / clean-up — **deferred**

- Inventory old DDTA/DermaTriage folders and files in `TESI`.
- For each old artifact, decide retained-as-reference / migrated / retired, with explicit mapping and Git diff.
- Archive references or remove obsolete duplicates **only after** the new workspace passes validation and user approval.
- No deletion, movement, or rewriting of existing repo trees is permitted by this bootstrap.

## Known follow-ups

- `core.ttl` contains nonsemantic autogenerated comment headings for some `#` IRIs, while triples use `/`. Preserve the uploaded file now; normalize comments only in a separately reviewed change.
- Consider a neutral, project-owned ontology IRI later, but **never change the namespace without explicit migration** and updated tests/queries.
- Current `derma:` namespace `https://example.org/ddta/dermatriage#` is an experimental identifier, not a finalized production IRI.
- Clarify how visualized `hasPart` handles multiple parents and collapsing large hierarchies before claiming generality.

## Core identity migration (2026-11-02, candidate)

- Ontology IRI: `https://w3id.org/ddta/core`; DDTA term namespace: `https://w3id.org/ddta/core#`.
- Migration applies to `core.ttl`, MR Turtle, SPARQL and visualization YAML together. Graph files need not change if their source entity IRIs and projected labels remain unchanged.
- Public `w3id.org/ddta` registration/redirect is **not yet completed or verified**; resolve and register it before publication.
- Do not use the old Protégé IRI in new documents. Keep original/historical references unchanged outside this workspace.
- DermaTriage `https://example.org/ddta/dermatriage#` remains an experimental namespace pending a separate explicit decision.

## Candidate follow-up — MR-01/MR-02 aggregated test

- [x] Create experimental MR-02 with shared `TriageOutcome` IRI.
- [x] Render MR-01 and MR-02 as one RDF graph with deterministic `--source` aggregation and SPARQL overview/structure views.
- [ ] Validate the generated overview on the local VS Code preview and GitHub.
- [ ] Decide how to assert system-level functional composition without conflating capability with physical part.
- [ ] Extend to MR-03 and MR-04 only after reviewing the combined view.
- [ ] Remove temporary `ontology/mentor-probe.ttl` from Git in a separate, reviewed cleanup.

## MR-03 experimental composition (2026-11-02)

- [x] Approve MR-03 candidate with TriageOutcome and ClinicalReview as inputs to ClinicalReviewManagement.
- [x] Define ClinicalReviewRecord as Information with both original inputs as logical `hasPart` components; no duplicate RDF identities.
- [x] Add reusable SPARQL views (`mr-functions-overview.rq`, `mr-functions-structure.rq`) selecting Function roots dynamically.
- [ ] Validate single-IRI containment view and MR-01/02/03 combined view in VS Code; treat all combined views as **on-demand temporary output**, not required Git artifacts.
- [ ] Evaluate composite information graph projection for cyclic flow layouts and whether Core needs new relations only if a **semantic** fact cannot be expressed.
- [ ] Continue MR-04 separately before asserting a complete system graph or extending visualization tools.

## MR-04 controlled adaptation experiment (2026-11-02)

- [x] Approve autonomous MR-04 Intent and Context: evidence from accumulated clinical reviews, versioned pipeline AI components, qualification before any possible adoption, stable function identities.
- [x] Express the structural MR-03 to MR-04 connection through shared `ClinicalReviewRecord` IRI and `AccumulatedClinicalReviewRecords hasPart ClinicalReviewRecord`.
- [x] Distinguish `AdaptationCandidate` (`Artifact`) from `AdaptationQualificationResult` (`Information`) using only existing Core ontology vocabulary.
- [x] Enable type-aware Artifact rendering through YAML with an existing style, without modifying Core or regenerating older graphs.
- [ ] Inspect isolated MR-04 and combined MR-01…MR-04 Mermaid graphs visually in VS Code; keep previews temporary.
- [ ] Later model the distinction between adaptation candidate, operational adoption, targeted stable Function and realization/version, when elaborating Decisions and FRs; do not invent automatic deployment semantics.
- [ ] Future multiplicity/cardinality and qualifying evidence rules belong to lower-level requirements/instance models, not a single `hasPart` triple.

<!-- DDTA-MR-TO-DEC-CHECKPOINT-20261105 BEGIN -->
## Checkpoint MR -> DEC (2026-11-05)

**Decisione di lavoro.** Per l'attuale livello di astrazione dei MacroRequirement di DermaTriage, la revisione semantica e la rappresentazione Graph L1/L2/L3 sono considerate **sufficienti per passare all'analisi delle Decision**. Non e' una dichiarazione di completezza definitiva del sistema, di conformita' dell'implementazione, ne' una promozione automatica dello stato `candidate` dei documenti.

### Baseline MR da conservare e usare come input

- **Sei documenti canonici**, senza copie storiche parallele: `dermatriage/mr/MR-01.md`, `MR-02.md`, `MR-03.md`, `MR-04.md`, `MR-C6.md`, `MR-C7.md`. Intent, Context e Turtle rimangono nello stesso Markdown; lo storico e' affidato a Git.
- **MR-01:** una funzione primaria, due `FunctionalMode` (con e senza immagine), input/output descritti con le proprieta' condivise `hasInput`/`hasOutput`, contratto con cardinalita' e output logico generale `TriageOutcome`. Le condizioni formali e le garanzie dei singoli elementi restano da approfondire nelle Decision/FR.
- **MR-02:** indirizzamento specialistico collegato a `TriageOutcome` tramite identita' RDF condivisa; non introdurre in MR regole di assegnazione o prenotazione.
- **MR-03:** composizione logica `ClinicalReviewRecord hasPart TriageOutcome, ClinicalReview`; lacuna documentale esplicita sulla sorgente operativa della revisione clinica.
- **MR-04:** `ControlledAdaptation` con due sottofunzioni, adattamento dei modelli di classificazione e dei prompt generativi; nessuna `FunctionalMode` per questa distinzione; dettaglio di addestramento, versionamento e accettazione rinviato.
- **MR-C6:** `EnvironmentPreparation prepares DermaTriageEnvironment` e struttura logica dell'ambiente; nessuna equivalenza tra ambiente e sistema.
- **MR-C7:** funzione di verifica autonoma che `verifies` sistema e ambiente; **non** dichiarare automaticamente `DermaTriage providesFunction DermaTriageVerification`.

### Regole condivise e baseline grafica

- RDF delle fonti selezionate unito per IRI; validazione prima dell'emissione dei grafici. Nessuna relazione inventata per rendere connessi i nodi.
- **SPARQL** sceglie contenuto e proiezione di vista; il **solo YAML grafico condiviso** determina le convenzioni di rappresentazione; il **renderer Python generico** traduce il risultato della query e lo YAML in Mermaid deterministico. Verificare l'output anche in VS Code.
- Graph L1/L2/L3 sono viste della documentazione, **non livelli ontologici intrinseci**. Graph L3 generale resta disponibile ma puo' essere denso; `--focus`, mappatura costrutti/livelli, profondita' L4 e selettore delle lacune sono **rinviati**, non requisiti implementativi correnti.
- I `Contract` e `ContractElement` restano nel Turtle, mentre Graph L3 standard proietta cardinalita' sulle informazioni senza duplicare i loro nodi. Le lacune RDF restano validate ma nascoste di default. `providesFunction` puo' essere omesso dalla vista come arco ridondante, non cancellato dal modello.
- Le proprieta' `modeHasInput`, `guaranteesOutput`, `requiresPresent`, `requiresAbsent` sono ritirate in favore di `hasInput`/`hasOutput` e dei contratti. Per gli elementi contrattuali e' stata concordata la rinomina `specifiesInformation` -> `constrainsInformation`. Le frecce `hasInput` e `hasOutput` devono avere etichetta nello YAML condiviso.

### Prossima fase: analisi delle Decision

1. [ ] **Verifica locale del checkpoint:** controllare che tutti gli ultimi pacchetti approvati siano applicati (Core, sei MR, SPARQL, YAML, validatore, test). Rigenerare L1/L2/L3 ed eseguire i controlli di determinismo; visionare lo stato Git prima del commit. Questo documento non certifica l'avvenuta installazione dei pacchetti sul PC.
2. [ ] **Inventario delle Decision:** individuare i documenti DEC pertinenti ai sei MR e confrontarli con il materiale LaTeX/PDF usato nell'esperimento di riscrittura; non importare senza revisione dettagli implementativi o semantica non confermata.
3. [ ] **Analisi una DEC alla volta:** definire/controllare Intent, Context, relazioni con il MR, identita' RDF riusate, nuove entita' e Turtle del singolo Markdown canonico. I documenti devono risultare autosufficienti, senza presentare la documentazione storica come fonte normativa interna.
4. [ ] **Ontologia AI specializzata quando necessaria:** approfondire pipeline, modelli, prompt, addestramento, riaddestramento, versioni, qualificazione e adozione nel modulo AI, **senza** appesantire il Core con concetti di dominio non necessari.
5. [ ] **Validazione e grafi DEC:** conservare le identita' condivise fra MR/DEC/FR; usare la pipeline RDF/SPARQL/YAML/Python gia' disponibile. Nuove viste o livelli solo quando i casi documentali mostrino una necessita' concreta.
6. [ ] **FR e sicurezza successivamente:** scendere a requisiti verificabili, implementazioni e analisi di sicurezza quando il livello DEC sia sufficientemente stabilizzato.

**Nota sulle sezioni precedenti del piano:** alcune checklist storiche possono riportare ancora attivita' MR o della pipeline come `pending`. Questo checkpoint registra la decisione corrente di passaggio alle DEC; lo stato effettivo dell'installazione e dei test va verificato nel checkout locale prima di aggiornare le vecchie checklist.

**Regola di gestione:** nessuna nuova versione `MR-xx_Rn.md` o copia `.ttl` parallela agli MR; nessuna modifica massiva o commit automatico. Se una DEC rivela una lacuna in un MR, correggere **lo stesso file MR** con revisione esplicita e test di regressione.
<!-- DDTA-MR-TO-DEC-CHECKPOINT-20261105 END -->
