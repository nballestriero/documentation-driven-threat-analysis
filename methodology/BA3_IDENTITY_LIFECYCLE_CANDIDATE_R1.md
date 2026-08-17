# DDTA BA3 cross-baseline identity/lifecycle candidate - R1

**Status:** PROVISIONAL CANDIDATE AFTER BA3-T2 / NOT CLOSED / BA3 OPEN

**Derived by:** BA3-T2 cross-baseline identity, staleness and lifecycle pressure test

**Repository baseline reviewed:** `52864d2ce177abdd694436306d8152db688effa0`

**Closed dependencies:** BA0 responsibility boundary; BA1 `BAReferent + BAProposition`; BA2 relation/action vocabulary; BA3-T1 provenance/origin lower bound.

## 1. Purpose

BA3-T2 asks what must remain stable, what must be revalidated and what must be replaced when governed documentation changes between baselines.

The pressure is mutation-driven. The candidate is not a generic version-control model and does not make Git history, document revision events or ThreatForge runtime state part of Base Analysis semantics.

The core result is that **baseline provenance, semantic identity continuity, review state and cross-baseline disposition are distinct concerns**.

## 2. Candidate cross-baseline lower bound

BA3-T1 already requires one provenance/origin attachment per materialized BA identity and baseline. BA3-T2 adds two representation-independent metadata contracts:

```text
BABaselineReview
|- targetElement          1     BAReferent | BAProposition
|- evaluatedBaselineKey   1
|- reviewState            1     PENDING_REVIEW | ACCEPTED | REJECTED
`- freshness              1     CURRENT | STALE

BACrossBaselineContinuity
|- priorElement           1     BAElementRef@priorBaseline
|- targetBaselineKey      1
|- disposition            1     RETAIN | REPLACE | RETIRE
|- successorElement       0..1  required for REPLACE
`- continuityBasis        1..*  GovernedSourceRef | BAElementRef
```

These are metadata contracts, not BAE identity families and not mandatory physical records/tables.

`SUPERSEDED` and `RETIRED` are lifecycle interpretations of an accepted continuity disposition:

```text
accepted REPLACE -> prior element is SUPERSEDED
accepted RETIRE  -> prior element is RETIRED
```

A retained element keeps the same semantic identity across the reviewed baselines. A newly introduced element has no predecessor continuity obligation.

## 3. Why the dimensions must remain separate

BA3-T1 already closed:

```text
originState = GROUNDED | DERIVED | DIAGNOSTIC_UNRESOLVED
```

That dimension answers **where/how meaning originated**.

BA3-T2 requires a separate review dimension because all of the following are valid:

```text
GROUNDED              + ACCEPTED
DERIVED               + ACCEPTED
DERIVED               + REJECTED
DIAGNOSTIC_UNRESOLVED + ACCEPTED
  [accepted as a diagnostic, not as project truth]
GROUNDED              + STALE       [relative to a newer baseline pending review]
```

Therefore:

```text
originState != reviewState != freshness/continuity disposition
```

Collapsing them would either treat a diagnostic as rejected merely because it is unresolved, or treat a grounded statement as current merely because it once came directly from a governed source.

## 4. `STALE` is target-baseline uncertainty, not historical invalidity

An accepted BA element from baseline `B0` does not become historically false merely because `B1` exists.

`STALE` means:

> the prior accepted meaning is potentially affected in the target baseline and MUST NOT be treated as current for that target baseline until revalidated.

Thus:

```text
valid for B0
    can coexist with
STALE relative to B1 review
```

After review, the target-baseline outcome is one of:

- `RETAIN` -> same identity is accepted/current in B1;
- `REPLACE` -> a successor identity is accepted/current and the old element is superseded;
- `RETIRE` -> no successor is required and the old element is retired;
- rejection of a proposed successor -> it does not enter the accepted B1 Base Analysis.

`STALE` is intentionally not a project-document lifecycle state. It is an analysis-layer revalidation state.

## 5. Cross-baseline identity rule for `BAReferent`

A `BAReferent` identity is retained when the same independently reusable methodology-neutral project meaning survives the governed change.

Changes in the following do **not by themselves** force a new referent identity:

- source wording;
- source locator;
- realization technology;
- ownership/responsibility relations;
- provider placement;
- propositions that classify, constrain or relate the referent.

A referent is replaced or retired when the independently reusable meaning itself changes or ceases to exist.

Candidate test:

> If consumers can still point to the same project-semantic thing across the two baselines while truthfully changing propositions about it, retain the referent identity. If the supposed continuity would make two materially different project meanings appear to be one thing, replace it.

## 6. Cross-baseline identity rule for `BAProposition`

`BAProposition` has a stricter continuity test because its identity is assertion identity.

A proposition may be retained only when its normalized assertion meaning remains equivalent across baselines. For the closed BA2 structure this requires materially equivalent:

```text
semanticOperatorKey
polarity
role-bound participants / controlled local values
condition / temporalScope modifiers
```

Participants are compared through accepted referent continuity, not lexical labels.

Changes only to provenance locators, source wording or display labels do not force proposition replacement if the assertion meaning is unchanged.

