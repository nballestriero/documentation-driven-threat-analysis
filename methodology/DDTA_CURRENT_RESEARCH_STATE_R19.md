# DDTA current research state - R19

**Prepared against repository baseline:** `8d8dae5f7c28d83b70cbdea090028e4ec0f93571`

**Purpose:** active semantic-state pointer after BA5 integrated closure review; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0 responsibility/non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- BA2 relation/action vocabulary: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA3 provenance/derivation/identity/lifecycle/change-revalidation: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA4 projections: **CLOSED FOR CURRENT THESIS SCOPE BY BA4-T3**.
- BA5-T1 canonical referent naming: **COMPLETED / PROVISIONAL PASS WITH CANONICAL-REFERENT-NAMING LOWER-BOUND**.
- BA5-T2 canonical semantic registry: **COMPLETED / PROVISIONAL PASS WITH DOMAIN-SCOPED REGISTRY AND GOVERNED-EXTENSION REFINEMENT**.
- BA5-T3 integrated closure review: **CLOSED / PASS**.
- BA5 canonical registry/controlled authoring: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA6 complete Base Analysis regression/closure: **NOT STARTED / NEXT PHASE**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## BA5 closed hypothesis

For semantically operative DDTA authoring:

```text
registered canonical token/name
    -> normative semantic input

unregistered alias / synonym
    -> rejected as normative input

free explanatory prose
    -> allowed outside semantic bindings
```

This closes a controlled semantic authoring contract, not a universal controlled natural language.

## Closed canonical registry shape

```text
CanonicalSemanticRegistrySet
|
+-- CanonicalReferentNameRegistry
+-- SemanticOperatorRegistry
+-- OperatorRoleRegistry
+-- SemanticKindRegistry
`-- ControlledValueRegistry 0..*
```

The umbrella is logical and is **NOT BAE**. Physical co-location is allowed when domain, scope/authority, canonical key and immutable revision where applicable remain mechanically recoverable.

## Referent naming

Within one governed baseline/naming scope, one shared named referent has one exact canonical name across governed semantic references, accepted BA rendering and derived views that present that same shared entity.

```text
cameraIngresso
```

is not silently interchangeable with `entryCamera`, `cameraEntrata`, `CameraIngresso` or `camera_ingresso`.

Canonical name remains distinct from BA semantic identity. A governed rename can retain the same BAReferent through BA3 continuity.

## Operator, role, kind and controlled-value discipline

The thirteen BA2 operator keys remain exact. Role lookup remains `(semanticOperatorKey, roleKey)` rather than a context-free role dictionary.

`semanticKind` remains a method-neutral evidence-gated registry; `store` and `contract` remain current accepted pressure examples while `channel` remains **DEFERRED / EVIDENCE-GATED**.

Reusable controlled values use explicit domain registries where applicable. Ordinary local literals are not auto-registered.

Evolving semantic registries resolve through immutable revisions for historical reproducibility.

## Governed extension boundary

A proposed new token is not accepted merely because it is lexically different.

- same meaning as an existing key -> use existing canonical key;
- method-specific term -> keep downstream;
- independent reusable project meaning -> BAReferent;
- genuinely new method-neutral kind/extensible value -> evidence-backed governed registry revision;
- materially new operator/role semantics -> smallest BA2 reopen.

BA5 therefore cannot become a backdoor for changing closed BA2 semantics.

## Projection and tool boundary

Shared projection rendering preserves canonical project referent naming. Method-owned types, aggregations and interpretations may use local vocabulary only under the BA4 ownership/trace boundary.

A tool may validate, complete, reject unknown tokens and propose corrections/extensions. It may not silently normalize an alias, mint an accepted term, alter a registry meaning or make LLM/NLP confidence into semantic authority.

## BA5 closure disposition

```text
BA5-T1    COMPLETED / PROVISIONAL PASS WITH CANONICAL-REFERENT-NAMING LOWER-BOUND
BA5-T2    COMPLETED / PROVISIONAL PASS WITH DOMAIN-SCOPED REGISTRY AND GOVERNED-EXTENSION REFINEMENT
BA5-T3    CLOSED / PASS
BA5       CLOSED FOR CURRENT THESIS SCOPE

normative synonym/alias registry       REJECTED AS UNNECESSARY
optional lexical/NLP assistance        DEFERRED
new BAE family                         NOT FORCED
new BA2 operator                       NOT FORCED
BA0 / BA1 / BA2 / BA3 / BA4 reopen    NOT TRIGGERED
```

## Base Analysis is not yet closed

BA0-BA5 are individually closed for the current thesis scope, but the complete Base Analysis milestone is **NOT YET CLOSED**.

Only BA6 may perform the integrated regression across the complete chain and close Base Analysis:

```text
governed documentation
 -> canonical controlled authoring
 -> accepted BA
 -> provenance/change continuity
 -> multiple projections
 -> governed change
 -> rebuild / re-analysis
```

BA6 must include the closed corpora and at least one structurally different holdout.

## Next authorized phase

> **BA6 - complete Base Analysis integrated regression and closure.**

Before executing BA6, define its smallest first bounded microstep against the now-closed BA0-BA5 contract. Do not begin downstream AnalysisRecord/Common Finding or formal STRIDE/STRIDE-AI schema work before BA6 closure.
