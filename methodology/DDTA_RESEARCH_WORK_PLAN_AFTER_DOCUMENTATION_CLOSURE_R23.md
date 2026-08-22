---
title: "DDTA research work plan after documentation-layer closure - R23"
---

# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 23**

**Status:** ACTIVE R24 WORK PLAN — SEMANTIC SUFFICIENCY / BA REGRESSION PRESSURE TESTING.

**Initially prepared against repository baseline:** `df404acb2cfcfb4880badefe34c4df7948f28b42`

**Current refinement baseline:** `87a612663d1e4827b7f67e83182838586e53d7ba`

**Supersedes:** Revision 22 only for forward execution state. R1-R22 remain historical research records.

**Current R24 checkpoint:** `DDTA_R24_SEMANTIC_REVIEW_CHECKPOINT_R1.md`

**Carried-forward BA2 lower-bound checkpoint:** `DDTA_R24_DECISION_RULE_CHECKPOINT.md`

## 1. Trigger for this revision

Repository alignment is complete. The Facial Access vertical slice was about to resume at `MR-0003` when a material semantic-classification problem emerged during human review.

Human review found that the current R24 `MR-0003` wording can support materially different readings depending on what is already known when the responsibility starts. In particular, the available evidence does not explicitly establish whether a specific `GovernedIdentity` is already selected/available as a reference before correspondence is determined.

The current R24 working documentation uses the name `IdentityVerification`, but that label must not be used as evidence to decide the unresolved entry-state fact or to force an identification/verification classification.

This is not treated as a wording-only defect. It exposes a more general methodology question:

> Can recurring problem, domain, security and requirement patterns help DDTA authors and reviewers recognize standard semantic situations and discriminate confusable cases before project documentation or Base Analysis freezes the wrong meaning?

R23 therefore inserts a bounded literature/research step before further modification of `MR-0003`.

No current project document, BA operator, BA proposition or authority classification is changed by this work plan.

## 2. Fixed prior state

The following state is retained:

- repository alignment: **COMPLETE**;
- current governed facial-access baseline: `FACIAL_ACCESS_CURRENT_R1`;
- R24 facial-access project documentation: **EXPERIMENTAL_NON_CANONICAL / working successor candidate**;
- BA1 identity semantics: retained;
- BA2 R2: active R24 working lower bound;
- BA3 / BA4 / BA5: retained for their closed scopes;
- authorization-side normalized comparison: open project-semantics pressure point;
- verification-selection `decisionRule`: not justified by the currently governed outcome-domain meaning alone;
- no pattern catalog is currently part of DDTA authority or the DDTA conceptual metamodel.

## 3. R23 objective

Determine, from literature and controlled comparison, whether DDTA should adopt a lightweight semantic-sufficiency / semantic-discrimination review integrated into existing authoring, with reusable problem/domain knowledge as optional candidate-generation support and Base Analysis derivation as a second semantic pressure test.

The research must distinguish at least four levels instead of collapsing them:

```text
problem / problem-frame pattern
    -> what recurring class of problem is present?

domain / analysis / semantic pattern
    -> what recurring semantic structure or task is present?

requirement / authoring pattern
    -> how can the governed obligation be expressed clearly?

design / integration / implementation pattern
    -> what reusable solution structure may realize it?
```

The working hypothesis is that DDTA may benefit primarily from the first three levels while design patterns remain downstream comparison material.

The hypothesis is **not accepted in advance**.

Current working result after the R23 reading and pressure-test pass:

- a mandatory DDTA pattern card is **not** justified as the next artifact;
- pattern/domain knowledge is more defensible as optional review knowledge that proposes candidate interpretations and critical differences;
- the smallest promising DDTA change is a semantic-sufficiency review with escalation only when a material ambiguity is plausible;
- Base Analysis derivation should also be used as a post-authoring semantic regression/back-check without becoming project authority;
- no new metamodel field, document type or BA operator is justified by the current evidence.

## 4. Research questions

### PAT-RQ1 — Problem recognition

Which existing approaches classify recurring system/application problems before architecture or implementation is selected?

### PAT-RQ2 — Semantic discrimination

Which approaches provide discriminators, recognition heuristics, applicability criteria, negative cases or critical differences that can distinguish superficially similar problem classes?

The immediate Facial Access example is:

```text
identification / one-to-many
    vs
verification / one-to-one
    vs
authentication
    vs
authorization
    vs
access decision
```

The literature study must not assume this provisional classification is already correct for DDTA.

### PAT-RQ3 — Pattern anatomy

Which fields make a reusable pattern useful for human recognition without turning it into a prescriptive architecture?

