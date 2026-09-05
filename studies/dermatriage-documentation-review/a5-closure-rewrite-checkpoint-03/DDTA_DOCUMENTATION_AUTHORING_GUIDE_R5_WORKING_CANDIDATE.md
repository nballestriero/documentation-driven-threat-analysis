# DDTA Documentation Authoring Guide - R5 Working Candidate

**Status:** WORKING CANDIDATE / A5-HOLDOUT SYNTHESIS / NON-AUTHORITATIVE  
**Methodology authority retained:** `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R4.tex`  
**Repository baseline used for this synthesis:** `0e60754d21aa24ea487f3f60803b6b0cce8d2e2b`  
**Holdout evidence:** DermaTriage documentation review through A5 cumulative closure  
**Date:** 5 September 2026

> This revision is a complete forward rewrite of the documentation-authoring guidance after the DermaTriage A5 holdout work. It is deliberately **not promoted** to methodology authority by this artifact. R4 remains authoritative until this candidate is reviewed, regression-tested and explicitly promoted.

## 1. Purpose and thesis boundary

DDTA documents the **minimum sufficient governed meaning** of a project so that people can understand what the project is responsible for, what material commitments it makes, what operational obligations follow from those commitments, and what properties must hold, while preserving explicit gaps instead of inventing missing detail.

The thesis scope is intentionally narrower than the full universe of requirements engineering. The documentation metamodel keeps `SpecializedRequirement` abstract because governed specializations may exist for quality, performance, safety, reliability and other concerns. The concrete specialization developed and evaluated in depth by the thesis is `SecurityRequirement`, because the research objective is security analysis over governed documentation.

Accordingly:

```text
Requirement [abstract]
|-- FunctionalRequirement
`-- SpecializedRequirement [abstract]
    `-- SecurityRequirement       <- concrete specialization in thesis scope
```

A non-security specialization discovered in a real project is **not discarded**. Its governed meaning is preserved and its existence is evidence that the abstract `SpecializedRequirement` layer is useful. Designing a complete concrete subtype family for that concern is outside the thesis scope unless a later explicit research decision reopens it.

## 2. Epistemic discipline: what is allowed to become project truth

### 2.1 Authority

**Authority** answers: *which artifact is allowed to define project meaning at this moment?*

Before authoring or changing any DDTA element:

1. identify the current governed baseline;
2. identify the authorized source set;
3. distinguish current, candidate, working, historical and superseded artifacts;
4. preserve source/revision provenance;
5. do not use recency as a substitute for authority;
6. do not allow Base Analysis, tests, code, tooling or threat-analysis output to become project authority automatically.

Normal direction:

```text
governed project documentation
        -> Base Analysis
        -> security/threat analysis
        -> finding / clarification / change candidate
        -> governed review
        -> updated project documentation
        -> rebuilt Base Analysis
```

### 2.2 Governed meaning

A proposition is **governed** when the project has enough authority and semantic commitment for that proposition to be treated as part of the project contract.

A source may accurately describe a current implementation without governing that implementation choice for the future. Therefore:

```text
source-observed fact != automatically governed requirement
```

Example from DermaTriage:

```text
RETRAINING_THRESHOLD=50
```

is useful realization/configuration evidence. The governed meaning identified during the holdout is that classifier adaptation is accumulation-gated by a threshold. The exact value `50` is a current documented binding whose fixed normative status and change authority are not specified.

### 2.3 Semantic owner

The **semantic owner** is the project responsibility/decision/requisite to which a meaning belongs.

Before creating a new element ask:

```text
Who owns this meaning?
```

Do not infer ownership merely because two facts appear in the same component, API response, table or sentence.

### 2.4 NOT SPECIFIED

`NOT SPECIFIED` is a valid documented result when the source does not establish a material distinction sufficiently.

It is preferable to:

```text
NOT SPECIFIED
```

than to create a precise but invented rule.

### 2.5 STOP

`STOP` means that no additional independently governed meaning has been justified at the current layer and scope. It does **not** mean the project has no more implementation detail.

Examples:

- DermaTriage MR-02 stops at MR because specialist destination semantics are not sufficiently governed downstream.
- A FunctionalRequirement may stop at FR when no independently governed specialized property is established.

## 3. L1-L4 separation

