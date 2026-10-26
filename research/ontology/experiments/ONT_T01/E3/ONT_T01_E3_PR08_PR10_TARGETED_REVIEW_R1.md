# ONT-T01 — PR-08 e PR-10: riesame mirato R1 (REVIEW CANDIDATE)

**Baseline Git:** `8e4449e`. **Stato:** PROPOSTE; nessuna decisione approvata e nessun protocollo congelato. Le annotazioni storiche E3 e gli output originali restano invariati.

## PR-08 — Verifica della capacità R3-057

- **Fonte originale:** «Una piattaforma di commercio elettronico permette ai clienti di acquistare prodotti disponibili nel catalogo.»
- **Rappresentazione DeepSeek:** `O-001`, `O-002`, `O-003` nominano gli oggetti e riportano la frase in `evidence`; `O-034` nomina «Acquisto» e `A-001` codifica la **conferma** di un acquisto, che non equivale alla **capacità** della piattaforma di permetterlo.
- **Controllo:** ricerca in tutti i campi tranne `evidence` delle quattro collezioni `objects`, `relations`, `actions`, `ambiguities`. Le menzioni di «acquisto» non codificano una relazione di abilitazione. Non emerge un predicato semantico «permette/abilita i clienti ad acquistare».
- **Proposta di delta:** `R3-057`, DeepSeek, `PARTIAL → MISSING` secondo PR-01/PR-08. **Non aggiornare** `ONT_T01_E3_DEEPSEEK_PILOT_MATCH_R1.csv`; non cambiare automaticamente altri matching.
- **Limite:** questa è una valutazione mirata guidata dalla rubrica candidata, non un audit completo degli extra-gold né una seconda valutazione indipendente.
- **SHA-256 input originale:** `ca7bf015ad7757de766f4a629722ba9ce2b72fc6d0705045a59172b4a4409e75`.

## PR-10 — Piano di revisione indipendente

- **Popolazione:** 64 unità gold, con 9 `PARTIAL` e 55 `MATCH` nella matrice DeepSeek storica; queste sono etichette candidate, non esiti approvati.
- **Campione:** 23 unità: tutte le **9 PARTIAL** più **14 MATCH** stratificate per `ENTITY_MENTION`, `SEMANTIC_FACT`, `BEHAVIOR`, `POLARITY_CHECK`, `UNCERTAINTY_CHECK`, `TEMPORAL_CHECK`. È un campione mirato/non probabilistico: non permette stime imparziali della performance globale né intervalli di confidenza.
- **Cecità:** consegnare al secondo annotatore il CSV `...BLIND_SAMPLE...` con gold, fonte, output originale e protocollo candidato, **senza** matrice pilota e senza file di riconciliazione, che contiene le etichette storiche.
- **Compilazione:** `independent_assessment ∈ {MATCH, PARTIAL, MISSING}`; indicare `extracted_ids`, campi semantici (non solo `evidence`), razionale e identità dell'annotatore. Lo stato rimane `AWAITING_INDEPENDENT_ANNOTATION` fino all'esecuzione reale.
- **Riconciliazione:** soltanto dopo la consegna irrevocabile del giudizio indipendente, confrontare con l'etichetta pilota e compilare `...RECONCILIATION...`; disaccordi riesaminati da adjudicator distinto, con motivazione e fonte citata. Registrare anche accordi e casi controversi con accordo apparente.
- **Misura:** pubblicare accordo grezzo per layer sul campione, matrice delle confusioni e lista dei disaccordi; Cohen kappa solo se appropriato e con caveat su prevalenza, piccolo n e campione intenzionale. **Nessuna soglia numerica di approvazione automatica** da questo pilota; tutte le divergenze sostanziali devono ricevere decisione motivata.
- **Revisione di completezza:** dopo il campione, doppia verifica degli altri 41 casi prima di dichiarare *tutti i 64* approvati; un campione non approva la popolazione intera.

## Stato degli artefatti

- `...BLIND_SAMPLE_R1.csv`: modulo indipendente **non compilato**.
- `...RECONCILIATION_TEMPLATE_R1.csv`: confronto futuro **non compilato**; NON consegnare in blind review.
- `...PR08_REASSESSMENT_CANDIDATE_R1.csv`: proposta R3-057, NON decisione definitiva.
- Nessuna modifica al Gold R3, al Protocollo E3 R1, ai 64 matching storici, o ai JSON LLM V1.
