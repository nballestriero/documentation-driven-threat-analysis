# DDTA R25 — DermaTriage Holdout Final Report R11

## 1. Executive summary

The DermaTriage holdout first-pass evidence collection is complete.

The central outcome is **not** that the frozen Base Analysis can represent every governed
meaning. The stronger result is:

```text
1. most governed project meaning can be represented without method-specific reinterpretation;

2. when the BA cannot preserve a governed meaning, the failure is localized as methodology
   pressure instead of silently approximated;

3. when the source itself is incomplete, the issue is preserved as a documentation gap instead
   of being repaired by analyst inference;

4. the two failure classes can coexist on different semantic portions of the same requirement;

5. no BA0–BA6 change was required or allowed during the holdout.
```

This is strong evidence for DDTA's intended authority model:

```text
governed documentation
    -> Base Analysis
    -> deterministic/reproducible projections
    -> optional method-specific interpretation
```

and against the invalid inversion:

```text
diagram / STRIDE / tool
    -> new project meaning
```

## 2. Coverage result

```text
MR-01:
    FIRST-PASS COMPLETE

MR-02:
    FIRST-PASS COMPLETE
    intentional STOP AT MR preserved

MR-03:
    FIRST-PASS COMPLETE

MR-04:
    FIRST-PASS COMPLETE

remaining active bounded source elements:
    0
```

The holdout did not force analysis of the superseded FR-11 as an active requirement.

## 3. What worked well

### 3.1 BAReferent identity discipline

The holdout repeatedly required distinct identities for meanings that are easy to conflate:

```text
authentication mechanism
    != credential
    != token lifecycle responsibility

original triage outcome
    != clinical review
    != validated outcome

service consumption
    != transfer
    != responsibility

adaptation candidate
    != qualification result
    != adopted adaptation
    != deployment

evidence accumulation
    != evidence qualification
    != evidence window
    != selected evidence set

pre-adoption tolerance T
    != post-adoption threshold R
    even when both literals are 5%
```

This identity discipline prevented multiple unsupported conclusions.

### 3.2 Progressive-detail analysis

MacroRequirements, Decisions and FunctionalRequirements contributed different levels of
semantic precision without forcing premature detail.

Examples:

```text
DEC-06:
    comparative qualification policy

FR-09:
    explicit qualification decisionRule

DEC-09:
    bounded/recent evidence policy

FR-06:
    operational production of current-cycle evidence set
    plus a concrete top-N selection counterexample
```

### 3.3 `decisionRule`

The construct moved from bounded/blocked evidence to strong positive DermaTriage evidence.

Clean positive cases:

```text
FR-09:
    qualification result = QUALIFIED_FOR_ADOPTION
    when governed qualification condition is satisfied

FR-07:
    classifier evidence qualifies on ClinicianDisagreement

FR-08:
    P1 -> HIGH
    P2 -> HIGH
    P3 -> MEDIUM
    P4 -> LOW
```

The holdout also confirmed when **not** to use it:

```text
FR-04 / FR-05:
    condition -> mandatory action
    is not conditional result selection

FR-06:
    top-N recency selection
    is not a per-item decisionRule

FR-10:
    rollback support
    does not imply an automatic rollback decisionRule
```

### 3.4 `classify`

`classify` emerged as substantially more useful than the initial extraction practice suggested.

Forward positive semantic kinds include:

```text
Capability
ActivationCondition
AdaptationCandidate
LifecycleResult
ModelVersion
AcceptanceCriterion
Threshold
Behavior
Store
Artifact
EvidenceWindow
EvidenceSet
EvidenceQualificationCondition
SupervisionTarget
Component
```

This exposes a likely **application-completeness issue**, not a missing methodology construct.

`CLASSIFICATION_COVERAGE_REVIEW_EVIDENCE` therefore remains open for a complete post-holdout
audit.

### 3.5 Documentation gap vs methodology pressure

The holdout strongly validated this distinction.

Example:

```text
FR-13/14/15

source:
    explicit non-implication / non-sufficiency meaning

BA:
    cannot represent it directly

result:
    METHODOLOGY PRESSURE
```

versus:

```text
DEC-07

source:
    says overall accuracy may degrade at most 5%
    but does not fully define arithmetic/population binding

result:
    DOCUMENTATION GAP
```

FR-06 demonstrates both at once:

```text
explicit:
    select the 20 most recent pertinent corrections

BA cannot structurally preserve:
    recency ranking + bounded membership
        -> methodology pressure

source does not define:
    ties / deduplication / underfill / reuse
        -> documentation gap
```

