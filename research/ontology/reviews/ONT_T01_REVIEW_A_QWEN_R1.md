# Rapporto di Revisione Indipendente — Gold Standard ONT-T01 R1

## 1. Valutazione generale

Il gold standard ONT-T01 R1 rappresenta un tentativo metodologicamente solido di catturare i fatti semanticamente rilevanti del testo originale. La distinzione tra classi O/R/A/N/U è coerente con le regole di estrazione, e le qualifiche temporali/condizionali (TRIGGER, SE, DOPO, QUANDO, PRIMA) sono applicate con rigore.

**Punti di forza:**

- Separazione corretta tra fatti positivi, negazioni esplicite e lacune informative
- Conservazione delle condizioni e dell'ordine temporale senza trasformarli in eventi verificati
- Evidenze letterali generalmente corrette
- Nota metodologica esplicita sulla non-automaticità delle normalizzazioni

**Criticità rilevate:**

- Tre oggetti esplicitamente menzionati nel testo (identificativo del cliente, prodotti selezionati, quantità richieste) sono assenti come referenti autonomi
- Una relazione esplicita (prodotti disponibili nel catalogo) non è modellata
- Un evento/risultato menzionato ("conferma della riserva") non è catturato come fatto
- Alcune evidenze sono troncate o incomplete
- Granularità disomogenea tra attributi del prodotto (aggregati) e campi della richiesta (aggregati ma con oggetti mancanti)

**Idoneità all'uso:** Il gold standard richiede una revisione mirata prima di poter essere utilizzato come riferimento sperimentale. I problemi identificati non invalidano l'impianto metodologico, ma compromettono la completezza e la tracciabilità di fatti espliciti nel testo.

---

## 2. Finding

