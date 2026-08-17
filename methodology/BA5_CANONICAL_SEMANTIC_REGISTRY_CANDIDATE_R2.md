# DDTA BA5 canonical semantic registry and controlled-authoring candidate - R2

**Status:** PROVISIONAL CANDIDATE AFTER BA5-T2 / BA5 OPEN

**Repository baseline reviewed:** `85622414b2ff52d58f3cd11776fef4b3753afc7d`

**Supersedes for active BA5 reasoning:** the R1 canonical-referent naming candidate. The R1 artifact remains immutable BA5-T1 derivation history.

**Closed dependencies:** documentation layer; BA0 responsibility boundary; BA1 `BAReferent + BAProposition`; BA2 proposition/operator/role/classification contract; BA3 provenance/continuity; BA4 projection contract; BA5-T1 canonical referent naming lower bound.

## 1. Purpose

BA5-T2 asks whether the strict T1 authoring rule can cover the wider operative Base Analysis vocabulary without introducing a synonym ontology or letting a tool decide semantic equivalence.

The starting rule remains:

```text
registered canonical token
    -> normative semantic authoring

unregistered alias / synonym
    -> not silently equivalent
```

T2 finds that the rule survives, but a single flat registry does not. Canonical tokens belong to semantic domains with different scoping, authority and extension rules.

## 2. Provisional R2 lower bound

The smallest current-scope registry model is a logical set of domain-scoped registries, not one universal token table:

```text
CanonicalSemanticRegistrySet                    [logical umbrella; NOT BAE]
|
+-- CanonicalReferentNameRegistry                [project-governed]
|    |- governedBaselineKey
|    |- namingScopeKey
|    `- canonicalName -> governed referent binding
|
+-- SemanticOperatorRegistry                     [BA2 contract-governed]
|    |- registryRevisionKey immutable
|    `- semanticOperatorKey -> normative BA2 meaning
|
+-- OperatorRoleRegistry                         [BA2 contract-governed]
|    |- registryRevisionKey immutable
|    `- (semanticOperatorKey, roleKey) -> BA2 role contract
|
+-- SemanticKindRegistry                         [method-neutral, extensible]
|    |- registryRevisionKey immutable
|    `- semanticKindKey -> normative method-neutral definition
|
`-- ControlledValueRegistry 0..*                 [domain-scoped, extensible where allowed]
     |- valueDomainKey
     |- registryRevisionKey immutable
     `- canonicalValueKey -> normative domain meaning
```

This is a semantic responsibility model. It does not require five databases, five files, graph node kinds or ThreatForge classes. Physical co-location is allowed when domain, scope, authority and revision remain mechanically recoverable.

## 3. Why one flat namespace is rejected

Token equality across domains does not establish semantic equality.

For example, a project might legitimately contain a referent named `source` while BA2 also uses `source` as the role of `transfer`.

```text
referent canonicalName = source
roleKey under transfer = source
```

Those tokens occupy different domains and must not collide or alias merely because their strings are identical.

Therefore uniqueness is domain-scoped:

```text
same domain + same active scope + same canonical token
    -> one registry meaning/binding

same token in different domains
    -> allowed when each domain resolution is unambiguous
```

A global token uniqueness rule is **REJECTED AS OVER-STRONG**.

## 4. Referent names retain the T1 rule

For a named shared project referent:

```text
one governed baseline / naming scope
    -> one exact canonicalName
```

The canonical name is project-governed lexical metadata, not BA identity. A governed rename may retain `BAReferent` identity through BA3 continuity.

Nothing in T2 weakens the T1 requirement that shared views use the same canonical referent name when presenting that shared entity.

## 5. Semantic operator registry coverage

All thirteen BA2 operator keys pass exact-token enforcement:

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

These tokens are not project-local synonyms. Their normative meaning belongs to the accepted BA2 methodology contract.

Examples:

```text
send            -> not an accepted semanticOperatorKey
transfer        -> accepted canonical key

usesService     -> not an accepted semanticOperatorKey
consumeService  -> accepted canonical key
```

Free explanatory prose may use natural language, but a machine-significant operator binding must resolve to the exact registered key. Hidden lexical mapping from `send` to `transfer` is not part of the BA5 core.

The operator registry is scoped to an immutable methodology/BA2 registry revision, not separately renamed by every project baseline.

## 6. Operator-scoped role registry

BA2 already rejects a context-free global role contract. T2 therefore rejects a flat role registry that stores `roleKey` without its operator context.

