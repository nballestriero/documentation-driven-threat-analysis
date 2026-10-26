# ONT-T01 — E3 DeepSeek pilot matching R1 (REVIEW CANDIDATE)

**Baseline Git:** `ccad45f`; **Gold:** R3, 64 unità; **Output:** `ONT_T01_ORA_V1_DEEPSEEK_ORIGINAL.json` (immutato).  **Stato:** proposta di annotazione, NON valutazione approvata.

## Scopo

Mappatura umana assistita esplicita per ogni unità R3. La corrispondenza **non** è attribuita sulla base di uguaglianza dei nomi. Una singola relazione n-aria può corrispondere a più unità (es. `R-001`→`R3-025..027`; `R-004`→`R3-030..032`). Conservo gli ID degli oggetti/relazioni/azioni dell’output originale. `ambiguities[0]` e `[1]` sono indici **zero-based** della lista, privi di id originali.

## Esito diagnostico **provvisorio**

- MATCH: **55**; PARTIAL: **9**; MISSING: **0**; totale: 64.
- Conteggi puramente descrittivi per rileggere la matrice; **non** sono un punteggio aggregato né prova di correttezza dei matching.
- `BEHAVIOR`: {'MATCH': 12, 'PARTIAL': 5, 'total': 17}
- `ENTITY_MENTION`: {'MATCH': 27, 'PARTIAL': 2, 'total': 29}
- `POLARITY_CHECK`: {'MATCH': 1, 'total': 1}
- `SEMANTIC_FACT`: {'MATCH': 11, 'PARTIAL': 1, 'total': 12}
- `TEMPORAL_CHECK`: {'MATCH': 1, 'total': 1}
- `UNCERTAINTY_CHECK`: {'MATCH': 3, 'PARTIAL': 1, 'total': 4}

## Questioni da sottoporre a doppia revisione

1. **R3-006/R3-064:** `O-009` etichettato “Disponibilità” è usato sia come informazione conservata (`R-003`) sia come disponibilità verificata (`A-003`). Non decidere che i due referenti siano necessariamente identici o diversi. `PARTIAL` è una proposta prudenziale.
2. **R3-038/R3-044/R3-045/R3-052:** comportamento principale rilevato, ma condizioni/precedenze non sempre espresse nel campo strutturato. Verificare se evidenze e azioni contigue bastino per `MATCH` secondo una regola **indipendente dal modello**.
3. **R3-040:** interrogazione Inventory Service compresa nel record `A-003` della verifica. L'assenza di un'azione distinta non costituisce automaticamente `MISSING`.
4. **R3-050/R3-062:** il common antecedent di conferma è conservato tramite `A-013.condition` e `A-014.condition`; non inferire sequenza Confirmed→notifica.
5. **R3-056:** `A-012` documenta richiesta di riserva; `O-025` menziona la riserva. Valutare se il limite d’inferenza sia sufficientemente preservato per il controllo U.
6. **R3-057/R3-058:** la prima frase è citata negli oggetti ma non formalizza autonomamente l’abilitazione all’acquisto né la relazione prodotti-catalogo.
7. **Ruoli impliciti:** ad esempio `A-014.actorId=null` è appropriato: il testo non identifica un mittente; `Notification Service` figura come mezzo, non come agente certo.

## Politica di valutazione

`MATCH`: copertura del fatto e dei ruoli/qualificazioni essenziali anche in record aggregati; `PARTIAL`: significato riconoscibile con informazione mancante o ambiguità di identità; `MISSING`: nessun supporto nell'estrazione. Una citazione letterale non sostituisce automaticamente un fatto strutturato. Affermare assenza/non-esistenza quando il testo tace sarebbe un'inferenza non autorizzata.

**Separazione obbligatoria:** `UNSUPPORTED` e `CONTRADICTED` degli output extra-rich gold richiedono un audit distinto E3-B; questo rapporto NON conclude che tali casi siano zero. La neutralità delle regole per Qwen/Mistral è ancora da controllare prima di applicare una rubrica congelata.

**Provenienza:** il gold e l'output vengono dal commit `ccad45f`; un controllo programmatico locale verifica esistenza degli ID, copertura della matrice, e SHA dell'originale, senza editarne i byte.
