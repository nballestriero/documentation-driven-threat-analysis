# ThreatForge improvement and evaluation ledger

## Purpose

This is a research-side planning ledger. It records implications derived from the completed DDTA
literature corpus and the focused thesis scope. It is not a ThreatForge requirement, ADR or
implementation authority.

Research observations must be reviewed before they become governed ThreatForge obligations.

## Frozen thesis direction

```text
governed documentation
-> reviewed methodology-neutral Base Analysis
-> isolated methodology plugin / overlay
-> methodology-specific Analysis Record
-> methodology-neutral Common Finding
-> explicit review
-> governed Security Requirement
-> documentation feedback
-> change-aware re-analysis
```

The main thesis question is whether the same neutral core can support distinct methodologies.
STRIDE and STRIDE-AI are the two planned demonstrator plugins. They are selected to exercise the
plugin boundary with different method-owned semantics; two implementations do not establish
universal methodology support.

Economic cost and ROI are outside the primary evaluation scope.

## Improvement and evidence ledger

| ID | Area | Current research implication | ThreatForge state to verify | Candidate improvement | Thesis priority | Evidence needed before product obligation |
|---|---|---|---|---|---|---|
| TFI-001 | Portable documentation to Base Analysis | Documentation satisfying the DDTA portability contract must yield reviewable Base Analysis candidates with explicit provenance without importing methodology-specific semantics into the common core | Candidate BAE boundary exists | Evaluate the mapping from contract-conformant governed documentation to Base Analysis candidates; preserve source evidence, stable candidate identity, review disposition and diagnostics for missing contract-required information | P0 | RQ1 portable-by-construction reference cases and expected Base Analysis oracle |
| TFI-002 | Neutral Base Analysis | The core must contain the minimum shared system knowledge, not the union of all methodology taxonomies | Methodology-neutral BAE model exists | Re-check BAE types/relations against the concrete information required by both demonstrator plugins | P0 | STRIDE and STRIDE-AI input mapping |
| TFI-003 | Plugin contract | Method semantics and applicability rules must remain outside the common core | Versioned methodology plugin ADR exists | Make required inputs, applicability diagnostics, plugin/version identity, deterministic candidate output and unavailable/incompatible behavior directly testable | P0 | RQ2 contract tests |
| TFI-004 | STRIDE plugin | First concrete plugin must prove the real contract rather than a fixture-only simulation | Current case study uses simulated STRIDE data | Implement governed STRIDE methodology payload, validation and candidate derivation | P0 | Published/controlled STRIDE reference cases |
| TFI-005 | STRIDE-AI plugin | A second method must consume the same Base Analysis while retaining AI/ML asset-centered semantics | Method boundary exists; production plugin not demonstrated | Implement STRIDE-AI as a separate plugin, preserving lifecycle assets, FMEA/failure-mode reasoning and method-owned classifications | P0 | Completed full Mauri/Damiani reading plus a defensible STRIDE-AI reference case and expected-results oracle |
| TFI-006 | Common Finding | Heterogeneous method outputs need a common review boundary without semantic erasure | Common Finding model exists | Verify that both plugins can map candidates to the common envelope while retaining method evidence by reference | P0 | RQ2 paired-plugin study |
| TFI-007 | Security Requirement feedback | Accepted findings must become uniform product obligations independent of method vocabulary | Security Requirement model and authoring path exist | Evaluate multiple findings/methods -> one or more Security Requirements and full reverse traceability | P0 | RQ3 expected derivations |
| TFI-008 | Staleness | Source and methodology changes must identify dependent analytical artifacts requiring re-evaluation | Baseline/staleness concepts exist | Propagate reasoned stale state across source -> candidate -> BAE -> analysis -> finding -> Security Requirement; keep unrelated artifacts valid | P0 | RQ4 controlled mutation cases |
| TFI-009 | Evaluation instrumentation | The thesis needs observable correctness, not economic claims | Existing case-study verification is deterministic but simulated | Record expected/missing/unexpected BAE and finding results, trace completeness, review disposition and stale outcomes | P0 | Approved evaluation protocol |
| TFI-010 | Human review lifecycle | Candidate generation must remain distinct from acceptance | Review states exist; reviewer identity/transition audit is limited | Add only the minimum review evidence needed for the thesis: disposition, rationale and correction history where required | P1 | RQ1/RQ3 protocol |
| TFI-011 | Documentation feedback loop | Analysis can expose missing or contradictory project knowledge | Documentation gaps are modeled separately from findings | Demonstrate gap -> governed documentation correction -> BAE refresh -> dependent analysis stale -> rerun | P1 | Controlled change scenario |
| TFI-012 | Generic/legacy documentation migration | Transforming arbitrary documentation into DDTA-portable form is a separate research problem involving information loss, inference, ambiguity and human correction | Not part of the current thesis evaluation | Future work only; study migration strategies, including model-assisted or LLM-assisted approaches and their provenance, under a separate protocol | Future work | Separate future-work study; no current product obligation |
| TFI-013 | Engineering testability and code quality | Scientific evidence is stronger when deterministic rules and persistent effects are independently verifiable; the thesis artifact must also remain maintainable | Engineering audit identified mixed effect boundaries in selected tools | Continue the code-quality/testability audit covering responsibility cohesion, import safety, deterministic cores, effect isolation, diagnostics, fault injection, coverage and duplicated rules; do not conflate engineering cleanup with DDTA scientific claims | P1 | ThreatForge audit and regression evidence |
| TFI-014 | Portable-by-construction documentation contract | Expected analyzability requires an explicit methodology-neutral input contract rather than arbitrary project documentation | Governed document models and authoring exist | Derive and evaluate the portable-by-construction DDTA writing/input profile; migration from generic/legacy documentation is future work | P0 | Literature-to-model mapping plus RQ1 input oracle |
| TFI-015 | Model neutrality audit | Registries, relations, taxonomies and vocabularies must not encode one analytical viewpoint as universal project truth | Neutrality is intended but has not been source-audited end-to-end against both demonstrator methods | Inventory every relevant model concept and classify common, method-specific, implementation-only or insufficiently supported; challenge forced aggregation and fixed-focus assumptions | P0 | Source-backed neutrality matrix and reviewed dispositions |
| TFI-016 | VS Code model authorability | Every governed model intended for user editing should be simple to create and modify with editor assistance | Shared governed Markdown assistance and Target Project schema routing exist | Verify model-by-model schema discovery, completion/diagnostics and lossless create/edit/revalidate round trip in platform and Target Projects | P1 | Editor/validator matrix plus round-trip fixtures |
| TFI-017 | Shared editor/checker validation semantics | Syntax and structural validity should not silently diverge between VS Code and repository gates | Reuse exists in parts of the authoring stack; complete parity is not yet audited | Reuse one deterministic validation core or artifacts generated from the same canonical rule source for shared editor/checker semantics; isolate adapter-only concerns | P1 | Positive/negative fixture parity across editor-facing and repository validation |
| TFI-018 | Guides and explanatory diagrams | ThreatForge must be usable and explainable independently of thesis prose | Technical documentation exists but coverage and baseline alignment are not yet audited end-to-end | Complete the minimum Diataxis guide set and baseline-bound diagrams for architecture, documentation model, VS Code integration, analysis/plugin lifecycle, provenance/staleness and Target Project boundaries | P1 | Documentation coverage matrix plus clean-user/maintainer walkthrough |

