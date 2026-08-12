# DDTA Documentation Metamodel Through Functional Requirement - Closure Checkpoint R2

**THESIS BASELINE CHECKPOINT**

## 1. Evidence rule

This checkpoint intentionally **excludes** the two earlier oversimplified order/inventory holdouts and the earlier facial direct-MR FR probes as evidence for hierarchy. Those examples embedded choices inside MR/FR prose or simplified domain responsibilities enough to bias the topology result.

The current hierarchy conclusion is based on the corrected access-control reasoning plus the realistic order/warehouse rewrite in `../03-example-order-fulfillment/ORDER_FULFILLMENT_COMPLETE_AUTHORING_PROBE_R3.*`.

## 2. Closed documentation hierarchy for thesis scope

![Closed documentation hierarchy](diagrams/DOCUMENT_HIERARCHY.png)

```text
Project problem framing        [method precondition, not governed document]
        |
        v
MacroRequirement
        |
        v
Decision
        |
        v
FunctionalRequirement
        |
        v
SpecializedRequirement
        |
        `-- SecurityRequirement   [next specialization to formalize]
```

Cardinality/lifecycle interpretation:

- an MR may exist before Decisions are authored;
- every Decision has exactly one MR parent;
- every FR has exactly one Decision parent;
- a Decision may exist before FR children are authored;
- no FR has a direct MR parent in the thesis baseline;
- no Decision is a child of FR;
- an FR may later own `0..*` Specialized Requirements.

## 3. Why keep the Decision layer constant

Across access-control and warehouse examples, apparently "direct" FRs repeatedly concealed a prior commitment:

- facial verification required choosing the verification modality/responsibility;
- biometric/reference management required choosing the source/authority boundary;
- warehouse receipt/reservation behavior required deciding whether stock is project-managed or delegated to an external WMS;
- payment behavior changed when processing was delegated to an external PSP.

The regular layer makes these commitments explicit and simplifies authoring, validation, navigation and tooling.

### Rare singleton-solution trade-off

The model accepts a controlled **necessity/default Decision** when no materially distinct admissible alternative exists. This is an intentional methodological normalization: the project documents the commitment and why the alternative set is singleton rather than varying the hierarchy.

The rule is not permission to invent false rationale. Context must show why alternatives are absent/excluded, Consequences must be material, and the Decision must be reopenable if the constraint changes.

## 4. Closed MR semantics

MR owns one stable macro responsibility inside the framed problem.

Key invariants:

- problem anchored;
- one coherent macro concern;
- architecture/temporal resilience;
- no solution commitment leakage;
- no atomic FR behavior;
- broad domain readability;
- explicit cross-MR dependency;
- teachability;
- analysis-enabling, not analysis-producing.

Fundamental question:

> Within the framed project problem, which stable macro responsibility are we governing, what macro result/value must it contribute, why does it matter, and who is involved?

## 5. Closed Decision semantics

Decision owns one significant commitment narrowing one MR.

Local core:

```text
Decision
|- title
|- context
|- decision
`- consequences
```

Normally it selects among alternatives; exceptionally it records a necessity/default commitment when the admissible alternative space is singleton after review.

## 6. Closed FR semantics

FR is an independently assessable operational obligation under one parent Decision.

It contains:

- one coherent functional obligation;
- one or more readable normative clauses;
- structured SPO references supporting those clauses;
- exactly one parent Decision.

Normative prose is primary; SPO does not replace conditional/concurrency/lifecycle/failure semantics.

## 7. Cross-MR service composition

The semantic rule is closed:

> A consumer branch may use a governed service/capability owned by another MR without transferring ownership or creating a second parent.

The exact L1 target of that consumption relation is **not** closed yet. It will be decided with Base Analysis because the natural target may be a service/capability/BAE/interface rather than one specific FR.

## 8. What remains deliberately open

The closure does not yet formalize:

- Base Analysis / BAE types, relations, provenance and incremental creation from governed documentation;
- formal service/capability representation between MR branches;
- overlay/plugin contract;
- Analysis Record and Common Finding integration;
- SecurityRequirement fields/cardinalities/provenance from accepted Finding;
- effective obligation construction (`FR + applicable SecurityRequirement`);
- canonical L2 Markdown/YAML encoding beyond the authoring contract;
- realization/verification evidence lifecycle.

## 9. Reopen conditions

Reopen MR/Decision/FR semantics only if a concrete later result demonstrates that:

1. a SecurityRequirement cannot correctly constrain an FR under this hierarchy;
2. Base Analysis cannot be built/integrated from governed documentation without requiring different document semantics;
3. a method overlay requires source information the authoring model cannot express without contaminating MR/Decision/FR with method-specific concepts;
4. the regular Decision layer creates a concrete recurring semantic failure rather than merely an extra rare normalization document.

## 10. Authorized next phase

```text
fixed documentation authoring
        |
        v
formal Base Analysis / BAE
        |
        v
method-neutral overlay contract
        |
        v
STRIDE plugin/overlay as first concrete test
        |
        v
Analysis Record -> reviewed Finding
        |
        v
SecurityRequirement
        |
        v
FR + SEC effective obligation
        |
        v
revised design -> re-analysis
```

The purpose of the next phase is to verify the entire DDTA loop, not merely to prove that an overlay can emit threat labels.
