# BA3-T1 - Source-to-Base-Analysis derivation and provenance lower-bound pressure test

**Revision:** R1

**Status:** COMPLETED / PROVISIONAL PASS WITH LOWER-BOUND CANDIDATE / BA3 NOT CLOSED

**Repository baseline reviewed:** `97ad32fb427f808521f9fe13fb6901465ccfd715`

**Phase:** BA3 - Derivation, provenance and authority mechanics

**BA0:** CLOSED

**BA1:** CLOSED

**BA2:** CLOSED

**BA4:** NOT STARTED

## 1. Question and test discipline

BA3-T1 asks only:

> What provenance/origin information must exist on Base Analysis identities so that a consumer can reproducibly reach the governed source baseline, distinguish direct grounding from analytical derivation and unresolved diagnostics, and preserve many-to-many source lineage without making Base Analysis or an analysis tool project authority?

This is a lower-bound derivation. It does not close BA3 and does not design the complete lifecycle/change model.

## 2. Evidence basis

The test reuses only already-accepted evidence:

1. BA0 requires source/origin provenance, baseline-scoped identity, source drill-down, uncertainty localization, change-impact traceability and source-localized feedback;
2. BA1 accepts independent `BAReferent` and `BAProposition` identities, including assertion-level provenance pressure;
3. BA2 closes the proposition/operator/role semantics that provenance must annotate without redefining them;
4. facial-access provides direct grounding, reusable terms, consumed-service/responsibility/realization separation and explicit architecture mutations;
5. order fulfillment provides cross-branch reuse, correlation, provider normalization and a physical handoff milestone reused by several document branches;
6. S1.5 already established provenance != normative semantics, historical many-to-many analysis/change lineage and analysis != governance authority.

No new corpus or threat-method vocabulary is introduced.

## 3. Pressure A - attach provenance to propositions only?

Alternative A records provenance only on `BAProposition` and assumes participating referents inherit it.

This fails. `RecognitionCapture` participates in acquisition, transfer, constraints and classifications; its identity is supported across more than one source location. A particular transfer proposition can be grounded only in `FR-3.4`. The proposition's source set therefore cannot stand in for the referent's own lineage.

The reverse collapse also fails: source support for a referent does not establish the provenance of each independently reviewable assertion about it.

### Disposition

```text
Provenance only on BAProposition: REJECTED
Provenance only on BAReferent:    REJECTED
Independent origin metadata on both: REQUIRED
```

## 4. Pressure B - one source per BA element?

A one-to-one `sourceId` looks minimal but fails both directions.

One clause can normalize into multiple explicit BA propositions. Conversely, one reusable meaning can be supported by several document branches. The order physical-handoff milestone is a direct multi-branch pressure case.

### Disposition

```text
Single sourceId field: REJECTED
Many-to-many governed source <-> BA lineage: REQUIRED
Reverse source-to-BA queryability: REQUIRED CAPABILITY
Separate reverse-edge semantic identity: NOT REQUIRED
```

## 5. Pressure C - what must a source locator contain?

A locator must support exact drill-down but must not copy the source prose into Base Analysis as a competing authority.

`documentIdentity` alone may be insufficient when several governed units are stored in one artifact or when only one clause/section supports the semantic assertion. Line numbers alone are representation-fragile. A copied text excerpt can become stale and appear authoritative.

The lower bound is an immutable baseline context plus logical document identity plus an exact local resolver.

### Disposition

```text
governedBaselineKey: REQUIRED
documentIdentity:    REQUIRED
exact local locator: REQUIRED
source text copy as authority: REJECTED
line number as universal locator form: REJECTED
content hash: NOT FORCED
```

## 6. Pressure D - is baseline context really necessary?

Yes.

The facial mutation from Ethernet to Wi-Fi is enough to falsify an unversioned source pointer. A pointer that says only `D-3.5` can refer to materially different realization semantics in different governed revisions.

