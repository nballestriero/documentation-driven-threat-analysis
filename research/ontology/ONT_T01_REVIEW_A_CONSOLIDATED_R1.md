# ONT-T01 — Registro consolidato Review A R1

**Stato:** REVIEW CANDIDATE — nessuna proposta approvata; nessuna modifica ai file Gold Standard R1.  
**Fonte di verità:** testo ONT-T01 in `ONT_T01_GOLD_STANDARD_R1.md`, §5.  
**Revisori:** Qwen (11 finding), DeepSeek (5), Gemini (4), Mistral (10); **30 segnalazioni originali**.  
**Output:** 19 questioni consolidate, NON 19 errori accertati.

## 1. Regole di consolidamento

- I report originali Qwen, DeepSeek e Mistral sono allegati verbatim in `research/ontology/reviews/`. La Review Gemini è stata fornita nel messaggio della conversazione e non si riproduce come falso file verbatim.
- I prefissi `Q:`, `D:`, `G:`, `M:` identificano unicamente il modello; i finding conservano gli ID **originali** di ciascun revisore. `§` identifica osservazioni nelle sezioni non numerate come finding.
- `ACCEPT_CANDIDATE` indica una proposta supportata preliminarmente ma **non approvata**; `NEEDS_REVIEW` richiede decisione; `PARTIAL_ACCEPT` accetta solo parte del rilievo; `OPTIONAL` segnala miglioramento editoriale. Non usare questi stati come verdetti finali.
- Un conteggio/consenso fra modelli non è prova della correttezza di un fatto. Confronto per significato, non per forma o numerazione degli output.
- `N` e `U` nel gold R1 sono tag trasversali di valutazione, non famiglie ontologiche addizionali. Una U non significa necessariamente che il documento dichiari espressamente "non specificato".
- Il trattamento di `UNSUPPORTED` e `CONTRADICTED` resta distinto: mancanza di supporto non equivale a contraddizione.
- Le evidenze nella matrice sintetica sono **ancore leggibili**, non necessariamente citazioni complete autonome: verificare contro il documento fonte e le singole review prima delle modifiche.

## 2. Matrice consolidata

| Issue | Questione | Provenienza | Gold R1 | Disposizione preliminare |
|---|---|---|---|---|
| C-01 | Capacità di acquisto della piattaforma | Q:F-011, D:F-01, M:F-01 | NEW;GS-001..004 | `ACCEPT_CANDIDATE` |
| C-02 | Prodotti disponibili nel catalogo | Q:F-004, D:F-01, M:F-02 | NEW;GS-003..004 | `ACCEPT_CANDIDATE` |
| C-03 | Campi della richiesta non autonomamente referenziati | Q:F-001, Q:F-002, Q:F-003, G:F-04, M:F-04 | GS-009;GS-028;GS-018 | `NEEDS_REVIEW` |
| C-04 | Attributi del prodotto: granularità | Q:F-006, G:F-01, D:§3.1, M:§3.1 | GS-025 | `ACCEPT_CANDIDATE` |
| C-05 | Campi della richiesta: granularità della relazione | Q:F-007, G:F-04, D:§3.2, M:§3.2 | GS-028 | `ACCEPT_CANDIDATE` |
| C-06 | Conferma della riserva menzionata | Q:F-005, D:F-05, M:F-07 | NEW;GS-045;GS-046;GS-052 | `ACCEPT_CANDIDATE` |
| C-07 | Lacune e ruoli non identificati: trattamento disomogeneo | D:F-04, G:F-03, M:F-06,F-08 | GS-034;GS-038;GS-043;GS-045..048;GS-051 | `NEEDS_REVIEW` |
| C-08 | Disponibilità verificata vs informazione conservata | M:F-05 | GS-006;GS-035 | `ACCEPT_CANDIDATE` |
| C-09 | Normalizzazione Richiesta di acquisto | Q:F-008, M:F-10 | GS-009 | `ACCEPT_CANDIDATE` |
| C-10 | Quantità ordinate vs quantità richieste | Q:F-010, M:F-04, D:§3.3 | GS-018;GS-028 | `ACCEPT_CANDIDATE` |
| C-11 | Ambiguità referenziale di ne / infrastruttura | D:F-02, Q:F-009 | GS-024;GS-032 | `NEEDS_REVIEW` |
| C-12 | Esternità Payment Provider doppio conteggio | D:F-03, M:§3.5 | GS-016;GS-029 | `ACCEPT_CANDIDATE` |
| C-13 | Evidenze incomplete delle condizioni temporali | M:F-09 | GS-040;GS-041;GS-045;GS-046 | `ACCEPT_CANDIDATE` |
| C-14 | Ancore senza corrispettiva O (Acquisto, servizio provider) | M:F-03, D:§3.5,§4, M:§3.3 | GS-031;GS-033 | `NEEDS_REVIEW` |
| C-15 | Classificazione negativa GS-032 e GS-051 | G:F-02, G:F-03, D:F-04 | GS-032;GS-051 | `PARTIAL_ACCEPT` |
| C-16 | Differenza tra richiesta di riserva ed esecuzione | D:§3.6, M:§3.6, Q:§3.4 | GS-044;GS-052 | `ACCEPT_CANDIDATE` |
| C-17 | Ordine temporale prima del contatto Payment Service | D:§3.7 | GS-048 | `ACCEPT_CANDIDATE` |
| C-18 | Coerenza Markdown/CSV e autorità delle note | D:§4, M:F-08,§4, Q:§4, G:§4 | GS-001..052 | `NEEDS_REVIEW` |
| C-19 | Citazione tronca GS-024 | Q:F-009, D:F-02 | GS-024 | `OPTIONAL` |

