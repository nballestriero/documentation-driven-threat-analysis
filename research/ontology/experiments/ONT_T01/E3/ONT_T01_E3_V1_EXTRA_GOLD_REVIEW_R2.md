# ONT-T01 — audit extra-gold, passaggio operativo R2

**Stato:** REVIEW CANDIDATE; input Git `b8c3c3f`. Non conclude la revisione indipendente né approva etichette.

## Distinzione metodologica

Il registro R2 propone una disposition per **13 finding preesistenti**. Le categorie `UNSUPPORTED_CANDIDATE`, `QUALIFICATION_LOSS_NOT_EXTRA`, `HYPOTHESIS_NOT_ASSERTION`, `IDENTITY_AMBIGUITY`, `CONTEXT_DEPENDENT`, `SUPPORTED_CANDIDATE` e `MODALITY_REVIEW` sono triage e **non** esiti definitivi. `CONTRADICTED` richiederebbe una frase contraria esplicita, che non è stata individuata fra i 13 casi; ciò NON significa zero contraddizioni nell'intero output.

Tre candidati Qwen meritano priorità per attribuzione/esecuzione, quantità richieste vs ordinate e conferma della richiesta vs acquisto. Le alternative possibili in `ambiguities` non sono asserzioni positive. I record devono essere letti integralmente, non solo attraverso etichette e citazioni.

## Copertura esaustiva e limiti

L'inventario storico contiene 190 record (DEEPSEEK 60; QWEN 67; MISTRAL 63). La **worklist generata** mantiene 190 righe con `review_status=PENDING_HUMAN_SEMANTIC_REVIEW`, inclusi i 13 segnalati: la creazione delle righe non è un giudizio semantico. Verificare per ciascun record ruoli, target, modalità, evidenze, eventuali claim distinti; inserire un giudizio per claim e una conclusione per record. Per ogni `UNSUPPORTED` citare claim e fonte esatta che non lo supporta; per `CONTRADICTED` anche la fonte contraria. Non derivare precision o hallucination-rate da questo triage.

## Prossimo step

Completare la worklist e una tabella di claim specifici, risolvere i casi controversi tramite adjudication, poi PR-10 e consolidamento V1. Non modificare gli output originali, Gold, matrici V1 o audit precedenti.
