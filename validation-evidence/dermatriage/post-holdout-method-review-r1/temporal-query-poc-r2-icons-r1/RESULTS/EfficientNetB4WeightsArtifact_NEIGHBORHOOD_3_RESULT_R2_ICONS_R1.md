# Risultato BA temporale — `EfficientNetB4WeightsArtifact`

`SELECT NEIGHBORHOOD 3 FROM BA WHERE REFERENT = 'EfficientNetB4WeightsArtifact';`

> **Ricostruzione di progetto, non execution log.** Temporal facts non sono BAProposition; le fasi future non sono eventi avvenuti.

## Incidenza BA: direzioni e ruoli, non causalita automatica

### Hop 1 · BAP-FRC6-01-03A1-04 [ACCEPTED]
- transfer : behavior=EfficientNetModelAcquisition, source=GoogleDriveModelStore, content=EfficientNetB4WeightsArtifact, destination=ActiveClassifierStore
  - Occorrenza `W_O02` a `T_SETUP` (DOCUMENTED_SETUP_ACTION)
### Hop 1 · BAP-FRC6-01-03A1-07 [ACCEPTED]
- hasPart : whole=GoogleDriveModelStore, part=EfficientNetB4WeightsArtifact
  - Occorrenza `W_O01` a `T_SETUP` (DOCUMENTED_STRUCTURE)
### Hop 1 · BAP-FRC6-01-03A1-08 [ACCEPTED]
- hasPart : whole=ActiveClassifierStore, part=EfficientNetB4WeightsArtifact
  - Occorrenza `W_O03` a `T_SETUP` (DOCUMENTED_STRUCTURE)
### Hop 2 · BAP-FRC6-01-03A1-09 [ACCEPTED]
- hasPart : whole=ModelResourceAcquisitionStage, part=EfficientNetModelAcquisition

Un hop per proposition e una proiezione di adiacenza, non un transfer implicito.
