# DDTA R25 - DermaTriage R14 Portability Checkpoint R15

Checkpoint:

`DDTA-R25-DERMATRIAGE-R14-PORTABILITY-CHECKPOINT-R15`

Required predecessor HEAD:

`4f2e87d7d9a0c940672e95ec2bbe27c8f2b273b5`

## Purpose

This is a technical, additive checkpoint.

It does not reopen CR-01 and does not change any Base Analysis construct,
semantic verdict, governed project meaning, or review ordering.

R14 remains the immutable semantic consolidation of CR-01.

## Technical issue recorded

The historical R14 verifier used raw SHA-256 hashes over checked-out text files.
On Windows, Git may materialize text with CRLF line endings while the committed
blob uses LF. The semantic content remains unchanged, but a raw byte hash over
the working-tree file can differ.

This is a verifier portability issue, not a methodology issue.

## R15 verification rule

R15 does not modify the R14 manifest or verifier.

Instead:

1. HEAD must be exactly the committed R14 baseline.
2. Git must report every R14 semantic/checkpoint file as unchanged.
   Git's normal clean/smudge handling makes this invariant to permitted
   line-ending conversion.
3. R14 semantic markers must remain present.
4. R15 files are verified with a canonical-text SHA-256 manifest:
   CRLF and standalone CR are normalized to LF in memory before hashing.
5. Verification is read-only.

## R14 files protected by this checkpoint

- `validation-evidence/dermatriage/post-holdout-method-review-r1/construct-reviews/CR-01_CLASSIFY.md`
- `validation-evidence/dermatriage/post-holdout-method-review-r1/CONSTRUCT_REVIEW_LEDGER.yml`
- `validation-evidence/dermatriage/post-holdout-method-review-r1/NEXT_STEP.md`
- `DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/README.md`
- `DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/CONSOLIDATION_SCOPE.yml`
- `DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/MANIFEST.sha256`
- `DDTA_R25_DERMATRIAGE_CR01_CLASSIFY_CONSOLIDATION_R14/VERIFY_DROPIN.ps1`

## No semantic change

Preserved without modification:

- CR-01 status: `COMPLETE`
- CR-01 verdict: `GUIDE_CLARIFICATION`
- operational macro-kind working set:
  `Actor`, `Component`, `Behavior`, `Interface`, `Boundary`, `Store`,
  `Information`, `State`
- BA0 R1 / BA1 R1 / BA2 R3 / BA3 R1 / BA4 R1 / BA5 R1 remain frozen
- next operational review: `CR-02 decisionRule + comparison condition language`

## Next operational step

After R15 is committed, use the resulting commit as the new repository
continuation baseline and begin CR-02 source-first.
