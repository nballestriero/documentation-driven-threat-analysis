# DermaTriage Construct Test Ledger — R8

| Construct | Status |
|---|---|
| BAReferent | TESTED_POSITIVE_STRONG |
| BAProposition | TESTED_POSITIVE_STRONG |
| transfer | TESTED_POSITIVE_STRONG |
| produce | TESTED_POSITIVE_STRONG |
| create | NOT_TESTED_POSITIVE |
| observe | TESTED_POSITIVE_STRONG |
| transition | NOT_TESTED_POSITIVE |
| correlate | TESTED_POSITIVE_STRONG |
| reference | NOT_TESTED_POSITIVE |
| dependOn | TESTED_POSITIVE_STRONG |
| consumeService | TESTED_POSITIVE_STRONG; rejected for evidence consumption |
| realize | TESTED_POSITIVE_STRONG |
| assignResponsibility | TESTED_POSITIVE_STRONG |
| constrain | TESTED_POSITIVE_STRONG |
| classify | NOT_TESTED_POSITIVE |
| decisionRule | TESTED_NECESSARY_BUT_BLOCKED / not generalized to conditional action |
| ordered comparisons | STRONG_REPEATED_PRESSURE |
| persistence/store association | POSSIBLE_MISSING_RELATION_STRONG |
| conditional action trigger | REPEATED_UNNUMBERED_COUNTEREXAMPLE |
| data/evidence consumption | UNNUMBERED_COUNTEREXAMPLE |
| acquisition/refresh action | UNNUMBERED_COUNTEREXAMPLE / carried |
| BA6 DermaTriage | NOT_EXECUTED |

Negative controls:

```text
activate != transition
activate != create
threshold value != complete trigger rule
evidence consumption != consumeService
cross-branch consumption != hierarchy ownership
```
