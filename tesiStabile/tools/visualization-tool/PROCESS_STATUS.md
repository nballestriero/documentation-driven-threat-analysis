# DDTA Visualization Tool — estensione PROCESS (R5)

**Un solo toolkit**: `tools/visualization-tool/`. Il punto di avvio `scripts/pipeline.py` conserva la modalità CORE originale senza opzioni PROCESS. L'estensione PROCESS è nei moduli `src/ddta_process.py` e `src/ddta_process_pipeline.py`, non in una seconda applicazione.

## Esempi e guide

- Ontologia: `../../ontologies/process/DDTA_PROCESS.md`
- Guida normativa grafica: `../../ontologies/process/DDTA_PROCESS_VISUALIZATION.md`
- Unico esempio progressivo: `../../examples/plate-gate/DDTA_TARGA_COSTRUZIONE_PROGRESSIVA.md`
- Verifica 17 esempi (RDF e Mermaid): `python scripts/verify_process_guide.py`
- Suite storica PROCESS: `python -m unittest discover -s tests/process -p 'test_*.py'`

## Modalità CORE invariata

`python scripts/pipeline.py --guides-md <guida_core> --ttl <core.ttl> --out-dir <cartella>`

## Modalità CORE+PROCESS candidata

`python scripts/pipeline.py --core-generator scripts/pipeline.py --core-guide ../../ontologies/core/DDTA_CORE_VISUALIZATION.md --core-ttl <core.ttl> --process-guide ../../ontologies/process/DDTA_PROCESS_VISUALIZATION.md --process-ttl <process.ttl> --out-dir <cartella>`

Opzione di proiezione: `--show-operand-resource-references`.

**Limite esplicito:** la composizione R7 fallisce se il Mermaid CORE include già `ProcessStep`. Il passaggio a un toolkit unico **non risolve ancora** il problema della composizione generale. La suite storica del renderer non è interamente verde: uno snapshot grafico differisce. La guida PROCESS è esercitata con 17 esempi deterministici. Il CORE runtime e le sue ontologie non vengono modificati (eccetto dispatch conservativo nell'entrypoint comune).

Non aggiornare snapshot storici senza revisione visiva.