This is one of the most valuable outcomes of the holdout.

## 4. Final methodology pressure evidence

### P-01 — Function/process/behavior identity binding

```text
status:
    CARRIED / MATERIAL
```

Behavior identities repeatedly matter independently of propositions and implementations.

### P-02 — Pipeline composition/order

```text
status:
    CARRIED
```

Sequential pipeline composition remains relevant and distinct from serialized proposition order.

### P-03 — Interface/path/invocation association

```text
status:
    STRONG
```

The API/integration branch showed that endpoint/path/service binding cannot be reconstructed
from generic transfer/service semantics alone.

### P-04 — Boundary/interaction association

```text
status:
    STRONG
```

Interaction and trust/boundary meaning require explicit association.

### P-05 — Ordered comparison vocabulary

```text
status:
    STRONG_REPEATED
```

Counterexamples include:

```text
greater-than
at-most
not-worse-than
threshold reach
post-adoption degradation > R
pre-adoption degradation within T
```

The post-holdout review should consider a minimal coherent ordered-comparison family, not only
one isolated `greaterThan`.

### P-06 — Scalar/property-addressing comparison

```text
status:
    STRONG_REPEATED
```

The holdout requires comparisons such as:

```text
candidate.sensitivity
    vs reference.sensitivity

candidate.falseLowPerformance
    vs reference.falseLowPerformance

candidate.overallAccuracy
    vs reference.overallAccuracy
```

This is related to P-05 but not identical.

### P-07 — Structured data/information contract

```text
status:
    STRONG
```

Input/output contracts, review payloads and training-input rules repeatedly require structured
information semantics.

### P-08 — Artifact/store/persistence association

```text
status:
    STRONG_REPEATED
```

Concrete examples:

```text
models/versions/
db/model_versions.json
models/efficientnet_b4.pth
db/prompts.json
ChromaDB / historical retrieval persistence evidence
```

The current relation vocabulary cannot preserve all `storedIn`, `persistedAt`, `trackedBy` and
active-artifact bindings without semantic approximation.

## 5. Final unnumbered pressure evidence

```text
ACQUISITION_REFRESH_ACTION_SEMANTICS
    REPEATED / FURTHER_STRENGTHENED

CONDITIONAL_ACTION_TRIGGER_SEMANTICS
    REPEATED

DATA_EVIDENCE_CONSUMPTION_SEMANTICS
    REPEATED / FURTHER_STRENGTHENED

NEGATIVE_IMPLICATION_NON_SUFFICIENCY_SEMANTICS
    STRONG_REPEATED

BOUNDED_RECENCY_SELECTION_SEMANTICS
    HOLDOUT_PRESSURE_EVIDENCE
```

Additional evidence not yet promoted to a separate pressure topic:

```text
CONFIGURATION_APPLICABILITY_BINDING_EVIDENCE
    PromptVersion used by Qwen2-VL / BioMistral
    SINGLE_HOLDOUT_EVIDENCE
    review against existing relation pressures first
```

No new numbered pressure was created during the frozen holdout.

## 6. Final source-governed documentation gap register

The governed source preserves the following open gaps:

```text
Diagnostic authority boundary

GAP-DERMA-NOIMAGE-INPUT-01
GAP-DERMA-PMAP-INPUT-01
GAP-DERMA-NOIMAGE-PMAP-BINDING-01
GAP-DERMA-SLA-01
GAP-DERMA-PATH-01

Specialist selection semantics

GAP-DERMA-REVIEW-CONTENT-01
GAP-DERMA-REVIEW-LIFECYCLE-01
GAP-DERMA-REVIEW-DISAGREEMENT-BINDING-01

GAP-DERMA-ADAPT-COUNTING-01
GAP-DERMA-ADAPT-THRESHOLD-AUTH-01
GAP-DERMA-PROMPT-WINDOW-01
GAP-DERMA-SUPERVISION-INPUT-01

GAP-DERMA-DEPLOY-01
GAP-DERMA-ACCEPT-BINDING-01
GAP-DERMA-ROLLBACK-BINDING-01
GAP-DERMA-EVAL-CONSISTENCY-01
```

Important final rule:

```text
absence of detail
    != automatic documentation gap

only a required unresolved meaning
    -> gap
```

Intentional decomposition stops and explicit out-of-scope meanings remain distinct from gaps.

## 7. Reconciliation state

Resolved or locally resolved:

