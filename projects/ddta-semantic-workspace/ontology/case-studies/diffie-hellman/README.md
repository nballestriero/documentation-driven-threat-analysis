# DDTA — Diffie-Hellman, caso di studio ontologico

**Stato: BOZZA / DA REVISIONARE.** Questa directory conserva un caso di studio separato dall'ontologia CORE definitiva. Non vengono aggiornati `DDTA_CORE.md`, eventuali `core.ttl` e `process.ttl` già presenti nel repository.

## Quali file aprire

1. `DDTA_DH_PROTOCOL_DRAFT_R1.md`: ragionamento e descrizione dell'intero protocollo, COSA/COME, sicurezza, limiti e decisioni.
2. `DDTA_DH_INSTANCE_SHEETS_R1.md`: **tutte le schede delle istanze** ricavate dal Turtle candidato, da revisionare in seguito.
3. `model/dh_r5a.ttl`: **fotografia RDF di lavoro corrente** del caso, non ontologia definitiva.
4. `generated/PC_process.md`, `generated/User_process.md`, `generated/architecture.md`, `generated/function_tree.md`: grafici Mermaid apribili in VS Code, generati dal Turtle.
5. `generated/steps_from_rdf.md`: tutti gli Step/ControlNode sul percorso nominale, con contratti e gap.
6. `SCHEDE_PROCESS_CANDIDATE_R1.md`: sole **schede di impatto** sulla Process Ontology; non affermazioni normative.
7. `context/DDTA_PROCESS_DRAFT_R1.md`: bozza generale Process già preparata, preservata come riferimento; separata dal caso.

## Snapshot storiche, non baseline corrente

- `snapshots/r4/`: prototipo di generazione Mermaid/traccia e diagnosi della R4.
- `snapshots/r5/`: completamento dei contratti funzionali e relative viste/test.
- `snapshots/r5a/`: verifica limitata e correzione degli operandi delle condizioni verso `ValidityA`/`ValidityB`.

Le snapshot sono preservate per ricostruire le decisioni. **La baseline da cui ripartire è `model/dh_r5a.ttl`.** Le altre copie del Turtle non devono essere confuse con la baseline né usate per aggiornare automaticamente le schede.

## Riprodurre la verifica (PowerShell)

```powershell
Set-Location 'projects/ddta-semantic-workspace/ontology/case-studies/diffie-hellman'
python -m pip install rdflib
python .	oolserify_minimal.py
python .	oolsender_case.py
```

Il validatore esegue i controlli minimi strutturali e la mutazione negativa; il renderer **legge** il Turtle e rigenera schede e viste, senza modificare il modello. La verifica non esegue Diffie-Hellman, non verifica la sicurezza, non esegue reasoning OWL o validazione SHACL completa.

## Convenzione di modifica

Le schede `DDTA_DH_INSTANCE_SHEETS_R1.md` sono attualmente un **riflesso generato** dell'RDF. In fase di revisione delle schede, annotare correzioni in `DDTA_DH_PROTOCOL_DRAFT_R1.md` o una nuova revisione esplicita; una volta approvate, applicarle al Turtle candidato e rigenerare le viste. Modifiche manuali ai grafici generati andrebbero perse alla rigenerazione.

Gli IRI `https://example.org/ddta/dh-deterministic-r4#` e `https://example.org/ddta/view#` sono **illustrativi/ausiliari** e da rivedere prima del consolidamento definitivo del Turtle.
