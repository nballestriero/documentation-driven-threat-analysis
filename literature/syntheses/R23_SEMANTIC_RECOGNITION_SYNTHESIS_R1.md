# R23 semantic recognition and review synthesis R1

**Status:** WORKING CROSS-SOURCE SYNTHESIS
**Prepared against DDTA baseline:** `87a612663d1e4827b7f67e83182838586e53d7ba`
**Scope:** R23 problem/domain/requirement/design-pattern reading pass and its implications for DDTA semantic review.

## 1. Synthesis question

R23 began by asking whether recurring problem/domain/requirements/security patterns could help DDTA recognize semantic situations before project documentation or Base Analysis freezes the wrong meaning.

The literature does not justify a mandatory DDTA pattern catalogue or an automatic classifier.

It does support a narrower and more useful conclusion: reusable problem/domain knowledge can help a reviewer propose candidate interpretations and critical differences, while project evidence and human review remain authoritative.

## 2. Strongest source-backed principles

### Structural and behavioural facts matter more than names

`SRC-0049` (Sutcliffe/Maiden, Domain Theory) supports classification/matching from structured application facts and critical-difference rules rather than names alone. It also preserves human confirmation/rejection and keeps unmatched facts visible.

DDTA inference: titles and capability names may be useful navigation labels, but they cannot close a semantic distinction that governed evidence leaves open.

### Near match and no-match are legitimate

`SRC-0063` (Jackson, Problem Analysis and Structure) treats recurring problem classes as analytical aids, not an exhaustive ontology. A near match may expose a separate difficulty rather than justify forcing the problem into a familiar frame.

DDTA inference: ambiguous, partial-match and no-match outcomes must remain valid review results.

### Problem meaning must remain distinct from solution progression

`SRC-0064` (Hall et al.) shows that architecture can inform problem analysis, but imported architecture must be explicit rather than silently treated as original problem fact.

`SRC-0065` (Li) distinguishes requirement-to-specification progression from matching/decomposition and shows that progression can rewrite context and introduce assumptions.

DDTA inference: semantic normalization must not silently introduce architecture, implementation assumptions or solution progression.

### Requirement-writing patterns do not solve semantic classification

`SRC-0058` (EARS) supports readable requirement syntax, but syntax does not determine whether the underlying responsibility was classified correctly.

`SRC-0056` (Withall, targeted sample) supports reusable requirement-authoring questions/pitfalls, not upstream semantic authority.

`SRC-0059` (Maiden et al.) applies patterns after a developed model to generate requirements text; it does not establish a document-to-semantics classifier.

DDTA inference: a well-formed requirement sentence can precisely encode the wrong semantic interpretation.

### Abstract security patterns are already conceptual solution knowledge

`SRC-0050` distinguishes application semantics from architecture and presents abstract security mechanisms. The material is useful for distinguishing security responsibilities, but these patterns are conceptual defences/mechanisms rather than neutral project facts.

DDTA inference: security patterns may suggest candidate questions but cannot be projected upstream as source authority.

### Design/integration pattern catalogues remain downstream

`SRC-0061`, `SRC-0062` and `SRC-0066` are useful comparison material for pattern anatomy, applicability, consequences and reusable solution structure.

DDTA inference: their vocabulary must not become hidden project ontology or be mistaken for problem semantics.

## 3. General DDTA synthesis

The working DDTA mechanism is:

```text
governed evidence
    ↓
minimal neutral responsibility reconstruction
    ↓
semantic sufficiency check
    ↓
materially different reading plausible?
   /                              \
 no                               yes
 ↓                                 ↓
continue                    observation scan
                                  ↓
                           candidate readings
                                  ↓
                           critical difference
                                  ↓
                           governed evidence
                         /                    \
                    sufficient             insufficient
                       ↓                       ↓
              clarify/place meaning        unresolved
```

The reviewer may inspect:

```text
A. Context / boundary
B. Participants / domains / relations
C. Initial / known / observable state
D. Events / activities / state transitions
E. Required effect / outcome / responsibility
F. Domain properties / constraints
```

These dimensions synthesize the reading pass for DDTA use. They are not claimed as a source-authored universal taxonomy and are not frozen as metamodel fields.

## 4. Critical differences are candidate-relative

R23 does **not** support a universal list such as:

```text
identification
verification
authentication
authorization
access decision
```

as general DDTA discriminators.

Those are domain-specific candidate interpretations for one pressure-test neighbourhood.

The general DDTA rule is instead:

```text
candidate A says X
candidate B says Y
        ↓
find the smallest materially important proposition where X != Y
        ↓
turn that proposition into a governed-evidence question
```

## 5. Authority boundary

Pattern/domain knowledge may:

- propose candidate interpretations;
- expose a likely critical difference;
- suggest a review question;
- explain known consequences or confusable cases.

It must not:

- create a governed requirement;
- create a project Decision merely because a catalogue distinguishes two patterns;
- create a BA referent/proposition/operator automatically;
- convert an inference into project fact;
- make catalogue completeness an assumption.

## 6. Base Analysis implication

The reading pass originally focused on pre-BA recognition.

R24 pressure testing adds a DDTA-specific inference: BA derivation itself can expose semantic choices that natural-language authoring hid.

This is **not** a direct literature claim from the R23 sources.

It is a candidate DDTA integration consistent with the existing governed documentation → BA → diagnostic → correction loop.

The post-BA back-check should look for:

- unsupported BA facts;
- choices between source-compatible interpretations;
- lost governed distinctions;
- source conflicts exposed by normalization;
- BA expressiveness limits.

BA remains diagnostic and downstream, never project authority.

## 7. Pattern-template conclusion

The original R23 plan expected a pattern-card/template candidate after synthesis.

Current evidence does not justify making such a template the next mandatory artifact.

The smallest justified next step is lighter:

```text
existing DDTA authoring
+ semantic sufficiency review
+ escalation only on material ambiguity
+ optional pattern/domain knowledge as candidate-generation aid
+ BA semantic regression back-check
```

A future pattern card may still be useful if repeated real cases show that a stable reusable structure reduces reviewer burden. It is no longer a prerequisite for resuming `MR-0003`.

## 8. Evidence limitations

- The registered R23 corpus contains full, partial, preview and access-limited sources; claims must remain bounded by the source notes actually read.
- The exact DDTA semantic-review integration is a researcher/method contribution, not something directly validated by Sutcliffe/Maiden or Jackson.
- Facial Access remains the originating real case and can bias method design.
- A controlled synthetic second case is exploratory only.
- The ThreatForge retrospective case uses historical documentation written before the current DDTA authoring method matured.
- Cross-LLM agreement supports reproducibility of one discriminator family but does not validate the method.
- More real authoring → BA → regression cycles are required before stable guide/thesis promotion.

## 9. R23 research-question disposition

| RQ | Working disposition |
|---|---|
| PAT-RQ1 problem recognition | reusable problem/domain classes can support review, but no exhaustive classifier is justified |
| PAT-RQ2 semantic discrimination | critical differences and structured facts are strongly useful as reviewer aids |
| PAT-RQ3 pattern anatomy | useful fields exist, but a mandatory DDTA pattern card is not yet justified |
| PAT-RQ4 authority boundary | pattern match remains non-authoritative and human-reviewed |
| PAT-RQ5 requirements authoring | writing patterns help expression after meaning is sufficiently governed |
| PAT-RQ6 thesis evidence | underlying principles are literature-backed; the exact DDTA integration still needs empirical pressure testing |

## 10. Next research use

Use this synthesis together with `methodology/DDTA_R24_SEMANTIC_REVIEW_CHECKPOINT_R1.md`.

Do not design a general pattern catalogue before resuming the real documentation/BA cycle.