DDTA separates four layers:

| Layer | Meaning | Typical contents |
|---|---|---|
| L1 | conceptual metamodel | MR, Decision, Requirement, FR, SR, SecurityRequirement, cardinalities and semantic invariants |
| L2 | authoring/representation contract | headings, fields, controlled terminology, normative-clause representation, registries |
| L3 | realization/model principles | schemas, validators, model loaders, derived indexes |
| L4 | tool support/conformance | editor assistance, checks, projections, reports |

A convenient YAML key or Markdown heading is not automatically a new L1 concept.

## 4. Normal DDTA authoring versus holdout reconstruction

### 4.1 Normal authoring

The normal process starts from project responsibility and governance:

```text
problem / responsibility
        -> authority
        -> MacroRequirement
        -> Decision
        -> FunctionalRequirement
        -> specialization review
        -> SecurityRequirement where governed
```

### 4.2 Existing-documentation validation

Reconstruction from traditional documentation is a **validation protocol**, not the normal production method:

```text
existing project documentation
        -> recover only supported project meaning
        -> apply normal DDTA authoring gates
        -> candidate governed documentation
        -> compare preserved / clarified / unresolved / lost
```

During a holdout, Base Analysis must not be consulted to decide what project meaning to introduce. A holdout is valuable precisely because it may expose a representability limitation.

## 5. End-to-end authoring sequence

The current working sequence is:

```text
A0 Authority/source gate
A1 Project problem framing
A2 MacroRequirement / D1
A3 Semantic sufficiency
A4 Decision / D2
A5 FunctionalRequirement / D3
A6 Requirement split
PRE-A7 scope + documentation<->BA consistency check
A7 SpecializedRequirement review
A8 SecurityRequirement review
A9 Cross-MR / consumed-service review
A10 Terminology / information / parameter bindings
A11 Downstream propagation / semantic regression
A12 Completeness / promotion readiness
ONLY THEN accepted Base Analysis
THEN security/threat analysis such as STRIDE / STRIDE-AI
THEN governed feedback into documentation
```

Local coherent-unit/split checks may occur before A6, but A6 is the project-wide regression of those local decisions.

## 6. A0 - Authority and source gate

Before deriving meaning record:

- source package identity and hash where available;
- principal semantic source;
- evidence/realization sources;
- excluded or non-authoritative reconstructions;
- current repository/methodology baseline.

For a holdout, distinguish at least:

```text
project authority
principal semantic source
evidence / realization source
historical reconstruction
analysis artifact
```

DermaTriage example:

- authoritative package: `DermaTriage-Docs-20260830T152637Z-1-001.zip`;
- package SHA-256: `E9ED2C507BEFB95F54A52084687CD1E8798863AE81CF69D09568864D8CBF280E`;
- OR2 Architecture Document: principal semantic source;
- test/training/dataset/configuration documents: supporting evidence unless they clearly govern project meaning;
- previous DDTA/BA reconstructions: not project authority.

## 7. A1 - Project problem framing

Start from the problem responsibility, not the implementation stack.

Bad framing:

```text
DermaTriage uses EfficientNet, Qwen, ChromaDB and BioMistral.
```

Better framing:

```text
DermaTriage supports early triage of dermatological cases concerning potentially oncological skin lesions,
using available case information to determine a priority of care and support routing toward appropriate specialist assistance.
```

The framing may expose unresolved boundaries. In DermaTriage, authority for definitive clinical diagnosis remains outside the established governed meaning.

## 8. A2 - MacroRequirement

A `MacroRequirement` governs one stable macro responsibility.

Recommended fields:

```text
Title
Intent
Context
Stakeholders
Scope
Assumptions / Constraints   [only when branch-wide]
dependsOn                  [only when genuinely governed]
```

### 8.1 MR split test

Split when two responsibilities can exist, evolve or be governed independently.

DermaTriage produced four macro responsibilities:

- MR-01 triage evaluation;
- MR-02 specialist routing support;
- MR-03 clinical review management;
- MR-04 controlled adaptation from accumulated clinical review evidence.

Clinical review and future adaptation were split because review can exist without retraining, and adaptation policy can change while review capture remains stable.

### 8.2 MR STOP

If the macro responsibility is governed but no material downstream choice/obligation is sufficiently specified, STOP at MR.

