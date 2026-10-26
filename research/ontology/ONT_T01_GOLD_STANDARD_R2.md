# ONT-T01 — Gold Standard R2 (REVIEW CANDIDATE)

**Origine:** Gold Standard R1; Review A Qwen, DeepSeek, Gemini, Mistral; 19 issue consolidate.
**Stato:** candidato per revisione, NON accettato / NON normativo.
**Baseline repository dichiarata dall’utente:** `0ceedcd` (master).

## Contratto del riferimento

1. Il testo ONT-T01 riportato sotto è unica fonte dei fatti sul caso; le Review A sono proposte critiche, non autorità.
2. Le unità di valutazione atomiche non impongono oggetti JSON distinti o BAReferent autonomi. Confrontare significato, partecipanti, modalità, condizione e polarità.
3. `O`, `R`, `A` sono dimensioni di estrazione; `N`, `U`, `T` etichette valutative trasversali. `T` segnala menzione/relazione temporale, non ontologia nuova.
4. Un evento descritto sotto `se`/`quando` non è un evento effettivamente osservato. Richiesta di riserva ≠ prova di esecuzione.
5. Non confondere entità e proprietà: disponibilità verificata vs informazioni sulla disponibilità conservate; quantità ordinate vs richieste; fornitore vs servizio. Conservare incertezza.
6. I fatti GS-025 e GS-028 di R1 sono scomposti in tre unità ciascuno ai fini del matching. LLM con una sola relazione n-aria può coprire tutte e tre.
7. `N` conserva la negazione esplicita, `U` conserva una lacuna esplicita o incertezza locale; non premiare illimitatamente i ruoli assenti.
8. `MATCH`, `PARTIAL`, `MISSING` sono giudizi per unità gold; `UNSUPPORTED` e `CONTRADICTED` sono verifiche anche sulle affermazioni extra del modello.
9. Il CSV R2 è registro operativo; il Markdown documenta lo stesso elenco, protocollo, questioni e fonte. La mappatura R1→R2 è nel CSV di trace.
10. Tutte le evidenze devono essere sottostringhe letterali e contigue della fonte; supporti molteplici richiedono evidenze separate.

## 64 unità valutabili

