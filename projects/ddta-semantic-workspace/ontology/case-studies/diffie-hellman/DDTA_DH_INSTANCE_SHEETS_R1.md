# DDTA Diffie-Hellman — schede delle istanze RDF, R5A

> **GENERATO dal Turtle, non normativo.** Modificare `model/dh_r5a.ttl`, quindi rigenerare con `python tools/render_case.py`. Non inserire in questa scheda relazioni che non figurano nel grafo.

## 1. Schede architetturali

### Environment

#### PCEnvironment

- **Classe:** `Environment`
- **Etichetta:** PCEnvironment
- **makesAvailable**: `PCEndpoint`

#### UserEnvironment

- **Classe:** `Environment`
- **Etichetta:** UserEnvironment
- **makesAvailable**: `UserEndpoint`

### System

#### PCSystem

- **Classe:** `System`
- **Etichetta:** PCSystem
- **hasOperationalEnvironment**: `PCEnvironment`
- **hasPrimaryFunction**: `PCKeyAgreement`
- **hasBoundary**: `PCBoundary`

#### UserSystem

- **Classe:** `System`
- **Etichetta:** UserSystem
- **hasOperationalEnvironment**: `UserEnvironment`
- **hasPrimaryFunction**: `UserKeyAgreement`
- **hasBoundary**: `UserBoundary`

### Boundary

#### PCBoundary

- **Classe:** `Boundary`
- **Etichetta:** PC trust boundary
- **encloses**: `PCEndpoint`

#### UserBoundary

- **Classe:** `Boundary`
- **Etichetta:** User trust boundary
- **encloses**: `UserEndpoint`

### Resource

#### PCEndpoint

- **Classe:** `Resource`
- **Etichetta:** PC logical endpoint

#### UserEndpoint

- **Classe:** `Resource`
- **Etichetta:** User logical endpoint

### CommunicationChannel

#### PCToUserChannel

- **Classe:** `CommunicationChannel`
- **Etichetta:** PC → User
- **hasSource**: `PCEndpoint`
- **hasDestination**: `UserEndpoint`

#### UserToPCChannel

- **Classe:** `CommunicationChannel`
- **Etichetta:** User → PC
- **hasSource**: `UserEndpoint`
- **hasDestination**: `PCEndpoint`

## 2. Schede Function: input, output e gerarchia

### DiffieHellmanKeyAgreement

- **Classe:** `Function`
- **Etichetta:** Diffie-Hellman · bilateral key agreement
- **hasSubFunction:** `PCKeyAgreement`, `UserKeyAgreement`
- **hasInputContract:** `DiffieHellmanKeyAgreementInputContract` → `EnteredB`, `GeneratorG`, `ModulusP`, `SubgroupOrderQ`
- **hasOutputContract:** `DiffieHellmanKeyAgreementOutputContract` → `PublicA`, `PublicB`, `SharedKPC`, `SharedKUser`

### PCCalculatePublic

- **Classe:** `Function`
- **Etichetta:** Calcola A
- **Sottofunzione di:** `PCKeyAgreement`
- **mustPrecede:** `PCSendPublic`
- **hasInputContract:** `PCCalculatePublicInputContract` → `GeneratorG`, `ModulusP`, `PrivateA`
- **hasOutputContract:** `PCCalculatePublicOutputContract` → `PublicA`

### PCDeriveSecret

- **Classe:** `Function`
- **Etichetta:** Deriva K_PC
- **Sottofunzione di:** `PCKeyAgreement`
- **hasInputContract:** `PCDeriveSecretInputContract` → `AcceptedBRequired`, `ModulusP`, `PrivateA`
- **hasOutputContract:** `PCDeriveSecretOutputContract` → `SharedKPC`

### PCGeneratePrivate

- **Classe:** `Function`
- **Etichetta:** Genera segreto a
- **Sottofunzione di:** `PCKeyAgreement`
- **mustPrecede:** `PCCalculatePublic`, `PCDeriveSecret`
- **hasInputContract:** `PCGeneratePrivateInputContract` → `EntropyPC`, `ModulusP`, `SubgroupOrderQ`
- **hasOutputContract:** `PCGeneratePrivateOutputContract` → `PrivateA`

