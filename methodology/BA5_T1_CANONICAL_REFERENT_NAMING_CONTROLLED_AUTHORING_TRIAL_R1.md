# DDTA BA5-T1 canonical referent naming and controlled-authoring trial - R1

**Status:** COMPLETED / PROVISIONAL PASS WITH CANONICAL-REFERENT-NAMING LOWER-BOUND

**Repository baseline reviewed:** `aa4b785dc72c2fbcd20fd04976e77fca3d07bf25`

**Executed scope:** BA5-T1 only.

## 1. Trial question

Can DDTA impose one exact canonical name for each named shared project referent across governed documentation, accepted Base Analysis and derived shared views, with tool enforcement and no normative synonym mapping, without confusing lexical naming with BA identity or restricting method-owned taxonomy?

## 2. Hypothesis under test

```text
H5-T1

For a named shared referent in one governed baseline/naming scope:
  exactly one canonical name is normative;
  all semantic references use that exact token;
  shared derived views preserve it;
  aliases/synonyms are not accepted as equivalent input;
  tool support enforces rather than interprets equivalence.
```

Example token:

```text
cameraIngresso
```

## 3. Fixed prior contracts

The trial holds BA1-BA4 closed unless a material counterexample forces the smallest reopen.

Relevant prior invariants:

- BA1: `BAReferent` identity is independently reusable methodology-neutral project meaning; lexical category or convenience does not create identity.
- BA2: stable semantic keys are distinct from source wording and display labels.
- BA3: wording change does not by itself force referent replacement; continuity is `RETAIN | REPLACE | RETIRE`.
- BA4: shared rendering preserves BA meaning; method-owned taxonomy and interpretation remain downstream.

## 4. Canonical-name propagation trial

Assume governed material introduces one referent under:

```text
cameraIngresso
```

The authoring/integration target is:

```text
Decision / FR / Specialized Requirement / Security Requirement
    -> cameraIngresso

accepted BAReferent rendering
    -> cameraIngresso

human projection
    -> cameraIngresso

flow-oriented projection
    -> [FlowParticipant] cameraIngresso

assurance-oriented projection
    -> [AssuranceSubject] cameraIngresso
```

The local projection kinds are intentionally incompatible. The entity name is not.

Result: **PASS**.

## 5. Alias negative control

Candidate second-document wording:

```text
entryCamera
```

when it intends the same shared referent as `cameraIngresso`.

If accepted as a second normative identifier, every consumer must either maintain synonym equivalence or guess identity. That reintroduces lexical resolution before the semantic architecture is fully integrated.

Disposition: **REJECTED**.

The valid options are:

1. use `cameraIngresso`; or
2. perform a governed rename for a later baseline.

## 6. Exact-token control

The following are not silently equivalent:

```text
cameraIngresso
CameraIngresso
camera_ingresso
camera-ingresso
```

The registry stores the accepted token and validation is exact under the project naming convention.

Disposition: **PASS / exact-token lower bound retained**.

## 7. Collision control

Suppose two different referents are authored with:

```text
cameraIngresso
```

within the same naming scope.

The registry can no longer resolve source/projection references unambiguously.

Disposition: **REJECTED**.

Therefore canonical names are unique within the active baseline/naming scope.

## 8. Human projection control

A human view wants a friendlier label:

```text
Entry Camera
```

If this text replaces the referent name, the no-synonym invariant is broken.

Disposition: **REJECTED AS REFERENT RENAME**.

The view may instead write explanatory prose around the canonical token:

```text
Entrance capture device: cameraIngresso
```

where only `cameraIngresso` is the project entity identifier.

## 9. Method projection control

A flow-oriented method wants:

```text
FlowParticipant
```

and an assurance-oriented method wants:

```text
AssuranceSubject
```

Both are allowed as projection-owned kinds:

```text
FlowParticipant(cameraIngresso)
AssuranceSubject(cameraIngresso)
```

The method taxonomy does not rename the shared referent.

Disposition: **PASS**.

## 10. Method-owned aggregation control

A method creates an item:

