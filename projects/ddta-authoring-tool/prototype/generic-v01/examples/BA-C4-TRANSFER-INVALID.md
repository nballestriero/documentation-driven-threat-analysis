---
type: MacroRequirement
schemaVersion: '0.1'
id: MR-BA-C4-INVALID
title: 'Synthetic missing-polarity case'
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
dependsOn: []
---

# MR-BA-C4-INVALID — Synthetic missing-polarity case

## Base Analysis

### BAReferent

| BAReferent | ID | Meaning |
|---|---|---|
| SystemA | BAR-EX-C4-A | Source |
| SystemB | BAR-EX-C4-B | Destination |
| DataX | BAR-EX-C4-X | Content |

### BAProposition

```text
BAP-EX-MR-BA-C4-INVALID-01 - transfer
  source      -> SystemA  # BAR-EX-C4-A
  destination -> SystemB  # BAR-EX-C4-B
  content     -> DataX    # BAR-EX-C4-X
```
