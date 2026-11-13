# Package `ddta_ontology`

Libreria riutilizzabile per validazione delle schede `yaml ddta-ontology` e conversione RDF/OWL. Non dipende da repository, percorsi fissi o elenco prestabilito di moduli. Gli identificatori di modulo provengono dai Markdown; i namespace possono arrivare da un registro YAML o da blocchi `yaml ddta-namespace` negli stessi file.

API principale: `discover_sources`, `load_config_file`, `validate_sources`, `generate_turtle`, `check_outputs`, `write_outputs` (esportate da `__init__.py`). La CLI è un livello separato definito in `cli.py`. La validazione non scrive su disco; `write_outputs()` è l'operazione esplicita di salvataggio.

Per la struttura completa, gli esempi e i diagrammi consultare `../docs/ARCHITECTURE.md`. Per la lettura di Python consultare `../docs/PYTHON_WALKTHROUGH.md`.

Il file `function_model.yaml` propone una vista funzionale DDTA del tool; non è un documento `yaml ddta-ontology` e non genera triple normative. `trace.py` crea indipendentemente una mappa AST del codice.
