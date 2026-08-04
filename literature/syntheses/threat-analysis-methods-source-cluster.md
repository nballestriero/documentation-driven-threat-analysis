# Threat-analysis methods source cluster

## Purpose

Map threat-analysis methods by required input, abstraction level, procedure, output, assurance
and validation. The cluster is used to identify which techniques can participate in a
documentation-first DDTA workflow and which primary studies require full reading.

## Analyzed

### SRC-0026 - Tuma, Calikli and Scandariato (2018)

Role: historical systematic taxonomy of 26 threat-analysis techniques represented by 38 primary
studies published before January 2017.

The source establishes that the reviewed literature is predominantly pre-implementation:
fourteen techniques apply at requirements level, eleven at architecture and thirteen at design,
while only two apply at implementation. Requirements and textual descriptions are common
inputs. Source code appears in one method and is optional there.

This does not mean raw project documentation is automatically sufficient. The reviewed methods
usually assume an analyst already has goals, requirements, scenarios, attacker assumptions or an
architectural model. The documentation-to-model transformation remains separate and unresolved.

## Initial DDTA separation

```text
raw and governed project documentation
-> Base Analysis construction
-> methodology-specific threat analysis
-> reviewed findings
-> security requirements
```

SRC-0026 mostly maps the second transformation. DDTA must investigate the first transformation
through requirements-to-model and document-understanding studies.

## Technique-focus taxonomy

- Risk-centric: assets, value, risk and residual-risk reduction.
- Attack-centric: attacker profiles, attack paths and threat coverage.
- Software-centric: software or architecture elements, such as STRIDE over a DFD.
- GORE: goals, anti-goals and goal refinement.
- SRE: security-requirement elicitation or refinement.
- Privacy: privacy-specific threat and requirement analysis.

The categories are analytical centers, not mutually exclusive implementation modules. DDTA can
represent common system facts in Base Analysis and let overlays declare their required views and
focus.

## Documentation-first evidence

Direct evidence from the review:

- early threat analysis commonly operates before code exists;
- requirements, high-level goals and textual descriptions can be inputs;
- architecture and design models are also common inputs;
- source code is rarely required;
- threat analysis can be repeated later in the lifecycle.

Researcher conclusion for DDTA:

```text
documentation_only is possible for some techniques
documentation_plus_model is required for others
raw_documentation_to_neutral_model is not established
```

The first analysis should therefore remain documentation-primary. Later code analysis should
corroborate, contradict or refine the prior model rather than become a hidden prerequisite.

## Outcome and assurance gap

The reviewed techniques distinguish threats, mitigations and security requirements. Only a
minority provide explicit quality assurance. Completion conditions, precise rules and
comparative validation are also weak.

DDTA candidate controls:

- typed outputs;
- source provenance;
- extracted versus inferred status;
- coverage declaration;
- explicit stopping condition;
- incomplete-input diagnostics;
- human review state;
- separate verification evidence;
- versioned reruns after change.

## Primary-study selection queue

### Existing registry entries to analyze fully

1. SRC-0003 - Sindre and Opdahl, misuse cases.
2. SRC-0004 - van Lamsweerde, intentional anti-models and KAOS-style anti-goals.

### New sources to retrieve

3. Haley et al. - security requirements and satisfaction arguments.
4. Whittle et al. - misuse scenarios, mitigation weaving and finite-state verification.
5. Hatebur and Heisel - security problem frames.
6. A recent empirical STRIDE study - DFD-based overlay effectiveness and analyst performance.

These sources cover:

```text
use-case text
goal models
problem descriptions
behavioral models
architecture/DFD overlays
quality assurance
```

## Evidence still missing

- automatic extraction of Base Analysis entities from heterogeneous documentation;
- sentence-to-model provenance;
- management of missing and contradictory documentation;
- current tool maturity;
- continuous rerun and stale detection;
- current LLM/RAG performance;
- evaluation against expert-created threat models;
- review effort and accepted-finding yield.

## Temporal caveat

SRC-0026 is a strong historical map but cannot describe the 2026 state of automation or tools.
Every maturity claim must be updated through recent systematic reviews and empirical studies.

## Reading order

```text
SRC-0026 historical method taxonomy
-> SRC-0003 misuse cases
-> SRC-0004 anti-models
-> Haley explicit assurance
-> Whittle behavioral transformation
-> problem frames
-> current empirical STRIDE
-> recent automated-tool review
```
