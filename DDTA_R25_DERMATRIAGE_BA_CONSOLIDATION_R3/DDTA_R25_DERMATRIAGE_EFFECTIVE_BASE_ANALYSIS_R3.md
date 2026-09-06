# DermaTriage Effective Working Base Analysis — R3

The effective R3 working state is:

```text
R1
+
DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R2
+
DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R3.md
```

Earlier checkpoints remain historically immutable.

## Effective analyzed scope

1. MR-01
2. DEC-12
3. DEC-13
4. DEC-14
5. DEC-01
6. FR-01
7. DEC-02
8. FR-02
9. FR-16
10. FR-17

## Effective identity changes

```text
BAREF-DERMA-023 ImageBasedUrgencyClassificationCapability
    -> WORKING_ACCEPTED

BAREF-DERMA-037 Confidence
    -> WORKING_ACCEPTED
```

## Effective FR-16 additions

```text
BAPROP-DERMA-FR16-001 realize
BAPROP-DERMA-FR16-002 produce
BAPROP-DERMA-FR16-003 constrain
```

## Effective refinement of DEC12-001

Historical R1:

```text
EfficientNet-B4
    produces
ImageUrgencyClassification
```

Preferred effective R3 analytical shape:

```text
ImageBasedUrgencyClassificationCapability
    produces
ImageUrgencyClassification + Confidence

EfficientNet-B4
    realizes
ImageBasedUrgencyClassificationCapability
```

The historical R1 proposition is not deleted; R3 records a later application
refinement.

## FR-17

No duplicate production proposition is created.

FR-17 strengthens source support for:

```text
Qwen2-VL-7B-Instruct
    produces
ClinicalDescription
```

Its minimum structured content is not yet materialized under frozen BA2 and is
registered under P-07.

## Effective pressure set

```text
P-01 function/process/behavior identity binding      NARROWED
P-02 pipeline composition/order                      STRENGTHENED
P-03 interface/path association                      OPEN
P-04 boundary/interaction association                OPEN
P-05 ordered comparison vocabulary                   STRONG
P-06 direct scalar/property-addressing comparison    STRENGTHENED
P-07 structured data/information contract            OPEN_HOLDOUT_PRESSURE
```

## Next

`FR-18`