## 3. Schede di decisione (una per questione)

### C-01 — Capacità di acquisto della piattaforma
- **Finding / sezioni:** Q:F-011;D:F-01;M:F-01.
- **Gold R1:** NEW;GS-001..004.
- **Ancora testuale/controllo:** «permette ai clienti di acquistare prodotti».
- **Proposta:** Aggiungere fatto di capacità/abilitazione, NON evento di acquisto verificato.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** Tre revisori convergono; capacità esplicita, categoria A/R finale da revisionare.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-02 — Prodotti disponibili nel catalogo
- **Finding / sezioni:** Q:F-004;D:F-01;M:F-02.
- **Gold R1:** NEW;GS-003..004.
- **Ancora testuale/controllo:** «prodotti disponibili nel catalogo».
- **Proposta:** Aggiungere fatto distinguibile di disponibilità-in-catalogo; non dedurre appartenenza fisica.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** Testo esplicito; non trasformare disponibilità nel catalogo in composizione o stock.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-03 — Campi della richiesta non autonomamente referenziati
- **Finding / sezioni:** Q:F-001;Q:F-002;Q:F-003;G:F-04;M:F-04.
- **Gold R1:** GS-009;GS-028;GS-018.
- **Ancora testuale/controllo:** «l’identificativo del cliente, i prodotti selezionati e le quantità richieste».
- **Proposta:** Definire tre unità valutabili indipendentemente; scelta fra O autonomi e attributi strutturati da review.
- **Disposizione preliminare:** `NEEDS_REVIEW`. **Motivo:** Il gold copre già i contenuti in GS-028: lacuna di atomizzazione e ancoraggio, non omissione totale.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-04 — Attributi del prodotto: granularità
- **Finding / sezioni:** Q:F-006;G:F-01;D:§3.1;M:§3.1.
- **Gold R1:** GS-025.
- **Ancora testuale/controllo:** «Ogni prodotto possiede un identificativo, una descrizione e un prezzo.».
- **Proposta:** Tre sottounità valutabili, mantenendo matching di relazioni aggregate n-arie.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** Convergenza dei quattro, ma due lo discutono in sezione modellistica, non finding.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-05 — Campi della richiesta: granularità della relazione
- **Finding / sezioni:** Q:F-007;G:F-04;D:§3.2;M:§3.2.
- **Gold R1:** GS-028.
- **Ancora testuale/controllo:** «la richiesta contenente l’identificativo del cliente, i prodotti selezionati e le quantità richieste».
- **Proposta:** Matching su tre contenuti distinti, ammettendo n-aria e relazioni binarie.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** Non imporre una forma JSON; collegato a C-03.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-06 — Conferma della riserva menzionata
- **Finding / sezioni:** Q:F-005;D:F-05;M:F-07.
- **Gold R1:** NEW;GS-045;GS-046;GS-052.
- **Ancora testuale/controllo:** «Dopo la conferma della riserva».
- **Proposta:** Registrare conferma come ancoraggio condizionale distinto, senza inventarne attore/esecuzione.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** Sì a fatto documentato; O/A/U sono alternative, richiedono policy.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-07 — Lacune e ruoli non identificati: trattamento disomogeneo
- **Finding / sezioni:** D:F-04;G:F-03;M:F-06,F-08.
- **Gold R1:** GS-034;GS-038;GS-043;GS-045..048;GS-051.
- **Ancora testuale/controllo:** «viene inviata una notifica al cliente tramite il Notification Service».
- **Proposta:** Definire soglia di materialità e tipi U: dichiarato non specificato vs ruolo non determinabile; usare note o righe U coerentemente.
- **Disposizione preliminare:** `NEEDS_REVIEW`. **Motivo:** Non creare una U per ogni possibile ruolo: proliferazione illimitata.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-08 — Disponibilità verificata vs informazione conservata
- **Finding / sezioni:** M:F-05.
- **Gold R1:** GS-006;GS-035.
- **Ancora testuale/controllo:** «L’Order Service verifica la disponibilità interrogando l’Inventory Service».
- **Proposta:** Non presupporre identità; annotare matching condizionale / ancore distinte.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** Identità non attestata come equivalenza; distinguere dato rappresentativo dal referente.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-09 — Normalizzazione Richiesta di acquisto
- **Finding / sezioni:** Q:F-008;M:F-10.
- **Gold R1:** GS-009.
- **Ancora testuale/controllo:** «la richiesta contenente l’identificativo del cliente».
- **Proposta:** Ancorare a Richiesta e tollerare alias contestuale; non imporre di acquisto nel match.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** Il modificatore non è letterale; rinomina solo facoltativa.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-10 — Quantità ordinate vs quantità richieste
- **Finding / sezioni:** Q:F-010;M:F-04;D:§3.3.
- **Gold R1:** GS-018;GS-028.
- **Ancora testuale/controllo:** «quantità ordinate».
- **Proposta:** Preservare non-equivalenza NON dimostrata, senza forzare distintività ontologica; collegare ancore.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** La menzione quantità ordinate è letterale, non normalizzazione inventata.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-11 — Ambiguità referenziale di ne / infrastruttura
- **Finding / sezioni:** D:F-02;Q:F-009.
- **Gold R1:** GS-024;GS-032.
- **Ancora testuale/controllo:** «La piattaforma utilizza il suo servizio, ma non ne gestisce l’infrastruttura.».
- **Proposta:** Estendere contesto evidenza; evitare attribuzioni di ownership o caratteri tecnici; annotare lettura contestuale.
- **Disposizione preliminare:** `NEEDS_REVIEW`. **Motivo:** Q riguarda solo la citazione corta; D segnala un’ulteriore ambiguità semantica.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-12 — Esternità Payment Provider doppio conteggio
- **Finding / sezioni:** D:F-03;M:§3.5.
- **Gold R1:** GS-016;GS-029.
- **Ancora testuale/controllo:** «un Payment Provider esterno».
- **Proposta:** Separare identità Provider e proprietà esterno a livello di scoring, senza penalità doppia.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** Non è duplicazione dello stesso tipo: oggetto vs proprietà; lo scoring può duplicare peso.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-13 — Evidenze incomplete delle condizioni temporali
- **Finding / sezioni:** M:F-09.
- **Gold R1:** GS-040;GS-041;GS-045;GS-046.
- **Ancora testuale/controllo:** «Dopo la conferma della riserva».
- **Proposta:** Estendere evidenza a sottostringa originale contigua che include qualifica.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** Citazioni correnti letterali ma non autosufficienti per verificare le qualifiche.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-14 — Ancore senza corrispettiva O (Acquisto, servizio provider)
- **Finding / sezioni:** M:F-03;D:§3.5,§4;M:§3.3.
- **Gold R1:** GS-031;GS-033.
- **Ancora testuale/controllo:** «Quando un cliente conferma un acquisto».
- **Proposta:** Esplicitare che ancore non-O sono ammesse; valutare O Acquisto se effettivamente richiesto.
- **Disposizione preliminare:** `NEEDS_REVIEW`. **Motivo:** Non obbligare la prima classe BAE; preservare il fatto e la referenza.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-15 — Classificazione negativa GS-032 e GS-051
- **Finding / sezioni:** G:F-02;G:F-03;D:F-04.
- **Gold R1:** GS-032;GS-051.
- **Ancora testuale/controllo:** «ma non ne gestisce l’infrastruttura.».
- **Proposta:** Conservare GS-032 come N trasversale; qualificare GS-051 come attore non determinabile, non negazione.
- **Disposizione preliminare:** `PARTIAL_ACCEPT`. **Motivo:** G:F-02 non dimostra errore: il protocollo R1 definisce N esplicitamente.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-16 — Differenza tra richiesta di riserva ed esecuzione
- **Finding / sezioni:** D:§3.6;M:§3.6;Q:§3.4.
- **Gold R1:** GS-044;GS-052.
- **Ancora testuale/controllo:** «richiede all’Inventory Service di riservare le quantità ordinate».
- **Proposta:** Non trasformare la richiesta in esecuzione incondizionata; distinguere UNSUPPORTED da CONTRADICTED.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** Q propone CONTRADICTED troppo ampio: riservare implicitamente non dimostra l’opposto.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-17 — Ordine temporale prima del contatto Payment Service
- **Finding / sezioni:** D:§3.7.
- **Gold R1:** GS-048.
- **Ancora testuale/controllo:** «la richiesta viene rifiutata prima di contattare il Payment Service».
- **Proposta:** Conservare anteriorità senza inventare una negazione permanente di contatto.
- **Disposizione preliminare:** `ACCEPT_CANDIDATE`. **Motivo:** Questione di scoring e non modifica automatica della riga.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-18 — Coerenza Markdown/CSV e autorità delle note
- **Finding / sezioni:** D:§4;M:F-08,§4;Q:§4;G:§4.
- **Gold R1:** GS-001..052.
- **Ancora testuale/controllo:** «(confronto delle colonne dei due artefatti)».
- **Proposta:** Dichiarare file operativo, funzione delle note, regola di sincronizzazione e verifica automatica.
- **Disposizione preliminare:** `NEEDS_REVIEW`. **Motivo:** Tutti riportano coerenza dei campi condivisi, ma CSV contiene campi e note aggiuntivi.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

