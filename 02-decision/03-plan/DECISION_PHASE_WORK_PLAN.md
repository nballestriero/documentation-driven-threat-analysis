# DDTA Decision phase - work plan

**Non-canonical research plan - checkpoint before facial-access Decisions**

## Checkpoint purpose

This file freezes the intended experimental sequence before authoring any Decision for the independent facial-access / controlled-access demo.

Expected local repository baseline for applying this checkpoint: commit `2db7604` (`research: add MR teachability and pre-close projection study`). The full 40-character SHA was not captured in the prior transcript, so application commands verify the short HEAD before extraction.

The current Decision construction candidate was built from the ThreatForge MR-0001 + MR-0002 historical ADR corpus only. The independent facial-access Decisions have not yet been written, and ThreatForge MR-0003, MR-0004 and MR-0005 remain untouched sequential holdouts.

## Current frozen construction-candidate baseline

The Decision-specific core is closed for the construction candidate:

```text
Decision
|- title
|- context
|- decision
`- consequences
```

All four fields are semantically required and non-null. Parentage to one Macro Requirement is an explicit semantic relation. Lifecycle/status and serialization storage remain separate concerns.

The following construction conclusions are also frozen unless a concrete independent counterexample reopens them:

1. Context is decision-local rather than a repetition of the parent MR.
2. One Decision expresses one coherent chosen position.
3. Consequences expose material effects/trade-offs of the choice.
4. Non-goals is not a Decision-core patch field; misleading Context + Decision must be rewritten.
5. Separate mandatory `rationale` and embedded `alternatives` are not currently justified.
6. DDTA/metamodel, governed project, ThreatForge tool and ThreatForge project operations have distinct semantic ownership.
7. A ThreatForge ADR may decide how the tool supports general semantics, but must not silently define those general semantics.
8. Cross-document persistence problems are not solved with topic-specific Decision fields.

Cross-cutting representation decisions are also frozen for this construction candidate:

- complete canonical field shape;
- explicit field-specific nullability / canonical empty values;
- semantic/representation separation;
- executable projections derived from one governed canonical document model.

## Experimental discipline

The next phases must preserve evidence independence.

- Do not use ThreatForge MR-0003/MR-0004/MR-0005 while authoring the facial-access Decisions.
- Do not refactor or rewrite ThreatForge implementation or canonical project documents during this conceptual study.
- Do not define Requirement semantics merely to make the Decision model easier to validate.
- Do not introduce lifecycle/status mechanics during the Decision semantic test.
- Do not add fields to Decision merely because one case needs persistent applicability, vocabulary, patterns, traceability or another cross-cutting concern.
- Technical/domain vocabulary is allowed when intrinsic to the actual choice; premature metamodel vocabulary must not become project semantics.
- Every change to the construction candidate after this checkpoint requires a concrete counterexample and an explicit regression over all previously used cases.

## Phase D1 - author independent facial-access Decisions

Use the four already-studied Macro Requirements of the independent facial-access / controlled-access example:

1. MR-0001 - Accesso controllato all'area riservata
2. MR-0002 - Gestione delle persone autorizzate
3. MR-0003 - Riconoscimento facciale per la verifica della persona
4. MR-0004 - Uso responsabile dei dati biometrici e delle decisioni automatiche

Author a deliberately small but varied Decision corpus, approximately 6-8 Decisions across the four MRs.

Authoring constraints:

- use only `Title`, `Context`, `Decision`, `Consequences` for Decision-specific semantics;
- write each field explicitly; no optional-by-omission representation;
- avoid Requirement-level independently checkable detail unless that precision is intrinsic to the choice itself;
- avoid premature architecture (camera topology, protocols, databases, thresholds, APIs, deployment) unless the Decision genuinely chooses it;
- include at least one non-software / policy-or-method Decision so the model is not validated only on architecture choices;
- keep the corpus independent from the historical ThreatForge wording.

Deliverable: a readable demo document containing the candidate facial-access Decisions, without changing the Decision metamodel during initial authoring.

## Phase D2 - analyze the facial-access Decisions against the frozen candidate

Analyze each new Decision using the same tests:

1. parent/MR narrowing;
2. decision-local Context;
3. explicit coherent choice;
4. consequence awareness;
5. semantic-owner correctness;
6. Decision-vs-downstream boundary;
7. no semantic patching;
8. model/tool independence;
9. survivability challenge without ad-hoc fields;
10. compatibility with complete-shape / derived executable representation.

For every Decision produce one of two outcomes:

```text
fits construction candidate

or

counterexample -> candidate correction required
```

A counterexample must state exactly which closed rule fails and why the information cannot be represented without loss or distortion.

## Phase D3 - regression and Decision candidate closure

If D2 exposes a counterexample:

1. revise only the minimum affected rule;
2. record the evidence that caused the revision;
3. rerun the affected facial-access cases;
4. rerun all 16 ThreatForge construction ADRs against the corrected model.

If no unresolved counterexample remains, mark the Decision model as **candidate closed after independent example validation**.

This does not yet establish universal validity; it authorizes the sequential holdout phase.

## Phase D4 - ThreatForge MR-0003 holdout

Read and analyze MR-0003 Decisions for the first time as holdout evidence.

- Do not rewrite the model pre-emptively.
- Classify every mismatch as historical ADR defect, ownership/conflation defect, downstream leakage, or genuine metamodel counterexample.
- Modify the model only for the last category.
- If modified, regress ThreatForge MR-0001/MR-0002 plus the facial-access corpus before continuing.

## Phase D5 - ThreatForge MR-0004 holdout

Repeat the same procedure using MR-0004 only after MR-0003 is resolved. Any model modification requires regression on all earlier evidence.

## Phase D6 - ThreatForge MR-0005 holdout

Repeat the same procedure using MR-0005 only after MR-0004 is resolved. This is the final Decision holdout in the planned sequence.

## Phase D7 - Decision-phase synthesis

After all three holdouts:

- state the final Decision semantic model and invariants supported by the evidence;
- separate stable general rules from ThreatForge case-study lessons;
- record remaining cross-document constraints that cannot be solved at Decision level;
- preserve the complete-shape / semantic-representation / executable-projection decisions for reuse by later document models;
- update authoring guidance and anti-patterns only after the final synthesis.

## Phase R1 - move to Requirement semantics

Only after Decision-phase synthesis, begin the next-level Requirement study.

Priority questions already carried forward:

- what makes an obligation independently checkable without reducing every Requirement to one implementation file;
- how pervasive/cross-cutting obligations are represented and covered;
- how persistent Decisions retain downstream effect without inheritance-by-copy;
- how single-source governed knowledge and effective governed context are represented;
- how humans, tools and LLMs recover applicable context without relying on memory;
- how Requirement semantics map into complete canonical representations and executable projections.

## Deferred beyond the current plan

- lifecycle/status transitions and historical governance;
- concrete YAML/Markdown serialization;
- ThreatForge refactoring/migration;
- production plugin/runtime changes;
- methodology-neutrality verdict;
- STRIDE/LINDDUN comparison or implementation.

## Commit discipline

This checkpoint should be committed **before** authoring the facial-access Decision corpus. Later empirical phases should use separate commits/checkpoints so that the evidence sequence remains reconstructable:

```text
checkpoint: Decision construction candidate + plan
    -> facial-access Decision authoring
    -> facial-access analysis / possible regression
    -> MR-0003 holdout
    -> MR-0004 holdout
    -> MR-0005 holdout
    -> Decision synthesis
```

The purpose is methodological traceability: later revisions should make it possible to identify which evidence changed which part of the model.
