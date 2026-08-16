# BA0-T3 - Base Analysis responsibility and non-goals closure review

**Revision:** R1

**Status:** CLOSED

**Repository baseline reviewed:** `ced13f9329c89c759b3608d66c3f81ac79b9469b`

**Phase:** `BA0 - Base Analysis responsibility and boundary`

**BA1 status at completion:** `NOT STARTED`

## 1. Purpose and closure question

BA0-T3 reviews BA0-R, BA0-T1 and BA0-T2 together and asks only whether the Base Analysis responsibility boundary is now precise enough to begin ontology work without importing a pre-approved type list, a threat-method model, a tool-native representation, or a second project source of truth.

The closure question is:

> What is the minimum methodology-neutral responsibility of Base Analysis between governed documentation, progressive human understanding, method-specific analysis, corrective feedback and change-aware re-analysis?

This review does not design BAE types, relations, view schemas, provenance serialization, Common Finding, STRIDE overlays or implementation structures.

## 2. Evidence basis

The review uses:

- [BA0-R closure](../literature/syntheses/BA0_R_CLOSURE_R1.md);
- [BA0-T1 trial](BA0_T1_FR3_4_APPLICATION_TRIAL_R1.md) and its provisional ledger;
- [BA0-T2 trial](BA0_T2_ANALYSIS_CONSUMPTION_TEACHABILITY_GOVERNED_FEEDBACK_TRIAL_R1.md) and its provisional ledger;
- [BA0 Working Hypothesis R2](BA0_BASE_ANALYSIS_WORKING_HYPOTHESIS_R2.md);
- [research questions](../research/research-questions.md);
- [candidate contributions](../research/contributions.md);
- [candidate hypotheses](../research/hypotheses.md);
- [Work Plan R4](DDTA_RESEARCH_WORK_PLAN_AFTER_DOCUMENTATION_CLOSURE_R4.md).

No Chapter 2-4 reopen criterion is triggered by this review. No new external literature claim is introduced.

## 3. Exit criteria inherited from BA0-R and R4

BA0 can close only if the review can decide, without ontology design:

1. the responsibility of Base Analysis;
2. the authority boundary between governed documentation and analysis;
3. what semantic canonicality means;
4. why a shared analytical representation is needed rather than independent re-interpretation by every consumer;
5. how origin/provenance and unresolved uncertainty are handled at responsibility level;
6. whether human progressive views, method projections, diagnostics, corrective feedback and change impact belong to the responsibility boundary;
7. explicit non-goals;
8. whether remaining uncertainty is properly deferred to BA1-BA6.

## 4. Falsification review

### 4.1 Could Base Analysis become a second project source of truth?

Yes, if analytical normalization or tool inference were allowed to create project commitments silently.

BA0-R and T1 already reject that move. T2 reinforces the boundary by returning the recognition-unavailability question as a corrective documentation candidate instead of inventing an access policy.

**Disposition:** the risk is controlled only if governed documentation remains project authority and every Base Analysis proposition that claims project meaning retains source/origin provenance. This responsibility is retained.

### 4.2 Does BA0 need one physically persistent canonical graph?

No. T1 shows that stable shared meaning is useful while persistence remains unproven. T2 demonstrates that human and method-specific projections can consume the same accepted semantics without requiring one storage technology.

**Disposition:** semantic canonicality is retained; physical canonical persistence is rejected as a BA0 requirement.

### 4.3 Does every useful semantic responsibility need a first-class BAE type?

No. BA0-R and T1 directly falsify this. Transport, realization, correlation, failure semantics, security applicability and responsibility separation may be analytically relevant without implying autonomous metaclasses.

**Disposition:** no BAE type is accepted by BA0-T3. Representation form remains BA1-BA4 work.

### 4.4 Must method-specific semantics enter the shared core to make analysis possible?

No. T2's bounded STRIDE probe consumes shared source/destination/information/correlation/responsibility semantics and keeps STRIDE dispositions outside the common core.

**Disposition:** method neutrality and consumer isolation are retained as Base Analysis responsibilities.