### PCKeyAgreement

- **Classe:** `Function`
- **Etichetta:** PCKeyAgreement
- **Sottofunzione di:** `DiffieHellmanKeyAgreement`
- **hasSubFunction:** `PCCalculatePublic`, `PCDeriveSecret`, `PCGeneratePrivate`, `PCReceivePublic`, `PCSendPublic`, `PCValidatePublic`
- **hasInputContract:** `PCKeyAgreementInputContract` → `GeneratorG`, `ModulusP`, `PublicB`, `SubgroupOrderQ`
- **hasOutputContract:** `PCKeyAgreementOutputContract` → `PublicA`, `SharedKPC`

### PCReceivePublic

- **Classe:** `CommunicationFunction`
- **Etichetta:** Riceve B
- **Sottofunzione di:** `PCKeyAgreement`
- **mustPrecede:** `PCValidatePublic`
- **usesChannel:** `UserToPCChannel`
- **Ruolo comunicazione (viz, ausiliario):** receive
- **hasInputContract:** `PublicBOverChannel` → `PublicB`
- **hasOutputContract:** `PCReceivePublicOutputContract` → `ReceivedB`

### PCSendPublic

- **Classe:** `CommunicationFunction`
- **Etichetta:** Invia A
- **Sottofunzione di:** `PCKeyAgreement`
- **usesChannel:** `PCToUserChannel`
- **Ruolo comunicazione (viz, ausiliario):** send
- **hasInputContract:** `PCSendPublicInputContract` → `PublicA`
- **hasOutputContract:** `PublicAOverChannel` → `PublicA`

### PCValidatePublic

- **Classe:** `Function`
- **Etichetta:** Verifica validità B
- **Sottofunzione di:** `PCKeyAgreement`
- **mustPrecede:** `PCDeriveSecret`
- **hasInputContract:** `PCValidatePublicInputContract` → `GeneratorG`, `ModulusP`, `ReceivedB`, `SubgroupOrderQ`
- **hasOutputContract:** `PCValidatePublicOutputContract` → `AcceptedBOptional`, `ValidityB`

### UserAcquirePrivate

- **Classe:** `Function`
- **Etichetta:** Acquisisce segreto b
- **Sottofunzione di:** `UserKeyAgreement`
- **mustPrecede:** `UserCalculatePublic`, `UserDeriveSecret`
- **hasInputContract:** `UserAcquirePrivateInputContract` → `EnteredB`, `ModulusP`, `SubgroupOrderQ`
- **hasOutputContract:** `UserAcquirePrivateOutputContract` → `PrivateB`

### UserCalculatePublic

- **Classe:** `Function`
- **Etichetta:** Calcola B
- **Sottofunzione di:** `UserKeyAgreement`
- **mustPrecede:** `UserSendPublic`
- **hasInputContract:** `UserCalculatePublicInputContract` → `GeneratorG`, `ModulusP`, `PrivateB`
- **hasOutputContract:** `UserCalculatePublicOutputContract` → `PublicB`

### UserDeriveSecret

- **Classe:** `Function`
- **Etichetta:** Deriva K_User
- **Sottofunzione di:** `UserKeyAgreement`
- **hasInputContract:** `UserDeriveSecretInputContract` → `AcceptedARequired`, `ModulusP`, `PrivateB`
- **hasOutputContract:** `UserDeriveSecretOutputContract` → `SharedKUser`

### UserKeyAgreement

- **Classe:** `Function`
- **Etichetta:** UserKeyAgreement
- **Sottofunzione di:** `DiffieHellmanKeyAgreement`
- **hasSubFunction:** `UserAcquirePrivate`, `UserCalculatePublic`, `UserDeriveSecret`, `UserReceivePublic`, `UserSendPublic`, `UserValidatePublic`
- **hasInputContract:** `UserKeyAgreementInputContract` → `EnteredB`, `GeneratorG`, `ModulusP`, `PublicA`, `SubgroupOrderQ`
- **hasOutputContract:** `UserKeyAgreementOutputContract` → `PublicB`, `SharedKUser`

### UserReceivePublic

