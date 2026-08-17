# BA3-T4 - Provenance, identity/lifecycle and derivation/change-impact closure review

**Revision:** R1

**Status:** CLOSED / PASS / BA3 CLOSED

**Repository baseline reviewed:** `a20a590d771b1053ecbd095d8a8c4255ae762bfe`

**Phase:** BA3 - provenance, derivation, identity/lifecycle and change-revalidation mechanics

**BA0:** CLOSED

**BA1:** CLOSED

**BA2:** CLOSED

**BA4:** NOT STARTED

## 1. Closure question

BA3-T4 asks only:

> Can the combined BA3-T1/T2/T3 contract be reduced, merged or simplified without losing source drill-down, derivation reproducibility, uncertainty localization, cross-baseline identity history, targeted revalidation or the governed-document authority boundary?

The review is adversarial closure, not vocabulary discovery. No new BA3 mechanism is accepted unless removal/collapse pressure exposes a concrete material counterexample.

## 2. Evidence reviewed

The closure review reuses the controlled evidence already established by the BA3 sequence:

1. BA0 responsibility/non-goals and governed-document authority boundary;
2. BA1 closed `BAReferent + BAProposition` identity ontology;
3. BA2 closed proposition/operator/role semantics;
4. BA3-T1 provenance/origin lower bound;
5. BA3-T2 M1/M2/M3 and order/WMS identity/lifecycle pressure;
6. BA3-T3 M4, provider-state normalization and feedback-authority pressure;
7. diagnostic resolution across governed correction.

No new method-specific ontology, STRIDE schema, ThreatForge runtime model or arbitrary implementation requirement is introduced.

## 3. Reduction review - provenance and baseline scope

### 3.1 Remove provenance from one BA1 identity family

**Attempt:** keep proposition provenance only and infer referent provenance from participating propositions, or vice versa.

**Result:** REJECTED.

A referent can survive while propositions about it change, and a proposition can cite a clause whose participating referents are supported across different source branches. Removing independent provenance from either family makes source drill-down and lifecycle review depend on indirect reconstruction.

**Disposition:** `PASS / INDEPENDENT PROVENANCE RETAINED`.

### 3.2 Remove immutable governed-baseline scope

**Attempt:** identify source evidence by document identity + locator only.

**Result:** REJECTED.

M1 directly falsifies this reduction: `D-3.5` can remain the recognizable Decision area while its realization changes from Ethernet to Wi-Fi. A baseline-free source pointer can conflate materially different governed meanings.

**Disposition:** `PASS / BASELINE SCOPE RETAINED`.

### 3.3 Replace exact locator with copied source prose

**Attempt:** copy source text into BA and treat the copy as evidence.

**Result:** REJECTED.

The copy can drift and would create a second authority. Exact drill-down to the governed baseline remains the semantic lower bound; cached excerpts remain non-authoritative display aids.

**Disposition:** `PASS / GOVERNED LOCATOR RETAINED`.

## 4. Reduction review - source, derivation and context links

### 4.1 Merge `sourceLink` and `derivationBasisBinding`

**Attempt:** use one undifferentiated `evidence` relation.

**Result:** REJECTED.

Direct governed support and analytical derivation input answer different authority questions. A derived classification may use an accepted BA proposition as basis, but that proposition is not itself the project authority for the classification. Conversely, a grounded transfer needs direct source support without being analytically derived.

**Disposition:** `PASS / SEMANTIC SEPARATION RETAINED`.

### 4.2 Merge `revalidationContext` into `sourceLink`

**Attempt:** treat every context that can invalidate an element as direct source provenance.

**Result:** REJECTED by M4.

The sibling representation Decision must make the old capture-transfer meaning stale, but it does not directly ground a successor `transfer(... OpaqueEvidenceReference)` proposition. Promoting it to source authority would permit silent BA repair from context rather than governance.

**Disposition:** `PASS / REVALIDATION CONTEXT RETAINED`.

### 4.3 Merge `revalidationContext` into derivation basis

**Attempt:** treat effective context as an analytical derivation input.

**Result:** REJECTED.