### 4.5 Is progressive teachability itself a Base Analysis workflow?

Not as a visualization or usability workflow. T2 only demonstrates that the same semantics can support an overview-to-source ladder.

However, if Base Analysis could not support bounded non-authoritative projections and source drill-down, the thesis would require a second independently authored model for human comprehension, undermining shared meaning and provenance.

**Disposition:** retain only **projection readiness and drill-down support** as a Base Analysis responsibility. Exact view types, rendering and empirical usability remain BA4/evaluation concerns.

### 4.6 Does Base Analysis own governed corrective feedback?

No. R2 is too broad if read as assigning the correction workflow to Base Analysis. Governed documentation already owns project decisions and acceptance.

T2 supports a narrower responsibility: an analysis result, insufficiency or diagnostic must be able to point back through shared semantics to the governed source area that requires review.

**Disposition:** replace `governed corrective feedback` as an operational BA responsibility with **source-localized feedback handoff**. Document ownership, decision-making, acceptance and lifecycle remain in documentation governance and later analysis workflow.

### 4.7 Is a reviewed analytical addition a required Base Analysis origin class?

Not proven. T1 rejected an unnecessary invented endpoint. T2 encountered missing project semantics and correctly returned a documentation gap rather than adding an analysis-layer project fact.

RQ1 requires explicit review of derived elements, but the current evidence does not require a standing class of shared-core analytical additions that introduce new project meaning.

**Disposition:** `grounded`, `derived` and `diagnostic/unresolved` responsibilities are retained. `reviewed analytical addition` is **DEFERRED / NOT REQUIRED BY BA0**. If BA1-BA6 later establishes a necessary methodology-neutral analytical construct not directly grounded in project commitments, it must remain explicitly non-project-authoritative, provenance-bearing and reviewed; that future case may trigger a BA0 reopen if it changes the responsibility boundary.

### 4.8 Must BA0 automatically detect every contradiction or ambiguity in governed documentation?

No. Reliable semantic contradiction detection over arbitrary narrative would exceed the current thesis scope and would collapse BA into an extraction/validation engine.

BA0 does need a rule for what happens when conflicting, ambiguous or insufficient evidence is encountered during derivation or consumption: it must not be silently resolved into accepted project meaning.

**Disposition:** retain **explicit unresolved/diagnostic state and localization**. Automatic discovery of all inconsistencies is not a BA0 requirement.

### 4.9 Does BA0 own re-analysis orchestration after changes?

No. RQ4 requires that provenance and baselines identify affected analytical artifacts; it does not require Base Analysis itself to schedule or execute analyses.

**Disposition:** retain **change-impact traceability** as a Base Analysis responsibility; exact identity lifecycle, stale-state rules and re-execution orchestration remain BA3, BA6 and the later analysis envelope.

## 5. Disposition of the R2 working invariants

| R2 item | T3 disposition | Closure interpretation |
|---|---|---|
| BA0-I1 Source authority | RETAIN | Governed documentation remains project authority. |
| BA0-I2 Analysis-layer semantic canonicality | RETAIN / REFINE | Stable accepted baseline-scoped identity and meaning; persistence optional. |
| BA0-I3 Explicit origin and provenance | RETAIN | Required for drill-down, review, feedback and change impact. |
| BA0-I4 No silent inference authority | MERGE | Consequence of source authority, provenance and explicit unresolved state. |
| BA0-I5 Method neutrality | RETAIN | Method-owned semantics stay outside the shared core. |
| BA0-I6 Representation independence | MOVE TO CLOSED NON-GOAL | No graph DB, notation, renderer or serialization is mandated by BA0. |
| BA0-I7 Bounded modeling scope | RETAIN AS MINIMALITY CONSTRAINT | Include only semantics justified by shared understanding/analysis/provenance/change needs. |
| BA0-I8 Change alignment and scoped revalidation | RETAIN / REFINE | BA must support impact identification; it does not own re-execution orchestration. |
| BA0-I9 Diagnostic visibility and localization | RETAIN / REFINE | Encountered ambiguity/conflict/insufficiency must remain explicit; universal detection is not required. |
| BA0-I10 No method/tool semantic ownership | MERGE | Consequence of source authority, method neutrality and representation independence. |
| BA0-I11 Progressive teachability | RETAIN / REFINE | Projection readiness and source drill-down, not a visualization/usability claim. |
| BA0-I12 Governed corrective feedback | REDUCE | BA supports source-localized feedback handoff; governance remains outside BA. |
| BA0-I13 Consumer isolation with shared meaning | MERGE | Covered by shared semantic identity plus method neutrality. |

