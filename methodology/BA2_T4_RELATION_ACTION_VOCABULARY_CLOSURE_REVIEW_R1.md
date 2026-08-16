# BA2-T4 - Relation/action vocabulary closure review

**Revision:** R1

**Status:** CLOSED / PASS / BA2 CLOSED

**Repository baseline reviewed:** `d16743a6417196ebf53840b1210a645e9dda4245`

**Phase:** BA2 - Relations and canonical action vocabulary

**BA0:** CLOSED

**BA1:** CLOSED

**BA3:** NOT STARTED

## 1. Closure question

BA2-T4 asks only:

> Does the regressed R2 proposition/operator/role/modifier candidate preserve the methodology-neutral project meaning required by the current thesis corpora and bounded consumers without material counterexample, hidden method taxonomy, BA1 reopen or BA3 leakage?

The review is a closure decision, not a discovery pass. It must not add vocabulary unless a concrete counterexample forces it.

## 2. Evidence reviewed

The closure review reuses the already-governed evidence chain:

1. BA1 closed identity ontology: `BAReferent + BAProposition` only;
2. BA2-T1 explicit semantic operator plus n-ary role-bound participation lower bound;
3. BA2-T2 operator/role/modifier pressure test;
4. BA2-T3 systematic replay over facial-access and order-fulfillment;
5. the reduced R2 operator/role/modifier candidate;
6. the bounded STRIDE-oriented camera transfer consumer only as a neutrality/consumption probe.

No new source corpus, method-specific ontology or implementation schema is introduced by T4.

## 3. Exit criterion 1 - thirteen-key seed sufficiency and minimality

The R2 seed is:

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

### Adversarial merge review

The closure review attempts the remaining plausible merges:

- `transfer` into `produce`: **REJECTED**. Conveyance from source to destination is mechanically relevant and distinct from result production.
- `produce` into `create`: **REJECTED**. A governed result/output can be produced from existing meaning; creation specifically asserts establishment of new project-semantic identity/event occurrence.
- `observe` into `produce`: **REJECTED**. Observation must remain distinguishable from output production/state creation because consumers may need side-effect-free read/query semantics.
- `transition` into `constrain`: **REJECTED**. A state/lifecycle change is an asserted project fact, not merely a rule restricting admissible state.
- `correlate` into `reference`: **REJECTED**. Same-request/evaluation/operation identity matching is stronger than generic reference.
- `reference` into `dependOn`: **REJECTED**. Explicit pointing need not imply prerequisite semantics.
- `dependOn` into `consumeService`: **REJECTED**. A prerequisite can exist without actual service consumption; consumption preserves a responsibility-relevant interaction.
- `consumeService` into `assignResponsibility`: **REJECTED**. Use/consumption does not imply ownership or authority.
- `realize` into `classify`: **REJECTED**. Abstract-to-concrete realization is a relation between project meanings, not semantic-kind assignment.
- `assignResponsibility` into `classify`: **REJECTED**. Responsibility/authority is scoped relational meaning involving responsible parties, not an intrinsic kind.
- `constrain` into modifiers: **REJECTED** for governed/reusable rules because they require independent queryability and later provenance/change disposition.
- `classify` into role inference: **REJECTED** because semantic kind must remain reusable outside one proposition context.

No additional key is forced by the two corpora. No surviving key can be removed without losing a project-semantic distinction already required by reviewed evidence.

**Disposition:** `PASS / CURRENT-SCOPE MINIMUM ACCEPTED`.

## 4. Exit criterion 2 - operator-role/cardinality coherence

The R2 matrix is checked for three failure modes:

1. anonymous positional semantics;
2. method-specific role concepts;
3. silent dependence on authoring wording.

None is forced.

Roles such as source/destination/content, actor/result/input, subject/fromState/toState, correlatedItem/correlationContext, consumer/service/provider and responsibleParty/responsibilityScope/responsibilityKind are method-neutral descriptions of the proposition semantics they support.

