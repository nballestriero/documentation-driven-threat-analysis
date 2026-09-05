# DDTA R25 - Base Analysis Work Plan after DermaTriage Promotion R1

**Status:** ACTIVE / BASE ANALYSIS AUTHORIZED TO START AFTER PROMOTION COMMIT  
**Promotion predecessor:** `bf2236cf921b73309b162c74af11e4edb6e95db9`  
**Project authority:** `DERMATRIAGE-GOV-R1`  
**Documentation-authoring methodology authority:** `DDTA_DOCUMENTATION_BA_AUTHORING_GUIDE_R5`  
**Base Analysis operational guide:** `DDTA_BASE_ANALYSIS_OPERATIONAL_GUIDE_R3`  
**Threat analysis:** BLOCKED UNTIL ACCEPTED BA

## 1. Current state

DermaTriage documentation is now promoted as a current governed project baseline and may be used as the primary source for Base Analysis.

The active project source is:

`governed-corpora/dermatriage/current-r1/`

The authority registry must classify it as:

```text
authorityBaselineKey: DERMATRIAGE-GOV-R1
authorityStatus: CURRENT_GOVERNED
primaryBASourceAllowed: true
```

The exact Git commit created after applying and reviewing the promotion drop-in becomes the concrete BA source revision. Record that full SHA before creating the first accepted BA element.

## 2. Authority discipline for BA

Base Analysis consumes the promoted project documentation. It does not decide missing project meaning.

For every BA candidate:

- ground identity and propositions in `DERMATRIAGE-GOV-R1`;
- preserve documentation gaps and `NOT SPECIFIED` meanings;
- do not reopen the original holdout package merely to add project meaning absent from the governed baseline;
- do not promote implementation assumptions, threat-method needs or tool convenience into project truth;
- if a material mismatch is found, route it back as a documentation-review trigger and rebuild/revalidate BA only after governed documentation changes.

## 3. BA execution sequence

Use the current BA contracts and operational guide without changing them opportunistically for DermaTriage.

```text
BA0  responsibility / authority boundary
  -> pin DERMATRIAGE-GOV-R1 + exact promotion commit

BA1  minimum reusable BAReferent identities
  -> create only identities needed by governed meaning

BA2  BAProposition operators / roles / structures
  -> represent governed assertions without inventing missing topology or behavior

BA3  provenance / derivation / lifecycle / freshness
  -> link propositions to their governed sources and change context

BA4  projection / traceability / interpretation / coverage
  -> materialize consumer views only from accepted BA

BA5  canonical semantic registry / controlled authoring
  -> normalize names, aliases and reusable bindings

BA6  integrated acceptance
  -> remains an explicit later gate
```

## 4. DermaTriage-specific BA pressure points

The promoted documentation makes the following concrete meanings available for BA review without requiring pre-BA manual normalization:

- image-based four-stage pipeline;
- EfficientNet-B4 classification behavior;
- Qwen2-VL-7B-Instruct clinical-description behavior;
- ChromaDB / all-MiniLM-L6-v2 historical-case retrieval;
- BioMistral-7B multi-source synthesis;
- direct `/analyze` and B4-integrated `/diagnose` paths;
- B4 external-service interactions and authentication mechanisms;
- symptom-only triage path;
- P-scale mapping;
- clinical review/correction correlation;
- prompt evolution and PromptManager state;
- classifier retraining/versioning/rollback behavior;
- cross-MR dependency from controlled adaptation to clinical review;
- explicit gaps around diagnostic authority, specialist routing semantics, SLA semantics and other unresolved bindings.

BA decides which of these require reusable referent identity and which assertions require BAProposition identity. The documentation does not pre-normalize that answer.

## 5. First bounded BA task

Start with BA0 and a source-grounding inventory over the promoted DermaTriage baseline.

Do not build diagrams first.

The first useful checkpoint should contain:

1. exact authority key and promotion commit;
2. proposed minimal BAReferent set with source links;
3. proposed BAProposition set for one bounded branch, preferably MR-01;
4. explicit `NOT SPECIFIED` / gap carry-through;
5. regression against the documentation to verify that no governed distinction was lost;
6. no STRIDE/STRIDE-AI interpretation yet.

## 6. Views and diagrams

Architecture/data-flow/component views are generated only after the relevant BA is accepted. They are deterministic or reproducible projections of BA semantics, not manually authored project documentation and not a source of new project meaning.

## 7. Stop conditions

Stop and return to documentation governance if BA requires a project fact that the current baseline does not establish.

Stop before threat analysis until the minimum BA required for the chosen consumer is explicitly reviewed and accepted.
