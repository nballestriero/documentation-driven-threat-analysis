# ONT-T01 — Chiusura V1 provvisoria e avvio V2

**Status: REVIEW CANDIDATE — baseline sperimentale non validata indipendentemente.**

## Fonti operative

- 3 JSON originali V1 (immutati)
- Gold R3: 64 unità di verifica sovrapposte, NON 64 osservazioni indipendenti
- Matrice comparativa V1: giudizi storici DeepSeek e candidati per Qwen/Mistral
- R3 semantic candidate file present locally: 190 records; status REVIEW CANDIDATE. Counts by source columns are not approved metrics.
- PR-10 blind independent review: NON ESEGUITA; non dichiarare riproducibilità dimostrata

## Conteggi descrittivi delle etichette nella matrice V1

| Modello | MATCH | PARTIAL | MISSING | Altro |
|---|---:|---:|---:|---:|
| DEEPSEEK | 55 | 9 | 0 | 0 |
| QWEN | 55 | 8 | 0 | 1 |
| MISTRAL | 58 | 6 | 0 | 0 |

I conteggi sono etichette per unità di verifica e NON tassi di accuratezza. I giudizi semantici restano candidati e alcuni richiedono riconciliazione.

## Limiti non bloccanti V2

- Qwen A-016: possibile inferenza non documentata di esecuzione autonoma della riserva.
- Potenziale fusione quantità ordinate/richieste e perdita di modalità temporali.
- Controllo PR-10 indipendente e adjudication atomica non conclusi.
- Le citazioni evidence rappresentano provenienza, non provano che la semantica sia codificata nei campi.

## Protocollo V2

Una singola esecuzione per modello, ciascuno riceve lo stesso testo e tutti e tre i JSON V1. Nessuna risposta V2 precedente è visibile ad altri modelli. Tre output totali; Gold e giudizi di valutazione esclusi dall’input. Confronto finale V1-V2 separato per categorie e regressioni. Attribuzione contributi dichiarativa, non causale.
