# DDTA BA5 canonical referent naming and controlled-registry candidate - R1

**Status:** PROVISIONAL CANDIDATE AFTER BA5-T1 / BA5 OPEN

**Repository baseline reviewed:** `aa4b785dc72c2fbcd20fd04976e77fca3d07bf25`

**Closed dependencies:** documentation layer; BA0 responsibility boundary; BA1 `BAReferent + BAProposition`; BA2 semantic registries; BA3 provenance/continuity; BA4 projection contract.

## 1. Purpose

BA5-T1 replaces the initial synonym-first pressure with a stronger falsifiable authoring hypothesis:

> For project referents that are named in governed DDTA material, one exact canonical name is used across the governed baseline, accepted Base Analysis and every derived view that presents that referent as shared project meaning. Synonymous or alternative entity identifiers are not normative input.

The motivating example is deliberately simple:

```text
canonical project referent name:
  cameraIngresso
```

If `cameraIngresso` denotes one governed project referent, a second document or derived shared view does not rename it to `entryCamera`, `cameraEntrata`, `CameraIngresso` or another alias.

The purpose is not stylistic uniformity. The purpose is to make cross-document identity, projection comparison, source drill-down and tool integration mechanically reliable without requiring synonym resolution before the Base Analysis architecture itself has been fully regressed.

## 2. Provisional lower-bound rule

For one governed baseline and naming scope:

```text
one shared named project referent
    -> exactly one canonicalName token

same referent across governed documents
    -> same exact canonicalName

same referent exposed by accepted BA / shared projection rendering
    -> same exact canonicalName

alternative lexical identifier for same referent
    -> REJECTED as normative authoring
```

Exact means token equality under the declared project convention. Case or formatting variants do not silently alias:

```text
cameraIngresso
CameraIngresso
camera_ingresso
entryCamera
```

are distinct lexical tokens. Only the registered canonical token is accepted for the referent.

## 3. Name is not identity

The strongest negative control in T1 is a governed rename.

BA1 identity and BA3 continuity already establish that lexical wording does not define semantic identity. BA3 explicitly permits a `BAReferent` to RETAIN when the same independently reusable methodology-neutral project meaning survives a change in wording.

Therefore BA5 must not make:

```text
canonicalName == BAReferent identity
```

The current lower bound is instead:

```text
BAReferent semantic identity
    != canonicalName

canonicalName
    is baseline-scoped governed lexical metadata
    used consistently wherever that referent is named
```

Example:

```text
B0:
  same semantic referent R-camera-entry
  canonicalName = cameraIngresso

B1 governed rename:
  same semantic referent retained by BA3
  canonicalName = cameraNord
```

Historical B0 material remains `cameraIngresso`; current B1 governed documents, BA rendering and rebuilt shared projections use `cameraNord`.

A rename is therefore a governed lexical change, not automatically a new BAE identity.

## 4. Canonical-name registry responsibility

BA5-T1 requires a governed canonical-name registry responsibility, but does not mandate one physical database, JSON registry, graph node family or ThreatForge table.

The semantic minimum is:

```text
CanonicalReferentNameRegistry             [governed lexical responsibility; NOT BAE]
|- governedBaselineKey               1
|- namingScopeKey                    1
`- entry                             0..*
     |- canonicalName                1 exact token
     `- governedReferentBinding      1 unambiguous within baseline/scope
```

An accepted BA materialization must be able to resolve a named `BAReferent` to that canonical token without inventing a synonym.

The registry may be realized as governed authoring metadata, a generated validated symbol table over governed files, or another auditable mechanism. The physical realization is deferred.

## 5. Registry authority boundary

The registry does not make Base Analysis or ThreatForge project authority.

The authority chain remains:

```text
governed project authoring / canonical-name registration
    -> governed documentation baseline
        -> accepted BA materialization
            -> derived views
```

A tool may enforce or validate the registered name, but may not silently decide that an unregistered alias is equivalent.

If the author attempts:

```text
entryCamera
```

when the registered referent is:

```text
cameraIngresso
```

the minimum valid behavior is rejection or an explicit correction proposal. Automatic hidden alias normalization is outside the accepted T1 core.

## 6. Cross-document naming invariant

For a named referent, every semantic reference in governed DDTA documents uses the canonical token.

Allowed:

```text
The component `cameraIngresso` transfers ...
Decision D-X constrains `cameraIngresso` ...
FR-Y requires `cameraIngresso` ...
```

Rejected as an alternative identifier for the same referent:

```text
entry camera
cameraEntrata
CameraIngresso
```

Free explanatory prose may surround the canonical token, but an alternative phrase must not become a second machine-significant identifier for the same referent.

BA5-T1 does not attempt automatic migration of arbitrary legacy narrative prose.

## 7. Uniqueness lower bound

Two different shared referents in the same governed baseline/naming scope cannot resolve to the same canonical token.

```text
referent A -> cameraIngresso
referent B -> cameraIngresso
```

is rejected because consumers could not know which identity a source or projection reference denotes.

The lower bound therefore requires canonical-name uniqueness within a declared naming scope.

T1 does not yet freeze whether a future implementation uses one project-global namespace or explicit sub-namespaces. That is a representation/governance detail for later pressure if concrete projects require it.

## 8. Shared projection rendering

BA4 permits presentation labels that preserve shared meaning. BA5-T1 narrows that freedom for shared referent naming:

> A projection may choose its own layout, local item kind, grouping and method vocabulary, but when it displays a traced BAReferent as the shared project entity, it uses the referent's canonical name.

Allowed:

```text
[FlowParticipant] cameraIngresso
[AssuranceSubject] cameraIngresso
```

Here `FlowParticipant` and `AssuranceSubject` are projection-owned kinds; `cameraIngresso` remains the shared entity name.

Rejected when presented as the same shared entity:

```text
[FlowParticipant] Entry Camera
[AssuranceSubject] Ingress Sensor
```

The method may still create a genuinely method-owned interpretation item such as:

```text
external-ingress-exposure
```

provided that item is explicitly method-owned, trace-bound and not presented as a replacement name for `cameraIngresso`.

## 9. Aggregation and local method items

A projection-local item need not correspond one-to-one with a BAReferent. A method may aggregate several BA elements under a local analysis item.

In that case the local item may have a method-owned label because it is not claiming to be the canonical project entity.

The boundary is:

```text
label denotes shared BAReferent
    -> canonicalName required

label denotes projection-owned aggregation/interpretation
    -> local label allowed
       + BA trace required
       + must not masquerade as shared referent identity
```

This preserves BA4 method freedom without sacrificing shared entity naming consistency.

## 10. Operator, role and semantic-kind keys

BA2 already closes stable canonical semantic keys such as:

```text
transfer
consumeService
assignResponsibility
source
destination
content
store
contract
```

The same controlled-registry philosophy is compatible with those keys, but BA5-T1 does not reopen or redesign their registries.

T1 is intentionally limited to the referent-name boundary. The next BA5 pressure target may test whether the same exact-token/no-synonym authoring rule can cover the complete operative BA vocabulary and registry-extension workflow without semantic loss.

## 11. Tool-support boundary

The initial tool hypothesis is intentionally narrow.

A tool may:

- validate exact canonical-name use;
- prevent duplicate names in the active naming scope;
- offer completion from the accepted registry;
- flag an unregistered token;
- present a candidate correction or candidate registry-extension request.

A tool may not, by default:

- create a hidden synonym dictionary;
- silently map an alias to a canonical referent;
- mint a new accepted referent name without governance;
- use method taxonomy as a replacement project name; or
- make a lexical guess into project or BA truth.

This keeps ThreatForge or any future tool in an enforcement/assistance role rather than semantic authority.

## 12. Mutation pressure

### N1 - second document introduces an alias

```text
D1: cameraIngresso
D2: entryCamera
```

If both intend the same referent, `entryCamera` is rejected as normative authoring. The author must use `cameraIngresso` or perform a governed rename.

