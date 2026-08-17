# DDTA BA3-T2 cross-baseline identity, staleness and lifecycle pressure test - R1

**Status:** COMPLETED / PROVISIONAL PASS WITH IDENTITY-LIFECYCLE REFINEMENT

**Repository baseline reviewed:** `52864d2ce177abdd694436306d8152db688effa0`

**Executed microstep:** `BA3-T2 - cross-baseline identity, staleness and lifecycle pressure test`

**Scope discipline:** this test does not close BA3, does not redesign BA2, does not define BA4 projections, AnalysisRecord/Common Finding, STRIDE overlays or ThreatForge implementation state.

## 1. Question under test

BA3-T1 proved that every BA identity needs baseline-scoped origin/provenance. T2 asks what happens when the governed baseline changes:

> Which BA meanings remain the same identities, which must be reviewed, which are replaced, and which disappear?

The test deliberately uses concrete governed mutations instead of inventing a generic lifecycle state machine.

## 2. Candidate attacked

T1 left these questions open:

- cross-baseline identity/equivalence;
- accepted/rejected/stale/superseded/retired semantics;
- diagnostic resolution after source correction.

The pressure hypothesis was intentionally minimal:

```text
H1 same source ID -> same BA identity
H2 one lifecycle rule can serve BAReferent and BAProposition
H3 source revise can be copied as BA revise
H4 originState can carry acceptance/freshness meaning
```

All four hypotheses were attacked by the mutation corpus.

## 3. Test A - M1 Ethernet to Wi-Fi

### 3.1 Governed mutation

The facial-access corpus changes only `D-3.5`:

```text
Ethernet available -> Wi-Fi available
```

Transport remains externally consumed; camera and recognition processor remain separated; FR-3.4 and its specialized constraints survive after review.

### 3.2 Identity pressure

The abstract `LocalConnectivity` meaning survives. The concrete realization does not.

If same document identity implied same BA proposition identity, the assertion:

```text
realize(LocalConnectivity, WiredEthernet)
```

would have to mutate in place into:

```text
realize(LocalConnectivity, WiFi)
```

That would make proposition identity denote two different normalized assertions over history.

### 3.3 Result

```text
LocalConnectivity referent                         RETAIN
WiredEthernet referent                            RETIRE if unused elsewhere
WiFi referent                                     INTRODUCE
old realize proposition                           REPLACE / SUPERSEDED
transfer/correlation/security propositions        RETAIN after review
same D-3.5 source identity -> same BA proposition REJECTED
```

**Finding A:** source-document continuity and BA assertion continuity are independent decisions.

## 4. Test B - M2 external to project-owned transport

### 4.1 Governed mutation

`D-3.4` changes from consumed external transport to project ownership/management.

### 4.2 Polarity pressure

BA2 represents the V0 boundary as a negative responsibility assertion. Project ownership changes that truth value.

Keeping one proposition identity while flipping polarity would violate assertion identity:

```text
assignResponsibility[negative](project, transport, ownership/management)
```

becomes:

```text
assignResponsibility[affirmative](project, transport, ownership/management)
```

### 4.3 Result

```text
abstract transport/connectivity referent          RETAIN if meaning survives
negative responsibility proposition               REPLACE / SUPERSEDED
affirmative responsibility proposition            INTRODUCE as successor
external consumeService proposition               RETIRE if consumption ceases
transfer + specialized constraints                RETAIN after review
new project-owned transport branch                INTRODUCE as needed
```

**Finding B:** changing responsibility relations does not automatically split the referent whose responsibility changed.

## 5. Test C - M3 remote to local recognition

### 5.1 Governed mutation

Recognition moves onto the camera. The remote RecognitionCapture transfer disappears.

### 5.2 Retire versus replace pressure

A bad lifecycle rule would transform the old transfer proposition into any new local processing behavior merely because both concern recognition.

That would destroy the proposition's identity semantics.

### 5.3 Result

```text
CameraSubsystem referent                           RETAIN
RecognitionCapture referent
  RETAIN if acquisition meaning survives
RecognitionProcessor                               REVIEW / possibly RETIRE
remote delivery behavior referent                  RETIRE
remote transfer proposition                        RETIRE
old delivery-targeted constraints
  RETIRE old form unless successor authored
D-3.3 placement proposition
  REPLACE when successor meaning is materialized
D-3.4/D-3.5 related elements
  STALE FOR REVIEW where relevance was transfer-dependent
```

**Finding C:** no successor is required merely because a neighboring function remains. `RETIRE` and `REPLACE` are materially different.

## 6. Test D - order-fulfillment internal versus external WMS

The order corpus states that `ADR-2.1` internal inventory authority is a genuine responsibility-boundary choice: an external WMS would replace many project-owned inventory FRs with integration/API/contract obligations.

This provides an independent domain control.

Expected BA effect:

- stable order/evaluation and governed result meanings may retain identity;
- internal inventory authority/capability/store meanings may retire or be replaced;
- internal mutation propositions retire/supersede;
- external service/contract referents and consumption/normalization propositions are introduced;
- payment and fulfillment meanings outside the affected boundary do not become stale merely because MR-2 changed.

**Finding D:** mutation-local lifecycle handling generalizes beyond the camera corpus without requiring a domain taxonomy.

## 7. Family-specific identity tests

### 7.1 BAReferent test

Retain identity when the independently reusable project-semantic thing remains the same despite changed propositions around it.

Mutation examples forcing retention:

