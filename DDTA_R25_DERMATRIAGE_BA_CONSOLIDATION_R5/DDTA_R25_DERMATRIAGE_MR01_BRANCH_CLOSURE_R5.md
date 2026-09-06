# MR-01 Branch Closure — R5

This is an **evidence-collection closure**, not final BA acceptance.

## Completed analyzed branch

```text
MR-01 — Valutazione di triage del caso dermatologico

DEC-12 — image-based pipeline
    FR-16
    FR-17
    FR-18
    FR-19

DEC-13 — baseline training
    FR-20

DEC-14 — service exposure and B4 integration
    FR-21
    FR-22

DEC-01 — no-image continuity
    FR-01

DEC-02 — P-scale
    FR-02
```

## What MR-01 taught the holdout

### Strongly useful current constructs

```text
BAReferent
BAProposition
transfer
produce
observe
correlate
dependOn
consumeService
realize
assignResponsibility
constrain
scopedModifier.condition
```

### Necessary but currently blocked / incomplete

```text
decisionRule
    ordered comparison greaterThan missing

direct scalar/property-addressing comparison
    P-06
```

### Current method pressures

```text
P-01 process/behavior identity binding
P-02 pipeline composition/order
P-03 endpoint -> invoked behavior binding
P-04 transfer -> boundary binding
P-05 ordered comparison vocabulary
P-06 direct scalar comparison
P-07 structured data contract
P-08 data artifact/store association
```

### Untested constructs are not rejected

```text
create
transition
classify
comparison.notEquals
anyOf
not
other ordered comparators
BA3 derivation machinery
BA4 actual projection materialization
```

## Documentation-improvement lesson

The MR-01 branch repeatedly demonstrates that DDTA can expose missing project meaning
without filling it in.

The strongest cross-cutting candidate is O-03 Data Interaction Completeness:

```text
WHAT data?
FROM WHERE?
TO WHERE?
WHO reads/writes/produces?
HOW?
WHICH path/interface?
WHICH boundary/medium?
WHICH data contract?
```

The next source element must not trigger methodology change merely because the MR-01
branch is now closed.

## Next

```text
MR-02 — Indirizzamento specialistico
```