- **Classe:** `CommunicationFunction`
- **Etichetta:** Riceve A
- **Sottofunzione di:** `UserKeyAgreement`
- **mustPrecede:** `UserValidatePublic`
- **usesChannel:** `PCToUserChannel`
- **Ruolo comunicazione (viz, ausiliario):** receive
- **hasInputContract:** `PublicAOverChannel` → `PublicA`
- **hasOutputContract:** `UserReceivePublicOutputContract` → `ReceivedA`

### UserSendPublic

- **Classe:** `CommunicationFunction`
- **Etichetta:** Invia B
- **Sottofunzione di:** `UserKeyAgreement`
- **usesChannel:** `UserToPCChannel`
- **Ruolo comunicazione (viz, ausiliario):** send
- **hasInputContract:** `UserSendPublicInputContract` → `PublicB`
- **hasOutputContract:** `PublicBOverChannel` → `PublicB`

### UserValidatePublic

- **Classe:** `Function`
- **Etichetta:** Verifica validità A
- **Sottofunzione di:** `UserKeyAgreement`
- **mustPrecede:** `UserDeriveSecret`
- **hasInputContract:** `UserValidatePublicInputContract` → `GeneratorG`, `ModulusP`, `ReceivedA`, `SubgroupOrderQ`
- **hasOutputContract:** `UserValidatePublicOutputContract` → `AcceptedAOptional`, `ValidityA`

## 3. Schede Contract

### DiffieHellmanKeyAgreementInputContract

- **Classe:** `Contract`
- **Definizione:** DiffieHellmanKeyAgreement/input: Specificazione bilaterale: due sistemi indipendenti utilizzano parametri compatibili. Il PC genera internamente a; b è acquisito dall’utente. Nessun segreto privato è comunicato.
- **Usato in input da:** `DiffieHellmanKeyAgreement`
- **Usato in output da:** —
- **hasContractElement:** `EnteredB`, `GeneratorG`, `ModulusP`, `SubgroupOrderQ`

### DiffieHellmanKeyAgreementOutputContract

- **Classe:** `Contract`
- **Definizione:** DiffieHellmanKeyAgreement/output: Risultati locali nominali; con scambio integro e valori validi K_PC = K_User. Il contratto NON garantisce autenticità o resistenza a MITM.
- **Usato in input da:** —
- **Usato in output da:** `DiffieHellmanKeyAgreement`
- **hasContractElement:** `PublicA`, `PublicB`, `SharedKPC`, `SharedKUser`

### PCCalculatePublicInputContract

- **Classe:** `Contract`
- **Definizione:** PCCalculatePublic/input: Calcola A = g^a mod p.
- **Usato in input da:** `PCCalculatePublic`
- **Usato in output da:** —
- **hasContractElement:** `GeneratorG`, `ModulusP`, `PrivateA`

### PCCalculatePublicOutputContract

- **Classe:** `Contract`
- **Definizione:** PCCalculatePublic/output: A è pubblicabile.
- **Usato in input da:** —
- **Usato in output da:** `PCCalculatePublic`
- **hasContractElement:** `PublicA`

### PCDeriveSecretInputContract

- **Classe:** `Contract`
- **Definizione:** PCDeriveSecret/input: Richiede il valore remoto accettato; l’obbligatorietà riguarda il percorso nominale valido.
- **Usato in input da:** `PCDeriveSecret`
- **Usato in output da:** —
- **hasContractElement:** `AcceptedBRequired`, `ModulusP`, `PrivateA`

### PCDeriveSecretOutputContract

- **Classe:** `Contract`
- **Definizione:** PCDeriveSecret/output: Produce K_PC soltanto localmente.
- **Usato in input da:** —
- **Usato in output da:** `PCDeriveSecret`
- **hasContractElement:** `SharedKPC`

### PCGeneratePrivateInputContract

- **Classe:** `Contract`
- **Definizione:** PCGeneratePrivate/input: Usa un generatore casuale adeguato, risorsa di realizzazione non descritta come ContractElement. Vincolo di intervallo determinato dai parametri del gruppo.
- **Usato in input da:** `PCGeneratePrivate`
- **Usato in output da:** —
- **hasContractElement:** `EntropyPC`, `ModulusP`, `SubgroupOrderQ`