- `LocalConnectivity` across Ethernet/Wi-Fi;
- `RecognitionCapture` across remote/local recognition when capture itself remains required;
- order-evaluation/result semantics across provider-boundary changes where governed meaning is preserved.

### 7.2 BAProposition test

Retain identity only under normalized assertion equivalence.

A proposition identity therefore cannot survive a material change in:

- operator;
- polarity;
- role-bound participant identity/value;
- governed constraint value;
- local condition/temporal scope.

Source wording and provenance may change without forcing replacement.

**Result:** one shared retention rule for both BA1 families is rejected.

## 8. Review-state pressure

Origin state alone cannot encode review state.

Examples:

```text
DERIVED + ACCEPTED
DERIVED + REJECTED
DIAGNOSTIC_UNRESOLVED + ACCEPTED
GROUNDED + STALE relative to new baseline
```

Therefore `PENDING_REVIEW | ACCEPTED | REJECTED` is required as a separate analytical review dimension.

This does not give BA project authority. It records whether analytical materialization is admitted to the accepted Base Analysis.

## 9. Staleness pressure

A new governed baseline does not invalidate all old BA meaning.

The minimum staleness rule is dependency-local:

```text
changed source locator
  -> directly grounded dependent BA elements need review

stale/replaced/retired derivation basis
  -> derived dependents need review

replaced/retired proposition participant
  -> proposition needs review
```

M3 also shows that effective context can matter even where the direct source file of an element did not change.

Therefore exact change-impact closure remains open, but `STALE` is required as a target-baseline revalidation state.

## 10. Supersession versus retirement

The mutation corpus forces both:

### SUPERSEDED

A successor exists and takes over the earlier semantic responsibility.

Examples:

- Ethernet realization proposition -> Wi-Fi realization proposition;
- negative ownership proposition -> affirmative ownership proposition;
- remote placement proposition -> local placement proposition.

### RETIRED

The old meaning ceases and no successor identity is required.

Examples:

- remote capture-transfer proposition after local recognition;
- delivery-behavior referent if no longer used;
- external service-consumption proposition after project ownership, if no external consumption remains.

Collapsing both into `inactive` would lose change explanation and targeted downstream invalidation.

## 11. Diagnostic resolution test

Suppose baseline B0 contains an accepted `DIAGNOSTIC_UNRESOLVED` element because sources conflict or are insufficient. B1 corrects the governed documentation.

Rejected behavior:

```text
same diagnostic identity
originState: DIAGNOSTIC_UNRESOLVED -> GROUNDED
```

That rewrites history.

Accepted provisional behavior:

```text
issue disappears       -> diagnostic RETIRE
new unresolved issue   -> diagnostic REPLACE / SUPERSEDE
new factual meaning    -> separate GROUNDED/DERIVED BA element
                         with own provenance
```

Thus origin remains historical while lifecycle expresses resolution.

## 12. Why BA-level `REVISE` is not required

The source corpus itself uses review labels such as `revise`, `revise/replace` and `retire/supersede` for governed documents.

Those labels are not a BA identity ontology.

At BA semantic identity level:

- non-identity metadata/provenance refresh with same meaning -> `RETAIN`;
- changed meaning with successor -> `REPLACE`;
- disappeared meaning -> `RETIRE`.

Adding `REVISE` would blur the exact boundary T2 is trying to protect: whether semantic identity survived.

## 13. Minimum candidate after pressure

```text
Origin/provenance dimension:
  GROUNDED | DERIVED | DIAGNOSTIC_UNRESOLVED

Review dimension:
  PENDING_REVIEW | ACCEPTED | REJECTED

Freshness dimension:
  CURRENT | STALE

Cross-baseline continuity disposition:
  RETAIN | REPLACE | RETIRE

Derived historical interpretation:
  accepted REPLACE -> SUPERSEDED
  accepted RETIRE  -> RETIRED
```

No new BAE family is forced.

## 14. Negative controls

- Do not make Git commit ancestry the semantic identity rule.
- Do not use document IDs as BA proposition identity.
- Do not preserve proposition identity solely because source wording is similar.
- Do not replace a referent merely because ownership/provider/realization changed.
- Do not auto-transfer retired security constraints to a new behavior.
- Do not mark the whole BA stale because one source file changed.
- Do not treat `REJECTED` analytical material as governed project truth.
- Do not mutate a resolved diagnostic into a grounded fact.

## 15. BA1 / BA2 reopen check

No mutation requires a third identity family or a new operator/role/modifier semantic.

The pressure is absorbed by:

- BA1 identities;
- BA2 proposition structure;
- BA3 provenance + continuity/lifecycle metadata.

```text
BA1 reopen trigger: false
BA2 reopen trigger: false
```

## 16. Exit disposition

```text
BA3-T2              COMPLETED / PROVISIONAL PASS
                    WITH IDENTITY-LIFECYCLE REFINEMENT
BA3                 STARTED / NOT CLOSED
BA1                 REMAINS CLOSED
BA2                 REMAINS CLOSED
```

The remaining BA3 work is narrower: derivation-rule reproducibility, effective dependency/change-impact lineage and feedback provenance, followed by closure review.

## 17. Next falsification target

Only after this package is committed, pushed and remotely verified:

> **BA3-T3 - derivation-rule reproducibility and change-impact lineage pressure test.**

T3 should use the facial M4 effective-governed-context pressure plus provider-state normalization/order boundary cases. It must not start BA4 or method-specific analysis schemas.
