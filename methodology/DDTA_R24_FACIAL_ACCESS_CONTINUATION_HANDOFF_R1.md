---
title: "DDTA R24 Facial Access continuation handoff - R1"
---

# DDTA R24 Facial Access continuation handoff

**Purpose:** detailed restart record for the next chat after the current checkpoint is committed and pushed.

**Prepared against committed parent:** `42aea43040b0db892e195ffe39645f76f8d14062`

**Important baseline rule:** the canonical continuation baseline is the **final Git commit that contains this handoff and the R24 work plan**. A file cannot contain its own Git commit SHA. At new-chat startup, verify `git rev-parse HEAD` and `git rev-parse origin/master` are identical and use that exact SHA as the continuation baseline.

## 1. What the next chat must read first

Read, in this order:

1. `methodology/DDTA_R24_FACIAL_ACCESS_CONTINUATION_HANDOFF_R1.md`
2. `methodology/DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R24.md`
3. `methodology/DDTA_DOCUMENTATION_METHOD_BASELINE_R24_CHECKPOINT_R1.md`
4. `methodology/DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R2.tex` or PDF
5. `methodology/DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R1.tex` or PDF
6. `governed-corpora/facial-access/candidate-r2/corpus.manifest.yml`
7. `governed-corpora/facial-access/candidate-r2/MR-0003_IDENTITY_DETERMINATION.md`
8. `governed-corpora/facial-access/candidate-r2/DECISIONS.md`
9. `governed-corpora/facial-access/candidate-r2/FUNCTIONAL_REQUIREMENTS.md`
10. `governed-corpora/facial-access/candidate-r2/SECURITY_REQUIREMENTS.md`
11. superseded R1 `DOCUMENTATION_GAPS.md` only as regression evidence for the next gap review.

Do not infer the current state from older summaries when these files are available.

## 2. Repository / authority checkpoint

At handoff preparation:

```text
committed parent HEAD
    42aea43040b0db892e195ffe39645f76f8d14062

working successor candidate
    facial-access-candidate-r2
    R2-CANDIDATE-12

authority
    EXPERIMENTAL_NON_CANONICAL

primaryBASourceAllowed
    false
```

The current chat has completed Decision, Functional Requirement and Security Requirement carry-forward review for the `MR-0003` successor candidate.

The candidate is **not promoted**.

No accepted Facial Access BA exists for this candidate.

## 3. User workflow constraints to preserve

Use small controlled microsteps.

For project-file changes, prefer a small local drop-in ZIP rather than direct GitHub mutation.

Before APPLY:

- verify required HEAD;
- verify exact pre-apply hashes of files that already contain uncommitted microsteps;
- do not require a clean working tree when the expected state deliberately contains reviewed uncommitted files.

After APPLY:

```text
git diff --check
$LASTEXITCODE
git status --short
$LASTEXITCODE
```

Before commit:

```text
git diff --check
git add ...
git diff --cached --check
git diff --cached --stat
git status --short
```

Always inspect `$LASTEXITCODE` after native git commands.

PowerShell 5.1 may display UTF-8-without-BOM files incorrectly with plain `Get-Content`. Use:

```powershell
Get-Content <file> -Encoding UTF8
```

Mojibake such as `â€”`, `Ã¨`, `proprietÃ` in default `Get-Content` does not by itself mean the file is corrupt.

Do not stage/commit/push until the user explicitly reaches the checkpoint step.

## 4. Review presentation rule

For Decision review, show:

```text
MR
-> Decision
-> review
```

For Functional Requirement review, show:

```text
MR
-> parent Decision
-> historical/current FR
-> review
```

For Security Requirement review, show:

```text
MR
-> parent Decision
-> parent FR
-> historical/current SR
-> review
```

For the next documentation-gap phase, use:

```text
MR
-> relevant Decision(s)
-> relevant FR/SR
-> historical gap
-> current evidence
-> disposition
```

Review **one gap at a time**.

The next gap is `DG-FA-001` only.

## 5. MR-0003 critical meaning

Current title:

`MR-0003 — Determinazione dell'identità al punto di accesso`

Core governed meaning:

- a person is present at the access point;
- when this responsibility begins, the specific governed identity corresponding to that person has **not yet been determined**;
- governed identities already exist and are managed elsewhere;
- this responsibility determines **which governed identity** corresponds to the person present;
- it does not create or administer governed identities;
- it does not grant/revoke authorization;
- it does not decide the individual access attempt;
- facial recognition, sensor, model, placement, network, protocol and security techniques are lower-level commitments.

Do not reintroduce a preselected identity through names such as `verification`, `RecognitionRequest` or BA structure.

## 6. Decision state

### D-3.1

Facial recognition is the current strategy used to determine which governed identity corresponds to the person present.

Do not add score/threshold/`1:N` semantics.

### D-3.2

Recognition produces a governed identity-determination outcome, not an access decision.

When determination succeeds, the outcome makes the determined governed identity available.

Successful, negative and inconclusive outcomes remain distinguishable.

