# ONT-T01 — Procedura pilota Ollama R3

Questa release **sostituisce R1/R2**; se non sono state installate, installare solo R3.

## Protocollo

- Due LLM (default: `qwen2.5-coder:3b`, `llama3.2:3b`) elaborano indipendentemente il testo ONT-T01 e la stessa ontologia base. Temperatura 0, seed 42.
- Al termine di ogni richiesta, inclusi retry invalidi, il client usa `keep_alive: 0` e richiede lo scaricamento del modello con `/api/generate`. La memoria liberabile è quella dei pesi gestiti da Ollama, non tutta la RAM di Windows; controllare anche `ollama ps`. Il server Ollama resta attivo.
- Dopo entrambe le estrazioni iniziali, attesa obbligatoria di **120 secondi** prima della revisione.
- Ciascun modello riceve una sola volta il risultato dell'altro. Un modello critica e rifiuta gli elementi non supportati, conserva quanto supportato, e restituisce un JSON completo. Sono 2 revisioni, **4 generazioni valide totali**.
- Non si chiede consenso a tutti i costi. La fonte originale prevale; Gold non incluso nei prompt. Gli output vengono validati per schema, identificativi, riferimenti, evidenze letterali; eventuali errori vengono inoltrati al modello per la correzione, max tre tentativi.
- Ogni output iniziale, intermedio e finale è conservato; ogni tentativo e parametri nel log. L'ordine dei due incontri è sequenziale (il secondo può vedere la revisione del primo), senza pretese di neutralità.
- L'esecuzione è riprendibile se gli artefatti salvati sono validi. Ogni cartella output è legata a modello, fonte, parametri e protocollo.

## Installazione / prova

Da `C:\Users\user\Documents\TESI`:

```powershell
$T = 'research\ontology\tools\ollama_collab'
python "$T\test_ont_ollama.py"
ollama list
# Scaricare soltanto i modelli mancanti:
ollama pull qwen2.5-coder:3b
ollama pull llama3.2:3b
```

Per ottenere il testo fonte di ONT-T01 usare un file UTF-8 che contenga **solo** il testo originale, verbatim: `source_ONT_T01.txt`; non includere Gold o prompt V2. Un file fonte è necessario e deve essere controllato rispetto al documento R3 originale.

```powershell
$T = 'research\ontology\tools\ollama_collab'
python "$T\ont_ollama.py" run --config "$T\models.example.json" --source "$T\source_ONT_T01.txt" --test-id ONT-T01 --output "$T\runs\ONT_T01_R3_PILOT"
python "$T\ont_ollama.py" check --config "$T\models.example.json" --source "$T\source_ONT_T01.txt" --test-id ONT-T01 --output "$T\runs\ONT_T01_R3_PILOT"
```

Non aggiungere `runs/` a Git senza revisione: contiene output voluminosi. Questo ambiente non ha eseguito inferenze Ollama; serve test locale.

## Risultati

`initial/` contiene i 2 JSON iniziali, `steps/` le 2 revisioni, `final/` le 2 estrazioni finali. Il confronto semantico con Gold e modelli online è **un'analisi successiva** e non è generato automaticamente dalla validazione strutturale.