The canonical lookup key is conceptually:

```text
(semanticOperatorKey, roleKey)
```

Examples from the closed BA2 contract:

```text
transfer:
  source
  destination
  content

produce:
  actor
  result
  input

create:
  actor
  created

observe:
  actor
  observed
  result

transition:
  subject
  toState
  actor
  fromState

correlate:
  correlatedItem
  correlationContext

reference:
  referencer
  referenced

dependOn:
  dependent
  prerequisite

consumeService:
  consumer
  service
  provider

realize:
  abstract
  realization

assignResponsibility:
  responsibleParty
  responsibilityScope
  responsibilityKind

constrain:
  constraintTarget
  constraintValue

classify:
  classifiedReferent
  semanticKind
```

The same lexical role token may recur under more than one operator without implying a context-free contract. Cardinality and required/optional semantics remain BA2 responsibilities; BA5 requires exact contextual lookup rather than redefining them.

Alias attempts such as `src`, `dest`, `owner` or `kind` do not silently normalize to registered roles.

## 7. Semantic-kind registry

BA2 closes a registry contract but intentionally does not close a universal semantic-kind taxonomy.

BA5-T2 therefore separates two questions:

```text
Is semanticKind a controlled canonical domain?   YES
Is every possible semanticKind pre-enumerated?   NO
```

Current evidence gives clear exact examples such as:

```text
store
contract
```

These can be used as canonical `semanticKind` tokens when their normative method-neutral definitions are registered.

BA2 also discusses slash-form conceptual examples:

```text
party/person
information/resource
behavior/event
```

BA5-T2 does **not** silently turn this explanatory wording into canonical keys. Exact token admission must be explicit.

A useful-looking term such as:

```text
channel
```

is therefore **CANDIDATE / EVIDENCE-GATED**, not automatically accepted merely because `Interface / Connection / Channel` was discussed during BA1 ontology pressure. If a governed corpus needs a method-neutral `channel` distinction that existing kinds cannot preserve, it may enter the governed extension workflow below.

## 8. Controlled-value registry domains

Not every non-referent value should become a registry token. T2 preserves the BA1/BA2 distinction between controlled vocabulary and ordinary typed/local values.

A controlled-value registry is justified when a value is selected from a reusable semantic domain whose distinctions must be stable across authoring and consumers.

Current BA2 examples include:

```text
polarity:
  affirmative
  negative

scopedModifierKind:
  condition
  temporalScope

responsibilityKind:
  ownership
  management
  ... evidence-gated additional authority modes
```

For `polarity` and `scopedModifierKind`, the accepted BA2 contract already closes the exact current-scope values.

For `responsibilityKind`, BA2 requires a controlled domain but does not claim an exhaustive universal list. `ownership` and `management` are current evidence-backed values; new authority modes are admitted only through governance.

A literal such as a duration, number, URI, threshold or project-specific string does not become a canonical registry term merely because it appears in a proposition. If it needs independent reusable identity, BA1 promotes it to a `BAReferent`; otherwise it remains an appropriate typed/local value.

## 9. Registry revision identity

T2 finds that mutable registry meaning would break reproducibility even when the canonical token string stays unchanged.

Therefore any registry whose definitions/contracts can evolve requires immutable revision identity:

```text
same token
+ registry revision R1
    may not be assumed equivalent to
same token
+ registry revision R2
```

A registry revision may preserve all prior meanings while adding a new entry, but the used revision remains inspectable.

The referent-name registry is already anchored by an immutable governed documentation baseline/naming scope. BA2 contract registries and extensible semantic/value registries require equivalent immutable revision resolution.

This refines registry governance; it does not create a new BAE lifecycle. BA3 already assumes reproducibility under the same accepted semantic registries.

## 10. Exact-token path across documentation, BA and projections

The accepted path is:

```text
governed semantic authoring
  -> exact domain-scoped canonical token
      -> accepted BA binding
          -> projection trace / shared rendering
```

For example:

```text
referent: cameraIngresso
operator: transfer
role: transfer/source
kind: store
```

A human or method projection may use its own presentation/type vocabulary, but it must not rewrite the underlying shared key when claiming to expose shared BA semantics.

Allowed:

```text
[FlowParticipant] cameraIngresso
method-owned kind = DataFlowEndpoint
BA trace -> transfer/source -> cameraIngresso
```

Rejected:

```text
method label "sender"
  silently substitutes for BA roleKey source
```

