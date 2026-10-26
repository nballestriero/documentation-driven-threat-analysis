# ONT-T01 — Gold standard di riferimento R1 (candidato a review)

**Stato:** DRAFT / REVIEW CANDIDATE. **Baseline:** `85c8e39`. **Scopo:** valutazione indipendente degli output O/R/A V1; non è una nuova autorità BA.

## 1. Protocollo di annotazione

- Unità primaria: **fatto semanticamente confrontabile**, non numero di record JSON. Relazioni aggregate o suddivise sono ammissibili se preservano tutti i fatti.
- `O` = referenti/contenuti espliciti, `R` = associazioni/stati di fatto, `A` = comportamenti descritti, `N` = negazione esplicita, `U` = lacune/limiti informativi. `N` e `U` sono etichette valutative trasversali alla tripartizione O/R/A, non nuove famiglie ontologiche.
- Le azioni condizionali descrivono comportamenti **previsti dal documento**, non eventi realmente accaduti; un futuro modello deve conservarne la guardia.
- Identificatori e nomi nella colonna partecipanti sono **ancore di confronto**, non BAReferent o BAProposition approvati. Le categorie O/R/A non equivalgono a una tassonomia `is-a`.
- Una citazione è valida se è una sottostringa letterale del testo originale; una prova che richiede più segmenti va suddivisa in più righe, mai fabbricata con ` / `.
- I campi non menzionati non si presumono né positivi né negativi; assenza di un mittente indicato ≠ mittente inesistente.
- Questo standard nasce dal testo, senza copiare o fondere le classificazioni dei quattro modelli. Richiede review umana prima di essere usato per punteggi definitivi.

## 2. Fatti atomici da verificare

| ID | Classe | Fatto di riferimento | Qualifica | Evidenza letterale |
|---|---|---|---|---|
| GS-001 | O | Piattaforma di commercio elettronico | — | Una piattaforma di commercio elettronico |
| GS-002 | O | Cliente/i | — | ai clienti |
| GS-003 | O | Prodotto/i | — | Ogni prodotto possiede |
| GS-004 | O | Catalogo | — | nel catalogo |
| GS-005 | O | Catalog Service | — | Catalog Service |
| GS-006 | O | Informazioni sulla disponibilità | — | informazioni sulla disponibilità |
| GS-007 | O | Inventory Store | — | Inventory Store |
| GS-008 | O | Order Service | — | Order Service |
| GS-009 | O | Richiesta di acquisto (denominazione normalizzata candidata) | Rinominazione: nel testo è «la richiesta» | la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste |
| GS-010 | O | Inventory Service | — | Inventory Service |
| GS-011 | O | Quantità disponibili | — | quantità disponibili |
| GS-012 | O | Ordine | — | crea un ordine |
| GS-013 | O | Order Store | — | Order Store |
| GS-014 | O | Payment Service | — | Payment Service |
| GS-015 | O | Autorizzazione del pagamento | — | l'autorizzazione del pagamento |
| GS-016 | O | Payment Provider esterno | — | Payment Provider esterno |
| GS-017 | O | Esito autorizzazione | — | l'esito dell'autorizzazione |
| GS-018 | O | Quantità ordinate | Equivalenza con QuantitaRichieste non dichiarata | quantità ordinate |
| GS-019 | O | Stato Confirmed | — | stato Confirmed |
| GS-020 | O | Notifica al cliente | — | una notifica al cliente |
| GS-021 | O | Notification Service | — | Notification Service |
| GS-022 | O | Stato Rejected | — | come Rejected |
| GS-023 | O | Organizzazione esterna | — | un'organizzazione esterna |
| GS-024 | O | Infrastruttura del Payment Provider | Il referente del pronome «ne» è contestuale | l'infrastruttura |
| GS-025 | R | Prodotto possiede identificativo, descrizione e prezzo | — | Ogni prodotto possiede un identificativo, una descrizione e un prezzo. |
| GS-026 | R | Catalog Service mantiene catalogo | — | Il catalogo viene mantenuto dal Catalog Service |
| GS-027 | R | Informazioni disponibilità conservate in Inventory Store | — | le informazioni sulla disponibilità sono conservate nell'Inventory Store |
| GS-028 | R | La richiesta contiene identificativo cliente, prodotti selezionati e quantità richieste | — | la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste |
| GS-029 | R | Payment Provider è esterno | — | un Payment Provider esterno |
| GS-030 | R | Organizzazione esterna gestisce Payment Provider | — | Il Payment Provider è gestito da un'organizzazione esterna. |
| GS-031 | R | Piattaforma usa servizio del Payment Provider | — | La piattaforma utilizza il suo servizio |
| GS-032 | N | Piattaforma NON gestisce infrastruttura del Payment Provider | NEGATIVA | ma non ne gestisce l'infrastruttura. |
| GS-033 | A | Cliente conferma un acquisto | TRIGGER | Quando un cliente conferma un acquisto |
| GS-034 | A | Order Service riceve richiesta | TRIGGER: conferma acquisto | l'Order Service riceve la richiesta contenente |
| GS-035 | A | Order Service verifica disponibilità | — | L'Order Service verifica la disponibilità interrogando l'Inventory Service |
| GS-036 | A | Order Service interroga Inventory Service | — | interrogando l'Inventory Service |
| GS-037 | A | Inventory Service consulta Inventory Store | — | che consulta l'Inventory Store |
| GS-038 | A | Inventory Service restituisce quantità disponibili | — | restituisce le quantità disponibili |
| GS-039 | A | Order Service crea un ordine | SE: tutti disponibili | Se tutti i prodotti richiesti sono disponibili, l'Order Service crea un ordine |
| GS-040 | A | Order Service registra ordine in Order Store | SE: tutti disponibili | e lo registra nell'Order Store |
| GS-041 | A | Order Service richiede autorizzazione a Payment Service | DOPO: registrazione ordine | richiede al Payment Service l'autorizzazione del pagamento |
| GS-042 | A | Payment Service comunica con Payment Provider | — | Il Payment Service comunica con un Payment Provider esterno |
| GS-043 | A | Payment Service restituisce esito autorizzazione | — | restituisce l'esito dell'autorizzazione |
| GS-044 | A | Order Service richiede riserva a Inventory Service | QUANDO: pagamento autorizzato | l'Order Service richiede all'Inventory Service di riservare le quantità ordinate |
| GS-045 | A | Ordine assume stato Confirmed | DOPO: conferma riserva | l'ordine assume lo stato Confirmed |
| GS-046 | A | Notifica inviata al cliente tramite Notification Service | DOPO: conferma riserva | viene inviata una notifica al cliente tramite il Notification Service |
| GS-047 | A | Ordine contrassegnato come Rejected | SE: pagamento NON autorizzato | l'ordine viene contrassegnato come Rejected |
| GS-048 | A | Richiesta rifiutata | SE: disponibilità insufficiente; PRIMA: contatto Payment Service | la richiesta viene rifiutata prima di contattare il Payment Service |
| GS-049 | U | Protocollo di comunicazione non specificato | NON SPECIFICATO | La documentazione non specifica il protocollo di comunicazione utilizzato |
| GS-050 | U | Meccanismo di annullamento autorizzazioni non specificato | NON SPECIFICATO | né il meccanismo di annullamento delle autorizzazioni di pagamento. |
| GS-051 | U | Soggetto mittente della notifica non identificato | NON IDENTIFICATO | viene inviata una notifica al cliente tramite il Notification Service |
| GS-052 | U | Esecuzione della riserva non direttamente descritta | NON CONCLUDERE esecuzione incondizionata | richiede all'Inventory Service di riservare le quantità ordinate |

