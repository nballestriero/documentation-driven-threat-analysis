---
title: "DDTA research work plan after documentation-layer closure - R24"
---

# DDTA research work plan after documentation-layer closure

**WORK PLAN - REVISION 24**

**Status:** ACTIVE R24 WORK PLAN — FACIAL ACCESS SUCCESSOR COMPLETION, GOVERNANCE PROMOTION, MINIMUM BA REBUILD AND POST-BA REGRESSION.

**Prepared against committed repository parent:** `42aea43040b0db892e195ffe39645f76f8d14062`

**Expected working candidate at preparation time:** `facial-access-candidate-r2 / R2-CANDIDATE-12`

**Supersedes:** Revision 23 only for forward execution state. R1-R23 remain historical research records.

**Documentation-method checkpoint:** `DDTA_DOCUMENTATION_METHOD_BASELINE_R24_CHECKPOINT_R1.md`

**Documentation authoring guide:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R2.tex/.pdf`

**Base Analysis operational guide:** `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R1.tex/.pdf`

**Detailed continuation handoff:** `DDTA_R24_FACIAL_ACCESS_CONTINUATION_HANDOFF_R1.md`

## 1. Why R24 replaces the forward state of R23

R23 inserted and completed the bounded literature/semantic-recognition cycle required to investigate the ambiguity found in Facial Access `MR-0003`. That work justified an integrated semantic-sufficiency review rather than a separate pattern methodology and established Base Analysis as a second semantic pressure test without making BA project authority.

The subsequent R24 authoring cycle has now exercised that method on real Facial Access documentation.

The controlled review has:

- clarified the entry-state ambiguity in `MR-0003`;
- carried the clarification through Decisions, Functional Requirements and Security Requirements;
- completed review of the current R1-derived Decision set;
- completed review of the current R1-derived Functional Requirement set;
- completed review of the current R1-derived Security Requirement set;
- preserved the authority boundary: candidate R2 is still `EXPERIMENTAL_NON_CANONICAL` and `primaryBASourceAllowed: false`;
- exposed concrete questions that must be resolved before promotion and before accepting a Base Analysis.

The forward problem is therefore no longer literature selection or Decision/FR/SR carry-forward. It is:

```text
review documentation gaps
    -> full semantic regression of successor candidate
    -> assemble coherent successor baseline
    -> explicit governance promotion
    -> rebuild minimum justified BA
    -> post-BA regression
    -> reopen only the smallest forced BA contract
    -> downstream analysis usefulness test
```

## 2. Fixed methodology state

The following state is retained unless a concrete counterexample forces reopening.

### 2.1 Documentation authoring

The forward authoring sequence remains the integrated semantic procedure frozen by the R24 documentation-method checkpoint:

```text
authority gate
-> project problem framing
-> MacroRequirement
-> semantic-sufficiency gate
-> Decision
-> FunctionalRequirement
-> Requirement coherent-unit / split
-> SpecializedRequirement
-> SecurityRequirement
-> cross-MR / consumed-service boundary
-> canonical terminology and review bindings
-> downstream semantic propagation after correction
-> documentation completeness / promotion gate
-> handoff to Base Analysis
-> BA/analysis feedback without authority inversion
```

Semantic sufficiency is not an absolute promise that documentation answers every possible downstream question.

The method now distinguishes:

```text
authoring sufficiency
    enough governed meaning to state the project responsibility/commitment stably

from

consumer-specific sufficiency
    enough governed meaning to answer one declared downstream analysis question
