# Automated trace-link recovery source cluster

## Purpose

Establish a reproducible benchmark floor before evaluating transformer, RAG or LLM-assisted
trace-link recovery for DDTA. This cluster separates method novelty from benchmark quality,
dataset coverage, absolute usefulness and reproduction completeness.

## Analyzed

### SRC-0024 - Wang et al. (2024)

Role: empirical RC-TLR benchmark and SOTA-selection framework. The paper reviews work from
2018 to 2023, selects candidate methods through quality and evidence scoring, and replicates
comparisons on 13 Java datasets.

The key result is not one universal winning algorithm. Method rankings change by dataset,
threshold, classifier, training ratio and class-balancing strategy. Classical IR and random
forest baselines remain credible comparisons in the study. On larger datasets, even the best
F1 values are often modest, so relative ranking must not be confused with operational adequacy.

Temporal caveat: the source is current as a 2024 benchmark floor, not as a complete 2026 SOTA
ranking. It treats GPT as future work and does not evaluate later RAG or LLM approaches.

Reproducibility caveat: the paper publishes a companion repository, but the pinned README
requires separately supplied corpora, CoreNLP and some large datasets and redirects two method
implementations to external repositories. The package is therefore useful but not self-contained.

## Provisional synthesis for DDTA evaluation

SRC-0024 and SRC-0025 jointly support the following benchmark and pipeline controls:

- pin method, dependency and dataset versions;
- publish the ground-truth provenance and negative-pair construction;
- use multiple projects and report per-project results;
- retain simple IR and classical-ML baselines;
- separate threshold tuning from final evaluation;
- report precision, recall and F1 together;
- add analyst-review effort, accepted-candidate yield and confidence calibration;
- test unseen projects, languages and artifact types;
- distinguish relative rank from absolute usefulness;
- record unavailable dependencies and partial reproduction packages as limitations;
- evaluate preprocessing separately from end-to-end recovery;
- preserve filtered fragments and record every exclusion decision;
- report rare-class precision and recall instead of relying only on weighted averages;
- distinguish fixed deployable thresholds from gold-optimized upper bounds;
- verify that a filter's semantics match the overlay task.

For the DDTA overlay, trace recovery is only one evaluation layer:

```text
document extraction
-> candidate trace recovery
-> reviewed semantic relation
-> finding generation
-> security requirement derivation
-> implementation and verification trace
```

A gain in requirement-to-code F1 does not establish improvement in finding quality or threat
coverage. Likewise, text that is irrelevant to functional code mapping may be essential security
or operational evidence. Those outcomes and filtering semantics require separate ground truth
and expert review.

## Next sources

### SRC-0025 - Hey, Keim and Corallo (2024)

Role: pretrained-transformer classification as task-specific preprocessing for requirement-to-code
recovery. The paper labels requirement elements, evaluates NoRBERT with an unseen-project design
and filters FTLR inputs before link recovery.

The automated functional-aspect filter yields a modest but statistically significant improvement
in the reported setup. With optimized thresholds, FTLR improves from 37.8 to 38.8 percent average
F1; combining template and functional filters reaches 40.7 percent. The user-related filter reduces
average performance because recall falls. Aggregate classification scores also conceal severe
rare-class behavior: the LibEST user-related class has 80 percent recall but only 1.7 percent
precision.

The main refinement to SRC-0024 is that preprocessing is itself a governed model component.
Its labels, confidence, class balance and errors determine which evidence reaches recovery.
Gold-standard classifications and per-project optimized thresholds are upper bounds and must be
kept separate from deployable performance.

Temporal caveat: NoRBERT is BERT-based 2024 evidence, not a generative-LLM evaluation. The
method ranking and absolute performance need post-2024 corroboration.

Reproducibility caveat: Zenodo v2 and the associated GitHub repository provide code, results,
datasets, installation guidance and Docker references. The package was structurally audited but
not executed in this reading workflow.

### SRC-0026 candidate - MTLink

Evaluate issue-to-commit recovery, pretrained language-model transfer, class imbalance,
cross-project behavior and the reproducibility of the published Zenodo package.

### Later RAG and LLM sources

Select peer-reviewed full-text studies that report:

- explicit baseline versions;
- unseen-project or cross-project evaluation;
- dataset and prompt release;
- precision, recall, F1 and calibration;
- analyst review or accepted-candidate measures;
- failure analysis and temporal validity.

## Reading order

```text
SRC-0024 classical and early-ML benchmark floor
-> SRC-0025 pretrained requirement classification and filtering
-> pretrained issue-to-commit recovery
-> RAG and generative LLM recovery
-> cross-project and human-review synthesis
```
