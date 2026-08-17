# DDTA BA3-T3 derivation-rule reproducibility and change-impact lineage pressure test - R1

**Status:** COMPLETED / PROVISIONAL PASS WITH DERIVATION-IMPACT REFINEMENT

**Repository baseline tested:** `5fc0b92809ece193deaba4206488d78f981f7855`

**Scope:** only BA3-T3. BA4, formal threat-method overlays, AnalysisRecord, Common Finding and implementation design remain out of scope.

## 1. Test objective

BA3-T3 tests three falsifiable propositions left open by T2:

1. `derivationBasis + derivationRuleRef` is enough for reproducible review only if the basis and rule semantics are sufficiently explicit;
2. direct source provenance plus BA structure is enough for localized change impact only if all meaning-relevant governed context is represented;
3. the analysis-to-correction feedback loop can remain outside BA source authority while still being traceable back into the next governed baseline.

The test uses concrete mutation/provider cases rather than constructing a generic dependency engine.

## 2. Starting lower bound

Before T3, BA3 had:

```text
BAOriginAttachment
|- targetElement
|- governedBaselineKey
|- originState
|- sourceLink
|- derivationBasis
`- derivationRuleRef

BABaselineReview
|- targetElement
|- evaluatedBaselineKey
|- reviewState
`- freshness

BACrossBaselineContinuity
|- priorElement
|- targetBaselineKey
|- disposition
|- successorElement
`- continuityBasis
```

T2 also identified a staleness candidate when known effective governed context changes, but the exact representation of that context remained open.

## 3. Falsification attempt A - plain derivation-basis list

### Hypothesis A0

> A derived BA element can remain reproducible with an unordered/untyped list of basis references plus an opaque rule reference.

### Pressure case

The order/payment corpus distinguishes provider-specific raw status from governed project status. A normalization derivation needs at least two conceptually different inputs:

```text
provider vocabulary/status evidence
project-governed mapping/contract
```

If both are stored merely as:

```text
derivationBasis = [source-A, source-B]
```

a reviewer cannot determine which source is the mapping authority, which one provides the raw vocabulary, or whether a tool silently embedded the mapping.

### Result

```text
A0 REJECTED
```

The basis must be role-bound under the referenced rule:

```text
inputRoleKey -> basisRef
```

The role key belongs to the rule contract, not BA2 proposition participation.

## 4. Falsification attempt B - opaque/unversioned derivation rule

### Hypothesis B0

> `derivationRuleRef = provider-normalization` is sufficient even if the rule definition can change in place.

### Counterexample

Suppose revision R1 maps provider outcomes using one governed status interpretation and revision R2 changes applicability/output semantics. If historical derived elements reference only the mutable name, replaying B0 later can silently use R2 and produce a different BA result.

### Result

```text
B0 REJECTED
```

A derivation reference must resolve to an immutable rule revision. The registry entry must expose input roles, applicability, output semantic contract and a method-neutral normative definition/rationale.

An implementation can store these as one document or several fields; the semantic responsibility is what matters.

## 5. Reproducibility threshold

The test deliberately rejects machine-execution as the threshold.

Required:

```text
same baseline
+ same role-bound basis
+ same immutable rule revision
+ same accepted semantic registries
    -> materially equivalent semantic result
       or an explicit non-applicability/diagnostic outcome
```

Not required:

```text
same UUID
same JSON byte order
same graph traversal order
same software implementation
same LLM/tool version
```

If hidden analyst/tool judgment is required to choose among materially different outputs, the derivation is not reproducible enough for silent `ACCEPTED` status.

## 6. Provider-state normalization replay

### Governed payment case

The corpus governs `PaymentAuthorizationResult` as:

```text
authorized
 declined
 indeterminate
