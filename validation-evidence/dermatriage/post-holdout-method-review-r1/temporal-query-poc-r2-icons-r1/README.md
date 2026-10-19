# DDTA — DermaTriage, BA temporale interrogabile — PoC R2 ICONS R1

**Stato**: prova sperimentale e riproducibile; **non** modifica la documentazione canonica DermaTriage, i BAReferent, le BAProposition, la guida BA o le altre guide metodologiche.

## Contenuto e finalità

L'esperimento verifica la possibilità di partire da un BAReferent per ottenere per query una selezione di relazioni BA, la loro proiezione Mermaid, una storia temporale logica e un resoconto delle relazioni non incluse. Le query funzionano su un **campione strutturato**, non sull'intero corpus DDTA. Lo studio rimane indipendente da STRIDE, PASTA o altri metodi di analisi.

Sorgente: `CASO_DERMATRIAGE_PESI.md` (schema embedded `ba-temporal-json` sperimentale); interrogatore: `ddta_temporal_query.py`; test: `test_ddta_temporal_query.py`; viste ed esiti: `RESULTS/`.

## Tre esempi visivi da rivedere in VS Code

- [`RESULTS/EfficientNetB4WeightsArtifact_HISTORY_VIEW_R2_ICONS_R1.md`](RESULTS/EfficientNetB4WeightsArtifact_HISTORY_VIEW_R2_ICONS_R1.md): dal trasferimento dallo store esterno allo store attivo, con storia temporale separata.
- [`RESULTS/ActiveClassifierStore_HISTORY_VIEW_R2_ICONS_R1.md`](RESULTS/ActiveClassifierStore_HISTORY_VIEW_R2_ICONS_R1.md): focus sullo store locale.
- [`RESULTS/ImageUrgencyAnalysis_HISTORY_VIEW_R2_ICONS_R1.md`](RESULTS/ImageUrgencyAnalysis_HISTORY_VIEW_R2_ICONS_R1.md): `LesionImage → ImageUrgencyAnalysis → ImageUrgencyClassification` (`produce`) e `EfficientNet-B4 → ImageUrgencyAnalysis` (`realize`).

I `.mmd` corrispondenti contengono il **grafo BA**, mentre ciascun `.md` HISTORY include un secondo diagramma temporale separato. `RESULTS/*_ONLY_GRAPH_*.md` mostra soltanto la topologia BA per un controllo più semplice.

## Riprodurre (PowerShell, Python 3 standard library)

```powershell
py -3 -m unittest -v .\test_ddta_temporal_query.py
py -3 .\ddta_temporal_query.py --query "SHOW REFERENTS FROM BA;"
py -3 .\ddta_temporal_query.py --query "SELECT HISTORY FROM BA WHERE REFERENT = 'ImageUrgencyAnalysis';" --out .\RESULTS --mermaid
py -3 .\ddta_temporal_query.py --query "SELECT HISTORY FROM BA WHERE REFERENT = 'EfficientNetB4WeightsArtifact';" --out .\RESULTS --mermaid
# Oppure: & .\RUN_DEMO.ps1
```

**Nota**: la riesecuzione aggiorna i file generati in `RESULTS/`; controllare `git diff` prima di conservare tali aggiornamenti.

## Limiti e scelte esplicite

- Sono inclusi solo **20 BAReferent e 8 BAProposition** del campione. Mancano deliberatamente relazioni non ancora formalizzate nel caso reale, in particolare nel retraining.
- I tempi distinguono procedure, comportamenti governati, evidenze storiche e occorrenze osservate. `T_RETRAIN` non significa che il retraining sia stato realmente eseguito.
- `UNKNOWN` non significa assenza; la presenza fra due contesti non può essere interpolata automaticamente.
- L'ordine logico è parziale. La mancata precedenza non indica contemporaneità.
- Il file `CASO_DERMATRIAGE_PESI.md` riporta riferimenti alle fonti originali **solo in quanto evidenza metodologica sperimentale**: non introduce riferimenti alle fonti esterne nella documentazione canonica DermaTriage.
- Lo stile grafico incorpora le forme documento, gli operatori colorati e il profilo B scelto dall'utente. La comparazione A/B con tutte le frecce visibili non è prova automatica del rendering di ogni diagramma generato.
- Lo stato ACCEPTED/CANDIDATE viene preservato dai dati di input e **non viene cambiato** dalle query.

## Cosa decidere dopo

Vedi [`TEMPORAL_METHODOLOGY_OPEN_QUESTIONS_R1.md`](TEMPORAL_METHODOLOGY_OPEN_QUESTIONS_R1.md): separa le proposte per guida BA, guida alla scrittura della documentazione e guida di proiezione Mermaid. Niente di ciò viene qui promosso a norma.
