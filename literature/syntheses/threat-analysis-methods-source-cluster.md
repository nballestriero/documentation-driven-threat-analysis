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


### SRC-0028 - Whittle, Wijesekera and Hartong (2008)

Role: documentation-plus-model executable misuse-case testing. The method starts from a precise
functional scenario model, adds attacker modification and attack scenarios, keeps mitigations as
separate aspects, weaves them into core behavior and generates communicating finite-state machines.
Specified attack traces are then executed as model-level tests and rerun as a regression suite.

The source confirms that known attacks and mitigations can be tested before implementation, but
only after use cases, EIODs, sequence diagrams, messages and relevant state conditions have been
modeled. It does not transform heterogeneous documentation into those views or discover attacks
automatically. Attack inputs in the studies came from an earlier code analysis or human
brainstorming.

A key boundary is that the reported MUCSIM tool supports animation and attack execution, not formal
analysis. EIODs and FSMs have formal semantics and external analyzers are suggested, but the paper
does not evaluate model checking or prove security. Regression success is relative to the modeled
traces and composed behavior.

The evaluation is preliminary. Seven of nine design-level EVS attacks were modelable; two required
lower-level storage or network information. The PTC study brainstormed nineteen attacks but modeled
four representatives. The authors explicitly limit validation to language suitability and
executability, not improved red-team effectiveness.

### SRC-0029 - Hatebur, Heisel and Schmidt (2006)

Role: documentation-plus-model security problem framing and problem-to-specification refinement.
The method starts from a bounded context, environmental domains, interfaces, shared phenomena,
a security requirement, domain knowledge and explicit assumptions. It then instantiates a security
problem frame, introduces a generic solution principle through a concretized frame and finally
instantiates a protocol and concrete mechanism.

The source strengthens the separation between the security problem, the concretized requirement,
the generic protocol and the implementable specification. Attacker capability and biddable-domain
assumptions constrain mechanism selection, while two implication obligations express conditional
adequacy from specification to concretized requirement and from concretized requirement to the
original security requirement.

The paper does not derive context or problem diagrams from heterogeneous documentation, automate
frame matching or mechanism selection, or provide a solver or model checker for the stated
obligations. Every substantial modeling and selection decision remains with the security engineer.
The remote-display example is illustrative and develops only one of six identified subproblems; it
does not establish completeness, comparative advantage or current cryptographic suitability.

### SRC-0030 - Mbaka et al. (2025)

Role: current controlled evaluation of the incremental usefulness of a DFD during validation of
pre-identified security threats. All participants received a textual scenario, STRIDE material,
structured threat descriptions and assumptions, and a sequence diagram; only the intervention
group additionally received a DFD.

Across a first and confirming experiment with 98 novice student participants, the additional DFD
did not produce a statistically significant improvement in correctly classifying actual or
fabricated threats. With the authors' equivalence margin of one, TP and TN were equivalent
separately, while equivalence was not established for the combined TP+TN score.

Participants who received both diagrams perceived the DFD as more useful than the sequence
diagram. This perception did not translate into a correctness improvement. Threat descriptions
and assumptions were consistently useful, supporting explicit evidence-bearing threat records
rather than DFD-only reasoning.

The study does not compare against a no-model condition, evaluate threat elicitation or expert
practitioners, or measure longitudinal maintenance. Its result challenges automatic DFD-centric
claims without establishing that DFDs are generally ineffective.

## Initial DDTA separation

```text
raw and governed project documentation
-> Base Analysis construction
-> methodology-specific threat analysis
-> optional problem-to-mechanism refinement
-> optional executable attack and mitigation regression
-> threat validation against structured evidence and model views
-> reviewed findings
-> security requirements
-> satisfaction and assurance evidence
-> accepted assurance or iteration
```

SRC-0026 mostly maps methodology-specific threat analysis. SRC-0003 demonstrates a scenario-based
implementation after a functional scenario view exists. SRC-0004 demonstrates a goal-oriented
implementation after a structured primal model exists. SRC-0027 adds a downstream assurance
layer after problem-context and behavior views exist. SRC-0028 adds executable attack regression
after precise scenario and behavior views exist. SRC-0029 adds a problem-frame refinement overlay
after context, domain, interface, requirement, assumption and attacker-capability views exist.
SRC-0030 adds controlled evidence that an additional DFD did not improve novice threat-validation
correctness when a sequence diagram and structured textual material were already provided, although
the DFD was perceived as more useful. DDTA must still investigate how heterogeneous documentation
becomes the neutral assets, actors, goals, interactions, objects, operations,
domains, phenomena and scenarios consumed by these overlays, arguments and tests.

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
- precise hostile scenarios can be woven into functional behavior and executed as regression tests;
- model animation and attack execution are not equivalent to formal verification;
- requirements-level models may defer storage, network and implementation-dependent attacks;
- structured scenarios, goal models, problem contexts and EIODs are not equivalent to raw heterogeneous documentation;
- security problem frames preserve the distinction between a security problem, a generic solution principle and a concrete mechanism;
- refinement and specification adequacy remain conditional on explicit assumptions and domain knowledge;
- attacker-capability assumptions may constrain mechanism strength without proving threat completeness;
- actual effectiveness and perceived usefulness can diverge for an additional architectural view;
- incremental model value depends on the task, baseline, population and outcome being measured;
- structured threat descriptions and assumptions can be central evidence during threat validation.

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
assumptions. SRC-0028 adds executable regression evidence for known hostile traces. SRC-0029 adds
conditional problem-to-specification adequacy obligations based on explicit assumptions and domain
knowledge. SRC-0030 adds controlled evidence that perceived usefulness of a model view need not
produce a measurable correctness improvement.

