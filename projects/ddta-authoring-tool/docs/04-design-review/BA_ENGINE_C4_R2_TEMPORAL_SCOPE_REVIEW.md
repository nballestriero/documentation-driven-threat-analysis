# C4 R2 — Superseded authority and optional temporalScope

**CANDIDATE / REVIEW REQUIRED.** Baseline commit: `4ee9b31`. No semantic
activation of `transfer` and no automatic migration of historical BA.

## Methodological source correction

- The previous operational guide R3 is obsolete and is **not a source of
  authority** for this or subsequent operator authoring.
- The R7 rebuild is the current **working review source**. It does not turn
  unreviewed proposals into accepted rules.
- The prior `reviews/transfer-review-r3.md` remains only as an archived
  historical draft. Active source references, the template and the
  operator registry point to R7.
- The `transfer` operator remains `methodStatus: candidate` and
  `reviewStatus: draft` until explicit joint approval.

## Optional time qualification

R7 chapter 7 (especially the canonical signature and LLM authoring shape)
places `temporalScope` at proposition level as a scoped modifier. It is not
a role of `transfer` and must not be duplicated in operator role definitions.

For C4 R2, the shared BAProposition contract declares an optional
`temporalScope` (candidate syntax `temporalScope = <value>`). The parser
recognizes it; a nonempty value produces `BA-TEMPORAL-SCOPE-UNVERIFIED`
with `complete=false`. Missing field is permitted. Empty/duplicate values
are errors; the full syntax and semantics of time, conditional/temporal
qualifiers and the general `scopedModifier` model are **deferred for review**.

This deliberately does not validate durations, intervals, point-in-time
assertions, event boundaries, or temporal truth. No implicit current or
unbounded time scope is introduced. Missing `polarity` remains an error.

## Implementation trace

The common field handling is implemented under:
`FR-MR02-03-02`, coverage reporting under `FR-MR02-03-03`, and
LLM diagnostics under `FR-MR02-02-03`. The loader still corresponds to
`FR-MR02-03-01`. Python docstrings/comments include these references;
no complete FR conformance is claimed.

## Validation

Run from `projects/ddta-authoring-tool/prototype/generic-v01`:

```powershell
py -3 -m unittest discover -s tests -v
py -3 -m ddta_tool check-workspace ../../docs --profile strict
py -3 -m ddta_tool check ../../guides/ba/operators/transfer.md --profile strict
py -3 -m ddta_tool check-ba examples/BA-C4-TRANSFER-VALID.md --json
```

The last check remains INCOMPLETE while `transfer` is draft. Do not
change `reviewStatus` merely to make the validation green.
