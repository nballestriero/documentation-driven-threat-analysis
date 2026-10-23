# DDTA — installazione e verifica su Windows

Avviare PowerShell dalla radice di `projects/ddta-authoring-tool`.

Prerequisiti: Python con `pip`, VS Code con comando `code` nel PATH; PyYAML installato tramite `prototype/generic-v01/requirements.txt`. Per **usare il motore CLI non serve** VS Code o Node.js; Node.js e' utile soltanto per `node --check` del client.

```powershell
Set-Location 'C:\Users\user\Documents\TESI\projects\ddta-authoring-tool'
python -m pip install -r 'prototype/generic-v01/requirements.txt'
Set-Location 'prototype/generic-v01'
python -m unittest discover -s tests -p 'test_*.py'
python -m ddta_tool check examples/FR-VALID.md --profile strict
Set-Location '../..'
python 'scripts/build_vsix.py'
```

Il nome del VSIX segue la versione letta da `vscode/ddta-authoring-pilot/package.json`, attualmente `0.1.2`. Per controllare e installare:

```powershell
$Version = (Get-Content 'vscode/ddta-authoring-pilot/package.json' -Raw | ConvertFrom-Json).version
$Vsix = Join-Path (Get-Location) "dist/ddta-authoring-pilot-$Version.vsix"
python 'scripts/build_vsix.py' --verify "$Vsix"
code --install-extension "$Vsix" --force
code --list-extensions --show-versions | Select-String 'ddta-research.ddta-authoring-pilot'
```

In VS Code eseguire `Developer: Reload Window`, dichiarare un workspace trusted e aprire `pilots/c9-independent-project/docs/03-functional-requirements/FR-DEMO-01.md`. La cartella TESI aperta come workspace permette attualmente autodiscovery del motore; altrimenti impostare `ddta.frameworkModuleRoot` alla cartella assoluta `.../prototype/generic-v01` e `ddta.pythonExecutable` all'interprete Python corretto. Provare `Ctrl+Space` nel front matter e l'errore temporaneo su `parentDecision`; ripristinare il file e **non salvare le alterazioni di prova**.

Se la CLI `code` non e' disponibile, installare il VSIX da `Extensions: Install from VSIX...`. Il messaggio Node.js `DEP0169` visto con il comando `code` non ha bloccato l'installazione verificata; eventuali errori effettivi vanno valutati separatamente.

Per riprodurre il build byte-per-byte usare stesso commit e script; i prerequisiti per ricompilare il VSIX sono Python stdlib e i due file sorgenti dell'estensione. Pubblicare una release GitHub e' una fase distinta, non eseguita da questi script.