```

while provider-specific raw states remain behind the adapter/contract boundary.

A valid derived normalization needs a governed source that authorizes the concrete mapping. The method-neutral rule may say:

> apply the governed provider-to-project status mapping and materialize the corresponding controlled project semantic result.

It may not say, without governed evidence:

```text
provider APPROVED means authorized
```

### Cross-domain control

The same pattern appears in:

- external WMS reservation results;
- carrier acceptance/status normalization;
- any provider-specific raw result mapped behind a governed project contract.

### Result

```text
PASS
```

One rule-registry contract works across the distinct domains without importing payment/WMS/carrier vocabulary into Base Analysis core semantics.

## 7. Falsification attempt C - direct provenance is enough for M4

### Hypothesis C0

> A grounded proposition needs only its direct source links; sibling governed context can be ignored until the direct FR changes.

### B0

The camera corpus has remote recognition and `FR-3.4` delivers `RecognitionCapture` to `RecognitionProcessor`.

A grounded BA proposition is:

```text
P0 = transfer(CameraSubsystem,
              RecognitionProcessor,
              RecognitionCapture)
```

### B1 mutation

A sibling representation Decision changes the boundary representation:

```text
RecognitionCapture -> OpaqueEvidenceReference
```

while, as an adversarial intermediate state, the old FR text has not yet been corrected.

With only `sourceLink(FR-3.4)`, P0 receives no change trigger and can be falsely treated as current.

### Result

```text
C0 REJECTED
```

The proposition requires an explicit `revalidationContext` link to the representation commitment when that commitment is known to determine validity/applicability.

## 8. M4 authority test - stale/diagnose, do not invent

Once the sibling representation Decision changes, T3 tests two possible reactions.

### Alternative 1 - silent rewrite

```text
P0 capture-transfer
    -> automatically rewrite to
P1 opaque-reference-transfer
```

without governed FR correction.

```text
REJECTED
```

This would allow BA to repair project documentation and become a second authority.

### Alternative 2 - localized revalidation

```text
changed revalidation context
    -> P0 STALE / PENDING_REVIEW
    -> source/context inconsistency localized
    -> DIAGNOSTIC_UNRESOLVED if no governed resolution exists
```

After governance corrects/supersedes `FR-3.4`, the next baseline can ground P1 from the corrected FR and apply T2 `REPLACE` continuity to P0.

```text
PASS
```

This is the required behavior.

## 9. Why `revalidationContext` is not a generic dependency graph

The pressure test tries three representations.

### Parentage only

Fails M4 because the influential Decision is sibling context.

### BA2 `dependOn`

Rejected because it would assert project-semantic prerequisite meaning that may not exist.

### Generic `affects`

Rejected as too weak/underspecified for the current lower bound; it invites a broad dependency ontology without saying what analytical responsibility the edge carries.

### Retained minimum

```text
revalidationContext(targetElement, contextRef)
```

with one precise analytical meaning: a material change to the context is a reason to revalidate the target.

## 10. Localized staleness algorithm probe

Starting changed governed source set `DeltaSource`, the lower bound can seed review without scanning every BA element semantically from scratch:

```text
Seed S with elements whose:
  sourceLink intersects DeltaSource
  OR revalidationContext intersects DeltaSource

Repeat:
  if a derived element has a basisRef in S -> add it to S
  if an element has revalidationContext to a BA element in S -> add it to S
  if a proposition binds a referent
     replaced/retired through T2 review
     -> add it to S

For each element in S:
  mark PENDING_REVIEW / STALE for target baseline
  resolve semantically to RETAIN | REPLACE | RETIRE
```

This is a responsibility-level algorithm sketch, not an implementation data structure or scheduler.

### Negative control

```text
one changed file -> all BA elements stale
```

remains rejected.

## 11. Rule revision change probe

A derived BA element records the immutable rule revision used in its historical origin.

If a later methodology revision changes the rule itself, historical meaning is not rewritten. For a new materialization/review context the element is re-evaluated under the explicitly selected current rule revision.

Possible T2 outcomes:

```text
same semantic result -> RETAIN
materially different result -> REPLACE
no longer applicable -> RETIRE or DIAGNOSTIC_UNRESOLVED
```

This prevents methodological drift from silently changing the meaning attributed to an older baseline.

## 12. Feedback lineage pressure

### Analysis-produced candidate

A downstream analysis may identify a gap in, for example, the representation/FR relationship. To localize corrective feedback it can carry:

```text
BAElementRef@B0
GovernedSourceRef@B0
```

obtained from Base Analysis provenance.

### Rejected correction

If governance rejects the proposed correction:

```text
analysis output exists
project documentation unchanged
BA source authority unchanged
```

No new grounded BA element is introduced.

### Accepted correction

If governance accepts the correction:

```text
analysis/candidate
    motivates