```

A downstream consumer may expose a missing distinction. It may not invent the answer.

### 2.2 Base Analysis

Retained contracts:

```text
BA0  responsibility / authority boundary       retained closed
BA1  BAReferent + BAProposition                retained closed
BA2  active R24 working R2                    open only to concrete pressure
BA3  provenance / derivation / lifecycle       retained closed
BA4  projection / interpretation / coverage    retained closed
BA5  canonical semantic registry               retained closed
BA6  integrated completion/regression           not yet completed
```

The main operational procedure is the organic BA guide, not BA0-BA5 as a learning sequence.

No BA operator is added merely because documentation uses a familiar verb or because a downstream model would be convenient.

## 3. Facial Access authority state

The historical/current R1 Facial Access corpus remains superseded evidence.

The active experimental successor is now:

```text
corpusKey: facial-access-candidate-r3
corpusRevision: R3-CANDIDATE-3
authorityStatus: EXPERIMENTAL_NON_CANONICAL
researchRole: CURRENT_THESIS_VALIDATION_CORPUS
primaryBASourceAllowed: false
```

`candidate-r3` integrates the reviewed MR-0003 successor chain with the reviewed MR-0001 access-decision consumer and MR-0002 authorization-to-identity binding. `DG-FA-001` is resolved at semantic level, `DG-FA-002` is resolved / reframed as governed outcome-conclusiveness semantics, and `DG-FA-003` is resolved at documentation semantic level with its BA representation pressure explicitly retained. The earlier `candidate-r2` remains unchanged as regression/provenance evidence.

Therefore:

- no accepted/current Facial Access BA may yet be derived;
- working BA pressure tests are allowed;
- promotion requires completion of the remaining bounded gap review, full semantic regression and an explicit governance step;
- the candidate must not be treated as `CURRENT_GOVERNED` merely because it is the active R24 experimental successor.

## 4. Candidate R3 content now reviewed

### 4.1 MacroRequirement

`MR-0003 — Determinazione dell'identità al punto di accesso`

The critical entry-state fact is now explicit:

> when the responsibility begins, the person is present at the access point but the specific governed identity corresponding to that person has not yet been determined.

The responsibility determines **which** governed identity corresponds. It does not create or maintain governed identities and does not decide authorization or access.

### 4.2 Decisions

Current autonomous candidate Decisions:

```text
D-3.1  facial recognition is the current identity-determination strategy
D-3.2  recognition produces a governed identity-determination outcome,
       not an access decision
D-3.4  CameraSubsystem acquires RecognitionCapture while a distinct
       RecognitionProcessor performs recognition
D-3.5  the realization consumes an available connectivity service and
       does not own/manage the underlying transport infrastructure
D-3.6  the current interaction uses available wired Ethernet connectivity
```

Historical `D-3.3` is not retained as a separate sibling. Its useful semantic-stability content is merged into `D-3.2`.

Important D-3.5/D-3.6 distinction:

```text
D-3.5
    who owns/manages transport capability?
    -> consumed service, not project-owned

D-3.6
    what governed medium does this realization currently use?
    -> wired Ethernet
```

A replaceable governed realization fact may be preserved even when the project does not own the underlying service. The reason for authoring it is not that the documentation author must anticipate a threat such as RF jamming; the fact is a governed baseline binding whose change can require downstream revalidation.

### 4.3 Functional Requirements

Current candidate set:

```text
FR-3.2.1  Produce governed identity-determination outcome
FR-3.2.2  Make governed identity-determination outcome available
FR-3.4.1  Acquire RecognitionCapture
FR-3.4.2  Deliver RecognitionCapture
```

Historical `FR-3.3.1` is carried forward as `FR-3.2.2` under `D-3.2` because historical `D-3.3` is retired as a separate Decision.

`IdentityDeterminationRequest` replaces historical `RecognitionRequest` and explicitly does not contain or presuppose a preselected `GovernedIdentity`.

`FR-3.4.1` states that when an `IdentityDeterminationRequest` requires a new `RecognitionCapture`, `CameraSubsystem` must acquire it for that request.

`FR-3.4.2` states that `CameraSubsystem` must deliver the `RecognitionCapture` to `RecognitionProcessor` while preserving the binding to the same `IdentityDeterminationRequest`.

No capture quality threshold, score, confidence, ranking, `1:N`, delivery outcome, acknowledgement, retry or protocol is introduced.

### 4.4 Security Requirements

Current candidate set under `FR-3.4.2`:

```text
SEC-3.4.2-C  Confidentiality
SEC-3.4.2-I  Integrity
SEC-3.4.2-P  AuthorizedProvenance
```

Retained distinctions:

```text
Confidentiality
    RecognitionCapture content must not become intelligible
    to unauthorized subjects during delivery

Integrity
    RecognitionCapture and its IdentityDeterminationRequest binding
    must not undergo unauthorized modification

AuthorizedProvenance
    provenance of the delivered RecognitionCapture must be established
    as authorized for the relevant IdentityDeterminationRequest
```

The Security Requirements do not prescribe TLS, mTLS, signatures, certificates, MACs, credentials, attestation, VLANs or other mechanisms.

Open authorization evidence is not silently invented:

- who is authorized to know the capture content?
- what governed evidence establishes which origins are authorized to provide a capture for a request?

Those are clarification/gap questions.

## 5. Consumed-service assurance rule retained

