# DDTA — Diffie-Hellman R5: contratti funzionali completi

**Stato:** revisione candidata del caso di studio (non modifica il DDTA CORE e non approva nuove classi).  
**Base:** grafo `dh_r4_baseline.ttl` della verifica R4.  
**Fonte della documentazione generata:** esclusivamente `dh_r5.ttl`.

## Scopo

Completare i contratti di **tutte le 15 funzioni** attualmente presenti nel caso di prova:

- 1 funzione complessiva `DiffieHellmanKeyAgreement`;
- 2 funzioni primarie (`PCKeyAgreement`, `UserKeyAgreement`);
- 12 sottofunzioni, incluse quattro `CommunicationFunction`.

Ogni funzione possiede un `hasInputContract` e un `hasOutputContract`, entrambi con `hasContractElement` e cardinalità `minOccurs`/`maxOccurs` esplicite. Nel caso risultano 30 associazioni Function→Contract e **28 Contract distinti**, perché i due contratti di attraversamento sono riutilizzati da mittente e destinatario:

- `PublicAOverChannel`: output di `PCSendPublic` e input di `UserReceivePublic`;
- `PublicBOverChannel`: output di `UserSendPublic` e input di `PCReceivePublic`.

Questa condivisione indica un **accordo sulla specifica di comunicazione**, non la consegna effettiva del dato o la sua integrità.

## File principali

- `dh_r5.ttl`: **grafo completo del caso R5**; conserva gli IRI della R4 per non scollegare le entità.
- `contracts_generated.md`: matrice di tutti i contratti e diagrammi Mermaid per i due sistemi.
- `contracts_PC.md`, `contracts_User.md`, `contracts_global.md`: viste Markdown per VS Code.
- `contracts_PC.mmd`, `contracts_User.mmd`, `contracts_global.mmd`: corrispondenti grafici Mermaid.
- `details/*.md` e `details/*.mmd`: 15 schede grafiche di dettaglio con archi `hasContractElement` espliciti.
- `steps_with_contracts_generated.md`: 16 Step/ControlNode ricostruiti dalle **transizioni RDF**, con contratti e guardie.
- `contract_elements_generated.csv`: esportazione di tutti i Function/Contract/ContractElement.
- `queries_r5.rq`: query SPARQL per recuperare contratti/elementi.
- `build_contracts_r5.py`: procedura di *authoring* che riparte dalla snapshot R4 e costruisce il Turtle R5.
- `verify_and_render_r5.py`: **legge** `dh_r5.ttl`, valida la completezza e rigenera viste e CSV.
- `render_steps_r5.py`: **legge** `dh_r5.ttl`, genera la tabella ordinata in base alle transizioni (ignorando `viz:localOrder`).
- `test_r5.py`: regressione con mutazioni negative.
- `dh_r4_baseline.ttl`: snapshot originale per confrontare il modello non contrattuale.
- `SHA256SUMS.txt`: hash di integrità dei file inclusi.

## Esecuzione in PowerShell

```powershell
$Zip = "$HOME\Downloads\DDTA_DH_CONTRACTS_R5.zip"
Expand-Archive -LiteralPath $Zip -DestinationPath "$HOME\Downloads" -Force
Set-Location "$HOME\Downloads\DDTA_DH_CONTRACTS_R5"

python -m pip install rdflib
python .\verify_and_render_r5.py
python .\render_steps_r5.py
python -m unittest -v test_r5
```

**Attenzione:** `build_contracts_r5.py` è usato soltanto per costruire la revisione a partire dalla R4. Non eseguirlo dopo aver modificato manualmente `dh_r5.ttl`: sovrascriverebbe le modifiche. I due renderer leggono il Turtle senza modificarlo.

## Decisioni preservate

- Il `ContractElement` è una specifica, non un valore runtime.
- `ReceivedA` e `ReceivedB` sono distinti dal contenuto atteso del canale: il dato potrebbe essere sostituito o alterato in un attacco.
- Il controllo matematica/validità non implica autenticazione del peer.
- `AcceptedAOptional` e `AcceptedBOptional` sono elementi `0..1`; i rispettivi ingressi delle funzioni di derivazione sono `AcceptedARequired` e `AcceptedBRequired`, elementi `1..1` **distinti** perché i vincoli contrattuali non coincidono.
- `EntropyPC` descrive l'input informativo di casualità richiesto alla generazione del segreto del PC. La risorsa RNG concreta non è ancora modellata.
- Nessuna procedura di gestione degli errori è stata inventata; restano i `?` già presenti nel grafo. Il caso di segreto digitato non valido è un gap ancora da inserire nel livello dei Process.
- Nessuna nuova proprietà `carries`, nessuna classe `Message`/`Transfer` e nessuna modifica a `DDTA_CORE.md` o alla bozza Process.

## Limiti della R5

1. La corrispondenza informativa fra output di validazione facoltativo e input obbligatorio della derivazione non è ancora espressa da una relazione formale; questa **non viene inferita** dalle somiglianze dei nomi.
2. Il predicato matematico completo e il legame tra `ValidityA/B` e guardie dei processi non sono formalizzati.
3. Gli scambi sono individuabili in modo univoco per **questo caso**, non è dimostrata una correlazione generale in presenza di ripetizioni o più scambi sullo stesso canale.
4. Non è stata eseguita una validazione dell'intera ontologia OWL/SHACL con relativo reasoning: i controlli qui sono RDFLib + verifiche strutturali Python e query SPARQL.
5. I comportamenti dei rami di errore sono esclusi, e non sono state introdotte nuove tecnologie di comunicazione o codice applicativo.