new governed documentation B1
    grounds
BA@B1
```

The BA@B1 `sourceLink` points to B1 governed documentation, **not** to the finding/candidate that motivated it. T2 continuity connects BA@B0 and BA@B1 where appropriate.

### Result

```text
PASS WITHOUT NEW BA ANALYSIS IDENTITY
```

The BA layer already exposes the handles required for downstream analysis/change provenance. Exact AnalysisRecord/change-event lineage remains downstream work and is not forced into BA3.

## 13. Cross-layer authority invariant

The complete tested chain is:

```text
governed docs B0
    -> BA B0
    -> downstream analysis
    -> corrective documentation candidate
    -> governed review
    -> governed docs B1
    -> BA B1
```

The only transitions that establish project truth are governed-document acceptance transitions. BA derivation rules and analysis outputs never bypass that gate.

## 14. Reopen checks

### BA1

No new independently reusable project-semantic identity family is required. Rule descriptors and revalidation links are metadata responsibilities.

```text
BA1 REOPEN: false
```

### BA2

No new project-semantic operator is required. In particular, `revalidationContext` is not `dependOn` and does not enter the BA2 operator registry.

```text
BA2 REOPEN: false
```

### BA3-T1

T1 is refined by role-binding `derivationBasis`; its provenance/origin responsibilities remain valid.

```text
T1 REOPEN: false
```

### BA3-T2

T2 staleness/lifecycle semantics remain valid; T3 supplies the previously open effective-context representation needed to seed them.

```text
T2 REOPEN: false
```

## 15. Disposition table

```text
Plain untyped derivationBasis list                 REJECTED
Role-bound derivationBasisBinding                  REQUIRED
Mutable/opaque derivation rule                     REJECTED
Immutable inspectable rule revision                REQUIRED
Universal executable rule language                 REJECTED
Semantic replay reproducibility                    REQUIRED
M4 parentage-only change detection                 REJECTED
Explicit revalidationContext                       REQUIRED
revalidationContext -> BA2 dependOn                REJECTED
Global BA invalidation on any source change        REJECTED
Localized staleness propagation                    PASS
Auto-repair BA from sibling source                 REJECTED
Provider mapping hidden in tool                    REJECTED
Governed provider mapping as derivation basis      REQUIRED
  when the mapping itself is derived
Analysis finding/candidate as BA source             REJECTED
New BAE family                                     NOT FORCED
BA1/BA2 reopen                                     NOT TRIGGERED
Distinct BA3 closure review                        REQUIRED
```

## 16. Exit condition assessment

BA3-T3 exits with:

```text
COMPLETED / PROVISIONAL PASS WITH DERIVATION-IMPACT REFINEMENT
```

The T1/T2 lower bounds survive with two refinements:

1. derivation basis is role-bound and references an immutable inspectable rule revision;
2. explicit `revalidationContext` captures non-source/non-derivation governed context needed to seed localized review.

The feedback loop requires no new BA authority or BAE family.

A distinct BA3 closure review is still required because T1-T3 have accumulated multiple orthogonal metadata responsibilities that must be adversarially checked for redundancy, contradiction and cross-corpus sufficiency before BA4 begins.

## 17. Next authorized microstep

Only after this package is reviewed, committed, pushed and remotely verified:

> **BA3-T4 - provenance, identity/lifecycle and derivation/change-impact closure review.**

Do not start BA4 until that review either closes BA3 or reopens the smallest failed BA3 responsibility.
