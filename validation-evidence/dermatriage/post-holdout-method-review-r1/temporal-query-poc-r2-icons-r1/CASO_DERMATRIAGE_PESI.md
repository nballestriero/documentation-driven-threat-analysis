# DDTA / BA — Caso DermaTriage: storia logica dei pesi EfficientNet-B4 (PoC R1)

**Esperimento R2 separato dalla documentazione canonica.** Non cambia BA, MR-C6, MR-04, MR-C7 o R50.
Le proposition sono riportate con **ID e ruoli reali** del caso DDTA, con lo stato ACCEPTED/CANDIDATE.
`temporalFacts`, `contexts`, `precedes`, `presence`, `versions`, `occurrences` e la metadata di vista `boundary` sono dati **sperimentali della query**, non nuovi operatori BA.

- `PRE_BASELINE` rappresenta test storici della versione 1.0.0, non una verifica di integrità dei pesi scaricati.
- `T_SETUP` e' la procedura documentata; nessun log di installazione individuale e' disponibile.
- `T_RETRAIN` e `T_QUALIFY` sono comportamenti **governati ma non osservati** nello stato descritto.
- `T_RUNTIME` e `T_RETRAIN` **non hanno un ordine imposto**: la mancata precedenza non prova la simultaneita'.
- Non creiamo `version 1.0.1`, `candidate weights` o un `produce` del retrainer come fatto BA accettato.
- La versione `baseline-1.0.0` non attesta hash identici tra file remoto e locale.