| Finding ID | Gold Fact ID | Tipo        | Severità | Evidenza letterale                                                                                     | Motivazione verificabile                                                                                                                                                                                                                                        | Correzione proposta                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------- | ------------ | ----------- | -------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| F-001      | NEW          | MISSING     | HIGH     | "l'identificativo del cliente"                                                                         | Il testo menziona esplicitamente "l'identificativo del cliente" come contenuto della richiesta. Non è modellato come oggetto autonomo nel gold standard.                                                                                                        | Aggiungere nuovo fatto: `GS-053, O, Identificativo del cliente, IdentificativoCliente, , "l'identificativo del cliente",`                                                                                                                                                                                                                                                                                                              |
| F-002      | NEW          | MISSING     | HIGH     | "i prodotti selezionati"                                                                               | Il testo menziona esplicitamente "i prodotti selezionati" come contenuto della richiesta. Non è modellato come oggetto autonomo.                                                                                                                                | Aggiungere nuovo fatto: `GS-054, O, Prodotti selezionati, ProdottiSelezionati, , "i prodotti selezionati",`                                                                                                                                                                                                                                                                                                                            |
| F-003      | NEW          | MISSING     | HIGH     | "le quantità richieste"                                                                                | Il testo menziona esplicitamente "le quantità richieste" come contenuto della richiesta. Non è modellato come oggetto autonomo.                                                                                                                                 | Aggiungere nuovo fatto: `GS-055, O, Quantità richieste, QuantitaRichieste, , "le quantità richieste",`                                                                                                                                                                                                                                                                                                                                 |
| F-004      | NEW          | MISSING     | MEDIUM   | "prodotti disponibili nel catalogo"                                                                    | Il testo afferma che i prodotti sono "disponibili nel catalogo", stabilendo una relazione di appartenenza/disponibilità non modellata nel gold standard.                                                                                                        | Aggiungere nuovo fatto: `GS-056, R, Prodotti disponibili nel catalogo, Prodotto → Catalogo, , "prodotti disponibili nel catalogo",`                                                                                                                                                                                                                                                                                                    |
| F-005      | NEW          | MISSING     | MEDIUM   | "Dopo la conferma della riserva"                                                                       | Il testo menziona esplicitamente "la conferma della riserva" come evento/risultato che precede il cambio di stato. Non è modellato come fatto.                                                                                                                  | Aggiungere nuovo fatto: `GS-057, O, Conferma della riserva, ConfermaRiserva, Evento/risultato, "Dopo la conferma della riserva",`                                                                                                                                                                                                                                                                                                      |
| F-006      | GS-025       | GRANULARITY | MEDIUM   | "Ogni prodotto possiede un identificativo, una descrizione e un prezzo"                                | GS-025 aggrega tre relazioni distinte in una sola. Il gold standard stesso riconosce l'ambiguità nella nota di review. Per confronto LLM, è preferibile separare le relazioni.                                                                                  | Sostituire GS-025 con tre fatti distinti: `GS-025a, R, Prodotto possiede identificativo, Prodotto → Identificativo, , "Ogni prodotto possiede un identificativo"; GS-025b, R, Prodotto possiede descrizione, Prodotto → Descrizione, , "una descrizione"; GS-025c, R, Prodotto possiede prezzo, Prodotto → Prezzo, , "e un prezzo"`                                                                                                    |
| F-007      | GS-028       | GRANULARITY | MEDIUM   | "la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste" | GS-028 aggrega tre contenuti della richiesta in una sola relazione. Con l'aggiunta di F-001, F-002, F-003, è preferibile separare le relazioni di contenimento.                                                                                                 | Sostituire GS-028 con tre fatti distinti: `GS-028a, R, La richiesta contiene identificativo cliente, Richiesta → IdentificativoCliente, , "la richiesta contenente l'identificativo del cliente"; GS-028b, R, La richiesta contiene prodotti selezionati, Richiesta → ProdottiSelezionati, , "i prodotti selezionati"; GS-028c, R, La richiesta contiene quantità richieste, Richiesta → QuantitaRichieste, , "le quantità richieste"` |
| F-008      | GS-009       | EVIDENCE    | LOW      | "la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste" | L'evidenza è corretta, ma il nome "Richiesta di acquisto" è una normalizzazione non presente nel testo. Il testo dice solo "la richiesta". La qualifica "Rinominazione" è corretta, ma andrebbe chiarito che è una scelta modellistica, non un fatto del testo. | Mantenere GS-009 ma aggiungere nota: "Normalizzazione accettabile per disambiguazione, ma il testo usa solo 'la richiesta'. Confrontare anche con output che usano 'Richiesta' senza qualifica."                                                                                                                                                                                                                                       |
| F-009      | GS-024       | EVIDENCE    | LOW      | "ma non ne gestisce l'infrastruttura"                                                                  | L'evidenza "l'infrastruttura" è tronca e non autosufficiente. Dovrebbe includere il contesto della negazione.                                                                                                                                                   | Correggere evidenza in: "ma non ne gestisce l'infrastruttura" oppure "La piattaforma utilizza il suo servizio, ma non ne gestisce l'infrastruttura"                                                                                                                                                                                                                                                                                    |
| F-010      | GS-018       | UNCERTAINTY | LOW      | "quantità ordinate"                                                                                    | GS-018 nota "Equivalenza con QuantitaRichieste non dichiarata", ma non esiste un oggetto GS per "Quantità richieste". Con l'aggiunta di F-003, questa relazione di equivalenza/non-equivalenza va esplicitata.                                                  | Aggiungere nota: "Da verificare se QuantitaOrdinate e QuantitaRichieste sono lo stesso referente o referenti distinti (richiesta vs ordine). Il testo non chiarisce."                                                                                                                                                                                                                                                                  |
| F-011      | NEW          | MISSING     | LOW      | "permette ai clienti di acquistare prodotti"                                                           | Il testo attribuisce alla piattaforma la capacità/funzione di permettere l'acquisto. Questo comportamento non è modellato come fatto.                                                                                                                           | Aggiungere nuovo fatto: `GS-058, A, Piattaforma permette acquisto, Piattaforma → Cliente → Prodotto, CAPACITÀ, "permette ai clienti di acquistare prodotti",`                                                                                                                                                                                                                                                                          |

---

## 3. Questioni modellistiche

**3.1 Granularità delle relazioni di possesso/composizione**

Il gold standard aggrega GS-025 (attributi del prodotto) e GS-028 (contenuti della richiesta) in relazioni multiple. Questa scelta è metodologicamente difendibile se si adotta il principio "relazioni aggregate o suddivise sono ammissibili se preservano tutti i fatti" (sezione 1 del Markdown).

Tuttavia, per il confronto LLM, la granularità fine è preferibile perché:

- Permette di valutare separatamente la correttezza di ogni relazione
- Evita che un errore parziale (es. dimenticare un attributo) invalidi l'intera relazione aggregata
- Facilita il matching con output che usano rappresentazioni diverse

**Raccomandazione:** Adottare granularità fine (tre relazioni binarie invece di una n-aria) come preferenza, ma accettare entrambe le rappresentazioni come semanticamente equivalenti se l'output LLM preserva tutti i fatti.

**3.2 Normalizzazione dei nomi**

GS-009 ("Richiesta di acquisto") e GS-018 ("Quantità ordinate") introducono normalizzazioni non presenti nel testo. Il gold standard riconosce esplicitamente queste scelte nelle qualifiche, il che è corretto.

**Raccomandazione:** Nel confronto LLM, considerare MATCH anche se l'output usa il termine esatto del testo ("la richiesta", "quantità richieste") senza normalizzazione. La normalizzazione è accettabile ma non obbligatoria.

