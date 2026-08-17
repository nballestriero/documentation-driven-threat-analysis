# DDTA current research state - R17

**Prepared against repository baseline:** `aa4b785dc72c2fbcd20fd04976e77fca3d07bf25`

**Purpose:** active semantic-state pointer after BA5-T1 canonical referent naming and controlled-authoring pressure testing; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0 responsibility/non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- BA2 relation/action vocabulary: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA3 provenance/derivation/identity/lifecycle/change-revalidation: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA4 projections: **CLOSED FOR CURRENT THESIS SCOPE BY BA4-T3**.
- BA5-T1 canonical referent naming/controlled authoring: **COMPLETED / PROVISIONAL PASS WITH CANONICAL-REFERENT-NAMING LOWER-BOUND**.
- BA5 canonical semantic registry/controlled authoring: **STARTED / NOT CLOSED**.
- BA6 complete Base Analysis regression/closure: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## BA5 hypothesis after T1

DDTA begins from a strict controlled-authoring assumption rather than a synonym-normalization assumption.

For a named shared project referent in one governed baseline/naming scope:

```text
one shared referent
  -> one exact canonicalName

all governed semantic references
  -> exact canonicalName

accepted BA/shared projection rendering
  -> exact canonicalName

alias/synonym as normative identifier
  -> rejected
```

Example:

```text
cameraIngresso
```

is not silently interchangeable with `entryCamera`, `cameraEntrata`, `CameraIngresso` or another lexical variant.

## Name is not identity

BA5-T1 explicitly rejects using the canonical name as the `BAReferent` identity key.

```text
BAReferent identity != canonicalName
```

The name is baseline-scoped governed lexical metadata.

A governed rename may therefore produce:

```text
B0 cameraIngresso
B1 cameraNord
```

while BA3 RETAIN preserves the same referent identity if the independently reusable project meaning is materially unchanged.

Historical B0 documentation/BA/projections retain the old name; B1 uses the new canonical name consistently.

## Registry responsibility

BA5-T1 requires a governed canonical-name registry responsibility with at least:

```text
governedBaselineKey
namingScopeKey
canonicalName
unambiguous governed referent binding
```

The physical realization is not closed.

The registry is not a BAE family and does not make BA or ThreatForge project authority.

## Projection naming rule

Projection-local types and method interpretation labels remain allowed.

```text
FlowParticipant(cameraIngresso)
AssuranceSubject(cameraIngresso)
```

is valid because the method-owned type differs while the shared entity name remains exact.

If a projection item is genuinely method-owned rather than a shared referent, it may have a local method label provided BA4 trace/interpretation boundaries remain explicit.

## Tool boundary

A tool may validate, complete and reject unregistered tokens.

It may propose a correction or candidate registry extension.

It may not silently normalize aliases or mint accepted semantic names without governance.

## T1 dispositions

```text
exact canonical referent naming                          REQUIRED
same referent same name across governed docs            REQUIRED
same referent same name across shared projections       REQUIRED
alias/synonym as normative entity identifier            REJECTED
canonical name uniqueness within baseline/scope         REQUIRED
canonicalName == semantic identity                      REJECTED
governed rename + BA3 RETAIN                            PASS
method local type/category labels                       ALLOWED
tool exact validation/completion                        ALLOWED
tool autonomous synonym normalization                   REJECTED IN CORE
new BAE family                                          NOT FORCED
new BA2 operator                                        NOT FORCED
BA1 / BA2 / BA3 / BA4 reopen                           NOT TRIGGERED
BA5                                                     STARTED / NOT CLOSED
```

## Smallest unresolved set

BA5 next needs to test whether the controlled-registry rule can cover the rest of the operative semantic vocabulary:

1. BA2 operator keys;
2. operator-scoped role keys;
3. semantic-kind keys such as `store` and `contract`;
4. controlled local values;
5. governance for adding a genuinely new canonical term; and
6. tool validation/completion without semantic-authority leakage.

Synonym machinery remains deferred unless a concrete integration failure forces it.

## Next authorized microstep

Only after the BA5-T1 package is reviewed, committed, pushed and remotely verified, execute:

> **BA5-T2 - canonical semantic registry coverage and governed-extension pressure test.**

Do not start BA6 or downstream analysis schemas before BA5 is explicitly closed.