The reduction from thirteen working invariants to a smaller closed responsibility set is intentional. BA0 closure should define the boundary, not pre-design the metamodel.

## 6. Closed Base Analysis responsibility statement

For a governed documentation baseline, **Base Analysis is the accepted methodology-neutral analytical representation of the shared project meaning required by DDTA**. It preserves baseline-scoped semantic identity, source/origin provenance and explicit unresolved state sufficiently to support reproducible reuse, progressive human and method-specific projections, source drill-down, change-impact reasoning and source-localized feedback handoff.

Base Analysis is **not project authority**. Governed documentation is. Base Analysis may normalize and derive analytical structure from governed meaning, but it must not silently create project commitments. Method-specific interpretations and analysis outputs remain outside the shared core.

The representation may be reused or reproducibly rebuilt. Semantic canonicality does not require one permanently materialized graph, one storage technology, one diagram or one modeling notation.

## 7. Closed responsibility set

### BA0-C1 - Authority and provenance boundary

Project facts represented in Base Analysis must be grounded in governed documentation, with origin and source traceability. Derived analytical normalization must remain distinguishable from source-stated meaning. No tool, method or analyst inference may silently become project truth.

### BA0-C2 - Baseline-scoped shared semantic identity

For a governed baseline, analytically relevant referents and propositions must have stable enough accepted identity and meaning to be reused across consumers, projections, comparison and revalidation. Exact identity/equivalence mechanics remain deferred.

### BA0-C3 - Method-neutral shared core

Base Analysis contains shared project semantics rather than STRIDE, STRIDE-AI or other method-owned threat semantics. Consumers may project the common meaning and attach isolated method-specific interpretation without redefining the core.

### BA0-C4 - Explicit uncertainty and diagnostic localization

When derivation or consumption encounters conflicting, ambiguous, missing or insufficient evidence, Base Analysis must preserve that unresolved status and enough provenance/context to localize review rather than silently selecting a project fact. BA0 does not require universal automatic inconsistency detection.

### BA0-C5 - Projection readiness and source drill-down

The same accepted semantics must support bounded, non-authoritative projections for progressive human understanding and method consumption, with a path back to exact governed sources. Exact view contracts and usability claims remain deferred.

### BA0-C6 - Change-impact traceability

The representation must preserve enough source, semantic and dependency linkage to identify which analytical meaning may require review after a relevant governed-source change and to support later targeted re-analysis. BA0 does not define the material stale-state/re-execution mechanism.

### BA0-C7 - Source-localized feedback handoff

Analysis results, insufficiencies and diagnostics must be able to reference the shared semantics and governed source area that motivates review. Base Analysis does not choose the corrective policy, document kind, acceptance decision or governance lifecycle.

### BA0-C8 - Minimality and representation independence

Base Analysis includes only methodology-neutral semantics justified by shared project understanding, multi-consumer analysis, provenance, diagnostics, projection or change/re-analysis needs. It is not required to be a complete systems model, and its responsibility is independent of one storage, graph, notation, renderer or implementation technology.

## 8. Origin-state closure

At BA0 responsibility level:

- **grounded:** REQUIRED;
- **derived:** REQUIRED, with explicit provenance and no new project commitment;
- **diagnostic / unresolved:** REQUIRED as an explicit state when accepted meaning cannot be justified;
- **reviewed analytical addition:** DEFERRED / NOT REQUIRED BY BA0.

