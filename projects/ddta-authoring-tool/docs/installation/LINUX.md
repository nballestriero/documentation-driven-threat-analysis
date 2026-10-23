# DDTA — installazione e verifica su Linux

Prerequisiti: Python 3 con `pip`, VS Code con comando `code` nel PATH. Per **CLI soltanto**, VS Code e Node.js non sono richiesti.

Eseguire dalla radice `projects/ddta-authoring-tool`:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r prototype/generic-v01/requirements.txt
(cd prototype/generic-v01 && python -m unittest discover -s tests -p 'test_*.py')
(cd prototype/generic-v01 && python -m ddta_tool check examples/FR-VALID.md --profile strict)
python scripts/build_vsix.py
VERSION=$(python -c 'import json;print(json.load(open("vscode/ddta-authoring-pilot/package.json"))["version"])')
VSIX="dist/ddta-authoring-pilot-${VERSION}.vsix"
python scripts/build_vsix.py --verify "$VSIX"
code --install-extension "$VSIX" --force
code --list-extensions --show-versions | grep 'ddta-research.ddta-authoring-pilot'
```

Ricaricare VS Code. Se l'autodiscovery non trova il motore, configurare `ddta.frameworkModuleRoot` al percorso assoluto di `prototype/generic-v01` e `ddta.pythonExecutable` all'interprete dell'ambiente virtuale. Aprire il pilota C9 e provare completamento YAML e diagnostica su buffer non salvato. **Il collaudo su Linux pulito e' ancora da eseguire**: questo file descrive una procedura proposta e verificabile, non una prova di successo gia' svolta.
