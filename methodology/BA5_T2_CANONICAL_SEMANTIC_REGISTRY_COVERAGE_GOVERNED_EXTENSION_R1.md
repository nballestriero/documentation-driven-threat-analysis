# DDTA BA5-T2 canonical semantic registry coverage and governed-extension pressure test - R1

**Status:** COMPLETED / PROVISIONAL PASS WITH DOMAIN-SCOPED REGISTRY AND GOVERNED-EXTENSION REFINEMENT

**Repository baseline tested:** `85622414b2ff52d58f3cd11776fef4b3753afc7d`

**Scope:** execute only BA5-T2 from Work Plan R20. Do not execute BA5 closure, BA6, AnalysisRecord/Common Finding, formal STRIDE/STRIDE-AI schema or ThreatForge implementation design.

## 1. Trial question

Can the exact-token/no-synonym discipline established for referent names in BA5-T1 cover the wider operative BA2 vocabulary and a realistic extension workflow without semantic loss or authority leakage?

The falsification target is stronger than simple lookup. T2 attempts to break the approach with:

- all thirteen BA2 operators;
- operator-scoped role contracts;
- semantic-kind keys;
- controlled values;
- colliding token strings across domains;
- aliases;
- genuinely new vocabulary;
- method-local terminology; and
- tool-assisted authoring.

## 2. Fixed inputs

T2 treats the following as closed dependencies rather than redesign targets:

```text
BA1: BAReferent + BAProposition

BA2 proposition:
  semanticOperatorKey
  participation(roleKey, term)
  polarity
  scopedModifier(condition | temporalScope)

BA3:
  provenance / derivation / continuity

BA4:
  projection trace + shared rendering
  method-owned interpretation remains downstream

BA5-T1:
  one canonical referent name per baseline/naming scope
  no normative referent aliases
```

## 3. Test A - thirteen operator keys

The complete current BA2 operator set is replayed under exact-token validation:

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

For each operator, the authoring contract requires the registered exact semantic key in the machine-significant binding.

Representative mutations:

```text
transfer <- send          REJECT alias
observe  <- read          REJECT alias
consumeService <- use     REJECT alias
realize  <- implement     REJECT alias
```

This does not forbid ordinary explanatory prose. It forbids a second normative semantic token from bypassing the registry.

**Result: PASS.** No synonym support is required.

## 4. Test B - operator-scoped role coverage

Every closed BA2 role contract is replayed. The decisive negative control removes the operator context.

Invalid abstraction:

```text
RoleRegistry:
  actor
  source
  destination
  result
  ...
```

Why invalid: BA2 role validity/cardinality is operator-scoped. A context-free row named `actor` does not tell the consumer whether it belongs to `produce`, `create`, `observe` or `transition`, and may hide different optionality/cardinality.

Accepted resolution:

```text
OperatorRoleRegistry entry key:
  (semanticOperatorKey, roleKey)
```

Representative examples:

```text
(transfer, source)
(transfer, destination)
(consumeService, provider)
(assignResponsibility, responsibilityKind)
(classify, semanticKind)
```

Mutation:

```text
(transfer, src)
```

is rejected rather than normalized to `(transfer, source)`.

**Result: PASS WITH REFINEMENT.** Canonical role enforcement must preserve operator context.

## 5. Test C - cross-domain token collision

A flat global namespace is deliberately attacked:

```text
project referent canonicalName = source
BA2 transfer roleKey           = source
```

If one global uniqueness constraint were used, this would be an artificial collision. Semantically it is not a collision: one token names a project referent, the other names a role in an operator contract.

Therefore:

```text
canonical uniqueness != repository-wide string uniqueness
canonical uniqueness = within the relevant registry domain/scope
```

**Result: PASS WITH REFINEMENT.** Flat global token namespace rejected.

## 6. Test D - semantic-kind coverage

T2 replays BA2 `classify`:

```text
classify
  classifiedReferent -> <BAReferent>
  semanticKind       -> <controlled method-neutral key>
```

