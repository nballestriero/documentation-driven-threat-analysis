# DermaTriage Base Analysis — Delta R9

**Disposition:** `ACCEPTED_FOR_CONTINUATION`  
**Methodology:** `BA0–BA6 FROZEN`  
**New numbered pressure:** `NONE`

R9 is additive after R8 and consolidates:

```text
DEC-05
FR-13
FR-14
FR-15
DEC-06
FR-09
```

---

# 1. DEC-05 — Separation of adaptation paths by capability

Existing path referents are strongly reinforced:

```text
BAREF-DERMA-068 PromptEvolutionPath
BAREF-DERMA-069 EfficientNetB4AdaptationPath
```

New reusable semantic kind:

```text
BAREF-DERMA-079 Capability
    WORKING_ACCEPTED
```

Accepted:

```text
BAPROP-DERMA-DEC05-001
classify(
  classifiedReferent=PromptEvolutionPath,
  semanticKind=Capability
)

BAPROP-DERMA-DEC05-002
classify(
  classifiedReferent=EfficientNetB4AdaptationPath,
  semanticKind=Capability
)
```

DEC-05 confirms that shared data / common project placement does not make activation
conditions, evidence qualification rules or lifecycle results equivalent.

Carry-forward evidence:

```text
CLASSIFICATION_COVERAGE_REVIEW_EVIDENCE
status: OPEN
disposition: APPLICATION_COMPLETENESS_REVIEW
not methodology pressure
review timing: after current evidence cycle and post-holdout method review
```

---

# 2. FR-13 — Activation-condition independence

New semantic kind:

```text
BAREF-DERMA-080 ActivationCondition
    WORKING_ACCEPTED
```

Accepted:

```text
BAPROP-DERMA-FR13-001
classify(
  classifiedReferent=PromptEvolutionEvidenceAccumulationCondition,
  semanticKind=ActivationCondition
)

BAPROP-DERMA-FR13-002
classify(
  classifiedReferent=ClassifierAdaptationEvidenceAccumulationCondition,
  semanticKind=ActivationCondition
)
```

Governed but not fully representable:

```text
BAREQ-DERMA-FR13-NONIMPLICATION-001

ActivationConditionOfPathA
  MUST NOT by itself imply
ActivationConditionOfPathB

status:
  GOVERNED_BUT_NOT_FULLY_REPRESENTABLE

candidateTopic:
  NEGATIVE_IMPLICATION_NON_SUFFICIENCY_SEMANTICS
```

Negative controls:

```text
non-sufficiency != negative dependOn
non-sufficiency != mutual exclusion
non-sufficiency != other condition false
```

---

# 3. FR-14 — Evidence-qualification independence

No new accepted classification is introduced because evidence qualification is path-relative.

```text
Evidence X qualifies for Path A
```

is relational/contextual and is not safely reduced to:

```text
classify(Evidence X, QualifiedEvidence)
```

Governed but not fully representable:

```text
BAREQ-DERMA-FR14-NONIMPLICATION-001

EvidenceQualifiedForPathA
  MUST NOT by itself imply
EvidenceQualifiedForPathB

status:
  GOVERNED_BUT_NOT_FULLY_REPRESENTABLE

candidateTopic:
  NEGATIVE_IMPLICATION_NON_SUFFICIENCY_SEMANTICS
```

`BAREF-DERMA-078 QualifiedClassifierDisagreementEvidence` remains
`PROVISIONAL_RECONCILIATION`, recheck at FR-07, and its path-specific meaning is reinforced.

---

# 4. FR-15 — Lifecycle-result independence

FR-15 governs:

```text
LifecycleResultOfPathA
  MUST NOT by itself imply
EquivalentLifecycleResultOfPathB
```

without yet identifying a concrete lifecycle-result referent.

Therefore:

```text
transition:
    CONSIDERED
    REJECTED

LifecycleResult:
    semantic-kind candidate
    deferred until a concrete result appears
```

Governed but not fully representable:

```text
BAREQ-DERMA-FR15-NONIMPLICATION-001

status:
  GOVERNED_BUT_NOT_FULLY_REPRESENTABLE

candidateTopic:
  NEGATIVE_IMPLICATION_NON_SUFFICIENCY_SEMANTICS
```

The same unnumbered pressure pattern is now repeated across condition, evidence
qualification and lifecycle result.

---

# 5. DEC-06 — Comparative classifier-adaptation acceptance

New referents:

```text
BAREF-DERMA-081 ClassifierAdaptationCandidate
    WORKING_ACCEPTED

BAREF-DERMA-082 AdaptationCandidate
    WORKING_ACCEPTED
    semantic kind

BAREF-DERMA-083 EfficientNetB4ReferenceModelVersion1_0_0
    PROVISIONAL_RECONCILIATION
    R-14

BAREF-DERMA-084 ClassifierAdaptationQualificationResult
    WORKING_ACCEPTED

BAREF-DERMA-085 LifecycleResult
    WORKING_ACCEPTED
    semantic kind

BAREF-DERMA-086 ClassifierAdaptationQualificationCondition
    WORKING_ACCEPTED
```

