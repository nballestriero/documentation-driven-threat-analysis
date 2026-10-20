# Prototype generic-v01 — assessment di implementazione verso FR (CANDIDATE)

**Stato:** `EXPERIMENTAL_NON_CANONICAL`; assessment tecnico del prototipo, **non** BA e **non** attestazione di conformita' completa.  
**Baseline documentale:** commit `a105cea` (`master`).  
**Sorgenti di codice:** `projects/ddta-authoring-tool/prototype/generic-v01/`.  
**Evidenza:** suite `tests/test_generic.py`: 33 test superati su Windows con Python 3.14 il 2026-10-20, confermati anche in ambiente di prova Linux; i tre esempi `examples/MR-VALID.md`, `DEC-VALID.md`, `FR-VALID.md` passano `strict` senza diagnostiche.

## Perimetro verificato

- Un'unica CLI, `python -m ddta_tool`, espone `new` e `check`.
- Un unico `ddta_tool/engine.py` carica definizioni YAML da `schemas/` e contiene le funzioni `load_schema()`, `render_template()`, `validate()`.
- Tre schemi dichiarativi: `MacroRequirement`, `Decision`, `FunctionalRequirement`. Il test `test_adding_fourth_schema_needs_no_python_changes` dimostra l'estensione con un quarto tipo sintetico **entro il vocabolario di vincoli gia' supportato**.
- Il motore non governa il significato dei testi; la sua verifica e' formale. I file documentali gia' presenti in `docs/` non hanno ancora il front matter richiesto e **non sono stati migrati**.

## Mappatura evidence-to-FR

| FR documentato | Evidenza concreta nel prototipo | Valutazione limitata |
|---|---|---|
| `FR-MR01-01-01` — Acquisizione uniforme del contenuto | `validate(text, ...)` riceve una stringa direttamente; CLI legge UTF-8 dal file | **Parziale:** manca un oggetto snapshot con contesto e identificativo sorgente uniforme |
| `FR-MR01-01-02` — Selezione dello scope documentale | CLI `check` accetta un file esplicito | **Parziale:** nessuno scope di directory o selezione riproducibile del workspace |
| `FR-MR01-01-03` — Invocazione del servizio condiviso di controllo | CLI `check` invoca `engine.validate()` e ne presenta il risultato | **Parziale:** ancora non copre snapshot/scope completi e canali multipli |
| `FR-MR01-01-04` — Controllo senza editor | `ddta_tool/__main__.py`, exit code, output testuale e `--json` | **Parziale:** CLI usabile in PowerShell e ambiente Linux, ma non include lo scope cartella dell'FR |
| `FR-MR01-02-01` — Identificazione dichiarativa | `validate()` legge `type`, `id`, `schemaVersion` dal YAML front matter, senza inferire dal filename | **Parziale:** gestione dei link dichiarativi limitata ai metadati degli schemi disponibili |
| `FR-MR01-02-02` — Creazione template | `render_template()` costruisce Markdown dai campi e dalle sezioni richieste dello schema selezionato | **Parziale:** nessuna generazione BA; DSL iniziale limitata |
| `FR-MR01-04-01` — Collegamento BA-documento | Nessuna capacita' BA implementata | **Non implementato** |
| `FR-MR02-01-01` — Selezione formato di verifica | `load_schema()` cerca per `schemaId` nei YAML e rifiuta definizioni invalide/sconosciute | **Parziale:** contratto di versione 0.1, non una gestione completa delle compatibilita' |
| `FR-MR02-01-02` — Verifica conformita' formale | `validate()` controlla metadati, sezioni, cardinalita', pattern e clausole | **Parziale:** grammatica Markdown e clausole intenzionalmente limitata; nessuna regola specialistica plug-in completa |
| `FR-MR02-02-01` — Diagnostiche strutturate | `Diagnostic`, `CheckResult.as_dict()`, CLI `check --json` | **Parziale:** gli errori CLI di I/O/generazione sono ancora separati dal contratto diagnostico dei documenti |
| `FR-MR02-02-02` — Profili draft/strict | `validate(..., profile)` differenzia incompletezze e problemi impeditivi; suite di regressione | **Parziale:** profili provati per la grammatica attualmente supportata |
| `FR-MR01-03-01..03` — Supporto editor | Nessun LSP o estensione VS Code | **Non implementati** |

## Confini non coperti

1. **MR-03:** controllo dell'esistenza delle identita' referenziate, unicita' e risoluzione cross-documento non implementati. Un metadato `parentDecision` formalmente presente non certifica l'esistenza del documento parent.
2. **MR-04/MR-05:** nessuna generazione Mermaid o LaTeX/PDF.
3. **BA:** nessun file BA, BAReferent, BAProposition o `realize` e' derivato da questo assessment.
4. **DSL:** il parser Markdown supporta front matter YAML e sezioni semplici; clausole nel formato di lista a singola riga. Sintassi non riconosciute non devono essere considerate implicitamente governate.
5. **Documenti legacy:** il prototipo non considera conformi i file del progetto in formato precedente. La compatibilita' e un'eventuale migrazione richiedono decisioni esplicite.

## Ripetizione dei controlli

Dalla directory `projects/ddta-authoring-tool/prototype/generic-v01`:

```powershell
py -3 -m pip install -r requirements.txt
py -3 -m unittest discover -s tests -v
py -3 -m ddta_tool check examples/MR-VALID.md --profile strict
py -3 -m ddta_tool check examples/DEC-VALID.md --profile strict
py -3 -m ddta_tool check examples/FR-VALID.md --profile strict
```

**Conclusione:** questo checkpoint conserva una **realizzazione tecnica sperimentale parziale** delle capacita' documentate. La matrice progettuale di moduli Python in `FR_TO_PYTHON_MAPPING_CANDIDATE.md` resta una **proposta**, non deve essere confusa con i file concreti `ddta_tool/` di questo prototipo.