If a meaning-bearing operator, polarity, participant binding, governed constraint value or local modifier changes, the old proposition MUST NOT be silently edited under the same assertion identity. It is replaced/superseded or retired.

This prevents `BAProposition` from becoming a mutable document slot.

## 7. Source-document revision does not determine BA continuity

A governed document can be revised while some BA elements are retained and others are replaced.

Therefore the source-layer dispositions:

```text
retain / revise / replace / retire
```

MUST NOT be copied mechanically into BA identity disposition.

In particular, BA3-T2 does **not** require `REVISE` as a separate BA semantic-identity disposition. A source revision yields one of three BA outcomes after semantic review:

```text
same meaning survives      -> RETAIN
assertion/meaning replaced -> REPLACE
meaning disappears         -> RETIRE
```

Non-identity metadata/provenance may of course be refreshed on a retained identity.

## 8. Mutation M1 - Ethernet to Wi-Fi

The governed mutation changes only `D-3.5` from wired Ethernet to available Wi-Fi while transport remains externally consumed and camera/processor remain separated.

### 8.1 Referent continuity

```text
LocalConnectivity       RETAIN
CameraSubsystem         RETAIN
RecognitionProcessor    RETAIN
RecognitionCapture      RETAIN
WiredEthernet           RETIRE if no other governed use remains
WiFi                    INTRODUCE
```

The abstract connectivity meaning survives even though its realization changes.

### 8.2 Proposition continuity

```text
realize(LocalConnectivity, WiredEthernet)
    REPLACE
        -> realize(LocalConnectivity, WiFi)

transfer(CameraSubsystem,
         RecognitionProcessor,
         RecognitionCapture)
    RETAIN after review

assignResponsibility[negative](project,
                               transport,
                               ownership/management)
    RETAIN after review
```

The old realization proposition is therefore `SUPERSEDED`, not merely textually revised. The source `D-3.5` may be revised under the same document identity while BA assertion identity changes.

The transfer and security constraints remain current only **after review**; their survival is not inferred solely from unchanged files.

## 9. Mutation M2 - external transport to project-owned transport

`D-3.4` changes the responsibility boundary from consuming external transport to project ownership/management.

### 9.1 Meanings that can survive

```text
LocalConnectivity / LocalTransportCapability
  RETAIN if the abstract capability meaning is preserved
RecognitionCapture                              RETAIN
transfer delivery behavior                      RETAIN
confidentiality/integrity/provenance constraints RETAIN after review
```

### 9.2 Responsibility propositions

The negative responsibility assertion cannot remain the same proposition when polarity changes:

```text
assignResponsibility [negative]
  project -> transport -> ownership/management

    REPLACE

assignResponsibility [affirmative]
  project -> transport -> ownership/management
```

The prior proposition is `SUPERSEDED`.

The old external `consumeService` relation is normally `RETIRED` if the project no longer consumes that transport as an external service. A new project-owned transport FR branch may introduce new referents and propositions; this does not require rewriting the consumer's existing transfer/security semantics.

## 10. Mutation M3 - remote recognition to local recognition

`D-3.3` changes structurally from separate recognition processor to recognition on the camera.

### 10.1 Referent outcomes

```text
CameraSubsystem          RETAIN
RecognitionCapture       RETAIN if acquisition/evidence meaning remains
RecognitionProcessor     REVIEW; RETIRE if it has no remaining governed role
remote delivery behavior RETIRE
```

The same capture identity can survive even when the transfer relation disappears. This is direct evidence that referent and proposition lifecycle rules cannot be identical.

### 10.2 Proposition outcomes

The remote transfer assertion no longer has a true successor with the same project meaning:

```text
transfer(CameraSubsystem,
         RecognitionProcessor,
         RecognitionCapture)
    RETIRE
```

It is not rewritten into an unrelated local-processing assertion.

Constraints whose target is specifically the retired delivery behavior are also retired in their old form unless governed documentation explicitly establishes successor obligations. They MUST NOT be dragged automatically onto local recognition merely because the concern remains security-relevant.

A placement/responsibility proposition for `D-3.3` is replaced by the new local-placement proposition if a semantically corresponding successor is materialized.

`D-3.4`/`D-3.5`-derived BA elements become at least **STALE for review** where their relevance depended on the removed capture transfer. They are not automatically retired because other project uses may remain.

## 11. Order-fulfillment responsibility-boundary control

The order corpus chooses project-owned internal inventory authority and explicitly states that an external WMS would move many project-owned receipt/adjustment/availability/reservation/concurrency/release/issue obligations toward integration/contract semantics.

The counterfactual applies the same rules:

- stable project-semantic meanings such as `OrderEvaluation`, governed `ReservationResult` and externally visible reservation semantics may retain identity where the contract preserves them;
- internal `InventoryService`/`InventoryLedger` meanings and internal mutation propositions are retired or replaced if project responsibility disappears;
- external WMS/service/contract meanings and new `consumeService`/normalization propositions are introduced;
- source-level responsibility change does not force wholesale replacement of unrelated order/payment/fulfillment BA identities.

