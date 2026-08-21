---
title: "DDTA BA5 canonical semantic registry and controlled-authoring contract - R1"
---

# DDTA BA5 canonical semantic registry and controlled-authoring contract - R1

**Status:** CLOSED BY BA5-T3 / ACCEPTED FOR CURRENT THESIS SCOPE
**R24 alignment note:** the BA5 canonical-registry/controlled-authoring contract remains retained. `BA6 NOT STARTED / NEXT PHASE` and `BA0 / BA1 / BA2 / BA3 / BA4 reopen NOT TRIGGERED` below are BA5 closure-time dispositions. R24 later reopened BA2 on concrete evidence without thereby reopening BA5. Current forward execution state is recorded in `DDTA_R24_DECISION_RULE_CHECKPOINT.md`.

**Closure baseline reviewed:** `8d8dae5f7c28d83b70cbdea090028e4ec0f93571`

**Closed dependencies:** documentation layer; closed BA0-BA4 contracts; BA5-T1 canonical referent naming; and BA5-T2 domain-scoped registry/governed-extension pressure test.

## 1. Closure statement

BA5 closes the minimum lexical and controlled-authoring boundary required by the current DDTA thesis evidence.

The closed position is intentionally strict:

```text
semantically operative DDTA position
    -> exact canonical token or canonical referent name

unregistered alias / synonym
    -> not normative semantic input

free explanatory prose
    -> may remain natural language
       provided it does not create a second semantic identifier/key
```

The result is a controlled semantic authoring contract, not a universal controlled natural language and not an NLP normalization layer.

For the current thesis scope, synonym/alias machinery is **NOT REQUIRED** in the normative DDTA core. Optional migration or authoring assistance may be studied later, but any such mechanism remains candidate-producing and cannot silently establish semantic equivalence.

## 2. Semantic-operability boundary

Canonical enforcement applies where a token carries DDTA semantics mechanically or governably, including:

- a governed shared referent name used as a semantic reference;
- a `semanticOperatorKey`;
- an operator-scoped `roleKey`;
- a controlled `semanticKind` key;
- a controlled semantic value such as polarity, modifier kind or a governed responsibility kind; and
- another future registry-controlled methodology-neutral value admitted under the extension rules below.

Canonical enforcement does **not** require every word in narrative prose to come from a DDTA dictionary.

Example:

```text
Human prose:
  The entrance camera sends the capture to recognition.

Semantically operative binding:
  transfer
    source      -> cameraIngresso
    destination -> recognitionProcessor
    content     -> recognitionCapture
```

The word `sends` may exist as human prose. It is not a second operator key and does not authorize `send` as an alias of `transfer`.

## 3. Closed registry lower bound

The smallest current-scope registry model is a logical set of domain-scoped registries:

```text
CanonicalSemanticRegistrySet                    [logical umbrella; NOT BAE]
|
+-- CanonicalReferentNameRegistry                [project-governed]
|    |- governedBaselineKey                 1
|    |- namingScopeKey                      1
|    `- canonicalName -> governed referent binding
|
+-- SemanticOperatorRegistry                     [BA2 contract-governed]
|    |- registryRevisionKey                 1 immutable
|    `- semanticOperatorKey -> normative BA2 meaning
|
+-- OperatorRoleRegistry                         [BA2 contract-governed]
|    |- registryRevisionKey                 1 immutable
|    `- (semanticOperatorKey, roleKey) -> BA2 role contract
|
+-- SemanticKindRegistry                         [method-neutral, extensible]
|    |- registryRevisionKey                 1 immutable
|    `- semanticKindKey -> normative method-neutral definition
|
`-- ControlledValueRegistry                 0..* [domain-scoped]
     |- valueDomainKey                       1
     |- registryRevisionKey                  1 immutable
     `- canonicalValueKey -> normative domain meaning
```

This is a semantic responsibility model. It does not require separate databases, graph node families, schema classes or ThreatForge tables.

Physical co-location is allowed if a consumer can mechanically recover domain, governing scope/authority, immutable revision where applicable, canonical key and normative definition/binding.

## 4. Domain-scoped resolution, not one flat namespace

Token equality across semantic domains does not establish semantic equality.

For example:

```text
project referent canonicalName = source
BA2 role                        = transfer/source
```

These may coexist because their lookup domains differ.

The closed rule is:

```text
same domain + same active scope/revision + same canonical token
    -> one unambiguous registry meaning/binding

same token in different domains
    -> allowed when domain resolution remains explicit
```

A universal flat token namespace is **REJECTED AS OVER-STRONG**.

## 5. Canonical referent naming

For one governed baseline and naming scope:

```text
one named shared project referent
    -> one exact canonicalName
```

Every governed semantic reference and every derived view that presents that same referent as shared project meaning uses the exact canonical name.

Example:

```text
cameraIngresso
```

is not silently interchangeable with:

```text
entryCamera
cameraEntrata
CameraIngresso
camera_ingresso
```

A view may add descriptive prose around the reference, but the machine-significant/shared entity identifier remains canonical.

### 5.1 Name is not semantic identity

