# DDTA Base Analysis Question-Driven Discrimination Matrix R1

Status: CANDIDATE COMPANION / NON-NORMATIVE.

Purpose: quick companion to DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R4_CANDIDATE_R4. It does not replace BA2 R3 or the guide.

## Core sequence

1. Pin authority and isolate the smallest governed semantic fact.
2. Decide whether independent reusable identity is needed (BAReferent).
3. Decide whether a governed assertion between meanings is needed (BAProposition).
4. Test current operators before candidate constructs.
5. Use pairwise discriminators where semantics overlap.
6. If no current form preserves meaning honestly, record diagnosis/pressure.
7. Stop when added detail no longer preserves a material governed distinction.

## Quick discriminators

| Question | Try first | Exclude / distinguish |
|---|---|---|
| Result made available? | `produce` | `create`, `transfer` |
| New project-semantic identity/occurrence? | `create` | `produce`, `transition` |
| Existing meaning read/inspected? | `observe` | `transfer`, selection |
| Same identity changes state? | `transition` | property update, classification |
| Content conveyed source -> destination? | `transfer` | service consumption |
| Same request/case/evaluation binding? | `correlate` | `reference` |
| Directional target reference only? | `reference` | `correlate`, `dependOn` |
| Real prerequisite? | `dependOn` | temporal ordering |
| Actual service/capability use? | `consumeService` | endpoint presence, transfer |
| Concrete materializes abstract? | `realize` | execution/perform |
| Explicit responsibility/authority assignment? | `assignResponsibility` | actor/provider/consumer |
| Reusable restriction on a target? | `constrain` | local decision condition |
| Semantic kind assigned? | `classify` | state/value assignment |
| Conditions/inputs map to result? | `decisionRule` | conditional action |
| Subject satisfies abstract condition? | `satisfies` | invented property boolean |
| Subset/top-K/recent-N/best selection? | local `selection` | ranking/bound/retrieval |
| Pipeline membership/order? | OPEN local structure review | `dependOn`, `transfer` |
| Initiation/start only? | `initiate` CANDIDATE | success/completion/transfer |
| No current construct fits honestly? | diagnosis / pressure | local vocabulary invention |

## Mandatory stopping questions

- Does this added element preserve a governed distinction?
- Does it answer a material downstream question in declared scope?
- Can every populated role and condition be justified from governed source?
- Am I turning NOT SPECIFIED into a default?
- Am I encoding implementation knowledge as project meaning?
- Can two separate propositions preserve the meaning better than one overloaded proposition?
- If the answer adds no material semantics, STOP.
