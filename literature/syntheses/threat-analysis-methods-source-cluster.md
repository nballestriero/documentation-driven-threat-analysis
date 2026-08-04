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


### SRC-0003 - Sindre and Opdahl (2005)

Role: documentation-primary, scenario-based security-requirements elicitation. The method extends
functional use cases with misusers, misuse cases and security use cases connected through
`threaten` and `mitigate`.

The source confirms that threat and security-requirement candidates can be elicited before code
or detailed design. It does not begin from arbitrary documentation: analysts need or create
structured functional scenarios, assets and security goals. Threat discovery, risk assessment and
countermeasure selection remain human activities.

A lightweight threat field gives each use case a visible review status. Extensive misuse cases
add harmful paths, assumptions, preconditions, mitigation points, guarantees, misuser profiles
and stakeholder risks. This supports a progressive path from early coverage to detailed analysis.

The main limitation is discovery assurance. Guidelines remain open-ended, global stopping and
prioritization are underdeveloped, and threats without an identifiable actor or action sequence
fit poorly. The method is therefore a candidate scenario overlay, not a complete neutral Base
Analysis or universal threat method.

## Initial DDTA separation

```text
raw and governed project documentation
-> Base Analysis construction
-> methodology-specific threat analysis
-> reviewed findings
-> security requirements
```

SRC-0026 mostly maps the second transformation. SRC-0003 demonstrates one scenario-based
implementation of that transformation after a functional scenario view exists. DDTA must still
investigate how heterogeneous documentation becomes the neutral assets, actors, goals,
interactions and scenarios consumed by overlays.

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
- threat analysis can be repeated later in the lifecycle;
- a scenario-based method can link functional behavior to threats and security requirements;
- structured scenarios are not equivalent to raw heterogeneous documentation.

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
- scenario-level review dispositions;
- progressive lightweight and extensive analysis profiles;
- coverage declaration;
- explicit stopping condition;
- incomplete-input diagnostics;
- human review state;
- separate verification evidence;
- versioned reruns after change.

## Primary-study selection queue

### Existing registry entry to analyze fully

1. SRC-0004 - van Lamsweerde, intentional anti-models and KAOS-style anti-goals.

### New sources to retrieve

2. Haley et al. - security requirements and satisfaction arguments.
3. Whittle et al. - misuse scenarios, mitigation weaving and finite-state verification.
4. Hatebur and Heisel - security problem frames.
5. A recent empirical STRIDE study - DFD-based overlay effectiveness and analyst performance.

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

- automatic extraction of Base Analysis entities and scenario views from heterogeneous documentation;
- sentence-to-model and sentence-to-scenario provenance;
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
-> SRC-0003 scenario-based misuse cases
-> SRC-0004 goal-oriented anti-models
-> Haley explicit assurance
-> Whittle behavioral transformation
-> problem frames
-> current empirical STRIDE
-> recent automated-tool review
```