```ba-temporal-json
{
  "schema": "ba-temporal-poc/dermatriage-weights-1",
  "focus": "EfficientNetB4WeightsArtifact",
  "referents": [
    {
      "id": "EfficientNetB4WeightsArtifact",
      "kind": "content"
    },
    {
      "id": "GoogleDriveModelStore",
      "kind": "store",
      "boundary": "EXTERNAL"
    },
    {
      "id": "ActiveClassifierStore",
      "kind": "store"
    },
    {
      "id": "EfficientNetModelAcquisition",
      "kind": "activity"
    },
    {
      "id": "EfficientNet-B4",
      "kind": "realization"
    },
    {
      "id": "ImageUrgencyAnalysis",
      "kind": "activity"
    },
    {
      "id": "LesionImage",
      "kind": "content"
    },
    {
      "id": "ImageUrgencyClassification",
      "kind": "content"
    },
    {
      "id": "ModelResourceAcquisitionStage",
      "kind": "stage"
    },
    {
      "id": "ClassifierVersionStore",
      "kind": "store"
    },
    {
      "id": "ClassifierAdaptationCycle",
      "kind": "candidate-activity"
    },
    {
      "id": "CandidateUrgencyClassificationAdaptation",
      "kind": "candidate-content"
    },
    {
      "id": "ApplicableReferenceVersion",
      "kind": "reference"
    },
    {
      "id": "ApplicableComparativeAcceptanceCriteria",
      "kind": "criteria"
    },
    {
      "id": "BaselineClassifierMetricEvaluation",
      "kind": "candidate-activity"
    },
    {
      "id": "BaselineClassifierEvaluationInput",
      "kind": "candidate-content"
    },
    {
      "id": "BaselineClassifierQualityObservation",
      "kind": "candidate-content"
    },
    {
      "id": "BaselineClassifierQualityVerification",
      "kind": "candidate-activity"
    },
    {
      "id": "BaselineQualityGateOutcome",
      "kind": "candidate-content"
    },
    {
      "id": "ClassifierQualityVerificationStage",
      "kind": "stage"
    }
  ],
  "versions": [
    {
      "id": "EfficientNetB4WeightsArtifact@baseline-1.0.0",
      "family": "EfficientNetB4WeightsArtifact",
      "note": "versione logica, NON fingerprint crittografico"
    }
  ],
  "contexts": [
    {
      "id": "PRE_BASELINE",
      "label": "Valutazione iniziale baseline (storica; ordine verso setup non formalizzato)",
      "kind": "historical-evidence"
    },
    {
      "id": "T_SETUP",
      "label": "Installazione - transfer da Google Drive",
      "kind": "documented-step"
    },
    {
      "id": "T_DEPLOY_CHECK",
      "label": "Verifica del servizio (non verifica integrità dei pesi)",
      "kind": "documented-test"
    },
    {
      "id": "T_RUNTIME",
      "label": "Esercizio - image urgency inference",
      "kind": "governed-behavior"
    },
    {
      "id": "T_RETRAIN",
      "label": "Retraining eventuale - condizionato a 50 correzioni",
      "kind": "governed-future-behavior"
    },
    {
      "id": "T_QUALIFY",
      "label": "Qualificazione candidata prima di eventuale adozione",
      "kind": "governed-future-behavior"
    }
  ],
  "precedes": [
    [
      "T_SETUP",
      "T_DEPLOY_CHECK"
    ],
    [
      "T_DEPLOY_CHECK",
      "T_RUNTIME"
    ],
    [
      "T_SETUP",
      "T_RETRAIN"
    ],
    [
      "T_RETRAIN",
      "T_QUALIFY"
    ]
  ],
  "overlaps": [],
  "presence": [
    {
      "subject": "GoogleDriveModelStore",
      "contexts": [
        "T_SETUP"
      ]
    },
    {
      "subject": "ActiveClassifierStore",
      "contexts": [
        "T_SETUP",
        "T_RUNTIME"
      ]
    },
    {
      "subject": "EfficientNetB4WeightsArtifact@baseline-1.0.0",
      "contexts": [
        "T_SETUP",
        "T_RUNTIME"
      ]
    }
  ],
  "propositions": [
    {
      "id": "BAP-FRC6-01-03A1-04",
      "semanticOperatorKey": "transfer",
      "roles": {
        "behavior": "EfficientNetModelAcquisition",
        "source": "GoogleDriveModelStore",
        "content": "EfficientNetB4WeightsArtifact",
        "destination": "ActiveClassifierStore"
      },
      "status": "ACCEPTED",
      "origin": "DDTA pp.52-53"
    },
    {
      "id": "BAP-FRC6-01-03A1-07",
      "semanticOperatorKey": "hasPart",
      "roles": {
        "whole": "GoogleDriveModelStore",
        "part": "EfficientNetB4WeightsArtifact"
      },
      "status": "ACCEPTED",
      "origin": "DDTA p.53"
    },
    {
      "id": "BAP-FRC6-01-03A1-08",
      "semanticOperatorKey": "hasPart",
      "roles": {
        "whole": "ActiveClassifierStore",
        "part": "EfficientNetB4WeightsArtifact"
      },
      "status": "ACCEPTED",
      "origin": "DDTA p.53"
    },
    {
      "id": "BAP-FRC6-01-03A1-09",
      "semanticOperatorKey": "hasPart",
      "roles": {
        "whole": "ModelResourceAcquisitionStage",
        "part": "EfficientNetModelAcquisition"
      },
      "status": "ACCEPTED",
      "origin": "DDTA p.53"
    },
    {
      "id": "BAP-FR03-01-02",
      "semanticOperatorKey": "realize",
      "roles": {
        "abstract": "ImageUrgencyAnalysis",
        "realization": "EfficientNet-B4"
      },
      "status": "ACCEPTED",
      "origin": "DDTA p.7"
    },
    {
      "id": "BAP-FR03-01-01",
      "semanticOperatorKey": "produce",
      "roles": {
        "actor": "ImageUrgencyAnalysis",
        "input": "LesionImage",
        "result": "ImageUrgencyClassification"
      },
      "status": "ACCEPTED",
      "origin": "DDTA p.7"
    },
    {
      "id": "BAP-FRC7-07-01-03",
      "semanticOperatorKey": "produce",
      "roles": {
        "actor": "BaselineClassifierMetricEvaluation",
        "input": "BaselineClassifierEvaluationInput",
        "result": "BaselineClassifierQualityObservation"
      },
      "status": "CANDIDATE",
      "origin": "DDTA p.79"
    },
    {
      "id": "BAP-FRC7-07-01-01",
      "semanticOperatorKey": "produce",
      "roles": {
        "actor": "BaselineClassifierQualityVerification",
        "input": "BaselineClassifierQualityObservation",
        "result": "BaselineQualityGateOutcome"
      },
      "status": "CANDIDATE",
      "origin": "DDTA p.79"
    }
  ],
  "occurrences": [
    {
      "id": "W_O01",
      "proposition": "BAP-FRC6-01-03A1-07",
      "context": "T_SETUP",
      "version_bindings": {
        "part": "EfficientNetB4WeightsArtifact@baseline-1.0.0"
      },
      "mode": "DOCUMENTED_STRUCTURE"
    },
    {
      "id": "W_O02",
      "proposition": "BAP-FRC6-01-03A1-04",
      "context": "T_SETUP",
      "version_bindings": {
        "content": "EfficientNetB4WeightsArtifact@baseline-1.0.0"
      },
      "mode": "DOCUMENTED_SETUP_ACTION"
    },
    {
      "id": "W_O03",
      "proposition": "BAP-FRC6-01-03A1-08",
      "context": "T_SETUP",
      "version_bindings": {
        "part": "EfficientNetB4WeightsArtifact@baseline-1.0.0"
      },
      "mode": "DOCUMENTED_STRUCTURE"
    },
    {
      "id": "W_O04",
      "proposition": "BAP-FR03-01-02",
      "context": "T_RUNTIME",
      "version_bindings": {},
      "mode": "GOVERNED_ROLE_NOT_EXECUTION_LOG"
    },
    {
      "id": "W_O05",
      "proposition": "BAP-FR03-01-01",
      "context": "T_RUNTIME",
      "version_bindings": {},
      "mode": "GOVERNED_ROLE_NOT_EXECUTION_LOG"
    },
    {
      "id": "W_O06",
      "proposition": "BAP-FRC7-07-01-03",
      "context": "PRE_BASELINE",
      "version_bindings": {},
      "mode": "CANDIDATE_LOGICAL_PROJECTION"
    },
    {
      "id": "W_O07",
      "proposition": "BAP-FRC7-07-01-01",
      "context": "PRE_BASELINE",
      "version_bindings": {},
      "mode": "CANDIDATE_LOGICAL_PROJECTION"
    }
  ],
  "temporalFacts": [
    {
      "id": "EF01",
      "subject": "EfficientNetB4WeightsArtifact",
      "context": "T_SETUP",
      "claim": "Pesi baseline 1.0.0 reperibili su Google Drive e posizionati in models/efficientnet_b4.pth.",
      "category": "DOCUMENTED_CONFIGURATION",
      "source": "OR4 Training Environment Config p.2-3; DDTA pp.52-53"
    },
    {
      "id": "EF02",
      "subject": "EfficientNetB4WeightsArtifact",
      "context": "PRE_BASELINE",
      "claim": "Valutazione storica EfficientNet-B4 1.0.0 su test set; NON prova il controllo del file scaricato in installazione.",
      "category": "HISTORICAL_EVIDENCE",
      "source": "OR2 Model Test Report pp.1,3-4"
    },
    {
      "id": "EF03",
      "subject": "EfficientNetB4WeightsArtifact",
      "context": "T_DEPLOY_CHECK",
      "claim": "Verifica operativita EfficientNet; integrita/autenticita dei pesi NOT SPECIFIED.",
      "category": "BOUNDARY_GAP",
      "source": "OR4 Training Environment Config p.3; OR5 Test Environment Setup p.2; DDTA p.53"
    },
    {
      "id": "EF04",
      "subject": "EfficientNetB4WeightsArtifact",
      "context": "T_RUNTIME",
      "claim": "Modello EfficientNet-B4 realizza ImageUrgencyAnalysis; il binding dei pesi attivi e models/efficientnet_b4.pth; nessun transfer inventato tra store e funzione.",
      "category": "DOCUMENTED_ROLE_NO_NEW_BAP",
      "source": "OR2 Architecture Document p.1; OR4 Training Environment Config p.2; DDTA pp.7,52"
    },
    {
      "id": "EF05",
      "subject": "EfficientNetB4WeightsArtifact",
      "context": "T_RETRAIN",
      "claim": "Protocollo di fine-tune degli ultimi due blocchi e classifier head, 10 epoche/ciclo; trigger a 50 disaccordi. Il retraining non era ancora attivato nello stato osservato.",
      "category": "GOVERNED_POTENTIAL_NOT_OBSERVED",
      "source": "OR4 Training Cycles Report pp.3-4; DDTA p.31"
    },
    {
      "id": "EF06",
      "subject": "EfficientNetB4WeightsArtifact",
      "context": "T_RETRAIN",
      "claim": "Il contenuto preciso in ingresso al nuovo fine-tune, l ID/versione dei pesi nuovi e il transfer in uno store restano non formalizzati come BAProposition.",
      "category": "BA_RELATION_GAP",
      "source": "DDTA p.31,37,52-53; OR4 Training Cycles Report p.3"
    },
    {
      "id": "EF07",
      "subject": "EfficientNetB4WeightsArtifact",
      "context": "T_QUALIFY",
      "claim": "Tre condizioni comparative obbligatorie (sensitivity non peggiora, false LOW non cresce, accuracy non diminuisce oltre 5%). Nessun candidate weights artifact concretamente osservato.",
      "category": "GOVERNED_POLICY_NOT_OBSERVED",
      "source": "OR4 Training Cycles Report p.3; DDTA p.37"
    },
    {
      "id": "EF08",
      "subject": "EfficientNetB4WeightsArtifact",
      "context": "T_QUALIFY",
      "claim": "Il ramo di qualificazione di MR-04 ha identities candidate per result/evaluation; qui non si genera un BA transfer né una versione futura.",
      "category": "BA_RELATION_GAP",
      "source": "DDTA p.37"
    }
  ]
}
```
