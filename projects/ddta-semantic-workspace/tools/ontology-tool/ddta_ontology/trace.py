"""Inventario statico del codice per future viste DDTA CORE e Mermaid.

Usa il modulo standard ast, non un tracciatore runtime: analizza funzioni
esplicite e chiamate staticamente risolvibili all'interno del pacchetto.
Le espressioni degli argomenti sono TESTO sorgente, non valori a runtime.
Non genera Mermaid né nuove triple del CORE: la semantica grafica sarà definita
in una fase successiva.
"""

from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Any


PACKAGE = "ddta_ontology"


def _python_signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[dict[str, str]]:
    """Estrae i parametri dichiarati dalla firma, compresi gli annotati."""
    args = node.args
    result: list[dict[str, str]] = []
    for p in args.posonlyargs + args.args:
        result.append({"name": p.arg,
                       "annotation": ast.unparse(p.annotation) if p.annotation else "unspecified"})
    if args.vararg:
        result.append({"name": "*" + args.vararg.arg,
                       "annotation": ast.unparse(args.vararg.annotation)
                       if args.vararg.annotation else "unspecified"})
    for p in args.kwonlyargs:
        result.append({"name": p.arg,
                       "annotation": ast.unparse(p.annotation) if p.annotation else "unspecified"})
    if args.kwarg:
        result.append({"name": "**" + args.kwarg.arg,
                       "annotation": ast.unparse(args.kwarg.annotation)
                       if args.kwarg.annotation else "unspecified"})
    return result


def _local_imports(module_name: str, tree: ast.Module) -> dict[str, str]:
    """Riconosce gli alias di import relativi dal pacchetto stesso."""
    result: dict[str, str] = {}
    for statement in tree.body:
        if isinstance(statement, ast.ImportFrom) and statement.level == 1:
            sub = statement.module
            if sub:
                for alias in statement.names:
                    result[alias.asname or alias.name] = f"{PACKAGE}.{sub}.{alias.name}"
            else:
                for alias in statement.names:
                    result[alias.asname or alias.name] = f"{PACKAGE}.{alias.name}"
    return result


def _call_target(call: ast.Call, module_name: str, names: set[str],
                 imports: dict[str, str]) -> str | None:
    """Risolve una chiamata diretta locale, escludendo metodi dinamici."""
    func = call.func
    if isinstance(func, ast.Name):
        if func.id in names:
            return f"{PACKAGE}.{module_name}.{func.id}"
        return imports.get(func.id)
    if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
        alias = imports.get(func.value.id)
        if alias and alias.count(".") == 1:  # import del modulo, non funzione
            return f"{alias}.{func.attr}"
    return None


def _assignment_name(node: ast.Call, parent: dict[ast.AST, ast.AST]) -> str | None:
    """Rileva il nome che riceve direttamente il risultato di una chiamata."""
    p = parent.get(node)
    if isinstance(p, ast.Assign) and p.value is node:
        return ", ".join(ast.unparse(t) for t in p.targets)
    if isinstance(p, ast.AnnAssign) and p.value is node:
        return ast.unparse(p.target)
    return None


def collect_call_map(package_dir: Path | None = None) -> dict[str, Any]:
    """Estrae funzioni, contratti di firma e chiamate interne risolvibili.

    Args:
        package_dir: Directory con i moduli Python; usa la directory
            corrente del pacchetto per impostazione predefinita.

    Returns:
        Documento JSON-compatible. Le chiavi `ddtaView` sono una PROIEZIONE
        per i grafici futuri: NON sono asserzioni OWL, non rappresentano
        `hasSubFunction` e non aggiungono una proprietà `calls` al CORE.
    """
    root = Path(package_dir) if package_dir else Path(__file__).resolve().parent
    trees: dict[str, ast.Module] = {}
    public: dict[str, list[ast.FunctionDef | ast.AsyncFunctionDef]] = {}
    for path in sorted(root.glob("*.py")):
        if path.name == "__init__.py":
            continue
        module = path.stem
        trees[module] = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        public[module] = [s for s in trees[module].body
                          if isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef))]
    nodes: list[dict[str, Any]] = []
    known: set[str] = set()
    for module in sorted(public):
        for fn in public[module]:
            fid = f"{PACKAGE}.{module}.{fn.name}"
            known.add(fid)
            description = ast.get_docstring(fn) or ""
            nodes.append({
                "id": fid,
                "name": fn.name,
                "ddtaView": {
                    "kind": "ddta:Function", "sourceCodeFunction": fid,
                    "hasInputContract": {
                        "kind": "ddta:Contract",
                        "elements": [{"kind": "ddta:ContractElement", **p}
                                     for p in _python_signature(fn)],
                    },
                    "hasOutputContract": {
                        "kind": "ddta:Contract",
                        "element": {"kind": "ddta:ContractElement", "name": "return",
                                    "annotation": ast.unparse(fn.returns)
                                    if fn.returns else "unspecified"},
                    },
                },
                "doc": description.splitlines()[0] if description else "",
                "codeReference": {"module": f"{PACKAGE}.{module}",
                                  "path": f"ddta_ontology/{module}.py",
                                  "line": fn.lineno},
            })
    calls: list[dict[str, Any]] = []
    signatures = {n["id"]: [p["name"] for p in n["ddtaView"]["hasInputContract"]["elements"]]
                  for n in nodes}
    for module in sorted(public):
        tree = trees[module]
        imports = _local_imports(module, tree)
        local_names = {f.name for f in public[module]}
        for fn in public[module]:
            parent = {child: n for n in ast.walk(fn) for child in ast.iter_child_nodes(n)}
            for expression in ast.walk(fn):
                if not isinstance(expression, ast.Call):
                    continue
                target = _call_target(expression, module, local_names, imports)
                if target not in known:
                    continue
                parameters = signatures[target]
                args = []
                for index, arg in enumerate(expression.args):
                    parameter = (parameters[index] if index < len(parameters) else "*args")
                    args.append({"parameter": parameter, "expression": ast.unparse(arg)})
                for kw in expression.keywords:
                    args.append({"parameter": kw.arg or "**kwargs",
                                 "expression": ast.unparse(kw.value)})
                calls.append({
                    "from": f"{PACKAGE}.{module}.{fn.name}", "to": target,
                    "line": expression.lineno,
                    "passedArguments": args,
                    "assignedTo": _assignment_name(expression, parent),
                    "relation": "staticPythonCall",
                })
    calls.sort(key=lambda c: (c["from"], c["line"], c["to"]))
    return {
        "schema": "ddta-code-map/1",
        "limitations": [
            "AST analysis only; no guarantee about runtime executions.",
            "Expressions of passed arguments are source-code text, not runtime values.",
            "Dynamic/reflected calls are not inferred.",
            "ddtaView is a suggested mapping for future graphics, not normative RDF.",
            "staticPythonCall is technical metadata, not a DDTA CORE predicate.",
        ],
        "functions": nodes,
        "calls": calls,
    }


def export_call_map(destination: Path, package_dir: Path | None = None) -> Path:
    """Scrive il JSON tecnico soltanto quando richiesto espressamente."""
    data = collect_call_map(package_dir)
    path = Path(destination).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    return path
