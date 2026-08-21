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

`governed-corpora/facial-access/current/` remains the current governed **thesis validation corpus**, registered as `FACIAL_ACCESS_CURRENT_R1` / `FACIAL-ACCESS-GOV-R1`, and is eligible as a primary BA source within its declared scope.

The R24 working project document:

- `methodology/DDTA_FACIAL_ACCESS_PROJECT_DOCUMENTATION_WORKING_R24_PROJECT_ONLY.tex`

is explicitly classified in `document-authority.registry.yml` as `EXPERIMENTAL_NON_CANONICAL` with `primaryBASourceAllowed: false`.

It is a working successor candidate used to pressure-test documentation authoring, BA derivation and downstream analysis. It does **not** supersede `FACIAL_ACCESS_CURRENT_R1` by chronology, filename, abstraction quality or research preference. Promotion requires an explicit authority change in the registry.

The following older facial-access materials remain historical/non-canonical evidence and are not primary sources for the current BA:

- `_working/ddta-metamodel-working-package/01-mr/03-example-facial-access/`
- `02-decision/05-example-facial-access/`
- `04-specialized-requirement/03-example-facial-access/`

Historical and working evidence is intentionally preserved rather than rewritten to look current.
## Baseline discipline

The package that introduced this registry was based on repository baseline:

`eef1031e47f91f60f18121aba09b6386699f8317`

That commit remains historical provenance for the introduction of the authority gate; it is not the repository's current HEAD.

The current facial-access corpus uses logical governed baseline key `FACIAL-ACCESS-GOV-R1`. Every concrete BA run must additionally pin the actual Git commit used as its source baseline.

The registry may record a later repository commit when its authority classifications are reviewed or extended. That metadata does not change the governed baseline key and does not promote any working artifact by chronology alone.