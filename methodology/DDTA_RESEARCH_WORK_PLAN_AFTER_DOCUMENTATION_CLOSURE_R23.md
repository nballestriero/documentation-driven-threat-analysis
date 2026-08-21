---
title: "DDTA research work plan after documentation-layer closure - R23"
---

# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 23**

**Status:** ACTIVE R24 WORK PLAN — LITERATURE-BACKED SYSTEM / SEMANTIC PATTERN RESEARCH.

**Prepared against repository baseline:** `df404acb2cfcfb4880badefe34c4df7948f28b42`

**Supersedes:** Revision 22 only for forward execution state. R1-R22 remain historical research records.

**Current R24 checkpoint:** `DDTA_R24_DECISION_RULE_CHECKPOINT.md`

## 1. Trigger for this revision

Repository alignment is complete. The Facial Access vertical slice was about to resume at `MR-0003` when a material semantic-classification problem emerged during human review.

The project use case begins with a person presenting at the access point while their governed identity is not yet known. The system must first determine which registered/governed identity, if any, corresponds to that person and only afterwards determine the relevant authorization state and access decision.

The current R24 working documentation uses the name `IdentityVerification`, while the reviewed behavior may instead involve an identification / one-to-many recognition problem before any one-to-one verification or authorization step.

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

Determine, from literature and controlled comparison, whether DDTA should adopt a lightweight pattern-based authoring/review aid for recurring system problem semantics.

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

## 9. Cross-source synthesis gate

Do not design the DDTA pattern template directly from one source.

After the reading pass, create a synthesis under `literature/syntheses/` that compares at least:

1. what each source calls a pattern/frame/model;
2. problem vs solution level;
3. recognition/applicability mechanism;
4. discriminators / critical differences / negative cases;
5. required semantic roles or structure;
6. consequences and trade-offs;
7. relationship to requirements authoring;
8. relationship to architecture/design;
9. human vs automated matching;
10. authority assumptions;
11. known limitations and evidence base;
12. implications for DDTA and thesis claims.

## 10. Pattern-template design gate

Only after the synthesis may DDTA propose a pattern-card/template.

The template must remain a **working authoring/review aid**, not project authority.

At minimum it must be tested against these failure modes:

- pattern name suggests the wrong semantic problem;
- two patterns are superficially similar but differ on a critical precondition;
- pattern application silently introduces architecture;
- pattern match automatically emits requirements or BA propositions;
- pattern vocabulary becomes a hidden canonical ontology without governance;
- pattern catalog is treated as exhaustive when the project does not fit;
- downstream design pattern is mistaken for a project problem pattern.

The exact fields and syntax remain open until the literature synthesis is complete.

## 11. Pilot pressure test

The first template candidate must be pressure-tested on the Facial Access semantic confusion that triggered R23.

The pilot must discriminate, without assuming the conclusion in advance:

```text
identification / one-to-many recognition
verification / one-to-one comparison
authentication
authorization
access decision / policy gate
```

The pilot must answer:

- what information is known before each responsibility starts?
- what population or specific identity is in scope?
- what question is the responsibility answering?
- what semantic outputs must later responsibilities consume?
- what failure/ambiguity outcomes are materially distinct?
- which terms in the current R24 project documentation are misleading or overloaded?

Only after this pressure test may `MR-0003` wording and capability/referent naming resume.

## 12. Guardrails

During R23:

- do not modify `MR-0003` merely to fit a literature pattern;
- do not rename `IdentityVerification` before the pattern/semantic analysis is complete;
- do not add pattern types to the DDTA L1 conceptual metamodel;
- do not add a BA2 operator because a pattern catalog uses a familiar verb;
- do not derive BA propositions automatically from a pattern match;
- do not treat design patterns as project authority;
- do not copy copyrighted source PDFs into Git;
- do not make a thesis claim from an unverified candidate source;
- do not treat the 14-source corpus as exhaustive if reading reveals a material missing source.

## 13. Exit condition

R23's pattern-literature step may close only when:

1. the selected core sources have repository source notes and citation-ready locations;
2. bibliographic identity and legal access are registered for every source actually used;
3. the cross-source synthesis is complete;
4. the difference between problem/domain/requirement/design pattern levels is explicit;
5. the synthesis identifies supported candidate fields and unsupported assumptions for a DDTA pattern template;
6. a first pattern template is drafted only from the synthesis;
7. the template passes the Facial Access identification/verification pressure test without becoming project authority;
8. any required additional literature has either been read or explicitly deferred with rationale.

## 14. Forward sequence

The active sequence is:

```text
R23 source registration / access verification
    -> reading cards using the existing source-note template
    -> citation-ready excerpts
    -> cross-source pattern synthesis
    -> DDTA pattern-template candidate
    -> Facial Access identification/verification pressure test
    -> return to MR-0003 wording
    -> MR-0003ADR-0001
    -> MR-0003ADR-0001FR-0001
    -> minimum justified BA derivation
    -> downstream analysis / test usefulness check
```

## 15. Exact next microstep

The exact next microstep after R23 is committed is:

> Register and obtain/verify legal access for `PAT-LIT-03 — The Domain Theory for Requirements Engineering`, assign its repository `SRC-*` identity, and create its reading note from `literature/templates/source-note.template.md`.

Do not start the DDTA pattern template during that microstep.