Result: **PASS**.

### N2 - case/format variation

```text
cameraIngresso
CameraIngresso
camera_ingresso
```

Only the registered exact token is accepted.

Result: **PASS**.

### N3 - derived human view renames the entity

```text
BAReferent -> cameraIngresso
view label -> Entry Camera
```

If the label claims to name the shared entity, reject it. A descriptive section heading may differ, but the entity reference itself remains canonical.

Result: **PASS**.

### N4 - method projection uses local type vocabulary

```text
FlowParticipant(cameraIngresso)
AssuranceSubject(cameraIngresso)
```

The local kind may vary while the entity name remains exact.

Result: **PASS**.

### N5 - governed rename across baselines

```text
B0 cameraIngresso
B1 cameraNord
```

If the same project meaning survives, BA3 may RETAIN referent identity while B1 adopts the new canonical name. Historical B0 remains unchanged.

Result: **PASS WITH REFINEMENT** - canonical name is baseline-scoped and must not be used as BAE identity.

### N6 - two referents request the same token

Within one naming scope, reject the collision or require distinct canonical names before the governed baseline is accepted.

Result: **PASS**.

## 13. Reopen checks

BA5-T1 finds no material reason to reopen closed BA responsibilities.

- BA1 remains sufficient: canonical naming is metadata over `BAReferent`, not a third identity family.
- BA2 remains sufficient: naming does not require a `nameOf` operator.
- BA3 already handles retained identity under wording/name change across baselines.
- BA4 remains sufficient: the new rule narrows permissible shared rendering labels but does not alter projection identity, coverage, trace or interpretation mechanics.
- The closed document metamodel need not be reopened: this is a cross-document controlled-authoring/governance constraint, not a new MR/Decision/FR/SR structural field family.

## 14. Provisional dispositions

```text
one named referent -> one canonicalName per baseline/scope       REQUIRED
exact canonical token in governed semantic references           REQUIRED
exact canonical token in shared derived referent rendering      REQUIRED
synonymous entity identifiers as normative authoring             REJECTED
case/format variants as implicit aliases                         REJECTED
canonical-name collision within naming scope                     REJECTED
canonicalName == BAReferent identity                              REJECTED
governed rename + BA3 RETAIN                                     PASS
projection-owned type/category labels                            ALLOWED
method-owned non-referent item labels                            ALLOWED DOWNSTREAM
tool exact validation/completion                                 ALLOWED
tool hidden synonym normalization                                REJECTED IN T1 CORE
new BAE family                                                   NOT FORCED
new BA2 operator                                                 NOT FORCED
BA1 / BA2 / BA3 / BA4 reopen                                    NOT TRIGGERED
documentation metamodel reopen                                   NOT TRIGGERED
BA5                                                              STARTED / NOT CLOSED
```

## 15. Falsification rules

Revise this candidate if concrete controlled-authoring/integration evidence demonstrates that:

1. one shared referent must have two concurrent normative names in the same baseline/scope to preserve necessary project meaning;
2. exact canonical naming makes a required methodology projection impossible rather than merely less convenient;
3. a canonical rename cannot be handled through existing BA3 continuity without semantic identity loss;
4. the registry cannot enforce uniqueness without introducing a missing shared identity responsibility;
5. method-specific labels must replace canonical entity names to preserve method semantics; or
6. a materially different corpus cannot be authored/integrated without synonym equivalence in the semantic core.

Until such evidence exists, synonym machinery remains unnecessary complexity.

## 16. Smallest unresolved set after BA5-T1

The next smallest BA5 question is no longer general synonym handling. It is registry coverage and extension:

1. test exact canonical authoring across operators, roles, semantic kinds and controlled values already closed by BA2;
2. define the minimum governed extension workflow when a genuinely new canonical term is required;
3. verify tool validation/completion can enforce the registry without becoming semantic authority; and
4. determine whether any concrete integration case forces aliases/synonyms despite the no-synonym default.

Do not start BA6 until BA5 is explicitly closed.
