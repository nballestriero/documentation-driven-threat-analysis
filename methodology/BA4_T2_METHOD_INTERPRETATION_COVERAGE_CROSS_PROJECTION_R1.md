# DDTA BA4-T2 method-owned interpretation, coverage loss and cross-projection consistency pressure test - R1

**Status:** COMPLETED / PROVISIONAL PASS WITH INTERPRETATION-COVERAGE REFINEMENT

**Executed against repository baseline:** `f90ef3a0bc0b7712cb8081165c28e8923aec9e2d`

**Input candidate:** `BA4_PROJECTION_BOUNDARY_TRACEABILITY_CANDIDATE_R1.md`

## 1. Question under test

Can the BA4-T1 projection boundary survive two intentionally incompatible method-oriented projections, aggressive information loss, non-current BA state and cross-baseline rebuild without either importing consumer semantics into Base Analysis or inventing a shared projection ontology?

The test is falsification-first. Each probe tries to force a semantic responsibility into the shared core. A responsibility is accepted only when removing it creates a concrete loss of reviewability, coverage honesty, qualification or traceability.

## 2. Fixed dependencies and guardrails

Fixed entering T2:

```text
BA0   CLOSED
BA1   CLOSED
BA2   CLOSED
BA3   CLOSED
BA4-T1 provisional projection lower bound active
```

T2 does not define:

- a complete STRIDE or STRIDE-AI schema;
- a DFD ontology;
- AnalysisRecord or Common Finding;
- ThreatForge classes/tables/UI;
- a universal projection taxonomy;
- BA5 lexical rules; or
- BA6 final holdout closure.

Method labels used below are bounded pressure instruments only.

## 3. Test basis

The main facial-access BA basis includes the already-reviewed meanings:

```text
transfer(CameraSubsystem,
         RecognitionProcessor,
         RecognitionCapture)

correlate(RecognitionCapture, RecognitionRequest)

consumeService(project, LocalConnectivity)

assignResponsibility[negative](
  project,
  underlyingTransport,
  ownership/management)

realize(LocalConnectivity, WiredEthernet)

constrain(delivery, completion/security properties)
```

Controls use facial mutations M1-M4 plus order/WMS/provider meanings, including project-owned versus external inventory responsibility and governed `PaymentAuthorizationResult` normalization.

## 4. Probe P1 - incompatible method taxonomies

### Hypothesis attacked

Two method projections need a shared category ontology to remain consistent.

### Projection F

Local kinds:

```text
FlowParticipant
FlowExchange
ExposureAnnotation
```

It selects transfer/service-use meaning and may interpret service-use plus negative responsibility as:

```text
externally-provided-transport-exposure
```

### Projection A

Local kinds:

```text
AssuranceSubject
AuthorityPlacement
ContractDependency
NormalizationExpectation
```

It selects responsibility/contract/normalization meaning and may interpret the same service/responsibility basis as:

```text
delegated-assurance-dependency
```

### Result

PASS without shared taxonomy.

The two items can be compared through overlapping role-bound BA trace. Their category difference is method-local, not a contradiction.

### Disposition

```text
universal shared projection ontology     REJECTED
BA trace as common semantic anchor        PASS
```

## 5. Probe P2 - descriptor plus trace reproducibility

### Hypothesis attacked

An immutable descriptor plus role-bound BA trace is always sufficient to reconstruct method-owned interpretation.

### Counterexample

One immutable projection revision contains two local rules whose inputs overlap:

```text
R-ext-service
  serviceUse + responsibilityBoundary
    -> externally-provided-transport-exposure

R-assurance-review
  serviceUse + responsibilityBoundary + constraintSet
    -> assurance-dependency-review
```

An item with only `serviceUse` and `responsibilityBoundary` trace identifies its source basis but not which local rule created its method-owned meaning when several rule paths remain valid under the same descriptor.

### Result

The T1 lower bound is insufficient for non-trivial method interpretation.

### Smallest refinement

```text
methodOwnedInterpretation present
    -> interpretationRuleRef required
```

The referenced local rule revision is already contained/resolved under the immutable projection descriptor revision.

### Negative control

No BA3 derivation rule is reused. The interpretation is not method-neutral and cannot create accepted BA meaning.

## 6. Probe P3 - aggressive lossy selection

### Hypothesis attacked

A generic coverage statement can represent both intentionally selective and complete-within-scope projections.

