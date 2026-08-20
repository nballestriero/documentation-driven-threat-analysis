# DDTA Research Work Plan R24 - Documentation / Base Analysis Co-authoring

**Status:** WORKING PLAN / R24 ACTIVE  
**Original experiment input baseline:** `9cc17a148726bd0734db51e26ac74e031020f340`  
**Current continuation parent baseline:** `26579f26b471d87f0d6267e315e77bb285aabc00`  
**Active phase:** Decision authoring / review (D2), with local downstream FR projection used as a diagnostic aid.  
**Preserved closures:** BA1, BA2, BA3 and BA5 remain closed unless a concrete R24 counterexample triggers the smallest applicable reopen criterion.

## 1. Purpose

R24 tests a correction to the way DDTA Base Analysis is applied while project documentation is being rewritten.

The central separation remains:

- governed project documentation establishes project meaning;
- BA reconstructs reusable meaning, propositions, provenance and unresolved semantics;
- BA-derived views test clarity/completeness but do not become project truth by themselves;
- research notes explain why authoring choices are useful and how the method should evolve;
- research commentary must not leak into the project documentation merely because it motivated an authoring decision.

The experiment aims to improve semantic precision without turning documentation into a research diary or creating a second semantic authority.

## 2. Main research questions

R24 continues to test:

1. whether breadth-first stabilization by semantic level gives a clearer project story than branch-local depth-first extraction;
2. whether closed BA1/BA2/BA3/BA5 contracts preserve the required project meaning without invented links;
3. which failures are documentation gaps, structure/granularity problems, BA limitations or projection limitations;
4. whether BA feedback can improve documentation while governed documentation remains authoritative;
5. whether the authoring process converges efficiently toward FR, tests, code and later security/threat analysis rather than accumulating semantic commentary;
6. whether canonical naming and provenance improve consistency without creating a second ontology;
7. whether project commitments that are obvious inside one professional domain must sometimes be made explicit to preserve meaning across other domains, implementers and automated analysis.

## 3. Source authority

Primary current authority remains the governed/current corpus and the explicitly accepted R24 working documentation. Historical material is regression evidence only unless rewritten and accepted as a current candidate.

Rules:

- historical Decisions/MRs may seed comparison and migration;
- historical wording is never copied as current truth merely because it exists;
- every migrated meaning must be checked against the current problem framing and current MR ownership;
- project documentation and research/methodology commentary must remain separate artifacts.

## 4. R24 execution model

Formal acceptance remains breadth-first by semantic level:

```text
LEVEL 0  authority + project problem framing
LEVEL 1  all MacroRequirements
LEVEL 2  all Decisions
LEVEL 3  all FunctionalRequirements
LEVEL 4  all Specialized/SecurityRequirements
LEVEL 5  integrated readability / method-overlay readiness
```

The formal gates remain:

```text
D0 -> Project framing
D1 -> complete MR set
D2 -> complete Decision set
D3 -> complete FR set
D4 -> Specialized/Security requirements
```

### 4.1 Authoring locality vs gate order - R24-WORKING

R24 now distinguishes **local authoring flow** from **formal level acceptance**.

While reviewing one candidate Decision it is useful to finish the local reasoning far enough to project the main downstream FR behavior:

```text
candidate Decision
  -> Decision BA delta
  -> immediate downstream FR projection
  -> significance / granularity / responsibility check
  -> next Decision
```

The projected FR is a working diagnostic/projection during D2. It does **not** by itself close or bypass D3.

Therefore:

> Authoring locality may be locally vertical; acceptance and gate closure remain breadth-first.

This avoids both failure modes:

- old branch-local depth-first completion that loses the global story;
- writing an entire Decision layer without checking whether individual Decisions actually converge toward operational behavior.

## 5. Documentation/BA authority loop

The authority loop remains:

```text
governed documentation B0
 -> accepted BA B0
 -> downstream analysis / diagnostics
 -> corrective documentation candidate
 -> governed review
 -> governed documentation B1
 -> accepted BA B1
```

A BA diagnostic never silently edits project truth. An AI/LLM may infer plausible domain meaning, but plausibility is not sufficient for `GROUNDED` project semantics.

## 6. Current MacroRequirement checkpoint

The current R24 macro set is:

1. `MR-0001 - Controllo dell'accesso all'area riservata`;
2. `MR-0002 - Gestione delle autorizzazioni di accesso`;
3. `MR-0003 - Verifica della persona al punto di accesso`;
4. `MR-0004 - Gestione delle identita`.

