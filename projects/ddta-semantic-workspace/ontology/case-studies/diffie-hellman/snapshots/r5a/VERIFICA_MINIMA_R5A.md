# DDTA / Diffie-Hellman — verifica minima di rappresentabilità R5A

**Scopo.** Verificare che le ontologie CORE e Process, applicate a un caso Diffie-Hellman con due sistemi, rappresentino funzioni, input/output, comunicazioni, ordine previsto, controlli e confini di trust. Non dimostrare la correttezza crittografica, la sicurezza del protocollo o l'aderenza di un'implementazione.

## Punto corretto nella R5

La condizione `PCPeerPublicValid` ora ha come operando un `Operand` che riferisce `ValidityB`, elemento del contratto di uscita di `PCValidatePublic`. Analogamente, `UserPeerPublicValid` fa riferimento a `ValidityA`, prodotto da `UserValidatePublic`.

Prima, le condizioni puntavano direttamente agli elementi `ReceivedB` e `ReceivedA`. Quel riferimento descriveva il dato ricevuto, non l'esito della sua verifica.

La correzione **non** cambia processi, strutture delle sottofunzioni, contratti, canali, transizioni, Boundary o gap. Fra R5 e R5A: 8 triple rimosse, 10 aggiunte (596 triple in R5A, contro 594).

## Ricostruzione nominale

- Due `System` distinti (`PCSystem`, `UserSystem`) con due `Environment`, due `Boundary` e due `Resource` endpoint.
- Due `Process` principali che `realizesFunction` le rispettive funzioni primarie; sei sottoprocessi per sistema, ciascuno collegato alla propria funzione.
- Quindici `Function` considerate, tutte con contratti input e output; contenuto di comunicazione `PublicA` e `PublicB` ottenibile attraverso contratti condivisi, con due `CommunicationChannel` direzionali.
- Le `ProcessTransition` rispettano la proprietà di appartenenza di entrambi gli estremi al processo proprietario; `ProcessStep --invokesProcess--> Process --realizesFunction--> Function` collega il COME al COSA.
- I due rami nominali che abilitano la prosecuzione della derivazione sono collegati a condizioni che si riferiscono agli **esiti** di validazione. I due rami negativi sono esplicitamente marcati `?` come `DocumentationGap`, non inventano azioni di errore.

## Limiti deliberatamente aperti

1. La condizione è collegata all'elemento funzionale `ValidityA`/`ValidityB`, ma l'operatore formale `= true` **non è ancora rappresentato** con una espressione completa di `AtomicCondition`. `viz:guardExpected "true"` rimane un metadato di vista, non una regola eseguibile o un assioma logico.
2. Una verifica matematica del valore pubblico **non autentica il mittente**, né garantisce l'integrità della comunicazione. La possibilità MITM resta una questione rilevante per l'analisi di sicurezza successiva.
3. La relazione tra `AcceptedBOptional`/`AcceptedAOptional` (output facoltativo della validazione) e i corrispondenti input necessari alla derivazione non è ancora formalizzata completamente. Per lo scopo presente basta che **l'esito di validazione sia esplicito e la derivazione risulti sul ramo positivo**.
4. Il caso di valore privato da tastiera non valido non ha ancora il proprio gap esplicito nella R5 e non viene aggiunto qui, per evitare di ampliare l'ambito.
5. Questa è una verifica strutturale RDF mediante Python (`rdflib`), non una verifica di esecuzione del protocollo, né validazione OWL/SHACL complessiva.

## Ripetizione

```powershell
python -m pip install rdflib
python .\verify_minimal.py
```

Risultati ottenuti: **596 triple RDF**, **107 asserzioni strutturali riuscite** e **un test negativo riuscito**, che reintroduce appositamente un riferimento a `ReceivedB` nella condizione PC e viene rifiutato.

## Esito e prossima decisione

**Obiettivo limitato raggiunto:** la rappresentazione contiene i collegamenti ontologici necessari per descrivere il comportamento nominale dei due partecipanti e per individuare i punti in cui dati esterni attraversano confini di trust e vengono controllati.

**Non ancora dimostrato:** che un generatore generico ricostruisca *ogni* protocollo senza convenzioni aggiuntive; che la logica delle condizioni sia formalmente completa; che Diffie-Hellman sia sicuro contro attacchi attivi. Questi temi non sono prerequisiti per considerare utile il caso come test di rappresentabilità.

Nessuna modifica al repository; R5 resta intatta e R5A è una copia corretta per revisione.
