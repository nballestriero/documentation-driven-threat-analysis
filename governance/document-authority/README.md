# DDTA document-authority governance

## Purpose

This directory prevents a repository artifact from becoming a current Base Analysis source merely because it is easy to find, appears realistic, or is chronologically recent.

The repository deliberately preserves historical, experimental and superseded material. Preservation is research evidence; it is not authority.

## Mandatory source gate

Before constructing a current Base Analysis:

1. pin the repository commit used as the source baseline;
2. resolve every candidate source through `document-authority.registry.yml`;
3. use as primary project sources only artifacts whose effective authority permits `primaryBASourceAllowed: true`;
4. keep historical/non-canonical artifacts available only for comparison, regression, falsification or provenance;
5. if authority is absent or ambiguous, stop current-BA construction and record a documentation-authority gap instead of guessing.

Chronological recency, directory depth, filename wording and tool/LLM confidence are never substitutes for this gate.

## Authority classes

- `CURRENT_GOVERNED` — current governed validation/project documentation in the declared scope; eligible as primary BA source.
- `CLOSURE_AUTHORITY` — artifact defining a closed DDTA semantic/documentation contract; authoritative for that contract, not automatically a project corpus.
- `HISTORICAL` — retained state of a prior phase.
- `SUPERSEDED` — explicitly replaced for forward use.
- `EXPERIMENTAL_NON_CANONICAL` — research/probe material that never acquired current project authority.
- `REGRESSION_EVIDENCE` — retained specifically to pressure-test or compare later behavior.

`researchRole` may complement `authorityStatus`; it never upgrades authority.

## Current facial-access rule

The current governed Facial Access R24 baseline is:

- `governed-corpora/facial-access/candidate-r3/`
- authority baseline `FACIAL-ACCESS-GOV-R2`

It was explicitly promoted **in place** from the regression-closed `R3-CANDIDATE-9` corpus after full successor semantic regression. Its effective authority is `CURRENT_GOVERNED` and `primaryBASourceAllowed: true`.

The directory name `candidate-r3/` is retained as provenance. Filename or directory wording does not override the explicit registry classification.

The former governed R1 corpus:

- `governed-corpora/facial-access/current/`
- `FACIAL-ACCESS-GOV-R1`

remains `SUPERSEDED` with `primaryBASourceAllowed: false` and is retained as regression evidence.

The earlier MR-0003-only successor candidate:

- `governed-corpora/facial-access/candidate-r2/`

remains `EXPERIMENTAL_NON_CANONICAL` with `primaryBASourceAllowed: false` and is retained for regression/provenance evidence.

The broader R24 working project document:

- `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_PROJECT_ONLY.tex`

also remains `EXPERIMENTAL_NON_CANONICAL`.

The following older facial-access materials remain historical/non-canonical evidence and are not primary sources for an accepted current BA:

- `_working/ddta-metamodel-working-package/01-mr/03-example-facial-access/`
- `02-decision/05-example-facial-access/`
- `04-specialized-requirement/03-example-facial-access/`

Historical and working evidence is intentionally preserved rather than rewritten to look current.
## Baseline discipline

The package that introduced this registry was based on repository baseline:

`eef1031e47f91f60f18121aba09b6386699f8317`

That commit remains historical provenance for the introduction of the authority gate; it is not the repository's current HEAD.

The superseded facial-access R1 corpus retains logical baseline key `FACIAL-ACCESS-GOV-R1` for historical provenance. The promoted integrated R24 successor uses `FACIAL-ACCESS-GOV-R2`. Candidate-r2 retains its candidate-only provenance and is not a governed BA source.

Every accepted BA run must pin both the explicitly promoted authority baseline `FACIAL-ACCESS-GOV-R2` and the concrete Git commit containing the promotion state used as its source baseline. The promotion decision was prepared against `4d6aa85385b79be926125d4e61390ac185f63cfd`; that source commit records the regression-closed candidate immediately before the authority change.

The registry may record later repository commits when authority classifications are reviewed or extended; chronology alone never promotes a working artifact.