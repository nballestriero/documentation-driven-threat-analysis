# BA5-T2 canonical semantic registry and governed-extension drop-in

**Expected repository baseline before application:** `85622414b2ff52d58f3cd11776fef4b3753afc7d`

This package executes only `BA5-T2 - canonical semantic registry coverage and governed-extension pressure test` from Work Plan R20.

It does **not** close BA5 and does not execute BA5-T3, BA6, formal STRIDE/STRIDE-AI schemas, AnalysisRecord/Common Finding or ThreatForge implementation work.

## Result

BA5-T2 broadens the T1 exact-token/no-synonym hypothesis across BA2 operator keys, operator-scoped roles, semantic-kind keys and controlled-value domains.

Key dispositions:

- exact canonical-token authoring: **REQUIRED**;
- one flat global token namespace: **REJECTED**;
- registry domain/context resolution: **REQUIRED**;
- all thirteen BA2 operator keys: **REQUIRED EXACT KEYS**;
- role lookup as `(semanticOperatorKey, roleKey)`: **REQUIRED**;
- role aliases such as `src`: **REJECTED**;
- `semanticKind` as controlled extensible domain: **REQUIRED**;
- universal semantic-kind taxonomy: **NOT FORCED**;
- `store` and `contract`: **ACCEPTED FOR T2 CANONICAL PRESSURE**;
- `channel`: **DEFERRED / EVIDENCE-GATED**;
- reusable controlled-value domains: **REQUIRED WHERE APPLICABLE**;
- literal/local value auto-registration: **REJECTED**;
- exact polarity `affirmative | negative`: **ACCEPTED**;
- exact modifier kinds `condition | temporalScope`: **ACCEPTED**;
- controlled `responsibilityKind` domain with current `ownership` / `management`: **ACCEPTED FOR T2 PRESSURE**;
- immutable registry revision resolution: **REQUIRED**;
- alias/synonym as new normative registry entry: **REJECTED**;
- governed extension of an already extensible method-neutral domain: **REQUIRED PATH**;
- changing a closed BA2 operator/role contract through BA5: **REJECTED**;
- material new operator/role -> smallest BA2 reopen: **REQUIRED ROUTING**;
- method taxonomy -> BA registry: **REJECTED**;
- tool domain/context validation and completion: **ALLOWED**;
- tool semantic equivalence/approval: **REJECTED**;
- new BAE family: **NOT FORCED**;
- BA1 / BA2 / BA3 / BA4 reopen: **NOT TRIGGERED**;
- synonym machinery: **NOT FORCED**;
- BA5: **STARTED / NOT CLOSED**.

The decisive T2 refinement is that a common canonical-authoring discipline does not imply one flat registry or one lifecycle. Referent names are project-baseline scoped; BA2 operators/roles are methodology-contract scoped; semantic-kind and controlled-value registries may be evidence-gated and extensible; method terminology remains downstream.

## Existing tracked file modified

- `README.md`

No other existing tracked file is replaced. BA0-BA4 closure artifacts, BA5-T1 artifacts, Chapters 2-4 and historical work plans remain unchanged.

## New methodology artifacts

- `methodology/BA5_CANONICAL_SEMANTIC_REGISTRY_CANDIDATE_R2.md/.tex/.pdf`
- `methodology/BA5_T2_CANONICAL_SEMANTIC_REGISTRY_COVERAGE_GOVERNED_EXTENSION_R1.md/.tex/.pdf`
- `methodology/BA5_T2_PROVISIONAL_LEDGER_R1.yml`
- `methodology/DDTA_CURRENT_RESEARCH_STATE_R18.md`
- `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R21.md/.tex/.pdf`

## Post-package state

```text
BA0                 CLOSED
BA1                 CLOSED
BA2                 CLOSED
BA3                 CLOSED
BA4                 CLOSED
BA5-T1              COMPLETED / PROVISIONAL PASS WITH CANONICAL-REFERENT-NAMING LOWER-BOUND
BA5-T2              COMPLETED / PROVISIONAL PASS WITH DOMAIN-SCOPED REGISTRY AND GOVERNED-EXTENSION REFINEMENT
BA5                 STARTED / NOT CLOSED
BA6                 NOT STARTED
```

## Next authorized microstep

Only after this package is reviewed, committed, pushed and remotely verified:

> `BA5-T3 - canonical registry, controlled-authoring and no-synonym closure review`

Do not start BA6 before BA5 is explicitly closed.

## Application rule

Before extraction, both `HEAD` and `origin/master` must equal the expected baseline and the worktree must be clean. Verify the ZIP SHA-256 supplied with the package. After extraction, expect exactly the one tracked modification listed above plus the thirteen new files in this README. Run `git diff --check` before staging and `git diff --cached --check` after staging; both must return no whitespace errors.
