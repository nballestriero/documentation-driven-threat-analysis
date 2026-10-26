# ONT-T01 — Gold Standard R3 (REVIEW CANDIDATE)

**Baseline di ingresso:** `9b040f7`. **Origine:** Gold R2 + semantic review R1 (SR-01..SR-15). **Stato:** REVIEW CANDIDATE, NON normativo, NON approvato. **R1/R2:** invariati.

## Protocollo di interpretazione e valutazione

1. L'unica fonte di fatti per il caso è il testo ONT-T01 riprodotto in fondo al documento. I finding di LLM e la review semantica non sono fonti di verità.
2. Le 64 righe sono **unità di verifica**, NON 64 osservazioni indipendenti e NON un denominatore unico di accuratezza. Non pubblicare un punteggio aggregato `MATCH/64`.
3. **ENTITY_MENTION (O):** copertura dei referenti/menzioni. **SEMANTIC_FACT (R):** relazioni e ruoli. **BEHAVIOR (A):** azione, attore, input/risultato, modalità e condizione. Le dimensioni trasversali **POLARITY_CHECK (N)**, **UNCERTAINTY_CHECK (U)**, **TEMPORAL_CHECK (T)** si riportano separatamente, senza somme automatiche alle altre dimensioni.
4. Le menzioni R3-059..061 e i legami R3-030..032 hanno informazioni sovrapposte; documentare entrambi gli esiti ma non trasformarli in sei premi indipendenti. Anche R3-062 e le qualifiche di R3-049/050 non si sommano automaticamente.
5. La granularità di annotazione è atomica; l'output LLM può rappresentare tre attributi tramite una relazione n-aria, più relazioni binarie o proprietà strutturate, purché preservi tutti i fatti.
6. `CAPABILITY` = comportamento abilitato, non occorrenza storica. `CONDITIONAL_OR_ORDERED` = comportamento descritto con trigger/guardia/ordine, non evento osservato. Non equiparare richiesta di riserva, esecuzione e conferma. Non attribuire attori/destinatari senza evidenza.
7. `EXPLICIT_UNSPECIFIED` e `UNRESOLVED_IN_TEXT` sono distinti. Non generare U per qualunque ruolo teoricamente assente. `NEGATED` non implica assenza di servizio; separare uso positivo e mancata gestione dell'infrastruttura.
8. Confrontare per significato, non per ID o numero di record JSON. Marcature per unità: `MATCH`, `PARTIAL`, `MISSING`. `UNSUPPORTED`/`CONTRADICTED` si verificano anche sulle affermazioni extra rispetto al gold. Una fusione di identità non supportata richiede nota distinta.
9. Un'evidenza esatta deve essere sottostringa contigua del testo originale e deve supportare il **fatto intero**, incluse qualifiche, modalità e ruoli. Se serve più di uno span, fornire più evidenze separatamente, non una citazione sintetica ricostruita. Le quattro citazioni estese SR-01..04 sono ora complete.
10. Per `Confirmed` e invio notifica è documentato il comune antecedente «Dopo la conferma della riserva»; non dedurre un ordine tra i due eventi. «Prima di contattare Payment Service» non significa «mai contattato».
11. Il CSV è il registro operativo; il Markdown è il protocollo e la vista leggibile. La trace R2→R3 è nel file separato. R3 non modifica il contratto BA1/BA2/BA3 né obbliga identità BAReferent autonome.
12. **Review ancora richiesta:** neutralità degli indicatori, valore dei ruoli impliciti e delle menzioni ai fini del matching, controllo umano delle 64 interpretazioni. Nessuna metrica LLM pubblicata.

## Le 64 unità

