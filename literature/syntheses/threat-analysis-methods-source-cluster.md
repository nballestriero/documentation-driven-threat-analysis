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

### SRC-0031 - Granata and Rak (2024)

Role: recent systematic analysis of automated threat-modelling techniques and supporting tools,
combined with an illustrative WordPress comparison. The review defines automation after a system
has already been represented as a typed model and maps model types, threat classifications,
selection mechanisms and tools across 55 included studies.

DFD and graph-based representations dominate, STRIDE is the most frequent classification, and
label- and relationship-based catalogue selection are the most common automation mechanisms. The
review also identifies richer use of properties, protocols, relationship roles, propagation and
rule or pattern matching.

The WordPress comparison shows that Microsoft, Threat Dragon, SLA-generator and PyTM attach threats
to different units and produce lists with different scope and granularity. Raw candidate counts are
therefore not a quality or completeness measure. The comparison has no independent ground truth,
precision, recall, effort or accepted-finding metric and contains unresolved count discrepancies.

The source establishes a model-to-candidate-threat automation boundary, not automatic interpretation
of heterogeneous documentation. Human work remains necessary for model construction, catalogue and
rule maintenance, candidate review, prioritization, deduplication and disposition. The review is not
a dedicated systematic study of model-based security testing, so that branch remains open.

### SRC-0032 - Lonetti, Bertolino and Di Giandomenico (2023)

Role: recent Rapid Review of model-based security testing for IoT. The source maps the
formalism, test objective, attack model, generation technique, execution artifact, target domain
and attack coverage of 17 primary studies selected from 803 considered publications.

The review establishes a model-to-test boundary. Requirements, specifications or an existing SUT
may inform construction of a security-enriched test model. Test-selection criteria then produce
abstract tests, which must be concretized through scripts, adapters and execution environments
before they can provide implementation-level evidence.

UML with OCL and timed automata are the most frequent formalism families. Attack trees and threat
templates supplement the system model in several studies. More than 40 percent of studies use
model-coverage criteria, almost 30 percent combine verification and testing, and more than 30
percent combine MBST with another strategy such as penetration testing, fuzzing or model learning.

The selected studies cover only about 40 percent of the adopted IoT attack taxonomy and are mostly
exploratory. Model complexity, heterogeneous and evolving environments, adapter construction,
limited attack coverage and the absence of large realistic comparisons prevent claims of complete
or mature automated security assurance.

### SRC-0033 - Umar and Lano (2024)

Role: recent systematic review of implemented automated requirements-engineering support. The
source classifies 85 empirical studies by input, generated artifact, RE phase, degree of
automation, development technique and evaluation method.

Natural-language text is the input for 94 percent of tools. UML is the most common model output,
but the reviewed tools also perform omission detection, consistency checking, validation,
classification, duplicate detection, mining, reuse and security-related analysis. The dominant
transformation is therefore documentation-to-candidate-artifact rather than only text-to-UML.

Most tools are semi-automated and most are one-shot. Even tools labelled fully automated produce
artifacts for human verification. The review explicitly identifies traceability from generated
elements back to source statements, model evolution, human-in-the-loop governance, industrial
validation and common benchmark cases as unresolved needs.

The source provides evidence that automated Base Analysis construction can begin from project
documentation, but it does not establish a complete, semantically correct, neutral or continuously
synchronized model. Generated outputs must remain candidates with source provenance, uncertainty,
review disposition and stale-state control.

### SRC-0034 - Souza, Moreira and Goulão (2019)

Role: systematic mapping study of methods that derive architectural models from requirements
specifications. The source classifies 39 primary studies by starting representation, requirements
type, benefits, analysis-synthesis-evaluation coverage, architectural views, ADL, automation and
validation.

Textual requirements are the largest input group, but goal models, feature models, problem frames,
sequence diagrams and unspecified architect-selected inputs also occur. All studies cover functional
requirements; external non-functional requirements are almost absent. Architectural view names and
notations are heterogeneous, and two thirds of the studies do not use or do not identify a standard
ADL.

Automation is partial and representation-specific. Methods transform a specific requirement form
into a specific candidate architectural model, which an architect then analyzes and improves. No
complete automated approach is identified. Decisions, alternatives and trade-offs depend strongly on
tacit expert knowledge, while requirements-to-architecture traceability appears as a claimed benefit
in only one study.

