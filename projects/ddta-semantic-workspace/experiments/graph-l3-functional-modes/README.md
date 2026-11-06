# Graph L3 — focus sulla funzione primaria (esperimento di visualizzazione)

Il solo documento MR-01 canonico si trova in `dermatriage/mr/MR-01.md`.
La precedente copia sperimentale `MR-01-L3-CANDIDATE.md` è stata ritirata.
Questo esperimento contiene soltanto query, runner e test di proiezione;
non introduce identità o versioni alternative dell'MR.

## Modello

- `FunctionalMode` è distinta da `Function` e `Process`.
- `hasMode` associa la funzione alle modalità; non è `hasPart`.
- `hasInput` e `hasOutput` descrivono l'interfaccia sia delle funzioni sia delle modalità.
- Le condizioni di assenza/presenza non sono formalizzate dal mancato arco RDF
  (semantica Open World); il contratto generale mantiene `LesionImage` opzionale.
- Le lacune RDF sono validate, mentre il Graph L3 generale le nasconde di default.
- La query di focus sperimentale può mostrare le lacune quando selezionata esplicitamente.

## Uso

Da `projects/ddta-semantic-workspace`:

```powershell
python experiments/graph-l3-functional-modes/run_experiment.py `
    --out "$env:TEMP\DDTA-L3-FOCUS"
code "$env:TEMP\DDTA-L3-FOCUS.graph.md"
python -m unittest discover -s tests -p test_l3_functional_modes.py -v
```

Per la vista generale ufficiale:

```powershell
python -m tools.visualize --mr "MR-01,MR-02,MR-03,MR-04,MR-C6,MR-C7" `
    --view l3 --out "$env:TEMP\DDTA-L3-ALL"
```
