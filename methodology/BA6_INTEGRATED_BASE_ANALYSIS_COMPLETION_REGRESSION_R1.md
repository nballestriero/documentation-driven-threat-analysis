# DDTA BA6 integrated Base Analysis completion and regression contract - R1

**Status:** CLOSED FOR CURRENT R24 THESIS SCOPE / ACTIVATES WITH ACCEPTED BA6 CLOSURE PACKAGE
**Prepared against research baseline:** `8af2257a1df94fa5a83d4853ed0a1eb4d020c429`
**Dependencies:** BA0 R1; BA1 R1; current accepted BA2 revision; BA3 R1; BA4 R1; BA5 R1.
**Validation corpus:** `FACIAL-ACCESS-GOV-R2`.
**Validation BA baseline:** `FACIAL-ACCESS-BA-R24-R1`.
**Authority note:** BA6 accepts an analytical baseline; it does not make Base Analysis project authority.

## 1. Purpose

BA6 closes the integration question left open by BA0-BA5:

> when may one concrete Base Analysis materialization be treated as an accepted shared analytical baseline for downstream DDTA consumers?

BA6 does not add a new project ontology, operator vocabulary, provenance model, projection language or authoring registry.

Instead it integrates the already closed responsibilities:

```text
BA0
    authority / minimality / unresolved-state responsibility

BA1
    BAReferent + BAProposition identity

BA2
    relation/action/proposition semantics

BA3
    provenance / derivation / review / continuity / revalidation

BA4
    projection / interpretation / coverage boundary

BA5
    canonical semantic registry / controlled authoring

BA6
    baseline-level completion + regression + downstream-readiness gate
```

## 2. BA6 completion is baseline-scoped

BA6 never declares Base Analysis universally complete.

It accepts one analytical baseline relative to:

```text
one governed project baseline
+ one pinned source revision
+ one BA contract revision set
+ one declared shared-analysis scope
```

A future governed counterexample may reopen the smallest affected BA contract.

A future source-baseline change triggers BA3 revalidation and normally a new BA baseline materialization.

## 3. Accepted BA baseline descriptor

The minimum BA6 acceptance envelope is:

```text
AcceptedBABaselineDescriptor              [methodology metadata; NOT BAE]
|- baBaselineKey                     1 immutable
|- governedBaselineKey               1
|- sourceRepositoryRevision          1 immutable
|- baContractRevisionSet             1
|- acceptedBAArtifactRef             1
|- declaredSharedScope               1
|- regressionEvidenceRef             1..*
|- unresolvedDiagnosticRef           0..*
`- reopenRule                         1
```

This descriptor is not project documentation and not a new BA1 identity family.

`baBaselineKey` supplies the stable analytical baseline identity required by BA4 projection materializations.

## 4. Completion Gate G1 — authority

Before BA acceptance:

```text
governed project baseline
    MUST be explicit

source revision
    MUST be pinned

primary BA source eligibility
    MUST be satisfied

superseded / candidate / diagnostic-only sources
    MUST NOT silently become project authority
```

Failure of G1 blocks BA6 acceptance.

## 5. Completion Gate G2 — identity/proposition coherence

The materialized BA must obey the active BA1/BA2 contracts.

At minimum:

- independently reusable project meaning receives `BAReferent` identity;
- independently reviewable analytical assertions receive `BAProposition` identity;
- BAProposition identity is not used as a proxy for project-semantic behavior identity;
- operator/role/cardinality rules resolve under the active BA2 revision;
- no local convenience creates an unregistered operator, role or semantic family.

A material representation failure reopens the smallest forced contract before BA6 may pass.

## 6. Completion Gate G3 — provenance and source drill-down

Every accepted meaning-bearing BA element must resolve to BA3 provenance sufficient to recover:

```text
governed baseline
+ source document
+ baseline-relative semantic locator
+ origin state
```

For `DERIVED` elements, BA3 derivation basis/rule requirements also apply.

A BA may normalize prose into canonical semantics while remaining `GROUNDED`.

A provenance attachment does not replace BA2 semantics.

## 7. Completion Gate G4 — explicit uncertainty and diagnostics

BA6 acceptance requires that material uncertainty be visible rather than guessed away.

Allowed current interpretations include:

```text
DIAGNOSTIC_UNRESOLVED
MULTIPLE MATERIAL BA CANDIDATES
BA REQUIRES UNSUPPORTED FACT
BA LOSES GOVERNED MATERIAL DISTINCTION
BA EXPOSES SOURCE CONFLICT
NOT SPECIFIED
```

A diagnostic may be accepted as analytical diagnostic without becoming project truth.

A non-blocking `NOT SPECIFIED` meaning does not prevent BA6 acceptance when the declared shared scope can still be represented honestly.

## 8. Completion Gate G5 — declared-scope semantic coverage

BA6 does not require byte-for-byte or sentence-for-sentence transcription.

For each material governed meaning within `declaredSharedScope`, one of these dispositions must be inspectable:

```text
REPRESENTED
    -> accepted BA meaning preserves it