The source establishes that requirements-to-architecture is a governed decision boundary rather
than a deterministic model conversion. Candidate architecture needs source provenance, explicit
alternatives, decision rationale, multi-view semantics, satisfaction evaluation and change control.
The historical corpus does not establish current LLM-based architecture synthesis.

### SRC-0035 - Ferrari, Abualhaija and Arora (2024)

Role: current exploratory study of GPT-3.5 generation of abstract UML sequence diagrams from 28
realistic requirements documents across 18 domains and three requirement formats. Researchers
construct 87 variants containing additions, removals, modifications, ambiguity, inconsistency and
incompleteness, score first-pass outputs on five quality dimensions and derive 23 issue categories
from evaluation logs.

The generated diagrams score strongly for PlantUML-oriented standard adherence, understandability
and terminology. Correctness does not score significantly above the neutral value, and completeness
remains imperfect. Visually convincing output can omit conditions, hide contradictions, mishandle
numbers and timing, assign behavior to the wrong component, invent terms or include incomplete trace
annotations.

The source establishes an LLM document-to-candidate-model boundary, not autonomous model
construction. Prompt, provider, model, interface, session, memory, context and renderer are execution
provenance. Source coverage, behavioral semantics, terminology mappings and traces require separate
validation, followed by human correction and disposition.

The study uses one historical GPT-3.5 configuration, one prompt pattern, functional requirements and
no gold-standard diagram. Its failure taxonomy is directly useful, while performance claims require
contemporary multi-model replication.

### SRC-0036 - Garaccione, Calabrese, Coppola and Ardito (2025)

Role: current multi-model empirical comparison of LLM generation of UML class diagrams from 15
Italian university exercises. GPT-4o, DeepSeek v3, Gemini 2.5 Pro and Qwen 3 receive the same
role-based few-shot prompt through free web interfaces and produce Apollon JSON diagram candidates.

The source decomposes quality into syntax errors, semantic errors and reference-solution
completeness. GPT-4o and Gemini have no syntax errors in the 15 cases, DeepSeek has the lowest mean
semantic-error count, Gemini has the highest mean completeness, and Qwen is significantly worse on
syntax. Most other pairwise semantic and completeness differences are not statistically significant,
so the paper establishes different error profiles rather than one universal winner.

Association type and multiplicity dominate semantic failures. The figures show that a model can
produce parser-compatible, structurally plausible output while still encoding the wrong containment,
generalization, direction or cardinality. Syntax validation, source coverage and structural-semantic
validation must therefore remain independent gates.

The study establishes a multi-model document-to-candidate-structural-model boundary, not autonomous
Base Analysis. It uses educational functional requirements, dynamic June-2025 web interfaces, no
assertion-level traces, no repeated runs, no change propagation and no security or privacy evaluation.
Every candidate still requires generation provenance, source-to-element trace review, correction and
explicit disposition.

### SRC-0037 - Abualhaija et al. (2025)

Role: direct empirical study of LLM- and RAG-assisted extraction of privacy requirements from the
GDPR and complementary legal sources. Six experts construct a reference set of 61 access and 47
portability requirements with source links, and XTRAREG generates candidate requirements, references
and rationales using GPT-3.5 or GPT-4o.

The source separates correctness, coverage, groundedness, plausibility and duplication. With GPT-4o,
ZSL and RAG, 18 of 22 ACC outputs and 12 of 14 PRT outputs are correct or partially correct, but only
16 of 61 ACC and 8 of 47 PRT reference requirements are identified. Grounded references fall to
68.2 percent for ACC and 50 percent for PRT. High acceptance among generated outputs therefore does
not establish high coverage of applicable obligations.

RAG improves most automated metrics but does not produce a comprehensive list beyond the directly
relevant GDPR articles. Generated outputs can be duplicated, generic, framed from the wrong
perspective, non-actionable, incomplete or misgrounded. Legal-source selection, applicability,
interpretation, correction and acceptance remain expert responsibilities.

For DDTA and the parallel ThreatForge project, the source establishes only a future-compatibility
boundary. The thesis does not implement regulatory extraction, legal review, compliance scoring, a
legal plugin or a new privacy document model. Existing provenance, candidate-review, Target Project
and methodology-neutral Base Analysis boundaries should merely avoid preventing a later governed
extension.

## Initial DDTA separation

