# ONT-T01 — Protocollo E3 di matching semantico R1

**Stato:** REVIEW CANDIDATE — NON approvato, NON applicato retroattivamente alle annotazioni.
**Baseline di sviluppo:** Git `237a37a` (Gold Standard R3 candidato + pilota DeepSeek R1).
**Ambito:** estrazioni originali ONT-T01 con prompt O/R/A V1; prima il pilota DeepSeek, poi Qwen e Mistral con regole identiche. Gemini: NOT CHECKED finché il JSON originale non è disponibile.
**Fonti vincolanti per il caso:** testo ONT-T01 conservato in `research/ontology/ONT_T01_GOLD_STANDARD_R3.md`; unità e scoring_layer in `research/ontology/ONT_T01_GOLD_FACTS_R3.csv`. Le annotazioni pilota non costituiscono verità metodologica.

## P-01 — Unità e separazione delle metriche

1. Le 64 righe R3 sono unità di verifica e NON 64 osservazioni statisticamente indipendenti. Vietato presentare `MATCH/64` come accuratezza.
2. Strati: `ENTITY_MENTION`, `SEMANTIC_FACT`, `BEHAVIOR`, `POLARITY_CHECK`, `UNCERTAINTY_CHECK`, `TEMPORAL_CHECK`. Pubblicare il dettaglio per strato. Non sommare automaticamente menzioni R3-059..061 con relazioni R3-030..032 né R3-062 con R3-049/050.
3. Un record estratto può coprire più unità gold: es. DeepSeek `R-001` copre R3-025..027; `R-004` copre R3-030..032. L'inverso è ammesso: più record collegati possono sostenere una sola unità.
4. Oggetti, attributi, valori e referenti non sono necessariamente `BAReferent` autonomi. Non richiedere modellazione OWL, BA2 o specifici nomi canonici.

## P-02 — Significato dei giudizi

- **MATCH:** significato dell'unità conservato esplicitamente nell'output estratto, con partecipanti e qualificazioni essenziali; può essere distribuito in più record la cui connessione sia determinabile dai campi semantici, senza ricostruire il testo sorgente per colmare i vuoti.
- **PARTIAL:** nucleo del fatto riconoscibile, ma manca o è ambigua una condizione, un ruolo, un legame fra record, la modalità, la polarità o una distinzione d'identità essenziale.
- **MISSING:** nessun contenuto semanticamente utilizzabile nell'output per quella unità. Una citazione letterale da sola, priva di rappresentazione semantica del fatto, non basta per MATCH/PARTIAL, salvo che il modello annoti l'affermazione come contenuto di un campo semantico libero (`description`, `uncertainty`, `possibleInterpretations`, ecc.).
- **UNSUPPORTED:** affermazione positiva del modello non giustificata dal testo, da registrare in un audit autonomo per gli extra output. Non implica automaticamente contraddizione.
- **CONTRADICTED:** affermazione per cui il testo sorgente contiene un'evidenza contraria; registrare nell'audit degli extra, con doppia citazione e motivazione.

## P-03 — Rappresentazione, evidenze, collegamento

1. La valutazione è semantica, non lessicale: un nome diverso può coprire una menzione, e una relazione n-aria può coprire più fatti. Gli ID possono essere richiamati più volte.
2. `evidence` è **provenienza**: citazione esatta o non esatta da controllare in E2. Non costituisce automaticamente una proprietà semantica codificata. Se il modello scrive `condition:null` e soltanto l'evidenza contiene «Se...» o «Dopo...», il fatto condizionale non è `MATCH` (di norma `PARTIAL` se il nucleo dell'azione è presente).
3. Una condizione può essere espressa in `condition`, `description`, `uncertainty`, ruoli espliciti o più record semanticamente connessi: non è obbligatorio il nome `condition`. La connessione deve essere tracciabile tramite ID, partecipanti o riferimento univoco, **non solo attraverso l'ordine dei record o una citazione comune**.
4. La registrazione di un comportamento con `condition:null` non implica comportamento incondizionato se non viene affermato esplicitamente; si segnala come qualificazione non rappresentata, non automaticamente `CONTRADICTED`.
5. Conservare la distinzione fra «richiede la riserva», «riserva eseguita» e «conferma della riserva»; non dedurre chi compie o comunica la conferma. Conservare modalità `CAPABILITY` per la possibilità di acquisto; non convertirla in acquisto storico.
6. Ruolo `actorId:null` può essere corretto per frasi passive; non penalizzare un attore che il testo non specifica. Non equiparare il Notification Service a mittente certo. Identità «disponibilità» / «informazioni sulla disponibilità» e «quantità richieste» / «quantità ordinate» non devono essere forzate.
7. Il «dopo la conferma» è antecedente comune del passaggio a Confirmed e della notifica; non richiedere un ordine tra questi ultimi. «Prima di contattare Payment Service» non significa «mai contattato».
8. Negazione esplicita: la piattaforma non gestisce l'infrastruttura, ma utilizza il servizio. Assenza di protocollo specificato ≠ assenza di protocollo; analogamente per meccanismo di annullamento.

