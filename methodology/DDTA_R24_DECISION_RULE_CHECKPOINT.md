# DDTA R24 - repository-alignment / decision-rule checkpoint

**Status:** WORKING CHECKPOINT / REPOSITORY ALIGNMENT COMPLETE
**Repository baseline reviewed:** `1912bc9a90bf076c50caf496f7f135bece010bad`
**Purpose:** record the current R24 research state, the authority boundary, the accepted BA pressure-test findings, and the completed repository-alignment state before project authoring resumes.

## 1. Authority boundary

The repository currently contains two intentionally different facial-access layers.

### Current governed baseline

`governed-corpora/facial-access/current/` remains the current governed facial-access baseline registered as `FACIAL_ACCESS_CURRENT_R1`.

It remains authoritative until an explicit promotion / supersession decision replaces it. Its content is not silently rewritten to match R24 research work.

### R24 working successor candidate

`methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_PROJECT_ONLY.tex` is working R24 project documentation used to pressure-test the methodology.

It is **not** `CURRENT_GOVERNED` and does not supersede `FACIAL_ACCESS_CURRENT_R1` merely because it is newer or more abstract.

The intended research flow is therefore:

```text
CURRENT_GOVERNED baseline
  -> R24 working successor candidate
  -> BA pressure test
  -> downstream analysis / test usefulness check
  -> explicit promotion / supersession decision
  -> next governed baseline
```

Historical drop-ins, checksums, snapshots and explicitly non-canonical working packages remain historical/research evidence and are not rewritten merely to make old artifacts look current.

## 2. Accepted BA2 findings retained

1. Functional Requirements should be independently assessable and should naturally support test-case derivation.
2. `IF / THEN / ELSE` is an appropriate readable form when an FR explicitly governs how a result is determined from conditions.
3. Detailed result-construction logic should not be pulled into MR merely because BA can represent it.
4. MR-level `produce` remains the correct coarse relation for a produced result.
5. `decisionRule` is the current BA2 construct for explicitly governed conditional result construction.
6. `condition`, `constrain` and `dependOn` remain valid semantics and must not be used as substitutes for a governed decision rule.
7. `dependOn` is retained because prerequisite semantics enable impact propagation and indirect criticality discovery.
8. `classify` remains proposition semantics; no current evidence justifies removing or collapsing it.
9. A governed finite semantic domain is a legitimate `constrain` use when the source restricts allowed values but does not govern how one value is selected.
10. For that case BA2 accepts a structured controlled `constraintValue`:

```text
constraintValue
  property   -> <controlled semantic key>
  vocabulary -> [<controlled typed local value | BAReferent> 1..*]
```

11. The vocabulary form does not assert a runtime value and does not define a selection algorithm.
12. No new `valueOf` operator is justified by the current evidence.
13. Current R24 comparison evidence addresses a governed property of a richer semantic referent. `IdentityVerificationEvidence = TRUE` would collapse the evidence object with the value of its `correspondence` property.
14. The current R24 `decisionRule.comparison` lower bound therefore requires `property -> <controlled semantic key>`.
15. No property-less comparison is admitted without a concrete governed counterexample.
16. `resultAssignment` remains `target + value`; no `resultAssignment.property` is justified by current evidence.
17. `[TRUE, FALSE, UNKNOWN]` may be a governed local vocabulary where documented; it does not introduce general three-valued BA truth tables, evaluation order or logical propagation.
18. No general cleanup/removal of other BA operators is authorized by this checkpoint.

## 3. Semantic separation retained

```text
produce
  -> what result is produced/made available

constrain
  -> which governed semantic values are allowed for a property

decisionRule
  -> how governed conditions select/construct a result value

comparison
  -> which governed property of an input is compared with which value

dependOn
  -> which prerequisite/dependency can propagate impact
```

`constrain` defines admissible / allowed semantic value space. `decisionRule` defines how governed conditions select or construct a result inside a governed result space.

## 4. MR-0003 verification-outcome pressure test

The active R24 working project document currently contains `MR-0003 — Verifica della persona al punto di accesso`. The candidate Decision and FR discussed in research have **not** yet been inserted into that project document.

Current candidate ownership remains:

```text
MR-0003ADR-0001
  -> semantic choice for correspondence outcome distinction

MR-0003ADR-0001FR-0001
  -> authoritative observable/testable functional meaning
```

The accepted semantic direction remains:

```text
IdentityVerificationEvidence.correspondence ∈
  [TRUE, FALSE, UNKNOWN]
```

with project meaning:

```text
TRUE
  -> evidence supports correspondence

FALSE
  -> evidence supports non-correspondence

UNKNOWN
  -> evidence supports neither conclusion sufficiently
```

The current BA candidate remains:

```text
constrain
  constraintTarget -> IdentityVerificationEvidence
  constraintValue
    property   -> correspondence
    vocabulary -> [TRUE, FALSE, UNKNOWN]
```

This representation intentionally does not invent thresholds, scores, algorithms, retry behavior or a general three-valued logical calculus.

A `decisionRule` selecting `TRUE`, `FALSE` or `UNKNOWN` is **not justified** by the current project documentation because no governed selection conditions, thresholds or algorithm are documented.

No project proposition ID is assigned to this candidate until the Decision/FR wording is accepted and inserted into the appropriate governed/working project source.

## 5. MR-0001 status and open pressure points

The MR-grounded proposition remains:

```text
P06
produce
  actor  -> ControlledAreaAccess
  input  -> AccessAuthorizationState
  input  -> IdentityVerificationEvidence
  result -> AccessDecision
```

A complete FR-grounded access `decisionRule` is not materialized yet.

The current access FR governs that access may be allowed only when both authorization and positive verification conditions are satisfied, but the positive branch still needs explicit project wording if the intended contract is:

