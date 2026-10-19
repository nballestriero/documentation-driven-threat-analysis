# DermaTriage — proiezione BA dinamica · `ActiveClassifierStore`

Query: `SELECT HISTORY FROM BA WHERE REFERENT = 'ActiveClassifierStore';`

> **PoC R2, non modifica della BA canonica.** Una proposition è inclusa solo se compare nei dati BA selezionati. Il diagramma non afferma la realizzazione di un evento operativo. Le relazioni mancanti non vengono inventate.

**2 BAProposition incluse · 4 BAReferent canonici coinvolti · 3 archi grafici (compresi eventuali helper di ruolo) · 0 proposition escluse per limite.**

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#FFFFFF","lineColor":"#171717","edgeLabelBackground":"#FFFFFF"}}}%%

flowchart LR

    %% Selected from structured BA Markdown: source is NOT the cumulative Mermaid.
    %% Profile B (verified in VS Code): R3 document icons, R50 actor/edge classes.
    %% BA_VIEW_WHITE is visual-only: not hasPart and not a trust boundary.
    subgraph BA_VIEW_WHITE["BA view — layout only"]
      direction LR
      subgraph HP_ActiveClassifierStore["ActiveClassifierStore — hasPart (semantic frame)"]
          direction TB
          R_ActiveClassifierStore[("ActiveClassifierStore")]
          O_BAP_FRC6_01_03A1_08@{ shape: doc, label: "EfficientNetB4WeightsArtifact<br/><span style='font-size:8px'>same BAReferent / view occurrence</span>" }
      end
      R_EfficientNetB4WeightsArtifact@{ shape: doc, label: "EfficientNetB4WeightsArtifact" }
      R_EfficientNetModelAcquisition("EfficientNetModelAcquisition")
      R_GoogleDriveModelStore[("GoogleDriveModelStore")]

      R_GoogleDriveModelStore -->|"transfer<br/>BAP-FRC6-01-03A1-04"| R_EfficientNetB4WeightsArtifact
      R_EfficientNetB4WeightsArtifact --> R_ActiveClassifierStore
      R_EfficientNetModelAcquisition -.-|"behavior role / projection only"| R_EfficientNetB4WeightsArtifact
    end

    classDef BAProduceActor fill:#212121,stroke:#000000,stroke-width:2px,color:#FFFFFF;
    classDef BARealizationD2 fill:#8F9295,stroke:#4C5054,stroke-width:2px,color:#FFFFFF;
    classDef BAStore fill:#EEF4F9,stroke:#275D86,stroke-width:2px,color:#17324D;
    classDef BAContent fill:#FFFFFF,stroke:#275D86,stroke-width:2px,color:#17324D;
    classDef BALogicalData fill:#FFFFFF,stroke:#5C99C1,stroke-width:2px,color:#23313D;
    classDef BATransferBehavior fill:#FFF4E3,stroke:#A96A16,stroke-width:2px,color:#17324D;
    classDef BAGap fill:#FFFFFF,stroke:#C62828,stroke-width:3px,color:#C62828;
    style BA_VIEW_WHITE fill:#FFFFFF,stroke:#D4DCE3,stroke-width:1px,color:#17324D;
    class O_BAP_FRC6_01_03A1_08,R_EfficientNetB4WeightsArtifact BAContent;
    class R_ActiveClassifierStore,R_GoogleDriveModelStore BAStore;
    class R_EfficientNetModelAcquisition BAProduceActor;
    style HP_ActiveClassifierStore fill:#F8FBFD,stroke:#275D86,stroke-width:2.5px,color:#17324D;
    linkStyle 0 stroke:#0047B3,stroke-width:2px;
    linkStyle 1 stroke:#0047B3,stroke-width:2px;
    linkStyle 2 stroke:#909090,stroke-width:1.3px,stroke-dasharray:3 5;
```

## Tempo logico — diagramma SEPARATO, metadati non BA

Il seguente grafo rappresenta solo i contesti e le precedenze documentate: non è connesso alla topologia BA perché non sono BAProposition.

```mermaid
flowchart LR
  %% Pure temporal metadata; NO edges here are BAPropositions.
  TC_T_SETUP["T_SETUP / PRESENT / documented-step"]
  TC_T_RUNTIME["T_RUNTIME / PRESENT / governed-behavior"]
  classDef BATemporalView fill:#F5F6F8,stroke:#8B949E,stroke-width:1.5px,stroke-dasharray:3 3,color:#40464E;
  class TC_T_SETUP,TC_T_RUNTIME BATemporalView;
