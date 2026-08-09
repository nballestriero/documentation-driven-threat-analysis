# Draft MR authoring guidance for LLMs and programmers

> Non-canonical notes. These are candidate guidance rules derived from the current MR metamodel study and the ThreatForge case study.

## Goal

Write Macro Requirements that provide an executive map of a project without collapsing Decisions, Requirements, implementation details or analysis-method semantics into the top level.

## Core guidance

1. Write for stakeholders who understand the **project domain**, not necessarily software architecture or security analysis.
2. Domain terminology is allowed, including technical terminology when it is intrinsic to the project domain.
3. Do not introduce technical vocabulary merely because the metamodel, tool or threat-analysis method uses it.
4. Keep `Intent` short enough that all MR titles + Intent can be read as a project summary.
5. Identify stakeholder groups at the level relevant to the macro concern.
6. Express a macro result, not a checklist of atomic `must` statements.
7. Move choices of solution into Decisions.
8. Move independently testable obligations into Requirements.
9. Move component inventories, flows, trust boundaries and similar technical decomposition into lower-level documentation/Base Analysis when they become necessary.
10. Keep methodology-specific threat/privacy categories in methodology-specific analysis records.

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