## P-04 — Procedura riproducibile per ogni unità

1. Leggere fatto, evidence, qualification, modality, scoring_layer del gold R3; citare l'ID gold.
2. Identificare gli ID reali dei record estratti (`O-*`, `R-*`, `A-*` o `ambiguities[index]` zero-based). Non inventare riferimenti.
3. Descrivere quali campi **semantici** preservano il fatto; conservare `evidence` come campo di provenienza separato.
4. Controllare partecipanti, ruolo, modalità, condizione, negazione, ordine e incertezza; motivare esplicitamente MATCH/PARTIAL/MISSING.
5. Salvare `review_status=PROVISIONAL_NEEDS_HUMAN_REVIEW` fino al riesame indipendente e alla decisione di congelamento.
6. Dopo i 64 giudizi, condurre audit extra-gold indipendente per UNSUPPORTED/CONTRADICTED, con riferimento agli ID degli output e al testo sorgente. **Non interpretare assenza di segnalazioni come assenza di errori.**
7. Per ogni modifica alle valutazioni del pilota, produrre un file di differenze separato; NON sovrascrivere il CSV pilota archiviato.

## P-05 — Esempi e casi-limite del pilota DeepSeek

| Gold | Record DeepSeek | Applicazione della regola (non giudizio definitivo) |
|---|---|---|
| R3-025..027 | R-001 | Una relazione n-aria preserva tutte e tre le proprietà del prodotto; niente penalità per aggregazione. |
| R3-030..032 | R-004 | Stessa regola per i tre campi della richiesta. |
| R3-044 | A-007 | L'azione di registrazione c'è, ma `condition:null`; la condizione della disponibilità compare nel testo sorgente e nel vicino A-006, senza un collegamento strutturato certo ad A-007: ricontrollare come `PARTIAL` candidato. |
| R3-045 | A-008 | «Successivamente» è nella sola evidence; precedenza temporale non codificata: `PARTIAL` candidato. |
| R3-048 | A-012 | La condizione di autorizzazione è esplicita: possibile `MATCH`, verificando tutti i ruoli. |
| R3-050 / R3-062 | A-014 / A-013 | `condition` fa riferimento alla conferma; non dedurre l'ordine tra notifica e stato Confirmed. |
| R3-057 | O-001 / O-002 / O-003 | La evidence menziona la capacità d'acquisto, ma oggetti citanti la frase non formalizzano di per sé il comportamento: ricontrollare come `MISSING` candidato, salvo rappresentazione semantica altrove. |
| R3-006 / R3-064 | O-009 / R-003 / A-003 | Valutare la copertura linguistica distinguendo l'identità ontologica non risolta dalla fusione esplicita impropria; non imporre separazione di BAReferent. |

## P-06 — Stato del protocollo e congelamento

**Questo protocollo è un candidato**, non è ancora una regola congelata. Per adottarlo occorre: riesame umano dei casi P-05 e delle 64 righe del pilota; decisione esplicita sulle rubriche di condizioni e collegamenti tra record; approvazione di una versione identificata del protocollo. Solo allora riprendere DeepSeek secondo la versione approvata e applicarla, invariata, a Qwen/Mistral. Le etichette e i conteggi 55/9/0 del pilota R1 restano storici e non sono punteggi approvati.

**Non modifica:** Gold R1/R2/R3, output originali O/R/A, prompt V1, ontologie BA1/BA2/BA3 e pilota DeepSeek R1.
