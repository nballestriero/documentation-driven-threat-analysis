---
type: Decision
schemaVersion: '0.1'
id: DEC-MR03-05
title: 'Verifica della continuità strutturale fra Base Analysis padre e figlio'
parentMacroRequirement: MR-03
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE
---

# DEC-MR03-05 — Verifica della continuità strutturale fra Base Analysis padre e figlio

## Context

La gerarchia documentale MR → Decision → FR definisce una relazione di specializzazione, ma la sola presenza del riferimento `parentMacroRequirement` o `parentDecision` non prova che la Base Analysis del figlio conservi un collegamento funzionale con la Base Analysis del padre. Una BA figlia può introdurre referent e proposition formalmente validi che rimangono tuttavia scollegati dalle identità rappresentate nel parent. Questo difetto strutturale è rilevante anche quando la congruità semantica delle proposition non può essere verificata automaticamente.

Le BA possono essere elaborate in momenti diversi e, secondo `DEC-MR01-04`, appartengono alle sezioni `## Base Analysis` dei rispettivi documenti DDTA. L'assenza della sezione BA non autorizza a inventare un collegamento né a dichiarare verificato l'aggancio. La risoluzione delle identità e delle relazioni parent appartiene a MR-03; i vincoli di ruolo dei singoli operatori appartengono a MR-02.

## Decision

**Scelta candidata, NON IMPLEMENTATA:** introdurre un controllo interdocumentale di **aggancio strutturale della BA** tra ciascuna coppia immediata di documenti MR → Decision oppure Decision → FR, quando entrambe le BA sono disponibili, interpretabili e correttamente associate alle identità dei rispettivi documenti. La relazione di parent viene determinata dai riferimenti YAML dichiarati e risolti nel workspace, non dal filename né dalla numerazione degli ID.

L'aggancio strutturale è osservato quando **almeno un BAReferent identificabile nella BA del parent viene richiamato con la medesima identità in un ruolo di almeno una BAProposition appartenente alla BA del figlio**. Non è sufficiente citare il referent in una tabella o ripeterne il nome nel testo: occorre il suo utilizzo in una proposition del figlio. Un'identità del parent può essere riutilizzata nel figlio senza ridefinirla né attribuirle un nuovo ID. La verifica opera su identificatori di BAReferent risolti, non sulla somiglianza dei nomi.

Se entrambe le BA sono disponibili e interpretabili ma nessun aggancio viene rilevato, il servizio futuro MUST restituire la diagnostica candidata `BA-PARENT-ANCHOR-MISSING`, inizialmente con severità **warning di review**, corredata da evidenza dell'assenza, identificativi parent/child e indicazioni per autore umano e LLM. Se la BA del parent o quella del figlio non è disponibile, oppure la loro associazione o le identità non sono risolvibili in modo affidabile, il servizio MUST rappresentare il controllo come `UNVERIFIED`/incompleto e MUST NOT produrre un PASS di continuità strutturale. La distinzione fra un warning di aggancio mancante e un controllo non eseguibile deve essere esplicita.

Il superamento del controllo prova soltanto l'esistenza di un **collegamento strutturale verificabile**: non dimostra che la specializzazione sia semanticamente adeguata. La diagnostica non conferisce al software o all'LLM l'autorità per aggiungere, inventare, rinominare o collegare identità al solo fine di rimuovere l'avviso. La guida generale BA e le regole dei singoli operatori conservano responsabilità distinte; questo controllo non è una regola specifica di `transfer`.

## Consequences

- Una Decision o FR con BA strutturalmente scollegata dal proprio parent può essere individuata e presentata per review, anche in assenza di una valutazione semantica automatica.
- La continuità è verificata per coppie immediate MR → Decision e Decision → FR, senza saltare livelli o sostituire i riferimenti dichiarati.
- Il controllo richiede una risoluzione esplicita delle identità BA del parent e del figlio; una BA assente o uno scope insufficiente non diventano falsi esiti positivi.
- Il warning di aggancio mancante non viene confuso con la mancanza di ruoli obbligatori di un operatore o con l'assenza di una BA.
- CLI, futuri client VS Code e LLM potranno consumare lo stesso risultato diagnostico strutturato, secondo `DEC-MR02-02` e `FR-MR02-02-03`.
- L'adozione futura di una severità bloccante in profilo `strict` richiederà review esplicita e casi di regressione; non è autorizzata implicitamente in questo checkpoint.

## Questioni di review (non normative)

- Formalizzare il controllo delle BA embedded nei rispettivi documenti (`DEC-MR01-04`), mantenendo separata la risoluzione delle identità BAReferent condivise.
- Precisare l'insieme dei referent del parent riconoscibili come candidati all'aggancio quando il parent riutilizza a sua volta identità ereditate, senza creare nuove identità.
- Testare su casi diversi da MR-01 / DEC-MR01-01 se ogni specializzazione documentale implichi lo stesso vincolo di aggancio e quando un'alternativa esplicita sia giustificata; fino alla review la severità resta warning.
- Definire la collocazione futura delle istruzioni diagnostiche machine-readable per le regole gerarchiche, distinta dalle guide dei singoli operatori, per evitare copie divergenti dei prompt.

## Base Analysis

**NOT YET AUTHORED.** Questa Decision formalizza un controllo candidato: non introduce automaticamente una BAProposition o un BAReferent per il servizio implementativo futuro.