Current evidence clearly supports exact tokens such as:

```text
store
contract
```

Mutation 1:

```text
repository
```

If its proposed normative meaning is the same as `store`, it is rejected as a synonym rather than admitted as a second key.

Mutation 2:

```text
channel
```

The term is familiar and was considered during BA1 category pressure, but T2 has no material evidence that current shared semantics cannot be represented without a distinct `channel` kind. It is therefore not promoted merely for convenience.

**Result: PASS.** `semanticKind` is an extensible canonical domain; `channel` remains DEFERRED / EVIDENCE-GATED.

## 7. Test E - controlled non-identifiable values

T2 tests whether controlled values can follow the same exact-token rule without turning every literal into vocabulary.

Closed BA2 examples:

```text
polarity:
  affirmative
  negative

scopedModifierKind:
  condition
  temporalScope
```

Responsibility semantics require a controlled `responsibilityKind` domain; current evidence includes:

```text
ownership
management
```

Mutation:

```text
owner
```

is not silently accepted as `ownership`.

Counter-control:

```text
constraintValue = 30s
```

A literal duration does not need a semantic registry entry merely because it is used in a proposition. Registry admission is for reusable controlled semantic distinctions, not every scalar/string value.

**Result: PASS WITH LOWER-BOUND REFINEMENT.** Domain-scoped controlled values are registries; literals are not registries by default.

## 8. Test F - registry revision mutability

Suppose the token `store` remains unchanged while its normative definition is edited in place.

Then:

```text
same BA baseline + token store
```

would not be enough to reconstruct which meaning a consumer used.

The mutation fails reproducibility.

Accepted rule:

```text
registry definitions/contracts
  -> immutable revision identity
```

A new registry revision may add an entry while preserving old entries, but old BA/materializations can still resolve the revision they consumed.

The T1 referent-name case already obtains immutability from the governed documentation baseline/naming scope.

**Result: PASS WITH REFINEMENT.** Immutable registry revision resolution is required.

## 9. Test G - genuinely new canonical term

T2 distinguishes five possible outcomes for an unregistered token.

### G1 - alias

```text
send ~= transfer
```

Reject new token; use `transfer`.

### G2 - method-specific term

```text
TrustBoundary
```

Keep it in the method/projection vocabulary. Do not promote to BA registry.

### G3 - independently identifiable project meaning

If the supposed "value" needs reuse/provenance/change identity, it becomes a `BAReferent`; it is not hidden in a controlled-value registry.

### G4 - genuinely new entry in an extensible domain

For example, a future corpus may force a new method-neutral `semanticKind` or `responsibilityKind` value. It requires an evidence-backed extension packet, governed acceptance and a new immutable registry revision.

### G5 - new closed-contract semantic construct

A genuinely new operator or role contract is not merely lexical. It changes BA2 semantics and therefore routes to the smallest BA2 reopen.

**Result: PASS.** The extension workflow prevents BA5 from bypassing BA1/BA2 boundaries.

## 10. Test H - exact path documentation -> BA -> projection

Representative shared binding:

```text
canonical referent: cameraIngresso
operator: transfer
roles:
  source      -> cameraIngresso
  destination -> recognitionProcessor
  content     -> recognitionCapture
```

A shared view retains the canonical referent names and inspectable BA keys.

A method projection may instead expose:

```text
projectionOwnedKind = DataFlowEndpoint
label = cameraIngresso
trace -> BA transfer/source
```

or create a genuinely method-owned aggregate/interpretation with its own label.

What it may not do is treat `sender` as an implicit BA `source` role or make a method category a new shared `semanticKind` without governance.

**Result: PASS.** BA4 freedom and BA5 strict canonical bindings coexist.

## 11. Test I - tool completion without semantic authority

A tool receives:

```text
semanticOperatorKey = transfer
```

It may deterministically offer:

```text
source
destination
content
```

from the accepted operator-role registry revision.

It may reject:

```text
src
recipient
payload
```

unless those tokens are registered in the relevant domain (they are not current BA2 role keys).

