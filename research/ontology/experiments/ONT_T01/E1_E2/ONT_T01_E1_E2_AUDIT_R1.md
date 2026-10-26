# ONT-T01 — E1/E2 Original inputs and structural audit R1

**Status:** REVIEW CANDIDATE. **Gold baseline:** `9593c37`, `ONT_T01_GOLD_STANDARD_R3.md`.

## Input provenance

The three `.json` files are byte-for-byte copies of original JSON supplied in the conversation. Their SHA-256 values are in the CSV and machine-readable audit. They have not been normalized or edited. Attribution to model is based on the count tuples from the user’s prior experiment; the original pasted files do not have an intrinsic `model` field.

| Model | Original input | O | R | A | Ambiguities |
|---|---|---:|---:|---:|---:|
| deepseek | archived (SHA-256 in CSV) | 34 | 7 | 17 | 2 |
| qwen | archived (SHA-256 in CSV) | 31 | 13 | 20 | 3 |
| mistral | archived (SHA-256 in CSV) | 31 | 9 | 18 | 5 |
| Gemini | **not archived**; partial information only from conversation | 14 | 3 | 14 | 0 |

## Automated checks

Checks: valid JSON; `testId`; top-level collection arrays; unique object/relation/action IDs; reference resolution (`participants[].objectId`, `actorId`, `resultIds`); literal evidence as contiguous substring of the R3 original source (including ambiguities). Evidence checks are string-literal and **not** semantic entailment checks.

| Model | JSON parsed | Duplicate IDs | Dangling object references | Nonliteral evidence |
|---|---|---:|---:|---:|
| deepseek | PASS | 0 | 0 | 0 / 60 |
| qwen | PASS | 0 | 0 | 3 / 67 |
| mistral | PASS | 0 | 0 | 0 / 63 |
| Gemini | NOT CHECKED | — | — | — |

## Evidence findings

### deepseek

All evidence strings match a contiguous substring of the source text.

### qwen

- `objects/O-018`: nonliteral evidence `l'Inventory Service consulta l'Inventory Store e restituisce le quantità disponibili`
- `actions/A-008`: nonliteral evidence `l'Inventory Service consulta l'Inventory Store`
- `actions/A-009`: nonliteral evidence `l'Inventory Service consulta l'Inventory Store e restituisce le quantità disponibili`

### mistral

All evidence strings match a contiguous substring of the source text.

## Limits and next gates

- Gemini original JSON is not available in the accessible uploaded files; **no Gemini structural PASS is claimed**. Obtain a verbatim copy before a 4-way scored comparison.
- Do not interpret number of rows as extraction accuracy. Do not derive a single score by dividing raw matches by 64.
- Preserve source V1 outputs without changing spelling, normalization, or evidence. Any corrective interpretation belongs in a separate mapping artifact.
- E3 semantic matching and E4 unsupported/contradicted assertions **not performed** in this package.
- The Gold R3 remains `REVIEW CANDIDATE` and is not modified.
