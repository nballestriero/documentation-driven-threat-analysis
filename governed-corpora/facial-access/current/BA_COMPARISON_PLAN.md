# Next experiment — old documentation vs current documentation in Base Analysis

**Status:** `DEFERRED` until the document-authority/current-corpus package is committed and its Git baseline is pinned.

No BA is materialized here.

## Experimental question

Does the documentation structure closed in Chapter 4 make the methodology-neutral Base Analysis of Chapter 5 more deterministic, less ambiguous and more change-stable than the historical facial-access documentation?

## Two source sets

### A — historical/regression only

Use the historical MR/Decision/S1 facial-access material strictly with `primaryBASourceAllowed: false`.

### B — current governed

Use `FACIAL-ACCESS-GOV-R1` at the concrete Git commit that contains it.

## Comparison dimensions

For the same semantic scope record at least:

1. canonical-name proposals required;
2. unresolved placeholders;
3. cross-scope unresolved references;
4. normative constraints hidden in narrative prose;
5. constraints already isolated as Specialized/Security Requirements;
6. doubtful `BAReferent` identity decisions;
7. `DERIVED` elements/rules required;
8. explicit abstract-function ↔ realization separations;
9. recoverability of intermediate dependencies/nodes;
10. recoverability of `transfer` ↔ channel/path binding;
11. source rereading needed by independent projections;
12. localization/revalidation behavior under the same controlled mutation.

## Falsification rule

The current documentation is not declared "better for BA" merely because it was written later.

The hypothesis survives only if the comparison shows a measurable reduction in reconstruction/ambiguity burden without hiding project meaning or moving methodology-specific semantics into the governed documentation.

Remaining gaps from the new BA then become evidence for the smallest correction to documentation or BA0–BA5.
