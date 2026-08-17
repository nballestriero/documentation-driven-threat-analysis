# DDTA BA3 provenance/derivation lower-bound candidate - R1

**Status:** PROVISIONAL CANDIDATE AFTER BA3-T1 / NOT CLOSED / BA3 OPEN

**Derived by:** BA3-T1 source-to-Base-Analysis derivation and provenance lower-bound pressure test

**Repository baseline reviewed:** `97ad32fb427f808521f9fe13fb6901465ccfd715`

**Closed dependencies:** BA0 responsibility boundary; BA1 `BAReferent + BAProposition`; BA2 relation/action vocabulary.

## 1. Purpose

BA3-T1 asks for the smallest provenance/origin contract needed to connect the closed Base Analysis semantics to governed documentation without making Base Analysis a second project authority.

The lower bound is intentionally metadata-oriented. It does **not** add a third BAE identity family, define a database schema, define analysis records/findings, or solve the complete BA3 lifecycle problem.

## 2. Candidate lower-bound contract

Every accepted `BAReferent` and every accepted `BAProposition` must independently carry, or resolve to, an origin/provenance attachment with this semantic minimum:

```text
BAOriginAttachment                         [metadata contract; NOT a BAE family]
|- targetElement       1     BAReferent | BAProposition
|- governedBaselineKey 1     immutable baseline identity
|- originState         1     GROUNDED | DERIVED | DIAGNOSTIC_UNRESOLVED
|- sourceLink          0..*  -> GovernedSourceRef
|- derivationBasis     0..*  -> GovernedSourceRef | BAElementRef
`- derivationRuleRef   0..1  required for DERIVED

GovernedSourceRef
|- documentIdentity    1     governed document ID
`- locator             1     exact baseline-relative source anchor
```

`BAOriginAttachment` and `GovernedSourceRef` are semantic metadata contracts. They are not new `BAReferent`/`BAProposition` subclasses and do not imply any physical class/table/edge implementation.

## 3. Why provenance attaches to both BA1 identity families

`BAReferent` and `BAProposition` have different independent semantic identities.

A proposition can be grounded in one clause while its participating referents are supported across several clauses or document branches. Conversely, a referent can remain stable while propositions about it are introduced, revised, derived or diagnosed independently.

Therefore:

```text
provenance(BAProposition) does not imply provenance(BAReferent)
provenance(BAReferent)    does not imply provenance(BAProposition)
```

**Candidate invariant:** every materialized BA1 identity has independently inspectable provenance/origin metadata.

## 4. Many-to-many source derivation is required

The current corpora already force both directions:

```text
one governed clause/document unit
    -> zero, one or many BAReferents/BAPropositions

one BAReferent/BAProposition
    -> one or many governed source units
```

Examples:

- facial `FR-3.4` can support the delivery proposition, correlation proposition and reusable delivery behavior meaning;
- `RecognitionCapture` is reused across acquisition and delivery sources rather than duplicated per clause;
- the order-fulfillment physical handoff milestone is supported/reused across fulfillment, inventory and payment branches.

A single `sourceId` field on a BA element is therefore insufficient.

No separate reverse-link identity is required by the lower bound: a source-to-BA index may be computed from the same many-to-many provenance links.

## 5. Governed source locator lower bound

A source locator must permit exact drill-down to the governed material that justifies or localizes the BA element while avoiding a copied prose payload as a second authority.

The minimum contract is:

```text
governedBaselineKey
+ documentIdentity
+ locator
```

`documentIdentity` names the governed logical document or document unit (`D-3.4`, `FR-3.4`, `SR-3.4-C`, etc.). `locator` resolves the exact relevant source unit inside that baseline. A realization may use a clause ID, structured fragment identifier, repository path plus section anchor, URI, JSON pointer or another stable resolver.

The lower bound does **not** require line numbers, a source-text copy or a content hash. Those may be implementation hardening or UI aids, but they are not semantic authority.

A cached excerpt, when used, is non-authoritative display material; the governed source identified by the locator remains authoritative.

## 6. Baseline identity is required

Document identity and local locator alone are insufficient because the same logical source may change meaning across governed revisions.

