# DermaTriage Construct Test Ledger — R1

This ledger records **empirical exercise status**, not global validity.

`NOT_TESTED` means only that the analyzed DermaTriage scope has not yet provided a
suitable case.

| Construct | Current status | Evidence / note |
|---|---|---|
| `BAReferent` | TESTED_POSITIVE | Reusable participants, information, outputs, processes, paths and boundaries encountered. |
| `BAProposition` | TESTED_POSITIVE | Independent analytical assertions with source-grounded meaning. |
| `transfer` | TESTED_POSITIVE | DEC-14 B4 <-> DermaTriage content exchange. |
| `produce` | TESTED_POSITIVE | MR-01, DEC-12, DEC-13, DEC-14. |
| `create` | NOT_TESTED | Not forced merely because training produces a baseline. |
| `observe` | TESTED_POSITIVE_WORKING | DEC-12 historical-case retrieval/query; re-check at FR-18. |
| `transition` | NOT_TESTED | No analyzed element yet requires state/lifecycle transition. |
| `correlate` | TESTED_POSITIVE | DEC-12 outputs bound to same dermatological case. |
| `reference` | NOT_TESTED | No analyzed meaning yet requires reference-only semantics. |
| `dependOn` | TESTED_POSITIVE | DEC-13 operational capability requires trained/selected baseline. |
| `consumeService` | NOT_TESTED | DEC-14 data consumption is not enough to infer service consumption. |
| `realize` | NOT_TESTED | No abstraction introduced merely to exercise the operator. |
| `assignResponsibility` | TESTED_POSITIVE | MR-01 authority/ownership boundaries; DEC-14 B4 does not acquire triage responsibility. |
| `constrain` | TESTED_POSITIVE | MR-01 P1-P4 operational-priority vocabulary. |
| `classify` | NOT_TESTED | Domain urgency classification is not BA2 semantic-kind classification. |
| `decisionRule` | NOT_TESTED | P-scale and checkpoint selection not analyzed at sufficient source detail yet. |
| BA3 `sourceLink` | TESTED_POSITIVE | Working elements localize to governed source IDs. |
| BA3 derivation basis/rule | NOT_TESTED | No accepted derived BA element in this checkpoint. |
| BA3 revalidation context | NOT_TESTED | No baseline mutation analysis in this checkpoint. |
| BA4 projection boundary | NOT_TESTED_IN_MATERIALIZATION | Preserved as rule; no projection generated. |
| BA5 canonicalization | PARTIALLY_TESTED_PRESSURE | Working names/keys require later canonical reconciliation. |
| BA6 integrated completion | NOT_EXECUTED_FOR_DERMATRIAGE | Holdout BA is incomplete. |

## Evidence policy

A construct moves from `NOT_TESTED` only when a governed DermaTriage meaning gives a
real opportunity to apply it.

A construct is not marked redundant merely because another representation is possible.
Redundancy requires evidence that the competing representation preserves the same
governed distinction without loss and with lower semantic cost.

A construct is not marked missing merely because authoring feels awkward. A missing
construct requires repeated governed evidence that cannot be represented honestly
with the frozen BA contracts.
