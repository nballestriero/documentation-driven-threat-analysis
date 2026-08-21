# DDTA minimal BAE identity ontology - R1

**Status:** CLOSED BY BA1-T3
**R24 alignment note:** BA1 identity semantics remain retained. Statements below that describe BA2 as `NOT STARTED / NEXT AUTHORIZED PHASE` are closure-time sequencing, not current execution state. Current R24 forward state is recorded in `DDTA_R24_DECISION_RULE_CHECKPOINT.md`; the active BA2 working revision is `BA2_RELATION_ACTION_VOCABULARY_R2.md`.

**Repository baseline reviewed:** `e88d7e220536863d564f9e3b9fac7f1592a8c440`

**Activation:** applies when the BA1-T3 closure package is accepted and committed.

**Authority note:** this artifact defines the minimal Base Analysis semantic identity boundary. Governed project documentation remains project authority.

## 1. Closed ontology statement

For the current thesis scope, the minimal first-class semantic identity ontology of Base Analysis contains exactly two families:

```text
BAReferent
BAProposition
```

`BAE` is an umbrella term for Base Analysis elements. BA1 does not require an additional `BAE` metaclass.

The two families are semantic distinctions. One implementation may materialize them in separate classes/tables, in one physical container with a discriminator, or in another representation, provided the closed semantic distinction is preserved.

## 2. `BAReferent` - ACCEPTED

A `BAReferent` is an independently identifiable unit of methodology-neutral shared project meaning that must be reusable across one or more analytical propositions, projections or governed baselines.

A BAReferent is not restricted to a concrete runtime object. Depending on governed project meaning, it may denote a participant, capability, information/resource concept, behavior/event, milestone, contract, store, boundary, state/context or another independently reusable semantic referent.

When project meaning must itself be reused, constrained, correlated, compared across baselines or targeted by multiple assertions, that meaning receives BAReferent identity.

## 3. `BAProposition` - ACCEPTED

A `BAProposition` is an independently identifiable methodology-neutral analytical assertion about one or more BAReferent identities, with enough independent identity to support assertion-level origin/provenance, diagnosis, reuse and change disposition.

A BAProposition is not the project-semantic thing it describes. If the underlying project meaning needs independent reuse or qualification, that meaning is represented as a BAReferent and propositions state the relevant semantics about it.

The exact internal structure of a proposition, its participation roles, arity, predicates, actions and cardinalities are not closed by BA1. They belong to BA2.

## 4. Why two identity families are necessary

Removing BAReferent would force propositions to point to raw source strings, document identities or ad-hoc duplicated concepts, weakening stable shared semantic identity, projection reuse and change-impact reasoning.

Removing BAProposition would force assertion-level origin, uncertainty and change disposition into properties of referents or into anonymous relation rows. The reviewed corpora require the same referent to survive while assertions about it are introduced, revised, superseded, retained or diagnosed. Reifying every assertion as an undifferentiated referent would merely rename proposition semantics rather than eliminate them.

Therefore semantic collapse into one undifferentiated family is rejected.

## 5. Domain kinds are not automatically first-class types

BA1 does not require dedicated first-class metaclasses for:

- Participant / Actor;
- Component / Capability;
- Information / Resource;
- Behavior / Event / Transition;
- Interface / Connection / Channel;
- Store / Persistence;
- Contract;
- Boundary / Externality;
- State / Mode / Context;
- Dependency / Allocation;
- Property / Constraint;
- DataFlow / Interaction.

A concrete meaning from any of these categories may still be represented as a BAReferent when independent identity is required.

Its category may be preserved through method-neutral classification, roles, values or propositions. BA1 intentionally does not freeze the exact classification vocabulary or cardinality.

## 6. First-class split criterion - CLOSED

A future dedicated BAE type/family is justified only when concrete evidence shows both:

1. **independent semantic identity** is required across propositions, projections or change; and
2. **reusable subtype-specific invariants** cannot be represented honestly as classifications, roles, values or propositions over the accepted families.