```text
raw and governed project documentation
-> optional accepted legal/privacy requirements as governed project documentation (future extension only)
-> automated or assisted extraction into candidate requirement and model artifacts
-> optional LLM generation of candidate behavioral or structural model projections
-> syntax, source-coverage, semantic and traceability validation
-> reviewed Base Analysis construction
-> requirements-to-architecture concern, decision and multi-view projection
-> reviewed and evaluated candidate architecture
-> methodology-specific threat analysis
-> automated model-to-threat candidate generation when a typed model exists
-> optional problem-to-mechanism refinement
-> optional executable attack and mitigation regression
-> threat validation against structured evidence and model views
-> reviewed findings
-> security requirements
-> optional model-based security test generation and concretization
-> executable conformance or vulnerability evidence
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
the DFD was perceived as more useful. SRC-0031 maps model-to-candidate-threat automation after a
typed model exists and shows that catalogues, rules, asset semantics and granularity differ across
tools. SRC-0032 maps the subsequent model-to-security-test boundary, distinguishing security
properties, attack models, test-selection criteria, abstract tests, concretization, adapters,
execution environments and observed evidence. SRC-0033 shows that natural-language requirements
can be processed into candidate UML and other requirement artifacts, while traceability,
uncertainty, model evolution, industrial validation and common benchmarks remain weak. SRC-0034
maps the following requirements-to-architecture transition and shows that transformation rules are
representation-specific, decisions remain tacit, traceability is exceptional and architecture
validation is often absent. SRC-0035 demonstrates that GPT-3.5 can produce readable first-pass
sequence diagrams from realistic requirements while still omitting, altering or inventing behavior
behind strong syntax and terminology. SRC-0036 adds a four-model class-diagram comparison and shows
that syntax, completeness and semantic correctness can favor different models, while association
type and multiplicity remain shared failure points. SRC-0037 adds direct privacy-requirement
generation evidence and shows that high correctness among generated outputs can coexist with low
coverage and incomplete or misgrounded legal references. For the thesis, this result establishes
future compatibility only; legal extraction and compliance analysis remain outside implementation
scope. DDTA must still establish how heterogeneous documentation becomes reviewed neutral assets,
actors, goals, interactions, objects, operations, domains, phenomena, scenarios and architectural
decisions consumed by these overlays, arguments and tests.

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
- structured threat descriptions and assumptions can be central evidence during threat validation;
- automated threat selection commonly begins only after a typed model has been supplied;
- labels, properties, relationships, protocols, propagation and catalogues can activate candidates;
- tools can attach threats to different model units and produce non-comparable granularity;
- generated candidate count is not evidence of correctness or completeness;
- security tests can be derived automatically after a security-enriched test model exists;
- abstract tests require concretization, adapters and an execution environment;
- model coverage, attack-class coverage and global security completeness are distinct;
- model checking evidence and executable test evidence should remain separate but traceable;
- natural-language text is the dominant direct input to automated requirements-engineering tools;
- automated RE produces heterogeneous candidate models, structured requirements and quality findings;
- a fully automated transformation step still requires expert verification in the wider RE process;
- most reviewed tools are one-shot and do not establish continuous synchronization;
- source-to-generated-artifact traceability and common comparative benchmarks remain open;
- requirements-to-architecture methods start from textual or modeled requirements and often use intermediate representations;
- architectural synthesis requires alternatives, quality-attribute trade-offs and expert decisions;
- partial transformations produce candidate views that require manual analysis and improvement;
- architectural-view names and ADLs are heterogeneous and can lose semantics when normalized;
- explicit requirements-to-architecture traceability is rare in the mapped corpus;
- generated architecture does not establish requirements satisfaction or evaluation evidence;
- a general-purpose LLM can produce abstract sequence-diagram candidates from realistic requirements;
- high understandability, terminology and parser compliance do not establish correctness or completeness;
- ambiguous, inconsistent, numerical and temporal requirements can be omitted or concealed;
- generated actors, components, ordering, states and terminology can contradict the source;
- LLM-produced trace notes and requirement identifiers can be incomplete or inaccurate;
- provider, model, prompt, session, memory, context and renderer state affect reproducibility;
- requirement modifications can be ignored and every accepted model needs explicit stale-state control.
- a contemporary multi-model comparison can produce different descriptive winners for syntax, semantics and completeness;
- syntax-valid class diagrams can still contain incorrect association types, directions and multiplicities;
- selecting a provider or model does not replace artifact-level coverage, semantic and trace validation;
- legal requirements can depend on authoritative sources beyond the primary regulation;
- generated privacy requirements can be largely correct or partially correct while covering only a small fraction of the expert reference set;
- retrieved context, citations and plausible rationales still require separate legal-grounding review;
- legal extraction remains a future-compatible extension rather than a thesis implementation requirement;Researcher conclusion for DDTA:

```text
documentation_only is possible for some techniques
documentation_plus_model is required for others
document_to_candidate_artifact can be automated or assisted from natural-language requirements
document_to_llm_candidate_model can produce readable but semantically unreliable projections
llm_candidate_model_to_accepted_model requires syntax, coverage, semantic and trace validation
llm_candidate_structural_model_to_accepted_model additionally requires association and multiplicity validation
legal_source_to_candidate_requirement requires applicability, authority, actionability, coverage and grounding review
future_legal_analysis_compatibility does not require implementation within the thesiscandidate_artifact_to_base_analysis requires source provenance and human review
base_analysis_to_candidate_architecture requires explicit concerns, alternatives and decisions
candidate_architecture_to_accepted_architecture requires multi-view review and satisfaction evidence
model_to_candidate_threat can be automated after a typed model exists
model_to_abstract_security_test can be automated after a security test model exists
abstract_test_to_execution requires governed concretization and adapters
raw_documentation_to_trustworthy_neutral_model is not established
```

The first analysis should therefore remain documentation-primary. Later code analysis should
corroborate, contradict or refine the prior model rather than become a hidden prerequisite.

## Outcome and assurance gap

The reviewed techniques distinguish threats, mitigations and security requirements. SRC-0027
shows how explicit assurance can be structured as conditional proof plus arguments for trust
assumptions. SRC-0028 adds executable regression evidence for known hostile traces. SRC-0029 adds
conditional problem-to-specification adequacy obligations based on explicit assumptions and domain
knowledge. SRC-0030 adds controlled evidence that perceived usefulness of a model view need not
produce a measurable correctness improvement. SRC-0031 adds model-to-candidate-threat automation
through typed elements, catalogues and rules, while showing that generated lists differ in scope and
granularity. SRC-0032 adds model-to-security-test derivation, the abstract-to-concrete test boundary
and implementation-level execution evidence. SRC-0033 adds documentation-to-candidate-artifact
automation and shows that provenance, review, evolution, benchmark and adoption evidence remain
incomplete. SRC-0034 adds the requirements-to-architecture decision boundary and shows that tacit
knowledge, weak traceability, heterogeneous views and insufficient evaluation remain central gaps.
SRC-0035 adds direct LLM document-to-behavioral-model evidence and shows that polished syntax,
terminology and understandability can coexist with omissions, incorrect behavior and weak traces.
SRC-0036 adds multi-model document-to-structural-model evidence and shows that parser-compatible
output and relatively high coverage can coexist with incorrect association type and multiplicity.
SRC-0037 adds regulatory-document-to-requirement-candidate evidence and shows that output
correctness, obligation coverage and legal grounding can diverge. Its project consequence is limited
to preserving future extensibility; no legal-analysis subsystem is required in the thesis.

All ten evidence forms remain relative to their source documents, model and session state, prompts,
modeled context, premises, behaviors, attacks, mechanism choices, architectural alternatives,
decisions, participants, baselines, transformation pipelines, catalogue versions, rule semantics,
test models, selection criteria, adapters, oracles, environments and measured outcomes. None
establishes global threat completeness, a complete neutral Base Analysis, a uniquely correct
architecture, a source-faithful LLM projection or implementation security. Completion conditions,
precise discovery rules, normalized cross-tool evaluation, provenance assurance,
architecture-satisfaction evidence, LLM semantic assurance, oracle assurance and longitudinal
maintenance evidence remain weak.

DDTA candidate controls:

- typed outputs;
- source document, version, segment and assertion provenance;
- future legal-source authority, jurisdiction, effective-date and applicability metadata without legal semantics in the core;
- separate legal correctness, obligation coverage and grounding results if a later regulatory extension is introduced;- extracted linguistic fact versus inferred entity or relation status;
- transformation pipeline, rule, ontology, model or prompt version;
- confidence, alternatives and external domain-knowledge dependencies;
- human-intervention stage, correction history and review disposition;
- one-shot versus maintained-editor execution mode;
- generated-artifact stale state and regeneration trigger;
- selected source assertions, exclusions, decomposition and requirement-quality state;
- LLM provider, model ID, immutable snapshot and interface or API version;
- system prompt, user prompt, template, sampling parameters and generation timestamp;
- session, conversation, memory, retrieval context, glossary and domain-knowledge provenance;
- generated textual notation plus parser and renderer identity and version;
- assertion coverage states for represented, omitted, contradicted, added and abstracted content;
- separate syntax, notation-semantic, behavioral-semantic and domain validation results;
- proposed versus verified source-to-model traces and terminology mappings;
- output alternatives, variability, human corrections and final disposition;
- architecturally significant requirement and concern classification;
- candidate architectural alternatives and comparison criteria;
- decision, rationale, quality-attribute trade-off and external knowledge provenance;
- pattern, style, tactic and deployment-choice identity;
- typed architectural views with declared semantics and ADL version;
- requirement-to-decision-to-element traceability;
- architecture-evaluation method, satisfaction criteria and result evidence;
- architectural knowledge-vaporization and stale-decision controls;
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
- versioned model projection, threat catalogue and selection rule set;
- candidate activation evidence linking element, relation, properties and applied rule;
- duplicate and overlap handling across catalogues and levels of granularity;
- explicit generated, accepted, rejected, deferred and duplicate candidate states;
- versioned security-test projection and security-property set;
- attack-model or threat-template identity and transformation evidence;
- test-selection criterion with explicit model and attack coverage semantics;
- separate abstract test, concretized test, adapter and executable script artifacts;
- adapter, target environment, oracle and verdict semantics;
- expected versus observed execution evidence with blocked and inconclusive states;
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

Automated threat modelling, model-based security testing, broad automated requirements engineering,
the historical requirements-to-architecture boundary, LLM behavioral and structural model
generation, and direct privacy-requirement generation are now covered by SRC-0031 through SRC-0037.
The final central reading should focus on maintenance, provenance, reproducibility, correction effort,
accepted-artifact yield or a contemporary closing synthesis.

```text
maintained candidate artifact or analysis evidence
-> source, model, prompt, version and change provenance
-> correction effort, acceptance yield and stale detection
-> closing evidence for thesis limits and evaluation
```


## Scenario, anti-goal, assurance, execution, problem-frame, validation, automation, MBST, automated-RE, architecture and LLM model-generation contrast

| Dimension | SRC-0003 | SRC-0004 | SRC-0027 | SRC-0028 | SRC-0029 | SRC-0030 | SRC-0031 | SRC-0032 | SRC-0033 | SRC-0034 | SRC-0035 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Starting view | functional scenarios | goal, object, agent and domain models | problem context, phenomena and behavior | EIOD and sequence behavior | context, domains, interfaces and security requirement | scenario, sequence diagram, structured threats and optional DFD | typed graph, DFD, code model or asset list plus catalogue/rules | security-enriched system/test model plus optional attack model | natural-language requirements plus optional domain knowledge, models and metadata | textual or modeled requirements plus NFRs and domain concerns | realistic functional requirements in shall, use-case and user-story formats |
| Main structure | harmful scenario | intentional AND/OR anti-goal graph | constrained requirement and argument graph | modification, attack and mitigation scenarios | security problem frame and concretized frame | actual/fabricated threat-validation experiment | automated candidate selection and cross-tool comparison | model-to-abstract-test derivation and concretized execution | document-to-candidate-artifact processing and tool-landscape comparison | analysis, alternatives, architectural decisions, views and evaluation | single-shot LLM generation plus expert quality and issue analysis |
| Formality | mostly informal | optional temporal logic and formal regression | formal outer proof plus informal inner argument | formal trace semantics and executable FSMs | conditional implication obligations; no implemented verifier | statistical difference and equivalence tests | typed mappings, Boolean conditions and catalogue/rule matching | UML/OCL, timed automata, CPN, attack trees and coverage criteria | NLP, ML, ontology, rules and heterogeneous output schemas | representation-specific rules, heterogeneous views and ADLs | GPT-3.5 free-form interpretation rendered as PlantUML sequence diagrams |
| Security output | misuse and mitigation | anti-requirement and vulnerability | primary/secondary security constraints | composed behavior and attack tests | concretized requirement, protocol, mechanism and specification | correctness and perceived-usefulness evidence | candidate threats, mitigations and control mappings | abstract tests, concrete scripts and execution observations | candidate UML, structured requirements and quality findings | candidate architectural elements, relations, decisions and views | candidate behavioral interactions, actors, conditions and trace notes |
| Assumption handling | template fields | domain properties | trust assumptions and rebuttals | pre/postconditions and interactive path choices | explicit attacker capability and domain knowledge | explicit threat assumptions used in binary validation | model properties, technologies, protocols and rule conditions | security properties, test purposes, adapters, environment and oracle | domain knowledge, preprocessing, interpretation and reviewer corrections | architect knowledge, quality trade-offs, patterns, styles and alternatives | prompt context, implicit pretrained knowledge and analyst-supplied clarification |
| Assurance | review status and trace links | local proof and derivation evidence | conditional satisfaction evidence | regression over known attack traces | conditional refinement and specification adequacy | expert-curated ground truth and measured participant outcomes | element-to-candidate trace; no independent completeness ground truth | model-to-test trace and SUT evidence; partial attack coverage | human verification; no common source-provenance or benchmark contract | manual refinement; requirements-satisfaction evaluation absent in most methods | expert source comparison; no gold standard; generated traces can be incomplete |
| Empirical evidence | descriptive examples | four anti-model cases | one industrial research application | two preliminary case studies | one illustrative remote-display case | controlled and confirming experiment with 98 students | 55-study SLR plus one illustrative WordPress comparison | Rapid Review of 17 mostly exploratory IoT studies | SLR of 85 heterogeneous implemented-tool studies | mapping study of 39 mostly weakly evaluated derivation methods | 28 documents, 87 variants, five scores, kappa 0.67 and 23 issue categories |

All eleven approaches are pre-code, documentation-primary, requirements-primary, model-primary,
LLM-candidate-producing or test-evidence producing. None establishes a trustworthy complete neutral
Base Analysis, assertion-level provenance, a uniquely correct architecture, a source-faithful LLM
projection and global completeness together. They support distinct documentation-processing,
architectural-decision, methodology, assurance, executable-scenario, problem-refinement,
empirical-validation, candidate-generation and security-testing roles over governed project evidence.

### SRC-0035 and SRC-0036 LLM-projection contrast

| Dimension | SRC-0035 | SRC-0036 |
|---|---|---|
| Generated view | behavioral sequence diagram | structural class diagram |
| Models | one GPT-3.5 web configuration | GPT-4o, DeepSeek v3, Gemini 2.5 Pro and Qwen 3 web interfaces |
| Input evidence | 28 realistic functional-requirement documents and 87 variants | 15 Italian university exercises |
| Output representation | PlantUML rendered with PlantText | Apollon JSON |
| Main assurance result | strong syntax and readability can hide omitted or incorrect behavior | syntax and completeness can coexist with wrong associations and multiplicities |
| Trace and change evidence | generated traces can be incomplete; modifications can be ignored | assertion-level traces and change handling are absent |
| DDTA role | candidate behavioral projection | candidate structural projection |

Together they establish that every generated view needs notation-specific syntax checks plus
source-coverage, semantic, trace and human-acceptance evidence. Neither a clear rendering nor a
provider-level model choice is an acceptance criterion.

### SRC-0035, SRC-0036 and SRC-0037 generated-artifact contrast

| Dimension | SRC-0035 | SRC-0036 | SRC-0037 |
|---|---|---|---|
| Generated artifact | behavioral UML sequence view | structural UML class view | privacy requirement text with reference and rationale |
| Input evidence | realistic functional requirements and variants | Italian educational requirements | GDPR plus selected complementary legal sources |
| Main failure boundary | readable syntax can hide omitted or incorrect behavior | syntax-valid structure can hide wrong relations | correct-looking outputs can have low coverage and weak grounding |
| Required independent gates | syntax, source coverage, behavior, traces | syntax, structural semantics, coverage, traces | actionability, correctness, obligation coverage, legal grounding |
| Human authority | analyst corrects and accepts model | analyst corrects and accepts model | legal and requirements experts select sources, interpret and accept |
| Thesis role | candidate behavioral projection evidence | candidate structural projection evidence | future-compatible regulatory-candidate boundary only |

Together they show that generated-artifact quality is multidimensional and artifact-specific. The
thesis implements neither autonomous model acceptance nor legal-compliance automation.

## Evidence still missing

- validated extraction of Base Analysis entities, scenario views and goal views from heterogeneous documentation;
- sentence-to-model, sentence-to-scenario, sentence-to-goal and sentence-to-context provenance;
- extracted-versus-inferred semantics, calibrated confidence and alternative interpretations;
- management of missing and contradictory documentation;
- common requirements benchmarks and cross-tool comparative evaluation;
- longitudinal accuracy, correction effort and stale-detection evidence for one-shot transformations;
- coverage of non-functional and security requirements comparable to functional-requirement evidence;
- validated identification of architecturally significant requirements and concerns;
- explicit alternatives, decision rationale and quality-attribute trade-off evidence;
- maintained requirement-to-decision-to-element traceability;
- comparable architecture-satisfaction evaluation and industrial evidence;
- semantic preservation across heterogeneous architectural views and ADLs;
- current requirements-to-architecture automation and LLM evidence beyond the historical corpus;
- contemporary multi-model generation evidence beyond educational class-diagram exercises;
- assertion-level gold standards or verified source-coverage mappings without requiring one canonical layout;
- broader industrial security, privacy and non-functional requirement generation evidence beyond two GDPR rights;
- reproducible provider/model/prompt/session configurations and longitudinal reruns;
- measured human correction effort, accepted-model yield and iterative prompting benefit;
- governed trust-assumption acceptance and residual-risk criteria;
- automatic argument maintenance and change impact;
- automatic document-to-problem-frame construction and frame-applicability checking;
- governed mechanism selection and automated validation of conditional adequacy obligations;
- current tool and catalogue maturity beyond SRC-0031's mainly 2022 search horizon;
- public reproducibility package and independent rerun of the WordPress comparison;
- precision, recall, false-positive rate and expert acceptance of generated threats;
- normalization and deduplication across tools with different scope and granularity;
- document/requirement-to-test-model provenance and uncertainty handling;
- shared model-coverage and attack-coverage semantics;
- validation of test oracles, concretization and adapter correctness;
- empirical MBST comparisons on large realistic systems;
- continuous rerun and stale detection;
- current LLM/RAG performance;
- legal-source applicability, authority, versioning and stale-state evidence for any future regulatory extension;
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
two scenarios, one fabricated-threat pattern and a sequence-diagram baseline. SRC-0031 was
published in the 2024 volume but its search and tool references extend mainly through 2022; all
2026 product, catalogue and maturity claims require fresh verification. SRC-0032 was published in
2023 from searches completed in April 2022 and includes only 17 mostly exploratory IoT studies
without quality assessment; current MBST maturity and tool claims require fresh verification.
SRC-0033 was published in 2024 from a search completed in December 2022; it primarily covers
classical NLP, ML and ontology techniques and cannot establish the performance, governance or
industrial maturity of generative-LLM-based RE in 2026. SRC-0034 was published in 2019 and its
selected primary studies extend through the mid-2010s; it remains useful for the tacit-knowledge,
traceability, multi-view and evaluation boundaries but cannot establish current tool or LLM-based
requirements-to-architecture maturity. SRC-0035 was published in 2024 but evaluates one GPT-3.5
configuration through the ChatGPT web interface; its failure categories remain relevant, while all
2026 performance, memory, prompting and comparative claims require contemporary replication.
SRC-0036 was published in 2025 and compares four models through free web interfaces available around
June 2025; its multidimensional quality and relationship-error findings remain relevant, while its
model ranking, interface behavior and provider descriptions must not be treated as current 2026 facts.
SRC-0037 was published in 2025 and uses fixed GPT-3.5 and GPT-4o snapshots with then-current OpenAI
and LangChain components. Its separation of correctness, coverage, groundedness and expert review
remains relevant, while exact performance and provider behavior require contemporary replication.

## Reading order

```text
SRC-0026 historical method taxonomy
-> SRC-0003 scenario-based misuse cases
-> SRC-0004 goal-oriented anti-models
-> SRC-0027 explicit satisfaction assurance
-> SRC-0028 executable misuse regression
-> SRC-0029 security problem frames
-> SRC-0030 empirical DFD threat validation
-> SRC-0031 automated threat-modelling review and tool comparison
-> SRC-0032 model-based security testing Rapid Review
-> SRC-0033 automated requirements-engineering support SLR
-> SRC-0034 requirements-to-architecture mapping study
-> SRC-0035 GPT-3.5 requirements-to-sequence-diagram study
-> SRC-0036 multi-model requirements-to-class-diagram comparison
-> SRC-0037 LLM/RAG GDPR privacy-requirement extraction case study
-> SRC-0038 maintenance, provenance, correction-effort or closing contemporary synthesis
```