DermaTriage MR-02 is the canonical example: an indication of specialist destination is present, but complete selection/routing semantics are not sufficiently defined.

## 9. A3 - Semantic sufficiency

Ask for the **smallest critical proposition** whose ambiguity would create materially different project meanings.

Possible dispositions:

```text
AFFIRMED
DENIED
NOT SPECIFIED
CONFLICTING
REWORK
```

Numerical precision does not imply semantic sufficiency. A table may say `24h`, `48h`, `72h`, `7 days`; if the documentation does not say what event must occur within those times, from which trigger the interval runs, and who owns compliance, the timing semantics remain `NOT SPECIFIED`.

## 10. A4 - Decision

A `Decision` governs one material commitment that narrows exactly one MR.

Recommended structure:

```text
Context
Decision
Consequences
```

A Decision should survive reasonable implementation substitution.

### 10.1 Decision kinds

Use the existing kinds:

- `SELECTABLE` - materially different alternatives exist;
- `NECESSITY-CONSTRAINED` - project constraints force the commitment;
- `DEFAULT` - a default position is governed while change remains possible.

Do not create fake Decision wrappers merely because the hierarchy expects a Decision before FR.

### 10.2 Decision versus operational rule

A Decision answers *which material project position is adopted*. A FunctionalRequirement answers *what operational behavior is required because of that position*.

DermaTriage example:

```text
DEC-02: adopt P1-P4 as operational priority scale
FR-02: derive the concrete P-scale level from urgency/confidence
```

### 10.3 Numeric neutralization at Decision level

When a candidate Decision is dominated by a concrete number, replace the number with a symbolic value and ask whether the policy still exists.

Example:

```text
Every 10 corrections -> evolve prompt
```

Neutralize:

```text
When accumulated relevant evidence reaches threshold N -> evolve prompt
```

The surviving Decision is the accumulation-gated adaptation strategy. `10` is not what makes the Decision exist.

## 11. A5 - FunctionalRequirement

A `FunctionalRequirement` is one independently assessable operational obligation under exactly one Decision.

A strong FR states enough to determine:

- triggering/applicability condition;
- responsible project behavior;
- input/output/state meaning needed to assess it;
- material context binding;
- failure or non-satisfaction semantics where governed;
- deliberate exclusions.

### 11.1 One FR does not equal one sentence

```text
1 Requirement != 1 textual sentence
1 Requirement  = 1 coherent normative obligation
```

A mapping table may contain several normative clauses and still be one FR if all rows jointly express one coherent transformation.

DermaTriage FR-08:

```text
P1 -> HIGH
P2 -> HIGH
P3 -> MEDIUM
P4 -> LOW
```

is one FR, not four requirements.

### 11.2 Do not merely restate the Decision

A Decision such as “use clinical disagreement as qualifying evidence” may still need an FR that makes the operational qualification rule assessable.

### 11.3 Responsibility boundary before FR

Do not assign to the project a behavior owned by a consumed service, a clinician or another responsibility.

DermaTriage FR-03 records/correlates a clinical review; it does not claim that DermaTriage performs the clinical judgment.

### 11.4 Contextual binding

When a relation must remain tied to the same case/request/outcome to avoid a materially different result, preserve that binding in FR semantics.

## 12. Decision-to-Requirement completeness counterexample

Before declaring STOP below a Decision, ask:

```text
Can all current downstream Requirements be satisfied while this Decision is still violated?
```

- If **NO**, STOP may be justified.
- If **YES**, downstream coverage is incomplete; search for the missing FR/SR rather than reopening the Decision automatically.

DermaTriage DEC-05 exposed this rule. FR-04 and FR-05 could both be satisfied while one adaptation path incorrectly triggered the other. FR-11 was therefore required to govern lifecycle independence.

## 13. Parameter Governance Boundary

Do not create a requirement or document for every number.

The correct sequence is:

```text
source value
    -> semantic owner
    -> lifecycle / purpose
    -> requirement/property classification
    -> neutralize concrete value to symbolic parameter
    -> semantic materiality test
    -> exact-value governance test
    -> governed semantic parameter OR realization/configuration STOP
```

### 13.1 Gate Q1 - does meaning survive replacement by N?

