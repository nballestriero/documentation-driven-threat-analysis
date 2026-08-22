# R24 semantic-review pressure tests R1

**Status:** WORKING RESEARCH EVIDENCE / NOT METHOD AUTHORITY
**DDTA baseline for current-method comparison:** `87a612663d1e4827b7f67e83182838586e53d7ba`

## 1. Purpose

Record the pressure tests that motivated the candidate semantic-sufficiency and BA-regression refinement without promoting local observations directly into DDTA rules.

## 2. Test A — Facial Access current working documentation

Trigger: `MR-0003` uses a familiar verification-oriented label while its neutral wording can be read in materially different ways.

Neutral competing readings:

```text
A. a specific GovernedIdentity is not yet selected;
   the responsibility determines which GovernedIdentity corresponds.

B. a specific GovernedIdentity is already available/selected;
   the responsibility determines whether correspondence holds.
```

Critical difference:

> Before correspondence determination begins, is a specific `GovernedIdentity` already available/selected as the reference?

Current result:

```text
stable macro responsibility independent from label: YES
material competing readings: YES
critical difference: YES
governed evidence sufficient to exclude one reading: NO / NOT EXPLICIT
semantic closure: UNRESOLVED
```

The wording may linguistically favour one reading, but candidate preference is not semantic closure.

## 3. Cross-LLM blind replication #1

A separate LLM received only the anonymized case and the blind-review procedure.

Result:

```text
PREFERRED INTERPRETATION BUT NOT FULLY RESOLVED
```

It independently recovered the same discriminator family: whether a specific `GovernedIdentity` is already proposed/known at entry or must be determined.

Grounded phase was blocked because that LLM could not access the exact pinned Git baseline.

Observed failure mode: its supposedly neutral reconstruction leaked an inferred "set" of identities even though that fact had been marked `NOT SPECIFIED`.

Interpretation: useful candidate/discriminator assistance; not semantic authority.

## 4. Cross-LLM blind/grounded replication #2

A second LLM completed the blind phase before repository access.

Blind result:

```text
AMBIGUOUS / UNRESOLVED
```

Blind critical difference again matched the same entry-state/reference-availability discriminator.

The grounded phase read the four allowed files at the exact baseline. One allowed guide contained Facial Access labels in its legitimate checkpoint section, creating a documented contamination risk after the blind result had already been frozen.

Grounded result remained:

```text
AMBIGUOUS / UNRESOLVED
SAME RESULT / SAME DISCRIMINATOR
THEORY IMPROVED EXPLANATION WITHOUT CHANGING RESULT
```

Observed failure mode: the final scorecard selected `MR` as owning level while the same response later classified that ownership claim as needing more evidence.

Interpretation: convergence on the critical difference is stronger evidence than convergence on closure/placement.

## 5. Controlled synthetic test — record coherence

A deliberately synthetic non-identity case compared two records representing the same business entity.

Material readings:

```text
A. one record/state is already authoritative and the other converges to it;
B. both records may contain valid contributions and a resulting coherent state must be reconciled.
```

Critical difference:

> Is the correct target state already authoritative, or must the target state itself be determined from competing valid states?

This pressure-tested a different semantic axis from Facial Access.

Evidence value:

```text
METHOD EXPLORATION
NOT EMPIRICAL VALIDATION
```

## 6. Retrospective ThreatForge test — implementation promotion

Historical real-project corpus:

Repository:
`nballestriero/threat-forge`

Product-semantic baseline:
`cae0f7b6b37f430ac4e857aabf6ef9f87c89dbb1`

Relevant documents:

- `docs/reference/project-model/body/macro-requirements/MR-0002_body.md`
- `docs/reference/project-model/body/decisions/MR-0002/ADR-0003_body.md`
- `docs/reference/project-model/body/requirements/MR-0002/MR-0002ADR-0003REQ-0002_body.md`
- supporting planner requirement `MR-0002ADR-0001REQ-0001_body.md`

Observed lifecycle wording:

```text
scaffolded
    ↓
real behavior + successful governed verification
    ↓
implemented
```

Material readings:

```text
A. "implemented" means the artifact is no longer merely a scaffold:
   substantive behavior exists and configured verification succeeds.

B. "implemented" means the linked governed Requirement has actually
   been demonstrated as satisfied by that artifact.
```

Critical difference:

> What proposition must the verification evidence justify before the artifact may become `implemented`?

Current source evidence explicitly requires real behavior, trace consistency and successful verification, but does not equally explicitly define whether successful evidence proves only artifact-lifecycle completion or Requirement satisfaction.

Result:

```text
material ambiguity candidate: YES
critical difference: YES
evidence sufficient to close the stronger proposition: NO / NOT EXPLICIT
different discriminator family from Facial Access: YES
```

Limitation: this is a retrospective pressure test on documentation written before the current DDTA authoring method matured. It is valuable as historical empirical evidence, not as a clean validation of current authoring.

## 7. Cross-case comparison

| Case | Primary semantic axis | Critical-difference form |
|---|---|---|
| Facial Access | entry knowledge / reference availability | is a specific reference already known? |
| Synthetic record coherence | state authority / reconciliation | is the target state already authoritative? |
| ThreatForge promotion | evidence / lifecycle meaning | what proposition does evidence justify? |

The mechanism is therefore not currently limited to one domain-specific discriminator.

## 8. What these tests do and do not support

They support continued pressure testing of:

```text
neutral reconstruction
→ material competing readings
→ critical difference
→ governed evidence
→ placement or unresolved
```

They do **not** yet support:

- a universal semantic taxonomy;
- a mandatory pattern catalogue;
- a metamodel change;
- automatic classification;
- automatic BA generation;
- a claim of general method validation.

## 9. Next empirical step

Return to real Facial Access authoring, derive only the minimum justified BA once meaning is sufficiently stable, then run the post-BA semantic regression back-check.

After that, repeat the same authoring → BA → regression cycle on another real governed responsibility before promoting the candidate review discipline into stable guide or thesis wording.
