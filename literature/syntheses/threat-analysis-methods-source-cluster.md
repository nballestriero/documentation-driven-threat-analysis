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


### SRC-0004 - van Lamsweerde (2004)

Role: documentation-plus-model, goal-oriented and partly formal security-requirements
elaboration. The method builds a primal model of goals, agents, objects, operations, requirements,
expectations and domain properties together with an intentional anti-model of attackers,
anti-goals, capabilities and vulnerabilities.

The source confirms that security analysis can begin from declarative assertions in stakeholder
interviews and documents before implementation or complete state-machine models. It does not
analyze raw documentation directly: the assertions must be interpreted into structured goal,
object, agent and domain models.

Anti-goal refinement distinguishes attacker-realizable anti-requirements from
attackee-realizable vulnerabilities. Formal regression and refinement patterns can provide local
derivation evidence, and bounded SAT solving can generate scenarios once formal models exist.
Sensitive-object identification, attacker motives, domain properties, risk assessment and
countermeasure selection remain analyst responsibilities.

The approach therefore provides stronger internal assurance than scenario templates, but at
higher modeling cost. Its global requirement/anti-requirement/countermeasure termination rule is
explicitly left open, and the anti-model extension had only four reported case studies.


### SRC-0027 - Haley, Laney, Moffett and Nuseibeh (2008)

Role: documentation-plus-model security-requirement assurance. The framework represents security
requirements as constraints on specific functional requirements and verifies conditional
satisfaction through a formal outer argument and structured informal inner arguments.

The source confirms that assurance can be constructed before implementation, but only after the
system context, domains, shared phenomena and behavior have been represented. Stage 1 requires a
context representation while leaving its derivation method open. The documentation-to-context
transformation remains outside the framework.

Outer arguments expose the domain-behavior premises needed for a requirement to hold. Inner
arguments challenge those premises through grounds, warrants, rebuttals and explicit trust
assumptions. Failure can reveal an infeasible requirement, missing context information or a need
for new functions, goals and requirements.

The CRISTAL UK/NATS application exposed previously unconsidered rebuttals and mitigations, but also
showed practitioner difficulty with formal arguments, preference for less expressive graphics,
lack of a complete rebuttal-discovery recipe and a need for stronger tool support. The evidence is
one project application, not a controlled comparison.

## Initial DDTA separation

```text
raw and governed project documentation
-> Base Analysis construction
-> methodology-specific threat analysis
-> reviewed findings
-> security requirements
-> satisfaction and assurance evidence
-> accepted assurance or iteration
```

SRC-0026 mostly maps methodology-specific threat analysis. SRC-0003 demonstrates a scenario-based
implementation after a functional scenario view exists. SRC-0004 demonstrates a goal-oriented
implementation after a structured primal model exists. SRC-0027 adds a downstream assurance
layer after problem-context and behavior views exist. DDTA must still investigate how
heterogeneous documentation becomes the neutral assets, actors, goals, interactions, objects,
operations, domains and phenomena consumed by these overlays and arguments.

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
- a goal-oriented method can operate on partial declarative models before implementation;
- formal threat derivation becomes possible after goal, object, agent and domain modeling;
- formal-plus-informal assurance becomes possible after context, phenomena and behavior modeling;
- failed assurance arguments can diagnose missing information and require design iteration;
- structured scenarios, goal models and problem contexts are not equivalent to raw heterogeneous documentation.

Researcher conclusion for DDTA:

```text
documentation_only is possible for some techniques
documentation_plus_model is required for others
raw_documentation_to_neutral_model is not established
```

The first analysis should therefore remain documentation-primary. Later code analysis should
corroborate, contradict or refine the prior model rather than become a hidden prerequisite.

## Outcome and assurance gap

The reviewed techniques distinguish threats, mitigations and security requirements. SRC-0027
shows how explicit assurance can be structured as conditional proof plus arguments for trust
assumptions, but its completeness remains relative to the modeled context and selected premises.
Completion conditions, precise discovery rules and comparative validation remain weak.

DDTA candidate controls:

- typed outputs;
- source provenance;
- extracted versus inferred status;
- scenario-level review dispositions;
- progressive lightweight and extensive analysis profiles;
- derivation rule, premises and proof status;
- software requirement versus environmental expectation responsibility;
- preserved alternative countermeasures and selection rationale;
- security-goal-to-requirement validation evidence;
- outer-argument premises, logic and proof status;
- inner claims, grounds, warrants, rebuttals and trust assumptions;
- primary-to-secondary cover/replace ancestry;
- coverage declaration;
- explicit stopping condition;
- incomplete-input diagnostics;
- human review state;
- separate verification evidence;
- versioned reruns after change.

## Primary-study selection queue

### New sources to retrieve

1. Whittle et al. - misuse scenarios, mitigation weaving and finite-state verification.
2. Hatebur and Heisel - security problem frames.
3. A recent empirical STRIDE study - DFD-based overlay effectiveness and analyst performance.

These sources cover:

```text
use-case text
goal models
problem descriptions
behavioral models
architecture/DFD overlays
quality assurance
```


## Scenario, anti-goal and assurance contrast

| Dimension | SRC-0003 | SRC-0004 | SRC-0027 |
|---|---|---|---|
| Starting view | functional scenarios | goal, object, agent and domain models | problem context, phenomena and behavior |
| Main structure | harmful scenario | intentional AND/OR anti-goal graph | constrained requirement and argument graph |
| Formality | mostly informal | optional temporal logic and formal regression | formal outer proof plus informal inner argument |
| Security output | misuse and mitigation | anti-requirement and vulnerability | primary/secondary security constraints |
| Assumption handling | template fields | domain properties | trust assumptions and rebuttals |
| Assurance | review status and trace links | local proof and derivation evidence | conditional satisfaction evidence |
| Empirical evidence | descriptive examples | four anti-model cases | one industrial research application |

All three approaches are pre-code. None solves source-document interpretation, assertion-level
provenance or global completeness. They support different methodology and assurance overlays over
a neutral Base Analysis.

## Evidence still missing

- automatic extraction of Base Analysis entities, scenario views and goal views from heterogeneous documentation;
- sentence-to-model, sentence-to-scenario, sentence-to-goal and sentence-to-context provenance;
- management of missing and contradictory documentation;
- governed trust-assumption acceptance and residual-risk criteria;
- automatic argument maintenance and change impact;
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
-> SRC-0027 explicit satisfaction assurance
-> Whittle behavioral transformation
-> problem frames
-> current empirical STRIDE
-> recent automated-tool review
```