If replacing the number by `N` destroys the governed proposition, the number may be part of the semantic rule itself rather than a replaceable parameter.

Example: the transformation `P2 -> HIGH` cannot be neutralized to `P2 -> X` without losing the governed meaning.

### 13.2 Gate Q2 - can parameter variation materially change governed behavior?

If no, the value is ordinary technical configuration and should normally stop below the semantic model.

If yes, preserve a semantic parameter.

### 13.3 Gate Q3 - is the concrete value itself governed?

- YES: preserve the exact value normatively.
- NO / NOT SPECIFIED: preserve the symbolic parameter and record the concrete value as a current binding.

DermaTriage examples:

| Semantic parameter | Current documented binding | Exact value governance |
|---|---:|---|
| `PromptEvolutionThreshold=N` | 10 | NOT SPECIFIED |
| `ClassifierAdaptationThreshold=N` | 50 | NOT SPECIFIED |
| `PromptEvidenceWindowSize=N` | 20 | NOT SPECIFIED |
| `AccuracyDegradationTolerance=T` | 5% | quantitative binding incomplete |
| `RollbackAccuracyDegradationThreshold=R` | 5% | quantitative binding incomplete |

The two `5%` values are **not** one parameter merely because the literal is equal. Semantic owner, lifecycle and purpose differ.

## 14. Information and realization bridge taxonomy

DDTA must preserve enough traceability to connect governed semantics to implementation without making implementation identifiers normative by default.

Observed bridge shapes:

```text
1. semantic concept
   -> data/state encoding

2. semantic parameter
   -> configuration value

3. semantic reference
   -> interface identifier

4. semantic reference
   -> governed transformation
   -> semantic output
   -> realization encoding
```

DermaTriage examples:

```text
ClinicianDisagreement
    -> source-observed encoding: agrees == False

ClassifierAdaptationThreshold=N
    -> current binding: 50

ClinicallyCorrectedPriority
    -> P1/P2/P3/P4 mapping
    -> ClassifierUrgencyTarget
    -> enum/string/class-index realization
```

The semantic concept remains stable even if a field name or enum representation changes.

## 15. A6 - Requirement split

A6 is the project-wide coherent-unit regression.

Split a Requirement when a part can be introduced, revised, retired, assessed, fail or be revalidated independently without changing the normative identity of the remaining parts.

Strong split indicators:

- different semantic owner;
- materially distinct failure mode;
- independent lifecycle/review;
- different specialization/security scope;
- independent change/revalidation.

Do not split merely because there are multiple verbs, multiple mapping rows or multiple test cases.

## 16. Pre-A7 scope and Documentation<->BA consistency check

Before A7 in the current thesis workflow perform a controlled consistency check:

1. verify that the documentation metamodel can preserve each discovered specialization meaning;
2. verify that the BA handoff can consume required project meaning without dictating document types;
3. preserve the thesis boundary: security specialization is the concrete research scope;
4. if a non-security specialization is discovered, preserve it without opening a full new subtype research program;
5. a pre-A7 BA probe, if used, is non-authoritative and exists only to test representability, not to decide project meaning.

## 17. A7 - SpecializedRequirement

A `SpecializedRequirement` is justified when an additional concern-specific property strengthens exactly one parent FR and can be governed independently from the ordinary functional behavior.

Semantic invariants:

- exactly one parent FR;
- conjunctive strengthening of the parent;
- removing the specialization leaves the ordinary function meaningful;
- no duplication of ordinary functional correctness;
- subordinate positive work may be required;
- an autonomous new capability belongs in a separate FR;
- realization mechanism is not the property;
- the specialization depends on the parent behavior.

### 17.1 Scope-limited specialization rule

In this thesis:

```text
specialization candidate
    -> security property? YES -> A8 SecurityRequirement
    -> security property? NO
         -> preserve governed property
         -> record extensibility evidence
         -> mark concrete non-security subtype OUTSIDE THESIS SCOPE
```

DermaTriage DEC-07 is the main holdout evidence: sensitivity non-degradation, false-low non-degradation and bounded accuracy degradation are plausible quality specializations of FR-09, but they are not security requirements and therefore do not justify expanding the thesis into a general quality-requirements taxonomy.

## 18. A8 - SecurityRequirement

A `SecurityRequirement` is a concrete specialized requirement in thesis scope.

