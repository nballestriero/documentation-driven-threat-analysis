# DEC-MR02-02 — Diagnostiche strutturate e profili di controllo

**Parent MacroRequirement:** `MR-02`\
**Lifecycle:** `candidate`\
**Authority:** `EXPERIMENTAL_NON_CANONICAL`\
**Decision kind:** `SELECTABLE` *(classificazione di review)*

## Context

Durante la redazione un documento può contenere campi ancora da compilare, mentre una verifica conclusiva deve rilevare tutte le incompletezze formalmente vietate. Inoltre un risultato utile a CLI, editor e agenti AI deve essere interpretato senza dipendere dalla presentazione grafica o da messaggi non strutturati. Occorre scegliere come rappresentare la diagnostica e differenziare l'uso in bozza dal controllo conclusivo.

## Decision

**Commitment progettuale candidato:** restituire diagnostiche strutturate e indipendenti dall'interfaccia, comprensive di identificativo della regola, posizione nel sorgente quando disponibile, severità e descrizione. Distinguere un profilo `draft` per documenti in elaborazione e un profilo `strict` per la verifica conclusiva. Il profilo può variare la severità delle incompletezze attese durante l'authoring, ma non rendere valida una struttura non interpretabile, un metadato ambiguo o una violazione formale che impedisce la corretta identificazione del documento.

Il servizio produce i risultati; le interfacce li presentano, senza reinterpretare o duplicare le regole. Nessuna diagnostica comporta di per sé una correzione automatica o l'accettazione semantica del contenuto.

## Consequences

- CLI, editor e client automatici possono consumare lo stesso esito diagnostico e rappresentarlo nel rispettivo ambiente.
- Una bozza incompleta può essere distinta da un documento formalmente conforme, senza che la modalità `draft` nasconda errori di interpretazione.
- Gli errori possono essere associati alle porzioni interessate del sorgente, quando tali posizioni sono note.
- La diagnostica non approva contenuti, non modifica il documento e preserva la distinzione tra controllo formale e review semantica.

## Questioni di review (non normative)

- Definire schema esatto del risultato, codici diagnostici, severità e posizionamento nel testo Markdown.
- Precisare quando una violazione resta errore anche in `draft` e quando una incompletezza può essere un avviso.
- Definire se e come suggerire correzioni senza applicarle automaticamente.

## Base Analysis

**NOT YET AUTHORED.** Nessuna relazione BA è dedotta dalla scelta del formato diagnostico.