Candidate fields may include problem, context, roles, discriminators, typical outcomes, confusable cases, critical differences, consequences, non-implications and review questions, but R23 does not freeze this list.

### PAT-RQ4 — Authority boundary

How can a pattern guide questions and review while preserving:

```text
pattern match
    != governed requirement
    != project authority
    != automatic Base Analysis derivation
```

### PAT-RQ5 — Requirements authoring

Which requirements-pattern approaches can help turn recognized project meaning into readable, testable project documentation without importing solution structure?

### PAT-RQ6 — Thesis evidence

Which pattern concepts are sufficiently supported and citable to justify a thesis contribution, comparison or design choice?

## 5. Existing literature workflow remains authoritative for reading records

R23 does **not** define a new reading-card format.

Every selected source must follow the existing repository workflow:

1. register the source in `literature/literature.registry.yml`;
2. record legal-access metadata in `literature/source-access.registry.yml`;
3. create the source note from `literature/templates/source-note.template.md`;
4. answer the existing four reading questions;
5. assess temporal validity;
6. record citation-ready locations under `literature/excerpts/`;
7. keep quotation (`C`), faithful paraphrase (`P`) and researcher interpretation (`I`) separate;
8. place cross-source conclusions only under `literature/syntheses/`.

Source PDFs remain local under `literature/local-pdf/` and are not committed merely for convenience.

## 6. Candidate reading corpus — plan-local identifiers

`PAT-LIT-*` identifiers are local to this work plan. They are **not** literature-registry `SRC-*` identifiers.

A source receives its repository `SRC-*` identity only when it is actually registered and its bibliographic/access metadata is checked.

### Core theory

| Plan ID | Source | Planned depth | Why it is in scope |
|---|---|---|---|
| `PAT-LIT-01` | Michael Jackson, “Problems and requirements (software development)”, Second IEEE International Symposium on Requirements Engineering, 1995, pp. 2–9 | DEEP | problem vs requirement vs solution boundary |
| `PAT-LIT-02` | Michael Jackson, *Problem Frames: Analysing and Structuring Software Development Problems*, Addison-Wesley, 2001, ISBN 978-0-201-59627-4 | TARGETED / selected chapters | recurring problem classes, context and problem decomposition |
| `PAT-LIT-03` | Alistair G. Sutcliffe, Neil A. M. Maiden, “The Domain Theory for Requirements Engineering”, *IEEE Transactions on Software Engineering* 24(3), 1998, pp. 174–196, DOI `10.1109/32.667878` | DEEP / FIRST | generic application models, matching and critical difference rules |
| `PAT-LIT-04` | Alistair G. Sutcliffe, “Domain analysis for software reuse”, *Journal of Systems and Software* 50(3), 2000, pp. 175–199, DOI `10.1016/S0164-1212(99)00096-5` | DEEP | grounded domains, meta-domains, generic tasks and recognition heuristics |
| `PAT-LIT-05` | Martin Fowler, *Analysis Patterns: Reusable Object Models*, Addison-Wesley, 1997, ISBN 978-0-201-89542-1 | TARGETED | conceptual/domain pattern structure distinct from GoF implementation design |

### Security / semantic patterns

| Plan ID | Source | Planned depth | Why it is in scope |
|---|---|---|---|
| `PAT-LIT-06` | Eduardo B. Fernandez, Nobukazu Yoshioka, Hironori Washizaki, Joseph Yoder, “Abstract security patterns and the design of secure systems”, *Cybersecurity* 5:7, 2022, DOI `10.1186/s42400-022-00109-w` | DEEP / SECOND | abstract security mechanisms based on application semantics rather than software architecture |
| `PAT-LIT-07` | Eduardo Fernandez-Buglioni, *Security Patterns in Practice: Designing Secure Architectures Using Software Patterns*, Wiley, 2013, ISBN 978-1-119-99894-5 | DEEP / selected chapters | pattern anatomy plus identity-management, authentication and authorization/access-control distinctions |

### Requirements / authoring patterns

| Plan ID | Source | Planned depth | Why it is in scope |
|---|---|---|---|
| `PAT-LIT-08` | Stephen Withall, *Software Requirement Patterns*, Microsoft Press, 2007, ISBN 978-0-7356-2398-9 | TARGETED | requirement-pattern anatomy, authoring questions, pitfalls and related requirements |
| `PAT-LIT-09` | Neil A. M. Maiden, Sara Manning, Sara Jones, John Greenwood, “Generating requirements from systems models using patterns: a case study”, *Requirements Engineering* 10, 2005, pp. 276–288, DOI `10.1007/s00766-005-0010-9` | TARGETED | bridge from model/pattern recognition to textual requirements in an industrial case |
| `PAT-LIT-10` | Alistair Mavin, Philip Wilkinson, Adrian Harwood, Mark Novak, “Easy Approach to Requirements Syntax (EARS)”, RE 2009, pp. 317–322, DOI `10.1109/RE.2009.9` | COMPARATIVE | lightweight requirement-writing patterns; useful to separate semantic recognition from sentence syntax |