Ask:

1. is the security property governed by project authority?
2. is its scope tied to a precise governed behavior/meaning?
3. can it evolve/fail independently from other properties?
4. are we stating a property rather than merely a mechanism?
5. is the security failure mode identifiable in the normative clauses?

Never infer:

```text
Confidentiality -> TLS
Integrity -> digital signature
Authorized provenance -> certificate
Authentication -> X-API-Key
```

unless the mechanism itself is a governed commitment.

Existing project documentation may already govern SecurityRequirements before threat analysis. Threat analysis may later produce **candidate** security obligations, but findings do not become SecurityRequirements automatically.

## 19. A9 - Cross-MR and consumed-service semantics

Distinguish:

```text
ownership
consumption
reference
dependency
second parent
```

They are not synonyms.

A FunctionalRequirement may reference a concept governed by another Decision/MR without acquiring a second parent.

DermaTriage DEC-11 consumes the P-scale domain governed under MR-01 while remaining owned by MR-04.

Consumed services do not become project-owned merely because their outputs are used.

## 20. A10 - Terminology, information, parameter and interface bindings

A10 consolidates the bridge ledger accumulated during authoring.

For each important datum classify it as one of:

1. governed normative meaning;
2. source-observed vocabulary/representation;
3. unresolved binding / NOT SPECIFIED;
4. current realization/configuration binding.

A10 should maintain structured registries rather than one document per value or field.

Do not invent requiredness, cardinality, type, missing-value policy, reset policy or change authority merely to make a data model look complete.

## 21. A11 - Downstream propagation and semantic regression

Recheck that upstream corrections are preserved through every descendant and reference.

Questions:

- did any downstream artifact silently narrow or widen an upstream meaning?
- did a current implementation value become a fixed normative requirement accidentally?
- did a cross-MR reference become ownership?
- did a gap disappear because of wording rather than evidence?
- can a Decision still be violated while all descendants pass?
- do canonical terms still denote the same semantic referent?

## 22. A12 - Completeness and promotion readiness

A documentation baseline can be promoted for BA use when:

- material semantic owners are established;
- required dependencies/cross-references are governed;
- blocking gaps are resolved or explicitly excluded from the declared scope;
- non-blocking NOT SPECIFIED meanings are preserved;
- specialization/security review is complete for thesis scope;
- A10 bindings are coherent;
- A11 semantic regression passes;
- governance explicitly authorizes the baseline as BA source.

Promotion is not “everything is fully specified”. Promotion means the baseline is **sufficiently governed for the declared scope**.

## 23. Handoff to Base Analysis

The handoff should include:

- authority/baseline identity;
- pinned source revision/source set;
- canonical governed subjects/referents;
- material behaviors, relations, conditions and states;
- specialized/security properties in scope;
- parameter semantics and current bindings where relevant;
- diagnostics, NOT SPECIFIED meanings and unresolved bindings;
- change/revalidation context when material.

The BA then applies its own minimum representation criterion. It must not retroactively dictate how the documentation should have been written.

## 24. STRIDE / STRIDE-AI and governed feedback

The intended thesis lifecycle is:

```text
GOVERNED DOCUMENTATION
        -> ACCEPTED BASE ANALYSIS
        -> STRIDE / STRIDE-AI
        -> FINDINGS
        -> candidate clarification / architecture change / accepted risk / SecurityRequirement
        -> GOVERNANCE REVIEW
        -> updated governed documentation if accepted
        -> rebuilt BA
```

A threat finding is analytical evidence, not project truth.

## 25. Extended worked example - DermaTriage adaptation branch

### 25.1 Source text

OR2 Architecture describes:

```text
Prompt evolution trigger: every 10 doctor corrections
Prompt evidence method: sliding window of 20 most recent examples
Classifier retraining trigger: 50 doctor corrections where agrees == False
Label mapping: P1/P2 -> HIGH, P3 -> MEDIUM, P4 -> LOW
Deploy condition: sensitivity/false-low non-degradation and bounded accuracy degradation
Rollback: current implementation reports automatic rollback beyond 5% accuracy degradation
```

### 25.2 Recover MR meaning

The stable responsibility is not “run PromptManager and EfficientNet”. It is:

```text
MR-04 - Controlled adaptation based on accumulated clinical review evidence
```

