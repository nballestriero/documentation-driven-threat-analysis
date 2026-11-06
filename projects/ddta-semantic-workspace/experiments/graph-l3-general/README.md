# Graph L3 generale — preparazione e audit MR

Il file `MR_L3_REVIEW_LEDGER_R1.md` documenta lo stato della verifica semantica dei sei MR (R1, 5 novembre 2026) e i punti da decidere prima di implementare la vista Graph L3 completa.

La procedura di inventario è riproducibile e **soltanto in lettura**:

```powershell
Set-Location "C:\Users\user\Documents\TESI\projects\ddta-semantic-workspace"
python experiments/graph-l3-general/audit_mr_sources.py
```

Il comando controlla l'unione RDF di MR-01, MR-02, MR-03, MR-04, MR-C6 e MR-C7 e ne mostra tipo, relazioni e hash dei sorgenti effettivi. `--json` restituisce una rappresentazione JSON adatta a confronto; `--mr-dir` e `--schema` consentono di specificare percorsi diversi. Per confrontare gli hash con la baseline di questo audit:

```powershell
python experiments/graph-l3-general/audit_mr_sources.py --baseline experiments/graph-l3-general/AUDIT_BASELINE_R1.json
```

Per testare una differenza fra il snapshot usato per R1 e il proprio checkout, confrontare i valori `sha256` per ciascun documento. Le eventuali differenze non indicano automaticamente errori: richiedono una nuova revisione.

Il comando **non** modifica i Turtle, gli MR, le query, YAML, il Core o i grafici esistenti. Il file `MR_L3_REVIEW_LEDGER_R1.md` è una nota di lavoro: le decisioni segnate REVIEW devono essere approvate prima di applicare patch ai MR canonici.
