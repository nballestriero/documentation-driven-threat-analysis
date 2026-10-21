---
type: Decision
schemaVersion: '0.1'
id: DEC-MR03-01
title: Risoluzione dichiarativa dei riferimenti documentali
parentMacroRequirement: MR-03
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE
---

# DEC-MR03-01 — Risoluzione dichiarativa dei riferimenti documentali

## Context

La verifica del singolo Markdown stabilisce se un campo di riferimento rispetta il formato previsto, ma non dimostra che la destinazione esista o sia del tipo appropriato. La presenza di piu' documenti con lo stesso identificativo rende inoltre ambigua qualsiasi risoluzione. Un controllo interdocumentale necessita di uno scope noto e riproducibile; il filename non puo' sostituire l'identita' dichiarata.

## Decision

**Commitment progettuale candidato:** costruire un indice delle identita' documentali dichiarate nei front matter YAML dei sorgenti MR, Decision e FR selezionati in uno scope esplicito. Risolvere su tale indice le relazioni dichiarative `parentMacroRequirement` (Decision verso MR), `parentDecision` (FR verso Decision) e `dependsOn` (MR verso MR). Segnalare identificativi duplicati, destinazioni assenti, tipi di destinazione incompatibili e riferimenti ambigui con diagnostiche strutturate, senza creare identita' per inferenza.

Il controllo deve riutilizzare la validazione formale di `MR-02` e il contratto diagnostico gia' disponibile. La risoluzione e' limitata ai documenti effettivamente selezionati: non certifica collegamenti esterni allo scope. L'interpretazione del significato delle relazioni e l'eventuale unificazione di identita' BA restano sottoposte a review e non sono realizzate da questa Decision.

## Consequences

- Documenti diversi possono riferirsi a un'identita' dichiarata senza dipendere dal nome fisico del file.
- Collisioni di ID e riferimenti non risolvibili impediscono un esito di verifica `PASS`.
- I collegamenti parent conservano i confini MR → Decision → FR senza introdurre relazioni dirette MR → FR.
- Le identita' dei BAReferent, le occorrenze BA e la tracciabilita' fra revisioni richiederanno Decision/FR distinti sotto `MR-03`.

## Questioni di review (non normative)

- Definire l'estensione futura dell'indice alle BA e alle revisioni documentali, senza accorpare le identita' documentali e BA.
- Chiarire se dipendenze MR cicliche costituiscano un errore oppure un warning semantico; il primo incremento non ne deduce automaticamente l'invalidita'.
- Valutare un'estensione generica agli ulteriori tipi DDTA quando siano definiti i rispettivi riferimenti YAML.

## Base Analysis

**NOT YET AUTHORED.** Un eventuale indice Python e' una realizzazione tecnica candidata; non assegna da solo BAReferent o BAProposition canoniche.