All four evidence forms remain relative to their modeled context, premises, behaviors, attacks,
mechanism choices, participants, baselines and measured outcomes. None establishes global threat
completeness or implementation security. Completion conditions, precise discovery rules,
comparative validation and longitudinal maintenance evidence remain weak.

DDTA candidate controls:

- typed outputs;
- source provenance;
- extracted versus inferred status;
- scenario-level review dispositions;
- progressive lightweight and extensive analysis profiles;
- derivation rule, premises and proof status;
- software requirement versus environmental expectation responsibility;
- preserved alternative countermeasures and selection rationale;
- separate security problem, concretized requirement, generic protocol, concrete mechanism and specification;
- versioned attacker-capability assumptions and domain knowledge;
- explicit conditional adequacy obligations with evidence and verification status;
- explicit task, baseline, population and outcome for each empirical evaluation;
- separate actual effectiveness, perceived usefulness and maintenance cost;
- information-cue provenance across text, model views, assumptions and external knowledge;
- security-goal-to-requirement validation evidence;
- outer-argument premises, logic and proof status;
- inner claims, grounds, warrants, rebuttals and trust assumptions;
- primary-to-secondary cover/replace ancestry;
- separate core behavior, attacker modification, attack test and mitigation aspect;
- weave scope, order, dependency and conflict evidence;
- versioned attack regression suite with explicit trace-level pass/fail semantics;
- deferred attack candidates with missing-representation reasons;
- coverage declaration;
- explicit stopping condition;
- incomplete-input diagnostics;
- human review state;
- separate verification evidence;
- versioned reruns after change.

## Primary-study selection queue

### New sources to retrieve

1. A recent review of automated threat-modeling tools and model-based security testing.

These sources cover:

```text
use-case text
goal models
problem descriptions
behavioral models
architecture/DFD overlays
quality assurance
```


## Scenario, anti-goal, assurance, execution, problem-frame and validation contrast

| Dimension | SRC-0003 | SRC-0004 | SRC-0027 | SRC-0028 | SRC-0029 | SRC-0030 |
|---|---|---|---|---|---|---|
| Starting view | functional scenarios | goal, object, agent and domain models | problem context, phenomena and behavior | EIOD and sequence behavior | context, domains, interfaces and security requirement | scenario, sequence diagram, structured threats and optional DFD |
| Main structure | harmful scenario | intentional AND/OR anti-goal graph | constrained requirement and argument graph | modification, attack and mitigation scenarios | security problem frame and concretized frame | actual/fabricated threat-validation experiment |
| Formality | mostly informal | optional temporal logic and formal regression | formal outer proof plus informal inner argument | formal trace semantics and executable FSMs | conditional implication obligations; no implemented verifier | statistical difference and equivalence tests |
| Security output | misuse and mitigation | anti-requirement and vulnerability | primary/secondary security constraints | composed behavior and attack tests | concretized requirement, protocol, mechanism and specification | correctness and perceived-usefulness evidence |
| Assumption handling | template fields | domain properties | trust assumptions and rebuttals | pre/postconditions and interactive path choices | explicit attacker capability and domain knowledge | explicit threat assumptions used in binary validation |
| Assurance | review status and trace links | local proof and derivation evidence | conditional satisfaction evidence | regression over known attack traces | conditional refinement and specification adequacy | expert-curated ground truth and measured participant outcomes |
| Empirical evidence | descriptive examples | four anti-model cases | one industrial research application | two preliminary case studies | one illustrative remote-display case | controlled and confirming experiment with 98 students |

All six approaches are pre-code. None solves source-document interpretation, assertion-level
provenance or global completeness. They support distinct methodology, assurance, executable-scenario,
problem-refinement and empirical-validation roles over a neutral Base Analysis.

## Evidence still missing

- automatic extraction of Base Analysis entities, scenario views and goal views from heterogeneous documentation;
- sentence-to-model, sentence-to-scenario, sentence-to-goal and sentence-to-context provenance;
- management of missing and contradictory documentation;
- governed trust-assumption acceptance and residual-risk criteria;
- automatic argument maintenance and change impact;
- automatic document-to-problem-frame construction and frame-applicability checking;
- governed mechanism selection and automated validation of conditional adequacy obligations;
- current tool maturity;
- continuous rerun and stale detection;
- current LLM/RAG performance;
- evaluation against expert-created threat models;
- expert and no-model replications of model-view usefulness;
- longitudinal model-maintenance cost and utility across the SDLC;
- review effort and accepted-finding yield.

## Temporal caveat

SRC-0026 is a strong historical map but cannot describe the 2026 state of automation or tools.
Every maturity claim must be updated through recent systematic reviews and empirical studies.
SRC-0029 remains conceptually relevant for problem/solution separation and explicit assumptions,
but its 768-bit RSA example is obsolete and must not be reused as current cryptographic guidance.
SRC-0030 is current 2025 empirical evidence, but its conclusions remain bounded to novice students,
two scenarios, one fabricated-threat pattern and a sequence-diagram baseline.

## Reading order

```text
SRC-0026 historical method taxonomy
-> SRC-0003 scenario-based misuse cases
-> SRC-0004 goal-oriented anti-models
-> SRC-0027 explicit satisfaction assurance
-> SRC-0028 executable misuse regression
-> SRC-0029 security problem frames
-> SRC-0030 empirical DFD threat validation
-> recent automated-tool review
```
