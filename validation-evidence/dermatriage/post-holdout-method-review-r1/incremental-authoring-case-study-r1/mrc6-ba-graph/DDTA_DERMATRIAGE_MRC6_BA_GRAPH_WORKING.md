<!--
DDTA working note — intentionally not rendered.
Scope: this MR-C6 graph is constructed exclusively from BA propositions belonging to MR-C6.
Do not infer cross-MR / DEC / FR composition from this graph unless those BA propositions are explicitly added in a later reviewed step.
The file is the single canonical working Mermaid graph for MR-C6; replace/update it in place instead of accumulating historical graph variants.
-->

# MR-C6 — BA-derived working graph

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#FFFFFF","primaryColor":"#FFFFFF","primaryTextColor":"#17324D","primaryBorderColor":"#0047B3","lineColor":"#0047B3","edgeLabelBackground":"#FFFFFF"},"themeCSS":".cluster rect { rx:28px !important; ry:28px !important; } .edgeLabel p { background:#FFFFFF !important; border:1px solid #B8CBE8 !important; border-radius:10px !important; padding:2px 7px !important; }"}}%%

flowchart LR

    EnvironmentPreparation["EnvironmentPreparation<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-01</span>"]

    subgraph DermaTriageEnvironment["DermaTriageEnvironment"]
        direction TB
        ComputeResources("ComputeResources<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-03</span>")
        SoftwareComponents("SoftwareComponents<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-04</span>")
        ModelResources("ModelResources<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-05</span>")
        DataResources("DataResources<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-06</span>")
        EnvironmentConfiguration("EnvironmentConfiguration<br/><span style='font-size:7px;color:#FFFFFF'>BAP-MRC6-07</span>")
    end

    EnvironmentPreparation -->|produce| DermaTriageEnvironment

    classDef BAProduceActor fill:#212121,stroke:#000000,stroke-width:2px,color:#FFFFFF;
    classDef BAReferentD1 fill:#267DFF,stroke:#0047B3,stroke-width:2px,color:#FFFFFF;

    class EnvironmentPreparation BAProduceActor;
    class ComputeResources,SoftwareComponents,ModelResources,DataResources,EnvironmentConfiguration BAReferentD1;

    style DermaTriageEnvironment fill:#0066FF,stroke:#0047B3,stroke-width:2.5px,color:#FFFFFF
```