The lower bound therefore requires a baseline identity that cannot silently move.

Git commit SHA is a current realization, not a semantic requirement.

### Disposition

```text
Immutable governed-baseline identity: REQUIRED
Git as mandatory provenance mechanism: REJECTED
Cross-baseline BA identity rules: OPEN / LATER BA3
```

## 7. Pressure E - origin-state collapse

Could all BA elements simply be marked `source-traceable`?

No. That would erase the authority difference among:

- meaning directly supported by governed documentation;
- analytical structure inferred/normalized beyond what is directly stated;
- an unresolved diagnostic that explicitly refuses to choose project meaning.

The BA0 lower bound therefore survives materially.

### Disposition

```text
GROUNDED               REQUIRED
DERIVED                REQUIRED
DIAGNOSTIC_UNRESOLVED  REQUIRED
Generic traceable flag REJECTED
```

## 8. Pressure F - grounded does not mean verbatim

A danger is treating any normalization as derivation. That would make almost every BA proposition derived merely because BA2 uses canonical semantic keys rather than authoring verbs.

The better boundary is semantic:

- `GROUNDED`: the underlying project meaning is directly asserted by governed documentation, even if BA normalizes representation;
- `DERIVED`: the analytical statement adds method-neutral structure that is justified but not directly stated as a project commitment.

Therefore `deliver` -> `transfer` can remain grounded, while an inferred semantic-kind classification can be derived.

### Disposition

```text
Grounded == verbatim source syntax: REJECTED
Grounded == directly supported project meaning: ACCEPTED CANDIDATE
```

## 9. Pressure G - derived basis versus ultimate source authority

Recording only the ultimate source locators for a derived proposition is insufficient. A reviewer would know *where* the authoritative project meaning lives but not *how* the analytical conclusion was obtained.

Recording only BA-element parents is also insufficient if the chain cannot reach the governed baseline.

A derived element therefore needs:

1. explicit derivation basis;
2. an inspectable method-neutral derivation rule/rationale reference;
3. source lineage whose transitive closure reaches governed source material in the same baseline.

The exact derivation-rule registry is not closed by T1.

### Disposition

```text
Derivation basis: REQUIRED
Inspectable derivation rule/rationale reference: REQUIRED CANDIDATE
Ultimate governed-source lineage: REQUIRED
Silent analyst/tool inference: REJECTED
Exact rule registry: OPEN
```

## 10. Pressure H - multi-branch referent support

One reusable BAReferent must not be duplicated merely because several document branches support it.

The physical handoff milestone in the order corpus is reused by fulfillment, inventory and payment. Its provenance therefore holds multiple source links while its semantic identity remains one BAReferent if BA1 identity criteria say the meaning is the same.

The same principle applies to a facial-access term such as `RecognitionCapture` reused across acquisition and delivery.

### Disposition

```text
Duplicate referent per source branch: REJECTED
One referent + multiple source links: SUPPORTED / LOWER BOUND
Exact cross-wording identity/equivalence rules: OPEN / LATER BA3
```

## 11. Pressure I - does T1 need acceptance/review lifecycle?

Origin and review are orthogonal.

A `DERIVED` element may be accepted for analytical use; a `GROUNDED` element may later become stale after source change; a `DIAGNOSTIC_UNRESOLVED` item may itself be accepted as a valid diagnostic while not being accepted as project fact.

Therefore encoding `accepted/rejected/stale/superseded` into `originState` would overload one field and make change semantics ambiguous.

Current evidence forces the separation but not the complete lifecycle state machine in T1.

### Disposition

```text
originState == review/lifecycle state: REJECTED
Separate review/lifecycle dimension: FORCED AS FUTURE BA3 RESPONSIBILITY
Exact review/lifecycle vocabulary: OPEN
```

## 12. Pressure J - method finding or ThreatForge state as provenance?

Rejected.