This cross-corpus control supports the family-specific continuity rules without introducing domain-specific lifecycle types.

## 12. Review state is required separately from origin state

BA3-T2 finds that `PENDING_REVIEW`, `ACCEPTED` and `REJECTED` are required analytical review states at the element/materialization boundary.

Why:

1. a prior accepted element may become stale relative to a new baseline before review;
2. a tool/analyst-derived candidate must not silently become accepted BA meaning;
3. an accepted diagnostic must remain distinguishable from a rejected derivation;
4. replacement candidates may be rejected without rewriting the historical predecessor.

A rejected proposal may be retained for audit/history, but it is not part of the accepted Base Analysis for that baseline.

This state is analysis-layer governance. It is not governed-document acceptance and does not make BA project authority.

## 13. Diagnostic resolution across baselines

A diagnostic with:

```text
originState = DIAGNOSTIC_UNRESOLVED
```

MUST NOT be retyped in place as `GROUNDED` merely because the source was later corrected.

If the governed correction removes the ambiguity/conflict/missing basis:

```text
old diagnostic -> RETIRE
```

If a materially different unresolved problem remains:

```text
old diagnostic -> REPLACE -> new diagnostic
```

Any new or retained grounded/derived project-semantic elements in the corrected baseline have their own origin/provenance and review state.

This preserves historical truth: the earlier diagnostic really existed and was unresolved in its baseline.

## 14. Minimal staleness triggers

BA3-T2 does not close a full change-impact algorithm, but mutation pressure forces a minimum rule for deciding what requires review in a target baseline.

A previously accepted BA element is at least a **staleness candidate** when:

1. one of its direct `sourceLink` targets changes or disappears;
2. one of its `derivationBasis` elements/sources becomes stale, replaced or retired;
3. one of a proposition's role-bound referents is replaced or retired;
4. a governed dependency/effective context known to justify the element changes materially.

Staleness may propagate transitively through derivation basis. It MUST NOT propagate to the entire Base Analysis merely because one document file changed.

The exact dependency closure, effective-governed-context representation and re-analysis scheduling remain later work.

## 15. Accepted provisional lifecycle semantics

```text
PENDING_REVIEW
  candidate or impacted carry-forward not yet accepted for target baseline

ACCEPTED
  accepted analytical materialization for the evaluated baseline

REJECTED
  reviewed candidate not admitted to accepted Base Analysis

STALE
  prior accepted meaning potentially impacted in target baseline
  and not yet revalidated

SUPERSEDED
  prior accepted element has an accepted REPLACE successor

RETIRED
  prior accepted element no longer applies and no successor identity is required
```

`SUPERSEDED` and `RETIRED` preserve history; neither deletes the old origin/provenance record.

## 16. Falsification rules

Revise this candidate if a concrete governed corpus demonstrates that:

1. `BAReferent` and `BAProposition` can use one identical identity-continuity rule without semantic distortion;
2. a proposition can change operator/polarity/role-bound meaning while honestly preserving assertion identity;
3. source-layer `revise` maps one-to-one to BA identity revision without ambiguity;
4. staleness can be inferred from origin state alone;
5. accepted/rejected review state can be removed without permitting silent candidate promotion;
6. a resolved diagnostic can safely mutate its historical origin from unresolved to grounded; or
7. a responsibility-boundary mutation forces a new BA1/BA2 semantic family rather than lifecycle/provenance handling.

No reviewed evidence currently forces such a revision.

## 17. Provisional dispositions

```text
Stable identity across baselines                       REQUIRED CAPABILITY
BAReferent continuity rule
  RETAIN WHEN REFERENT MEANING SURVIVES
BAProposition continuity rule
  STRICT SEMANTIC EQUIVALENCE REQUIRED
Source document revision == BA identity revision       REJECTED
BA continuity disposition                              RETAIN | REPLACE | RETIRE
BA-level REVISE as fourth identity disposition         NOT REQUIRED
PENDING_REVIEW / ACCEPTED / REJECTED                   REQUIRED
CURRENT / STALE distinction                            REQUIRED
REPLACE -> SUPERSEDED
  REQUIRED SEMANTIC INTERPRETATION
RETIRE -> RETIRED
  REQUIRED SEMANTIC INTERPRETATION
Resolved diagnostic mutates to GROUNDED                REJECTED
Historical provenance deletion on replacement          REJECTED
Third BAE lifecycle family                              NOT FORCED
BA1 reopen                                              NOT TRIGGERED
BA2 reopen                                              NOT TRIGGERED
BA3                                                     STARTED / NOT CLOSED
```

## 18. Remaining BA3 questions

The smallest unresolved set after T2 is:

1. exact method-neutral derivation-rule/rationale registry and reproducibility contract;
2. effective governed context and dependency representation sufficient for principled staleness/change-impact propagation;
3. source-to-analysis and analysis-to-source feedback lineage after a corrective governed change;
4. closure review over provenance + identity/lifecycle once those dependencies are pressure-tested.

The next microstep should attack derivation reproducibility and change-impact lineage without designing BA4 or analysis-method schemas.