### Counterexample

Two views have the same eligible BA scope:

```text
current accepted transfer propositions
```

but one promises to render all eligible transfers while the other intentionally chooses only transfers touching one analysis focus.

If both use only the statement `transfer propositions are in scope`, an omitted transfer is ambiguous:

- incomplete projection build; or
- valid selective omission.

### Result

T1 coverage contract requires an explicit mode:

```text
EXHAUSTIVE_FOR_DECLARED_SCOPE
SELECTIVE
```

### Important boundary

An omission from an exhaustive projection is a projection completeness defect. It is not a project-level negative proposition and does not prove source documentation incompleteness.

## 7. Probe P4 - omission as negative fact

### Hypothesis attacked

If an exhaustive projection omits an item, the consumer may treat the missing meaning as false in the project.

### Result

REJECTED.

Even under exhaustive coverage, the claim is only:

```text
this materialization failed its declared projection contract
```

The source of project truth remains governed documentation through accepted BA.

## 8. Probe P5 - diagnostic/stale review projection

### Hypothesis attacked

A projection can expose stale or diagnostic BA meaning using the same rendering semantics as current accepted BA.

### M4 pressure

Representation context changes while an older transfer source remains inconsistent. BA3 can mark the old transfer `STALE` and localize a `DIAGNOSTIC_UNRESOLVED` condition.

Two projection purposes are tested:

```text
normal current-state method view
  qualificationPolicy = ACCEPTED + CURRENT

review/change view
  qualificationPolicy includes STALE / DIAGNOSTIC_UNRESOLVED
```

### Result

The review projection is valid only when the non-current/unresolved qualification remains visible in the consumed meaning.

The diagnostic is not promoted to project fact merely because it is accepted as a diagnostic.

### Smallest refinement

`qualificationPolicy` is explicit inside the projection coverage contract.

No duplicate BA3 lifecycle state machine is introduced.

## 9. Probe P6 - interpretation over stale basis

### Hypothesis attacked

A method-owned annotation may be presented as a current result even when one of its BA inputs is stale.

### Result

REJECTED for current shared interpretation.

A review-oriented method projection may still compute the local annotation to identify potentially affected analysis, but it must preserve that its basis is stale/unresolved.

No new universal projection status enum is forced; the projection descriptor and trace to BA3-qualified inputs are sufficient.

## 10. Probe P7 - cross-projection consistency

### Hypothesis attacked

Two projections over the same BA must have equivalent categories/items to be considered consistent.

### Result

REJECTED.

Consistency is checked against BA, not by pairwise method taxonomy equality.

For the same BA baseline:

```text
Projection F item
  basis = {consumeService, negative responsibility}
  interpretation = externally-provided-transport-exposure

Projection A item
  basis = {consumeService, negative responsibility}
  interpretation = delegated-assurance-dependency
```

Both are valid if each is allowed by its own immutable local interpretation rule and remains explicitly method-owned.

### Comparison rule

```text
cross-projection common denominator = BA trace
```

No first-class method-to-method equivalence identity is required.

## 11. Probe P8 - contradictory shared rendering

### Hypothesis attacked

Different projections can disagree about shared BA truth as long as their methods differ.

### Counterexample

BA contains negative project responsibility for underlying transport.

Projection F renders:

```text
project does not own/manage underlying transport
```

Projection A renders as shared truth:

```text
project owns underlying transport
```

### Result

Projection A fails semantic preservation. Method diversity does not excuse inversion of shared BA polarity.

No cross-projection contradiction proposition is needed; the failing projection can be diagnosed directly against its traced BA basis.

## 12. M1 replay - realization change

B0:

```text
realize(LocalConnectivity, WiredEthernet)
```

B1:

```text
realize(LocalConnectivity, WiFi)
```

Projection F ignores realization technology under its declared scope and can rebuild with the same flow meaning.

Projection A includes realization/assurance context and changes local output.

PASS: different projection deltas are expected because coverage differs.

## 13. M2 replay - responsibility change

When transport becomes project-owned:

- negative responsibility is replaced by affirmative responsibility;
- external service consumption may retire;
- Projection F's external-service exposure rule ceases to apply;
- Projection A can emit a different authority-placement item.

PASS: local categories evolve through rebuild from BA, not through BA mutation from the projections.

## 14. M3 replay - remote to local recognition

