# BAProposition common contract — C4 candidate

The shared contract is declared in [`ba-proposition.yaml`](ba-proposition.yaml). The validator checks each proposition ID for uniqueness **within its owner document**, not globally. The DDTA document identity is declared in its YAML front matter; cross-document identity uniqueness is checked separately by `check-workspace`.

Every BAProposition **MUST** declare `polarity = affirmative` or `polarity = negative` explicitly. Missing, empty or unsupported polarity is an **error in both `draft` and `strict`**. `negative` asserts an explicit governed negation, not missing evidence. Never silently migrate older propositions to affirmative.

Operator-specific roles are exclusively read from the executable contract inside approved operator guides; there is no Python signature table. An unrecognized semantic operator is an error; a recognized operator with no executable guide makes BA coverage **INCOMPLETE**, never PASS.

This increment parses existing fenced plain-text BAPropositions within a DDTA document's `## Base Analysis` / `### BAProposition`. Separate BA files and identity resolution across documents are not yet implemented; the validator must not claim those checks. ID format/derivation from the document will require its own reviewed convention before automated enforcement; only nonempty and local uniqueness are implemented here. A structural PASS does not imply semantic acceptance.

Operator guides and explanatory text are in English. Mermaid projection rules remain separate.