M4's old transfer is grounded in `FR-3.4`; the sibling Decision affects its validity but does not make the proposition derived. The same problem appears wherever a grounded assertion's applicability depends on a separately governed context.

**Disposition:** `PASS / CONTEXT IS NOT DERIVATION`.

### 4.4 Promote `revalidationContext` to BA2 `dependOn`

**Attempt:** reuse the project-semantic dependency operator.

**Result:** REJECTED.

A revalidation trigger does not assert that the project-semantic target requires the context as a domain prerequisite. Doing so would invent project meaning merely to support analysis bookkeeping.

**Disposition:** `PASS / BA2 REMAINS CLOSED`.

## 5. Reduction review - origin, review and freshness dimensions

### 5.1 Collapse `GROUNDED` and `DERIVED`

**Attempt:** treat every accepted BA element as simply source-backed.

**Result:** REJECTED.

Provider normalization and method-neutral classification require explicit analytical transformation. Collapsing origin would allow tool/analyst inference to masquerade as directly governed project truth.

### 5.2 Collapse `DIAGNOSTIC_UNRESOLVED` into `REJECTED`

**Attempt:** treat unresolved meaning as a failed candidate.

**Result:** REJECTED.

A localized contradiction/ambiguity can itself be an accepted analytical diagnostic even though no project-semantic answer is accepted. M4 can require exactly this outcome when sibling Decision and FR remain inconsistent.

### 5.3 Remove `reviewState`

**Attempt:** infer acceptance from presence in the BA store.

**Result:** REJECTED.

Tool/analyst candidates and replacement proposals require a state before acceptance, and rejected candidates may remain auditable without entering accepted BA meaning.

### 5.4 Collapse `freshness` into `reviewState`

**Attempt:** use `PENDING_REVIEW` as the only marker for both new candidates and impacted prior meaning.

**Result:** REJECTED.

A new unreviewed candidate and a previously accepted meaning made suspect by a target-baseline change are different analytical conditions. Historical acceptance for `B0` must coexist with staleness relative to `B1`; freshness therefore remains a distinct semantic dimension even if an implementation computes or co-locates it.

**Disposition for Section 5:** `PASS / ORIGIN != REVIEW != FRESHNESS`.

## 6. Reduction review - derivation reproducibility

### 6.1 Return to untyped `derivationBasis`

**Attempt:** record only an unordered set of basis references.

**Result:** REJECTED by provider normalization.

The raw provider vocabulary and the governed project mapping are not interchangeable inputs. The rule must know which basis item fills which input responsibility.

### 6.2 Allow mutable/unversioned rule references

**Attempt:** reference a logical rule key whose meaning can change in place.

**Result:** REJECTED.

The same basis could produce a different accepted result while historical provenance still points to the same rule name. Exact immutable rule revision is therefore necessary for replay.

### 6.3 Require a universal executable derivation language

**Attempt:** close BA3 only if every derivation can be expressed in one executable DSL.

**Result:** REJECTED AS UNNECESSARY.

Current evidence requires inspectable input roles, applicability, output semantics and normative rationale. Semantic replay is sufficient; byte-identical/tool-identical execution is not a BA0 responsibility.

### 6.4 Require exhaustive derivation-rule enumeration before closure

**Attempt:** predefine every future rule key.

**Result:** REJECTED AS UNNECESSARY.

The descriptor contract is closed; the inventory remains corpus-driven and extensible. A new rule key that satisfies the closed descriptor does not by itself reopen BA3.

**Disposition:** `PASS / ROLE-BOUND BASIS + IMMUTABLE INSPECTABLE RULE IS THE CURRENT LOWER BOUND`.

## 7. Reduction review - continuity and lifecycle

### 7.1 Use one identity-continuity rule for referents and propositions

**Attempt:** retain/replace both families under one generic textual or source-based equivalence test.

**Result:** REJECTED.

M1 preserves `LocalConnectivity` referent identity while replacing the Ethernet realization proposition. M3 can preserve capture identity while retiring remote-transfer assertion identity. Referent reuse and assertion identity therefore have materially different continuity tests.

### 7.2 Copy source-layer `revise` into BA lifecycle