The remote transfer is retired by BA.

An exhaustive current-flow projection must omit the old exchange in B1 because it is no longer eligible current BA meaning.

A method view retaining the B0 flow merely because its local item existed fails rebuild semantics.

PASS: no cross-baseline projection item identity is required.

## 15. M4 replay - stale/unresolved representation

A current projection excludes stale capture transfer under its qualification policy.

A review projection may include:

```text
stale transfer
unresolved representation conflict
```

with explicit qualification.

REJECTED controls:

- silently rewrite transfer payload from sibling Decision;
- show stale transfer as current;
- use diagnostic as new governed project fact.

## 16. Order/WMS replay

Externalizing inventory authority toward a WMS produces different local effects:

```text
flow/integration projection
  new service/interchange focus

assurance/responsibility projection
  moved authority/contract dependency focus
```

Unrelated payment/fulfillment BA meaning is not invalidated merely because one projection changes strongly.

PASS: method deltas remain localized by BA trace and coverage.

## 17. Provider-normalization replay

A method that needs `PaymentAuthorizationResult` must consume the accepted BA normalized result.

The method may then derive a local branch or assurance category under its own interpretation rule.

REJECTED:

```text
raw provider state
  -> private method mapping
  -> projected value presented as shared governed result
```

PASS: BA3 remains the authority-preserving normalization layer.

## 18. Cross-baseline and cross-projection comparison

T2 tries to force a new shared identity for projection items across methods and baselines.

The requirement does not survive.

Same-baseline comparison uses role-bound BA trace. Cross-baseline comparison first resolves BA3 continuity, then rebuilds each projection against the target BA baseline.

Projection-local continuity may still be useful to a UI/tool, but current DDTA evidence does not require it as a Base Analysis projection semantic responsibility.

## 19. Attempts to force earlier reopen

### BA1

No method-local node/category requires new shared project-semantic identity with subtype-specific invariants.

`BA1 reopen = NOT TRIGGERED`.

### BA2

No method-owned category exposes missing methodology-neutral project meaning requiring a new operator/role.

`BA2 reopen = NOT TRIGGERED`.

### BA3

Source provenance, review/freshness and BA continuity remain sufficient to qualify projection input and rebuild after change.

`BA3 reopen = NOT TRIGGERED`.

## 20. T2 dispositions

```text
Two incompatible method taxonomies                       PASS
Shared projection ontology                               REJECTED
Method interpretation promoted into BA                   REJECTED
Descriptor + trace alone for multiple local rules        REJECTED
Interpretation rule reference                            REQUIRED
Role-bound BA trace                                      RETAINED
Selective/exhaustive coverage collapse                   REJECTED
Coverage mode                                            REQUIRED
Exhaustive omission -> project negation                  REJECTED
Exhaustive omission -> projection defect                 REQUIRED
Qualification policy                                     REQUIRED
Diagnostic/stale review projection                       PASS
Non-current BA presented as current shared truth         REJECTED
Cross-projection taxonomy equality                       NOT REQUIRED
Cross-projection comparison through BA trace             PASS
New shared projection identity                           NOT FORCED
Projection item BA-like lifecycle                        NOT FORCED
Universal projection DSL                                 REJECTED
New BAE family                                           NOT FORCED
New BA2 operator                                         NOT FORCED
BA1 / BA2 / BA3 reopen                                   NOT TRIGGERED
BA4-T1                                                   NOT REOPENED
BA4                                                      STARTED / NOT CLOSED
```

## 21. Provisional conclusion

BA4-T2 does not falsify the T1 projection boundary, but it does falsify two under-specified parts of the lower bound:

1. method-owned interpretation needs item-to-rule accountability when several local rules can use overlapping BA bases; and
2. coverage needs to distinguish selective views from views that promise exhaustive representation within an inspectable declared BA scope.

The accepted refinement remains projection-local and does not expand BA ontology.

## 22. Smallest remaining BA4 question

The next step should be an integrated closure review, not another method taxonomy exercise.

It must try to remove the T2 refinements, regress the combined T1/T2 contract across both corpora and determine whether BA4 can close for current thesis scope.

## 23. Next authorized microstep

Only after this T2 package is reviewed, committed, pushed and remotely verified:

> **BA4-T3 - projection boundary, interpretation/coverage and cross-projection closure review.**

Do not begin BA5 before BA4 is explicitly closed.