### PCGeneratePrivateOutputContract

- **Classe:** `Contract`
- **Definizione:** PCGeneratePrivate/output: Produce a senza comunicarlo.
- **Usato in input da:** —
- **Usato in output da:** `PCGeneratePrivate`
- **hasContractElement:** `PrivateA`

### PCKeyAgreementInputContract

- **Classe:** `Contract`
- **Definizione:** PCKeyAgreement/input: Il valore B è richiesto come informazione remota ricevibile; a è generato internamente dalla sottofunzione dedicata.
- **Usato in input da:** `PCKeyAgreement`
- **Usato in output da:** —
- **hasContractElement:** `GeneratorG`, `ModulusP`, `PublicB`, `SubgroupOrderQ`

### PCKeyAgreementOutputContract

- **Classe:** `Contract`
- **Definizione:** PCKeyAgreement/output: A è esposto al peer tramite CommunicationFunction; K_PC rimane locale. L’uscita segreta è prevista sul percorso nominale valido.
- **Usato in input da:** —
- **Usato in output da:** `PCKeyAgreement`
- **hasContractElement:** `PublicA`, `SharedKPC`

### PCReceivePublicOutputContract

- **Classe:** `Contract`
- **Definizione:** PCReceivePublic/output: ReceivedB è il dato ricevuto grezzo: non è ancora validato né autenticato.
- **Usato in input da:** —
- **Usato in output da:** `PCReceivePublic`
- **hasContractElement:** `ReceivedB`

### PCSendPublicInputContract

- **Classe:** `Contract`
- **Definizione:** PCSendPublic/input: Input locale: A già calcolato. La CommunicationFunction utilizza PCToUserChannel.
- **Usato in input da:** `PCSendPublic`
- **Usato in output da:** —
- **hasContractElement:** `PublicA`

### PCValidatePublicInputContract

- **Classe:** `Contract`
- **Definizione:** PCValidatePublic/input: Controlla validità matematica secondo i parametri concordati; predicato specifico non ancora formalizzato. Non verifica l’identità del peer.
- **Usato in input da:** `PCValidatePublic`
- **Usato in output da:** —
- **hasContractElement:** `GeneratorG`, `ModulusP`, `ReceivedB`, `SubgroupOrderQ`

### PCValidatePublicOutputContract

- **Classe:** `Contract`
- **Definizione:** PCValidatePublic/output: Fornisce sempre l’esito ValidityB; fornisce AcceptedBOptional solo sul percorso valido. Il ramo non valido resta ? documentale.
- **Usato in input da:** —
- **Usato in output da:** `PCValidatePublic`
- **hasContractElement:** `AcceptedBOptional`, `ValidityB`

### PublicAOverChannel

- **Classe:** `Contract`
- **Definizione:** PCSendPublic/output: Contratto condiviso PublicAOverChannel: A è previsto come informazione inviata, non prova di ricezione.
- **Usato in input da:** `UserReceivePublic`
- **Usato in output da:** `PCSendPublic`
- **hasContractElement:** `PublicA`

### PublicBOverChannel

- **Classe:** `Contract`
- **Definizione:** PCReceivePublic/input: Contratto condiviso PublicBOverChannel: ci si aspetta B, ma il contenuto concretamente ricevuto potrebbe essere B_r diverso.
- **Usato in input da:** `PCReceivePublic`
- **Usato in output da:** `UserSendPublic`
- **hasContractElement:** `PublicB`

### UserAcquirePrivateInputContract

- **Classe:** `Contract`
- **Definizione:** UserAcquirePrivate/input: L’utente inserisce un valore privato candidato; il contratto richiede che sia accettabile secondo i vincoli del gruppo.
- **Usato in input da:** `UserAcquirePrivate`
- **Usato in output da:** —
- **hasContractElement:** `EnteredB`, `ModulusP`, `SubgroupOrderQ`

### UserAcquirePrivateOutputContract

