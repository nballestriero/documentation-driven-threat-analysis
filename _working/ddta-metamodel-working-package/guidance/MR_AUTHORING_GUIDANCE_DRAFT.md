# Draft MR authoring guidance for LLMs and programmers

> Non-canonical notes. These are candidate guidance rules derived from the current MR metamodel study and the ThreatForge and facial-access examples.

## Goal

Write Macro Requirements that provide an executive map of a project without collapsing Decisions, Requirements, implementation details, temporary design state or analysis-method semantics into the top level.

## Core guidance

1. Write for stakeholders who understand the **project domain**, not necessarily software architecture or security analysis.
2. Domain terminology is allowed, including technical terminology when it is intrinsic to the project domain.
3. Do not introduce technical vocabulary merely because the metamodel, tool or threat-analysis method uses it.
4. Keep `Intent` short enough that all MR titles + Intent can be read as a project summary.
5. Identify stakeholder groups at the level relevant to the macro concern.
6. Express a macro result, not a checklist of atomic `must` statements.
7. Move choices of solution into Decisions.
8. Move independently testable obligations into Requirements.
9. Move component inventories, flows, trust boundaries and similar technical decomposition into lower-level documentation or later analysis representations when they become necessary.
10. Keep methodology-specific threat/privacy categories in later methodology-specific analysis artifacts.
11. Do not describe temporary design progress in the MR (`not yet decided`, `currently evaluating`, `will be selected later`). Record that state in working notes or Decision lifecycle/status instead.
12. Do not partition project MRs by analysis methodology. Describe project concerns first; later analyses may choose different methods for different scopes or subjects.

## Temporal-stability test

For every sentence in `Context`, `Scope`, `Assumptions` and `Constraints`, ask:

> If a lower-level architectural or design Decision were taken tomorrow, would this sentence become obsolete even though the macro project concern remained the same?

If **yes**, the sentence normally does not belong in the MR.

Examples to move out of MR:

- "The communication protocol has not yet been selected."
- "Inference is currently expected to run on a PC."
- "The team is evaluating whether the camera connects through LAN."

A domain statement such as "authorizations may be suspended or revoked" is different: it remains relevant after architecture Decisions because it describes the application domain rather than design progress.

## Boundary test before splitting or merging MRs

When creating or refactoring Macro Requirements, do not decide the boundary from MR prose alone. If an existing corpus already contains Decisions, inspect them as evidence of the responsibility historically assigned to the MR.

Ask, in order:

1. Does each candidate MR provide independently explainable project-level value?
2. Do its descendant Decisions form one coherent family of choices?
3. Does the distinction remain after removing names of current tools, components, schemas and analysis representations?
4. Is the relationship really a dependency (`dependsOn`) rather than containment or duplication?
5. Can domain stakeholders distinguish the two concerns from title + Intent?
6. If merged, would the MR combine substantially different kinds of Decisions?
7. If kept separate, are we preserving a project concern or merely copying the current architecture?

For an existing corpus, prefer this sequence:

`MR prose -> descendant Decisions -> solution-independent concern -> candidate rewrite -> boundary test`

Do **not** use this sequence:

`rewrite two MR summaries -> compare wording -> merge because they sound similar`

## Deferred analysis-applicability lesson

A project may contain concerns that are better examined by different analysis paradigms. For example, an ML recognition concern and a biometric/privacy concern can coexist in the same project without requiring the MR hierarchy to be organized by analysis methodology.

Guidance for now:

- do not write an "STRIDE-AI MR", "privacy-analysis MR" or similar methodology-owned project branch merely to make analysis convenient;
- keep the MR focused on the project concern in domain language;
- later, let an analysis select an explicit scope or governed subjects and the method appropriate to that analysis;
- expect results from different methods to return through one governed documentation/project lifecycle, preserving traceability and review.

The exact common analysis model is intentionally deferred.

## Candidate anti-patterns

### AP-MR-001 - MR as implementation checklist

**Symptom:** many atomic rules about commands, files, rollback, APIs, adapters, staging, rendering or similar mechanisms.

**Why problematic:** the MR stops explaining the project concern and starts specifying how one solution works.

### AP-MR-002 - Tool elevated to project objective

**Symptom:** a specific editor, framework, renderer, storage engine or protocol appears as the purpose of the MR even though it is only one possible implementation choice.

**Exception:** the technology may be named when it is itself part of the product/domain being developed.

### AP-MR-003 - Analysis representation treated as universal

**Symptom:** DFD, asset inventory, attack tree, STRIDE category or another method-specific structure is required directly by the MR model.

**Why problematic:** the documentation becomes biased toward a particular analysis paradigm.

### AP-MR-004 - Value or stakeholders are implicit

**Symptom:** the MR describes mechanism but a reader cannot tell who benefits or why the macro block exists.

### AP-MR-005 - Same obligation repeated at MR, Decision and Requirement

**Symptom:** nearly identical normative statements appear at several hierarchy levels.

**Why problematic:** semantic ownership becomes ambiguous and documentation becomes verbose.

### AP-MR-006 - Internal project-tool vocabulary in executive text

**Symptom:** title/Intent require prior knowledge of internal implementation terms that are not domain concepts.

### AP-MR-007 - Technical-word prohibition

**Symptom:** an author removes useful domain terminology merely because it sounds technical.

**Why problematic:** readability should be judged against the project stakeholders, not against a generic non-technical audience with no domain knowledge.

### AP-MR-008 - Architecture leaked into the MR

**Symptom:** changing a component, protocol or deployment topology forces the MR to change even though the project-level concern and value remain the same.

**Heuristic:** if two plausible architectures satisfy the same MR without changing its Intent, the MR is likely at the right abstraction level.

### AP-MR-009 - Merge by paraphrase

**Symptom:** two rewritten MRs sound similar, so they are merged without inspecting the Decisions or project responsibilities below them.

**Why problematic:** both rewrites may have been framed through the same consumer or benefit even though they govern different concerns.

**Correction:** inspect descendant Decision families and restate each concern without current solution vocabulary before deciding.

### AP-MR-010 - Historical split treated as proof

**Symptom:** two MRs are kept separate only because the current implementation, repository layout or architecture already separates them.

**Why problematic:** architectural layers are not automatically project-level concerns.

**Correction:** require independent project value and a solution-independent distinction; otherwise consider merging or moving the separation down to Decisions.

### AP-MR-011 - Temporary design status in MR

**Symptom:** MR prose says that a protocol, component, architecture, deployment choice or other solution detail is "not yet decided", "under evaluation" or "to be chosen".

**Why problematic:** the MR becomes stale as soon as the Decision is taken and requires review even though the macro concern did not change.

**Correction:** omit the temporary state from the MR and govern the unresolved choice in working material or the Decision lifecycle.

### AP-MR-012 - Project partitioned by methodology

**Symptom:** MRs are created or renamed around STRIDE, STRIDE-AI, privacy analysis or another method rather than around project concerns.

**Why problematic:** methodology becomes part of the project topology and makes it harder to apply different methods to overlapping or complementary concerns.

**Correction:** keep project concerns method-agnostic; select methodology later for an explicit analysis scope and return results through common governance.
