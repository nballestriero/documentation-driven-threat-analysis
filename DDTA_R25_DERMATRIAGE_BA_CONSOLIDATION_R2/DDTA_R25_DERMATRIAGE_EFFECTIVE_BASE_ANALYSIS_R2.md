# DermaTriage Effective Working Base Analysis — R2

The effective R2 BA is the versioned composition:

```text
DDTA_R25_DERMATRIAGE_BA_CONSOLIDATION_R1/DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_WORKING_SNAPSHOT_R1.md
+
DDTA_R25_DERMATRIAGE_BASE_ANALYSIS_DELTA_R2.md
```

## Effective analyzed scope

1. MR-01
2. DEC-12
3. DEC-13
4. DEC-14
5. DEC-01
6. FR-01
7. DEC-02
8. FR-02

## R2 additions

```text
BAREF-DERMA-034 SymptomOnlyTriageProcess
BAREF-DERMA-035 SymptomBasedUrgency
BAREF-DERMA-036 B4ChatbotInteractionFields
BAREF-DERMA-037 Confidence

BAPROP-DERMA-FR01-001 produce
BAPROP-DERMA-FR01-002 correlate
BAPROP-DERMA-FR01-003 produce
```

## Blocked semantic requirement

FR-02 requires a real `decisionRule`, but valid materialization is blocked by frozen
BA2 pressure P-05/P-06. This is part of the effective analytical state as a diagnostic,
not as accepted project-semantic truth.

## Effective pressure set

```text
P-01 function/process/behavior identity binding
P-02 pipeline composition/order
P-03 interface/path association
P-04 boundary/interaction association
P-05 ordered comparison vocabulary
P-06 direct scalar / property-addressing comparison
```

## Next

`FR-16`