### C-19 — Citazione tronca GS-024
- **Finding / sezioni:** Q:F-009;D:F-02.
- **Gold R1:** GS-024.
- **Ancora testuale/controllo:** «ma non ne gestisce l’infrastruttura».
- **Proposta:** Estendere citazione senza richiedere che ogni evidenza O contenga l’intera relazione.
- **Disposizione preliminare:** `OPTIONAL`. **Motivo:** Migliora intelligibilità, ma una evidenza parziale esatta non è erronea.
- **Decisione umana:** `PENDING` — motivazione e data da registrare.

## 4. Correzioni critiche alle review (non approvazioni)

- Qwen §3.2 definisce "quantità ordinate" una normalizzazione assente dal testo, ma l’espressione è presente letteralmente.
- Qwen §3.4 suggerisce `CONTRADICTED` per riserva data come incondizionata; più propriamente `UNSUPPORTED` salvo evidenza opposta.
- Gemini F-02 non dimostra un difetto: `N` è deliberatamente dichiarata etichetta valutativa nel protocollo R1.
- I tre attributi prodotto e i tre campi richiesta possono essere valutati come fatti separati anche se un LLM li produce in una relazione aggregata.
- DeepSeek e Mistral segnalano un’asimmetria U/note, ma la soluzione non è necessariamente moltiplicare le righe U per ogni proprietà non espressa.

## 5. Decision gates verso Gold Standard R2

1. Revisionare prima `C-03`, `C-04`, `C-05` (unità atomica di scoring versus formato).
2. Fissare una policy `U`: esplicita lacuna, ruolo non determinato, possibile coreferenza; indicare quando è valutabile.
3. Definire la separazione: identità candidata, attributo, relazione, azione, evento, capacità, stato e guardia; non promuovere tutto a tipo BAE.
4. Preservare l’autorità del testo e le evidenze letterali incluse le guardie; controllare la validità CSV e id cross-reference.
5. Solo dopo approvazione creare **R2** con change log e mappa R1→R2. Non modificare R1 in luogo.

## 6. Registro delle 30 segnalazioni originali (copertura)

| Revisore | Identificativi finding originali | Totale |
|---|---|---:|
| Qwen | F-001..F-011 | 11 |
| DeepSeek | F-01..F-05 | 5 |
| Gemini | F-01..F-04 | 4 |
| Mistral | F-01..F-10 | 10 |

Tutti i finding originali sono riferiti nelle schede `C-01..C-19`. Le sezioni di discussione dei modelli sono evidenziate separatamente. Le Review A originali restano fonte di dettaglio: questo registro non le sostituisce.