This is not a material schema. BA3 must define the concrete provenance/review model. BA1 must not interpret these labels as BAE metaclasses by default.

## 9. Closed non-goals

Base Analysis is not responsible for:

- replacing governed project documentation or its governance workflow;
- reliable automatic extraction or migration from arbitrary, legacy or unstructured narrative;
- silently accepting LLM/NLP/tool/analyst inference as project truth;
- automatically discovering every contradiction or ambiguity in arbitrary text;
- defining the final BAE type taxonomy in BA0;
- requiring every useful semantic responsibility to become a first-class metaclass;
- copying SysML, KerML, ArchiMate, AADL or another general-purpose modeling language;
- being a STRIDE DFD, STRIDE-AI model or universal threat-analysis ontology;
- defining AnalysisRecord, Common Finding, Finding-to-SecurityRequirement acceptance or formal overlay schemas;
- governing corrective project decisions or choosing the target document type;
- proving universal support for every threat-analysis method;
- enforcing one persisted graph, database, serialization, diagram or renderer;
- empirically proving that a particular visualization reduces reading time or improves comprehension;
- executing or scheduling downstream re-analysis itself.

## 10. Questions deliberately deferred after BA0

The following are not BA0 closure blockers:

- which responsibilities become first-class BAE types, relations, roles, properties, constraints or projections - BA1;
- minimal relation and canonical action vocabulary - BA2;
- exact identity/equivalence/lifecycle rules, source locators, provenance materialization, review state and stale state - BA3;
- exact progressive-human and method-specific view/projection contracts - BA4;
- controlled vocabulary and optional authoring/extraction assistance - BA5;
- holdout regression, broader method-neutrality pressure and full Base Analysis closure - BA6;
- AnalysisRecord, Common Finding and formal overlay contracts - after BA6.

## 11. Alignment with research questions and hypotheses

The closed boundary preserves the thesis commitments without expanding them:

- RQ1/H1: governed documentation can yield a reviewed methodology-neutral Base Analysis with provenance and explicit review of derived structure;
- RQ2/H2: distinct methods can consume the same semantic core while method-owned meaning remains isolated;
- RQ3/H3: later accepted findings can retain provenance through Base Analysis to governed project subjects without making BA the governance owner;
- RQ4/H4: baseline/source/dependency traceability can support identification of impacted analytical artifacts after change.

The closure does not claim that these research questions or hypotheses are already empirically proven.

## 12. Closure decision

The falsification review found two R2 overextensions - operational ownership of governed corrective feedback and the implied necessity of a reviewed analytical-addition class - but neither requires a new BA0 experiment once narrowed as above.

The remaining open questions concern representation choices, schemas, projection contracts and regression evidence rather than the responsibility boundary itself.

**Decision: `BA0 RESPONSIBILITY AND NON-GOALS = CLOSED`.**

**No BAE type or relation is accepted by BA0-T3.**

**BA1 remains `NOT STARTED` by this microstep.**

The next authorized microstep after this closure is:

> **BA1-T1 - minimal BAE ontology candidate derivation from the closed BA0 responsibilities.**

BA1-T1 must begin from BA0-C1..C8, BA0-R prior-art pressure and the governed DDTA corpora. Historical `actor/component/asset/boundary/data_flow` categories, ThreatForge structures, STRIDE DFD elements and systems-modeling metaclasses are candidates only if independently justified; none is inherited as accepted ontology.

## 13. Reopen criteria

Reopen BA0 only if a later phase produces a material responsibility-level counterexample, for example:

1. BA1-BA3 requires a methodology-neutral semantic responsibility that cannot fit BA0-C1..C8 without changing the boundary;
2. a concrete method consumer can operate only by moving method-owned semantics into the shared core;
3. provenance/identity work shows that governed-document authority cannot be preserved under the closed boundary;
4. BA4 cannot generate coherent human/method projections without introducing a second independently authored project model;
5. BA6 holdout regression reveals that the closed responsibilities are insufficient or mutually inconsistent.

Ordinary choices among types, relations, properties, storage technologies or renderings do not reopen BA0.