Compatibility/cardinality remains operator-scoped. This prevents terms such as `source`, `target` or `context` from becoming globally ambiguous slots and prevents BA3 provenance `source` from colliding with transfer `source`.

The accepted cardinalities are current-scope contracts, not universal maxima. A future concrete corpus may reopen the smallest role contract if it requires widening or splitting while preserving method-neutral semantics.

**Disposition:** `PASS / ACCEPT`.

## 5. Exit criterion 3 - ownership/management merge

BA2-T3 merged `ownOrManage` into:

```text
assignResponsibility
+ responsibilityKind
+ polarity
```

The facial-access case still preserves both facts independently:

```text
consumeService(LocalConnectivity) = affirmative
assignResponsibility(project, underlyingTransport,
  ownership/management) = negative
```

Therefore service use does not collapse into ownership/authority and the responsibility boundary remains mechanically visible.

The merge reduces operator proliferation without losing project meaning.

**Disposition:** `PASS / MERGE ACCEPTED`.

## 6. Exit criterion 4 - polarity and modifier lower bound

Explicit polarity survives because negative semantics occur across both corpora and should not create `notX` operators.

The closure review retains only:

```text
condition
temporalScope
```

as embedded modifier kinds, subject to the promotion rule.

`condition` covers proposition-local applicability/guards. `temporalScope` covers proposition-local before/after/during/until semantics. If either becomes reusable, separately reviewable or participant-bearing, it is promoted to explicit referent/proposition semantics.

No current evidence requires a broader embedded modifier language.

**Disposition:** `PASS / ACCEPT`.

## 7. Exit criterion 5 - governed rules as explicit constraints

The closure review confirms the BA2-T3 reduction:

- incomplete delivery must not count as successful completion;
- atomic full-order reservation;
- concurrency exclusion;
- idempotent handling;
- all-or-nothing commitment;
- normalized provider/carrier result semantics;
- confidentiality, integrity and authorized provenance restrictions.

When these are governed or analytically relevant, they are independently queryable project rules. Encoding them as broad local modifier flags would weaken provenance, reuse and analysis selection.

They therefore belong in explicit `constrain` propositions (or another accepted explicit proposition where the semantics warrant it), not in a generic modifier bag.

**Disposition:** `PASS / ACCEPT`.

## 8. Exit criterion 6 - classification-as-proposition

Classification through `classify` remains preferable to an opaque intrinsic BAReferent type field because classification itself can later be grounded, derived, disputed, revised or superseded while the referent identity remains stable.

A universal semantic-kind taxonomy is not needed to close BA2. What is required is the registry contract:

- stable controlled method-neutral key;
- normative definition;
- mechanically consumable distinction;
- no STRIDE/DFD/tool-specific meaning;
- extension only when a consumer would otherwise need to reinterpret raw prose.

This preserves useful distinctions such as capability, information/resource or behavior/event without creating BA1 subtype families.

**Disposition:** `PASS / ACCEPT REGISTRY CONTRACT; UNIVERSAL ENUMERATION NOT REQUIRED`.

## 9. Exit criterion 7 - semantic key versus lexical label

BA2-T3 demonstrated that source predicates such as `deliver`, `send`, `submit`, `reads`, `queries`, `creates`, `records`, `maps`, `requestsCapture`, `confirmsHandoff` and others do not need to become BA operator keys one-for-one.

The closure rule is:

```text
source wording
    !=
BA semantic key
    !=
display label / synonym
```

Mapping from governed source to semantic key belongs to BA3 derivation mechanics. Display labels and authoring synonyms belong to BA5.

**Disposition:** `PASS / CLOSED`.

## 10. Exit criterion 8 - BA3 boundary

The following unresolved responsibilities are not defects in BA2:

- exact source locator representation;
- many-to-many source-to-BA derivation;
- grounded/derived/diagnostic origin state;
- assertion acceptance/rejection/stale/superseded lifecycle;
- baseline/equivalence/change identity mechanics;
- source-to-analysis and analysis-to-source traceability.

They are provenance/authority/lifecycle responsibilities explicitly allocated to BA3.

Likewise canonical display labels/synonyms are BA5 concerns and complete Base Analysis holdout regression is BA6.

**Disposition:** `PASS / NO BA3 LEAKAGE REQUIRED FOR BA2 CLOSURE`.

## 11. Exit criterion 9 - BA1 reopen test

No operator, role, polarity, modifier or semantic-kind value needs independent first-class project-semantic identity beyond `BAReferent` and `BAProposition`.

No subtype-specific invariant forces an `Action`, `Relation`, `Role`, `Participation`, `Information`, `State`, `Boundary`, `Store` or other new first-class BAE family.

**Disposition:** `PASS / BA1 REMAINS CLOSED`.

## 12. General logical-composition check

BA2-T1 left logical-composition language open. T4 checks whether this blocks closure.

Current evidence does not force a general logical-expression metamodel. Compound governed clauses can derive to multiple `BAProposition` assertions that share relevant `BAReferent` identities and later share provenance to the same source clause. N-ary participation preserves the atomic scope of each assertion; local condition/time, polarity and explicit constraints cover the reviewed conditional/negative/rule semantics.

A future concrete corpus may reopen BA2 if one atomic governed assertion cannot be preserved without an explicit logical-composition construct.

**Disposition:** `NOT REQUIRED BY CURRENT EVIDENCE / REOPEN ON MATERIAL COUNTEREXAMPLE`.

## 13. Bounded method-consumer confirmation

The camera-transfer consumer remains constructible from the closed candidate:

- delivery behavior via reusable behavior/event meaning and `transfer`;
- source/destination/content roles;
- `correlate` for RecognitionRequest;
- `consumeService` plus `assignResponsibility` for external transport responsibility;
- `realize` for Ethernet/Wi-Fi realization;
- `constrain` for completion and existing security properties;
- `classify` for method-neutral information/capability/behavior distinctions.

No DFD process/data-store/data-flow/trust-boundary root and no STRIDE category is required in Base Analysis.

**Disposition:** `PASS / METHOD NEUTRALITY PRESERVED`.

## 14. Closure decision

No material relation/action/role/modifier counterexample remains in the current thesis evidence. All remaining open responsibilities can be allocated honestly to BA3, BA5 or BA6 without weakening mechanical analysis consumption.

Therefore:

```text
BA2-T4    CLOSED / PASS
BA2       CLOSED FOR CURRENT THESIS SCOPE
BA1       REMAINS CLOSED
BA3       NOT STARTED
```

The canonical BA2 contract is `BA2_RELATION_ACTION_VOCABULARY_R1.md`.

## 15. BA2 reopen criteria

Reopen BA2 only for a concrete governed counterexample showing one of the following:

1. the accepted proposition shape cannot preserve an atomic project fact without hidden prose reconstruction;
2. no accepted semantic operator can preserve a required method-neutral distinction without semantic loss;
3. an accepted operator-role/cardinality contract cannot represent the governed participant structure and cannot be safely widened without changing semantics;
4. a required qualifier cannot remain local and cannot be represented through existing explicit propositions;
5. a general logical-composition construct is required by a concrete atomic governed assertion;
6. classification cannot supply reusable semantic kind without raw-prose reinterpretation;
7. a required BA2 distinction turns out to be method-specific and must be removed from the common core.

Do not reopen BA2 because a new label, diagram, database table, programming class or threat method would be more convenient.

## 16. Next authorized microstep

After this closure package is reviewed, committed, pushed and remotely verified, execute only:

> **BA3-T1 - source-to-Base-Analysis derivation and provenance lower-bound pressure test.**

Do not start BA4, formal threat-method overlays, Common Finding schema or implementation work.