PRESERVED_UNDER_SPECIFIED
    -> source intentionally does not govern enough detail;
       BA does not invent it

DIAGNOSTIC_UNRESOLVED
    -> a material ambiguity/conflict/missing basis is explicit

OUTSIDE_DECLARED_SHARED_SCOPE
    -> not required by the accepted shared BA scope
```

An unacknowledged material omission fails BA6.

## 9. Completion Gate G6 — post-BA regression

The complete BA must be regressed against the pinned governed source after any material BA contract reopen.

The regression checks at least:

```text
ONE BA / ONE STABLE MEANING

no unsupported project fact

no lost governed material distinction

no authority inversion

no accidental semantic strengthening

no incorrect propagation of local properties

explicit under-specification preserved
```

A regression failure returns to the smallest relevant source/BA review step.

## 10. Completion Gate G7 — projection readiness

At least one controlled BA4-compatible downstream check must demonstrate that the accepted BA can be consumed without reparsing project prose.

The check must show both:

1. one useful governed distinction can be recovered from BA; and
2. the consumer cannot legitimately infer a stronger project fact than BA/source support.

This is a readiness check, not a full threat-method evaluation.

## 11. Completion Gate G8 — no unresolved contract pressure

BA6 may pass only when there is no known material counterexample that requires reopening BA0-BA5 for the declared baseline/scope.

This does not mean future corpora cannot reopen them.

The rule is:

```text
no current counterexample
    -> accept current contract set

future concrete counterexample
    -> reopen smallest affected contract
```

## 12. Completion Gate G9 — immutable baseline and change path

An accepted BA baseline is retained as historical analytical evidence.

A material future change uses BA3:

```text
governed source changes
    -> identify potentially impacted BA meaning
    -> revalidate
    -> RETAIN / REPLACE / RETIRE as applicable
    -> materialize next accepted BA baseline
    -> rebuild projections
```

Do not silently mutate an accepted historical baseline and pretend the prior analysis used the new semantics.

## 13. Relationship to BA4 coverage

BA6 `declaredSharedScope` and BA4 projection `eligibleBAScope` are different.

```text
BA6 declaredSharedScope
    -> what shared project meaning the accepted BA claims to cover

BA4 eligibleBAScope
    -> what subset of accepted BA meaning one projection considers relevant
```

A selective projection may intentionally omit accepted BA meaning.

That omission does not reduce BA6 acceptance.

## 14. Relationship to BA5

BA5 remains the lexical/controlled-authoring boundary.

When BA2 is legitimately reopened:

```text
new BA2 operator / role / local structured form
    -> canonical tokens are governed by that BA2 revision
    -> BA5 does not need reopening merely to duplicate the new list
```

BA6 verifies only that the active registries resolve the operative BA2 semantics unambiguously.

For the current R24 baseline this includes:

```text
decisionRule
transfer/behavior
decisionRule/satisfies
```

without introducing aliases.

## 15. Facial Access controlled usefulness test

The validation BA contains:

```text
RecognitionCaptureDelivery.interconnectionMedium = WIRED_ETHERNET
```

A selective downstream consumer may conclude:

```text
a threat whose necessary precondition is
"this governed delivery uses an RF/wireless medium"
    -> not applicable to this governed interaction
```

The consumer may **not** conclude:

```text
the consumed provider infrastructure
is wired end-to-end
```

because D-3.5 / D-3.6 do not govern hidden provider topology.

This test demonstrates both usefulness and BA4 authority restraint.

## 16. Facial Access BA6 result

The current validation cycle establishes:

```text
project authority
    FACIAL-ACCESS-GOV-R2

source revision
    8af2257a1df94fa5a83d4853ed0a1eb4d020c429

BA baseline
    FACIAL-ACCESS-BA-R24-R1

BA1
    PASS

BA2 R3
    PASS

BA3
    PASS

BA4 projection-readiness
    PASS

BA5 controlled authoring
    PASS

post-BA regression
    PASS

new project semantic gap
    NONE

known unresolved BA contract pressure
    NONE

AUTH-C / AUTH-P
    NOT SPECIFIED / NON-BLOCKING

acquisition operator
    intentionally not selected
```

## 17. BA6 closure disposition

```text
BA6
    CLOSED FOR CURRENT R24 THESIS SCOPE

accepted BA baseline
    FACIAL-ACCESS-BA-R24-R1

universal BA completeness
    NOT CLAIMED

reopen trigger
    concrete governed counterexample
    or source change requiring BA3 revalidation

next methodology step
    revise human-readable Documentation/BA Authoring Guide
    revise Base Analysis Operational Guide
    align forward research checkpoint
```

BA6 completion makes the accepted BA suitable as the shared input to later human-readable projections and threat-method studies. It does not itself perform STRIDE / STRIDE-AI.