Recurring usefulness, familiar systems-modeling terminology, diagram convenience, programming classes, database tables or a method-specific category are insufficient by themselves.

## 7. Closed family-boundary invariants

1. **Two-family minimum:** Base Analysis preserves the semantic distinction between project-semantic referent identity and analytical assertion identity.
2. **Referent reuse:** independently reusable project meaning is represented through BAReferent identity.
3. **Assertion identity:** independently reviewable/provenance-bearing shared analytical claims are represented through BAProposition identity.
4. **No proposition proxy:** BAProposition is not required to serve as a proxy project referent; reusable project meaning receives BAReferent identity.
5. **Method neutrality:** neither family embeds STRIDE, STRIDE-AI, DFD or tool-owned semantic categories.
6. **Document separation:** governed document kinds remain source-layer concepts and are not copied into Base Analysis as BAE types by inheritance.
7. **Classification is cheaper than splitting:** method-neutral semantic kind or participation-role information does not create a new first-class type unless the split criterion is met.
8. **Representation independence:** the semantic family boundary does not mandate a programming class hierarchy, graph notation, database schema or persisted canonical graph.
9. **Authority preservation:** BAReferent and BAProposition identities do not make Base Analysis project authority; governed documentation remains authoritative.
10. **Phase separation:** relation/action structure is BA2; provenance/identity mechanics are BA3; projections BA4; vocabulary assistance BA5; implemented Base Analysis regression BA6.

## 8. Explicit non-types and downstream constructs

The following are not BA1 domain BAE metaclasses:

- document-layer roots/commitments: `MacroRequirement` and `Decision`;
- document-layer requirement types: `Requirement` and `FunctionalRequirement`;
- `SpecializedRequirement` (document layer);
- `SecurityRequirement` and `NormativeClause` (document layer);
- grounded, derived and diagnostic/unresolved origin/state categories;
- source locator or provenance record;
- view/projection;
- AnalysisRecord, Finding or Common Finding;
- ThreatForge implementation objects;
- STRIDE/STRIDE-AI/DFD elements.

Their relevant responsibilities remain source-layer, metadata, projection, analysis-envelope or later-phase concerns as already allocated by BA0 and the research work plan.

## 9. Correct interpretation of specialization

BA1 closure does not claim that all BAReferents are semantically identical.

A facial-access delivery behavior, a RecognitionCapture information concept, a PaymentProviderContract and an InventoryLedger can all be distinct BAReferents with different method-neutral classifications and different propositions.

The closure only says that current evidence does not require separate **first-class identity families** for those categories. BA2 may define roles/relations/classification mechanics needed to distinguish and consume them. A later concrete counterexample may reopen BA1 if classification is insufficient and a true subtype-specific invariant is required.

## 10. Reopen criteria

Reopen BA1 only for a material identity-ontology counterexample, for example:

1. a governed corpus requires a semantic kind with independent identity plus subtype-specific invariants that cannot be represented honestly over BAReferent/BAProposition;
2. a method-neutral consumer cannot construct its required projection without independently reconstructing a missing first-class semantic distinction from raw prose;
3. BA2 cannot define coherent proposition participation/role semantics without introducing an unacknowledged third identity family;
4. BA3 shows that assertion-level provenance/diagnosis/change cannot be attached coherently to BAProposition identity;
5. a concrete case proves BAProposition identity can be removed without losing any BA0 responsibility, materially falsifying the two-family lower bound.

Do not reopen BA1 merely because a dedicated subtype would make code, a diagram, a query or one analysis method more convenient.

## 11. Closure disposition

```text
BA1             CLOSED
BAReferent      ACCEPTED first-class semantic identity family
BAProposition   ACCEPTED first-class semantic identity family
BAE             umbrella term; no additional metaclass required
Domain splits   NOT REQUIRED by current evidence
BA2             NOT STARTED / NEXT AUTHORIZED PHASE
```
