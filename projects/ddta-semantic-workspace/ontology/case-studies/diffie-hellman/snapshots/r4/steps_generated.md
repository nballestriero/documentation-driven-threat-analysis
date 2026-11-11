# Traccia dei passi generata dal grafo RDF

> Gli ordini sono locali a ciascun processo: non costituiscono una cronologia globale.

| Processo | Ordine | Step | Funzione | Input | Output | Canale | Condizione/gap |
|---|---:|---|---|---|---|---|---|
| PC | 1 | PCGeneratePrivateStep | PCGeneratePrivate | — | PrivateA | — | — |
| PC | 2 | PCCalculatePublicStep | PCCalculatePublic | InputsPCPublic | PublicA | — | — |
| PC | 3 | PCSendPublicStep | PCSendPublic | LocalPublicA | PublicA | PCToUserChannel | — |
| PC | 4 | PCReceivePublicStep | PCReceivePublic | PublicB | ReceivedB | UserToPCChannel | — |
| PC | 5 | PCValidatePublicStep | PCValidatePublic | ReceivedB | ValidityB | — | PeerPublicValid; false → ❓ GAP |
| PC | 6 | PCDeriveSecretStep | PCDeriveSecret | InputsPCDerive | SharedKPC | — | — |
| User | 1 | UserAcquirePrivateStep | UserAcquirePrivate | EnteredB | PrivateB | — | — |
| User | 2 | UserReceivePublicStep | UserReceivePublic | PublicA | ReceivedA | PCToUserChannel | — |
| User | 3 | UserValidatePublicStep | UserValidatePublic | ReceivedA | ValidityA | — | PeerPublicValid; false → ❓ GAP |
| User | 4 | UserCalculatePublicStep | UserCalculatePublic | InputsUserPublic | PublicB | — | — |
| User | 5 | UserSendPublicStep | UserSendPublic | LocalPublicB | PublicB | UserToPCChannel | — |
| User | 6 | UserDeriveSecretStep | UserDeriveSecret | InputsUserDerive | SharedKUser | — | — |

## Scambi associati deterministicamente

L’associazione è ottenuta da **identico contratto di attraversamento**, canale comune e ruoli espliciti di invio/ricezione.
- `PC` → `User`: `PublicA` su `PCToUserChannel` (contratto `PublicAOverChannel`).
- `User` → `PC`: `PublicB` su `UserToPCChannel` (contratto `PublicBOverChannel`).

**Nota:** la tabella documenta il comportamento previsto, non eventi runtime né garanzie di autenticità.
