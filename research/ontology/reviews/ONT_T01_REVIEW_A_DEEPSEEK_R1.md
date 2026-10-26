# Revisione indipendente ONT-R0-GOLD-REVIEW-A-V1 — ONT-T01

## 1. Valutazione generale

Il gold standard R1 è nel complesso ben costruito: la maggior parte dei fatti è supportata dal testo originale, le evidenze sono in larga misura citazioni letterali e la separazione tra oggetti, relazioni, azioni, negazioni e lacune informative è generalmente coerente con il testo. Non emergono contraddizioni dimostrabili né fatti palesemente inventati.

Rimangono tuttavia alcune criticità significative:

- manca la factificazione della capacità/relazione espressa nella prima frase (“la piattaforma permette ai clienti di acquistare prodotti disponibili nel catalogo”);
- l’ambiguità del pronome “ne” in “non ne gestisce l’infrastruttura” è risolta in modo troppo netto in GS-032;
- l’esternità del Payment Provider è duplicata in GS-016 e GS-029;
- diverse informazioni non specificate (mittente della richiesta, destinatario delle quantità, destinatario dell’esito, attore dei cambi di stato/rifiuto) sono trattate solo come note CSV o non trattate come U, mentre altre informazioni non specificate ricevono U facts dedicati;
- la “conferma della riserva” è usata come condizione in GS-045/GS-046 ma non è factificata né come evento/azione né come U.

Il gold standard non è quindi pronto per una valutazione definitiva senza revisione, ma non richiede un rifacimento massivo.

## 2. Finding

| **Finding ID** | **Gold Fact ID interessato**                   | **Tipo**    | **Severità** | **Evidenza letterale**                                                                                                                                                                                                                                  | **Motivazione verificabile**                                                                                                                                                                                                                                                                                                       | **Correzione proposta**                                                                                                                                                                                                                                                                     |
| :------------- | :--------------------------------------------- | :---------- | :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| F-01           | NEW                                            | MISSING     | MEDIUM       | “Una piattaforma di commercio elettronico permette ai clienti di acquistare prodotti disponibili nel catalogo.”                                                                                                                                         | Il gold standard factifica Piattaforma, Cliente, Prodotto e Catalogo (GS-001–GS-004), ma non la capacità/permesso della piattaforma né la relazione “prodotti disponibili nel catalogo”. Non è equivalente a GS-033, che riguarda la conferma di un acquisto come trigger del flusso, né a GS-025 o GS-026.                        | Aggiungere un fatto NEW di tipo A/R: “Piattaforma permette ai clienti di acquistare prodotti disponibili nel catalogo”, qualifica CAPACITÀ/PERMESSO, con partecipanti Piattaforma, Cliente, Prodotto e Catalogo. In alternativa, separare la relazione “Prodotto disponibile nel Catalogo”. |
| F-02           | GS-024, GS-032                                 | UNCERTAINTY | MEDIUM       | “La piattaforma utilizza il suo servizio, ma non ne gestisce l’infrastruttura.”                                                                                                                                                                         | Il pronome “ne” può riferirsi al Payment Provider oppure al servizio del Payment Provider. GS-024 e soprattutto GS-032 risolvono il riferimento su “Payment Provider” senza riportare l’ambiguità nel fatto; la nota presente in CSV/MD su GS-024 non copre GS-032.                                                                | Rendere esplicita l’ambiguità in GS-024 e GS-032, ad esempio: GS-024 “Infrastruttura (referente pronominale: Payment Provider o servizio)”; GS-032 “Piattaforma NON gestisce l’infrastruttura [del Payment Provider / del servizio]”. In alternativa, aggiungere una riga U dedicata.       |
| F-03           | GS-016, GS-029                                 | DUPLICATE   | LOW          | “un Payment Provider esterno”                                                                                                                                                                                                                           | GS-016 include “esterno” nel nome dell’oggetto; GS-029 factifica nuovamente “Payment Provider è esterno”. La stessa informazione è codificata due volte, con rischio di doppio conteggio o match sovrabbondante.                                                                                                                   | Rinominare GS-016 in “Payment Provider” e mantenere GS-029 come stato/relazione “è esterno”; oppure eliminare GS-029 e documentare che l’esternità è solo nel label di GS-016. Preferibile la prima soluzione.                                                                              |
| F-04           | GS-034, GS-038, GS-043, GS-045, GS-047, GS-048 | UNCERTAINTY | MEDIUM       | “l'Order Service riceve la richiesta contenente”; “restituisce le quantità disponibili”; “restituisce l'esito dell'autorizzazione”; “l'ordine assume lo stato Confirmed”; “l'ordine viene contrassegnato come Rejected”; “la richiesta viene rifiutata” | Il gold standard tratta GS-051 come U per il mittente non identificato della notifica, ma per altre informazioni non specificate analoghe lascia solo note CSV o nessuna U fact. Questo rende incoerente la distinzione tra “non specificato” e “non presente” e può penalizzare output che conservano correttamente l’incertezza. | Aggiungere U facts per: mittente della richiesta; destinatario delle quantità disponibili; destinatario dell’esito dell’autorizzazione; attore del cambio a Confirmed; attore della contrassegnazione a Rejected; attore del rifiuto della richiesta. Riportare le note anche nel Markdown. |
| F-05           | NEW / GS-052                                   | MISSING     | LOW          | “Dopo la conferma della riserva”                                                                                                                                                                                                                        | Il testo menziona una “conferma della riserva” come condizione temporale per GS-045 e GS-046, ma il gold standard non la factifica né come O/A né come U. GS-052 riguarda l’esecuzione della riserva, non la conferma menzionata. Un output che rappresenta la conferma come evento/azione non ha un fatto di riferimento.         | Aggiungere una U: “Conferma della riserva menzionata ma attore, modalità e timing non specificati”, evidenza “Dopo la conferma della riserva”. Non trasformarla in esecuzione certa della riserva.                                                                                          |