Each has been authored through:

```text
id -> title -> lifecycle -> intent -> context -> stakeholders
-> scope -> assumptions? -> constraints? -> dependsOn
```

Current direct dependencies:

- MR-0001 depends on MR-0002 and MR-0003;
- MR-0002 depends on MR-0004;
- MR-0003 depends on MR-0004;
- MR-0004 has no direct MR dependency.

The complete MR audit found no blocking split, merge, overlap, solution leakage or missing direct dependency. Work has therefore moved into Decision review by explicit project/research choice. If a separate formal D1 evidence artifact is required later, it remains a packaging/evidence task rather than a reason to reopen MR semantics without a concrete finding.

## 7. Current MR-level Base Analysis checkpoint

Working candidate BAReferents:

```text
BEHAVIORAL pressure-test notation
*<ControlledAreaAccess>
*<AccessAuthorizationManagement>
*<IdentityVerification>
*<IdentityManagement>

NON-BEHAVIORAL pressure-test notation
#<IdentityVerificationEvidence>
#<AccessAuthorizationState>
#<AccessDecision>
#<GovernedIdentity>
#<PersonAtAccessPoint>
```

`*` and `#` remain authoring/projection pressure-test notation, not an accepted BA1 core distinction. `@<...>` denotes BA2 operator keys in working documentation.

Current propositions:

- P01 `create`: `*<IdentityManagement>` creates `#<GovernedIdentity>`;
- P02 `correlate`: authorization state and governed identity in `*<AccessAuthorizationManagement>`;
- P03 `produce`: `*<AccessAuthorizationManagement>` produces `#<AccessAuthorizationState>`;
- P04 `correlate`: person at access point and governed identity in `*<IdentityVerification>`;
- P05 `produce`: `*<IdentityVerification>` produces `#<IdentityVerificationEvidence>`;
- P06 `produce`: `*<ControlledAreaAccess>` uses authorization state and verification evidence to produce `#<AccessDecision>`;
- P07 `dependOn`: `*<ControlledAreaAccess>` depends on both authorization management and identity verification;
- P08 `dependOn`: authorization management depends on identity management;
- P09 `dependOn`: identity verification depends on identity management.

P01-P09 remain `GROUNDED / PENDING_REVIEW` in the working BA checkpoint.

Known MR-level BA diagnostics still retained:

- MR-0001 scope also covers making access possible when the outcome permits it, not yet separately materialized by P06;
- MR-0002 maintenance-over-time semantics are not separately materialized by P02/P03;
- MR-0004 maintenance-over-time semantics are not separately materialized by P01;
- behavioral vs non-behavioral BAReferent nature remains a pressure point, not an accepted contract change.

## 8. Decision authoring - working rules

A Decision is a significant governed commitment that narrows exactly one MR through a policy, strategy, responsibility boundary, convention, technology/architecture choice or other project position with downstream consequences.

Core shape remains:

```text
Decision
|- title
|- context
|- decision
`- consequences
```

### 8.1 Decision significance threshold - R24-WORKING

Semantic importance alone is not enough to justify a standalone Decision.

A candidate Decision is stronger when one or more of the following hold:

- materially different project alternatives exist;
- the choice governs multiple downstream behaviors/FRs;
- rationale, trade-off or responsibility boundary has value independent of one operational clause;
- the commitment may be reopened independently if assumptions/constraints change;
- the choice stabilizes project meaning across different realizations.

A `1 Decision -> 1 FR` cardinality is **not** a defect. The test is semantic function, not count. A necessity/default Decision remains valid when no materially distinct alternative exists, provided it is a real, reopenable commitment with downstream consequences.

### 8.2 Cross-domain semantic explicitness - R24-WORKING

Working authoring principle to preserve and pressure-test:

> A materially determining project commitment should not be left only to the implicit knowledge of one professional domain when competent consumers from another domain could reconstruct materially different behavior while believing it compatible with the documentation.

Companion safeguards:

- domain knowledge that merely explains reality does not automatically become a Decision;
- `AI-INFERABLE` does not mean `BA-GROUNDED`;
- `HUMAN-OBVIOUS` does not mean `GOVERNED-EXPLICIT`;
- necessary explicitness must be placed at the semantically correct document level, not promoted automatically to an ADR;
- do not duplicate meaning already governed at another level.

This principle belongs in research/authoring guidance. It must **not** be inserted into a project ADR as commentary about humans, programmers, LLMs or the research method.

### 8.3 Downstream projection test - R24-WORKING

During D2, each candidate Decision should be projected immediately toward its principal FR consequences before moving on.

Questions:

1. What observable/testable behavior would operationalize this commitment?
2. Does the projection reveal that the candidate is actually only an FR-level obligation?
3. Does the Decision retain independent semantic value after the FR is written?
4. Does the projection expose a missing responsibility boundary or undocumented dependency?
5. Does the projection converge toward tests/code, or only add semantic prose?

Projected FRs remain working D2 evidence until D3 review.

### 8.4 Operational convergence - R24-WORKING

Documentation quality is a means to reliable realization and analysis, not an end in itself.

> A decomposition that keeps adding semantic contour without increasing the ability to derive operational FRs, tests, code trace or useful analysis is a signal of excessive granularity or misplaced documentation.

The expected direction is:

```text
Problem framing
 -> MR
 -> significant Decision
 -> operational FR
 -> Specialized/Security requirement where justified
 -> test evidence
 -> realization/code