**Attempt:** add or reuse a BA `REVISE` state whenever a governed document is revised.

**Result:** REJECTED.

One source revision can cause some BA identities to retain, others to replace and others to retire. Source revision is not BA semantic identity disposition.

### 7.3 Merge `REPLACE` and `RETIRE`

**Attempt:** use one generic `CHANGE/END` disposition.

**Result:** REJECTED.

M1 realization change has a semantic successor; M3 remote transfer can simply cease to exist. Successor identity versus no successor is analytically material and must remain explicit.

### 7.4 Remove `continuityBasis`

**Attempt:** store only the disposition and successor link.

**Result:** REJECTED.

Cross-baseline identity decisions would become opaque precisely when source wording, realization or document location changes while semantic identity is retained. Baseline-scoped evidence/rationale is required for reproducible continuity review.

### 7.5 Store `SUPERSEDED` and `RETIRED` as independent lifecycle state machines

**Attempt:** create another first-class status dimension.

**Result:** REJECTED AS REDUNDANT.

They are historical interpretations of accepted `REPLACE` and `RETIRE`. No separate semantic family/state machine is required.

**Disposition:** `PASS / RETAIN | REPLACE | RETIRE WITH FAMILY-SPECIFIC IDENTITY RULES RETAINED`.

## 8. Cross-corpus localized-change regression

### 8.1 Facial M1 - Ethernet -> Wi-Fi

Expected closed behavior:

```text
LocalConnectivity                         RETAIN
WiredEthernet                             RETIRE if unused elsewhere
WiFi                                      INTRODUCE
realize(LocalConnectivity, WiredEthernet) REPLACE -> WiFi successor
```

Only directly sourced/context-linked semantics are candidates for revalidation. A transport-realization change does not by itself invalidate unrelated transfer or responsibility assertions, and it does not force BA-wide staleness.

**Result:** PASS.

### 8.2 Facial M2 - external -> project-owned transport

The negative responsibility proposition is replaced by affirmative project responsibility; external service consumption retires if consumption ceases; new transport obligations may be introduced. Abstract connectivity and unrelated consumer meaning can retain.

**Result:** PASS.

### 8.3 Facial M3 - remote -> local recognition

The remote transfer proposition retires; it is not rewritten as a local-processing assertion. Retirement/replacement of the `RecognitionProcessor` participant and explicit context links localize affected transport semantics. Unrelated project meaning is not invalidated globally.

**Result:** PASS.

### 8.4 Facial M4 - raw capture -> opaque reference

The sibling representation Decision is explicit `revalidationContext` for the affected old transfer meaning. When it changes, the old proposition becomes stale. If `FR-3.4` remains inconsistent, BA emits/localizes `DIAGNOSTIC_UNRESOLVED`; it does not synthesize a successor project commitment from the sibling Decision.

**Result:** PASS / decisive evidence that direct source parentage alone is insufficient.

### 8.5 Order/WMS responsibility control

Internal inventory authority semantics retire/replace when responsibility moves to an external WMS. Service/contract/normalization meaning is introduced as required. Unrelated payment/fulfillment/order identities do not become stale without explicit source/basis/context/participant impact.

**Result:** PASS.

### 8.6 Provider-state normalization

A derived governed result uses role-bound raw-vocabulary and governed-mapping inputs under an immutable generic normalization rule. If either input changes, only dependent derived meaning becomes stale. Missing or contradictory mapping yields diagnostic/rejection rather than tool-private truth.

**Result:** PASS.

**Disposition for Section 8:** `PASS / NO OVER-INVALIDATION OR UNDER-INVALIDATION COUNTEREXAMPLE SURVIVES CURRENT EVIDENCE`.

## 9. Diagnostic resolution regression

A prior accepted `DIAGNOSTIC_UNRESOLVED` identity is historical analytical truth for its baseline.

After governed correction:

```text
issue removed                        -> old diagnostic RETIRE
materially different issue remains  -> old diagnostic REPLACE
new grounded/derived meaning         -> own origin/provenance/review
```

Retyping the old diagnostic in place as `GROUNDED` would falsify its historical origin.

**Disposition:** `PASS`.