The facial-access mutation family provides the direct pressure: a current interconnection realization can change from Ethernet to Wi-Fi while the logical Decision identity/area remains recognizable. A provenance pointer such as `D-3.5` without baseline context could silently conflate two different governed meanings.

Therefore every BA origin attachment is scoped to exactly one immutable governed baseline identity.

A Git commit SHA is an acceptable realization in the current repository, but Git is **not** mandated by the semantic contract.

The exact cross-baseline identity/equivalence rules for BA elements remain a later BA3 question.

## 7. Origin-state lower bound

BA0 already closes three responsibility-level origin states. BA3-T1 gives them minimum operational meaning.

### 7.1 `GROUNDED`

Meaning: the BA element states/denotes project meaning directly supported by governed documentation, although the BA representation may normalize wording into the closed BA1/BA2 semantics.

Minimum rule:

```text
originState      = GROUNDED
sourceLink       = 1..*
derivationBasis  = 0
derivationRuleRef= 0
```

Normalization such as source wording `deliver` -> semantic key `transfer` does not make the proposition `DERIVED` when the underlying meaning is directly stated by the governed source.

### 7.2 `DERIVED`

Meaning: the BA element adds methodology-neutral analytical structure that is justified by governed meaning but is not itself directly stated as a project commitment.

Minimum rule:

```text
originState       = DERIVED
derivationBasis   = 1..*
derivationRuleRef = 1
```

The basis may cite governed source references and/or already materialized BA elements. Its transitive lineage must terminate in governed source material from the same baseline.

A derived element may also carry `sourceLink` entries for direct contextual evidence, but those links do not convert the derived conclusion into a grounded project fact.

`derivationRuleRef` identifies an inspectable method-neutral normalization/inference rationale or rule. The exact rule registry and representation are **OPEN**; what is rejected is an unrecorded analyst/tool inference that cannot be reviewed.

### 7.3 `DIAGNOSTIC_UNRESOLVED`

Meaning: Base Analysis has localized conflict, ambiguity, missing information or insufficient basis and cannot silently choose a project-semantic answer.

Minimum rule:

```text
originState = DIAGNOSTIC_UNRESOLVED
sourceLink + derivationBasis >= 1
```

The diagnostic must point to the governed source area and/or BA meaning that creates the unresolved condition. It is accepted as an analytical diagnostic, **not** as a governed project fact.

The exact diagnostic-kind vocabulary and resolution lifecycle remain open.

## 8. Direct source authority versus derivation basis

A derived statement must preserve two different questions:

```text
Where is the project authority ultimately located?
        !=
What evidence/BA meaning was used to derive this analytical statement?
```

The source authority is always governed documentation. `derivationBasis` records the inputs to the analytical derivation; it does not promote those BA elements to project authority.

This distinction is required for source drill-down and for diagnosing why a derived classification/relation changes when one underlying source changes.

## 9. Facial-access replay

Illustrative provenance (identifiers and locator syntax are not implementation commitments):

```text
BAReferent RecognitionCapture
  baseline: <B0>
  state: GROUNDED
  sourceLink:
    - FR-3.3 / exact clause anchor
    - FR-3.4 / exact clause anchor

BAProposition P-FR34-transfer
  operator: transfer
  baseline: <B0>
  state: GROUNDED
  sourceLink:
    - FR-3.4 / delivery obligation anchor

BAProposition P-D34-responsibility
  operator: assignResponsibility
  polarity: negative
  baseline: <B0>
  state: GROUNDED
  sourceLink:
    - D-3.4 / transport-responsibility Decision anchor

BAProposition P-D35-realization
  operator: realize
  baseline: <B0>
  state: GROUNDED
  sourceLink:
    - D-3.5 / Ethernet realization anchor
```

A reusable semantic-kind classification may instead be derived:

```text
BAProposition P-classify-capture
  operator: classify
  classifiedReferent -> RecognitionCapture
  semanticKind       -> information-resource
  baseline: <B0>
  state: DERIVED
  derivationBasis:
    - RecognitionCapture
    - P-FR34-transfer
  derivationRuleRef:
    - <controlled method-neutral classification rule>
```

