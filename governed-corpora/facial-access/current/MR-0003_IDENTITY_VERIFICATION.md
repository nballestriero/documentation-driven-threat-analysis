# MR-0003 — Verifica dell'identità al punto di accesso

**Lifecycle:** superseded
**Authority:** `SUPERSEDED` — not a primary Base Analysis source.
**R24 semantic-review note:** this R1 is preserved as regression evidence. The semantic review found that it does not explicitly govern whether a specific governed identity is already determined when the responsibility begins. The candidate successor is under `governed-corpora/facial-access/candidate-r2/` and is not current authority until explicit promotion.

## Intent

Consentire al processo di accesso di stabilire se la persona presente al punto di accesso corrisponde a un'identità governata, producendo evidenza di verifica interpretabile senza far coincidere la verifica della persona con la decisione organizzativa di autorizzazione o apertura.

## Context

Il controllo dell'accesso richiede evidenza sulla corrispondenza tra la persona presente e un'identità governata. Il modo con cui tale evidenza viene ottenuta è una scelta di progetto che può evolvere: il MacroRequirement non fissa riconoscimento facciale, sensore, modello ML, placement dell'elaborazione, rete o protocollo.

Le Decision figlie governano tali commitment. Una sostituzione della strategia di verifica non dovrebbe richiedere la riscrittura di questo MR se il macro-concern resta la verifica dell'identità al punto di accesso.

## Stakeholders

- persone che si presentano al punto di accesso;
- responsabili del servizio di accesso;
- addetti alla sicurezza fisica;
- responsabili organizzativi che devono poter distinguere verifica dell'identità e autorizzazione.

## Scope

Include il macro-concern di ottenere e rendere consumabile evidenza di verifica dell'identità al punto di accesso.

Non stabilisce:

- chi concede o revoca l'autorizzazione all'accesso;
- quale strategia tecnica realizza la verifica;
- dove viene eseguita l'elaborazione;
- quale mezzo di comunicazione viene usato;
- quali tecniche di sicurezza realizzano le proprietà richieste.

## Cross-branch note

Il consumer governato dell'evidenza appartiene al ramo che possiede la decisione di accesso. Questa R1 migra soltanto MR-0003: il binding esatto al consumer cross-MR resta `OPEN` finché il ramo MR-0001 non viene migrato/analizzato nello stesso baseline.