## Evaluation case strategy

Prefer cases with explicit expected results:

```text
documented case
-> expected Base Analysis
-> method-specific expected analysis facts
-> expected finding set where defensible
-> reviewed Common Findings
-> expected Security Requirement derivation
```

Use published worked examples when their inputs and outputs are sufficiently explicit. Otherwise
prepare an independent reference model before running ThreatForge and record who created/reviewed it.

Possible measures:

- Base Analysis expected / missing / unexpected elements and relations;
- source-provenance completeness;
- method-input coverage;
- expected / missing / unexpected finding candidates;
- plugin isolation and Base Analysis invariance;
- Common Finding schema and trace validity;
- Security Requirement provenance completeness;
- stale true positives, false positives and false negatives for controlled changes.

Precision, recall and F1 are allowed only when the reference case defines TP/FP/FN meaningfully.

## Targeted methodology references

The central-reading corpus remains complete at 21/21.

Targeted references needed to implement or evaluate the two demonstrator methodologies do not
increment that corpus. They must still be read and recorded faithfully before final thesis citation.

First targeted reference:

```text
Mauri, Lara; Damiani, Ernesto.
Modeling Threats to AI-ML Systems Using STRIDE.
Sensors 22(17), 6662, 2022.
DOI 10.3390/s22176662.
Role: STRIDE-AI method definition, asset-centered framing, candidate published reference case.
State: full citation-ready reading completed on 2026-08-08; method framing, lifecycle/assets, FMEA mapping, TOREADOR case and limitations reviewed; used in standalone Chapters 2 and 3; remains outside the central 21/21 corpus.
```

