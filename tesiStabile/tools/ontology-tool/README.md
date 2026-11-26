# Ontology Markdown Tool

**Strumento Python portabile per validare ontologie descritte in Markdown e generare, su richiesta, Turtle RDF/OWL leggibile.**

Non dipende dal nome o dal percorso di un repository, dal numero dei moduli, dai nomi dei file Markdown o da una specifica organizzazione delle cartelle. Legge le dichiarazioni normative `yaml ddta-ontology` presenti nei documenti selezionati. Il parametro `module` identifica il modulo cui ogni scheda appartiene.

Il programma **non scrive file quando valida**. Con `--generate` produce un `.ttl` per ciascun modulo trovato. Con `--check` confronta file già generati senza modificarli. Il codice Python è organizzato in moduli riutilizzabili, con docstring e test automatici.

## Struttura

```text
ontology-tool/
├── README.md
├── ontology_from_md.py          # Punto di ingresso
├── ontology-tool.yaml           # Namespace iniziali (configurabili)
├── requirements.txt             # Dipendenze
├── pyproject.toml               # Packaging e comando installabile
├── ddta_ontology/               # Libreria riutilizzabile
│   ├── default_config.yaml      # Configurazione caricabile anche dopo installazione
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── source.py
│   ├── yaml_support.py
│   ├── schema.py
│   ├── rdf_builder.py
│   ├── turtle.py
│   ├── workflow.py
│   ├── models.py
│   ├── errors.py
│   ├── trace.py
│   └── function_model.yaml
├── docs/
│   ├── ARCHITECTURE.md
│   └── PYTHON_WALKTHROUGH.md
└── tests/
    ├── fixtures/NETWORK_SAMPLE.md
    └── test_ontology_tool.py
```

## Installazione

È richiesto **Python 3.11 o successivo**. Aprire PowerShell nella cartella in cui si è estratto il tool:

```powershell
python -m venv .venv
$py = ".\.venv\Scripts\python.exe"
& $py -m pip install -r requirements.txt
& $py ontology_from_md.py --help
```

Per installare anche il comando `ontology-md` (opzionale):

```powershell
& $py -m pip install -e .
& ".\.venv\Scripts\ontology-md.exe" --help
```

Il programma usa librerie esistenti, senza implementare da zero parser Markdown, YAML o RDF: `markdown-it-py`, `PyYAML` e `RDFLib`. Per analizzare il codice usa il modulo standard `ast`.

## Comandi principali

`--source` accetta un singolo file Markdown (ripetibile); `--source-dir` cerca ricorsivamente i Markdown contenenti schede normative (ripetibile). Le due opzioni possono essere combinate.

```powershell
# Valida tutti gli MD normativi sotto la cartella indicata, senza creare TTL
& $py ontology_from_md.py --source-dir "C:\Progetto\ontologies"

# Valida solo un insieme esplicitamente selezionato di Markdown
& $py ontology_from_md.py --source "C:\Sorgenti\base.md" --source "C:\Sorgenti\estensione.md"

# Valida e genera un TTL per ogni modulo individuato
& $py ontology_from_md.py --source-dir "C:\Progetto\ontologies" --generate --output-dir "C:\Risultati\ttl"

# Confronta i TTL con i sorgenti attuali: nessuna scrittura
& $py ontology_from_md.py --source-dir "C:\Progetto\ontologies" --check --output-dir "C:\Risultati\ttl"

# Esporta una mappa statica di funzioni Python, chiamate e argomenti
& $py ontology_from_md.py --source-dir "C:\Progetto\ontologies" --export-call-map "C:\Risultati\calls.json"
```

Per l'elenco completo e le opzioni disponibili usare `--help`. I codici di uscita sono `0` (OK), `1` (errore di validazione/I/O) e `2` (opzioni CLI non valide).

## Aggiungere nuove ontologie

Il codice **non contiene un elenco fisso di moduli**. Puoi aggiungere un Markdown con un modulo nuovo a una cartella selezionata tramite `--source-dir`, oppure specificarlo con `--source`.

Per i nuovi namespace puoi scegliere tra due strategie:

1. Dichiarare un blocco `yaml ddta-namespace` nel Markdown (esempio sotto).
2. Aggiungere il modulo al file `ontology-tool.yaml`, oppure a un file equivalente selezionato con `--config`.

Un esempio minimo e indipendente dai moduli esistenti:

````markdown
```yaml ddta-namespace
module: network
prefix: network
namespace: https://example.org/ontologies/network#
```

```yaml ddta-ontology
record: class
module: network
iri: network:Router
status: approved
label:
  en: Router
  it: Router
definition:
  en: An identifiable forwarding resource.
  it: Una risorsa identificabile per l'inoltro dei dati.
```
````

Il programma produrrà `network.ttl`. Il file Markdown può chiamarsi come si preferisce. Si possono distribuire **più schede dello stesso modulo su più file `.md`**; le dichiarazioni vengono aggregate e validate insieme.

**Dipendenze fra moduli:** se `network:Router` deriva da `ddta:Resource`, la scheda di `ddta:Resource` deve essere inclusa fra gli input selezionati e il prefisso `ddta:` deve essere definito. La sola definizione del prefisso **non** equivale a dichiarare la classe. Questo comportamento previene dipendenze non documentate e definizioni OWL fittizie.

Le tre voci del file `ontology-tool.yaml` fornito sono soltanto **configurazioni iniziali per il vocabolario già disponibile**, non un vincolo sui moduli ammessi.

## Ambito e limiti

Sono elaborati soltanto i blocchi con info-string **esatta** `yaml ddta-ontology` e, facoltativamente, i blocchi `yaml ddta-namespace`. La validazione copre schema supportato, YAML, duplicati, stato `approved`, IRI e tipi delle relazioni. Al momento non genera SHACL e non valida matrici M1/M2, esempi, prosa o tutti i possibili costrutti OWL. Non esegue il codice degli esempi Markdown.

Per nuove categorie di dichiarazioni non previste (`record` diversi da classi/proprietà/individui) servirà un'estensione consapevole del parser e della serializzazione: **aggiungere un nuovo modulo non richiede modifiche Python; aggiungere una nuova grammatica sì**.

## Documentazione

- [Architettura, API, contratti e diagrammi Mermaid](docs/ARCHITECTURE.md)
- [Lettura guidata del codice e ripasso Python](docs/PYTHON_WALKTHROUGH.md)

La descrizione candidata in `ddta_ontology/function_model.yaml` e il JSON prodotto da `--export-call-map` sono due viste distinte: la prima descrive responsabilità logiche DDTA; la seconda chiamate tecniche rilevabili staticamente. Non equivalgono a una generazione automatica normativa di RDF sul programma.