```text
IF authorization valid AND verification positive
THEN MUST ALLOW
ELSE MUST NOT_ALLOW
```

That issue remains separate from the MR-0003 verification-outcome work.

### `AccessAuthorizationState` remains unresolved

The current MR-0002 project documentation does not yet govern a semantic property/vocabulary such as:

```text
AccessAuthorizationState.authorized -> TRUE | FALSE
```

and it does not govern `UNKNOWN` as an authorization-state value.

Therefore the following comparison must **not** be treated as already grounded project meaning:

```text
comparison
  referent      -> AccessAuthorizationState
  property      -> authorized
  comparisonKey -> equals
  value         -> TRUE
```

This is an open project-semantics pressure point, not a counterexample that falsifies the current BA2 requirement for property-addressed comparisons.

The verification-side condition remains semantically well-formed once its project meaning is governed:

```text
comparison
  referent      -> IdentityVerificationEvidence
  property      -> correspondence
  comparisonKey -> equals
  value         -> TRUE
```

## 6. Downstream usefulness question remains open

The current `constrain` representation is sufficient to encode that `IdentityVerificationEvidence.correspondence` has the allowed domain `[TRUE, FALSE, UNKNOWN]` and that no fourth value is admitted.

It has **not yet been demonstrated** that BA alone carries every oracle needed to derive concrete tests for the functional meanings:

```text
TRUE     -> evidence supports correspondence
FALSE    -> evidence supports non-correspondence
UNKNOWN  -> evidence supports neither conclusion sufficiently
```

Before adding any BA operator or richer structure, R24 must first decide what information downstream test derivation is expected to obtain directly from BA and what information may remain governed by the traced FR prose.

This is a future pressure test after repository alignment and exact project wording are stabilized.

## 7. Repository-alignment closure

The repository-alignment audit was repeated against baseline `1912bc9a90bf076c50caf496f7f135bece010bad` before this closure pass.

At that reviewed baseline:

1. Root `README.md` correctly distinguishes `FACIAL_ACCESS_CURRENT_R1` as `CURRENT_GOVERNED` from the R24 working successor/research material.
2. Root `INDEX.md` is aligned as the repository map rather than the older working-package-style index.
3. `governance/document-authority/` preserves the explicit authority boundary: R24 working material is not promoted merely because it is newer.
4. `governance/decisions/TADR-0001_separate_research_repository.md` is lifecycle-aligned with the repository practice already in use.
5. `BA2_RELATION_ACTION_VOCABULARY_R2.md` is the active R24 working BA2 revision and is aligned with the findings in this checkpoint; the unresolved authorization representation remains an open project-semantics pressure point.
6. BA1, BA3, BA4 and BA5 remain closed for their accepted scopes. Their R24 alignment notes correct forward-use sequencing without reopening those closed semantics.
7. `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R1.md` is aligned with the current `decisionRule` lower bound and no longer treats `AccessAuthorizationState.authorized = TRUE` as grounded facial-access meaning.
8. The tracked `.tex/.pdf` renderings associated with the aligned BA1, BA3, BA4 and BA5 Markdown contracts are regenerated in this closure pass so those artifact triads remain synchronized.
9. Historical state/work-plan snapshots, drop-ins, checksums and explicitly non-canonical working packages remain historical evidence unless they incorrectly claim current authority.

No additional forward-facing repository-alignment debt was identified by the repeated audit. Repository alignment is complete once this closure pass is committed and pushed.
## 8. Exact next research microstep

Repository alignment is complete. Before resuming the Facial Access vertical slice at `MR-0003`, R24 now executes the bounded literature/pattern step defined by `DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R23.md`.

The trigger is a material semantic-classification question discovered during human review: the current Facial Access use case begins with a person whose governed identity is not yet known, while the working project model currently uses `IdentityVerification`. R24 must determine whether literature-backed problem/domain/requirements/security patterns can help discriminate identification, verification, authentication, authorization and access-decision responsibilities without importing architecture or becoming project authority.

The active sequence is:

```text
R23 literature source registration / access verification
  -> standard reading cards + citation-ready excerpts
  -> cross-source pattern synthesis
  -> DDTA pattern-template candidate
  -> Facial Access identification/verification pressure test
  -> return to MR-0003 wording
  -> MR-0003ADR-0001
  -> MR-0003ADR-0001FR-0001
  -> minimum justified BA derivation
  -> downstream analysis / test usefulness check
```

The first R23 reading microstep is `PAT-LIT-03 — The Domain Theory for Requirements Engineering`, using the existing `literature/templates/source-note.template.md`. `PAT-LIT-*` is a work-plan-local label; the source receives a real `SRC-*` identity only when it is registered in the literature corpus.

No pattern catalog, pattern match or design pattern becomes project authority. Pattern research must not automatically emit project requirements, BA referents, BA propositions or BA2 operators.

The vertical slice must preserve the current authority boundary: R24 remains working/non-canonical until an explicit promotion or supersession decision changes that status.

The authorization-side normalized comparison remains open until governed project semantics justify its property/value structure. Do not materialize `AccessAuthorizationState.authorized = TRUE`, scalar `AccessAuthorizationState = AUTHORIZED`, or an equivalent normalized authorization comparison without that evidence.

A verification-selection `decisionRule` remains **NOT JUSTIFIED** while the project source governs only the correspondence outcome domain/meaning and not the selection conditions, thresholds or algorithm.

Before BA2 is considered stable beyond this working R24 lower bound, pressure-test it against at least one non-Facial-Access governed domain.

Normative keywords in project prose remain English (`MUST`, `MUST NOT`, etc.). Semantic operator keywords remain English (`produce`, `dependOn`, `decisionRule`, `condition`, `constrain`, `classify`, `actor`, `result`).