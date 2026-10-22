---
type: Decision
schemaVersion: '0.1'
id: DEC-MR03-02
title: Tracciabilità esplicita fra FunctionalRequirement e artefatti di realizzazione
parentMacroRequirement: MR-03
lifecycle: candidate
authority: EXPERIMENTAL_NON_CANONICAL
decisionKind: SELECTABLE
---

# DEC-MR03-02 — Tracciabilità esplicita fra FunctionalRequirement e artefatti di realizzazione

## Context

Un assessment statico può descrivere una realizzazione tecnica in un particolare checkpoint, ma diventa storicamente datato quando cambiano funzioni, file o contratti. È necessario distinguere gli obblighi normativi dell'FR dalle evidenze tecniche correnti; l'esistenza di codice non dimostra che tutti gli obblighi siano soddisfatti. La tracciabilità deve essere verificabile senza inventare identità BA o attribuire automaticamente conformità.

## Decision

**Scelta progettuale candidata:** ogni `FunctionalRequirement` può dichiarare nel front matter YAML `implementationClaim` (`unassessed`, `partial`, `implemented`) e una lista `implementationBindings` di elementi `percorso-relativo-al-progetto.py::simbolo`. La dichiarazione di `implementationClaim` è una responsabilità esplicita del programmatore (o del responsabile tecnico della realizzazione): il servizio non assegna, non promuove e non corregge automaticamente il valore `implemented`. La claim non costituisce da sola approvazione semantica o dimostrazione di conformità delle clausole. La claim `unassessed` può coesistere con binding tecnici già conosciuti, anche quando la realizzazione è ancora in sviluppo o la conformità funzionale non è stata valutata. Ogni binding dichiarato, indipendentemente dalla claim, è sottoposto alla verifica formale di risolvibilità; un binding non risolvibile produce diagnostica senza essere interpretato come prova di non conformità funzionale. Se la claim è `partial` oppure `implemented`, deve esistere almeno un binding risolvibile in uno scope di progetto esplicito. Ciascun simbolo Python dichiarato deve contenere nella propria docstring un riferimento testuale `DDTA-FR: <ID-FR>`; le interfacce e i validatori non devono mantenere copie autonome delle associazioni.

La verifica formale controlla soltanto la risolvibilità del file, la presenza del simbolo nel sorgente Python e il riferimento di ritorno al FunctionalRequirement realmente indicato. Anche per `implemented` è obbligatorio almeno un binding verificabile; un binding mancante o invalido impedisce un esito positivo del controllo di tracciabilità, ma il suo esito positivo non assegna né conferma automaticamente la completezza funzionale della claim. Non valuta la copertura delle `normativeClause`, l'equivalenza semantica, l'adeguatezza dei test o lo stato di accettazione. I metadati sono supporto documentale L2 sperimentale; non introducono una nuova proprietà L1 o una BA. Non vengono modificati automaticamente i vecchi assessment: restano evidenze datate, non il registro corrente dei binding.

## Consequences

- Un FR con claim `partial` o `implemented` ma senza artefatto/simbolo verificabile genera una diagnostica, anziché un PASS apparente.
- L'associazione corrente è consultabile direttamente nel FR e nel codice; l'assenza di una claim non equivale a «non implementato».
- `unassessed` non vieta di conoscere la realizzazione tecnica: un binding dichiarato viene verificato formalmente, ma non attesta una valutazione della conformità funzionale o il completamento dello sviluppo.
- La validazione delle implementazioni opera **solo sui FunctionalRequirement**, separata dal controllo di sintassi e dal controllo dei parent documentali.
- Il superamento del controllo di tracciabilità non trasforma una claim `partial` in `implemented` e non certifica soddisfatte le clausole dell'FR.
- Le scelte di trasferimento, rinomina e conservazione delle identità richiedono una Decision differente e una review semantica.

## Questioni di review (non normative)

- Quali evidenze di test e review delle singole clausole il programmatore deve consultare per giustificare la propria dichiarazione `implemented`? Le eventuali regole di assessment aggiuntive richiederanno un contratto documentato distinto; il validatore corrente non le inventa.
- Come estendere i binding a metodi, classi non Python o repository esterni con regole esplicite, senza supporre automaticamente la loro equivalenza?

## Base Analysis

**NOT YET AUTHORED.** Nessun BAReferent o legame `realize` è derivato dai nomi dei moduli Python.