## 3. Questioni modellistiche

1. **Attributi del prodotto (GS-025).** La relazione “Prodotto possiede identificativo, descrizione e prezzo” aggrega tre attributi. Sono rappresentazioni equivalenti ammissibili: una relazione n-aria, tre relazioni binarie oppure tre oggetti attributo separati. Il confronto dovrebbe accettare tutte queste forme se i tre attributi sono preservati.
2. **Campi della richiesta (GS-028).** “Identificativo del cliente”, “prodotti selezionati” e “quantità richieste” sono aggregati in una relazione. Un output che li rappresenta come oggetti separati non dovrebbe essere penalizzato automaticamente, purché la relazione di contenimento nella richiesta resti preservata.
3. **“Quantità richieste” vs “quantità ordinate”.** GS-018 nota correttamente che l’equivalenza con “QuantitaRichieste” non è dichiarata. Il confronto non deve imporre l’identità tra i due referenti; se un output li identifica, va trattato come scelta non supportata, salvo motivazione.
4. **“Servizio del Payment Provider” (GS-031).** È rappresentato come relazione, non come oggetto autonomo. Un output che crea un oggetto “servizio” e una relazione di appartenenza al Payment Provider dovrebbe essere considerato equivalente se conserva il fatto.
5. **“Acquisto” in GS-033.** Nel CSV, “Acquisto” compare come partecipante normalizzato, ma non esiste un O fact corrispondente. Poiché il protocollo dichiara che i partecipanti sono ancore di confronto e non BAReferent, la cosa è ammissibile, ma andrebbe chiarita per evitare incoerenza con gli altri partecipanti mappati su O.
6. **“Conferma della riserva”.** Può essere rappresentata come condizione, evento o stato. Il gold standard la usa solo come qualificatore in GS-045/GS-046; un output che la factifica come evento dovrebbe essere ammesso se non attribuisce attori o modalità non documentati.
7. **“Prima di contattare il Payment Service” (GS-048).** Il testo non afferma esplicitamente che il Payment Service non venga contattato; indica solo che il rifiuto avviene prima di un eventuale contatto. Il confronto non deve trasformare automaticamente questa espressione in una negazione esplicita di contatto.

## 4. Verifica di coerenza Markdown–CSV

Non risultano contraddizioni fattuali tra il Markdown e il CSV: ID, classi, fatti, qualifiche ed evidenze coincidono per i 52 fatti. Tuttavia:

- il CSV contiene numerose `nota_review` assenti nel Markdown. Questo non è di per sé un errore, ma crea un’asimmetria informativa. Le note più rilevanti riguardano GS-034, GS-038, GS-043, GS-045, GS-047, GS-048 e GS-052; alcune di esse esprimono incertezze che nel Markdown non sono rappresentate né come note né come U facts.
- In GS-052, il Markdown riporta la qualifica “NON CONCLUDERE esecuzione incondizionata”, mentre il CSV aggiunge la nota “Esiste anche una successiva conferma della riserva”. Non è una contraddizione, ma la nota CSV è più informativa e dovrebbe essere integrata nel Markdown.
- Nel CSV, GS-033 usa “Acquisto” come partecipante normalizzato senza un O fact corrispondente; GS-031 usa “servizio Provider” senza un O fact corrispondente. Poiché il protocollo ammette ancore non-O, non è un errore dimostrabile, ma va documentato esplicitamente per evitare ambiguità nel confronto.

## 5. Proposte di modifica

1. **Aggiungere NEW A/R per la prima frase.**
   - A: “Piattaforma permette ai clienti di acquistare prodotti disponibili nel catalogo”; qualifica: CAPACITÀ/PERMESSO; partecipanti: Piattaforma, Cliente, Prodotto, Catalogo; evidenza: “Una piattaforma di commercio elettronico permette ai clienti di acquistare prodotti disponibili nel catalogo.”
   - Oppure, se si preferisce granularità maggiore, aggiungere anche R: “Prodotto disponibile nel Catalogo”; partecipanti: Prodotto, Catalogo; evidenza: “prodotti disponibili nel catalogo”.
2. **Modificare GS-024 e GS-032 per l’ambiguità del pronome “ne”.**
   - GS-024: nome “Infrastruttura (referente pronominale: Payment Provider o servizio)”; qualifica: “Il referente del pronome «ne» è ambiguo”.
   - GS-032: fatto “Piattaforma NON gestisce l’infrastruttura [del Payment Provider / del servizio]”; aggiungere uncertainty esplicita.
3. **Risolvere la duplicazione GS-016/GS-029.**
   - Modificare GS-016 in “Payment Provider”.
   - Mantenere GS-029 “Payment Provider è esterno”.
   - In alternativa, eliminare GS-029 e documentare che l’esternità è nel label di GS-016.
4. **Aggiungere U facts per informazioni non specificate.**
   - U “Mittente della richiesta non identificato”; evidenza: “l'Order Service riceve la richiesta contenente”.
   - U “Destinatario delle quantità disponibili non espresso”; evidenza: “restituisce le quantità disponibili”.
   - U “Destinatario dell’esito dell’autorizzazione non espresso”; evidenza: “restituisce l'esito dell'autorizzazione”.
   - U “Attore del cambiamento a Confirmed non specificato”; evidenza: “l'ordine assume lo stato Confirmed”.
   - U “Attore della contrassegnazione a Rejected non specificato”; evidenza: “l'ordine viene contrassegnato come Rejected”.
   - U “Attore del rifiuto della richiesta non specificato”; evidenza: “la richiesta viene rifiutata”.
   - U “Attore dell’autorizzazione del pagamento non specificato”; evidenza: “il pagamento viene autorizzato”.
5. **Aggiungere U per la conferma della riserva.**
   - U “Conferma della riserva menzionata ma attore, modalità e timing non specificati”; evidenza: “Dopo la conferma della riserva”.
6. **Integrare nel Markdown le note CSV rilevanti**, almeno per GS-034, GS-038, GS-043, GS-045, GS-047, GS-048 e GS-052, oppure dichiarare il CSV come parte integrativa obbligatoria del gold standard.
7. **Chiarire le ancore non-O** “Acquisto” in GS-033 e “servizio Provider” in GS-031, oppure aggiungere O facts dedicati se si vuole mantenere la mappatura completa dei partecipanti.

## 6. Valutazione finale

**Classificazione: REVISION_REQUIRED**

Il gold standard R1 è sostanzialmente corretto e utilizzabile come base, ma richiede revisioni mirate prima della valutazione definitiva. Le criticità principali non sono errori diffusi di supporto testuale, bensì: la mancata factificazione della prima frase, l’ambiguità del pronome “ne” risolta troppo nettamente, una duplicazione dell’esternità del Payment Provider e un trattamento non uniforme delle informazioni non specificate. Questi elementi possono alterare il confronto con output LLM semanticamente equivalenti, perciò il gold standard non è ancora `READY_FOR_EVALUATION`. Non si configura tuttavia un `MAJOR_REWORK_REQUIRED`, perché la maggior parte dei fatti è corretta, supportata e ben evidenziata.

*Questa risposta è generate da IA. Controllarne l'accuratezza.*