- **Classe:** `Contract`
- **Definizione:** UserAcquirePrivate/output: PrivateB è prodotto soltanto se il candidato è accettato. Il comportamento per input non valido non è ancora documentato (?).
- **Usato in input da:** —
- **Usato in output da:** `UserAcquirePrivate`
- **hasContractElement:** `PrivateB`

### UserCalculatePublicInputContract

- **Classe:** `Contract`
- **Definizione:** UserCalculatePublic/input: Calcola B = g^b mod p.
- **Usato in input da:** `UserCalculatePublic`
- **Usato in output da:** —
- **hasContractElement:** `GeneratorG`, `ModulusP`, `PrivateB`

### UserCalculatePublicOutputContract

- **Classe:** `Contract`
- **Definizione:** UserCalculatePublic/output: B è pubblicabile.
- **Usato in input da:** —
- **Usato in output da:** `UserCalculatePublic`
- **hasContractElement:** `PublicB`

### UserDeriveSecretInputContract

- **Classe:** `Contract`
- **Definizione:** UserDeriveSecret/input: Richiede il valore remoto accettato; l’obbligatorietà riguarda il percorso nominale valido.
- **Usato in input da:** `UserDeriveSecret`
- **Usato in output da:** —
- **hasContractElement:** `AcceptedARequired`, `ModulusP`, `PrivateB`

### UserDeriveSecretOutputContract

- **Classe:** `Contract`
- **Definizione:** UserDeriveSecret/output: Produce K_User soltanto localmente.
- **Usato in input da:** —
- **Usato in output da:** `UserDeriveSecret`
- **hasContractElement:** `SharedKUser`

### UserKeyAgreementInputContract

- **Classe:** `Contract`
- **Definizione:** UserKeyAgreement/input: L’operatore fornisce il valore privato candidato b; A è la specifica del valore pubblico atteso dall’altro partecipante.
- **Usato in input da:** `UserKeyAgreement`
- **Usato in output da:** —
- **hasContractElement:** `EnteredB`, `GeneratorG`, `ModulusP`, `PublicA`, `SubgroupOrderQ`

### UserKeyAgreementOutputContract

- **Classe:** `Contract`
- **Definizione:** UserKeyAgreement/output: B è esposto al peer tramite CommunicationFunction; K_User rimane locale. L’uscita segreta è prevista sul percorso nominale valido.
- **Usato in input da:** —
- **Usato in output da:** `UserKeyAgreement`
- **hasContractElement:** `PublicB`, `SharedKUser`

### UserReceivePublicOutputContract

- **Classe:** `Contract`
- **Definizione:** UserReceivePublic/output: ReceivedA è il dato ricevuto grezzo: non è ancora validato né autenticato.
- **Usato in input da:** —
- **Usato in output da:** `UserReceivePublic`
- **hasContractElement:** `ReceivedA`

### UserSendPublicInputContract

- **Classe:** `Contract`
- **Definizione:** UserSendPublic/input: Input locale: B già calcolato. La CommunicationFunction utilizza UserToPCChannel.
- **Usato in input da:** `UserSendPublic`
- **Usato in output da:** —
- **hasContractElement:** `PublicB`

### UserValidatePublicInputContract

- **Classe:** `Contract`
- **Definizione:** UserValidatePublic/input: Controlla validità matematica del valore remoto ricevuto; predicato non formalizzato. Non verifica provenienza o autenticità.
- **Usato in input da:** `UserValidatePublic`
- **Usato in output da:** —
- **hasContractElement:** `GeneratorG`, `ModulusP`, `ReceivedA`, `SubgroupOrderQ`

### UserValidatePublicOutputContract

- **Classe:** `Contract`
- **Definizione:** UserValidatePublic/output: Fornisce sempre ValidityA; fornisce AcceptedAOptional solo sul percorso valido. Il ramo non valido resta ? documentale.
- **Usato in input da:** —
- **Usato in output da:** `UserValidatePublic`
- **hasContractElement:** `AcceptedAOptional`, `ValidityA`

## 4. Schede ContractElement e cardinalità

