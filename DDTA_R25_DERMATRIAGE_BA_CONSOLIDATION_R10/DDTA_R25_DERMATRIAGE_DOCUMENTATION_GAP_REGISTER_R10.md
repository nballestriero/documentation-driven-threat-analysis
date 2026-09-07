# DermaTriage Documentation Gap / Assessment Register — R10

R10 preserves:

```text
documentation gap
    !=
methodology pressure
```

and also demonstrates that both may coexist on different semantic portions of the same
bounded source.

## Carried — GAP-DERMA-DEPLOY-01

```text
scope:
    FR-09 lifecycle

status:
    OPEN / CARRIED
```

Qualification still does not establish deployment automaticity or final deployment authority.

## Strengthened — GAP-DERMA-ACCEPT-BINDING-01

```text
scope:
    DEC-06 / DEC-07

status:
    OPEN
    FURTHER_STRENGTHENED_BY_DEC07
```

DEC-07 makes the gap materially relevant because qualification depends on:

```text
sensitivity non-degradation
false-low non-degradation
overall-accuracy degradation tolerance = 5%
```

while complete reference/evaluation population and exact interpretation of the 5% remain
insufficiently governed.

## Strengthened — GAP-DERMA-EVAL-CONSISTENCY-01

```text
scope:
    FR-09 / DEC-07

status:
    OPEN
    MATERIALLY_RELEVANT_TO_ACCEPTANCE
```

The source reports HIGH sensitivity 90.24% but also HIGH recall 81.71% / 134 of 164 HIGH
correct, without fully binding the relationship/evaluation mode. R10 does not reconcile these
through external ML conventions.

## Strongly exercised — GAP-DERMA-ROLLBACK-BINDING-01

```text
scope:
    DEC-08 / FR-10

status:
    OPEN
    STRONGLY_MATERIALLY_EXERCISED
```

Insufficiently governed dimensions include:

```text
unit
reference
population
observation window
timing
automaticity
authorization
exact rollback target
```

R10 therefore does not infer an automatic rollback rule, final rollback authority or a
canonical lifecycle transition.

What is documented and therefore not a gap:

```text
models/versions/
db/model_versions.json
models/efficientnet_b4.pth
```

The inability of current BA2 to encode their persistence/store relations is P-08 methodology
pressure, not a documentation gap.

## Strongly exercised — GAP-DERMA-PROMPT-WINDOW-01

```text
scope:
    DEC-09 / FR-06

status:
    OPEN
    STRONGLY_MATERIALLY_EXERCISED
```

Source-governed meaning:

```text
use/select the 20 most recent pertinent clinical corrections
for each prompt-evolution cycle
```

Insufficiently specified details include:

```text
exact ordering basis / tie behavior
deduplication
underfill
reuse / overlap across cycles
exact membership edge cases
```

The governed bounded-recency selection itself is explicit enough to create methodology
pressure `BOUNDED_RECENCY_SELECTION_SEMANTICS`; the edge cases above remain documentation
gaps.

## R10 distinction example

```text
SOURCE EXPLICIT:
    select the 20 most recent pertinent corrections

CURRENT BA CANNOT STRUCTURALLY PRESERVE TOP-N MEMBERSHIP:
    methodology pressure

SOURCE INCOMPLETE:
    deduplication / underfill / overlap / tie behavior

    documentation gap
```
