# DDTA facial-access document-authority + current-slice drop-in R1

## Required repository baseline

Apply only when:

```text
git rev-parse HEAD
eef1031e47f91f60f18121aba09b6386699f8317
```

This package intentionally does **not** contain Base Analysis output and does not open BA6.

## Semantic microstep

Establish one unambiguous source-authority gate for facial-access research material and materialize a current governed MR-0003 validation slice compliant with the closed documentation hierarchy.

## Historical preservation rule

No historical `.md`, `.tex` or `.pdf` artifact is overwritten, moved or deleted.

Three new `AUTHORITY_NOTICE.md` files mark high-risk historical directories. The global authority registry is the source of truth for current-vs-historical classification.

## Files changed/added

Modified tracked file:

- `README.md`

New files:

- `governance/document-authority/README.md`
- `governance/document-authority/document-authority.registry.yml`
- `_working/ddta-metamodel-working-package/01-mr/03-example-facial-access/AUTHORITY_NOTICE.md`
- `02-decision/05-example-facial-access/AUTHORITY_NOTICE.md`
- `04-specialized-requirement/03-example-facial-access/AUTHORITY_NOTICE.md`
- `governed-corpora/facial-access/current/README.md`
- `governed-corpora/facial-access/current/corpus.manifest.yml`
- `governed-corpora/facial-access/current/MR-0003_IDENTITY_VERIFICATION.md`
- `governed-corpora/facial-access/current/DECISIONS.md`
- `governed-corpora/facial-access/current/FUNCTIONAL_REQUIREMENTS.md`
- `governed-corpora/facial-access/current/SECURITY_REQUIREMENTS.md`
- `governed-corpora/facial-access/current/DOCUMENTATION_GAPS.md`
- `governed-corpora/facial-access/current/HISTORICAL_TO_CURRENT_MIGRATION.md`
- `governed-corpora/facial-access/current/BA_COMPARISON_PLAN.md`

Plus this README and checksum manifest.

## Intended post-review state

- historical facial corpora: preserved, not primary BA sources;
- `FACIAL-ACCESS-GOV-R1`: current governed thesis validation corpus;
- BA6: still `NOT STARTED`;
- next semantic experiment: rebuild BA from current documentation and compare with historical-source BA as regression evidence.

## Apply

Extract the ZIP at repository root, preserving paths.

Then validate before staging:

```powershell
git rev-parse HEAD
git status --short
git diff --check
git diff -- README.md
```

Because new files are untracked, inspect them explicitly before staging. Then stage only this package's repository files and run:

```powershell
git diff --cached --check
git diff --cached --stat
git diff --cached -- README.md
git status --short
```

Do not commit until the staged file set and content have been reviewed against this manifest.
