# DDTA R24 — semantic sufficiency and BA regression checkpoint R1

**Status:** WORKING CHECKPOINT / CANDIDATE METHOD REFINEMENT / NOT METHOD CLOSURE
**Prepared against repository baseline:** `87a612663d1e4827b7f67e83182838586e53d7ba`
**Forward execution owner:** `DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R23.md`
**Carried-forward BA lower bound:** `DDTA_R24_DECISION_RULE_CHECKPOINT.md`

## 1. Purpose

This checkpoint freezes the research state reached after the R23 literature pass, the Facial Access semantic pressure test, cross-LLM replication, a controlled synthetic pressure test, and a retrospective ThreatForge pressure test.

It exists so project authoring and Base Analysis work can resume without prematurely freezing a new metamodel, a mandatory pattern catalogue, or a final thesis formulation.

This checkpoint does **not**:

- rename `MR-0003` or `IdentityVerification`;
- classify the Facial Access responsibility as identification, verification, authentication, authorization or access decision;
- modify governed Facial Access authority;
- add BA referents, BA propositions or BA2 operators;
- introduce a new documentation type;
- make pattern knowledge or LLM output project authority;
- close the final DDTA authoring syntax.

## 2. Research result carried forward

The strongest current finding is not a domain label. It is a review mechanism.

A project statement may be readable and internally coherent while still permitting materially different interpretations of the stable responsibility. Familiar labels can hide that instability.

The candidate DDTA refinement is therefore:

```text
normal progressive authoring
        ↓
semantic sufficiency review
        ↓
one stable responsibility?
   /                \
 YES                 NO
  ↓                   ↓
continue        semantic discrimination escalation
                       ↓
                 candidate readings
                       ↓
                 critical difference
                       ↓
                 governed evidence
                  /             \
             sufficient       insufficient
                ↓                 ↓
         clarify / place       unresolved
```

`semantic sufficiency review` is the normal lightweight check.

`semantic discrimination escalation` is activated only when a materially different reading is plausible. It is not a mandatory pattern-classification step for every MR.

## 3. General observation dimensions

The current literature-backed observation set is:

```text
A. Context / boundary
B. Participants / domains / relations
C. Initial / known / observable state
D. Events / activities / state transitions
E. Required effect / outcome / responsibility
F. Domain properties / constraints
```

These are **review dimensions**, not metamodel fields.

They are places to look when meaning is unstable. They must not be converted into six mandatory sections on every project document without further evidence.

Provenance, authority, uncertainty, conflict and missing information remain separate DDTA governance concerns rather than semantic dimensions.

## 4. Building a critical question without knowing it in advance

DDTA must not require the author to guess the correct domain-specific discriminator before review.

The candidate construction procedure is:

1. reconstruct the responsibility while temporarily ignoring suggestive titles and capability labels;
2. inspect only the semantic dimensions needed to understand that responsibility;
3. identify a relevant fact that is not sufficiently governed;
4. ask whether different values of that fact would produce materially different stable responsibilities, relations or outcomes;
5. if not, stop — the missing detail is not a semantic critical difference;
6. if yes, form the minimum competing readings needed to expose the contrast;
7. identify the smallest proposition on which the readings differ;
8. convert that proposition into a project-evidence question;
9. classify the evidence as `AFFIRMED`, `DENIED`, `NOT SPECIFIED` or `CONFLICTING`;
10. do not use an inference, title or pattern name to close the distinction.

Candidate interpretations may be linguistically ranked, but candidate preference does not equal semantic closure.

## 5. Placement rule

A critical difference does not automatically belong to an MR or Decision.

Use this working placement test:

```text
critical difference
        ↓
sufficient governed evidence?
        │
        ├─ NO → UNRESOLVED
        │
        └─ YES
             ↓
does evidence already determine the stable responsibility?
        │
        ├─ YES → clarify at the owning semantic level, normally MR if
        │         the fact changes the stable macro responsibility
        │
        └─ NO
             ↓
is there a genuine admissible project choice?
        │
        ├─ YES → Decision
        │
        └─ NO
             ↓
is the remaining detail operational input/condition/behavior?
                  ├─ YES → FR
                  └─ NO  → review again / unresolved
```

A Decision governs a genuine project commitment. It must not be invented merely to repair missing semantic evidence.

An FR operationalizes governed meaning. It must not silently select one macro interpretation because the higher-level documentation was ambiguous.

## 6. Base Analysis as a second semantic pressure test

Pre-BA review cannot be expected to discover every ambiguity.

The derivation of the minimum justified Base Analysis is therefore also a diagnostic projection.

```text
governed documentation
        ↓
pre-BA semantic sufficiency review
        ↓
minimum justified BA
        ↓
post-BA semantic regression back-check
        ↓
meaning still stable?
    /                 \
 YES                   NO
  ↓                     ↓
analysis          correction candidate
                         ↓
                  governed review
                         ↓
                 updated documentation
                         ↓
                      rebuilt BA
```

BA remains downstream and is **not** semantic authority.

The regression back-check asks at least:

1. **Provenance check** — does every materially important BA fact have sufficient governed support?
2. **Choice check** — did derivation have to choose between interpretations that the documentation did not distinguish?
3. **Neutral-label check** — after removing suggestive labels, do referents, relations and behaviors still reconstruct one coherent responsibility?
4. **Reconstruction check** — can materially different responsibilities be reconstructed from the same justified BA/source relation?
5. **Loss check** — did the BA discard a distinction that the documentation clearly governs?