**3.3 Identificazione del mittente/attore**

Il gold standard segnala correttamente (GS-034, GS-038, GS-043, GS-045, GS-046, GS-047, GS-048, GS-051) i casi in cui l'attore o il mittente non sono specificati. Questo è coerente con la regola "I campi non menzionati non si presumono né positivi né negativi".

**Raccomandazione:** Nel confronto LLM, penalizzare come UNSUPPORTED qualsiasi output che attribuisca un attore non documentato (es. "Order Service invia notifica" quando il testo dice solo "viene inviata una notifica tramite Notification Service").

**3.4 Distinzione tra richiesta ed esecuzione**

GS-044 e GS-052 distinguono correttamente tra "Order Service richiede riserva" e "esecuzione della riserva". Il testo dice "richiede all'Inventory Service di riservare" e "Dopo la conferma della riserva", indicando che la richiesta e la conferma sono eventi distinti.

**Raccomandazione:** Nel confronto LLM, considerare CONTRADICTED qualsiasi output che presenti la riserva come eseguita incondizionatamente, senza menzionare la conferma.

---

## 4. Verifica di coerenza Markdown–CSV

Ho verificato la corrispondenza tra i 52 fatti nel Markdown e nel CSV.

**Risultato:** Coerenza completa per tutti i fatti da GS-001 a GS-052.

**Dettagli:**

- Tutti gli ID sono presenti in entrambi i file
- Le colonne `classe`, `fato_atomico`, `qualificazione`, `evidenza_esatta` corrispondono
- Le note di review nel CSV corrispondono alle qualifiche nel Markdown
- La colonna `partecipanti_normalizzati` nel CSV non ha corrispondente nel Markdown, ma questo è previsto dalla struttura (è un'aggiunta per facilitare il confronto)

**Nessuna discrepanza rilevata.**

---

## 5. Proposte di modifica

### 5.1 Fatti da aggiungere (NEW)

```
csv
```

`GS-053,O,Identificativo del cliente,IdentificativoCliente,,"l'identificativo del cliente", GS-054,O,Prodotti selezionati,ProdottiSelezionati,,"i prodotti selezionati", GS-055,O,Quantità richieste,QuantitaRichieste,,"le quantità richieste", GS-056,R,Prodotti disponibili nel catalogo,Prodotto → Catalogo,,"prodotti disponibili nel catalogo", GS-057,O,Conferma della riserva,ConfermaRiserva,Evento/risultato,"Dopo la conferma della riserva", GS-058,A,Piattaforma permette acquisto,Piattaforma → Cliente → Prodotto,CAPACITÀ,"permette ai clienti di acquistare prodotti",`

### 5.2 Fatti da modificare

**GS-024:** Correggere l'evidenza da `"l'infrastruttura"` a `"ma non ne gestisce l'infrastruttura"`

**GS-025:** Sostituire con tre fatti distinti (vedere F-006)

**GS-028:** Sostituire con tre fatti distinti (vedere F-007)

### 5.3 Note da aggiornare

**GS-009:** Aggiungere nota: "Normalizzazione accettabile per disambiguazione, ma il testo usa solo 'la richiesta'"

**GS-018:** Aggiornare nota: "Da verificare se QuantitaOrdinate e QuantitaRichieste (GS-055) sono lo stesso referente o referenti distinti"

### 5.4 Fatti da eliminare

Nessuno. Tutti i 52 fatti originali sono supportati dal testo.

---

## 6. Valutazione finale

**Classificazione:** REVISION_REQUIRED

**Motivazione:**

Il gold standard ONT-T01 R1 presenta un impianto metodologico solido e coerente con le regole di estrazione ontologica preliminare. La distinzione tra fatti positivi, negazioni e lacune è corretta, e le condizioni temporali sono ben preservate.

Tuttavia, sono stati identificati **tre fatti mancanti ad alta priorità** (identificativo del cliente, prodotti selezionati, quantità richieste) che sono esplicitamente menzionati nel testo come contenuti della richiesta. La loro assenza compromette la completezza del gold standard e potrebbe portare a penalizzare erroneamente output LLM che li includono correttamente.

Inoltre, sono stati identificati **due fatti mancanti a media priorità** (relazione prodotti-catalogo, conferma della riserva) e **problemi di granularità** (GS-025, GS-028) che, sebbene non invalidino l'impianto, riducono la precisione del confronto.

Le correzioni proposte sono mirate e non richiedono una ristrutturazione completa del gold standard. Dopo l'implementazione delle modifiche indicate nella sezione 5, il gold standard sarà pronto per la valutazione.

**Tempo stimato per la revisione:** 1-2 ore per un revisore umano.