| Elemento | Significato | Definizione | minOccurs | maxOccurs |
|---|---|---|---:|---:|
| `AcceptedAOptional` | A_r accettato (se valido) | Dato remoto accettato come matematicamente valido, disponibile soltanto sul percorso valido. | 0 | 1 |
| `AcceptedARequired` | A_r accettato (richiesto) | Dato remoto già accettato, richiesto dal calcolo del segreto nell’ambiente utente. | 1 | 1 |
| `AcceptedBOptional` | B_r accettato (se valido) | Dato remoto accettato come matematicamente valido, disponibile soltanto sul percorso valido. | 0 | 1 |
| `AcceptedBRequired` | B_r accettato (richiesto) | Dato remoto già accettato, richiesto dal calcolo del segreto nell’ambiente PC. | 1 | 1 |
| `EnteredB` | Valore b digitato | Valore privato candidato fornito dall’operatore umano; non ancora accettato. | 1 | 1 |
| `EntropyPC` | Materiale casuale imprevedibile | Input informativo richiesto per la generazione di a; la sua fornitura dipende da una risorsa RNG da modellare successivamente. | 1 | 1 |
| `GeneratorG` | Generatore g | Generatore pubblico compatibile con il gruppo concordato. | 1 | 1 |
| `ModulusP` | Modulus p | Parametro pubblico del gruppo Diffie-Hellman, modulo p. | 1 | 1 |
| `PrivateA` | Segreto privato a | Esponente privato del PC; rimane nel proprio dominio di trust. | 1 | 1 |
| `PrivateB` | Segreto privato b | Esponente privato accettato dall’ambiente utente; non trasmesso al peer. | 1 | 1 |
| `PublicA` | Valore pubblico A | Valore pubblico g^a mod p specificato per il canale PC→User. | 1 | 1 |
| `PublicB` | Valore pubblico B | Valore pubblico g^b mod p specificato per il canale User→PC. | 1 | 1 |
| `ReceivedA` | Valore ricevuto A_r | Dato ricevuto come presunto A; potrebbe differire da A per alterazioni o sostituzione. | 1 | 1 |
| `ReceivedB` | Valore ricevuto B_r | Dato ricevuto come presunto B; potrebbe differire da B per alterazioni o sostituzione. | 1 | 1 |
| `SharedKPC` | Segreto condiviso K_PC | Segreto derivato localmente nel PC; non trasferito sul canale. | 1 | 1 |
| `SharedKUser` | Segreto condiviso K_User | Segreto derivato localmente nel sistema utente; non trasferito sul canale. | 1 | 1 |
| `SubgroupOrderQ` | Ordine q (se applicabile) | Ordine del sottogruppo, quando richiesto dai parametri adottati. | 0 | 1 |
| `ValidityA` | Esito validità A_r | Esito della verifica di validità matematica del valore remoto A_r; non autenticità. | 1 | 1 |
| `ValidityB` | Esito validità B_r | Esito della verifica di validità matematica del valore remoto B_r; non autenticità. | 1 | 1 |

## 5. Schede Process e sottoprocessi

### PCCalculatePublicProcess

- **realizesFunction:** `PCCalculatePublic`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

### PCDeriveSecretProcess

- **realizesFunction:** `PCDeriveSecret`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

### PCGeneratePrivateProcess

- **realizesFunction:** `PCGeneratePrivate`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

### PCProcess

- **realizesFunction:** `PCKeyAgreement`
- **hasSubProcess (candidata approvata):** `PCCalculatePublicProcess`, `PCDeriveSecretProcess`, `PCGeneratePrivateProcess`, `PCReceivePublicProcess`, `PCSendPublicProcess`, `PCValidatePublicProcess`
- **hasStep:** `PCCalculatePublicStep`, `PCDeriveSecretStep`, `PCEnd`, `PCGeneratePrivateStep`, `PCPublicValidityDecision`, `PCReceivePublicStep`, `PCSendPublicStep`, `PCValidatePublicStep`
- **hasTransition (Process):** `PCTransition01`, `PCTransition02`, `PCTransition03`, `PCTransition04`, `PCTransition05`, `PCTransition06`, `PCTransition07`

### PCReceivePublicProcess

- **realizesFunction:** `PCReceivePublic`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

### PCSendPublicProcess

- **realizesFunction:** `PCSendPublic`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

### PCValidatePublicProcess

