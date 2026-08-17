---
title: "DDTA BA5-T3 canonical registry, controlled-authoring and no-synonym closure review - R1"
---

# DDTA BA5-T3 canonical registry, controlled-authoring and no-synonym closure review - R1

**Status:** CLOSED / PASS

**Repository baseline reviewed:** `8d8dae5f7c28d83b70cbdea090028e4ec0f93571`

**Microstep:** `BA5-T3 - canonical registry, controlled-authoring and no-synonym closure review`

**Scope boundary:** this review closes BA5 only if the integrated T1/T2 contract survives adversarial pressure. It does not execute BA6, does not add a method schema and does not introduce ThreatForge implementation semantics.

## 1. Question under test

The closure question is:

> Can DDTA, for its semantically operative authoring surface, rely on exact canonical referent names and exact domain-scoped semantic tokens, with governed extension and tool enforcement, without normative synonym/alias machinery and without reopening BA0-BA4?

The burden of proof is on additional lexical machinery. Convenience is not sufficient evidence.

## 2. Inputs integrated by T3

T3 integrates:

- BA5-T1 exact canonical referent naming;
- BA5-T2 domain-scoped operator/role/kind/value registries;
- BA2 closed operator and operator-scoped role semantics;
- BA3 cross-baseline identity continuity;
- BA4 shared-rendering and method-owned interpretation separation; and
- the portable-by-construction documentation assumption already fixed by the project.

The review attacks the combined contract rather than repeating the individual T1/T2 trials.

## 3. Falsification matrix

The integrated attacks and dispositions are:

- **C1 - referent alias:** second normative identifier required -> **PASS; alias rejected**.
- **C2 - operator alias:** `send` required beside `transfer` -> **PASS**.
- **C3 - role alias:** `src` required beside `source` -> **PASS**.
- **C4 - semantic-kind alias:** `repository` required beside `store` for the same meaning -> **PASS**.
- **C5 - controlled-value alias:** `owner` required beside `ownership` -> **PASS**.
- **C6 - same token in two domains:** flat collision makes lookup unusable -> **PASS WITH DOMAIN-SCOPE**.
- **C7 - governed rename B0 to B1:** name must become BA identity/alias history -> **PASS WITH BA3 RETAIN**.
- **C8 - registry evolution:** historical semantics cannot be replayed -> **PASS WITH IMMUTABLE REVISION**.
- **C9 - ordinary human prose:** all prose must become controlled language -> **PASS WITH OPERABILITY BOUNDARY**.
- **C10 - incompatible projections:** local taxonomy must leak into BA -> **PASS**.
- **C11 - method-owned aggregation:** shared referent must be renamed -> **PASS WITH BA4 BOUNDARY**.
- **C12 - typed literal:** every local value must become registry vocabulary -> **PASS; literal remains local**.
- **C13 - genuine new semantic kind:** no extension path exists without synonyms -> **PASS WITH GOVERNED EXTENSION**.
- **C14 - material new operator/role:** BA5 must silently change BA2 -> **PASS; routed to BA2 reopen**.
- **C15 - tool/LLM alias suggestion:** suggestion must become truth -> **PASS; candidate only**.
- **C16 - translated/descriptive presentation:** second semantic identifier is unavoidable -> **PASS; binding remains canonical**.

No trial produces a material counterexample that forces normative synonym support.

## 4. C1 - referent alias attack

Start with:

```text
canonical project referent:
  cameraIngresso
```

Attack:

```text
D1 -> cameraIngresso
D2 -> entryCamera
human view -> Camera Ingresso
```

If all three intend the same shared referent, the additional identifiers are not admitted as normative semantic names. The author/view uses `cameraIngresso` for the semantic reference.

Descriptive prose can still say "entrance camera" around that reference.

**Result:** PASS. No alias registry is required.

## 5. C2/C3 - operator and role alias attacks

Canonical binding:

