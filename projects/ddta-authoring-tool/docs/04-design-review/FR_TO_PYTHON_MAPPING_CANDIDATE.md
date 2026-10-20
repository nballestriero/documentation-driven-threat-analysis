# Ramo MR-01 — Tracciamento funzionale verso realizzazioni Python (PROPOSTA)

**Stato:** `CANDIDATE / REVIEW ONLY`. I nomi di librerie e API nella matrice sono **proposte di architettura**, non una descrizione dell'effettiva struttura del prototipo. Non identificano BAProposition o `realize` accettati. Per il codice sperimentale realmente disponibile, vedere `GENERIC_PROTOTYPE_V01_FR_ASSESSMENT.md` e `../../prototype/generic-v01/`.

## Regola metodologica

La catena di tracciamento desiderata è: `FR (obbligo documentale)` → `BAProposition/BAReferent logico (da analizzare)` → `realize` → `componente Python concreto (da implementare)` → `test di conformità`. Un FR non *contiene* per definizione il nome del modulo Python: il nome è una realization sostituibile.

## Matrice candidata

| FR | Funzione logica possibile (non ancora BA) | Realizzazione proposta | Confine |
|---|---|---|---|
| FR-MR01-01-01 | DocumentSnapshotAcquisition | `ddta/source/snapshots.py` | MR-01 |
| FR-MR01-01-02 | DocumentScopeSelection | `ddta/workspace/selection.py` | MR-01; riusa MR-03 per riferimenti |
| FR-MR01-01-03 | ValidationRequestOrchestration | `ddta/application/check.py` | MR-01 consuma MR-02 |
| FR-MR01-01-04 | CommandLineAccess | `ddta/interfaces/cli.py`, `ddta/__main__.py` | MR-01; nessuna duplicazione del validator |
| FR-MR01-02-01 | DocumentTypeRecognition | `ddta/document/reader.py` | MR-01; contratto documentale condiviso |
| FR-MR01-02-02 | DocumentTemplateCreation | `ddta/authoring/templates.py` | MR-01; legge schemi governati |
| FR-MR01-03-01 | InteractiveCheckInitiation | `ddta/interfaces/lsp_server.py` | MR-01 client; MR-02 valida |
| FR-MR01-03-02 | FieldCompletion | `ddta/authoring/completion.py` | MR-01; legge gli stessi schemi |
| FR-MR01-03-03 | EditorDiagnosticPresentation | `ddta/interfaces/lsp_server.py` + piccolo client VS Code | MR-01 presenta; MR-02 produce diagnostiche |

## Confini con gli altri MR

- **MR-02:** può realizzare `validate(snapshot, profile) -> DiagnosticReport`, ad esempio in `ddta/validation/engine.py`. Nessuna copia in CLI o nel Language Server.
- **MR-03:** governa risoluzione, riuso, unicità e riferimenti canonici, ad esempio con un servizio `resolve_referent(...)` (modulo e contratto da decidere).
- **MR-04:** proietta la BA in viste componibili; nessuna logica Mermaid deve vivere dentro un modulo di completamento editoriale.
- **MR-05:** genera LaTeX/PDF a partire da sorgenti validati; non ha autorità per modificarne il contenuto.

## Contratto minimo comune proposto

```text
DocumentSnapshot:
  source_uri
  text
  workspace_context
  source_revision

CheckRequest:
  snapshot_or_scope
  schema_version
  validation_profile

DiagnosticReport:
  document_uri
  rule_id
  severity
  range_start/range_end
  message
  suggested_fix (optional)
```

I campi sono **proposti** per la futura Decision/FR di MR-02 e non rappresentano un metamodel BA accettato.

## Esempi d’uso (NON implementati)

```powershell
# PowerShell, file già scritto da una persona o da un agente AI
python -m ddta check docs/01-macro-requirements/MR-01.md
```

```bash
# Linux shell, stesso comando e stesso motore
python -m ddta check docs/01-macro-requirements/MR-01.md
```

```text
VS Code client → didOpen/didChange → Language Server Python
               → snapshot → stesso servizio di controllo MR-02
               → Diagnostics + Completion per i campi
```

Per VS Code, l'estensione client può richiedere un piccolo modulo JavaScript/TypeScript; **parser, schemi e validatore rimangono Python**. Un agente AI che usa la CLI non necessita di un percorso proprio. Se chiama direttamente la libreria, deve consumare lo stesso servizio.

## Scelte ancora da risolvere per completare il prodotto

1. Identità dichiarata tramite metadati YAML front matter oppure altra sintassi?
2. Come riconoscere workspace root e file inclusi in un controllo su cartella?
3. Completamento dell’editor: evento automatico, invocazione esplicita o entrambi?
4. Contratto diagnostico e semantica `draft`/`strict`, sotto MR-02.
5. API in memoria esposta da subito oppure dopo la prima CLI?
6. Versioni degli schemi e politica di migrazione di documenti esistenti.