A STRIDE finding, methodology-plugin result or ThreatForge runtime object can point to BA identities and source locators in its own analysis layer. It cannot serve as governed `sourceLink` for a grounded/shared BA project fact.

If downstream analysis motivates a change, governance must accept/change documentation first; the new governed source then becomes the authority for subsequent BA revalidation.

### Disposition

```text
Method finding as governed source: REJECTED
ThreatForge runtime object as source authority: REJECTED
Analysis result -> automatic BA project fact: REJECTED
Governed-document round trip preserved: PASS
```

## 13. Candidate lower bound

BA3-T1 retains this candidate:

```text
BAOriginAttachment
|- targetElement            1     BAReferent | BAProposition
|- governedBaselineKey      1
|- originState              1     GROUNDED | DERIVED | DIAGNOSTIC_UNRESOLVED
|- sourceLink               0..*  -> GovernedSourceRef
|- derivationBasis          0..*  -> GovernedSourceRef | BAElementRef
`- derivationRuleRef        0..1  [required for DERIVED; exact form OPEN]

GovernedSourceRef
|- documentIdentity         1
`- locator                  1
```

This is a semantic metadata contract, not a storage schema or new BAE family.

## 14. Bounded corpus replay

### 14.1 Facial access

The candidate can distinguish:

- grounded `RecognitionCapture` identity with more than one source anchor;
- grounded FR-3.4 transfer and correlation assertions;
- grounded D-3.4 negative responsibility placement;
- grounded D-3.5 Ethernet realization;
- derived classification without pretending the semantic-kind key was authored in the source;
- baseline-specific provenance so a later Wi-Fi realization is not conflated with the earlier Ethernet one.

### 14.2 Order fulfillment

The candidate can distinguish:

- one source clause yielding multiple normalized propositions;
- one `OrderEvaluation`/Reservation/payment meaning reused across several FRs;
- the physical handoff milestone with support from several MR branches;
- derived provider-normalization/classification semantics whose basis remains reviewable;
- source-to-BA reverse lookup for localized change impact.

No third identity family is forced.

## 15. BA0 responsibility check

```text
BA0-C1 authority/provenance boundary       PASS
BA0-C2 baseline-scoped identity            PASS / LOWER BOUND
BA0-C4 diagnostics/unresolved              PASS
BA0-C5 source drill-down                   PASS
BA0-C6 change-impact traceability          PASS / LIFECYCLE OPEN
BA0-C7 source-localized feedback            PASS / ANALYSIS LATER
BA0-C8 representation independence         PASS
```

## 16. Trial disposition

```text
Provenance target both BA1 families       REQUIRED
Many-to-many source lineage               REQUIRED
Baseline-scoped exact source locator       REQUIRED
Grounded/derived/diagnostic states         REQUIRED
Derived basis distinct from source authority REQUIRED
Derivation rule/rationale reference        REQUIRED CANDIDATE / EXACT FORM OPEN
Acceptance/review lifecycle                OPEN / LATER BA3
New provenance BAE family                  NOT FORCED
BA1 reopen                                 NOT TRIGGERED
BA2 reopen                                 NOT TRIGGERED
BA3-T1                                     COMPLETED / PROVISIONAL PASS
BA3                                        STARTED / NOT CLOSED
BA4                                        NOT STARTED
```

## 17. Explicit unresolved set

BA3-T1 does not close:

- cross-baseline identity/equivalence retention;
- stale/superseded/retired semantics after source change;
- accepted/rejected/review state;
- diagnostic resolution lifecycle;
- exact derivation-rule registry/materialization;
- full change-impact propagation and downstream analysis feedback lineage.

These are real provenance/lifecycle targets, not a license to expand BA2 semantics.

## 18. Next authorized microstep

Execute only:

> **BA3-T2 - cross-baseline identity, staleness and lifecycle pressure test.**

Use concrete governed mutations to attack retention/equivalence and stale/superseded/review semantics. Do not start BA4, formal threat-method overlays, Common Finding or implementation work.