Method-specific taxonomy remains projection-owned under BA4; it is not admitted into the BA registry merely because it is useful.

## 11. Governed extension workflow

When authoring needs an unregistered semantic token, the tool or author does not immediately add it.

The minimum decision path is:

```text
unregistered semantic need
    |
    +-- lexical alias of existing registered meaning?
    |      -> REJECT new entry
    |      -> use existing canonical token
    |
    +-- method-specific/projection-local meaning?
    |      -> keep downstream in projection/method registry
    |
    +-- independently reusable project-semantic identity?
    |      -> represent as BAReferent, not controlled local value
    |
    +-- new entry inside an already extensible method-neutral domain?
    |      -> candidate registry extension
    |      -> evidence + normative definition + non-equivalence check
    |      -> governed review
    |      -> new immutable registry revision if accepted
    |
    `-- changes a closed BA2 operator/role/polarity/modifier contract?
           -> smallest BA2 reopen candidate
           -> BA5 cannot smuggle it in as lexical metadata
```

This is the central T2 authority boundary.

## 12. Minimum extension packet

For an extensible `semanticKind` or controlled-value domain, an accepted new canonical entry requires at least:

1. `registryDomain` / `valueDomainKey`;
2. proposed exact canonical token;
3. normative methodology-neutral definition;
4. concrete governed evidence or integration need;
5. comparison against existing entries showing that it is not merely an alias;
6. confirmation that the meaning is not method-specific;
7. confirmation that independent BAE identity is not the actual missing requirement;
8. governed acceptance; and
9. publication in an immutable registry revision used by subsequent authoring/BA baselines.

The tool may assemble and validate this packet. It may not approve it as semantic authority.

## 13. Closed BA2 contract versus extensible registry content

T2 makes an important distinction:

```text
new semanticKind / controlled value
within an already open registry contract
    -> may be admitted by governed registry extension

new semanticOperatorKey
or changed operator-scoped role contract
or new polarity/modifier kind
    -> changes closed BA2 semantics
    -> smallest BA2 reopen required
