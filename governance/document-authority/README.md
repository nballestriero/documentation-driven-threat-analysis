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

`governed-corpora/facial-access/current/` is the current governed **thesis validation corpus** for the facial-access branch introduced by this package.

The following remain historical/non-canonical evidence and are not primary sources for the new BA:

- `_working/ddta-metamodel-working-package/01-mr/03-example-facial-access/`
- `02-decision/05-example-facial-access/`
- `04-specialized-requirement/03-example-facial-access/`

They are intentionally not deleted or rewritten.

## Baseline discipline

The package that introduces this registry is based on repository baseline:

`eef1031e47f91f60f18121aba09b6386699f8317`

The current facial-access corpus uses logical governed baseline key `FACIAL-ACCESS-GOV-R1`. A concrete BA run must additionally pin the Git commit containing the applied package; this file deliberately does not guess that future commit SHA.