## 3. Regole di confronto con gli output LLM

1. Confrontare per significato, indipendentemente dalla numerazione `O-###`, `R-###` o `A-###` e dalla granularità delle relazioni.
2. Marcatura per ogni fatto: `MATCH`, `PARTIAL`, `MISSING`, `UNSUPPORTED`, `CONTRADICTED`; `PARTIAL` richiede motivazione e componente informativa mancante.
3. Valutare separatamente: partecipanti, qualifiche/condizioni, negazione, continuità delle identità, evidenza letterale, lacune non inventate.
4. Un testo che afferma *se/quando X, allora Y* non autorizza una segnalazione di Y come evento verificatosi incondizionatamente.
5. Le proposte di protocolli, rollback, mittenti o esecutori non documentati sono `UNSUPPORTED` se presentati come fatti; possibili interpretazioni esplicitamente ipotetiche vanno comunque separate dalle evidenze del testo.
6. Per le righe `U`, considerare soddisfatto il controllo se l'output conserva correttamente l'incertezza, anche se non crea un oggetto specifico.
7. Non sommare indistintamente le righe `O`, `R`, `A`, `N`, `U`: i conteggi e l'interdipendenza differiscono. Pubblicare risultati separati, e soltanto dopo review del gold standard.

## 4. Questioni di review prima dell'accettazione

- Stabilire il livello di granularità per dati-attributo: identificativo/prezzo/descrizione e singoli campi della richiesta sono registrati in una riga aggregata, ma potrebbero diventare fatti atomici distinti.
- Verificare se `Richiesta di acquisto` sia una normalizzazione troppo forte del termine «richiesta».
- Determinare se la frase sul Payment Provider consenta di distinguere l'identità del provider da quella del servizio offerto; non imporre il merge.
- Per la conferma della riserva, distinguere il risultato menzionato dalla procedura, dall'attore e dall'evento effettivo.
- Non interpretare `Confirmed` e `Rejected` come occorrenze simultanee: sono alternative sotto condizioni diverse.
- L'inventario di omissioni non è necessariamente esaustivo: un protocollo non specificato non va trattato come oggetto presente.

## 5. Fonte del caso (testo esatto)

Una piattaforma di commercio elettronico permette ai clienti di acquistare prodotti disponibili nel catalogo. Ogni prodotto possiede un identificativo, una descrizione e un prezzo. Il catalogo viene mantenuto dal Catalog Service, mentre le informazioni sulla disponibilità sono conservate nell'Inventory Store.

Quando un cliente conferma un acquisto, l'Order Service riceve la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste. L'Order Service verifica la disponibilità interrogando l'Inventory Service, che consulta l'Inventory Store e restituisce le quantità disponibili.

Se tutti i prodotti richiesti sono disponibili, l'Order Service crea un ordine e lo registra nell'Order Store. Successivamente richiede al Payment Service l'autorizzazione del pagamento. Il Payment Service comunica con un Payment Provider esterno e restituisce l'esito dell'autorizzazione.

Quando il pagamento viene autorizzato, l'Order Service richiede all'Inventory Service di riservare le quantità ordinate. Dopo la conferma della riserva, l'ordine assume lo stato Confirmed e viene inviata una notifica al cliente tramite il Notification Service.

Se il pagamento non viene autorizzato, l'ordine viene contrassegnato come Rejected. Se la disponibilità è insufficiente, la richiesta viene rifiutata prima di contattare il Payment Service.

Il Payment Provider è gestito da un'organizzazione esterna. La piattaforma utilizza il suo servizio, ma non ne gestisce l'infrastruttura. La documentazione non specifica il protocollo di comunicazione utilizzato né il meccanismo di annullamento delle autorizzazioni di pagamento.