```text
R-02 specialist destination indication vs full routing
    RESOLVED

R-11 B4 client logical placement
    RESOLVED_FOR_CURRENT_EVIDENCE

BAREF-DERMA-078 QualifiedClassifierDisagreementEvidence
    SPECIFIC FR-07 RECHECK RESOLVED
    now WORKING_ACCEPTED
```

Still open:

```text
R-08 triage output / indication binding
R-09 original outcome identity
R-10 review/validation/validated-outcome identity
R-12 administrative client identity/placement
R-13 broader clinical-review evidence identity/lineage
R-14 classifier reference-model identity/lineage
R-15 post-adoption reference identity/lineage
R-16 training qualified-correction evidence identity
```

These must be reconciled before integrated BA6 claims semantic closure.

## 8. Construct-test result

```text
BAReferent:
    TESTED_POSITIVE_STRONG

BAProposition:
    TESTED_POSITIVE_STRONG

transfer:
    TESTED_POSITIVE_STRONG

transfer.behavior:
    TESTED_POSITIVE_CROSS_CORPUS_STRONG

produce:
    TESTED_POSITIVE_STRONG

create:
    NOT_TESTED_POSITIVE_IN_DERMATRIAGE

observe:
    TESTED_POSITIVE_STRONG

transition:
    NOT_TESTED_POSITIVE_IN_DERMATRIAGE

correlate:
    TESTED_POSITIVE_STRONG

reference:
    NOT_TESTED_POSITIVE_IN_DERMATRIAGE

dependOn:
    TESTED_POSITIVE_STRONG

consumeService:
    TESTED_POSITIVE_STRONG

realize:
    TESTED_POSITIVE_STRONG

assignResponsibility:
    TESTED_POSITIVE_STRONG

constrain:
    TESTED_POSITIVE_STRONG

classify:
    TESTED_POSITIVE_STRONG_IN_DERMATRIAGE

decisionRule:
    TESTED_POSITIVE_STRONG_IN_DERMATRIAGE
```

Unused constructs are **NOT_TESTED**, not failures and not reasons to force artificial coverage.

## 9. Key methodological observations

```text
O-03 DATA / INTERACTION COMPLETENESS
O-04 LOGICAL FLOW != PHYSICAL EXCHANGE
O-05 SERVICE CONSUMPTION != TRANSFER != RESPONSIBILITY
O-06 INTENTIONAL DECOMPOSITION STOP != GAP
O-07 SEMANTIC PRESERVATION != STORAGE IMPLEMENTATION
O-08 RECORDING != ORIGIN / AUTHORSHIP
O-09 DOCUMENTATION DETAIL STATUS MUST BE EXPLICIT
O-10 AUTHENTICATION != TRANSPORT PROTECTION
O-11 AUTH MECHANISM != CREDENTIAL != LIFECYCLE
O-12 NOT GOVERNED / OUT OF SCOPE != NEGATIVE RESPONSIBILITY
O-13 THRESHOLD VALUE != COMPLETE TRIGGER RULE
O-14 CROSS-BRANCH SEMANTIC CONSUMPTION != HIERARCHY OWNERSHIP
O-15 SHARED DATA / PROJECT CONTEXT != SEMANTIC EQUIVALENCE / RULE INHERITANCE
O-16 NON-SUFFICIENCY != MUTUAL EXCLUSION / NEGATIVE STATE
O-17 SEMANTIC KIND != CONTEXT-RELATIVE QUALIFICATION
O-18 LIFECYCLE RESULT != LIFECYCLE STATE
O-19 PRODUCTION != QUALIFICATION != ADOPTION / DEPLOYMENT
O-20 NON-DEGRADATION != EQUALITY
O-21 SAME LITERAL != SAME SEMANTIC IDENTITY
O-22 SUPPORT RESPONSIBILITY != DECISION / AUTHORIZATION RESPONSIBILITY
O-23 SELECTION WINDOW != SELECTED EVIDENCE SET
O-24 BOUND SIZE != MEMBERSHIP RULE
```

These observations are important candidates for the future authoring/documentation guide because
they explain recurrent modeling errors in ordinary project documentation.

## 10. Strengths of DDTA demonstrated by the holdout

### Authority preservation

DDTA maintained a stable authority chain from governed source to BA and prevented source meaning
from being invented by downstream projections or threat-analysis methods.

### Explicit non-inference

The methodology made absence meaningful without turning it into negative truth.

Examples:

```text
no governed deployment authority
    != DermaTriage forbidden to deploy

condition A does not imply condition B
    != condition B is false

omitted decisionRule ELSE
    != implicit reject/fallback
```

