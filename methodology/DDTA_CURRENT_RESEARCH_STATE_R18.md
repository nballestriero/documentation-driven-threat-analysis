# DDTA current research state - R18

**Prepared against repository baseline:** `85622414b2ff52d58f3cd11776fef4b3753afc7d`

**Purpose:** active semantic-state pointer after BA5-T2 canonical semantic registry coverage and governed-extension pressure testing; historical state/work-plan revisions remain immutable research history.

## Current semantic state

- Chapters 2-4: **CLOSED / FINAL for current thesis scope**.
- Documentation layer: **CLOSED**.
- BA0 responsibility/non-goals: **CLOSED**.
- BA1 minimal BAE identity ontology: **CLOSED**.
- BA2 relation/action vocabulary: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA3 provenance/derivation/identity/lifecycle/change-revalidation: **CLOSED FOR CURRENT THESIS SCOPE**.
- BA4 projections: **CLOSED FOR CURRENT THESIS SCOPE BY BA4-T3**.
- BA5-T1: **COMPLETED / PROVISIONAL PASS WITH CANONICAL-REFERENT-NAMING LOWER-BOUND**.
- BA5-T2: **COMPLETED / PROVISIONAL PASS WITH DOMAIN-SCOPED REGISTRY AND GOVERNED-EXTENSION REFINEMENT**.
- BA5 canonical semantic registry/controlled authoring: **STARTED / NOT CLOSED**.
- BA6 complete Base Analysis regression/closure: **NOT STARTED**.
- Formal STRIDE/STRIDE-AI overlay, AnalysisRecord and Common Finding: **NOT STARTED**.
- ThreatForge remains a case study/tool-support subject, never DDTA semantic authority.

## BA5 controlled-authoring hypothesis after T2

The normative semantic path uses exact canonical tokens rather than synonym normalization:

```text
registered canonical token
  -> normative semantic binding

unregistered alias / synonym
  -> reject or candidate extension review
  -> never hidden equivalence
```

T2 extends this discipline from referent names to the operative BA2 vocabulary.

## Domain-scoped registry lower bound

One flat global string namespace is rejected. The current provisional registry set is:

```text
CanonicalSemanticRegistrySet
|- CanonicalReferentNameRegistry
|- SemanticOperatorRegistry
|- OperatorRoleRegistry
|- SemanticKindRegistry
`- ControlledValueRegistry 0..*
```

These are semantic/governance responsibilities, not new BAE families or mandatory physical stores.

### Referent names

- exact canonical name per governed baseline/naming scope;
- canonical name is not BA identity;
- governed rename may retain referent identity under BA3.

### Operators

All thirteen BA2 operator keys remain exact canonical keys:

```text
transfer produce create observe transition correlate reference
dependOn consumeService realize assignResponsibility constrain classify
```

### Roles

Role lookup is operator-scoped:

```text
(semanticOperatorKey, roleKey)
```

A flat context-free role registry is insufficient because BA2 role validity/cardinality is operator-scoped.

### Semantic kinds

`semanticKind` is a controlled but extensible method-neutral registry domain. `store` and `contract` are current exact evidence used by T2. A familiar term such as `channel` remains **DEFERRED / EVIDENCE-GATED** until a governed case proves the distinction is necessary.

### Controlled values

Reusable semantic value domains use exact canonical keys where applicable. Current BA2 pressure includes:

```text
polarity: affirmative | negative
scopedModifierKind: condition | temporalScope
responsibilityKind: ownership | management | evidence-gated extensions
```

Ordinary literals are not registry entries by default.

## Immutable registry revisions

Registry definitions/contracts that can evolve require immutable revision resolution. A token string alone is insufficient if its normative definition can change.

The T1 referent-name registry obtains historical immutability from the governed documentation baseline/naming scope. BA2 contract and extensible semantic/value registries require equivalent immutable revision identity.

## Governed extension routing

For an unknown token:

```text
alias of existing meaning
  -> reject new entry; use canonical token

method-specific meaning
  -> projection/method local

meaning needs independent reusable identity
  -> BAReferent

new semanticKind/controlled value inside extensible contract
  -> evidence-backed governed extension
  -> new immutable registry revision

new operator/role/polarity/modifier contract
  -> smallest BA2 reopen candidate
```

BA5 therefore cannot become a back door for changing closed BA2 semantics.

## Tool boundary

A tool may perform domain/context-aware validation and completion, show definitions, flag unknown tokens and assemble extension requests.

It may not infer hidden synonym equivalence, approve new semantics, mutate registry definitions in place or promote method taxonomy into BA.

## T2 dispositions

```text
strict canonical-token authoring                         REQUIRED
flat global token namespace                              REJECTED
domain/context registry resolution                       REQUIRED
13 BA2 operator exact keys                               REQUIRED
operator-scoped role exact keys                          REQUIRED
semanticKind controlled/extensible domain                REQUIRED
universal semanticKind taxonomy                          NOT FORCED
store / contract current exact pressure                  PASS
channel                                                   DEFERRED / EVIDENCE-GATED
controlled value domains                                 REQUIRED WHERE APPLICABLE
literal auto-registration                                REJECTED
immutable registry revision resolution                   REQUIRED
alias/synonym normative entry                            REJECTED
method taxonomy -> BA registry                           REJECTED
governed extensible-domain admission                     REQUIRED
closed BA2 mutation through BA5                          REJECTED
tool context completion                                  ALLOWED
tool semantic equivalence/approval                       REJECTED
new BAE family                                           NOT FORCED
BA1 / BA2 / BA3 / BA4 reopen                            NOT TRIGGERED
BA5                                                       STARTED / NOT CLOSED
```

## Smallest unresolved set

T1/T2 now cover the registry pieces individually. BA5 requires one integrated closure review before BA6:

1. combine referent naming with operator/role/kind/value registries;
2. replay a governed referent rename together with registry revision change;
3. replay human and incompatible method projections without method-vocabulary leakage;
4. attack extension routing with alias, method-local, new-value and new-operator cases;
5. verify exact-token tool assistance without semantic authority; and
6. decide whether any concrete evidence forces synonym support.

## Next authorized microstep

Only after the BA5-T2 package is reviewed, committed, pushed and remotely verified, execute:

> **BA5-T3 - canonical registry, controlled-authoring and no-synonym closure review.**

Do not start BA6 or downstream analysis schemas before BA5 is explicitly closed.