A comparable authoritative STRIDE method/reference-case source must be selected before the STRIDE
plugin evaluation is treated as thesis evidence.

## Working proposition - portable-by-construction documentation

The thesis scope is intentionally restricted to one input mode:

```text
portable-by-construction governed documentation
-> DDTA portability / analysis-readiness contract satisfied
-> methodology-neutral Base Analysis
-> analyzability evaluated
```

The current thesis does not evaluate the transformation of arbitrary, legacy or
unstructured project documentation into this portable form. That is explicitly
deferred to future work, where the difficulties of migration, information loss,
inference, ambiguity and human correction can be studied independently.

"Portable-by-construction" does not mean embedding STRIDE, STRIDE-AI or another
threat methodology into project documentation. It means that common project
knowledge is written so that multiple analytical viewpoints can consume it
without changing its canonical meaning.

The portability contract should be derived from evidence and should cover, at
minimum:

- stable identity for governed subjects;
- explicit semantic meaning of governed records;
- explicit relations when those relations are analytically relevant;
- source provenance;
- baseline/version information;
- controlled vocabularies with governed extension;
- explicit representation of uncertainty, contradiction and missing required
  information where these are part of the governed model;
- separation between common project knowledge and methodology-owned semantics;
- extension points that allow method-specific overlays without mutating the core.

The proposition to evaluate is therefore not universal analysis from arbitrary
documentation. It is:

```text
documentation designed to satisfy a method-neutral portability contract
-> common analyzable representation
-> multiple isolated methodology overlays
```

This working proposition must be validated before it becomes the final DDTA
writing method.

## Literature-to-model neutrality audit before the writing method

Before freezing the DDTA writing method, compare the current ThreatForge
documentation/model vocabulary with the completed literature corpus and the
targeted STRIDE / STRIDE-AI references.

Inventory at least:

```text
ThreatForge Base Analysis types and relations
document-model registries
Requirement and Security Requirement structures
analysis records and Common Finding envelope
taxonomies and controlled vocabularies
reference/provenance records
materialization/projection rules
extension mechanisms
research/methodology/primary-analysis-focus.md
```

For every type, field, relation and controlled concept, record:

```text
concept
current semantic meaning
canonical owner
literature/source support
required by STRIDE?
required by STRIDE-AI?
required by both?
plausibly common across other reviewed viewpoints?
method-specific leakage?
implementation-convenience-only?
forced aggregation or lossy mapping risk?
provenance/version requirement
editor/validator representation
disposition: keep / revise / move to extension/plugin / insufficient evidence
```

The audit must explicitly challenge the current research working proposition that
every Functional Requirement has exactly one primary Base Analysis focus selected
from `actor`, `component`, `asset`, `boundary` or `data_flow`. The proposition may
survive, be generalized, become optional, or be rejected; it must not become part
of the writing method merely because it already exists in a working file.

The output of this audit is a source-backed neutrality matrix, not an immediate
ThreatForge change.

## Writing-method gate

Only after the neutrality audit should the thesis freeze how a DDTA-portable
project is written.