The governed meaning does not depend on the current technical output format.

### Historical D-3.3

Retired as a separate sibling.

Its semantic-stability principle is merged into D-3.2.

### D-3.4

`CameraSubsystem` acquires `RecognitionCapture`.

A distinct `RecognitionProcessor` performs recognition.

The separation creates the need to make `RecognitionCapture` available between them.

D-3.4 does not determine transport service, medium, protocol or security mechanism.

### D-3.5

The realization consumes an available connectivity service to support delivery.

It does not own/manage the underlying transport infrastructure.

Needed service properties can be relied upon only when governed service evidence explicitly guarantees them.

A missing/not-specified/conflicting guarantee creates an assurance/coverage question, not an automatic requirement/control.

### D-3.6

The current interaction uses available **wired Ethernet** connectivity.

This is a governed replaceable baseline binding for the interaction.

It does not mean the project owns the transport service.

It does not mean the entire provider infrastructure is wired end-to-end.

## 7. Functional Requirement state

### FR-3.2.1

Produce a governed identity-determination outcome.

At least:

```text
successful
negative
inconclusive
```

On successful determination, make the specific determined governed identity available.

Do not represent the outcome as authorization or access decision.

### FR-3.2.2

Successor of historical `FR-3.3.1`, reparented under D-3.2.

Make the governed identity-determination outcome available to downstream access-control responsibilities.

The consumer must not be forced to interpret the particular technical output format of the current recognition realization.

### FR-3.4.1

When an `IdentityDeterminationRequest` requires a new `RecognitionCapture`, `CameraSubsystem` must acquire it for that request.

`IdentityDeterminationRequest` means a request to determine which governed identity corresponds to the person present.

It does **not** contain or presuppose a preselected governed identity.

Historical `appropriate` capture wording was removed because no capture quality/sufficiency criterion is currently governed.

Do not alter the documentation merely to choose BA `create` vs `observe`.

### FR-3.4.2

For every capture intended for recognition by `RecognitionProcessor`, `CameraSubsystem` must deliver it to `RecognitionProcessor` while preserving the binding to the same `IdentityDeterminationRequest` for which it was acquired.

No delivery status/outcome, acknowledgement, retry, protocol or transport mechanism is introduced by this FR.

## 8. Security Requirement state

All three are direct children of `FR-3.4.2`.

### SEC-3.4.2-C — Confidentiality

During FR-3.4.2, RecognitionCapture content must not become intelligible to subjects unauthorized to know it.

Open clarification:

```text
what governed evidence identifies subjects authorized
to know RecognitionCapture content?
```

No encryption mechanism is prescribed.

### SEC-3.4.2-I — Integrity

During FR-3.4.2, the `RecognitionCapture` and its binding to the relevant `IdentityDeterminationRequest` must not undergo unauthorized modification.

This covers content tampering and request/capture substitution/rebinding.

It does not introduce an acceptance/validity state.

Integrity remains distinct from AuthorizedProvenance.

### SEC-3.4.2-P — AuthorizedProvenance

During FR-3.4.2, provenance of the delivered `RecognitionCapture` must be established as authorized to provide the capture for the relevant `IdentityDeterminationRequest`.

Open clarification:

```text
what governed evidence identifies origins authorized
to provide RecognitionCapture for a request?
```

No certificate/signature/credential/attestation mechanism is prescribed.

## 9. Current terminology bindings

Use consistently:

```text
PersonAtAccessPoint
GovernedIdentity
IdentityDeterminationRequest
RecognitionCapture
IdentityDeterminationOutcome
CameraSubsystem
RecognitionProcessor
ConnectivityService [conceptual working term unless source evidence names a concrete service]
```

Important:

- `RecognitionRequest` is historical wording and should not return in the successor candidate;
- `IdentityDeterminationRequest` does not imply preselected identity;
- `RecognitionCapture` is not the same thing as `IdentityDeterminationOutcome`;
- authorization state and access decision remain downstream/different responsibilities.

## 10. Current documentation gaps to review next

Historical R1 gap set:

### DG-FA-001 — cross-MR consumer binding

MR-0003 makes its result available downstream, but the exact access-decision consumer branch is not yet migrated into the candidate.

Do not invent a definitive consumer referent.

### DG-FA-002 — quality/sufficiency criterion

Historical material mentioned sufficient quality/evidence.

Candidate R2 deliberately removed `appropriate` capture wording because no governed sufficiency criterion is currently available.

Do not invent thresholds.

### DG-FA-003 — transfer-to-channel/path binding

Current documentation governs:

```text
FR-3.4.2  delivery
D-3.5     consumed transport service
D-3.6     wired Ethernet medium
```

But the exact structural binding:

```text
THIS transfer
    uses
THIS connectivity/path
```

must still be pressure-tested.

### DG-FA-004 — intermediate transport nodes

Do not invent switch/firewall/hops.

Absence is not automatically a defect when the project consumes the connectivity service.

### DG-FA-005 — test/code evidence linkage