For a property `P` required by the consumer:

```text
consumer requires P
        |
        v
is P explicitly guaranteed by governed service evidence?
      /   \
    yes    no / not specified / conflicting
     |               |
may rely on P   assurance / coverage question
                       |
                       v
              determine semantic owner from evidence
```

Rules:

```text
NOT SPECIFIED != DENIED
NOT SPECIFIED != GUARANTEED
coverage gap != automatic Requirement
coverage gap != automatic Decision
coverage gap != automatic SecurityRequirement
coverage gap != automatic control/mechanism
```

The project may require Confidentiality/Integrity/AuthorizedProvenance for its information even when it consumes the transport service. It may only rely on the service for those properties when governed service evidence guarantees them.

## 6. Documentation-gap review is the next mandatory phase

The existing gaps remain diagnostic and are reviewed one at a time against active candidate R3.

Current state:

```text
DG-FA-001  cross-MR consumer binding              RESOLVED_AT_SEMANTIC_LEVEL
DG-FA-002  quality/sufficiency criterion          RESOLVED / REFRAMED
DG-FA-003  transfer-to-channel/path binding       RESOLVED DOC SEMANTICS / BA PRESSURE RETAINED
DG-FA-004  intermediate transport nodes           NEXT REVIEW
DG-FA-005  test/code evidence linkage              OPEN
DG-FA-006  positive access-decision branch        OPEN / NOT SPECIFIED
```

Additional clarification questions exposed by the SR review remain pending:

```text
AUTH-C
which governed evidence determines who is authorized
to know RecognitionCapture content?

AUTH-P
which governed evidence determines which origins are authorized
to provide RecognitionCapture for an IdentityDeterminationRequest?
```

For each remaining gap:

1. show relevant current MR;
2. show relevant parent Decision(s);
3. show relevant FR/SR when applicable;
4. show historical gap wording;
5. determine whether the gap is still real, resolved, reframed or outside current scope;
6. do not invent a solution;
7. update candidate documentation only after explicit disposition.

The next bounded documentation-gap microstep is **DG-FA-004 only**.

## 7. Required full-candidate regression before promotion

After gap review, perform a full semantic regression across the successor candidate.

At minimum verify:

- no artifact silently reintroduces a preselected `GovernedIdentity`;
- `IdentityDeterminationRequest` has one stable meaning everywhere;
- `RecognitionCapture`, `IdentityDeterminationOutcome`, authorization state and access decision remain distinct;
- D-3.4 / D-3.5 / D-3.6 remain separate commitments;
- FR-3.4.1 acquisition and FR-3.4.2 delivery remain independently assessable;
- Security Requirements do not smuggle realization mechanisms into project truth;
- authorization/provenance evidence gaps are explicit rather than inferred;
- no score/confidence/threshold/ranking/`1:N` semantics have been added without governed evidence.

## 8. Successor assembly and promotion gate

Only after gap review and full regression:

```text
assemble coherent successor baseline
        |
        v
check completeness and authority metadata
        |
        v
explicit human governance promotion
```

Promotion must be explicit.

Before promotion:

```text
authorityStatus: EXPERIMENTAL_NON_CANONICAL
primaryBASourceAllowed: false
```

After promotion, update authority metadata only through an explicit governed microstep. Do not equate "review complete" with "promoted".

## 9. Minimum justified BA rebuild after promotion

After promotion, derive the BA again from the promoted documentation rather than mechanically reusing the earlier working pressure test.

Candidate semantic identities/operators must earn their place from governed meaning.

Pressure points already discovered:

### 9.1 Identity determination

Do not model `GovernedIdentity` as a preselected input.

The responsibility determines which identity corresponds to the person present.

### 9.2 Outcome semantics

The governed outcome has at least:

```text
SUCCESS
NEGATIVE
INCONCLUSIVE
```

No score/threshold/selection rule is implied.

### 9.3 Capture acquisition

The documentation deliberately says **acquire**.

Do not rewrite the project documentation merely to choose a BA operator.

During BA rebuild, pressure-test whether `create`, `observe`, `produce`, a combination or another already-governed structure is actually forced. If multiple material BA candidates remain, diagnose rather than guess.

### 9.4 Capture/request binding

`FR-3.4.1` and `FR-3.4.2` explicitly govern the binding:

```text
RecognitionCapture <-> IdentityDeterminationRequest
```

This is concrete pressure for `correlate` or another existing structure, but the source must drive the representation.