```

BA should reduce cognitive cost through normalized identity, relations, provenance and generated views; it must not become an additional bureaucracy layer.

## 9. Project documentation vs research commentary - R24-WORKING

Two artifacts are intentionally separated:

### Project documentation

Contains only current facial-access project meaning:

- Project Problem Framing;
- current MR candidates;
- current project Decisions;
- current working FR content as it is introduced.

It must not contain:

- why a wording choice is useful to LLMs;
- cross-domain research conclusions;
- BA contract pressure-point discussion;
- methodology diagnostics/checkpoint prose;
- commentary about authoring experiments.

### Research/methodology artifacts

Contain:

- BA delta and diagnostics;
- cross-domain semantic explicitness observations;
- Decision significance/granularity findings;
- downstream projection protocol;
- gate/evidence state;
- migration rationale and falsification targets.

This separation is now a required quality check for future generated project-documentation PDFs.

## 10. Current Decision checkpoint - MR-0001 / ADR-0001

Current candidate:

`ADR-0001 - Politica congiuntiva per la decisione di accesso`

Semantic commitment:

```text
ALLOW requires
  favorable #<AccessAuthorizationState>
  AND
  positive #<IdentityVerificationEvidence>
```

Neither condition is sufficient alone.

The ADR contains only project context, project commitment and project consequences. Cross-domain/AI motivation is intentionally retained only in this work plan/handoff.

### 10.1 Downstream FR projection

Current working projection:

`FR-0001 - Determinazione congiuntiva dell'esito di accesso`

Operational meaning:

- when authorization state is favorable and verification evidence is positive, `*<ControlledAreaAccess>` must produce an `#<AccessDecision>` that allows access;
- when at least one condition is not satisfied, it must produce an `#<AccessDecision>` that does not allow access.

The current projection naturally supports a test matrix over authorization x verification. It is included in the working project-documentation artifact for continuity, but D3 has not been globally reviewed/closed.

### 10.2 BA delta pressure test for ADR-0001

Do not assign a new proposition ID yet.

Initial `constrain` modeling was reconsidered because authorization state and verification evidence are not naturally `constraintValue` terms. The stronger candidate is a Decision/FR-level specialization of the existing `produce` semantics:

```text
produce
actor  -> *<ControlledAreaAccess>
input  -> #<AccessAuthorizationState>
input  -> #<IdentityVerificationEvidence>
result -> #<AccessDecision>
condition -> authorization favorable AND verification positive
```

This must be checked against BA3 identity/continuity rules before deciding whether it is a distinct BAProposition, a replacement/specialization relation, or another supported representation. P06 must not be silently rewritten.

## 11. Historical Decision corpus migration rule

Historical Decisions remain regression evidence and must be decomposed under the current MR ownership map rather than copied branch-for-branch.

The next historical item of interest is the old MR-0001 decision concerning non-conclusive verification outcomes. It previously mixed at least two meanings:

```text
A. verification semantics:
   inconclusive != positive != negative
   -> natural owner: current MR-0003

B. access consequence:
   inconclusive cannot satisfy positive verification
   -> may already follow from ADR-0001 + verification semantics
```

The next session must determine whether A is a significant Decision or belongs directly at FR level under the current hierarchy. Do not create a second MR-0001 ADR merely to restate a consequence already implied by the conjunctive access policy.

## 12. Phase-2 Decision workflow from this checkpoint

For each historical/current candidate Decision:

