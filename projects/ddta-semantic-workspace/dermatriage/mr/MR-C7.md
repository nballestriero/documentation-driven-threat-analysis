---
type: MacroRequirement
schemaVersion: '0.1'
id: MR-C7
title: Verifica del sistema DermaTriage
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
dependsOn: []
---

# MR-C7 — Verifica del sistema DermaTriage

## Intent

Verificare la disponibilità operativa dell'ambiente DermaTriage e il funzionamento delle capacità, delle interfacce, delle integrazioni e dei comportamenti rilevanti del sistema mediante controlli espliciti, con risultati osservabili e valutabili rispetto ai criteri applicabili quando documentati.

## Context

La verifica riguarda sia l'ambiente operativo predisposto per DermaTriage sia il comportamento del sistema applicativo. Comprende la disponibilità dei servizi, le interfacce e le operazioni API, i singoli stadi della pipeline AI, il comportamento end-to-end, le integrazioni esterne e gli altri controlli funzionali e di qualità documentati.

I risultati osservati, i risultati attesi, le condizioni di superamento e i criteri di accettazione sono concetti distinti: il solo svolgimento di una verifica non implica che un criterio sia soddisfatto. La granularità dei controlli e dei loro esiti viene precisata nei documenti subordinati.

La verifica è una responsabilità autonoma dalla predisposizione dell'ambiente e dalla realizzazione del comportamento applicativo. Può essere eseguita su un'installazione già disponibile, senza richiedere una nuova esecuzione del setup. L'eventuale workflow che orchestra setup e verifica è distinto dalle due responsabilità e non è definito in questo MR.

## Turtle

```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix derma: <https://example.org/ddta/dermatriage#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

derma:DermaTriage
    a ddta:System .

derma:DermaTriageVerification
    a ddta:Function ;
    rdfs:label "Verifica sistema"@it ;
    ddta:verifies derma:DermaTriage,
                  derma:DermaTriageEnvironment ;
    ddta:hasOutput derma:VerificationResults .

derma:VerificationResults
    a ddta:Information .
```