### Validation / classification limits

| Plan ID | Source | Planned depth | Why it is in scope |
|---|---|---|---|
| `PAT-LIT-11` | Karl Cox, Keith Phalp, Steven J. Bleistein, June M. Verner, “Deriving requirements from process models via the problem frames approach”, *Information and Software Technology* 47(5), 2005, pp. 319–337, DOI `10.1016/j.infsof.2004.09.002` | COMPARATIVE | industrial pressure test showing real problems do not always fit a small fixed frame catalog |
| `PAT-LIT-12` | Alistair G. Sutcliffe, “Requirements Engineering Domain Dimensions”, Dagstuhl Seminar Proceedings 08412, 2009, DOI `10.4230/DagSemProc.08412.12` | COMPARATIVE / SHORT | discriminating dimensions for application/domain genres |

### Design-pattern comparison only

| Plan ID | Source | Planned depth | Why it is in scope |
|---|---|---|---|
| `PAT-LIT-13` | Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*, Addison-Wesley, 1994 | COMPARATIVE / introductory sections only | mature pattern anatomy, applicability and consequences; downstream solution level |
| `PAT-LIT-14` | Gregor Hohpe, Bobby Woolf, *Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions*, Addison-Wesley, 2003, ISBN 978-0-321-20068-6 | COMPARATIVE / introductory sections only | pattern language, recurring integration problems and technology-independent solution vocabulary |

## 7. Reading order

The default reading order is evidence-driven rather than chronological.

### Wave 1 — recognition and semantic discrimination

```text
PAT-LIT-03  Domain Theory for Requirements Engineering
PAT-LIT-06  Abstract Security Patterns
PAT-LIT-01  Problems and Requirements
PAT-LIT-04  Domain Analysis for Software Reuse
PAT-LIT-07  Security Patterns in Practice
```

These receive the deepest first reading because they most directly pressure the proposed DDTA use of patterns.

### Wave 2 — pattern structure and requirements authoring

```text
PAT-LIT-02  Problem Frames
PAT-LIT-05  Analysis Patterns
PAT-LIT-08  Software Requirement Patterns
PAT-LIT-09  Generating requirements from systems models using patterns
```

### Wave 3 — limits and downstream comparison

```text
PAT-LIT-10  EARS
PAT-LIT-11  industrial Problem Frames pressure test
PAT-LIT-12  RE Domain Dimensions
PAT-LIT-13  GoF introductory pattern anatomy
PAT-LIT-14  Enterprise Integration Patterns introductory material
```

The order may change only when a reading card identifies a concrete prerequisite or a more authoritative source.

## 8. Reading outputs

For each source actually read:

```text
registered SRC identity
+ source-access record
+ standard source note
+ exact citation-ready excerpts/locations
+ temporal-validity assessment
+ explicit DDTA relevance / tension / gap
```

The reading note must answer the existing four repository reading questions; R23 adds no replacement questionnaire.

### 8.1 Current R23 corpus state

At refinement baseline `87a612663d1e4827b7f67e83182838586e53d7ba`, the R23 pattern/semantic corpus is registered as `SRC-0049` through `SRC-0066`.

The corpus contains full, partial, preview and access-limited sources. Cross-source claims must therefore remain bounded by the source notes actually read and by their recorded access limitations.

The working synthesis for the current transition is:

- `literature/syntheses/R23_SEMANTIC_RECOGNITION_SYNTHESIS_R1.md`

This working synthesis satisfies the gate needed to resume controlled method pressure testing. It does not claim exhaustive literature closure or general empirical validation.

## 9. Cross-source synthesis gate — working gate satisfied

Do not design DDTA review structure directly from one source.

The current working cross-source synthesis is:

- `literature/syntheses/R23_SEMANTIC_RECOGNITION_SYNTHESIS_R1.md`

It compares problem/solution level, recognition mechanisms, critical differences, authoring relation, design relation, human judgment, authority assumptions, limitations and DDTA implications.

The synthesis is sufficient to resume controlled authoring/BA pressure testing, but it is not a claim of exhaustive literature closure.

## 10. Semantic-review mechanism gate

