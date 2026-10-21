# BAProposition common contract — C4 candidate

The shared contract is declared in [`ba-proposition.yaml`](ba-proposition.yaml). The validator checks each proposition ID for uniqueness **within its owner document**, not globally. The DDTA document identity is declared in its YAML front matter; cross-document identity uniqueness is checked separately by `check-workspace`.

Every BAProposition **MUST** declare `polarity = affirmative` or `polarity = negative` explicitly. Missing, empty or unsupported polarity is an **error in both `draft` and `strict`**. `negative` asserts an explicit governed negation, not missing evidence. Never silently migrate older propositions to affirmative.

Operator-specific roles are exclusively read from the executable contract inside approved operator guides; there is no Python signature table. An unrecognized semantic operator is an error; a recognized operator with no executable guide makes BA coverage **INCOMPLETE**, never PASS.

This increment parses existing fenced plain-text BAPropositions within a DDTA document's `## Base Analysis` / `### BAProposition`. Separate BA files and identity resolution across documents are not yet implemented; the validator must not claim those checks. ID format/derivation from the document will require its own reviewed convention before automated enforcement; only nonempty and local uniqueness are implemented here. A structural PASS does not imply semantic acceptance.

Operator guides and explanatory text are in English. Mermaid projection rules remain separate.

## Optional temporal scope (C4 R2)

R7 chapter 7 treats `temporalScope` as a proposition-scoped modifier, not an
operator role or a global BAReferent classification. The shared declarative
contract now reserves the optional `temporalScope` field. Prototype syntax:
`temporalScope = <source-supported expression>` inside the proposition.
This notation does not settle the full `scopedModifier` grammar or the
semantics of time points, intervals, phases, dates, or conditions.

- Missing `temporalScope` is valid: no time constraint may be inferred.
- Explicit `temporalScope` is parsed and reported as `BA-TEMPORAL-SCOPE-UNVERIFIED`
  (warning and incomplete BA coverage, not PASS) until a temporal DSL is approved.
- An empty or duplicate `temporalScope` declaration is a formal **error**.
- Missing `polarity` remains a formal **error**, regardless of temporalScope.

**Methodological source:** `methodology/DDTA_BASE_ANALYSIS_GUIDE_REBUILD_R7.tex`
(working review source); obsolete R3 is not authority.