### 9.5 Delivery / consumed service / medium binding

After `DG-FA-003`, this remains the most important retained BA2 **representation** pressure, but no longer an open documentation-semantics gap.

The bounded documentation review established that the existing project sources already identify the same governed interaction without adding a new extraction-oriented cross-reference:

```text
FR-3.4.2
    RecognitionCapture delivery
    CameraSubsystem -> RecognitionProcessor

D-3.5
    available ConnectivityService supports that delivery

D-3.6
    current governed interaction medium = WIRED_ETHERNET
```

No `channel`/`path` document field and no new hard-coded reference to `FR-3.4.2` is justified merely to help BA extraction.

Do not modify BA2 now. During the minimum BA rebuild after promotion, pressure-test whether:

1. the BA can derive the binding reproducibly from the existing governed sources;
2. existing BA structures preserve the material delivery/service/medium distinction;
3. `transfer` genuinely needs an optional channel/behavior binding only if a concrete representation failure remains;
4. another smaller representation solves the problem without inventing topology.

## 10. Post-BA regression

After the minimum BA is accepted for the promoted baseline, regress it against documentation.

Use these diagnostics:

```text
ONE BA / ONE STABLE MEANING
MULTIPLE MATERIAL BA CANDIDATES
BA REQUIRES UNSUPPORTED FACT
BA LOSES GOVERNED MATERIAL DISTINCTION
BA EXPOSES SOURCE CONFLICT
```

A BA expressiveness problem is not automatically a documentation defect.

A downstream question may reveal information absent from current project truth. The feedback path is:

```text
consumer question
    -> diagnostic / clarification request
    -> governed project review
    -> documentation update if justified
    -> rebuild BA
    -> rerun consumer
```

No authority inversion is allowed.

## 11. Downstream usefulness test after BA regression

Use at least the controlled transport-medium example.

The governed fact:

```text
RecognitionCapture delivery uses WIRED_ETHERNET
```

may allow a consumer to reject a threat that specifically requires an RF/wireless medium **for the governed interaction**.

It must not allow the consumer to infer:

```text
the entire consumed connectivity infrastructure
is wired Ethernet end-to-end
```

If internal provider topology is not governed, threats depending on that hidden topology remain unresolved rather than automatically applicable or inapplicable.

This test is evidence for preservation of a governed material distinction, not a reason for the original documentation author to anticipate security analysis.

## 12. Explicit non-goals / guardrails

Do not:

- derive an accepted BA before promotion;
- add score, confidence, threshold, ranking or `1:N` semantics;
- add a Decision/FR merely to satisfy hierarchy shape;
- invent a project-owned transport FR from D-3.5;
- infer provider-internal network topology from D-3.6;
- add TLS/mTLS/certificates/signatures merely because Security Requirements exist;
- convert diagnostic gaps automatically into requirements;
- let BA or a threat method become project authority;
- physically rewrite superseded R1 history;
- reopen BA1/BA3/BA4/BA5 without a concrete counterexample;
- add a BA2 operator or role before the smallest real corpus pressure is demonstrated.

## 13. Forward execution sequence

The active forward sequence is:

```text
R3-CANDIDATE-3
    -> DG-FA-001 resolved at semantic level
    -> DG-FA-002 resolved / reframed under D-3.2 and FR-3.2.1
    -> DG-FA-003 resolved at documentation semantic level / BA pressure retained
    -> review DG-FA-004
    -> review DG-FA-005
    -> reconcile AUTH-C / AUTH-P clarification questions
    -> review DG-FA-006 at the appropriate bounded semantic-owner step
    -> full successor semantic regression
    -> explicit governance promotion
    -> minimum justified BA rebuild
    -> full post-BA regression
    -> evaluate transfer/delivery/service/medium structural pressure
    -> reopen/supersede smallest forced BA contract only if necessary
    -> downstream threat-analysis usefulness test
    -> BA6 completion decision
```

Each documentation-gap microstep is reviewed separately. Do not batch unresolved semantic decisions for convenience.

## 14. Checkpoint meaning

This R24 plan records forward execution state only.

It does not:

- promote candidate R3;
- accept a Facial Access BA;
- close DG-FA-004 through DG-FA-006;
- close BA as a whole;
- claim that the security-property authorization models already exist;
- claim that wired Ethernet describes hidden provider topology.

The next authorized project-semantics action is **DG-FA-004 review only**.