- **realizesFunction:** `PCValidatePublic`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

### UserAcquirePrivateProcess

- **realizesFunction:** `UserAcquirePrivate`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

### UserCalculatePublicProcess

- **realizesFunction:** `UserCalculatePublic`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

### UserDeriveSecretProcess

- **realizesFunction:** `UserDeriveSecret`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

### UserProcess

- **realizesFunction:** `UserKeyAgreement`
- **hasSubProcess (candidata approvata):** `UserAcquirePrivateProcess`, `UserCalculatePublicProcess`, `UserDeriveSecretProcess`, `UserReceivePublicProcess`, `UserSendPublicProcess`, `UserValidatePublicProcess`
- **hasStep:** `UserAcquirePrivateStep`, `UserCalculatePublicStep`, `UserDeriveSecretStep`, `UserEnd`, `UserPublicValidityDecision`, `UserReceivePublicStep`, `UserSendPublicStep`, `UserValidatePublicStep`
- **hasTransition (Process):** `UserTransition01`, `UserTransition02`, `UserTransition03`, `UserTransition04`, `UserTransition05`, `UserTransition06`, `UserTransition07`

### UserReceivePublicProcess

- **realizesFunction:** `UserReceivePublic`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

### UserSendPublicProcess

- **realizesFunction:** `UserSendPublic`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

### UserValidatePublicProcess

- **realizesFunction:** `UserValidatePublic`
- **hasSubProcess (candidata approvata):** —
- **hasStep:** —
- **hasTransition (Process):** —

## 6. Schede Step, ControlNode, condizioni e gap

> Le righe `?` sono `viz:DocumentationGap`, non `ProcessStep`.

### PCCalculatePublicStep

- **Classe:** `ProcessStep`
- **Etichetta:** Calcola A
- **Process owner:** `PCProcess`
- **invokesProcess (candidata):** `PCCalculatePublicProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### PCDeriveSecretStep

- **Classe:** `ProcessStep`
- **Etichetta:** Deriva K_PC
- **Process owner:** `PCProcess`
- **invokesProcess (candidata):** `PCDeriveSecretProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### PCEnd

- **Classe:** `ControlNode`
- **Etichetta:** PC fine processo
- **Process owner:** `PCProcess`
- **invokesProcess (candidata):** —
- **controlKind:** EndProcess
- **gap ramo negativo:** —

### PCGeneratePrivateStep

- **Classe:** `ProcessStep`
- **Etichetta:** Genera segreto a
- **Process owner:** `PCProcess`
- **invokesProcess (candidata):** `PCGeneratePrivateProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### PCPublicValidityDecision

- **Classe:** `ControlNode`
- **Etichetta:** PC peer public valid?
- **Process owner:** `PCProcess`
- **invokesProcess (candidata):** —
- **controlKind:** —
- **gap ramo negativo:** `PCInvalidPublicGap`

### PCReceivePublicStep

- **Classe:** `ProcessStep`
- **Etichetta:** Riceve B
- **Process owner:** `PCProcess`
- **invokesProcess (candidata):** `PCReceivePublicProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### PCSendPublicStep

- **Classe:** `ProcessStep`
- **Etichetta:** Invia A
- **Process owner:** `PCProcess`
- **invokesProcess (candidata):** `PCSendPublicProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### PCValidatePublicStep

- **Classe:** `ProcessStep`
- **Etichetta:** Verifica validità B
- **Process owner:** `PCProcess`
- **invokesProcess (candidata):** `PCValidatePublicProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### UserAcquirePrivateStep

- **Classe:** `ProcessStep`
- **Etichetta:** Acquisisce segreto b
- **Process owner:** `UserProcess`
- **invokesProcess (candidata):** `UserAcquirePrivateProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### UserCalculatePublicStep

- **Classe:** `ProcessStep`
- **Etichetta:** Calcola B
- **Process owner:** `UserProcess`
- **invokesProcess (candidata):** `UserCalculatePublicProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### UserDeriveSecretStep