```text
transfer
  source      -> cameraIngresso
  destination -> recognitionProcessor
  content     -> recognitionCapture
```

Attacks:

```text
send
src
dst
payload
```

None is needed as a normative key. A human authoring interface may search for or suggest `transfer`, `source`, `destination`, `content`, but the persisted/accepted semantic binding remains exact.

**Result:** PASS.

## 6. C4/C5 - semantic-kind and controlled-value aliases

Attacks:

```text
repository  -> intended same meaning as store
owner       -> intended same responsibility meaning as ownership
```

When the intended meaning is already represented, the alternative token is rejected as a second normative key.

If `repository` actually denotes a materially different methodology-neutral concept, it is not treated as a synonym. It becomes an evidence-backed candidate under the semantic-kind extension rule.

**Result:** PASS. Lexical difference does not decide semantic difference.

## 7. C6 - cross-domain token collision

Attack:

```text
referent canonicalName = source
transfer roleKey        = source
```

A flat global dictionary fails here, but T2 already refined the hypothesis to domain-scoped resolution.

Lookup remains unambiguous because the two tokens resolve through different domains/scopes.

**Result:** PASS WITH DOMAIN-SCOPE REFINEMENT retained. No semantic collapse.

## 8. C7 - cross-baseline rename

Attack:

```text
B0  cameraIngresso
B1  cameraNord
```

If the independently reusable project meaning survives, BA3 can RETAIN the same `BAReferent` identity while the current baseline changes its canonical name.

Historical material does not need an alias bridge:

```text
B0 artifacts -> cameraIngresso
B1 artifacts -> cameraNord
continuity   -> BA3 RETAIN
```

**Result:** PASS. Name remains baseline-scoped lexical metadata rather than semantic identity.

## 9. C8 - semantic registry evolution

Attack: keep token `store` while silently changing its normative definition.

This would destroy historical reproducibility.

The closed answer is immutable registry revision resolution:

```text
SemanticKindRegistry@R1 / store
SemanticKindRegistry@R2 / store
```

If R2 changes meaning materially, the change is inspectable and historical BA continues to resolve R1. A semantic change cannot be hidden behind the same unversioned token.

**Result:** PASS WITH IMMUTABLE REVISION requirement retained.

## 10. C9 - natural-language pressure

A too-strong interpretation would require every sentence to use only canonical verbs and nouns. That is unnecessary and would convert BA5 into a controlled-natural-language project.

The smallest sufficient boundary is:

```text
human explanation
    may use natural language

machine-significant / governed semantic binding
    must use canonical registry key/name
```

For example "sends" in prose does not create a `send` operator when the semantic binding is `transfer`.

**Result:** PASS WITH OPERABILITY BOUNDARY. This is a minimization, not a relaxation of semantic consistency.

## 11. C10/C11 - projection incompatibility pressure

Two incompatible consumers may classify/render the same shared referent differently:

```text
FlowParticipant(cameraIngresso)
AssuranceSubject(cameraIngresso)
```

The projection-owned kinds differ while the shared referent name is stable.

A genuinely method-owned aggregation may instead use:

```text
external-ingress-exposure
```

because that label denotes a downstream method item rather than the shared referent. BA4 trace and interpretation rules preserve the boundary.

**Result:** PASS. Method terminology does not need to enter the BA registry.

## 12. C12 - literal inflation attack

Attack:

```text
timeout = 30s
```

Registering every local value would turn the registry into a universal value store. The controlled-value registry applies only to reusable governed semantic distinctions.

`30s` remains a typed/local value unless independent reusable semantic identity forces a `BAReferent` under BA1.

**Result:** PASS. Registry inflation is not required.

## 13. C13/C14 - extension routing pressure

### New method-neutral semantic kind

A genuinely new kind may be admitted only after evidence, method-neutral definition and review, producing a new immutable registry revision.

### New operator or role semantic

A materially new operator or changed role contract is not a lexical addition. It reopens the smallest BA2 responsibility.