### Localized diagnostics

When a representation failed, the evidence could be attributed to a bounded source and a
specific semantic need.

### Documentation feedback

The BA exposed incomplete project documentation through concrete missing bindings rather than
generic statements such as "more detail is needed."

### Projection readiness

Stable identity, classification and explicit propositions create a credible basis for
deterministic view selection without reparsing the source.

## 11. Weaknesses / costs exposed by the holdout

### Analyst-discipline cost

The method strongly depends on disciplined distinction among identity, classification,
relationship and inference. The discovery of likely under-application of `classify` is direct
evidence of this cost.

### Reconciliation overhead

Preserving identity instead of prematurely merging meanings creates a reconciliation backlog.
This is intentional but operationally expensive.

### Relation-vocabulary incompleteness

Several common engineering semantics remain outside the frozen BA2 vocabulary:

```text
ordered comparisons
persistence/store binding
conditional mandatory actions
evidence consumption
bounded top-N selection
negative implication / non-sufficiency
acquisition/refresh actions
```

### No integrated projection proof yet

The BA has not yet been used to materialize the complete DermaTriage projection set.

### Incomplete construct coverage

`create`, `transition` and `reference` did not receive clean positive DermaTriage examples.
They must remain NOT_TESTED for this holdout rather than being forced.

## 12. How DDTA can improve documentation

The holdout suggests concrete authoring improvements.

Documentation should explicitly distinguish:

```text
identity
semantic kind
responsibility
authority
behavior
result
state
artifact/store
interface/path
data contract
comparison property
reference baseline
threshold role
trigger
selection rule
```

Numeric literals should be accompanied by semantic binding.

Badly under-specified:

```text
degradation <= 5%
```

Better governed documentation must clarify when required:

```text
which metric
which reference
which population
relative vs absolute interpretation
observation window
decision effect
owner / authority
```

Collection rules should distinguish:

```text
bound size
eligibility
ordering
tie handling
deduplication
underfill
reuse / overlap
```

Lifecycle wording should distinguish:

```text
qualified
accepted
adopted
deployed
revoked
restored
```

and state explicitly who owns each authority.

Persistence documentation should name:

```text
what is persisted
where
which identity/version it represents
who updates it
how active state is selected
retention/history semantics
```

This is the practical documentation-improvement value demonstrated by DDTA.

## 13. Final holdout assessment

Current conclusion:

```text
SEMANTIC EXTRACTION:
    STRONG / PROMISING

METHOD MINIMALITY:
    PROMISING
    no holdout mutation required

PRESSURE LOCALIZATION:
    STRONG

DOCUMENTATION DIAGNOSTICS:
    STRONG

CLASSIFICATION APPLICATION COMPLETENESS:
    OPEN / REVIEW REQUIRED

RECONCILIATION:
    OPEN

BA4 PROJECTION MATERIALIZATION:
    NOT YET EXECUTED

INTEGRATED DERMATRIAGE BA6:
    NOT YET EXECUTED

FULL METHODOLOGY VALIDATION:
    NOT YET CLAIMED
```

The strongest defensible statement at this stage is:

```text
DDTA can preserve most governed meaning in a method-neutral Base Analysis,
identify where its frozen representation vocabulary is insufficient,
separate those insufficiencies from documentation incompleteness,
and prevent downstream analysis from silently inventing missing project truth.
```

## 14. Required post-holdout sequence

Do not immediately edit BA0–BA6.

Perform:

```text
1. POST-HOLDOUT PRESSURE REVIEW
   review P-01..P-08 and all unnumbered evidence

2. CLASSIFICATION COVERAGE AUDIT
   apply the existing classify mechanism consistently across the complete DermaTriage BA

3. RECONCILIATION PASS
   resolve or explicitly retain R-08..R-16

4. EFFECTIVE BA REBUILD
   produce one complete reconciled DermaTriage BA

5. INTEGRATED BA6
   test completeness, traceability, authority preservation and unresolved evidence

6. DETERMINISTIC PROJECTION TEST
   materialize canonical views from accepted BA without reparsing the source

7. ONLY THEN
   optional STRIDE / threat-method interpretation
```

Recommended first projection set:

```text
Data Exchange View
Responsibility / Service Interaction View
Authentication + Boundary View
Adaptation / Evidence / Lifecycle View
```

The projection test criterion remains:

> Can the relevant views be reconstructed from accepted BA without reinterpreting the governed
> source?

That is the next major validation step.
