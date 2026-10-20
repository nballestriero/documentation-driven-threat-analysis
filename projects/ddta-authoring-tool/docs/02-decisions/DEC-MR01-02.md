# DEC-MR01-02 — Sorgente Markdown dichiarativo e template per tipo DDTA

**Parent MacroRequirement:** `MR-01`\
**Lifecycle:** `candidate`\
**Authority:** `EXPERIMENTAL_NON_CANONICAL`\
**Decision kind:** `SELECTABLE` *(classificazione di review)*\

## Context

Un Markdown completamente libero è leggibile, ma non consente di riconoscere deterministicamente il tipo documentale, i campi obbligatori e i valori enumerati. Il solo nome file non rappresenta una fonte affidabile per stabilire tipo e identità documentale. La scelta è fra convenzioni testuali implicite e campi strutturati espliciti, conservando le sezioni di prosa DDTA leggibili.

## Decision

**Scelta candidata, da confermare prima di implementare:** usare Markdown come sorgente documentale; dichiarare tipo, ID, titolo, lifecycle e governance in un blocco di metadati strutturati, e rappresentare i campi narrativi come sezioni Markdown con nomi canonici. Per i metadati si propone *YAML front matter*; questa rappresentazione non è ancora approvata. I template per MR, Decision, FR, SpecializedRequirement, SecurityRequirement e BA devono derivare da schemi formalizzati e versionati, non da copie di template gestite separatamente per CLI e VS Code.

## Consequences

- Un documento deve dichiarare esplicitamente il proprio tipo; il nome del file può essere convenzionale, non l’unica fonte dell’identità.
- Gli schemi governano nomi dei campi, ordine suggerito, cardinalità, tipi e campi opzionali, preservando la distinzione fra regola accettata e candidata.
- La creazione di un template predispone la struttura, ma non inventa Intent, Context, Decision, normativeClause o BAProposition.
- Il contenuto Markdown deve restare leggibile per l’autore, non solo dal parser; la rappresentazione LaTeX/PDF verrà governata in MR-05.

## Questioni di review (non normative)

- YAML front matter oppure altra forma di metadati leggibili: scelta non ancora accettata.
- Un documento Markdown contiene solo la documentazione oppure anche una sezione BA canonica?
- Quale autorità governa le versioni degli schemi e cosa accade a documenti redatti con schemi precedenti?

## Base Analysis

**NOT YET AUTHORED.** Questo documento governa il commitment, non assegna in anticipo BAReferent, BAProposition o relazioni `realize`.