Therefore BA5 cannot become a backdoor for semantic expansion.

**Result:** PASS.

## 14. C15 - tool/LLM authority attack

Attack:

```text
user writes: send
model confidence: 0.97 that send == transfer
```

Allowed behavior:

```text
"send is not a registered operator; did you mean transfer?"
```

Rejected behavior:

```text
silently persist transfer
or register send as an accepted synonym
```

The author/governance path decides accepted semantic binding. The model remains assistance, not authority.

**Result:** PASS.

## 15. C16 - translation/accessibility pressure

A human view may need explanatory or translated presentation.

This does not force a second normative semantic identifier. For example:

```text
Entrance camera (`cameraIngresso`)
```

may be presentation text while the underlying/shared semantic reference remains `cameraIngresso`.

If a downstream method owns a translated/local item rather than the shared referent, BA4 method-owned labeling applies.

**Result:** PASS. Translation support and semantic aliasing remain distinct responsibilities.

## 16. Cross-corpus closure reasoning

The two already reviewed project pressures remain compatible with the closed BA5 boundary:

- facial-access cases use stable named referents plus the closed BA2 operators/roles for transfer, correlation, service consumption, realization, responsibility and constraints;
- order, WMS and provider cases use stable referent naming plus dependency, service, responsibility and classification semantics and governed project-specific mappings without requiring a second normative lexical key.

T3 does not claim arbitrary prose migration. It asks whether intentionally analysis-ready governed documentation can preserve the shared semantics using canonical bindings. The reviewed cases do not falsify that claim.

A structurally different holdout remains reserved for BA6 integrated regression, as required by the work plan.

## 17. BA0-BA4 reopen review

### BA0
No authority/non-goal responsibility fails. Documentation remains project authority.

**Disposition:** NOT TRIGGERED.

### BA1
Canonical keys/names do not require a third BAE identity family.

**Disposition:** NOT TRIGGERED.

### BA2
No new operator or role is materially forced by T3. The existing extension rule remains adequate.

**Disposition:** NOT TRIGGERED.

### BA3
Cross-baseline rename and historical interpretation are handled by existing continuity/provenance responsibilities plus immutable registry revision references where applicable.

**Disposition:** NOT TRIGGERED.

### BA4
Shared rendering and method-owned interpretation remain separable. No projection counterexample requires method taxonomy to become BA vocabulary.

**Disposition:** NOT TRIGGERED.

## 18. What T3 explicitly does not claim

T3 does not claim:

- that natural language has no synonyms;
- that arbitrary legacy prose can be migrated automatically;
- that semantic-kind vocabulary is universally complete;
- that future projects can never force BA5 reopening;
- that translations or fuzzy search are useless;
- that an LLM cannot assist authoring;
- that ThreatForge determines canonical vocabulary; or
- that Base Analysis as a whole is closed.

It claims only that current DDTA evidence does not require normative synonym machinery in the semantic core when authoring is controlled by construction.

## 19. Closure decision

The integrated T1/T2 contract survives the T3 adversarial review without a material counterexample.

```text
BA5-T3       CLOSED / PASS
BA5          CLOSED FOR CURRENT THESIS SCOPE

synonym support in normative core      REJECTED AS UNNECESSARY
optional lexical/NLP assistance        DEFERRED
BA0-BA4 reopen                         NOT TRIGGERED
BA6                                    NOT STARTED / NEXT PHASE
```

The final BA5 contract is recorded in the companion R1 contract artifact included in this package.

## 20. Next boundary

BA5 closure authorizes BA6 as the next phase, but this microstep does **not** execute it.

BA6 must regress the complete BA0-BA5 design through the integrated chain:

```text
governed documentation
 -> canonical controlled authoring
 -> accepted BA
 -> BA3 provenance/change continuity
 -> multiple BA4 projections
 -> governed change
 -> rebuild / re-analysis
```

Only BA6 may close the complete Base Analysis milestone for the current thesis scope.