The classification can therefore be reviewed independently without pretending the source literally contained the BA semantic-kind key.

## 10. Multi-branch referent replay

The order corpus reuses the governed physical handoff milestone across fulfillment, stock issue and payment capture.

A single reusable BAReferent can therefore have several source links:

```text
BAReferent PhysicalHandoffMilestone
  baseline: <B0>
  state: GROUNDED
  sourceLink:
    - ADR-2.7 / stock-issue milestone
    - ADR-3.4 / payment-capture milestone
    - ADR-4.4 / physical-handoff definition
    - FR-4.4  / handoff confirmation behavior
```

This does not create four document-local BA referents merely to simplify provenance. Identity equivalence across wording remains BA1/BA3 governed semantic work, not a storage shortcut.

## 11. Negative control - method findings and tool state

Threat-method results and ThreatForge runtime state are not governed source provenance.

Rejected patterns:

```text
sourceLink -> STRIDE finding
sourceLink -> ThreatForge object id
GROUNDED proposition because a plugin inferred it
```

A method-specific finding may reference BA elements and governed source locators in its own downstream analysis record. If it motivates a documentation correction, only the accepted governed change can later ground new/revised BA meaning.

This preserves:

```text
analysis may diagnose/propose
        !=
analysis governs project truth
```

## 12. Acceptance/review state is not the same as origin state

BA3-T1 finds no current evidence requiring a complete per-element review/lifecycle state machine in the origin lower bound.

`GROUNDED`, `DERIVED` and `DIAGNOSTIC_UNRESOLVED` answer **where/how the analytical meaning originates**. They do not answer whether a BA element is newly proposed, accepted, rejected, stale, superseded or retired.

Those lifecycle/review questions are materially distinct and remain open for later BA3 pressure.

## 13. Lower-bound dispositions

```text
Provenance on BAReferent                         REQUIRED
Provenance on BAProposition                      REQUIRED
Independent provenance per BA1 identity          REQUIRED
Many-to-many source <-> BA mapping                REQUIRED
Immutable governed-baseline context              REQUIRED
Exact source drill-down locator                   REQUIRED
Copy of governed prose inside BA as authority     REJECTED
GROUNDED / DERIVED / DIAGNOSTIC_UNRESOLVED        REQUIRED
Derived analytical basis                         REQUIRED
Inspectable derivation rule/rationale reference  REQUIRED CANDIDATE
Exact derivation-rule registry                    OPEN
Per-element acceptance/review lifecycle           NOT CLOSED BY T1
Third BAE identity family for provenance           NOT FORCED
Method finding as governed source                 REJECTED
ThreatForge runtime state as governed source       REJECTED
BA1 reopen                                        NOT TRIGGERED
BA2 reopen                                        NOT TRIGGERED
BA3                                                STARTED / NOT CLOSED
```

## 14. Falsification rule

Revise this lower bound if a concrete governed corpus demonstrates that:

1. provenance on only one BA1 identity family is sufficient without losing source drill-down/revalidation;
2. one-to-one source provenance preserves the reviewed multi-source/multi-proposition cases without duplication or ambiguity;
3. a source locator without immutable baseline context cannot conflate revised meaning;
4. `grounded`, `derived` and `diagnostic/unresolved` can be collapsed without permitting silent inference authority or losing uncertainty localization;
5. a derived element can be reproducibly reviewed without an explicit basis/rationale; or
6. current requirements force provenance metadata to become a third project-semantic BAE identity family.

No reviewed evidence currently forces such a revision.

## 15. Explicit unresolved set after BA3-T1

BA3 remains open. The smallest unresolved set is:

1. cross-baseline identity/equivalence and retain/change rules for `BAReferent` and `BAProposition`;
2. accepted/rejected/stale/superseded/retired lifecycle and review semantics;
3. diagnostic resolution/replacement behavior after governed source correction;
4. exact derivation-rule/rationale registry and whether all derived cases need the same material form;
5. change-impact propagation and source-to-analysis / analysis-to-source feedback mechanics.

The next pressure target should attack the first three together using concrete baseline mutations rather than expanding the provenance schema.
