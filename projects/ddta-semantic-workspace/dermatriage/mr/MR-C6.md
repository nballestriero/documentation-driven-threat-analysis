---
type: MacroRequirement
schemaVersion: '0.1'
id: MR-C6
title: Predisposizione e inizializzazione dell'ambiente DermaTriage
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
dependsOn: []
---

# MR-C6 — Predisposizione e inizializzazione dell'ambiente DermaTriage

## Intent

Predisporre e inizializzare l'ambiente necessario affinché DermaTriage disponga delle risorse, dei componenti e delle configurazioni richieste per poter essere eseguito e per supportare le attività di addestramento previste dal progetto.

## Context

DermaTriage è il sistema applicativo; `DermaTriageEnvironment` è il suo ambiente operativo, distinto dall'identità del sistema. L'ambiente si compone, a livello logico e stabile, di risorse di calcolo (`ComputeResources`), componenti software (`SoftwareComponents`), risorse dei modelli (`ModelResources`), risorse dati (`DataResources`) e configurazione dell'ambiente (`EnvironmentConfiguration`).

Queste cinque identità descrivono la struttura generale dell'ambiente, indipendentemente dalle tecnologie, dalle versioni e dagli artifact concretamente installati. Le loro realizzazioni potranno essere precisate e cambiare nelle Decision e nei FunctionalRequirement, senza sostituire le identità logiche definite qui.

La predisposizione comprende la disponibilità delle risorse, l'installazione delle dipendenze, la configurazione, l'inizializzazione delle risorse locali necessarie e l'avvio dei servizi. I processi, i prodotti tecnici e le modalità concrete saranno descritti nei documenti subordinati. La verifica del sistema rimane una responsabilità distinta.

## Turtle

```turtle
@prefix ddta: <https://w3id.org/ddta/core#> .
@prefix derma: <https://example.org/ddta/dermatriage#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

derma:DermaTriage
    a ddta:System ;
    ddta:hasOperationalEnvironment derma:DermaTriageEnvironment .

derma:EnvironmentPreparation
    a ddta:Function ;
    rdfs:label "Preparazione ambiente"@it ;
    ddta:prepares derma:DermaTriageEnvironment .

derma:DermaTriageEnvironment
    a ddta:Environment ;
    ddta:hasPart derma:ComputeResources,
                 derma:SoftwareComponents,
                 derma:ModelResources,
                 derma:DataResources,
                 derma:EnvironmentConfiguration .

derma:DermaTriageEnvironment rdfs:label "Ambiente DermaTriage"@it .
derma:ComputeResources rdfs:label "Risorse di calcolo"@it .
derma:SoftwareComponents rdfs:label "Componenti software"@it .
derma:ModelResources rdfs:label "Risorse dei modelli"@it .
derma:DataResources rdfs:label "Risorse dati"@it .
derma:EnvironmentConfiguration rdfs:label "Configurazione dell'ambiente"@it .
```
