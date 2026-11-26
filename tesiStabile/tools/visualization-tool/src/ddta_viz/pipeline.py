"""Pipeline end-to-end, stessa logica invocabile anche un modulo alla volta."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from rdflib import URIRef
from .catalog import Catalog
from .compile_rules import compile_rules
from .extract_guides import extract_guides
from .select_graph import select_subgraph
from .project_view import project
from .render_mermaid import render
from .common import dump_json, qname_or_uri


def main(argv=None):
    ap=argparse.ArgumentParser(description='Pipeline DDTA: guide Markdown/YAML + TTL + query SPARQL opzionale -> IR -> Mermaid.')
    src=ap.add_mutually_exclusive_group(required=True)
    src.add_argument('--guides-md',nargs='+',type=Path,help='Una o più guide Markdown da cui estrarre YAML')
    src.add_argument('--rules-yaml',nargs='+',type=Path,help='Uno o più YAML grafici già estratti')
    ap.add_argument('--ttl',nargs='+',required=True,type=Path,help='Uno o più file Turtle del sistema')
    ap.add_argument('--query',type=Path,help='Query SELECT ?s ?p ?o; assente = tutti i dati')
    ap.add_argument('--focus',help='IRI/QName radice; senza focus si mostrano le radici del grafo')
    ap.add_argument('--view',choices=['association','functional-flow'],default='association',help='Vista della comunicazione')
    ap.add_argument('--strict',action='store_true',help='Blocca generazione in presenza di ambiguità')
    ap.add_argument('--out-dir',required=True,type=Path,help='Cartella di output')
    args=ap.parse_args(argv)
    out=args.out_dir; out.mkdir(parents=True,exist_ok=True)
    if args.guides_md:
        extracted=out/'01_rules_extracted.yaml'
        extract_guides(args.guides_md,extracted)
        inputs=[extracted]
    else:inputs=args.rules_yaml
    compiled=out/'02_rules_compiled.yaml'
    compile_rules(inputs,compiled)
    selected=out/'03_selected.ttl'
    g=select_subgraph(args.ttl,args.query,selected)
    focus=URIRef(qname_or_uri(g,args.focus)) if args.focus else None
    catalog=Catalog([compiled])
    ir=project(g,catalog,focus=focus,view=args.view,strict=args.strict)
    dump_json(ir,out/'04_projection.json')
    mmd=render(ir,catalog)
    (out/'05_graph.mmd').write_text(mmd,encoding='utf-8')
    (out/'05_graph.md').write_text('```mermaid\n'+mmd+'```\n',encoding='utf-8')
    report={'regole':len(catalog.records),'triple':len(g), 'statistiche':ir['statistics'],
            'diagnostici':ir['diagnostics'],'view':args.view,
            'note':'Le occorrenze grafiche multiple hanno lo stesso IRI RDF, non sono nuove entità.'}
    dump_json(report,out/'06_diagnostics.json')
    print('Pipeline completa:')
    print(f'  {len(catalog.records)} regole, {len(g)} triple, {ir["statistics"]["rdfIndividuals"]} individui')
    warning_count = sum(1 for d in ir['diagnostics'] if d['severity']=='warning')
    info_count = sum(1 for d in ir['diagnostics'] if d['severity']=='info')
    print(f'  Avvisi: {warning_count}; informazioni: {info_count}')
    print(f'  Mermaid: {out / "05_graph.md"}')
    return 0

if __name__=='__main__':raise SystemExit(main())