```

## Perché questi elementi sono inclusi

| BAProposition | Selezione | Semantica e ruoli | Stato | Contesti di occorrenza | Fonte BA |
|---|---|---|---|---|---|
| `BAP-FRC6-01-03A1-04` | diretta | **transfer** · behavior: `EfficientNetModelAcquisition`, source: `GoogleDriveModelStore`, content: `EfficientNetB4WeightsArtifact`, destination: `ActiveClassifierStore` | ACCEPTED | T_SETUP (DOCUMENTED_SETUP_ACTION) | DDTA pp.52-53 |
| `BAP-FRC6-01-03A1-08` | diretta | **hasPart** · whole: `ActiveClassifierStore`, part: `EfficientNetB4WeightsArtifact` | ACCEPTED | T_SETUP (DOCUMENTED_STRUCTURE) | DDTA p.53 |

**Regola di completezza:** tutti i ruoli di ciascuna BAProposition inclusa sono rappresentati; le ripetizioni grafiche entro i frame `hasPart` non rappresentano nuove identità BA.

## Relazioni non incluse

- Nessuna proposition scartata per il limite di nodi.
- `BAP-FRC6-01-03A1-07`: non raggiunta dai criteri della query (focus / hop / contesto).
- `BAP-FRC6-01-03A1-09`: non raggiunta dai criteri della query (focus / hop / contesto).
- `BAP-FR03-01-02`: non raggiunta dai criteri della query (focus / hop / contesto).
- `BAP-FR03-01-01`: non raggiunta dai criteri della query (focus / hop / contesto).
- `BAP-FRC7-07-01-03`: non raggiunta dai criteri della query (focus / hop / contesto).
- `BAP-FRC7-07-01-01`: non raggiunta dai criteri della query (focus / hop / contesto).
**Assenza dalla vista ≠ assenza dalla BA.**

## Tempo logico e informazioni contestuali

I contesti qui sotto qualificano occorrenze o fatti documentali: **non sono edges BA inventati**. `precedes` descrive solo l’ordine parziale esplicitato nel campione.

- Precedenze dichiarate: `T_SETUP` → `T_DEPLOY_CHECK`, `T_DEPLOY_CHECK` → `T_RUNTIME`, `T_SETUP` → `T_RETRAIN`, `T_RETRAIN` → `T_QUALIFY`.
- Sovrapposizioni dichiarate: nessuna (non implica serialità).

| Contesto | Esistenza focus | Fatto contestuale specifico (NON BAProposition) | Fonte |
|---|---|---|---|
| `PRE_BASELINE` | UNKNOWN (non e assenza) | — | — |
| `T_SETUP` | PRESENT (attestato nella vista) | — | — |
| `T_DEPLOY_CHECK` | UNKNOWN (non e assenza) | — | — |
| `T_RUNTIME` | PRESENT (attestato nella vista) | — | — |
| `T_RETRAIN` | UNKNOWN (non e assenza) | — | — |
| `T_QUALIFY` | UNKNOWN (non e assenza) | — | — |

## Interpretazione e limiti

- La selezione usa la co-partecipazione ai ruoli di una **BAProposition intera**, non un percorso di causalità automatico.
- Il grafo non collega automaticamente pesi, modello e retraining quando manca la BAProposition corrispondente.
- `produce` è la coppia di frecce nere continue `input -> actor -> result`, con BAProposition ID sull’arco actor -> result secondo lo stile del cumulativo R50; `realize` è la freccia grigia tratteggiata con etichetta realize. Gli archi `produce`, `transfer` e `realize` corrispondono a proposition selezionate; `hasPart` viene mostrato come frame. Gli archi grigi `precedes / NON BA` nel pannello temporale sono metadati di ordine logico, **non** BAProposition; l’eventuale arco grigio `behavior role / projection only` è un helper di visualizzazione.
- L’esistenza `UNKNOWN` indica che non ci sono prove sufficienti in questo dataset, non che l’elemento sia assente.
- Le versioni logiche non certificano uguaglianza crittografica fra copie di file.

