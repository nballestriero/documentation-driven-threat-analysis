# DDTA Diffie-Hellman — prova deterministica R4

**Scopo:** verificare se, a partire da un unico grafo RDF, è possibile generare (1) un Mermaid dell'interazione, (2) un Mermaid del flusso con gap, (3) l'elenco dei ProcessStep con funzione, contratti e canali. **Non è ancora una descrizione definitiva delle ontologie né un'implementazione crittografica.**

## File

- `dh_r4.ttl`: grafo RDF del caso con due `System`, due `Environment`, due `Boundary`, due canali, funzioni, contratti, processi e sottoprocessi.
- `generate.py`: costruzione del caso, verifiche e generatori *che leggono il grafo*.
- `sequence_generated.mmd`: una possibile linearizzazione del flusso come Mermaid `sequenceDiagram`.
- `flow_generated.mmd`: i due ordini locali, la relazione di comunicazione e i gap `?`.
- `steps_generated.md` e `steps_generated.csv`: passaggi determinati dal grafo.

## Esecuzione

Requisito: Python 3.10+ e `rdflib` (`python -m pip install rdflib`).

```powershell
python .\generate.py
python .\generate.py --render-only
python .\generate.py --render-only --negative-test
```

`--render-only` **non costruisce o modifica** il Turtle: rilegge `dh_r4.ttl`, verifica i vincoli e rigenera le viste. È la prova più importante della separazione tra fonte RDF e visualizzazione. Il test negativo modifica il grafo soltanto in memoria, simula una transizione fra processi diversi e controlla che sia respinta.

## Come funziona il collegamento invio/ricezione

Per la specifica di comunicazione di A:

1. `PCSendPublic` è `CommunicationFunction`, usa `PCToUserChannel` e ha come **output** il contratto `PublicAOverChannel`.
2. `UserReceivePublic` è `CommunicationFunction`, usa lo **stesso canale** e ha come **input** `PublicAOverChannel`.
3. Il contratto identifica `PublicA` mediante `hasContractElement`.
4. L'associazione viene accettata se esistono precisamente una funzione di invio e una di ricezione, e se il canale è lo stesso. Il ruolo invio/ricezione è **metadato di vista** `viz:communicationRole`, non nuova proprietà CORE. Lo stesso vale in direzione opposta per `PublicBOverChannel`.
5. Ogni `ProcessStep` usa `proc:invokesProcess` per individuare il sottoprocesso, che a sua volta `ddta:realizesFunction` collega alla funzione di comunicazione. La sequenza si ricava dalle `ProcessTransition` **locali**.

La condivisione esplicita dell'identità del contratto è una convenzione **del caso di prova**, non una regola OWL secondo cui due contratti simili sono automaticamente lo stesso contratto. Per più invii sullo stesso canale o ripetizioni, la sola identità del contratto non distingue occorrenze individuali: servirà un'identificazione ulteriore dello scambio nella specializzazione Process, non necessariamente una nuova classe `Message` nel CORE.

## Condizioni e gap

I nodi `PCPublicValidityDecision` e `UserPublicValidityDecision` sono `proc:ControlNode`. Le transizioni verso il percorso nominale hanno `proc:hasGuard` con una `AtomicCondition`; `Operand` riferisce il `ContractElement` dell'informazione ricevuta. I nodi `?` sono `viz:DocumentationGap` e **non** `ProcessStep`; la relazione `viz:unresolvedFalseBranch` indica il ramo non documentato senza inventare l'azione da eseguire. Questo è un metadato documentale di esempio che andrà collegato al meccanismo ufficiale dei gap DDTA.

La condizione è volutamente **solo identificata semanticamente**: non è ancora stata formalizzata la regola di validazione matematica del valore pubblico. Non è una verifica di provenienza o autenticità: il Diffie-Hellman non autenticato resta vulnerabile a MITM.

## Limiti deliberati

- `hasSubProcess` è la relazione approvata nella discussione; `invokesProcess`, `ProcessTransition`, `ControlNode`, `Operand`, `hasGuard` sono parti candidate dell'estensione Process.
- `viz:*` è un namespace **ausiliario per la prova**, non un aggiornamento di DDTA CORE o della Process Ontology: `viz:localOrder` serve soltanto a presentare un'etichetta di ordine per Step (l'ordine effettivo viene verificato dalle transizioni), `viz:initialStep`, `viz:communicationRole`, `viz:unresolvedFalseBranch` sono metadati dichiarati esplicitamente. Nessuna proprietà è inferita tacitamente.
- Non è ancora un generatore generale per qualsiasi ontologia. Funziona per due processi, ognuno con un percorso nominale aciclico, e due scambi. Quando il grafo è ambiguo o incoerente i validatori rifiutano anziché inventare relazioni.
- Il `sequenceDiagram` mostra **una linearizzazione deterministica valida**, non un ordine globale obbligatorio. Per la concorrenza e i rami affidarsi al `flow_generated.mmd`.
- Non è documentato il comportamento dei rami di errore. Non è definito un protocollo di autenticazione. Nessuna modifica al repository.
