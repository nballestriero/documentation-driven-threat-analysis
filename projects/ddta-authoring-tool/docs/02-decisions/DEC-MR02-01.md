---
type: Decision
schemaVersion: '0.1'
id: DEC-MR02-01
title: 'Verifica comune guidata dal formato documentale'
parentMacroRequirement: MR-02
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE  # classificazione di review, non normativa
---

# DEC-MR02-01 — Verifica comune guidata dal formato documentale

## Context

I tipi documentali DDTA presentano vincoli differenti di struttura, campi, cardinalità e riferimenti. Un validatore separato per ciascun tipo duplicherebbe la logica comune e potrebbe restituire risultati diversi per vincoli equivalenti. Occorre distinguere l'interpretazione del formato dalla verifica dei vincoli propri di un tipo.

## Decision

**Commitment progettuale candidato:** adottare un servizio di validazione comune che identifica il tipo dichiarato del documento, seleziona la definizione di formato applicabile e verifica i vincoli formalizzabili mediante un motore condiviso. Il servizio utilizza le stesse definizioni caricabili previste da `DEC-MR01-02`, distinguendo controlli generici e regole specialistiche esplicitamente dichiarate, senza introdurre un validatore indipendente per ciascun tipo.

La verifica dei riferimenti tra documenti può consumare servizi di identità di `MR-03`; non deve dedurne autonomamente significati o corrispondenze. La correttezza strutturale non equivale ad accettazione semantica delle affermazioni o delle BAProposition.

## Consequences

- MR, Decision e FR sono verificabili dal medesimo flusso di controllo selezionando i rispettivi formati, mentre i loro vincoli distintivi restano espliciti.
- Un formato non riconosciuto, assente, incompatibile o invalido impedisce di dichiarare una verifica conclusa positivamente e produce un risultato diagnostico.
- I controlli generici non sono replicati per ogni tipo; i vincoli non esprimibili dal formato comune devono essere riconoscibili come controlli specializzati.
- Il motore non approva automaticamente la sufficienza del significato governato e non trasforma convenzioni candidate in regole metodologiche.

## Questioni di review (non normative)

- Quale contratto di definizione YAML e quali validatori specializzati sono necessari per la prima implementazione MR/Decision/FR?
- Quali controlli richiedono un workspace per risolvere parent e riferimenti e quali operano sul singolo documento?
- Come gestire documenti preesistenti non ancora convertiti al formato dichiarativo?

## Base Analysis

**NOT YET AUTHORED.** Non sono assegnati BAReferent o `realize` a moduli Python ipotetici.