The canonical name remains lexical metadata, not the `BAReferent` identity key.

```text
BAReferent semantic identity != canonicalName
```

A governed rename across baselines can therefore retain the same semantic identity under BA3:

```text
B0  canonicalName = cameraIngresso
B1  canonicalName = cameraNord

BA3 continuity = RETAIN
    when the independently reusable project meaning is unchanged
```

Historical B0 artifacts keep `cameraIngresso`; current B1 semantic references and rebuilt shared projections use `cameraNord`.

## 6. Canonical operator registry

The thirteen BA2 current-scope operator keys remain exact canonical keys:

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

An authoring word such as `send`, `deliver`, `read`, `use` or `owns` does not become an alternative operator key merely because it may express related natural-language meaning.

A material new method-neutral operator cannot be admitted through BA5. It requires the smallest BA2 reopen under the BA2 extension rule.

## 7. Operator-scoped roles

Role lookup is closed as:

```text
(semanticOperatorKey, roleKey)
```

Examples:

```text
transfer/source
transfer/destination
transfer/content

consumeService/consumer
consumeService/service
consumeService/provider

classify/classifiedReferent
classify/semanticKind
```

Aliases such as `src`, `dst`, `payload` or a context-free role dictionary are not normative replacements.

This preserves the BA2 rule that role validity and cardinality are operator-scoped.

A material role-contract change is a BA2 semantic change, not a BA5 lexical extension.

## 8. Semantic-kind registry

`semanticKind` remains a controlled, method-neutral and evidence-gated registry domain.

A registry entry requires:

1. a stable canonical key;
2. a normative method-neutral definition;
3. a distinction needed by reusable human/method consumers without raw-prose reconstruction; and
4. no method-specific meaning.

Current evidence includes kinds such as `store` and `contract`. The registry contract is closed, not a universal exhaustive taxonomy.

`channel` remains **DEFERRED / EVIDENCE-GATED**: familiarity or modeling convenience is insufficient to admit it. A concrete governed case must demonstrate a required shared method-neutral distinction.

A lexical alternative such as `repository` is not automatically a synonym for `store`. It is either rejected as an alias, or - if it denotes a genuinely different method-neutral concept - evaluated as a separate evidence-backed candidate.

## 9. Controlled-value domains

Reusable finite or governed semantic distinctions may use domain-scoped controlled registries.

Current examples include:

```text
polarity
  affirmative
  negative

scopedModifierKind
  condition
  temporalScope

responsibilityKind
  ownership
  management
  ... only governed evidence-backed extensions
```

Ordinary typed/local literals are not auto-registered:

```text
timeout = 30s
retryCount = 3
```

If a value requires independent reusable identity across propositions, projections or change, BA1 requires a `BAReferent` rather than registry inflation.

## 10. Immutable registry revision requirement

A semantic registry whose content or normative definitions can evolve resolves through an immutable revision identity.

```text
registry domain
+ registryRevisionKey
+ canonical token
    -> one inspectable normative meaning
```

This is required for reproducible historical interpretation. Reusing the same key with silently changed meaning is rejected.

Project referent names are instead anchored to the immutable governed documentation baseline and naming scope. Their history is handled through BA3 continuity and governed baseline history rather than by turning names into BA identity.

## 11. Governed extension workflow

An unknown proposed token is classified before admission:

```text
candidate token
    |
    +-- same meaning as an existing canonical token?
    |      -> REJECT alias
    |      -> use existing canonical token
    |
    +-- method-specific taxonomy / presentation term?
    |      -> keep downstream in projection/method
    |
    +-- meaning requires independent reusable identity?
    |      -> represent through BAReferent
    |
    +-- new method-neutral semanticKind or extensible value?
    |      -> evidence + normative definition + review
    |      -> new immutable registry revision
    |
    `-- new operator or role-contract semantics?
           -> smallest BA2 reopen
```

A tool or model may create an extension **candidate**, but acceptance is a governed methodological/project decision according to the relevant domain authority.

## 12. Projection boundary

BA4 method freedom remains intact.

When a projection renders a shared `BAReferent`, the canonical project name is preserved:

```text
[FlowParticipant]  cameraIngresso
[AssuranceSubject] cameraIngresso
```

`FlowParticipant` and `AssuranceSubject` may be projection-owned kinds.

A genuinely method-owned aggregation or interpretation may have a local label, for example:

```text
external-ingress-exposure
```

provided it remains explicitly method-owned, BA-trace-bound and is not presented as a replacement project name or BA semantic kind.

Method-local taxonomy does not enter the BA registry merely because several methods use similar words.

## 13. Tool-support boundary

A conforming tool may:

- validate exact tokens in their semantic domain;
- validate canonical referent names in the active baseline/scope;
- offer context-sensitive completion;
- reject duplicate/colliding names inside one naming scope;
- reject unknown operator/role/value keys;
- show the normative definition and immutable registry revision;
- propose an existing canonical token as an explicit correction; and
- create a candidate request for governed registry extension.

A conforming tool may not silently:

- treat an alias as equivalent;
- mint an accepted canonical term;
- alter an immutable registry definition;
- reinterpret a method term as shared BA semantics;
- change a closed BA2 operator/role contract; or
- turn LLM/NLP confidence into semantic authority.

ThreatForge, if used, remains one implementation/case-study instrument subject to this contract.

## 14. Cross-layer authority rule

The authority chain remains:

```text
governed project documentation / authoring registration
    -> accepted Base Analysis using closed semantic registries
        -> derived human/method projections
            -> downstream analysis findings
                -> governed documentation candidate
