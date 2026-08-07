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
| TFI-001 | Documentary extraction | Raw documentation must not become canonical analytical knowledge without evidence and review | Candidate BAE boundary exists | Preserve assertion-level evidence, extracted-vs-inferred state, stable candidate identity, contradiction and missing-information diagnostics | P0 | RQ1 reference cases and extraction oracle |
| TFI-002 | Neutral Base Analysis | The core must contain the minimum shared system knowledge, not the union of all methodology taxonomies | Methodology-neutral BAE model exists | Re-check BAE types/relations against the concrete information required by both demonstrator plugins | P0 | STRIDE and STRIDE-AI input mapping |
| TFI-003 | Plugin contract | Method semantics and applicability rules must remain outside the common core | Versioned methodology plugin ADR exists | Make required inputs, applicability diagnostics, plugin/version identity, deterministic candidate output and unavailable/incompatible behavior directly testable | P0 | RQ2 contract tests |
| TFI-004 | STRIDE plugin | First concrete plugin must prove the real contract rather than a fixture-only simulation | Current case study uses simulated STRIDE data | Implement governed STRIDE methodology payload, validation and candidate derivation | P0 | Published/controlled STRIDE reference cases |
| TFI-005 | STRIDE-AI plugin | A second method must consume the same Base Analysis while retaining AI/ML asset-centered semantics | Method boundary exists; production plugin not demonstrated | Implement STRIDE-AI as a separate plugin, preserving lifecycle assets, FMEA/failure-mode reasoning and method-owned classifications | P0 | Full targeted reading of Mauri/Damiani and a defensible reference case |
| TFI-006 | Common Finding | Heterogeneous method outputs need a common review boundary without semantic erasure | Common Finding model exists | Verify that both plugins can map candidates to the common envelope while retaining method evidence by reference | P0 | RQ2 paired-plugin study |
| TFI-007 | Security Requirement feedback | Accepted findings must become uniform product obligations independent of method vocabulary | Security Requirement model and authoring path exist | Evaluate multiple findings/methods -> one or more Security Requirements and full reverse traceability | P0 | RQ3 expected derivations |
| TFI-008 | Staleness | Source and methodology changes must identify dependent analytical artifacts requiring re-evaluation | Baseline/staleness concepts exist | Propagate reasoned stale state across source -> candidate -> BAE -> analysis -> finding -> Security Requirement; keep unrelated artifacts valid | P0 | RQ4 controlled mutation cases |
| TFI-009 | Evaluation instrumentation | The thesis needs observable correctness, not economic claims | Existing case-study verification is deterministic but simulated | Record expected/missing/unexpected BAE and finding results, trace completeness, review disposition and stale outcomes | P0 | Approved evaluation protocol |
| TFI-010 | Human review lifecycle | Candidate generation must remain distinct from acceptance | Review states exist; reviewer identity/transition audit is limited | Add only the minimum review evidence needed for the thesis: disposition, rationale and correction history where required | P1 | RQ1/RQ3 protocol |
| TFI-011 | Documentation feedback loop | Analysis can expose missing or contradictory project knowledge | Documentation gaps are modeled separately from findings | Demonstrate gap -> governed documentation correction -> BAE refresh -> dependent analysis stale -> rerun | P1 | Controlled change scenario |
| TFI-012 | LLM execution provenance | If model-assisted extraction is evaluated, output validity must not depend on provider/model name alone | Candidate strategy may be model-assisted; universal LLM replay is out of scope | Record input snapshot, model/interface identity, prompt/configuration, raw output and human correction for evaluated runs only | P1 | Only if an LLM-assisted path enters the evaluation |
| TFI-013 | Engineering testability | Scientific evidence is stronger when deterministic rules and persistent effects are independently verifiable | Engineering audit identified mixed effect boundaries in selected tools | Continue the separate governed hardening audit before refactoring; do not conflate engineering cleanup with DDTA scientific claims | P1 | ThreatForge audit and regression evidence |

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
State: publisher identity/abstract verified; full citation-ready reading pending.
```

A comparable authoritative STRIDE method/reference-case source must be selected before the STRIDE
plugin evaluation is treated as thesis evidence.

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