```

This prevents BA5 from becoming a back door for modifying BA2.

A hypothetical new `publish` operator that is merely conveyance is rejected as an alias of `transfer`. If concrete evidence proves a distinct method-neutral action not representable by the thirteen accepted operators, that evidence belongs to BA2 reopen review, not an automatic vocabulary extension.

## 14. Tool-support boundary

A future tool may:

- validate exact tokens against the correct domain/revision;
- offer context-sensitive completion;
- after selecting `transfer`, offer only its accepted role keys;
- flag duplicate/colliding referent names inside the active naming scope;
- flag unregistered semantic kinds or controlled values;
- show normative definitions and registry provenance;
- classify an unregistered token as a candidate extension request;
- assemble evidence for human/governed review.

It may not:

- infer hidden synonym equivalence;
- pick a new canonical token and treat it as accepted;
- change an operator/role contract through a local project registry;
- promote method taxonomy into BA vocabulary;
- decide that a local value needs BAE identity; or
- mutate a registry definition in place.

ThreatForge remains an enforcement/integration instrument, never the semantic authority.

## 15. T2 mutation pressure

### V1 - operator alias

```text
send -> transfer
```

`send` is not accepted as a second normative operator token. Use `transfer` in the semantic binding.

Result: **PASS / ALIAS REJECTED**.

### V2 - role alias and context loss

```text
transfer/src
```

`src` is rejected. `source` is valid only through the `transfer` role contract. A context-free role lookup is insufficient.

Result: **PASS WITH DOMAIN/CONTEXT REFINEMENT**.

### V3 - same token in different domains

```text
referent canonicalName = source
transfer roleKey       = source
```

No collision exists because the registries are domain-scoped.

Result: **PASS; FLAT GLOBAL NAMESPACE REJECTED**.

### V4 - semantic-kind alias

```text
repository
```

If the proposed definition is materially the same as registered `store`, reject the new token as a synonym. If governed evidence shows a distinct method-neutral concept, process it as a new semantic-kind candidate rather than guessing from the word.

Result: **PASS**.

### V5 - candidate `channel`

`channel` is not admitted merely because it is a familiar systems term. No T2 evidence proves that current `BAReferent + classify + transfer/realize` semantics lose required shared meaning without it.

Result: **DEFERRED / EVIDENCE-GATED**.

### V6 - responsibility kind

`ownership` and `management` remain controlled values. A proposed `control` value must receive a normative distinction and evidence; it cannot enter as a loose synonym.

Result: **PASS**.

### V7 - genuinely new operator

A proposed operator whose meaning is not representable by the thirteen-key BA2 registry cannot be accepted through BA5 alone.

Result: **BA2 REOPEN PATH REQUIRED IF MATERIAL EVIDENCE SURVIVES**; no current reopen triggered.

### V8 - projection terminology

A method may display `DataFlowEndpoint`, `TrustBoundary` or another method-owned type while tracing to canonical BA keys. Those labels do not enter the BA registry.

Result: **PASS**.

### V9 - tool autocomplete

With `semanticOperatorKey = transfer`, the tool may offer `source`, `destination`, `content` from the immutable role contract. It may not offer `src` or invent another role based on usage frequency.

Result: **PASS**.

## 16. Reopen checks

No current T2 case forces a reopen of BA0-BA4.

- BA1: registry entries are not a third semantic identity family; independent identity still promotes to `BAReferent`.
- BA2: current operators/roles remain sufficient for the tested cases. The extension workflow explicitly routes a genuinely new operator/role back to BA2 rather than changing it silently.
- BA3: immutable registry revision resolution is compatible with its existing reproducibility assumption and does not add a project lifecycle.
- BA4: method-local taxonomy remains downstream; canonical BA token trace remains sufficient.
- Documentation metamodel: controlled authoring remains a cross-document governance constraint, not a new MR/Decision/FR/SR family.

## 17. Provisional dispositions

```text
strict canonical-token authoring                         REQUIRED
one flat global token namespace                          REJECTED
registry domain/context resolution                       REQUIRED
referent canonicalName baseline/naming scoped            REQUIRED
13 BA2 operator keys exact                               REQUIRED
operator role lookup as (operatorKey, roleKey)           REQUIRED
role alias/synonym normalization                          REJECTED
semanticKind as controlled extensible domain              REQUIRED
universal semanticKind taxonomy                           REJECTED / NOT FORCED
store / contract as current exact semanticKind evidence  ACCEPTED FOR T2 PRESSURE
channel                                                   DEFERRED / EVIDENCE-GATED
controlled reusable value domains                         REQUIRED WHERE APPLICABLE
literal/local value -> registry entry by default          REJECTED
polarity affirmative|negative                             ACCEPTED EXACT KEYS
modifier kind condition|temporalScope                     ACCEPTED EXACT KEYS
responsibilityKind controlled domain                      REQUIRED
ownership / management current values                     ACCEPTED FOR T2 PRESSURE
immutable registry revision resolution                    REQUIRED
alias candidate -> new registry entry                     REJECTED
method-specific term -> BA registry                       REJECTED
governed extensible-domain admission                      REQUIRED
new operator/role through BA5 extension                   REJECTED
material new operator/role -> smallest BA2 reopen         REQUIRED PATH
tool validation/context completion                        ALLOWED
tool semantic approval/equivalence                        REJECTED
new BAE family                                             NOT FORCED
BA1 / BA2 / BA3 / BA4 reopen                              NOT TRIGGERED
BA5                                                        STARTED / NOT CLOSED
```

## 18. Falsification rules

Revise this candidate if concrete corpus/integration evidence demonstrates that:

1. a normative alias must coexist with a canonical token in the same semantic domain to preserve necessary shared meaning;
2. role semantics cannot be resolved through operator-scoped canonical keys;
3. a flat registry is actually necessary for interoperability and domain separation loses required semantics;
4. a semantic-kind/controlled-value extension cannot be governed without turning the tool into authority;
5. immutable registry revisions are insufficient to replay the meaning used by an accepted BA baseline;
6. method projection semantics require method-specific taxonomy to enter the shared BA registry; or
7. the extension decision tree routes a genuine shared semantic need to the wrong layer.

Until such evidence exists, synonym/alias machinery remains unnecessary complexity.

## 19. Smallest unresolved set after BA5-T2

T1 and T2 now cover named referents, BA2 operators, operator-scoped roles, semantic kinds, controlled values, exact-token enforcement, extension governance and the tool authority boundary.

The smallest remaining BA5 task is an integrated closure review that tries to break the combined contract across:

- referent rename plus registry revision change;
- human and incompatible method projections;
- current facial/order examples;
- extensible versus closed registry domains;
- alias pressure; and
- tool completion/extension workflow.

If no material counterexample survives, BA5 may close for current thesis scope. Do not start BA6 before that closure is official.
