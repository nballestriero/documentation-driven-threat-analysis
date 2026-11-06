# Graph L3 — vista generale degli MR selezionati

**Stato:** vista generica in revisione, riproducibile dai Markdown canonici. Nessun MR alternativo.

## Obiettivo e semantica

Graph L3 rappresenta le identità RDF e le relazioni **esplicitamente dichiarate** nei MacroRequirement selezionati, conservando i collegamenti architetturali dei livelli precedenti ed espandendo i costrutti logici:

- `System` / `Environment`: `hasOperationalEnvironment`, `hasPart`, `prepares`, `verifies`.
- `Function`: `hasPrimaryFunction`, `hasInput`, `hasOutput`, `hasPart` (sottofunzioni), `hasMode` (modalità, **non** sottofunzioni).
- `Information`: `hasPart`, identità condivise tra documenti, input/output dichiarati.
- `Contract` / `ContractElement`: conservati e validati nel Turtle; nella vista L3 standard vengono proiettate sulle Information solo le cardinalità.
- `FunctionalMode`: `hasInput`, `hasOutput` (identiche alle proprietà della Function). `hasMode` distingue una modalità da una sottofunzione. Le proprietà specifiche di modalità sono state eliminate dal Core.

Nessun DEC o FR è caricato nel comando standard. Non sono derivati trasferimenti, sequenze di esecuzione, implementazioni, autenticazione o risultati di verifica/qualificazione.

**Lacune documentali:** rimangono nei Turtle originali e vengono validate dall'autore, ma sono **omesse dalla proiezione standard** di Graph L3. La visibilità su richiesta e il focus saranno definiti successivamente; non esiste ancora un selettore.

**Collegamenti nascosti nella vista:** `providesFunction` (ridondante nella rappresentazione L3), `informationLink` e `informationCompositionLink` non sono riprodotti come archi supplementari nella vista L3, poiché le dichiarazioni sorgente `hasInput`, `hasOutput` e `hasPart` sono mostrate direttamente. La relazione `providesFunction` resta nel modello RDF, ma non è visualizzata in L3. Le triple RDF non vengono eliminate né sostituite nel modello originale.

**Contratti compatti:** `Contract` e `ContractElement` non compaiono come nodi o frecce nella vista L3 standard. Non vengono cancellati dall’RDF. Una vista dedicata potrà disegnarli.

**Cardinalità:** la rappresentazione 0..1 e 1..1 viene derivata dal `ContractElement` e aggiunta soltanto come metadato di vista `urn:ddta:view#minOccurs` e `urn:ddta:view#cardinality` al risultato SPARQL, non al Turtle del MR.

**Contenimento grafico:** l'uso di `subgraph` per `hasPart`/`hasMode` non implica esecuzione, collocazione fisica, possesso esclusivo o realizzazione. `ClinicalReviewRecord` contiene logicamente `TriageOutcome` e `ClinicalReview` anche quando la realizzazione fisica usa soltanto riferimenti.

## Comandi di rigenerazione (Windows / PowerShell)

Dalla cartella `C:\Users\user\Documents\TESI\projects\ddta-semantic-workspace`:

```powershell
$MRs = "MR-01,MR-02,MR-03,MR-04,MR-C6,MR-C7"
$Out = Join-Path $env:TEMP "DDTA-Generic-Graph\L3_ALL"
python -m tools.visualize --mr $MRs --view l3 --out $Out `
  --emit-merged --emit-query-result
code "$Out.graph.md"
```

Il tool legge **direttamente** i sei file `dermatriage/mr/MR-*.md`. Produce `.mmd`, `.graph.md`, `.merged.ttl` e `.result.ttl` fuori dal repository. È possibile rigenerare gli stessi risultati con `--check` senza scrivere.

```powershell
python -m unittest tests.test_l3_general -v
python -m unittest tests.test_graph_pipeline tests.test_l3_functional_modes -v
```

## Controllo incrociato (ricostruzione al 2026-11-05)

- **MR-01:** un'unica funzione primaria, modalità con e senza immagine, `TriageOutcome` condiviso; `GeneralCaseInformation 1..1`, `LesionImage 0..1` come elementi del contratto.
- **MR-02:** `SpecialistDestinationDetermination` consuma lo stesso `TriageOutcome` di MR-01, senza assumere quale parte utilizzi.
- **MR-03:** `ClinicalReviewManagement` consuma `TriageOutcome` e `ClinicalReview`; `ClinicalReviewRecord hasPart` entrambi a livello logico. Lacuna esplicita sulla sorgente operativa della revisione.
- **MR-04:** `ControlledAdaptation hasPart` due sottofunzioni (`ImageClassificationModelAdaptation`, `GenerativePromptAdaptation`), non modalità. `AccumulatedClinicalReviewRecords hasPart ClinicalReviewRecord`.
- **MR-C6:** `EnvironmentPreparation prepares DermaTriageEnvironment`, `DermaTriage hasOperationalEnvironment DermaTriageEnvironment`, cinque componenti dell'ambiente. Le categorie non sono tipizzate con nuove classi Core per semplice convenienza grafica.
- **MR-C7:** `DermaTriageVerification verifies` il sistema e l'ambiente; non è una `providesFunction` di DermaTriage e non implica superamento dei controlli.

Nella ricostruzione verificata dopo la semplificazione: sei documenti, 112 triple RDF, 98 triple nel risultato L3 standard e tre lacune RDF nascoste. **Questi numeri vanno riconfermati sul checkout reale** durante l'installazione/rigenerazione: non sono un vincolo sul contenuto futuro degli MR.

## Questioni lasciate aperte per DEC/FR

- Contenuto minimo dei campi di `GeneralCaseInformation`.
- Produzione e vincoli dell’elemento di priorità operativa nel percorso senza immagine.
- Provenienza architetturale, interfacce e boundary dell'input `ClinicalReview`.
- Semantica e criteri di scelta della destinazione specialistica.
- Processi di aggiornamento dei modelli e dei prompt; futura ontologia AI specializzata.
- Controlli, criteri e procedure di verifica su sistema/ambiente, senza confondere verifica e superamento.

## Limitazioni della prima vista generale

La proiezione è completa rispetto alle **relazioni supportate elencate sopra**, non rispetto a ogni proprietà che potrebbe essere definita nel Core o nei futuri DEC/FR. Il grafo cumulativo può diventare denso; focus/subgraph tematici verranno aggiunti dopo la revisione della vista generale.
