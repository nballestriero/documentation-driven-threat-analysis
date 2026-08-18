# Documentation gaps and explicit placeholders — current R1

Questa lista impedisce alla costruzione della BA di riparare silenziosamente ciò che la documentazione corrente non ha ancora governato.

I record sono diagnostici. Non diventano automaticamente nuovi requisiti o nuove semantiche BA.

## OPEN — DG-FA-001: cross-MR consumer binding

`MR-0003` produce evidenza di verifica consumata dal processo di accesso, ma questa R1 non migra ancora il ramo `MR-0001`.

**Placeholder:** `@ACCESS_DECISION_CONSUMER`

Durante una BA limitata a MR-0003:

- il consumer può essere mantenuto come riferimento cross-scope non risolto;
- NON deve essere inventato un canonical referent definitivo;
- il gap diventa errore documentale solo se, dopo la migrazione/analisi del ramo MR-0001, non esiste un target governato univoco.

## OPEN — DG-FA-002: quality/sufficiency criterion

Il corpus storico parlava di qualità "sufficiente" per supportare la decisione di accesso. La nuova MR non nasconde quel criterio dentro il macro testo, ma R1 non possiede ancora uno SpecializedRequirement governato che definisca come giudicare la sufficienza.

**Placeholder:** `@IDENTITY_EVIDENCE_QUALITY_CRITERION`

**Specialization review candidate:** valutare un requisito specializzato verificabile collegabile a test/evidence. Non inventare soglie durante la BA.

## OPEN — DG-FA-003: transfer-to-channel/path binding

`FR-3.4.2` governa il delivery; `D-3.5` governa il responsibility boundary del trasporto; `D-3.6` governa Ethernet nel baseline R1.

La documentazione non possiede ancora una relazione strutturale univoca equivalente a:

```text
THIS transfer
    uses
THIS connectivity/path
```

**Placeholder:** `@FR-3.4.2-TRANSPORT-BINDING`

Questo gap deve essere testato prima di modificare BA2. Alternative da falsificare:

1. la documentazione può esprimere meglio il binding usando relazioni già governate;
2. la BA può derivare il binding in modo riproducibile da fonti sufficienti;
3. il contratto `transfer` necessita davvero un ruolo opzionale `channel`/analogo;
4. serve una diversa modellazione minima, senza trasformare BA in topologia di rete.

## CANDIDATE — DG-FA-004: intermediate transport nodes

Il corpus R1 non governa switch, firewall o altri hop intermedi.

Questa assenza NON è automaticamente un difetto: il progetto consuma un servizio di connettività e può non possedere tali dettagli.

Diventa documentation gap se un declared analysis scope richiede di comprendere nodi/intermediari governati necessari alla macro-funzionalità e la documentazione autorevole non consente di recuperarli.

Regola proposta da testare:

```text
governed intermediate node/capability
    -> must remain recoverable

required-for-declared-analysis but undocumented
    -> documentation gap

not governed / not required
    -> do not invent
```

## OPEN — DG-FA-005: test/code evidence linkage

I Security Requirements sono ora documenti autonomi e quindi possono diventare target stabili per test, verification evidence e code trace.

R1 non introduce ancora un metamodel di test/code trace. La BA non deve inventarlo; il prossimo confronto può però misurare se l'estrazione dei vincoli dalla prosa alta verso SR migliora concretamente la possibilità di collegare evidence downstream.
