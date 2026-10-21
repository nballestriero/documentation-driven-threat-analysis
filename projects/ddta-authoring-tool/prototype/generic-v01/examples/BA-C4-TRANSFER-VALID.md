---
type: MacroRequirement
schemaVersion: '0.1'
id: MR-BA-C4-VALID
title: 'Synthetic transfer acceptance case'
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
dependsOn: []
---

# MR-BA-C4-VALID — Synthetic transfer acceptance case

## Base Analysis

### BAReferent

| BAReferent | ID | Meaning |
|---|---|---|
| SystemA | BAR-EX-C4-A | Source |
| SystemB | BAR-EX-C4-B | Destination |
| DataX | BAR-EX-C4-X | Content |

### BAProposition

```text
BAP-EX-MR-BA-C4-VALID-01 - transfer
  source      -> SystemA  # BAR-EX-C4-A
  destination -> SystemB  # BAR-EX-C4-B
  content     -> DataX    # BAR-EX-C4-X
  polarity    = affirmative
```
