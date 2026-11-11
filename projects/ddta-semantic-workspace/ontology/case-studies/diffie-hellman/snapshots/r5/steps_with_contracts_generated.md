# Diffie-Hellman R5 — passi ricavati dalle transizioni e dai contratti

**Fonte unica:** `dh_r5.ttl`. Gli ordinali sono locali al processo e *derivati* dalle transizioni; `viz:localOrder` viene ignorato.

| Processo | Ordine locale | Step | Tipo | Funzione realizzata | ContractElement di input | ContractElement di output | Guardia / gap |
|---|---:|---|---|---|---|---|---|
| PCProcess | 1 | PCGeneratePrivateStep | ProcessStep | PCGeneratePrivate | EntropyPC, ModulusP, SubgroupOrderQ | PrivateA | — |
| PCProcess | 2 | PCCalculatePublicStep | ProcessStep | PCCalculatePublic | GeneratorG, ModulusP, PrivateA | PublicA | — |
| PCProcess | 3 | PCSendPublicStep | ProcessStep | PCSendPublic | PublicA | PublicA | — |
| PCProcess | 4 | PCReceivePublicStep | ProcessStep | PCReceivePublic | PublicB | ReceivedB | — |
| PCProcess | 5 | PCValidatePublicStep | ProcessStep | PCValidatePublic | GeneratorG, ModulusP, ReceivedB, SubgroupOrderQ | AcceptedBOptional, ValidityB | — |
| PCProcess | 6 | PCPublicValidityDecision | ControlNode | — | — | — | PCPeerPublicValid on transition PCTransition06; gap ? → PCInvalidPublicGap |
| PCProcess | 7 | PCDeriveSecretStep | ProcessStep | PCDeriveSecret | AcceptedBRequired, ModulusP, PrivateA | SharedKPC | — |
| PCProcess | 8 | PCEnd | ControlNode | — | — | — | — |
| UserProcess | 1 | UserAcquirePrivateStep | ProcessStep | UserAcquirePrivate | EnteredB, ModulusP, SubgroupOrderQ | PrivateB | — |
| UserProcess | 2 | UserReceivePublicStep | ProcessStep | UserReceivePublic | PublicA | ReceivedA | — |
| UserProcess | 3 | UserValidatePublicStep | ProcessStep | UserValidatePublic | GeneratorG, ModulusP, ReceivedA, SubgroupOrderQ | AcceptedAOptional, ValidityA | — |
| UserProcess | 4 | UserPublicValidityDecision | ControlNode | — | — | — | UserPeerPublicValid on transition UserTransition04; gap ? → UserInvalidPublicGap |
| UserProcess | 5 | UserCalculatePublicStep | ProcessStep | UserCalculatePublic | GeneratorG, ModulusP, PrivateB | PublicB | — |
| UserProcess | 6 | UserSendPublicStep | ProcessStep | UserSendPublic | PublicB | PublicB | — |
| UserProcess | 7 | UserDeriveSecretStep | ProcessStep | UserDeriveSecret | AcceptedARequired, ModulusP, PrivateB | SharedKUser | — |
| UserProcess | 8 | UserEnd | ControlNode | — | — | — | — |

**16 nodi complessivi**, inclusi i ControlNode. Non è una sequenza globale obbligatoria.

La guardia è mostrata sul ControlNode che possiede la transizione condizionata; gli Step precedenti non ne ereditano automaticamente il significato.

Il ramo per `EnteredB` non valido, non presente nel grafo R4, è una lacuna da affrontare quando rivedremo i processi; non è stato aggiunto qui.