1. identify the still-valid project meaning;
2. determine the current MR semantic owner;
3. test whether the meaning is already governed by the MR;
4. apply the Decision significance threshold;
5. write `title/context/decision/consequences` only if it is a real Decision;
6. reconstruct the Decision-level BA delta without changing accepted MR BA silently;
7. perform the immediate downstream FR projection test;
8. keep the FR projection provisional until the breadth-first D2 Decision set is complete;
9. move to the next Decision at the same abstraction level;
10. only after all relevant Decisions are reviewed, decide D2 and enter formal D3 review.

## 13. D2 gate

D2 passes when:

- all relevant Decisions across all MR branches have been examined at the same abstraction level;
- each surviving Decision clearly narrows exactly one MR;
- Decision inflation has been avoided;
- cross-domain explicitness gaps that materially affect project commitments are governed at the appropriate level;
- responsibility boundaries needed by FRs are explicit;
- downstream projections show plausible operational convergence;
- Decision-level BA delta is representable or an explicit BA pressure point is recorded;
- the MR story remains valid and is concretized rather than rewritten accidentally.

## 14. FR phase constraints carried forward

When D3 formally begins:

- every FR has exactly one parent Decision;
- FRs are readable, independently assessable operational obligations;
- cross-MR service/meaning reuse does not create multiple parents;
- split capability only when behaviors can change independently;
- preserve failure/correlation/lifecycle semantics actually governed;
- do not invent request origins, stores, model bindings, channels or processors to make a diagram complete;
- prefer requirements that can be connected naturally to test cases and later code/realization evidence.

## 15. Specialized/Security phase constraint

The deliberate problem-framing phrase concerning consequences of personal/biometric information remains an observation/falsification target. Do not introduce a privacy/security MR merely to satisfy it. Observe whether the concern emerges naturally at Decision, FR or, more plausibly, Specialized/Security Requirement level and under later security/privacy analysis methods.

## 16. Specific R24 pressure/falsification targets retained

Retain at least:

- behavioral vs non-behavioral BAReferent nature;
- MR scope semantics not yet separately represented by P01-P09;
- Decision significance vs ADR inflation;
- cross-domain semantic explicitness;
- downstream FR projection as a scalability/efficiency mechanism;
- hierarchy pressure when an FR seems necessary but no materially significant non-default Decision exists;
- cross-MR handoff/binding;
- verification evidence sufficiency and non-conclusive semantics;
- test/code traceability boundary;
- later transport/channel/model/request bindings when functionally justified;
- emergence (or non-emergence) of privacy/security obligations from the problem framing.

## 17. Current project documentation artifacts

Active pure project-documentation pair:

- `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_PROJECT_ONLY.tex`
- `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_PROJECT_ONLY.pdf`

The artifact uses the established two-column layout and contains only facial-access project documentation at the current working state: framing, four MRs, ADR-0001 and FR-0001. Research commentary/BA diagnostics are intentionally excluded.

The earlier `...MR_COMPLETE.tex/.pdf` remains research working evidence and should not be mistaken for the active project-only document.

## 18. Evidence and packaging rules

For each checkpoint retain:

- exact parent repository baseline;
- changed files only;
- project documentation source + rendered PDF when changed;
- updated research work plan when protocol/checkpoint state changes;
- handoff for continuation when changing chat/session;
- package README with application scope;
- SHA-256 checksums;
- exact resulting commit SHA after push.

Do not commit generated conversation commentary or temporary render images.

## 19. Immediate next step after handoff

Resume at D2 without reopening the accepted current project documentation unless a concrete review finding requires it.

Exact next microstep:

1. read this work plan and the project-only documentation pair;
2. verify the repository HEAD is the commit containing the handoff;
3. keep ADR-0001 as the current first Decision checkpoint;
4. inspect the historical non-conclusive-verification Decision;
5. split its meanings by current MR ownership;
6. decide whether the MR-0003 meaning is a true Decision or should be carried to FR level;
7. if a Decision survives, author it in project-only form, reconstruct its BA delta and immediately project its FR consequence;
8. do not descend into formal D3 closure or SR work yet.

## 20. Stop rules

STOP and classify before continuing when:

- source authority is ambiguous;
- a candidate Decision only repeats MR/FR meaning without an independent commitment;
- project documentation starts containing research/methodology commentary;
- a BA relation would require inventing a semantic role or project link;
- an AI/domain inference is plausible but not governed;
- a projected FR reveals a missing responsibility boundary or current MR ownership conflict;
- a closed BA contract appears insufficient and a concrete smallest counterexample must be isolated.

Do not resolve a STOP by adding undocumented components, relations, thresholds, security mechanisms or domain assumptions.
