# DDTA R25 Incremental Authoring Consolidation R44 - Continuation

## Baseline

Repository: `nballestriero/documentation-driven-threat-analysis`  
Branch: `master`  
Baseline commit: `0b8249e11bcd2c93f12866b1f43e0b2d5508fbc3`

No commit or push is performed by this package.

## Consolidated state

Two artifacts are intentionally developed in parallel and incrementally:

1. `methodology/DDTA_DOCUMENTATION_AUTHORING_GUIDE_R7_REBUILD_R1.*`
   - rebuilt from an initially empty guide;
   - currently contains the Project Problem Framing section only as the first completed methodological slice;
   - contains a temporary, visibly marked reference to `DDTA_DOCUMENTATION_AUTHORING_GUIDE_R6_CANDIDATE_R2.tex`, to be deleted before a future final version;
   - human guidance and LLM execution guidance are separated;
   - the LLM profile includes source-first constraints and an exact analysis/final-output schema.

2. `validation-evidence/dermatriage/post-holdout-method-review-r1/incremental-authoring-case-study-r1/DDTA_DERMATRIAGE_PARALLEL_CASE_STUDY_R1.*`
   - source-first DermaTriage reconstruction/validation artifact;
   - current governed content is the approved Project Problem Framing;
   - the next content element is the first MacroRequirement, to be derived from OR2 rather than copied from prior governed reconstruction;
   - Base Analysis remains empty at framing level because no BAReferent/BAProposition decomposition is yet justified.

## Approved DermaTriage Project Problem Framing

> Il problema che DermaTriage deve affrontare è il supporto al triage precoce di casi dermatologici relativi a lesioni potenzialmente oncologiche. Il progetto parte dalle informazioni già disponibili sul caso per determinarne l’urgenza e una priorità operativa di presa in carico, con l’obiettivo di favorire un instradamento specialistico tempestivo.

## Current MacroRequirement lesson under validation

The first attempted MR exposed several authoring risks that are now inputs to the rebuilt guide:

- a child must narrow its parent rather than reword it;
- fields must not be populated merely because the template exposes them;
- `Scope` or `Assumptions / Constraints` may be `—` when no independent source-governed meaning exists;
- solution details known from the source must not be pulled prematurely into a higher semantic level;
- human-readable guidance may be concise, while the LLM execution profile can remain more explicit and constraint-oriented.

## Next step

Return to OR2 and derive one MacroRequirement responsibility at a time. Before adding MR-01 to the case-study PDF, validate:

1. source support;
2. parent-to-child narrowing;
3. one durable macro responsibility only;
4. no Decision/FR leakage;
5. no field-level rewording;
6. STOP/PROCEED result.

After the MR is accepted, add the corresponding MacroRequirement methodology section to the rebuilt guide and update both page-MD5 indexes.

## Integrity mechanism consolidation

During R44 packaging, the DermaTriage case-study source was migrated from its original three-page hard-coded MD5 macro implementation to the same generic `PAGE-CONTENT` / `PAGE-DESC` / `PAGE-HASH-DEFS` / `PAGE-INTEGRITY-ROWS` mechanism used by the rebuilt guide. This is an integrity-tooling change only.

- page 1 MD5 remains `ccabe4bed7cca4d2f68a2005e42f36e3`;
- page 2 MD5 remains `0fb76dc0491da2793823b20571e5268b`;
- page 3 integrity-index MD5 changes to `54275f1583e53f3d9e98664420b2b6c6` because the index-page canonical payload now contains the generic integrity markers;
- PDF render comparison before/after the migration reports no visual page changes.