| ID | Dim. | Fatto | R1 | Issue | Evidenza |
|---|---|---|---|---|---|
| R2-001 | O | Piattaforma di commercio elettronico | GS-001 | — | Una piattaforma di commercio elettronico |
| R2-002 | O | Cliente/i | GS-002 | — | ai clienti |
| R2-003 | O | Prodotto/i | GS-003 | — | Ogni prodotto possiede |
| R2-004 | O | Catalogo | GS-004 | — | nel catalogo |
| R2-005 | O | Catalog Service | GS-005 | — | Catalog Service |
| R2-006 | O | Informazioni sulla disponibilità | GS-006 | — | informazioni sulla disponibilità |
| R2-007 | O | Inventory Store | GS-007 | — | Inventory Store |
| R2-008 | O | Order Service | GS-008 | — | Order Service |
| R2-009 | O | Richiesta | GS-009 | C-09 | la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste |
| R2-010 | O | Inventory Service | GS-010 | — | Inventory Service |
| R2-011 | O | Quantità disponibili | GS-011 | — | quantità disponibili |
| R2-012 | O | Ordine | GS-012 | — | crea un ordine |
| R2-013 | O | Order Store | GS-013 | — | Order Store |
| R2-014 | O | Payment Service | GS-014 | — | Payment Service |
| R2-015 | O | Autorizzazione del pagamento | GS-015 | — | l'autorizzazione del pagamento |
| R2-016 | O | Payment Provider | GS-016 | C-12 | Payment Provider esterno |
| R2-017 | O | Esito autorizzazione | GS-017 | — | l'esito dell'autorizzazione |
| R2-018 | O | Quantità ordinate | GS-018 | C-10 | quantità ordinate |
| R2-019 | O | Stato Confirmed | GS-019 | — | stato Confirmed |
| R2-020 | O | Notifica al cliente | GS-020 | — | una notifica al cliente |
| R2-021 | O | Notification Service | GS-021 | — | Notification Service |
| R2-022 | O | Stato Rejected | GS-022 | — | come Rejected |
| R2-023 | O | Organizzazione esterna | GS-023 | — | un'organizzazione esterna |
| R2-024 | O | Infrastruttura associata al servizio del Payment Provider | GS-024 | C-11;C-19 | La piattaforma utilizza il suo servizio, ma non ne gestisce l'infrastruttura. |
| R2-025 | R | Prodotto possiede identificativo | GS-025 | C-04 | Ogni prodotto possiede un identificativo, una descrizione e un prezzo. |
| R2-026 | R | Prodotto possiede descrizione | GS-025 | C-04 | Ogni prodotto possiede un identificativo, una descrizione e un prezzo. |
| R2-027 | R | Prodotto possiede prezzo | GS-025 | C-04 | Ogni prodotto possiede un identificativo, una descrizione e un prezzo. |
| R2-028 | R | Catalog Service mantiene catalogo | GS-026 | — | Il catalogo viene mantenuto dal Catalog Service |
| R2-029 | R | Informazioni disponibilità conservate in Inventory Store | GS-027 | — | le informazioni sulla disponibilità sono conservate nell'Inventory Store |
| R2-030 | R | Richiesta contiene identificativo cliente | GS-028 | C-03;C-05 | la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste |
| R2-031 | R | Richiesta contiene prodotti selezionati | GS-028 | C-03;C-05 | la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste |
| R2-032 | R | Richiesta contiene quantità richieste | GS-028 | C-03;C-05 | la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste |
| R2-033 | R | Payment Provider è esterno | GS-029 | — | un Payment Provider esterno |
| R2-034 | R | Organizzazione esterna gestisce Payment Provider | GS-030 | — | Il Payment Provider è gestito da un'organizzazione esterna. |
| R2-035 | R | Piattaforma usa servizio del Payment Provider | GS-031 | — | La piattaforma utilizza il suo servizio |
| R2-036 | N | Piattaforma NON gestisce infrastruttura del Payment Provider | GS-032 | C-11;C-12;C-15 | ma non ne gestisce l'infrastruttura. |
| R2-037 | A | Cliente conferma un acquisto | GS-033 | — | Quando un cliente conferma un acquisto |
| R2-038 | A | Order Service riceve richiesta | GS-034 | — | l'Order Service riceve la richiesta contenente |
| R2-039 | A | Order Service verifica disponibilità | GS-035 | C-08 | L'Order Service verifica la disponibilità interrogando l'Inventory Service |
| R2-040 | A | Order Service interroga Inventory Service | GS-036 | — | interrogando l'Inventory Service |
| R2-041 | A | Inventory Service consulta Inventory Store | GS-037 | — | che consulta l'Inventory Store |
| R2-042 | A | Inventory Service restituisce quantità disponibili | GS-038 | — | restituisce le quantità disponibili |
| R2-043 | A | Order Service crea un ordine | GS-039 | — | Se tutti i prodotti richiesti sono disponibili, l'Order Service crea un ordine |
| R2-044 | A | Order Service registra ordine in Order Store | GS-040 | C-13 | Se tutti i prodotti richiesti sono disponibili, l'Order Service crea un ordine e lo registra nell'Order Store. |
| R2-045 | A | Order Service richiede autorizzazione a Payment Service | GS-041 | C-13 | Successivamente richiede al Payment Service l'autorizzazione del pagamento. |
| R2-046 | A | Payment Service comunica con Payment Provider | GS-042 | — | Il Payment Service comunica con un Payment Provider esterno |
| R2-047 | A | Payment Service restituisce esito autorizzazione | GS-043 | — | restituisce l'esito dell'autorizzazione |
| R2-048 | A | Order Service richiede riserva a Inventory Service | GS-044 | — | l'Order Service richiede all'Inventory Service di riservare le quantità ordinate |
| R2-049 | A | Ordine assume stato Confirmed | GS-045 | C-06;C-13 | Dopo la conferma della riserva, l'ordine assume lo stato Confirmed |
| R2-050 | A | Notifica inviata al cliente tramite Notification Service | GS-046 | C-06;C-13 | Dopo la conferma della riserva, l'ordine assume lo stato Confirmed e viene inviata una notifica al cliente tramite il Notification Service. |
| R2-051 | A | Ordine contrassegnato come Rejected | GS-047 | — | l'ordine viene contrassegnato come Rejected |
| R2-052 | A | Richiesta rifiutata | GS-048 | C-17 | la richiesta viene rifiutata prima di contattare il Payment Service |
| R2-053 | U | Protocollo di comunicazione non specificato | GS-049 | — | La documentazione non specifica il protocollo di comunicazione utilizzato |
| R2-054 | U | Meccanismo di annullamento autorizzazioni non specificato | GS-050 | — | né il meccanismo di annullamento delle autorizzazioni di pagamento. |
| R2-055 | U | Soggetto mittente della notifica non identificato | GS-051 | — | viene inviata una notifica al cliente tramite il Notification Service |
| R2-056 | U | Esecuzione della riserva non direttamente descritta | GS-052 | C-06;C-16 | richiede all'Inventory Service di riservare le quantità ordinate |
| R2-057 | A | Piattaforma permette ai clienti di acquistare prodotti | NEW | C-01 | Una piattaforma di commercio elettronico permette ai clienti di acquistare prodotti disponibili nel catalogo. |
| R2-058 | R | Prodotti disponibili nel catalogo | NEW | C-02 | prodotti disponibili nel catalogo |
| R2-059 | O | Identificativo del cliente (menzione) | NEW | C-03;C-05 | l'identificativo del cliente |
| R2-060 | O | Prodotti selezionati (menzione) | NEW | C-03;C-05 | i prodotti selezionati |
| R2-061 | O | Quantità richieste (menzione) | NEW | C-03;C-05 | le quantità richieste |
| R2-062 | T | Conferma della riserva menzionata come antecedente | NEW | C-06;C-16 | Dopo la conferma della riserva |
| R2-063 | O | Acquisto (menzione) | NEW | C-14 | un acquisto |
| R2-064 | O | Disponibilità (menzione distinta da informazione conservata) | NEW | C-08 | verifica la disponibilità |

