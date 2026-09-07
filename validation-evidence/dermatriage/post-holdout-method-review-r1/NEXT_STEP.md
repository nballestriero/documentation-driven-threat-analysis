# Next step

R14 checkpoint:

`DDTA-R25-DERMATRIAGE-CR01-CLASSIFY-CONSOLIDATION-R14`

Required repository HEAD before applying the R14 drop-in:

`81b94f5dd0fba9eaf6ba22f9b8c263158d62e55d`

After R14 is applied, verified, committed, and the resulting commit hash is recorded, begin:

```text
CR-02 — decisionRule + comparison condition language
```

## Preserved method freeze

The individual construct-review rule remains active:

```text
BA0 R1
BA1 R1
BA2 R3
BA3 R1
BA4 R1
BA5 R1

review evidence
    -> candidate clarification/delta
    -X-> immediate normative mutation
```

CR-01 does not modify BA2. Its primary verdict is `GUIDE_CLARIFICATION`.

## CR-02 operational rule

CR-02 must begin source-first and must not start from a verdict.

Before the aggregate verdict, show in chat:

1. the frozen `decisionRule` construct;
2. the frozen comparison/condition forms relevant to the case;
3. each material governed source excerpt;
4. the exact evidence-bearing wording in **bold**;
5. the current BA representation attempt;
6. whether the source requires:
   - decision logic,
   - a comparison condition,
   - a negative/non-sufficiency meaning,
   - a generic conditional action trigger,
   - or no `decisionRule` at all;
7. the source-to-construct semantic link.

Primary pressure basis:

```text
P-05
P-06
```

Do not use CR-01 macro-kind questions to create new project requirements. Their documentation-QA outcomes remain limited to:

```text
ANSWERED
CLARITY_OPPORTUNITY
GOVERNED_GAP
NOT_APPLICABLE
```
