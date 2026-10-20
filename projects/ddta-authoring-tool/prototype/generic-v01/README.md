# DDTA Authoring Tool — Generic MR/Decision/FR prototype 0.1

**CANDIDATE / REVIEW ONLY.** This is a technical prototype, not a new methodological authority, not a Base Analysis, and not a migration of existing Markdown files.

## Principle verified

One generator and one validator operate on different document types through loadable YAML format definitions. Existing files in the repository without YAML front matter are not migrated or silently accepted. **Adding another type only needs another YAML schema if all required rules fit the common supported grammar.** Unsupported features are explicitly rejected; Python must be extended once, generically, before such additional schema rules are accepted.

## Project requirements this prototype addresses partially

- `DEC-MR01-02` / `FR-MR01-02-01`: document type and identity are declared in YAML rather than inferred from filename.
- `DEC-MR01-02` / `FR-MR01-02-02`: generate Markdown from a selected schema, without inventing governed content.
- `DEC-MR02-01` / `FR-MR02-01-01`: load the document's declared format; reject missing or unsupported definitions.
- `DEC-MR02-01` / `FR-MR02-01-02`: check generic fields, sections, cardinalities, and a declared clauses grammar.
- `DEC-MR02-02` / `FR-MR02-02-01`, `FR-MR02-02-02`: structured diagnostics, draft vs strict.
- `DEC-MR01-01` / `FR-MR01-01-04`: execute from PowerShell or Linux via Python CLI.

No complete FR compliance, semantic acceptance, editor LSP, reference resolution (MR-03), BA or Mermaid projection is claimed.

## Windows UTF-8 regression fix (FIX1)

The original review package had test fixtures read with `Path.read_text()` without an explicit encoding. On Windows with a non-UTF-8 locale this converted the Unicode em dash in the H1 into mojibake, triggering a false `DOC-H1-MISMATCH` in four tests. FIX1 updates **only the test fixture I/O encoding** to UTF-8; the shared Python engine, CLI and all three format definitions remain unchanged. The 33-test suite is verified in both the normal runtime and a UTF-8-disabled locale simulation.

## Runtime

Python 3.10+, PyYAML 6; run from the `prototype/generic-v01` folder.

### PowerShell

```powershell
py -3 -m pip install -r requirements.txt
py -3 -m unittest discover -s tests -v
py -3 -m ddta_tool check examples/MR-VALID.md --profile strict
py -3 -m ddta_tool check examples/DEC-VALID.md --profile strict
py -3 -m ddta_tool check examples/FR-VALID.md --profile strict
py -3 -m ddta_tool check examples/FR-INVALID.md --profile draft --json

py -3 -m ddta_tool new MacroRequirement --id MR-NEW --output "$HOME\Downloads\MR-NEW.md"
py -3 -m ddta_tool new Decision --id DEC-NEW --set parentMacroRequirement=MR-NEW --output "$HOME\Downloads\DEC-NEW.md"
py -3 -m ddta_tool new FunctionalRequirement --id FR-NEW --set parentDecision=DEC-NEW --output "$HOME\Downloads\FR-NEW.md"
```

### Linux

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
python3 -m ddta_tool check examples/MR-VALID.md --profile strict
python3 -m ddta_tool check examples/DEC-VALID.md --profile strict
python3 -m ddta_tool check examples/FR-VALID.md --profile strict
```

`new` creates an intentionally incomplete draft; `check --profile draft` warns for missing content, while `strict` fails. `new` refuses to overwrite an existing file.

`check --json` reports `type`, `complete`, `valid`, `errors`, `warnings`, and diagnostic code/severity/message/position (`null` when unavailable). Exit codes: 0 pass, 1 nonconformity/unavailable schema, 2 CLI/IO/generation error.

Schemas are discovered from `schemas/*.yaml`. To use another schema directory, put `--schemas-dir <directory>` **before** the command: `python -m ddta_tool --schemas-dir extra-schemas new ExampleNote ...`.

## Schema contract 0.1 (supported DSL)

- `schemaId` and `schemaVersion` strings.
- `metadata` fields with `type: string` or `string-list`, optional `required`, `default`, `const`, `enum`, `pattern`, list constraints `unique`, `disallowSelf`, `minItems`.
- `sections` ordered entries with `name`, `required`, `kind: text|clauses`, optional `hint`; clause sections require `minItems`, `itemPattern` (two capture groups: clause identifier and content), and `itemTemplate` for generation.
- Unknown schema keys/types are rejected before validation: a constraint must not be silently ignored.

*MR*: `Intent`, `Context`, `Stakeholders`, `Scope` required; `Assumptions / Constraints` optional, `dependsOn` optional list. *Decision*: `parentMacroRequirement` and `Context`, `Decision`, `Consequences`. *FR*: `parentDecision`, `Functional obligation`, `Normative clauses` with >=1 nonempty clause; `SPO references` optional. The optional `decisionKind` is authoring/review metadata, not a new DDTA L1 field.

## Deliberate limitations

- This is a **structural** checker; it does not determine if an MR, Decision or normative clause is semantically correct.
- It checks parent fields are present and are strings; it **does not confirm** that the referenced document exists (MR-03).
- Inline Markdown headings inside fenced blocks are ignored. Parsing is limited to simple `#` / `##` headings; this is not a full CommonMark implementation.
- Clause statements currently use the single-line Markdown list format `- **NC-1:** text`, controlled by the FR YAML schema. Multiline/nested clause syntax is not supported by this initial DSL; do not claim that the complete DDTA clause grammar has been implemented.
- The existing repository's DDTA Markdown uses different headings and no YAML front matter; bulk conversion is not included.
- Profile `draft` only downgrades expected incompleteness; a noninterpretable format is an error in both modes.

## Evidence

`TEST_RESULTS.txt` includes the executed tests. The suite demonstrates MR, Decision and FR, and creation/validation of a **fourth synthetic type by adding its YAML schema only**, without modifying the engine.

## Checkpoint and user environment confirmation (2026-10-20)

The FIX1 package was tested by the author on Windows PowerShell with Python 3.14: **33/33 tests OK**; all three strict example checks (MR, Decision, FR) reported `0 errors, 0 warnings; PASS`. This confirmation supplements, rather than rewrites, the original `TEST_RESULTS.txt` snapshot, whose last line predates the Windows run. No full specification conformance is claimed.