Security Requirements now have stable document identity, but no test/code trace metamodel is authorized merely because such linkage could be useful.

## 11. First microstep in the next chat

Do **DG-FA-001 only**.

Before proposing any change, show:

1. current `MR-0003`;
2. relevant Decision(s), especially D-3.2 for outcome meaning;
3. `FR-3.2.2`;
4. historical `DG-FA-001`;
5. current cross-branch note in MR-0003;
6. candidate interpretations/disposition.

Do not batch DG-FA-002 through DG-FA-005.

## 12. BA working pressure-test already performed

A non-authoritative working BA pressure test was performed before FR/SR carry-forward was complete.

Useful provisional referents included:

```text
PersonAtAccessPoint
GovernedIdentity
IdentityDeterminationCapability
IdentityDeterminationOutcome
FacialRecognitionCapability
CameraSubsystem
RecognitionProcessor
RecognitionCapture
RecognitionCaptureDelivery
ConnectivityService
```

Useful provisional proposition shapes included:

```text
produce
realize
constrain
reference
transfer
consumeService
```

Do not treat this list as accepted BA.

The test produced three important observations.

### 12.1 `create` is not automatically required

MR-0003 does not create GovernedIdentity.

For capture acquisition, current documentation uses `acquire`; BA `create` vs `observe` remains a pressure point rather than a documentation-writing target.

### 12.2 `correlate` now has stronger source evidence

FR-3.4.1/2 explicitly preserve:

```text
RecognitionCapture <-> IdentityDeterminationRequest
```

The promoted BA rebuild should test whether `correlate` naturally represents this governed binding.

### 12.3 Main unresolved structural pressure

The strongest current BA question is still:

```text
transfer(CameraSubsystem,
         RecognitionProcessor,
         RecognitionCapture)

        ?
        |
RecognitionCaptureDelivery
        |
consumeService
        v
ConnectivityService
        |
medium
        v
WIRED_ETHERNET
```

Do not change BA2 before the documentation-gap review and promoted BA rebuild.

## 13. Downstream analysis lesson from wired Ethernet

The discussion used RF jamming as a **downstream example**, not as authoring authority.

Correct method:

```text
author documents governed replaceable baseline binding
        -> BA preserves it
        -> downstream consumer asks its own question
```

The initial documentation author is not required to anticipate the threat catalog.

If a downstream consumer needs a distinction not governed by project evidence:

```text
cannot determine
    -> diagnostic / clarification question
    -> governed project review
```

not:

```text
consumer invents missing project fact
```

For the current medium:

- a threat that specifically requires an RF/wireless medium may be inapplicable to the governed wired interaction;
- this does not prove hidden provider infrastructure is entirely wired;
- questions about opaque provider internals remain unresolved unless governed evidence answers them.

## 14. Consumed-service assurance lesson

D-3.5 and Security Requirements must remain compatible.

The project may impose properties on its own information/behavior while using an external service.

It may not assume the consumed service supplies those properties merely because they are required.

For every required service-supported property:

```text
explicit guarantee
    -> consumer may rely

DENIED / NOT SPECIFIED / CONFLICTING
    -> assurance/coverage question
    -> determine semantic owner
```

No automatic TLS, SR, FR or other mechanism follows.

## 15. Promotion and BA sequence after gap review

After DG-FA-001 through DG-FA-005 and the SR authorization clarifications are reviewed:

```text
full semantic regression
-> assemble coherent successor baseline
-> explicit promotion
-> rebuild minimum justified BA from scratch
-> full post-BA regression
-> evaluate BA2 pressure
-> downstream usefulness test
```

Do not derive an accepted BA before explicit promotion.

## 16. Hard guardrails

Do not:

- add score/confidence/threshold/ranking/`1:N`;
- infer a specific identity is selected before MR-0003 begins;
- rewrite historical R1 in place;
- promote candidate merely because review appears complete;
- create a project-owned connectivity FR solely because D-3.5 exists;
- infer hidden network topology;
- prescribe crypto/security mechanisms without a separate governed choice;
- turn gaps into requirements automatically;
- let BA or threat analysis become project authority;
- force all known facts into BA if they lack independent/reusable meaning;
- reopen BA contracts before a concrete corpus counterexample.

## 17. Checkpoint completion protocol for the current chat

Before moving to the next chat, the current chat should:

1. apply and validate the Security Requirement completion;
2. apply this work-plan/handoff package;
3. run `git diff --check`;
4. stage the complete intended checkpoint only;
5. run `git diff --cached --check`;
6. inspect staged stat/status;
7. verify remote has not advanced unexpectedly;
8. commit;
9. push;
10. verify `HEAD == origin/master`;
11. verify clean working tree;
12. record the resulting final commit SHA in the new-chat continuation prompt.

Suggested checkpoint intent:

```text
research: complete MR-0003 documentation carry-forward
```

The final commit SHA cannot be embedded in this file because this file is part of that commit. Supply the verified final SHA externally when starting the next chat.
