# BA parent/child structural anchor — review fixture R1

**Status:** candidate assessment; documentation only; not an executable rule and not a new methodology authority.

## Why this exists

The MR → Decision → FR declaration is a document-level parent link. A separate BA structural anchor establishes that at least one **resolved** parent BAReferent participates as a role within a BAProposition owned by the immediate child. These are two distinct checks; neither certifies the semantic soundness of a specialization.

## Fixture A — structural anchor present

**Parent** `MR-01` declares `DDTADocumentAuthoring` (`BAR-EX-MR01-01`):

```text
BAP-EX-MR01-01 - produce
  actor  -> DDTADocumentAuthoring  # BAR-EX-MR01-01
  result -> DDTADocument           # BAR-EX-MR01-02
```

**Child** `DEC-MR01-01` contains:

```text
BAP-EX-DEC-MR01-01-CS01 - consumeService
  consumer -> DDTADocumentAuthoring       # BAR-EX-MR01-01
  service  -> SharedDocumentVerification  # BAR-EX-DEC-MR01-01-05
```

**Expected structural result:** `STRUCTURAL_ANCHOR_FOUND`. Does not imply semantic acceptance.

## Fixture B — parent BAReferent appears only in the child's table

If `BAR-EX-MR01-01` appears only in the child BAReferent table or its prose but in **no role** of any child BAProposition, it does not establish an anchor.

**Expected result:** `BA-PARENT-ANCHOR-MISSING`; review warning with human guidance and LLM instructions.

## Fixture C — missing or unresolved BA

If either BA is unavailable, unparsable, or cannot be reliably associated with its declared DDTA document, or identifiers/scope cannot be resolved, the structural check cannot conclude.

**Expected result:** `BA-PARENT-ANCHOR-UNVERIFIED` / incomplete. Do not claim a structural PASS, and do not falsely declare the anchor absent.

## Review constraints

1. Check only the immediate parent (`parentMacroRequirement` or `parentDecision`).
2. Compare resolved BAReferent identities; never name similarity.
3. Read linked standalone BA files when present; do not assume inline-only BA.
4. Never fabricate a BAProposition to satisfy the checker.
5. A future implementation must point back to `FR-MR03-05-01` using `DDTA-FR: FR-MR03-05-01` in the implementation symbol's docstring as required by the existing FR-to-code trace convention.
6. The place and format of machine-readable guidance for cross-document diagnostics is still to be decided; do not hard-code a duplicate prompt in the code.