The writing method must define:

```text
minimum required documentary knowledge
stable identity rules
relation-writing rules
source/provenance rules
baseline/version rules
controlled vocabulary and extension rules
how uncertainty, contradiction and missing required information are written
what a human must review
portable-by-construction conformance criteria
```

The writing method is itself part of the thesis artifact: it defines the input
contract against which RQ1 can be evaluated.

It must remain methodology-neutral. STRIDE/STRIDE-AI categories, applicability
rules, failure modes and other method-owned semantics belong to their overlays.

Migration from generic or legacy documentation into this portable form is outside
the current thesis scope and belongs to future work.

## ThreatForge artifact-quality and usability evidence

The thesis artifact must also be evaluated as software, separately from the DDTA
scientific claims.

Before the implementation/evaluation phase is considered complete, inspect:

### Code quality and testability

- responsibility cohesion and maintainability;
- deterministic callable cores;
- import safety;
- explicit effect boundaries;
- stable structured diagnostics;
- rollback and deterministic failure injection where mutations exist;
- direct/integration/negative-fixture coverage;
- reproducible coverage evidence where coverage is claimed;
- duplicated canonical values or validation rules.

### VS Code authoring and round trip

For every governed model intended for user editing, verify:

```text
create in VS Code
-> schema/assistance discovered
-> edit controlled fields and relations
-> receive completion/diagnostics
-> save
-> repository syntax/structure checker agrees
-> reopen without information loss
```

Run the same check for Target Projects where local schema routing applies.

### Shared validation semantics

Prefer one canonical source of syntax/structural truth:

```text
canonical schema / model rules
        |
        v
reusable deterministic validation
        +--> CLI / repository gate
        +--> VS Code schema or diagnostics
        +--> Target Project local authoring support
```

The exact implementation may differ by adapter, but shared validity rules should
not be manually duplicated. The audit must identify any divergence before a
refactor is proposed.

### Guides and diagrams

Treat documentation as artifact evidence, not optional polish. Audit or create
the minimum Diataxis set needed by a new user and maintainer:

- tutorial for the first governed project and first analysis;
- how-to guides for authoring, VS Code, checks, Target Projects and analysis;
- reference for models, contracts, taxonomies, commands and diagnostics;
- explanation for governance, DDTA lifecycle, plugin isolation and provenance.

Prepare baseline-bound diagrams for:

- ThreatForge architecture;
- registry/body/schema/validator relationships;
- VS Code integration and shared validation;
- Base Analysis -> plugin -> Analysis Record -> Common Finding -> Security Requirement;
- provenance and stale propagation;
- ThreatForge / Target Project boundaries.

## Revised pre-implementation order

The research/product sequence is now:

```text
1. close targeted STRIDE-AI reading bookkeeping
2. select and fully read an authoritative STRIDE method/reference case
3. inventory ThreatForge model semantics on immutable baseline cae0f7b6
4. perform the literature-to-model neutrality audit
5. derive the portable-by-construction DDTA documentation contract and writing method
6. freeze RQ1-RQ4 evaluation cases, oracles, measures and acceptance criteria
7. expand the ThreatForge code-quality / VS Code / validator-reuse audit
8. inspect existing product governance authority
9. make only the smallest required governed product changes
10. implement the real STRIDE and STRIDE-AI vertical slice
11. execute the frozen evaluation and preserve negative/partial results
12. complete guides, diagrams and final thesis chapters from observed evidence
```

Scientific DDTA evidence and general software-quality evidence remain distinct.
A well-engineered artifact does not by itself prove H1-H4; conversely, a passing
case study does not excuse unmaintainable or poorly documented product code.

The transformation of generic/legacy documentation into portable DDTA
documentation is explicitly deferred to future work.

## Product-governance rule

No item in this ledger automatically creates a ThreatForge requirement. For each P0/P1 item:

```text
research implication
-> inspect immutable ThreatForge baseline
-> check existing MR / ADR / Requirement authority
-> select the smallest governance change
-> define verification evidence
-> only then modify implementation
```
