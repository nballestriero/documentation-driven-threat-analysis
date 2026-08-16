# DDTA current research state - R8

**Prepared against repository baseline:** `4d832bcf90109106d543029cb517be32a6fe7ea7`

**Purpose:** active semantic-state pointer after BA2-T3 cross-corpus regression and reduction; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0-R systems-modeling prior-art research: **CLOSED**.
- BA0 responsibility and non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- `BAReferent`: **ACCEPTED**.
- `BAProposition`: **ACCEPTED**.
- BA2-T1 proposition shape/participation lower-bound derivation: **COMPLETED / PROVISIONAL CANDIDATE**.
- BA2-T2 operator/role/modifier vocabulary pressure test: **COMPLETED / PROVISIONAL PASS WITH VOCABULARY-ARCHITECTURE REFINEMENT**.
- BA2-T3 cross-corpus regression: **COMPLETED / PROVISIONAL PASS WITH REDUCTION**.
- BA2 relations and canonical action vocabulary: **STARTED / NOT CLOSED**.
- BA3 provenance/authority mechanics: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## Active BA2 structure

```text
BAProposition
|- semanticOperatorKey   1
|- participation         1..*
|    |- roleKey          1
|    `- term             1
|- polarity              1
`- scopedModifier        0..*
```

The active reduced vocabulary candidate is `BA2_SEMANTIC_VOCABULARY_CANDIDATE_R2.md`.

## BA2-T3 reductions

- operator-family facet: **REMOVED FROM NORMATIVE CORE**;
- seed operators: **REDUCED 14 -> 13**;
- `ownOrManage`: **MERGED** into `assignResponsibility` using `responsibilityKind` and polarity;
- no missing method-neutral operator: **FORCED = NONE**;
- `input` role under `produce`: **ADDED / FORCED BY REGRESSION**;
- `responsibilityKind` under `assignResponsibility`: **ADDED / FORCED BY MERGE**;
- semantic-key/source-lexical separation: **PASS**;
- explicit polarity: **RETAIN**;
- embedded modifier lower bound: `condition` + `temporalScope` only;
- completion/failure, atomicity, concurrency and idempotency: **PROMOTE TO `constrain`** when governed/analytically relevant;
- classification-as-proposition: **RETAIN**;
- fixed exhaustive semantic-kind taxonomy: **NOT REQUIRED**;
- third BA1 identity family: **NOT FORCED**.

## Reduced operator seed

```text
transfer
produce
create
observe
transition
correlate
reference
dependOn
consumeService
realize
assignResponsibility
constrain
classify
```

The list is still **CANDIDATE / NOT CLOSED** until BA2-T4.

## Classification boundary

Base Analysis requires controlled semantic-kind keys and `classify` propositions so consumers do not reconstruct reusable semantic kind from raw prose. BA2-T3 rejects a fixed universal systems-modeling taxonomy as a current-scope requirement. Registry labels/synonyms remain separate from semantic identity.

## Method-consumer boundary

The bounded camera-transfer STRIDE projection remains constructible from transfer, correlation, service-consumption/responsibility, realization, constraint and classification semantics without importing DFD/STRIDE categories into Base Analysis.

## Smallest unresolved set

The remaining work is a closure decision over the regressed R2 candidate, not another discovery pass:

1. thirteen-key seed;
2. operator-role/cardinality matrix;
3. responsibility/ownership merge;
4. polarity and narrowed modifier contract;
5. semantic-kind registry contract without universal enumeration;
6. BA1/BA3 boundary check.

## Next authorized microstep

Execute only:

> **BA2-T4 - relation/action vocabulary closure review over the regressed R2 candidate.**

Do not start BA3, formal threat-method overlays, Common Finding or implementation work.
