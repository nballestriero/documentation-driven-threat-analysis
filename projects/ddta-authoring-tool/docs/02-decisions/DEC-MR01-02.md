# DEC-MR01-02 — Sorgenti Markdown modulari e template per tipo DDTA

**Parent MacroRequirement:** `MR-01`\
**Lifecycle:** `candidate`\
**Authority:** `EXPERIMENTAL_NON_CANONICAL`\
**Decision kind:** `SELECTABLE` *(classificazione di review)*\

## Context

Un documento DDTA deve restare leggibile, ma una sorgente Markdown completamente libera non consente di riconoscere in modo affidabile tipo, identità e campi governati. Inoltre documentazione, Base Analysis (BA) e proiezioni Mermaid hanno ruoli differenti: conservarle in un unico file rende più difficile verificare sintassi, provenienza e coerenza; mantenerle come sorgenti concorrenti rischia di introdurre discrepanze. Il nome del file, da solo, non può definire l'identità governata.

## Decision

**Commitment candidato sul modello dei file:**

- **Documentazione DDTA:** ogni elemento documentale governato (MR, Decision, FR o specializzazione) è redatto in un proprio file Markdown. Contiene il significato documentale e i suoi campi, non la rappresentazione canonica delle BAProposition.
- **Base Analysis:** la BA relativa a un elemento documentale è conservata in un **file Markdown distinto**, collegato in modo esplicito all'identità del documento che analizza. Può essere creata e mantenuta anche in modo incrementale, senza essere automaticamente accettata per il solo fatto di esistere. Le identità BA condivise devono essere risolte in modo coerente, non duplicate per ogni file.
- **Mermaid:** ogni proiezione locale è conservata in un **file Markdown distinto**, con un blocco Mermaid generato dalla BA e non editato come fonte alternativa di verità. Sono ammesse viste che compongono BA collegate a più documenti; la loro generazione e composizione sono governate nel ramo `MR-04`, non mediante concatenazione manuale dei Mermaid locali.
- **Identificazione:** tipo, identità e collegamenti fra artefatti devono essere dichiarati e verificabili indipendentemente dalle convenzioni di denominazione. La risoluzione dei riferimenti e il riuso delle identità sono responsabilità di `MR-03`.
- **Template:** la creazione di documenti DDTA e di file BA utilizza schemi formalizzati e versionati condivisi tra CLI e VS Code. Il Mermaid viene prodotto dal sistema di proiezione a partire dalla BA validata; il relativo file non è un template da riempire manualmente.

Si conferma Markdown come formato comune dei file. La **sintassi precisa dei metadati** (per esempio YAML front matter), i nomi dei campi di collegamento e le convenzioni dei percorsi restano *candidate da specificare*, non sono approvati da questa Decision.

## Consequences

- Documentazione, BA e Mermaid possono essere sottoposti a controlli sintattici separati; la correttezza di ciascun file non dimostra automaticamente la coerenza semantica con gli altri.
- È possibile avere un documento DDTA senza una BA già redatta oppure con una BA `IDENTIFIED`/`CANDIDATE`, senza produrre automaticamente una vista Mermaid o dichiarare la BA accettata.
- Il generatore di template non crea significati di progetto, BAReferent, BAProposition o collegamenti di `realize` in assenza di analisi.
- I nomi dei file possono essere convenzionali, ma l'associazione documento–BA–vista dipende da identità dichiarate e riferimenti controllabili.
- La grammatica dei campi e degli operatori è soggetta al servizio di validazione di `MR-02`; la risoluzione delle identità compete a `MR-03`.
- `MR-04` governa il modello grafico intermedio, il rendering locale e la composizione di viste cumulative senza alterare le relazioni BA. `MR-05` governa la pubblicazione in LaTeX/PDF.
- Questa Decision non specifica il linguaggio di programmazione, le librerie, il protocollo dell'editor o il layout visivo concreto.

## Questioni di review (non normative)

- Quale struttura esatta deve dichiarare tipo/ID del documento, ID del documento analizzato dalla BA e selezione/provenienza della vista Mermaid?
- Quali convenzioni di percorso e suffisso rendono distinguibili i file senza trasformare il filename in fonte d'identità?
- Dove risiede il registro canonico BA e come sono gestiti il riuso e le occorrenze cross-documento (`MR-03`)?
- Come sono selezionate, rigenerate e verificate le viste locali e cumulative (`MR-04`)?
- Quale politica disciplina versioni di schema e migrazione dei file esistenti?
- La BA di questa Decision non è ancora stata redatta in un file separato; nessuna BAProposition viene introdotta dalla presente revisione.
