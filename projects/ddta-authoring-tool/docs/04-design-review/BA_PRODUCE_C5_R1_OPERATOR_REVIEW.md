# C5 R1 — `produce` operator guide candidate (review, not activation)

**Status:** candidate for human review. Baseline `e1f4aa6` (`master`). This
checkpoint adds a draft English operator guide, three standalone fixture
Markdown files, and a test module. It does not modify or activate the engine,
change the recognized-operator registry, or edit historical MR-01 BA.

## Source and proposed contract

**Methodological review source:**
`methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex`, chapter 8,
described pages 32–38. R3 is obsolete and is not a source for current review.

The R7 signature is encoded as:

```text
produce
  actor  -> BAReferent [1]
  input  -> BAReferent [0..*]
  result -> BAReferent [1..*]
```

`polarity = affirmative | negative` is a required shared BAProposition field,
not an operator role. The optional common `temporalScope` is recognized but
semantically unverified. R7 also discusses `condition`, but the current C4
parser/contract does not support it. This C5 checkpoint does not add a silent
`condition` interpretation or an independent `scopedModifier` grammar.

## Semantic review checkpoints

1. **Minimal production fact:** an identified actor makes at least one
   governed result available. This does not imply a new object was created.
2. **Optional input:** absent inputs are valid; an input can be included only
   where governed by the same source assertion, never because it exists upstream.
3. **Reuse identities:** an unchanged result can reappear as transfer content
   or a later input with the same BAReferent ID. This isn't resolved
   cross-document by the current engine.
4. **Many outputs:** multiple results belong to the same proposition only
   when the governed source supports one production fact binding them.
5. **Explicit negative polarity:** negation of production must be governed;
   unknown/missing source evidence cannot be converted to negative polarity.
6. **No inferred implementation:** no algorithm, model, intermediary,
   destination, transfer, persistence, ownership, creation or runtime success.
7. **R7's operator disambiguation section is unfinished:** do not invent
   new formal distinctions to fill the optional heading.

## Test purpose and expected outputs

The guide has `methodStatus: candidate` and `reviewStatus: draft`.
The BA loader must recognize it as `pending`, not as `active`.

- `check ../../guides/ba/operators/produce.md --profile strict`: expected
  PASS for **document format only**.
- `check-ba examples/BA-C5-PRODUCE-VALID.md --json`: expected `complete=false`
  and `BA-OP-UNCOVERED` while `produce` remains draft. This is **not** a
  valid BA PASS despite the fixture's structurally conformant roles.
- `check-ba examples/BA-C5-PRODUCE-MISSING-POLARITY.md --json`: expected
  `BA-POLARITY-MISSING` **error**, including when the operator is draft.
- A **temporary copy** of the guide with `reviewStatus: reviewed` is used
  only in unit tests: the unchanged generic loader checks actor, optional
  input, results, guide-derived diagnostics and cardinalities. Temporary
  approval does not change the actual guide in the repository.
- The previously activated `transfer` must continue to pass its own tests.
- The historic MR-01 BA is intentionally not migrated: it still lacks
  explicit `polarity`. Only a later reviewed correction may fix it.

## Boundaries and next human decision

- R7 is the working methodological review source; the guide remains a
  candidate until explicit approval.
- No Python operator-specific branch was added.
- Structural validation does not decide if the document truly governs
  production, whether the BAReferents are identical across documents, or
  whether parent/child BA are structurally anchored.
- After source and example review, a **separate** checkpoint may set
  `reviewStatus: reviewed` while retaining `methodStatus: candidate`.
- A complete `temporalScope`/`condition` model is deferred to a separate
  shared-contract review. It is not a role of `produce`.

## Local verification commands

Run from `projects/ddta-authoring-tool/prototype/generic-v01`:

```powershell
py -3 -m unittest discover -s tests -v
py -3 -m ddta_tool check-workspace ../../docs --profile strict
py -3 -m ddta_tool check ../../guides/ba/operators/produce.md --profile strict
py -3 -m ddta_tool check-ba examples/BA-C5-PRODUCE-VALID.md --json
py -3 -m ddta_tool check-ba examples/BA-C5-PRODUCE-MISSING-POLARITY.md --json
```

For the two final `check-ba` commands, exit code 1 is **expected** until the
first is activated and until the second has an explicit supported polarity.
A unit-test PASS is not evidence of semantic approval or complete FR compliance.
