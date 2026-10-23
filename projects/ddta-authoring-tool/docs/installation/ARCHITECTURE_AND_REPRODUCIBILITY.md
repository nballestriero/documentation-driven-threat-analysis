# DDTA — Architettura client-indipendente e riproducibilita (checkpoint C9)

**Stato: guida operativa non normativa.** Non sostituisce MR, Decision, FR o contratti BA.

## Invariante architetturale

La metodologia DDTA e i suoi contratti sono distinti dalla loro implementazione. Il motore Python `prototype/generic-v01/ddta_tool/` e' l'implementazione attuale dei controlli. CLI, VS Code e futuri client CI/AI sono adattatori che consumano il servizio: **il motore non deve importare o richiedere VS Code, Node.js o un LLM**. Il client non copia regole, enum o cataloghi; i risultati devono essere coerenti a parita' di input, versione dei contratti e profilo.

I contratti dichiarativi sono caricabili dal motore entro le grammatiche che supporta. Nuovi tipi/operatori nella grammatica nota non richiedono codice dedicato; una nuova grammatica puo' richiedere un incremento generale del motore. Questo principio e' un **gate da dimostrare**, non una prova gia' completata.

## Tre gate di riproducibilita

1. **Build**: dato un commit Git identificato, `scripts/build_vsix.py` include i byte originali di `extension.js` e `package.json`, impacchetta con un ordine e metadati ZIP fissi e verifica l'artefatto. I package VSIX non sono autorita' del codice.
2. **Installazione**: installare un interprete Python con PyYAML, VS Code e il VSIX sul sistema target; configurare i percorsi esplicitamente quando l'autodiscovery non risolve il motore. Windows e Linux sono percorsi documentati; test su una macchina pulita ancora da eseguire.
3. **Comportamento**: rieseguire unittest e casi manuali su documenti pilota, confrontando diagnostiche CLI e VS Code con uguali scope, contratti e profilo. Non equiparare `121 test OK` al completamento di tutti gli FR.

## Confini e limiti attuali

- L'estensione 0.1.2 riconosce i documenti Markdown nelle tre cartelle MR/Decision/FR; la scoperta dichiarativa di altre directory e' una verifica C9 successiva.
- Il completamento schema-driven YAML e' stato osservato nel pilota; hover, guide BA self-hosted e un tipo aggiunto senza codice non sono ancora provati.
- Per CLI e VS Code il motore e' lo stesso; i test Python non dipendono dall'installazione del client.
- I contratti caricati e le versioni devono essere espliciti nei futuri test di portabilita; non sostituire silenziosamente schemi stabili con varianti in lavorazione.

## Criteri di evidenza

Registrare commit, OS, versioni Python/Node/VS Code, `package.json` version, SHA256 VSIX, test, percorso progetto pilota, risultati delle prove e limiti. Per nuove release: costruire dai sorgenti tracciati, verificare, installare, eseguire prova, soltanto dopo consolidare o pubblicare il package.