| ID | Dim. | Fatto | Source R2 | Evidence |
|---|---|---|---|---|
| R3-001 | O | Piattaforma di commercio elettronico | R2-001 | Una piattaforma di commercio elettronico |
| R3-002 | O | Cliente/i | R2-002 | ai clienti |
| R3-003 | O | Prodotto/i | R2-003 | Ogni prodotto possiede |
| R3-004 | O | Catalogo | R2-004 | nel catalogo |
| R3-005 | O | Catalog Service | R2-005 | Catalog Service |
| R3-006 | O | Informazioni sulla disponibilità | R2-006 | informazioni sulla disponibilità |
| R3-007 | O | Inventory Store | R2-007 | Inventory Store |
| R3-008 | O | Order Service | R2-008 | Order Service |
| R3-009 | O | Richiesta | R2-009 | la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste |
| R3-010 | O | Inventory Service | R2-010 | Inventory Service |
| R3-011 | O | Quantità disponibili | R2-011 | quantità disponibili |
| R3-012 | O | Ordine | R2-012 | crea un ordine |
| R3-013 | O | Order Store | R2-013 | Order Store |
| R3-014 | O | Payment Service | R2-014 | Payment Service |
| R3-015 | O | Autorizzazione del pagamento | R2-015 | l'autorizzazione del pagamento |
| R3-016 | O | Payment Provider | R2-016 | Payment Provider esterno |
| R3-017 | O | Esito autorizzazione | R2-017 | l'esito dell'autorizzazione |
| R3-018 | O | Quantità ordinate | R2-018 | quantità ordinate |
| R3-019 | O | Stato Confirmed | R2-019 | stato Confirmed |
| R3-020 | O | Notifica al cliente | R2-020 | una notifica al cliente |
| R3-021 | O | Notification Service | R2-021 | Notification Service |
| R3-022 | O | Stato Rejected | R2-022 | come Rejected |
| R3-023 | O | Organizzazione esterna | R2-023 | un'organizzazione esterna |
| R3-024 | O | Infrastruttura associata al servizio del Payment Provider | R2-024 | La piattaforma utilizza il suo servizio, ma non ne gestisce l'infrastruttura. |
| R3-025 | R | Prodotto possiede identificativo | R2-025 | Ogni prodotto possiede un identificativo, una descrizione e un prezzo. |
| R3-026 | R | Prodotto possiede descrizione | R2-026 | Ogni prodotto possiede un identificativo, una descrizione e un prezzo. |
| R3-027 | R | Prodotto possiede prezzo | R2-027 | Ogni prodotto possiede un identificativo, una descrizione e un prezzo. |
| R3-028 | R | Catalog Service mantiene catalogo | R2-028 | Il catalogo viene mantenuto dal Catalog Service |
| R3-029 | R | Informazioni disponibilità conservate in Inventory Store | R2-029 | le informazioni sulla disponibilità sono conservate nell'Inventory Store |
| R3-030 | R | Richiesta contiene identificativo cliente | R2-030 | la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste |
| R3-031 | R | Richiesta contiene prodotti selezionati | R2-031 | la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste |
| R3-032 | R | Richiesta contiene quantità richieste | R2-032 | la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste |
| R3-033 | R | Payment Provider è esterno | R2-033 | un Payment Provider esterno |
| R3-034 | R | Organizzazione esterna gestisce Payment Provider | R2-034 | Il Payment Provider è gestito da un'organizzazione esterna. |
| R3-035 | R | Piattaforma usa servizio del Payment Provider | R2-035 | La piattaforma utilizza il suo servizio |
| R3-036 | N | Piattaforma NON gestisce infrastruttura del Payment Provider | R2-036 | ma non ne gestisce l'infrastruttura. |
| R3-037 | A | Cliente conferma un acquisto | R2-037 | Quando un cliente conferma un acquisto |
| R3-038 | A | Order Service riceve richiesta | R2-038 | Quando un cliente conferma un acquisto, l'Order Service riceve la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste. |
| R3-039 | A | Order Service verifica disponibilità | R2-039 | L'Order Service verifica la disponibilità interrogando l'Inventory Service |
| R3-040 | A | Order Service interroga Inventory Service | R2-040 | interrogando l'Inventory Service |
| R3-041 | A | Inventory Service consulta Inventory Store | R2-041 | che consulta l'Inventory Store |
| R3-042 | A | Inventory Service restituisce quantità disponibili | R2-042 | restituisce le quantità disponibili |
| R3-043 | A | Order Service crea un ordine | R2-043 | Se tutti i prodotti richiesti sono disponibili, l'Order Service crea un ordine |
| R3-044 | A | Order Service registra ordine in Order Store | R2-044 | Se tutti i prodotti richiesti sono disponibili, l'Order Service crea un ordine e lo registra nell'Order Store. |
| R3-045 | A | Order Service richiede autorizzazione a Payment Service | R2-045 | Successivamente richiede al Payment Service l'autorizzazione del pagamento. |
| R3-046 | A | Payment Service comunica con Payment Provider | R2-046 | Il Payment Service comunica con un Payment Provider esterno |
| R3-047 | A | Payment Service restituisce esito autorizzazione | R2-047 | restituisce l'esito dell'autorizzazione |
| R3-048 | A | Order Service richiede riserva a Inventory Service | R2-048 | Quando il pagamento viene autorizzato, l'Order Service richiede all'Inventory Service di riservare le quantità ordinate. |
| R3-049 | A | Ordine assume stato Confirmed | R2-049 | Dopo la conferma della riserva, l'ordine assume lo stato Confirmed |
| R3-050 | A | Notifica inviata al cliente tramite Notification Service | R2-050 | Dopo la conferma della riserva, l'ordine assume lo stato Confirmed e viene inviata una notifica al cliente tramite il Notification Service. |
| R3-051 | A | Ordine contrassegnato come Rejected | R2-051 | Se il pagamento non viene autorizzato, l'ordine viene contrassegnato come Rejected. |
| R3-052 | A | Richiesta rifiutata | R2-052 | Se la disponibilità è insufficiente, la richiesta viene rifiutata prima di contattare il Payment Service. |
| R3-053 | U | Protocollo di comunicazione non specificato | R2-053 | La documentazione non specifica il protocollo di comunicazione utilizzato |
| R3-054 | U | Meccanismo di annullamento autorizzazioni non specificato | R2-054 | né il meccanismo di annullamento delle autorizzazioni di pagamento. |
| R3-055 | U | Soggetto mittente della notifica non identificato | R2-055 | viene inviata una notifica al cliente tramite il Notification Service |
| R3-056 | U | Esecuzione della riserva non direttamente descritta | R2-056 | richiede all'Inventory Service di riservare le quantità ordinate |
| R3-057 | A | Piattaforma permette ai clienti di acquistare prodotti | R2-057 | Una piattaforma di commercio elettronico permette ai clienti di acquistare prodotti disponibili nel catalogo. |
| R3-058 | R | Prodotti disponibili nel catalogo | R2-058 | prodotti disponibili nel catalogo |
| R3-059 | O | Identificativo del cliente (menzione) | R2-059 | l'identificativo del cliente |
| R3-060 | O | Prodotti selezionati (menzione) | R2-060 | i prodotti selezionati |
| R3-061 | O | Quantità richieste (menzione) | R2-061 | le quantità richieste |
| R3-062 | T | Conferma della riserva menzionata come antecedente | R2-062 | Dopo la conferma della riserva |
| R3-063 | O | Acquisto (menzione) | R2-063 | un acquisto |
| R3-064 | O | Disponibilità verificata (menzione; identità rispetto a informazioni conservate non risolta) | R2-064 | verifica la disponibilità |