Accepted:

```text
BAPROP-DERMA-DEC06-001
classify(
  classifiedReferent=ClassifierAdaptationCandidate,
  semanticKind=AdaptationCandidate
)

BAPROP-DERMA-DEC06-002
classify(
  classifiedReferent=ClassifierAdaptationQualificationResult,
  semanticKind=LifecycleResult
)

BAPROP-DERMA-DEC06-003
dependOn(
  dependent=ClassifierAdaptationQualificationResult,
  prerequisite=ClassifierAdaptationQualificationCondition
)

BAPROP-DERMA-DEC06-004
dependOn(
  dependent=ClassifierAdaptationQualificationCondition,
  prerequisite=EfficientNetB4ReferenceModelVersion1_0_0
)
```

Important distinctions:

```text
candidate produced != candidate qualified
qualification != adoption
qualification != automatic deployment
LifecycleResult != LifecycleState
measured reference metric != constrain
```

R-14 is opened for:

```text
EfficientNetB4ReferenceModelVersion1_0_0
    ?
EfficientNetBaseline
    ?
BestBaselineCheckpoint
```

---

# 6. FR-09 — Comparative qualification of classifier-adaptation candidate

## Source-governed functional clauses

```text
NC-09.1
When a classifier-adaptation candidate is considered for adoption,
DermaTriage MUST evaluate it comparatively against the applicable
reference version using governed acceptance criteria.

NC-09.2
DermaTriage MUST consider the candidate qualified for adoption
only if all applicable governed comparative criteria are satisfied.
```

FR-09 provides the first clean DermaTriage admission of `decisionRule`.

New referents:

```text
BAREF-DERMA-087 ModelVersion
    WORKING_ACCEPTED
    semantic kind

BAREF-DERMA-088 ClassifierAcceptanceCriteria
    WORKING_ACCEPTED
```

Accepted classification:

```text
BAPROP-DERMA-FR09-001
classify(
  classifiedReferent=EfficientNetB4ReferenceModelVersion1_0_0,
  semanticKind=ModelVersion
)
```

Accepted prerequisite:

```text
BAPROP-DERMA-FR09-002
dependOn(
  dependent=ClassifierAdaptationQualificationCondition,
  prerequisite=ClassifierAcceptanceCriteria
)
```

Accepted decision rule:

```text
BAPROP-DERMA-FR09-003

operator: decisionRule

actor:
  DermaTriage

input:
  ClassifierAdaptationCandidate
  EfficientNetB4ReferenceModelVersion1_0_0
  ClassifierAcceptanceCriteria

result:
  ClassifierAdaptationQualificationResult

rule:
  IF
    satisfies(
      subject=ClassifierAdaptationCandidate,
      condition=ClassifierAdaptationQualificationCondition
    )

  THEN
    resultAssignment(
      target=ClassifierAdaptationQualificationResult,
      value=QUALIFIED_FOR_ADOPTION
    )

  ELSE:
    OMITTED
```

The omitted ELSE has no inferred meaning.

This is valid because FR-09, unlike DEC-06, is a concrete Functional Requirement that
explicitly governs conditional result selection.

No current BA proposition asserts deployment.

---

# 7. R9 source-governed documentation gaps

The governed source itself identifies:

```text
GAP-DERMA-DEPLOY-01
FR-09 lifecycle:
final authority and deployment automaticity after qualification unspecified.

GAP-DERMA-ACCEPT-BINDING-01
DEC-06 / DEC-07:
complete quantitative binding of acceptance criteria, including reference/evaluation
population and interpretation of 5%, unspecified.

GAP-DERMA-EVAL-CONSISTENCY-01
FR-09 / DEC-07:
HIGH sensitivity 90.24% vs HIGH recall 81.71% / 134 of 164 HIGH correct;
relationship/evaluation mode not specified.
```

These are documentation gaps, not methodology pressure.

---

# 8. R9 observations

```text
O-15
SHARED DATA / COMMON PROJECT CONTEXT
  !=
SEMANTIC EQUIVALENCE / RULE INHERITANCE
    STRONG MULTI-DIMENSIONAL CONFIRMATION

O-16
NON-SUFFICIENCY
  !=
MUTUAL EXCLUSION / NEGATIVE STATE
    STRONG REPEATED CONFIRMATION

O-17
SEMANTIC KIND
  !=
CONTEXT-RELATIVE QUALIFICATION
    CANDIDATE

O-18
LIFECYCLE RESULT
  !=
LIFECYCLE STATE
    STRONGLY REINFORCED

O-19
PRODUCTION
  !=
QUALIFICATION
  !=
ADOPTION / DEPLOYMENT
    STRONGLY SUPPORTED
```

No BA0–BA6 change is authorized.