```text
external-ingress-exposure
```

from several traced BA elements including `cameraIngresso`.

This label is allowed because it names a method-owned interpretation/aggregation, not the project referent. Its trace still names/reaches `cameraIngresso` canonically.

Disposition: **PASS WITH BA4 BOUNDARY**.

## 11. Governed rename falsification control

The strongest test intentionally changes the canonical name:

```text
B0: cameraIngresso
B1: cameraNord
```

Assume the independently reusable project meaning is materially unchanged; only the governed name changes.

If BA5 equated name and identity, the rename would force a new `BAReferent`, contradicting BA3's closed identity rule that wording changes do not by themselves force replacement.

The correct result is:

```text
B0 BAReferent R
  canonicalName cameraIngresso

BACrossBaselineContinuity
  R@B0 -> RETAIN -> R@B1

B1 BAReferent R
  canonicalName cameraNord
```

Historical B0 projections remain `cameraIngresso`. Rebuilt B1 shared projections use `cameraNord`.

Disposition: **PASS WITH REFINEMENT**.

This falsifies a globally immutable-name hypothesis and closes the narrower rule:

> canonical name is exact and invariant within one governed baseline/naming scope, while governed cross-baseline rename may retain semantic identity.

## 12. Source authority control

Negative pattern:

```text
ThreatForge sees entryCamera
  -> silently decides it means cameraIngresso
  -> writes BA/project binding
```

Disposition: **REJECTED**.

Allowed pattern:

```text
tool detects unregistered entryCamera
  -> blocks or proposes cameraIngresso
  -> author/governance accepts correction
  -> governed material uses cameraIngresso
```

The tool enforces the registry; it does not become the registry's semantic authority.

## 13. BA reopen pressure

The trial tries to force additional semantic machinery.

### New BAE family?

Not needed. Naming metadata attaches to/resolves for `BAReferent`.

### New BA2 operator such as `nameOf`?

Not needed. Canonical naming is lexical/governance metadata, not a methodology-neutral project assertion requiring proposition identity.

### BA3 reopen?

Not needed. Existing continuity already handles a retained identity under wording/name change.

### BA4 reopen?

Not needed. BA5 simply narrows shared referent rendering: local projection kinds remain free, shared referent names become exact-canonical.

### Documentation metamodel reopen?

Not forced. The constraint is cross-document controlled authoring and naming governance rather than a new structural field family for Decision/FR/SR/Security Requirement.

## 14. Trial dispositions

```text
canonical name exact within baseline/scope                 PASS
same shared referent same name across governed docs        PASS
same shared referent same name across shared views         PASS
alias/synonym as second normative identifier               REJECTED
case/format variant as implicit alias                      REJECTED
collision between two referents                            REJECTED
canonicalName as semantic identity                         REJECTED
governed cross-baseline rename with RETAIN                 PASS
projection-owned type vocabulary                           PASS
method-owned interpretation label                          PASS
tool registry validation/completion                        PASS
tool autonomous alias normalization                        REJECTED
new BAE family                                             NOT FORCED
new BA2 operator                                           NOT FORCED
BA1-BA4 reopen                                             NOT TRIGGERED
BA5                                                        STARTED / NOT CLOSED
```

## 15. Result

BA5-T1 passes with one important refinement.

The initial strong controlled-vocabulary direction survives, but `canonicalName` cannot be treated as an eternal identity key. The accepted provisional lower bound is:

```text
same named referent
+ same governed baseline/naming scope
    -> one exact canonicalName everywhere shared

cross-baseline governed rename
    -> may RETAIN BAReferent identity
    -> new baseline uses new canonicalName consistently
```

No synonym registry is required by the current evidence.

## 16. Next smallest falsification target

BA5-T2 should pressure-test **registry coverage and governed extension**, not general synonym normalization:

- operators;
- operator-scoped roles;
- semantic kinds such as `store` and `contract`;
- controlled values;
- new canonical-term admission; and
- tool enforcement/completion across the complete registry.

Only concrete failure should force alias/synonym machinery.