```

BA and tooling do not become project authority by enforcing canonical vocabulary.

A registry-owned normative BA meaning also does not make a methodology projection authoritative over BA.

## 15. No-synonym closure disposition

The integrated T1/T2/T3 pressure does not produce a material case that requires normative synonym support.

Therefore, for the current thesis scope:

```text
normative alias/synonym registry                 REJECTED AS UNNECESSARY
hidden lexical normalization                    REJECTED
automatic arbitrary-narrative migration         NOT REQUIRED
NLP/LLM semantic equivalence                    REJECTED AS AUTHORITY
optional assistive synonym/search mechanisms    DEFERRED
```

This is not a claim that synonyms do not exist in natural language. It is a design decision that portable-by-construction DDTA authoring does not need to admit them into the semantic contract unless later evidence falsifies the controlled-authoring hypothesis.

## 16. Closure invariants

1. **Canonical semantic input:** every semantically operative registry position uses an exact canonical token.
2. **Natural-language freedom outside bindings:** prose may remain natural language but cannot create a second normative semantic key or referent identifier.
3. **Domain-scoped resolution:** canonical tokens resolve within an explicit semantic domain and governing scope/revision.
4. **Referent-name consistency:** one named shared referent has one exact canonical name per governed baseline/naming scope.
5. **Name/identity separation:** canonical name is not BA semantic identity; BA3 continuity governs rename history.
6. **Operator stability:** BA2 operators remain exact closed keys; BA5 cannot extend them by aliasing.
7. **Role context:** role keys are interpreted under their operator contract.
8. **Evidence-gated extensibility:** semantic kinds and extensible controlled values grow only through governed evidence-backed revision.
9. **Literal restraint:** ordinary local literals do not inflate the registry.
10. **Projection separation:** method-local vocabulary remains downstream; shared referent rendering preserves canonical project naming.
11. **Tool non-authority:** tools may validate, complete and propose, never silently approve semantic equivalence or extension.
12. **Historical reproducibility:** evolving semantic registries resolve through immutable revisions; project renames remain baseline-historical.
13. **No synonym requirement:** normative aliases are absent unless a future material counterexample forces reopening.
14. **Representation independence:** registry responsibilities do not mandate a storage technology or class hierarchy.

## 17. Reopen criteria

Reopen only the smallest BA5 responsibility if concrete evidence demonstrates that:

1. a single shared referent needs two simultaneous normative identifiers in one baseline/naming scope to preserve required project meaning;
2. a required shared semantic binding cannot be authored or consumed with one canonical operator/role/kind/value without material semantic loss;
3. a methodology-neutral consumer requires synonym equivalence rather than an exact token plus projection-local presentation;
4. multilingual or accessibility needs cannot be satisfied with descriptive presentation while retaining one canonical semantic binding;
5. governed registry revision cannot preserve historical interpretation without lexical aliases;
6. the extension workflow cannot admit a genuinely new method-neutral concept without treating a synonym as normative; or
7. tool-independent reproducibility fails because exact canonical lookup is insufficient.

If the counterexample is actually a new operator/role semantic distinction, reopen BA2 rather than BA5. If it requires a new independently reusable identity family, apply the BA1 split criterion. If it is method-specific, keep it downstream.

Do not reopen BA5 merely because aliases, translations, fuzzy search or NLP would improve convenience.

## 18. Final closure disposition

```text
BA5-T1    COMPLETED / PROVISIONAL PASS WITH CANONICAL-REFERENT-NAMING LOWER-BOUND
BA5-T2    COMPLETED / PROVISIONAL PASS WITH DOMAIN-SCOPED REGISTRY AND GOVERNED-EXTENSION REFINEMENT
BA5-T3    CLOSED / PASS
BA5       CLOSED FOR CURRENT THESIS SCOPE

canonical referent name discipline             ACCEPTED
canonical semantic token discipline             ACCEPTED
domain-scoped registry resolution               ACCEPTED
immutable semantic registry revision            ACCEPTED
operator-scoped role lookup                     ACCEPTED
governed extension workflow                     ACCEPTED
normative synonym/alias registry                REJECTED AS UNNECESSARY
optional lexical assistance                     DEFERRED
new BAE family                                  NOT FORCED
new BA2 operator                                NOT FORCED
BA0 / BA1 / BA2 / BA3 / BA4 reopen             NOT TRIGGERED
BA6                                             NOT STARTED / NEXT PHASE
```

BA5 closure does not close Base Analysis as a whole. Only BA6 may perform the integrated Base Analysis regression and close the complete BA milestone for the current thesis scope.
