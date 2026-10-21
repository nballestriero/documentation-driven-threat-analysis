---
type: MacroRequirement
schemaVersion: '0.1'
id: MR-BA-C5-VALID
title: 'Synthetic produce without governed input'
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
dependsOn: []
---

# MR-BA-C5-VALID — Synthetic produce without governed input

## Base Analysis

### BAReferent

| BAReferent | ID | Meaning |
|---|---|---|
| DDTADocumentAuthoring | BAR-EX-C5-ACTOR | Document authoring capability |
| DDTADocument | BAR-EX-C5-DOC | Document made available |

### BAProposition

```text
BAP-EX-MR-BA-C5-VALID-01 - produce
  actor    -> DDTADocumentAuthoring # BAR-EX-C5-ACTOR
  result   -> DDTADocument          # BAR-EX-C5-DOC
  polarity = affirmative
```
