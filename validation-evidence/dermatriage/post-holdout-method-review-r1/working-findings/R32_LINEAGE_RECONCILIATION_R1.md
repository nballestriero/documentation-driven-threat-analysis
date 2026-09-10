# R32 Lineage Reconciliation R1

## Status

`GOVERNANCE CORRECTION / NO NORMATIVE METHOD CHANGE`

The intended first-candidate-group drop-in checked for predecessor `ca99122b2f628f169bed85e04e731c8f3f89ca3c`, but the local repository was already at `666c192581dc58c0c464703807d36328bdbf4f7e`. Its verifier correctly failed. The package was then extracted and committed, producing `3cdd912e76ceeb19d2224efa6a506a793d35f26c`.

Actual parentage is therefore `ca99122b2f628f169bed85e04e731c8f3f89ca3c -> 666c192581dc58c0c464703807d36328bdbf4f7e -> 3cdd912e76ceeb19d2224efa6a506a793d35f26c`.

`666c192581dc58c0c464703807d36328bdbf4f7e` is the earlier R32 checkpoint `Establish post-operator-audit disposition work plan R32`. It had already introduced a post-operator-audit R4 plan, ledger R18 and disposition matrix R1. The later first-candidate-group package independently reused R32/R4/R18 labels and modified R18.

The later commit is a normal fast-forward child of `666c192581dc58c0c464703807d36328bdbf4f7e`. Its semantic findings remain useful; the defect is governance metadata and revision collision, not conceptual corruption.

Do not amend or force-push. R33 creates R5, R19 and matrix R2 and declares both R32 commits historical predecessors.

From R33 onward: published revision artifacts are immutable; semantic checkpoints use fresh checkpoint numbers; ledgers/plans/matrices use next revisions; a failed predecessor check blocks application until lineage is reconciled.

Semantic result preserved: `consumeData` rejected redundant; `provideService` insufficient evidence; `perform` irreducibility not demonstrated; generic `modify` rejected; OBS-OT-01 retained; top-level operator count remains 14.
