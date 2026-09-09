# General Discovery + Specific Pack Validation Protocol R1

```text
artifactKind: METHOD_OBSERVATION
normativeStatus: CANDIDATE_FOR_INTEGRATED_BA_GUIDE_REVISION
documentationAuthoringMethodMutation: NONE
```

Hypothesis: construct-specific packs are more reliable when preceded by a short neutral semantic discovery pass over the **entire governed documentation**.

```text
governed documentation
 -> GENERAL_BA_SEMANTIC_DISCOVERY_PACK
 -> candidate facts + routing
 -> construct-specific packs
 -> representation tests / delete-merge-first
 -> accepted BA / rejected inference / application QA / documentation QA / method pressure
```

This is intended to reduce confirmation bias, source-verb/operator mapping, missed negative controls and missed cross-construct routing.

The packs MUST NOT create project truth, requirements, gaps, or automatic BA mutations.

R21 uses OP-05 `transition` as the first explicit end-to-end validation target.

Success dimensions:

```text
REVIEW_COMPLETENESS
SEMANTIC_ROUTING
APPLICATION_QA
DOCUMENTATION_QA
NON_INFERENCE
```

Normative promotion is deferred to integrated BA-method revision.
