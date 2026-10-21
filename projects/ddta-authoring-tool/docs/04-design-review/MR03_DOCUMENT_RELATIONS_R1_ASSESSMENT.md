# MR-03 — Controllo sperimentale delle relazioni documentali R1

**Lifecycle:** `candidate`  
**Authority:** `EXPERIMENTAL_NON_CANONICAL`  
**Baseline di partenza:** `267465a` (`master`)  
**Data:** 2026-10-21

## Perimetro documentale

- `MR-03`: continuita' delle identita' e tracciabilita' dei documenti e delle BA; resta un MR piu' ampio del presente incremento.
- `DEC-MR03-01`: risoluzione dichiarativa dei riferimenti documentali a partire dall'identita' YAML.
- `FR-MR03-01-01`: indice dichiarativo univoco delle identita' dei documenti dello scope.
- `FR-MR03-01-02`: verifica tipizzata dei collegamenti MR → Decision → FR e delle dipendenze MR.
- Il contratto diagnostico e la verifica strutturale esistenti restano pertinenti a `MR-02` / `DEC-MR02-01`, `DEC-MR02-02`.

## Realizzazione tecnica candidata

`prototype/generic-v01/ddta_tool/relations.py` introduce `check_workspace()`. La CLI condivisa (`ddta_tool/__main__.py`) espone `check-workspace`. Lo scope e' una directory `docs/` con sottocartelle documentali riconosciute, oppure una di tali sottocartelle; il tool non pretende di verificare riferimenti fuori dallo scope selezionato. L'indice usa `id` e `type` dal front matter, mai il filename. `engine.validate()` continua a verificare ogni documento prima della risoluzione; il suo codice rimane invariato.

Codici nuovi principali: `REL-ID-DUPLICATE`, `REL-TARGET-MISSING`, `REL-TARGET-TYPE`, `REL-TARGET-AMBIGUOUS`, `REL-SCOPE-UNAVAILABLE`, `REL-SCOPE-EMPTY`, `REL-SCOPE-UNSUPPORTED`, `REL-SOURCE-READ`, `REL-IDENTITY-UNRESOLVED`. Le diagnostiche del motore conservano i codici `DOC-*` originali.

## Scenari di regressione

`tests/test_relations.py` include prove positive e negative: gerarchia valida, parent MR/Decision mancante, parent del tipo errato, ID duplicati anche tra tipi, riferimenti MR `dependsOn`, identita' indipendente dal filename, sorgente non interpretabile, scope vuoto/assente, `draft` non permissivo sui link, JSON CLI ed esiti deterministici. La suite originale `tests/test_generic.py` e gli esempi continuano a essere inclusi nelle verifiche.

`PREPARE.ps1` ricostruisce i file completi, esegue in un workspace temporaneo entrambe le suite e controlla il nuovo albero documentale `28/28` in `strict` prima di consentire l'applicazione. I risultati devono essere confermati dall'output PowerShell; questo documento non dichiara gia' eseguiti i test nella macchina dell'autore.

## Limiti espliciti

1. **Solo relazioni dichiarate e solo scope selezionato:** non vengono scandite directory arbitrarie del repository, link nei testi o file BA/Mermaid.
2. **Identita' BA:** nessuna risoluzione di BAReferent, BAProposition, sinonimi o equivalenze. Sono necessari altri costrutti D2/D3 di `MR-03`.
3. **Versioni e revisioni:** non viene implementata la tracciabilita' temporale fra versioni dello stesso documento.
4. **Significato dei legami:** un target formalmente risolto non attesta che il parent o la dipendenza siano semanticamente appropriati.
5. **Cicli dependsOn:** non viene ancora applicata una regola sui cicli; non e' stata assunta implicitamente come vincolo DDTA.
6. **Generazione da schema:** la grammatica dei campi di relazione e' ancora esplicita per i tre tipi correnti; l'estensione generica a nuovi tipi richiede una Decision specifica e, se necessario, una estensione del contratto YAML.

Non promuovere lo stato di `MR-03`, della Decision, dei due FR o delle proposition BA a `current` in conseguenza del solo superamento di test tecnici.
