# ONT-T01 V2 — Esecuzione singolo prompt per modello

**Status:** REVIEW CANDIDATE. **Baseline Git:** `2569141` (il file R3 delle 190 assessment potrebbe trovarsi soltanto nella working copy). I dati originali non vengono modificati.

## Procedura

1. Eseguire `python research/ontology/experiments/ONT_T01/V2/BUILD_V2_SINGLE_ROUND_R1.py` dalla root del repository. Il builder legge tre JSON V1 e la matrice V1 locali e genera **tre prompt completi `.txt`**, un report V1 provvisorio e un manifest con SHA256. I prompt sono grandi e comprendono **testo originale + tre JSON integrali**. Non incollare i soli titoli o gli snippet.
2. Incollare `ONT_T01_V2_PROMPT_DEEPSEEK_R1.txt` in una nuova chat con DeepSeek, `...QWEN...` con Qwen e `...MISTRAL...` con Mistral. Utilizzare modelli e versioni identificabili; se non disponibili documentare modello effettivamente usato. Nessuna seconda iterazione né accesso alle altre risposte V2. Non aggiungere il Gold Standard né le valutazioni V1.
3. Salvare per intero ciascuna risposta (incluso testo, blocchi JSON, eventuali errori/troncamenti) in `ONT_T01_V2_RAW_DEEPSEEK_R1.txt`, `ONT_T01_V2_RAW_QWEN_R1.txt`, `ONT_T01_V2_RAW_MISTRAL_R1.txt` nella cartella V2. Indicare nel successivo resoconto data, versione e interfaccia usata. Non correggere silenziosamente JSON non validi.
4. Dopo aver raccolto le tre risposte, procedere direttamente al confronto V1–V2 e al rapporto finale ONT-T01. Nessun'altra worklist preparatoria.

Il builder produce soltanto input reali da inviare alle chat; **non genera né simula output V2**.

**Vincoli metodologici:** sei confronti direzionali interni a tre analisi, ma solo **tre chiamate LLM**. Le fonti di verità sono esclusivamente le frasi del testo ONT-T01. L'esito V1 è provvisorio; nessun `MATCH/64` viene riportato come accuracy. L'attribuzione di un miglioramento a un peer è solo indiziaria.