Possible diagnostic outcomes include:

```text
ONE BA / ONE STABLE MEANING
MULTIPLE MATERIAL BA CANDIDATES
BA REQUIRES UNSUPPORTED FACT
BA LOSES GOVERNED MATERIAL DISTINCTION
BA EXPOSES SOURCE CONFLICT
```

A BA expressiveness problem must not be misreported as a documentation defect.

## 7. Pattern and LLM role

Current evidence supports pattern/domain knowledge as optional review knowledge:

```text
candidate generator
+ possible critical-difference hint
≠ project classifier
≠ requirement generator
≠ BA generator
≠ project authority
```

LLMs may be useful for:

- proposing alternative readings;
- proposing review questions;
- suggesting critical differences;
- checking whether evidence is affirmed, denied or absent.

Observed failure modes already include:

- leaking an inferred fact into a supposedly neutral reconstruction;
- overcommitting a placement/closure conclusion while later admitting insufficient evidence;
- anchoring on familiar labels when labels are visible.

Human/governed review remains required.

## 8. Pressure-test evidence status

The evidence is recorded separately in:

- `studies/semantic-review/R24_SEMANTIC_REVIEW_PRESSURE_TESTS_R1.md`
- `literature/syntheses/R23_SEMANTIC_RECOGNITION_SYNTHESIS_R1.md`

Current pressure-test set:

1. Facial Access — real current research trigger;
2. cross-LLM blind replication #1 — valid blind replication; grounded phase blocked;
3. cross-LLM replication #2 — blind plus grounded analysis; grounded phase carries a documented contamination caveat because an allowed guide contained Facial Access labels;
4. record-coherence case — controlled synthetic exploration only;
5. ThreatForge implementation-promotion case — retrospective real-project pressure test on historical documentation.

The set is promising but does not constitute general empirical validation.

## 9. What is currently justified

Current working judgement:

```text
new documentation type                NO
new mandatory MR fields               NO
new metamodel cardinalities           NO
mandatory pattern catalogue           NO
automatic pattern classification      NO
BA semantic-authority role             NO
BA2 operator change                    NO
lightweight semantic review            PROMISING
semantic escalation on material cases  PROMISING
post-BA semantic regression            PROMISING
human confirmation                     REQUIRED
```

The smallest justified methodological direction is a review discipline distributed across existing DDTA authoring and the existing documentation↔BA correction loop.

## 10. Forward-facing document synchronization

This checkpoint intentionally synchronizes forward-facing state without rewriting historical evidence.

After this checkpoint:

- `README.md` and `INDEX.md` point here for current R24 semantic-review state;
- `DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R23.md` remains the active work plan but is updated to the new execution sequence;
- `DDTA_R24_DECISION_RULE_CHECKPOINT.md` is retained as the BA2 lower-bound checkpoint and marked superseded for forward execution;
- `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R1.md` remains the active working authoring baseline; semantic sufficiency/regression is **not yet promoted** into its stable question set;
- `DDTA_AUTHORING_RULES_THROUGH_FR_R2.md` remains the thesis writing-contract baseline and carries only a pointer to this experimental refinement;
- thesis Chapter 4 is **not** substantively rewritten at this checkpoint. Its impact is tracked below until more real authoring/BA cycles have been pressure-tested.

Historical snapshots are not rewritten merely to make them look current.

## 11. Thesis impact ledger

Candidate future changes, not yet promoted:

| Candidate impact | Current status |
|---|---|
| Describe the hierarchy as progressive stabilization of governed meaning, not only progressive detail | TESTED PARTIALLY |
| Add semantic sufficiency review as a lightweight authoring/review discipline | TESTED PARTIALLY |
| Distinguish semantic clarification from genuine Decision commitments | TESTED PARTIALLY |
| Explain `NOT SPECIFIED != DENIED` and unresolved as legitimate outcomes | TESTED |
| Explain pattern knowledge as review knowledge, not authority | LITERATURE-SUPPORTED / DDTA INTEGRATION CANDIDATE |
| Explain BA derivation as a second semantic pressure test | NEW DDTA CANDIDATE / NEEDS MORE REAL CYCLES |
| Add a semantic-regression figure to Chapter 4 | NOT YET PROMOTED |
| Rewrite Chapter 4 authoring rules | DEFERRED |

Literature support for the underlying recognition principles is stronger than the evidence for this exact DDTA integration. The thesis must preserve that distinction.

## 12. Exact next execution sequence

Resume the Facial Access vertical slice; do not design another abstract template first.

```text
MR-0003 working documentation
    ↓
neutral responsibility reconstruction
    ↓
semantic sufficiency review
    ↓
is the critical entry-state fact already governed?
    ├─ NO  → keep unresolved / seek governed clarification
    └─ YES → clarify the correct owning level
                 ↓
          Decision only for a genuine project choice
                 ↓
          FR operationalization
                 ↓
          minimum justified BA
                 ↓
          semantic regression back-check
                 ↓
     discrepancy? → governed correction candidate → rebuild BA
                 ↓
          downstream analysis / test usefulness
                 ↓
          repeat on another real governed responsibility
                 ↓
only then consider promotion into stable guide/method/thesis wording
```

The immediate next microstep is therefore to return to the current `MR-0003` working project documentation and determine, from available project evidence rather than from the `IdentityVerification` label, whether the discriminating entry-state fact is governed, absent, conflicting or genuinely undecided.

Do not rename the capability during that microstep.
