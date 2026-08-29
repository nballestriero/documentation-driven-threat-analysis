# DDTA research work plan after repository coherence audit - R24

**Status:** AUDIT GATE ACTIVE / BA6 INTEGRATED CLOSURE PROVISIONAL
**Prepared against repository baseline:** `8af2257a1df94fa5a83d4853ed0a1eb4d020c429`
**Project authority:** `FACIAL-ACCESS-GOV-R2`
**Facial Access BA:** `FACIAL-ACCESS-BA-R24-R1` — full Facial Access regression evidence retained
**BA6 integrated acceptance:** NOT YET COMPLETE
**Current audit:** `DDTA_R24_REPOSITORY_COHERENCE_AUDIT_R1.md`
**Commit:** BLOCKED pending audit-gate resolution
**Threat-method evaluation:** NOT STARTED
**Thesis substantive rewrite:** PAUSED

## 1. Why this plan supersedes the pre-audit forward state

The previous working draft assumed:

```text
BA6 complete
human-readable consolidation complete
next -> thesis chapter review
```

The repository coherence audit found that the BA5 closure had reserved additional mandatory evidence for BA6:

```text
structurally different holdout

and integrated regression:
governed documentation
 -> canonical controlled authoring
 -> accepted BA
 -> BA3 provenance/change continuity
 -> multiple BA4 projections
 -> governed change
 -> rebuild / re-analysis
```

The recent Facial Access BA6 work did not execute that entire gate.

Therefore the correct current state is:

```text
Facial Access BA regression
    PASS

BA2 R3 on Facial Access
    PASS

candidate BA6 contract
    AVAILABLE

BA6 integrated closure
    PROVISIONAL / INCOMPLETE
```

## 2. Frozen evidence to retain

Do not discard the work already completed.

Retain as valid evidence:

```text
FACIAL-ACCESS-GOV-R2

minimum justified BA rebuild

BA representation-pressure review

BA2 R3:
    transfer.behavior
    decisionRule.satisfies

full Facial Access BA

Facial Access post-BA regression PASS

AUTH-C / AUTH-P NOT SPECIFIED

human-readable guide content
    subject to BA6-status correction
```

## 3. Audit gate A — no commit yet

Until the BA6 acceptance issue is resolved:

```text
git add
git commit
git push
```

remain unauthorized for the current accumulated working tree.

Do not normalize the current status labels into repository history.

## 4. Audit gate B — complete BA6 integrated evidence

### B1 — holdout selection

Identify a **structurally different** case not used to design the current BA2 R3 refinements.

Selection criteria:

- enough governed/project evidence to build a BA honestly;
- structural difference from Facial Access;
- no need to invent implementation detail;
- useful pressure on BA0-BA5 responsibilities;
- provenance and change scenario can be exercised;
- avoid choosing solely because it trivially fits the current vocabulary.

Before adoption, record whether the candidate was previously used during BA design and therefore whether it is a genuine holdout or only a regression corpus.

### B2 — source pin

For the selected case record:

```text
authority status
source set
immutable revision/baseline
declared shared-analysis scope
known NOT SPECIFIED meanings
```

### B3 — source-first minimum BA

Construct the BA using current contracts without changing them first.

If the case cannot be represented:

```text
record concrete counterexample
identify smallest owning BA layer
pressure-review
reopen only if forced
```

### B4 — multiple BA4 projections

Produce at least two materially distinct downstream projections/views from the same accepted BA.

The projections must:

- preserve trace to BA;
- not redefine shared BA semantics;
- demonstrate selective/consumer-specific interpretation;
- avoid source reparsing as the semantic authority.

These do not have to be STRIDE and STRIDE-AI unless later deliberately selected; BA6 itself is methodology-integration validation, not threat-method effectiveness evaluation.

### B5 — governed change

Apply one governed change to the holdout/source baseline with explicit before/after identity.

Exercise:

```text
source change
 -> BA3 impact/revalidation context
 -> RETAIN / REPLACE / RETIRE
 -> rebuild affected BA
 -> rebuild/re-evaluate projections
```

### B6 — integrated regression

Regress the full chain:

```text
governed documentation
 -> canonical controlled authoring
 -> accepted BA
 -> BA3 provenance/change continuity
 -> multiple BA4 projections
 -> governed change
 -> rebuild / re-analysis
```

Only after this step decide whether BA6 is closed for the current thesis scope.

## 5. Audit gate C — current-state synchronization after BA6 verdict

Do not perform final synchronization before Gate B, because it would encode a provisional state as current truth.

After BA6 verdict, audit/update as needed:

```text
README.md
INDEX.md

candidate-r3/README.md
candidate-r3/corpus.manifest.yml
candidate-r3/DOCUMENTATION_GAPS.md

BA2 R3 status/alignment
BA3/BA4/BA5 forward alignment pointers
BA6 contract/checkpoint
Facial Access BA status label

Authoring Guide R3
Operational Guide R2
human-readable consolidation checkpoint
this work plan
```

Historical closure evidence remains unchanged.

## 6. Audit gate D — thesis coherence repair

After BA6 status is stable:

### D1 — thesis navigation

Update:

```text
thesis/README.md
thesis/outline.md
```

so they reflect the actual standalone/frozen chapter structure.

### D2 — Chapters 2-4

```text
Chapter 2
    semantic status: CLOSED / PASS
    action: forward-reference check only

Chapter 3
    semantic status: CLOSED / PASS
    action: no current semantic rewrite

Chapter 4
    semantic status: CLOSED / PASS
    action: editorial forward-state correction only
```

Do not alter `CHAPTERS_2_4_CLOSURE_R1.md`; it is historical closure evidence.

### D3 — old master

`thesis/latex/DDTA_tesi.tex` remains non-authoritative working history.

Do not patch it incrementally as the thesis source of truth.

Rebuild/integrate a thesis master later from reviewed standalone chapters.

### D4 — claim/evidence management

Consolidate current research evidence into:

```text
thesis/claims/claims.registry.yml
thesis/evidence/evidence.registry.yml
```

while preserving the distinction:

```text
method-development evidence
case-validation evidence
empirical hypothesis evidence
```

Do not treat one Facial Access case as proof of general empirical claims.

## 7. Audit gate E — thesis drafting

Only after Gates B-D:

1. freeze corrected thesis outline;
2. inventory remaining chapters;
3. distinguish:
   - finalizable before threat-method evaluation;
   - structurally draftable with evidence placeholder;
   - blocked by STRIDE/STRIDE-AI results;
4. draft/revise the next standalone chapter;
5. create a stable pre-threat-method thesis checkpoint.

## 8. Threat-method evaluation remains later

Do not run STRIDE / STRIDE-AI merely to satisfy BA6 unless the BA6 projection design deliberately and justifiably chooses them.

Final threat-method evaluation remains:

```text
same stable accepted BA
 -> STRIDE
 -> STRIDE-AI
 -> compare method-specific findings
 -> Common Finding / review
 -> governed feedback
```

It must not redefine the shared BA.

## 9. DG-FA-005 / lifecycle-test-code work remains deferred

The repository audit does not create a reason to pull lifecycle/test/code traceability into the current closure path.

Revisit only if later thesis evidence shows it materially contributes to the research questions.

## 10. Immediate next microstep

**HOLDOUT CANDIDATE INVENTORY ONLY.**

Before modifying BA6 artifacts:

1. inventory existing non-Facial-Access studies/corpora used during BA0-BA5 design;
2. identify which are disqualified as genuine holdout because they already shaped the contracts;
3. identify any structurally different unused candidate;
4. if no valid holdout exists, define the minimum new governed holdout case;
5. present the choice and rationale before executing it.

No current-state correction package, thesis rewrite or commit occurs in this microstep.
