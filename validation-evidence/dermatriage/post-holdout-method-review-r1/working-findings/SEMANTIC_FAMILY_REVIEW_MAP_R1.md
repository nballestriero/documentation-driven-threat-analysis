# DDTA R25 — Semantic-Family Review Map R1

## Status

`EXECUTION MAP / NON-NORMATIVE`

This artifact maps existing constructs, pressures and candidate semantic slots into review families. It does not modify BA2.

## SF-01 Flow / consumption / service

```text
Existing: transfer, produce, observe, dependOn, consumeService, realize
Pressure: PR-03 invocation, PR-07 structured data, PR-08 store/persistence, PR-11 consumeData
Candidate: CC-02 provideService ?
Active: OP-09 consumeService
```

Stress shapes:

```text
Producer -> Data -> [Queue/Store/Topic] -> Consumer
Provider -> Service/Capability -> Consumer
Client -> Endpoint -> Service/Capability
```

## SF-02 Capability / realization / execution

```text
Existing: realize, produce, consumeService, dependOn
Pressure: PR-01 performs/executes, PR-03 invocation/exposure
Candidate: provideService ?
Active after SF-01: OP-10 realize
```

## SF-03 Responsibility / service provision / ownership

```text
Existing: assignResponsibility, consumeService.provider, realize
Pressure: PR-01 performer identity
Candidate: provideService ?
Active after SF-02: OP-11 assignResponsibility
```

## SF-04 Restriction / decision / condition

```text
Existing: constrain, decisionRule
CL: comparison, satisfies, allOf, anyOf, not
Pressure: PR-05, PR-06, PR-10, PR-12, PR-14
Active: OP-12 then OP-14 + CL audit
```

## SF-05 State / persistence / acquisition / applicability

```text
Anchors: transition, observe, transfer, produce
Pressure: PR-08, PR-09, PR-14
```

## SF-06 Pipeline / ordering / boundary

```text
Anchors: dependOn, transfer
Pressure: PR-02, PR-03, PR-04
```

## Cross-cutting overlays

```text
PR-07 structured information contracts
PR-13 bounded selection policies
```

These may be structured method mechanisms rather than top-level operators.

## Queue after existing constructs

```text
OP-09 consumeService
OP-10 realize
OP-11 assignResponsibility
OP-12 constrain
OP-14 decisionRule
CL-01..CL-05
then PR/CC disposition by family
```

## Admission rule

Characterization may occur early; admission may not.

```text
characterize adjacent pressure now
    !=
admit method delta now
```
