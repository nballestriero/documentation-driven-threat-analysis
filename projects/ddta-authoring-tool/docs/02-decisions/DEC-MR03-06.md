---
type: Decision
schemaVersion: '0.1'
id: DEC-MR03-06
title: 'Tracciabilita reciproca delle specifiche di test verso FR e codice'
parentMacroRequirement: MR-03
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE
---

# DEC-MR03-06 — Tracciabilita reciproca delle specifiche di test verso FR e codice

## Context

I test del prototipo verificano aspetti strutturali, errori e vincoli, ma una lista di test eseguiti non ne documenta lo scopo. Test introdotti per contrastare architetture scartate o per riprodurre episodi storici possono sopravvivere senza giustificazione funzionale. Serve una tracciabilita verificabile tra il comportamento governato in un FunctionalRequirement, il caso di test che lo verifica e il codice che lo esegue. Uno SpecializedRequirement DDTA, invece, aggiunge una obbligazione normativa al parent: una specifica di test non deve svolgere quel ruolo.

## Decision

**Scelta candidata:** definire `TestSpecification` come documento di verifica distinto da uno SpecializedRequirement, con esattamente un `parentFunctionalRequirement` dichiarato. Una TestSpecification puo contenere piu casi di test con ID stabili: ciascun caso indica almeno la clausola `NC` del parent che verifica, la motivazione, le precondizioni, l'azione, il risultato atteso e uno o piu binding a funzioni di test Python.

**Granularita dei casi ed equivalenza degli scenari:** ogni `TestCase` documenta uno scenario di verifica distinguibile per condizioni di ingresso, azione astratta, contesto o profilo applicabile e risultato atteso, rispetto a una o piu NC del proprio FR. La condivisione della stessa NC, dello stesso codice diagnostico o di un nome di test simile non dimostra da sola l'equivalenza di due scenari. Uno stesso caso puo avere piu `testBindings` se i metodi verificano lo stesso comportamento osservabile rispetto a contratti applicabili equivalenti: ad esempio, due tipi documentali possono imporre lo stesso vincolo dichiarativo, pur usando campi parent diversi. Il `rationale` del caso deve motivare l'equivalenza richiamando i contratti pertinenti, mentre `preconditions`, `action` ed `expectedResult` devono descrivere lo scenario comune senza nascondere differenze sostanziali. Se cambiano l'obbligazione verificata, la condizione rilevante, il profilo o l'esito atteso, occorrono casi distinguibili, anche se la NC e la stessa. L'equivalenza fra contratti e una valutazione di review, non una deduzione automatica dal numero di funzioni collegate; un controllo di tracciabilita puo verificare i binding, non provare tale equivalenza.

Il collegamento e bidirezionale: il documento di test dichiara ogni simbolo che lo realizza; la docstring di ciascuna funzione di test dichiara `DDTA-TC: <ID-caso>`. Il servizio confronta entrambe le dichiarazioni e risolve il parent e la clausola senza dedurli dal filename, dal nome del metodo o dalla sua somiglianza semantica. La localizzazione di una funzione Python e verificata, ma tale presenza non prova che la funzione verifichi correttamente la clausola.

Ogni test deve avere una giustificazione derivabile da un FR o da un contratto governato dall'FR. Evitare casi dedicati all'assenza di componenti storici che non fanno parte del progetto. Per il catalogo BA, la proprieta da verificare e la corrispondenza completa fra guide ammesse e operatori riconosciuti, indipendentemente dai singoli operatori presenti. Un elenco di nomi specifici non e la fonte del catalogo.

**Impronte delle clausole:** le NC conservano un identificatore stabile (`NC-1`, ...) ma non richiedono versioni manuali. Un servizio comune, utilizzabile da test e validatori, estrae il contenuto normativo di ogni clausola di un FR e calcola un MD5 deterministico del testo normalizzato. Il formato di normalizzazione è governato da un FR dedicato e non può variare implicitamente fra ambienti o componenti. Il numero della NC non è incluso nell'impronta: l'identità e il contenuto sono due verifiche indipendenti. MD5 è usato unicamente come rilevatore di modifiche documentali, **non** come controllo di integrità contro alterazioni intenzionali.

Ogni caso di TestSpecification dichiara le NC coperte **con i rispettivi MD5 attesi**; ciascuna funzione Python di test dichiara `DDTA-TC` e i riferimenti `DDTA-NC: FR-ID/NC-ID MD5=<impronta>`. Il validatore confronta i tre lati FR / TestSpecification / codice: un riferimento orfano, una versione di contenuto superata o un disallineamento fra le due dichiarazioni di test produce una diagnostica. Le impronte attese **non** vengono aggiornate automaticamente quando cambia il FR: la modifica richiede review dei test e conferma esplicita del nuovo riferimento.

**Organizzazione della suite:** per i test di un FunctionalRequirement, l'organizzazione operativa preferita e una TestSpecification con piu casi e un modulo Python di test associato a quello stesso FR. Le funzioni dichiarano l'identita del caso e gli MD5 delle NC verificate; il modulo non e fonte autonoma di requisiti. I file e le funzioni devono essere risolti dai binding, non soltanto dai nomi convenzionali. La scoperta automatica tramite `unittest discover` rimane una modalita di esecuzione del prototipo, distinta dalla futura composizione della suite a partire dagli FR correnti. Se un FR scompare, la relativa specifica e i test devono essere segnalati come orfani prima di qualsiasi eliminazione; nessuna cancellazione automatica e autorizzata.

L'introduzione e incrementale: in una fase pilota il controllo circoscritto alle TestSpecification dichiarate puo riuscire mentre la suite legacy resta **non riconciliata**. Un controllo globale non puo dare un PASS di copertura finche esistono funzioni di test senza caso o casi senza binding reciproco. La review semantica dei test rimane responsabilita umana.

## Consequences

- La fonte del comportamento testato rimane l'FR, non la suite Python.
- Un caso di test viene giustificato una volta sola e puo avere piu realizzazioni tecniche dichiarate quando l'equivalenza dello scenario e motivata in riferimento ai contratti; condizioni distinguibili rimangono casi separati.
- Test con riferimenti assenti, duplicati o discordanti sono riconoscibili automaticamente.
- La riconciliazione degli attuali test avviene per invariante funzionale, non per numero di metodi o per cronologia dei checkpoint.
- I risultati dei test sono evidenze tecniche, non accettazione semantica delle clausole.
- La modifica del contenuto di una NC cambia la sua impronta e rende visibile la necessità di riesaminare i test che vi fanno riferimento, indipendentemente da una versione manuale.
- Il controllo di completezza delle NC senza test resta distinto dal controllo dei riferimenti reciproci; nessun PASS pilota attesta copertura globale.

## Questioni di review (non normative)

- Valutare la futura espressione di una copertura quantitativa per clausola senza trasformarla in prova automatica di adeguatezza.
- Rivedere i test legacy prima di eliminarli, identificando gli eventuali comportamenti essenziali non ancora esplicitati nei casi di test. Nei casi con piu binding, verificare e documentare se i metodi condividono davvero uno scenario o se vanno separati.

## Base Analysis

**NOT YET AUTHORED.** Il nuovo tipo documentale e le funzioni Python proposte non introducono automaticamente BAReferent o BAProposition.