## 10. Feedback-authority regression

The candidate chain remains:

```text
governed docs B0
 -> BA B0
 -> downstream analysis
 -> corrective documentation candidate
 -> governed review
 -> governed docs B1
 -> BA B1
```

Two adversarial reductions fail:

1. using the analysis finding/candidate as `sourceLink` for `BA@B1` - **REJECTED**, because analysis would become project authority;
2. patching BA directly after an accepted analysis decision before governed documentation changes - **REJECTED**, because the authoritative commitment would exist only in BA/tool state.

The accepted correction grounds the next BA only through governed documentation `B1`.

No `AnalysisRecord`, Finding identity or change-event identity is required inside BA3 to preserve this authority boundary.

**Disposition:** `PASS / GOVERNED DOCUMENTATION REMAINS SOLE PROJECT AUTHORITY`.

## 11. BA1 reopen test

The combined BA3 mechanics require semantic identity for project referents and analytical assertions, but not for a third BAE family.

Provenance attachments, review records, continuity records, rule descriptors, source references, baseline keys and revalidation contexts have metadata responsibilities. None demonstrates both BA1 split criteria: independent project-semantic identity plus reusable subtype-specific invariants that cannot be represented honestly outside a new BAE family.

**Disposition:** `PASS / BA1 REMAINS CLOSED`.

## 12. BA2 reopen test

BA3 uses metadata relations such as source, basis, continuity and revalidation context, but these are not project-semantic assertions.

No current case forces a BA2 `affects`, `derivedFrom`, `revalidates`, `supersedes` or lifecycle operator. Existing project meaning remains representable with the closed 13-key registry.

**Disposition:** `PASS / BA2 REMAINS CLOSED`.

## 13. Analytical-materialization identity check

T4 also asks whether `governedBaselineKey` is insufficient because derivation-rule revisions can evolve independently of project documentation.

Current evidence does not force a new first-class BA materialization identity: every accepted derived element records the exact immutable rule revision used, and the current thesis requires one accepted BA materialization per governed baseline/review context rather than concurrent semantically divergent accepted variants.

This remains an explicit reopen criterion: if a concrete workflow requires multiple concurrent accepted BA materializations for the same governed baseline and their semantic-registry/rule-version context cannot be recovered from element provenance, reopen only this BA3 baseline/materialization responsibility.

**Disposition:** `PASS FOR CURRENT SCOPE / NO NEW BASELINE BAE FAMILY OR MANDATORY KEY FORCED`.

## 14. Representation-independence/minimality check

Several contracts can be physically co-located without semantic loss:

- source/basis/context links may share one edge table with distinct link kinds;
- review/freshness may share one record;
- reverse source-to-BA navigation may be computed;
- lifecycle historical labels may be derived from accepted continuity dispositions.

What cannot be removed is the ability to recover the distinct semantic questions.

This is the closure-level interpretation of the project rule:

```text
semantic responsibility exists
    !=
must become first-class metaclass / class / table / graph node
```

**Disposition:** `PASS / SEMANTIC CONTRACT FROZEN, PHYSICAL REPRESENTATION OPEN`.

## 15. Closure decision

No material counterexample survives the integrated reduction/regression review.

The current evidence does not force:

- reopening BA1 or BA2;
- a new first-class BAE family;
- a new BA2 operator;
- a universal derivation DSL;
- a general dependency graph;
- whole-BA invalidation;
- analysis-output authority;
- or implementation-specific storage semantics.

The T1/T2/T3 responsibilities are therefore accepted as the current-scope lower bound, with the physical-combination freedom and reopen criteria recorded in `BA3_PROVENANCE_DERIVATION_LIFECYCLE_CHANGE_CONTRACT_R1.md`.

```text
BA3-T1   COMPLETED / PROVISIONAL PASS
BA3-T2   COMPLETED / PROVISIONAL PASS
BA3-T3   COMPLETED / PROVISIONAL PASS
BA3-T4   CLOSED / PASS
BA3      CLOSED FOR CURRENT THESIS SCOPE
```

**Next phase:** BA4 projections. BA4 is not executed by this closure package.
