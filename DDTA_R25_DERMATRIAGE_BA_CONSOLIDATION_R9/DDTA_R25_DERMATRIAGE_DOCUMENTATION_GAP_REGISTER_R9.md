# DermaTriage Documentation Gap / Assessment Register — R9

R9 preserves the distinction:

```text
documentation gap
    !=
methodology pressure
```

The governed DermaTriage source itself identifies three gaps material to DEC-06 / FR-09.

## Source-governed gap — GAP-DERMA-DEPLOY-01

```text
scope:
    FR-09 lifecycle

meaning:
    final authority and automaticity of deployment after qualification are unspecified

status:
    SOURCE_GOVERNED_DOCUMENTATION_GAP
    OPEN
```

BA must therefore not infer:

```text
qualified for adoption
    ->
automatic deployment

or

qualification
    ->
deployment authority assigned to DermaTriage
```

## Source-governed gap — GAP-DERMA-ACCEPT-BINDING-01

```text
scope:
    DEC-06 / DEC-07

meaning:
    complete quantitative binding of acceptance criteria is not specified,
    including reference/evaluation population and interpretation of the documented 5%.

status:
    SOURCE_GOVERNED_DOCUMENTATION_GAP
    OPEN

next material review:
    DEC-07
```

R9 does not pre-analyze DEC-07 criteria.

## Source-governed gap — GAP-DERMA-EVAL-CONSISTENCY-01

```text
scope:
    FR-09 / DEC-07

meaning:
    model report gives HIGH sensitivity 90.24%
    and HIGH recall 81.71% / 134 of 164 HIGH correct,
    without specifying whether they derive from different evaluation modes.

status:
    SOURCE_GOVERNED_DOCUMENTATION_GAP
    OPEN

next material review:
    DEC-07
```

Do not reconcile the metrics using external ML conventions.

## R9 no-gap decisions

The following remain non-gaps at this stage:

```text
FR-13/14/15 lack of a direct BA representation
    -> methodology pressure, source is explicit

lack of lifecycle states in FR-15 / DEC-06
    -> no transition inferred

path-relative evidence qualification
    -> not a missing classification
```
