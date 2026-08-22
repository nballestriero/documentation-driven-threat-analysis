# MR-0003 — Determinazione dell'identità al punto di accesso

**Lifecycle:** candidate
**Authority:** `EXPERIMENTAL_NON_CANONICAL` — not a primary Base Analysis source.

## Intent

Consentire al processo di accesso di determinare quale identità governata corrisponde alla persona presente al punto di accesso e di rendere disponibile l'esito di tale determinazione alle responsabilità successive del controllo dell'accesso.

## Context

Quando questa responsabilità inizia, la persona è presente al punto di accesso ma la specifica identità governata che le corrisponde non è ancora determinata.

Le identità governate costituiscono riferimenti già gestiti dal progetto; questa responsabilità non le crea né le amministra, ma determina quale identità governata corrisponde alla persona presente.

Il modo con cui tale determinazione viene realizzata è una scelta di progetto che può evolvere: il MacroRequirement non fissa riconoscimento facciale, sensore, modello ML, placement dell'elaborazione, rete o protocollo.

## Stakeholders

- persone che si presentano al punto di accesso;
- responsabili del servizio di accesso;
- addetti alla sicurezza fisica;
- responsabili organizzativi interessati alla corretta distinzione tra determinazione dell'identità, autorizzazione e decisione di accesso.

## Scope

Rientrano nella responsabilità la determinazione di quale identità governata corrisponde alla persona presente al punto di accesso e la disponibilità del relativo esito alle responsabilità successive del controllo dell'accesso.

Non rientrano nella responsabilità:

- la creazione o il mantenimento delle identità governate;
- la concessione, revoca o gestione delle autorizzazioni di accesso;
- la decisione relativa al singolo tentativo di accesso;
- la strategia tecnica utilizzata per determinare l'identità;
- il placement dell'elaborazione;
- il mezzo di comunicazione;
- le tecniche di sicurezza utilizzate dalla realizzazione.

## Cross-branch note

Il consumer governato del risultato appartiene al ramo che possiede il controllo e la decisione di accesso. Il binding esatto tra l'identità determinata, il relativo stato di autorizzazione e la decisione di accesso deve essere verificato quando i relativi rami vengono analizzati nello stesso baseline.