## Fonte originale ONT-T01 (letterale)

Una piattaforma di commercio elettronico permette ai clienti di acquistare prodotti disponibili nel catalogo. Ogni prodotto possiede un identificativo, una descrizione e un prezzo. Il catalogo viene mantenuto dal Catalog Service, mentre le informazioni sulla disponibilità sono conservate nell'Inventory Store.

Quando un cliente conferma un acquisto, l'Order Service riceve la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste. L'Order Service verifica la disponibilità interrogando l'Inventory Service, che consulta l'Inventory Store e restituisce le quantità disponibili.

Se tutti i prodotti richiesti sono disponibili, l'Order Service crea un ordine e lo registra nell'Order Store. Successivamente richiede al Payment Service l'autorizzazione del pagamento. Il Payment Service comunica con un Payment Provider esterno e restituisce l'esito dell'autorizzazione.

Quando il pagamento viene autorizzato, l'Order Service richiede all'Inventory Service di riservare le quantità ordinate. Dopo la conferma della riserva, l'ordine assume lo stato Confirmed e viene inviata una notifica al cliente tramite il Notification Service.

Se il pagamento non viene autorizzato, l'ordine viene contrassegnato come Rejected. Se la disponibilità è insufficiente, la richiesta viene rifiutata prima di contattare il Payment Service.

Il Payment Provider è gestito da un'organizzazione esterna. La piattaforma utilizza il suo servizio, ma non ne gestisce l'infrastruttura. La documentazione non specifica il protocollo di comunicazione utilizzato né il meccanismo di annullamento delle autorizzazioni di pagamento.
