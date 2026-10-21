---
type: MacroRequirement
schemaVersion: '0.1'
id: MR-BA-C5-MISSING-POLARITY
title: 'Synthetic produce missing shared polarity'
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
dependsOn: []
---

# MR-BA-C5-MISSING-POLARITY — Synthetic produce missing shared polarity

## Base Analysis

### BAReferent

| BAReferent | ID | Meaning |
|---|---|---|
| DDTADocumentAuthoring | BAR-EX-C5-ACTOR | Document authoring capability |
| DDTADocument | BAR-EX-C5-DOC | Document made available |

### BAProposition

```text
BAP-EX-MR-BA-C5-MISSING-POLARITY-01 - produce
  actor    -> DDTADocumentAuthoring # BAR-EX-C5-ACTOR
  result   -> DDTADocument          # BAR-EX-C5-DOC
```