## Decisioni candidate e controlli aperti

- C-03/04/05: unità atomiche valutabili anche se JSON aggregato; menzioni dei campi NON richiedono BAReferent autonomi.
- C-07/C-15: lacune esplicite diverse da ruoli omessi, ambiguità d’identità diverse da inferenze non supportate. Per GS-051 resta un controllo mirato, non un precedente per moltiplicare le U.
- C-06/08/16: conferma della riserva è menzionata, non sono documentati attore o procedura; disponibilità e informazioni sulla disponibilità senza identità forzata.
- C-01/02/09/10/11/12/14/17/18/19: capacità, disponibilità in catalogo, alias, polarità, esternità, infrastruttura, temporalità e ruoli sono preservati nelle unità e nelle note.
- Review aperta: valutare se `Acquisto`/`Disponibilità` e le tre menzioni della richiesta vadano computati come dimensione O oppure in una metrica distinta di copertura lessicale.
- Review aperta: GS-041 è successivo alla registrazione; GS-040 mantiene la guardia di disponibilità; l’ordine di invio notifica rispetto al cambio di stato Confirmed non è imposto oltre al comune antecedente documentato.
- NON applicare automaticamente le etichette BA2 o classificazioni OWL/`is-a`.

## Fonte originale ONT-T01 (letterale)

Una piattaforma di commercio elettronico permette ai clienti di acquistare prodotti disponibili nel catalogo. Ogni prodotto possiede un identificativo, una descrizione e un prezzo. Il catalogo viene mantenuto dal Catalog Service, mentre le informazioni sulla disponibilità sono conservate nell'Inventory Store.

Quando un cliente conferma un acquisto, l'Order Service riceve la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste. L'Order Service verifica la disponibilità interrogando l'Inventory Service, che consulta l'Inventory Store e restituisce le quantità disponibili.

Se tutti i prodotti richiesti sono disponibili, l'Order Service crea un ordine e lo registra nell'Order Store. Successivamente richiede al Payment Service l'autorizzazione del pagamento. Il Payment Service comunica con un Payment Provider esterno e restituisce l'esito dell'autorizzazione.

Quando il pagamento viene autorizzato, l'Order Service richiede all'Inventory Service di riservare le quantità ordinate. Dopo la conferma della riserva, l'ordine assume lo stato Confirmed e viene inviata una notifica al cliente tramite il Notification Service.

Se il pagamento non viene autorizzato, l'ordine viene contrassegnato come Rejected. Se la disponibilità è insufficiente, la richiesta viene rifiutata prima di contattare il Payment Service.

Il Payment Provider è gestito da un'organizzazione esterna. La piattaforma utilizza il suo servizio, ma non ne gestisce l'infrastruttura. La documentazione non specifica il protocollo di comunicazione utilizzato né il meccanismo di annullamento delle autorizzazioni di pagamento.