The next mandatory artifact is **not** a pattern-card/template.

The current candidate mechanism is:

```text
normal DDTA authoring
    -> semantic sufficiency check
    -> if materially unstable: inspect relevant semantic dimensions
    -> minimal competing readings
    -> critical difference
    -> governed-evidence question
    -> clarify / place / unresolved
```

Reusable problem/domain/pattern knowledge may help generate candidate readings or critical-difference hints. It remains optional review knowledge and cannot substitute for governed project evidence.

Current evidence does not justify:

- six mandatory semantic fields on every document;
- a new semantic-review document type;
- a universal pattern taxonomy;
- automatic pattern matching;
- automatic requirement or BA generation.

## 11. Pressure-test status and next empirical cycle

The preliminary Facial Access pressure test is complete at the semantic-review level.

It found a material critical difference without closing the domain classification:

> Before correspondence determination begins, is a specific `GovernedIdentity` already available/selected as the reference?

The current working evidence does not explicitly close that fact.

Cross-LLM blind replication independently recovered the same discriminator family. One grounded replication carries a documented contamination caveat because an allowed DDTA guide exposed Facial Access labels after the blind result had been frozen.

A controlled synthetic record-coherence case exercised a different discriminator family. A retrospective ThreatForge implementation-promotion case exercised another: what proposition verification evidence actually justifies.

These tests are recorded in:

- `studies/semantic-review/R24_SEMANTIC_REVIEW_PRESSURE_TESTS_R1.md`

The next empirical cycle must now return to real Facial Access documentation, then derive the minimum justified BA and run a post-BA semantic regression back-check.

Do not classify the responsibility from the `IdentityVerification` label and do not rename it before governed evidence closes or preserves the ambiguity.

## 12. Guardrails

During R23:

- do not modify `MR-0003` merely to fit a literature pattern;
- do not rename `IdentityVerification` before the pattern/semantic analysis is complete;
- do not add pattern types to the DDTA L1 conceptual metamodel;
- do not add a BA2 operator because a pattern catalog uses a familiar verb;
- do not derive BA propositions automatically from a pattern match;
- do not treat design patterns as project authority;
- do not turn the six semantic observation dimensions into mandatory document fields without additional evidence;
- do not let BA resolve a semantic ambiguity that project documentation leaves open;
- do not let a post-BA discrepancy automatically mutate governed documentation; it produces a correction candidate for governed review;
- do not copy copyrighted source PDFs into Git;
- do not make a thesis claim from an unverified candidate source;
- do not treat the 14-source corpus as exhaustive if reading reveals a material missing source.

## 13. Transition condition

R23's literature/semantic-recognition step may transition into applied authoring/BA pressure testing when:

1. the selected source corpus is registered with its access limitations;
2. the source notes used for current claims are available;
3. a cross-source working synthesis exists;
4. problem/domain/requirement/design pattern levels remain explicit;
5. the synthesis distinguishes literature-backed recognition principles from the DDTA-specific integration;
6. the Facial Access test identifies a material critical difference without forcing a domain label;
7. at least one independent or non-Facial-Access pressure test is recorded with limitations;
8. no mandatory pattern template, new metamodel field or automatic BA derivation is assumed;
9. the next cycle explicitly tests documentation → minimum BA → semantic regression.

`DDTA_R24_SEMANTIC_REVIEW_CHECKPOINT_R1.md` records that working transition. This is a transition to applied pressure testing, not final method closure.

## 14. Forward sequence

The active sequence is:

```text
R23 registered corpus + source notes
    -> R23 semantic-recognition synthesis
    -> R24 semantic-review checkpoint
    -> return to MR-0003 neutral semantic review
    -> determine whether the critical entry-state fact is governed / conflicting / unresolved
    -> clarify MR only if the fact defines the stable responsibility
    -> create/use a Decision only for a genuine project choice
    -> FR operationalization
    -> minimum justified BA derivation
    -> semantic regression back-check
    -> if needed: governed documentation correction candidate -> rebuild BA
    -> downstream analysis / test usefulness check
    -> repeat on another real governed responsibility
    -> only then promote stable guide/method/thesis wording
```

## 15. Exact next microstep

The exact next microstep after this checkpoint is applied is:

> Return to `MR-0003` in the R24 working Facial Access project documentation. Ignore the `IdentityVerification` label while reconstructing the responsibility, then inspect available project evidence for the critical entry-state fact: whether a specific `GovernedIdentity` is already available/selected before correspondence determination begins.

Classify that evidence as affirmed, denied, conflicting or not specified.

Do not rename the capability and do not create a Decision merely to resolve missing evidence during that microstep.