For an unknown `semanticKind`, it may show existing definitions and create a candidate extension request. It cannot decide that the unknown word is equivalent to an existing key or approve a new meaning.

**Result: PASS.** Tooling remains enforcement/assistance, not semantic authority.

## 12. Test J - authority and extension scope

T2 attacks the idea that every registry has the same lifecycle.

This collapses important distinctions:

- referent names are governed with the project baseline/naming scope;
- BA2 operators/roles/polarity/modifier kinds belong to the methodology contract;
- semantic-kind and other controlled-value registries may be extensible under their accepted method-neutral contract;
- projection-local terms belong downstream.

A single mutable project registry cannot legitimately redefine `transfer` or add a new BA2 role.

**Result: PASS WITH REFINEMENT.** Common validation discipline does not imply common authority/lifecycle.

## 13. Alias/synonym necessity check

T2 explicitly tries to force synonyms through:

```text
send / transfer
src / source
repository / store
owner / ownership
method label / shared BA key
```

Every case is representable by one of:

- use the existing canonical key;
- use free explanatory prose around a canonical binding;
- keep the term method-local;
- request a genuinely new evidence-backed registry entry; or
- reopen the correct semantic contract if the meaning is truly new.

No case requires a normative synonym table.

**Result: NO SYNONYM/ALIAS SUPPORT FORCED.**

## 14. Reopen pressure

T2 asks whether the wider registry requires semantic reopen.

```text
new BAE family                         NOT FORCED
new BA2 operator                       NOT FORCED
BA1 reopen                             NOT TRIGGERED
BA2 reopen                             NOT TRIGGERED
BA3 reopen                             NOT TRIGGERED
BA4 reopen                             NOT TRIGGERED
documentation metamodel reopen         NOT TRIGGERED
```

The fact that a future material new operator would trigger BA2 reopen is a routing rule, not evidence that BA2 currently fails.

## 15. Trial dispositions

```text
13 operator exact keys                                  PASS
operator-scoped role exact keys                         PASS WITH REFINEMENT
flat global registry namespace                          REJECTED
registry domain/context resolution                      REQUIRED
semanticKind controlled domain                          PASS
store / contract current canonical pressure             PASS
channel                                                  DEFERRED / EVIDENCE-GATED
polarity exact values                                    PASS
modifier-kind exact values                              PASS
responsibilityKind controlled domain                    PASS
literal value auto-registration                         REJECTED
immutable registry revision identity                    REQUIRED
alias candidate admission                               REJECTED
method taxonomy promotion                               REJECTED
governed extensible-domain extension                    PASS
closed BA2 contract mutation via BA5                     REJECTED
tool exact/context completion                           PASS
tool autonomous equivalence/approval                    REJECTED
synonym machinery                                       NOT FORCED
BA1-BA4 reopen                                          NOT TRIGGERED
BA5                                                      STARTED / NOT CLOSED
```

## 16. Result

BA5-T2 completes with:

```text
COMPLETED / PROVISIONAL PASS WITH
DOMAIN-SCOPED REGISTRY AND GOVERNED-EXTENSION REFINEMENT
```

The controlled-authoring hypothesis survives broader coverage. The decisive refinements are:

1. canonical registries are domain-scoped rather than one flat global namespace;
2. role keys require operator context;
3. registry meaning must resolve through immutable revisions;
4. semantic-kind/controlled-value content may be evidence-gated and extensible under governance;
5. closed BA2 operator/role semantics cannot be altered through BA5 lexical extension; and
6. aliases/synonyms remain unnecessary in the normative core.

BA5 is not closed by T2 alone.

## 17. Next smallest microstep

Execute one integrated BA5 closure review:

> **BA5-T3 - canonical registry, controlled-authoring and no-synonym closure review**

It should attempt to break the combined T1/T2 contract across referent renames, registry revisions, human/method projections, extension routing, current corpus examples and tool enforcement. If no material counterexample survives, close BA5 for current thesis scope and authorize BA6.
