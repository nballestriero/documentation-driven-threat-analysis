# DDTA – DermaTriage BA temporal query PoC R2 ICONS R1

**Scopo:** fissare nel generatore dinamico il profilo grafico B, testato in VS Code dall'utente con tutti e tre gli archi visibili. **Nessuna modifica alla BA canonica, alla guida o al repository.**

## Risultato della diagnosi

L'utente ha verificato che **sia A che B mostrano tutti i collegamenti**; la variante **B con le forme documento** è quella selezionata per lo stile DDTA. Di conseguenza non possiamo attribuire il problema precedente esclusivamente alla sintassi `@{shape: doc}`. Il nuovo generatore riproduce il *profilo completo B*: fondo bianco esplicito tramite un frame esclusivamente grafico, document icons per `content`, actor scuro e classi colore del cumulativo R50, due frecce nere da 3px per `produce`, `realize` grigio tratteggiato. Le BAProposition e gli operatori restano immutati. Il frame `BA_VIEW_WHITE` **non è `hasPart` né trust boundary**.

**Resta una divergenza da riconciliare in futuro:** il profilo B usa l'actor scuro del cumulativo R50, mentre la guida R3 documenta anche un `BAActor` chiaro. Qui il colore segue il profilo B verificato dall'utente; nessuna modifica o approvazione formale della guida è implicita.

## File da aprire

- `RESULTS/ImageUrgencyAnalysis_HISTORY_VIEW_R2_ICONS_R1.md` — `LesionImage -> ImageUrgencyAnalysis -> ImageUrgencyClassification` e `EfficientNet-B4 -.-> ImageUrgencyAnalysis`, con icone documento e stile B.
- `RESULTS/ActiveClassifierStore_HISTORY_VIEW_R2_ICONS_R1.md` — focus sullo store attivo.
- `RESULTS/EfficientNetB4WeightsArtifact_HISTORY_VIEW_R2_ICONS_R1.md` — pesi, transfer e contenimenti in store, inclusa cornice rossa tratteggiata per lo store esterno.
- Ciascun `.md` contiene **due diagrammi separati** (topologia BA e pannello temporale). Il corrispondente `.mmd` contiene **solo la topologia BA**.

## Ripetere la prova da PowerShell

Da questa cartella, con Python 3 disponibile:

```powershell
py -3 .\ddta_temporal_query.py --query "SHOW REFERENTS FROM BA;"
py -3 .\ddta_temporal_query.py --query "SELECT HISTORY FROM BA WHERE REFERENT = 'ImageUrgencyAnalysis';" --out .\RESULTS --mermaid
py -3 .\ddta_temporal_query.py --query "SELECT HISTORY FROM BA WHERE REFERENT = 'EfficientNetB4WeightsArtifact';" --out .\RESULTS --mermaid
py -3 -m unittest -v test_ddta_temporal_query.py
```

Oppure: `& .\RUN_DEMO.ps1`.

## Garanzie e limiti

- **58 test automatici passati.** Includono selezione delle proposition, presenza dei tre archi, stili, shape documento, `linkStyle` consecutivi e mancata introduzione di relazioni BA.
- Codice Mermaid nei `.md` e rispettivi `.mmd` identico per ciascuna query.
- Solo **20 BAReferent e 8 BAProposition** del campione strutturato, non l'intera BA del repository.
- Il profilo grafico B è stato verificato in VS Code dall'utente; le nuove query generate devono ancora essere viste nel suo renderer per la conferma end-to-end.
- L'assenza di una relazione nella vista non ne dimostra l'assenza nella documentazione.
- Il ciclo di retraining non è dichiarato realmente eseguito nel campione; `UNKNOWN` non significa assente.