- **Classe:** `ProcessStep`
- **Etichetta:** Deriva K_User
- **Process owner:** `UserProcess`
- **invokesProcess (candidata):** `UserDeriveSecretProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### UserEnd

- **Classe:** `ControlNode`
- **Etichetta:** User fine processo
- **Process owner:** `UserProcess`
- **invokesProcess (candidata):** —
- **controlKind:** EndProcess
- **gap ramo negativo:** —

### UserPublicValidityDecision

- **Classe:** `ControlNode`
- **Etichetta:** User peer public valid?
- **Process owner:** `UserProcess`
- **invokesProcess (candidata):** —
- **controlKind:** —
- **gap ramo negativo:** `UserInvalidPublicGap`

### UserReceivePublicStep

- **Classe:** `ProcessStep`
- **Etichetta:** Riceve A
- **Process owner:** `UserProcess`
- **invokesProcess (candidata):** `UserReceivePublicProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### UserSendPublicStep

- **Classe:** `ProcessStep`
- **Etichetta:** Invia B
- **Process owner:** `UserProcess`
- **invokesProcess (candidata):** `UserSendPublicProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### UserValidatePublicStep

- **Classe:** `ProcessStep`
- **Etichetta:** Verifica validità A
- **Process owner:** `UserProcess`
- **invokesProcess (candidata):** `UserValidatePublicProcess`
- **controlKind:** —
- **gap ramo negativo:** —

### PCPeerPublicValid

- **Classe:** `AtomicCondition`
- **leftOperand:** `PCValidationOutcomeOperand`
- **referencesContractElement:** `ValidityB`

### UserPeerPublicValid

- **Classe:** `AtomicCondition`
- **leftOperand:** `UserValidationOutcomeOperand`
- **referencesContractElement:** `ValidityA`

### PCInvalidPublicGap

- **Classe:** `viz:DocumentationGap` (ausiliaria, non ProcessStep)
- **Etichetta:** ? valore remoto non valido

### UserInvalidPublicGap

- **Classe:** `viz:DocumentationGap` (ausiliaria, non ProcessStep)
- **Etichetta:** ? valore remoto non valido

## 7. Schede ProcessTransition (ordine locale e guardie)

| Transizione | Processo | Da Step | A Step | Guardia | Valore atteso (viz) |
|---|---|---|---|---|---|
| `PCTransition01` | `PCProcess` | `PCGeneratePrivateStep` | `PCCalculatePublicStep` | — | — |
| `PCTransition02` | `PCProcess` | `PCCalculatePublicStep` | `PCSendPublicStep` | — | — |
| `PCTransition03` | `PCProcess` | `PCSendPublicStep` | `PCReceivePublicStep` | — | — |
| `PCTransition04` | `PCProcess` | `PCReceivePublicStep` | `PCValidatePublicStep` | — | — |
| `PCTransition05` | `PCProcess` | `PCValidatePublicStep` | `PCPublicValidityDecision` | — | — |
| `PCTransition06` | `PCProcess` | `PCPublicValidityDecision` | `PCDeriveSecretStep` | `PCPeerPublicValid` | `true` |
| `PCTransition07` | `PCProcess` | `PCDeriveSecretStep` | `PCEnd` | — | — |
| `UserTransition01` | `UserProcess` | `UserAcquirePrivateStep` | `UserReceivePublicStep` | — | — |
| `UserTransition02` | `UserProcess` | `UserReceivePublicStep` | `UserValidatePublicStep` | — | — |
| `UserTransition03` | `UserProcess` | `UserValidatePublicStep` | `UserPublicValidityDecision` | — | — |
| `UserTransition04` | `UserProcess` | `UserPublicValidityDecision` | `UserCalculatePublicStep` | `UserPeerPublicValid` | `true` |
| `UserTransition05` | `UserProcess` | `UserCalculatePublicStep` | `UserSendPublicStep` | — | — |
| `UserTransition06` | `UserProcess` | `UserSendPublicStep` | `UserDeriveSecretStep` | — | — |
| `UserTransition07` | `UserProcess` | `UserDeriveSecretStep` | `UserEnd` | — | — |

**Nota sulle denominazioni:** non si deduce causalità da un nome di classe o di individuo. L’ordine dichiarato è quello delle `ProcessTransition` nel Turtle.
