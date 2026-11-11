# Traccia locale ricostruita dalle transizioni R5A

> Generata dal Turtle, non dall’ordine alfabetico, da `viz:localOrder` o da un evento runtime. Rappresenta il solo percorso nominale con i gap negativi dichiarati.

| Processo | N. locale | Step | Tipo | Sottoprocesso → Function | Input | Output | Guardia/gap |
|---|---:|---|---|---|---|---|---|
| PCProcess | 1 | PCGeneratePrivateStep | ProcessStep | PCGeneratePrivateProcess → PCGeneratePrivate | EntropyPC, ModulusP, SubgroupOrderQ | PrivateA | guard= |
| PCProcess | 2 | PCCalculatePublicStep | ProcessStep | PCCalculatePublicProcess → PCCalculatePublic | GeneratorG, ModulusP, PrivateA | PublicA | guard= |
| PCProcess | 3 | PCSendPublicStep | ProcessStep | PCSendPublicProcess → PCSendPublic | PublicA | PublicA | guard= |
| PCProcess | 4 | PCReceivePublicStep | ProcessStep | PCReceivePublicProcess → PCReceivePublic | PublicB | ReceivedB | guard= |
| PCProcess | 5 | PCValidatePublicStep | ProcessStep | PCValidatePublicProcess → PCValidatePublic | GeneratorG, ModulusP, ReceivedB, SubgroupOrderQ | AcceptedBOptional, ValidityB | guard= |
| PCProcess | 6 | PCPublicValidityDecision | ControlNode | — | — | — | guard=PCPeerPublicValid / ❓ gap=PCInvalidPublicGap |
| PCProcess | 7 | PCDeriveSecretStep | ProcessStep | PCDeriveSecretProcess → PCDeriveSecret | AcceptedBRequired, ModulusP, PrivateA | SharedKPC | guard= |
| PCProcess | 8 | PCEnd | ControlNode | — | — | — | — |
| UserProcess | 1 | UserAcquirePrivateStep | ProcessStep | UserAcquirePrivateProcess → UserAcquirePrivate | EnteredB, ModulusP, SubgroupOrderQ | PrivateB | guard= |
| UserProcess | 2 | UserReceivePublicStep | ProcessStep | UserReceivePublicProcess → UserReceivePublic | PublicA | ReceivedA | guard= |
| UserProcess | 3 | UserValidatePublicStep | ProcessStep | UserValidatePublicProcess → UserValidatePublic | GeneratorG, ModulusP, ReceivedA, SubgroupOrderQ | AcceptedAOptional, ValidityA | guard= |
| UserProcess | 4 | UserPublicValidityDecision | ControlNode | — | — | — | guard=UserPeerPublicValid / ❓ gap=UserInvalidPublicGap |
| UserProcess | 5 | UserCalculatePublicStep | ProcessStep | UserCalculatePublicProcess → UserCalculatePublic | GeneratorG, ModulusP, PrivateB | PublicB | guard= |
| UserProcess | 6 | UserSendPublicStep | ProcessStep | UserSendPublicProcess → UserSendPublic | PublicB | PublicB | guard= |
| UserProcess | 7 | UserDeriveSecretStep | ProcessStep | UserDeriveSecretProcess → UserDeriveSecret | AcceptedARequired, ModulusP, PrivateB | SharedKUser | guard= |
| UserProcess | 8 | UserEnd | ControlNode | — | — | — | — |

La tabella non implica precedenza obbligatoria fra PC e User. I messaggi si associano attraverso canali e contratti condivisi.
