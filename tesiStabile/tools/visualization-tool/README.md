# DDTA — Visualization Tool

Tool Python per generare grafici Mermaid a partire da uno o più grafi RDF/Turtle e dalle regole `yaml ddta-visualization` dichiarate nelle guide grafiche delle ontologie DDTA.

**La fonte autorevole delle regole non è in questo tool**: si trova in `ontologies/<modulo>/`, per esempio `ontologies/core/DDTA_CORE_VISUALIZATION.md`. La libreria non contiene uno schema fisso delle classi CORE. Supporta più guide e più file TTL; l'integrazione con nuove ontologie è un'estensione delle regole, non una riscrittura del motore, finché si usano primitive già supportate.

## Uso

Requisito: Python 3.11+ e dipendenze indicate in `requirements.txt`.

```powershell
$repo = "$env:USERPROFILE\Documents\tesiStabile"
$tool = "$repo\tools\visualization-tool"
python -m pip install -r "$tool\requirements.txt"
python "$tool\scripts\pipeline.py" `
    --guides-md "$repo\ontologies\core\DDTA_CORE_VISUALIZATION.md" `
    --ttl "C:\percorso\modello.ttl" `
    --out-dir "$env:TEMP\ddta-viz-output"
code "$env:TEMP\ddta-viz-output\05_graph.md"
```

La CLI supporta anche più guide (`--guides-md <file1> <file2>`) e più TTL (`--ttl <file1> <file2>`), più `--query`, `--focus`, `--view association|functional-flow`, `--strict`. Per dettagli e diagrammi, leggere [Guida al funzionamento](docs/GUIDA_FUNZIONAMENTO.md) e [Logica di sviluppo](docs/LOGICA_DI_SVILUPPO.md).

## Struttura

- `src/ddta_viz/`: libreria di parsing YAML, catalogo regole, selezione RDF, proiezione IR e renderer Mermaid.
- `scripts/`: 7 punti di ingresso eseguibili, uno per ogni fase; `pipeline.py` coordina l'intero flusso.
- `tests/`: test automatici di comportamento e di identità RDF condivisa; usa la guida CORE del repository senza duplicarla.
- `examples/extension/`: seconda ontologia illustrativa per verificare l'estendibilità, non un nuovo modulo DDTA approvato.
- `docs/`: manuale d'uso e architettura del motore con Mermaid.

## Test

```powershell
Set-Location "$repo\tools\visualization-tool"
python -m unittest discover -s tests -v
```

Le occorrenze multiple dello stesso IRI RDF sono consentite e riportate come diagnostiche `info`. Gli errori di proiezione esplicitamente previsti nelle regole non vengono soppressi. I test sulle nuove ontologie non sostituiscono la validazione delle loro guide prima dell'adozione.

Gli output (`01_rules_extracted.yaml` fino a `06_diagnostics.json`, i Mermaid `.mmd` e `.md` e le icone incorporate) si generano nella directory indicata dall'utente, **non** si versionano nel tool.
