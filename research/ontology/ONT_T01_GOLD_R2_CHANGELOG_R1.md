# ONT-T01 Gold R2 — changelog e controlli (REVIEW CANDIDATE)

- R1: 52 righe; R2: 64 unità; 50 unità provenienti 1:1 da R1, 6 unità provenienti da 2 righe R1 aggregate, 8 nuove unità candidate. Nessuna riga R1 eliminata senza mappatura.
- `GS-025` e `GS-028` mappano a tre unità ciascuno; il punteggio non richiede tre record JSON separati.
- Nuove unità: capacità d'acquisto, relazione prodotti–catalogo, tre menzioni dei campi richiesta, conferma della riserva come antecedente temporale, acquisto come menzione, disponibilità verificata come menzione distinta dalle informazioni conservate.
- Aggiornamenti conservativi: nome richiesta, externality Provider, infrastruttura pronominale, GS-035 disponibilità, evidenza condizionale nelle righe GS-040/041/045/046.
- `T`, `N`, `U` sono etichette di valutazione, non nuove famiglie ontologiche BA.
- Criteri per accettazione futura: validazione automatica CSV/Markdown; review umana di nuove unità e del trattamento N/U/T; revisione dei finding conflittuali senza applicare il voto di maggioranza; conservazione output LLM V1 immutati.
- Non abbiamo ancora misurato gli output dei quattro LLM contro R2. Nessuna metrica pubblicata.
- Problema noto storico: nel commit `0ceedcd` possono restare tre righe con trailing whitespace del consolidato R1; questo pacchetto non modifica quel file, che va gestito separatamente.