### 25.3 Recover Decisions

The source supports distinct commitments:

- DEC-04 accumulation-gated adaptation;
- DEC-05 separate adaptation paths by behavioral capability;
- DEC-06 comparative pre-adoption qualification;
- DEC-07 asymmetric quality prioritization;
- DEC-08 classification adaptation reversibility;
- DEC-09 bounded recent evidence for prompt evolution;
- DEC-10 clinical disagreement as qualifying classifier-adaptation evidence;
- DEC-11 corrected P-scale as classifier-supervision source.

### 25.4 Recover FRs without hardcoding implementation

```text
FR-04 prompt adaptation activation at semantic threshold N
FR-05 classifier adaptation activation at semantic threshold N
FR-06 bounded recent prompt-evidence window
FR-07 clinical disagreement qualification
FR-08 corrected P-scale -> classifier target mapping
FR-09 comparative qualification
FR-10 rollback capability for materially degrading adopted adaptation
FR-11 path lifecycle independence
```

### 25.5 Preserve bindings rather than freezing them

```text
PromptEvolutionThreshold=N           current N=10
ClassifierAdaptationThreshold=N      current N=50
PromptEvidenceWindowSize=N           current N=20
```

The current literals are traceability evidence, not automatically immutable normative constants.

### 25.6 Preserve data/state encoding separately

```text
ClinicianDisagreement
    governed semantic concept

agrees == False
    source-observed current encoding
```

Changing the field name does not change the requirement if the same semantic state remains represented.

### 25.7 Preserve non-security specialization without expanding thesis scope

DEC-07 points to quality properties that specialize FR-09. They are preserved for A7 review. They are not reclassified as SecurityRequirements and they do not force a new `QualityRequirement` subtype in the current thesis.

## 26. Practical authoring worksheet

For every candidate element record:

| Question | Result |
|---|---|
| source evidence | exact source/section or governed predecessor |
| candidate meaning | concise project-semantic statement |
| semantic owner | MR / Decision / FR / specialization |
| material alternatives | what materially different reading/change is excluded? |
| responsibility boundary | who actually owns the behavior/judgment/property? |
| implementation-neutrality test | does the meaning survive technology substitution? |
| split/coherent-unit test | can parts change or fail independently? |
| parameter/binding test | semantic parameter or current realization value? |
| gap status | AFFIRMED / DENIED / NOT SPECIFIED / CONFLICTING |
| disposition | PASS / REWORK / STOP / ROUTE |
| methodology feedback | guide, metamodel, BA, tooling or project-source pressure? |

## 27. Final authoring checklist

Before promoting a documentation baseline ask:

1. Is the source/authority boundary explicit?
2. Is every MR a stable responsibility rather than a technology bundle?
3. Does every Decision contain one material commitment?
4. Does every FR have exactly one honest parent Decision?
5. Can every FR be independently assessed without reconstructing hidden obligations from its parent?
6. Have mapping rows and normative clauses been kept in one Requirement when they form one coherent obligation?
7. Have independent obligations been split?
8. Have concrete numeric values passed semantic-owner and parameter-governance gates?
9. Are semantic concepts separated from current field/config/interface encodings?
10. Could all current descendants pass while a Decision is still violated?
11. Are cross-MR references distinguished from ownership and dependency?
12. Are non-security specialization candidates preserved without expanding the thesis scope unnecessarily?
13. Are SecurityRequirements properties rather than mechanisms?
14. Are unresolved meanings explicitly NOT SPECIFIED rather than silently invented?
15. Has project-wide propagation/regression been run?
16. Is the baseline explicitly authorized before Base Analysis begins?

## 28. Status of this R5 working candidate

This document incorporates holdout-supported refinements through DermaTriage A5 closure, especially:

- semantic-owner-first numeric classification;
- Parameter Governance Boundary;
- information/parameter/reference/transformation bridge taxonomy;
- Decision-to-Requirement counterexample test;
- scope-limited handling of non-security specializations;
- explicit documentation -> BA -> STRIDE -> governed feedback lifecycle.

It **does not** by itself promote these refinements into methodology authority. Promotion requires review against R4, A6-A12 evidence, the pre-A7 documentation/BA consistency check, and regression against the Facial Access corpus.
