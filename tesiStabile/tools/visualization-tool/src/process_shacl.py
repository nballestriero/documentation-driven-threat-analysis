#!/usr/bin/env python3
"""Compile SHACL shapes deterministically from `yaml ontology-validation` blocks.

The ontology Markdown is the only normative source of constraints. Optional
pySHACL runtime validates shapes using the compiled graph; no silent skipping.
"""
from __future__ import annotations
import argparse,re,sys
from pathlib import Path
import yaml
from rdflib import Graph, BNode, URIRef, Literal, RDF, Namespace

NS={'process':Namespace('https://w3id.org/ddta/process#'),
    'ddta':Namespace('https://w3id.org/ddta/core#')}
SH=Namespace('http://www.w3.org/ns/shacl#')
BASE=Namespace('https://w3id.org/ddta/process-validation#')

def uri(qname:str):
    prefix,local=qname.split(':',1)
    if prefix not in NS:raise ValueError('IRI namespace not supported: '+qname)
    return NS[prefix][local]

def compile_shapes(document:Path)->Graph:
    content=document.read_text(encoding='utf8')
    blocks=re.findall(r'```yaml ontology-validation\s*\n(.*?)\n```',content,re.S)
    if not blocks:raise ValueError('No ontology-validation blocks found')
    g=Graph();g.bind('sh',SH);g.bind('process',NS['process']);g.bind('ddta',NS['ddta'])
    ids=set()
    for source in blocks:
        doc=yaml.safe_load(source)
        if doc.get('engine')!='SHACL':raise ValueError('Expected SHACL engine')
        target=uri(doc['target'])
        shape=BASE['Shape_'+doc['target'].replace(':','_')]
        g.add((shape,RDF.type,SH.NodeShape));g.add((shape,SH.targetClass,target))
        for c in doc['constraints']:
            rid=c['id']
            if rid in ids:raise ValueError('Duplicated constraint ID '+rid)
            ids.add(rid)
            if c['type']=='property-count':
                for i,p in enumerate(c['properties']):
                    property_shape=BASE[rid+'_P'+str(i+1)]
                    g.add((shape,SH.property,property_shape));g.add((property_shape,RDF.type,SH.PropertyShape))
                    g.add((property_shape,SH.path,uri(p['path'])))
                    for key,term in [('minCount',SH.minCount),('maxCount',SH.maxCount)]:
                        if key in p:g.add((property_shape,term,Literal(int(p[key]))))
                    g.add((property_shape,SH.message,Literal(rid+' '+p['path'])))
            elif c['type']=='sparql':
                sp=BASE[rid]
                g.add((shape,SH.sparql,sp));g.add((sp,RDF.type,SH.SPARQLConstraint))
                g.add((sp,SH.select,Literal(c['select'])))
                g.add((sp,SH.message,Literal(rid+': '+c.get('message',{}).get('it',rid),lang='it')))
            else:raise ValueError('Unknown shape constraint '+c['type'])
    return g

def main():
    ap=argparse.ArgumentParser(description='Compile and optionally run DDTA PROCESS SHACL')
    root=Path(__file__).resolve().parents[1]
    ap.add_argument('--ontology',type=Path,default=root/'ontologies/process/DDTA_PROCESS.md')
    ap.add_argument('--output',type=Path,default=root/'shapes/process-shapes.ttl')
    ap.add_argument('--core',type=Path,default=root/'examples/00_PLATE_GATE_CORE_BASELINE.ttl')
    ap.add_argument('--process',type=Path,default=root/'examples/02_RECOGNIZE_PLATE_PROCESS_R6_CANDIDATA.ttl')
    ap.add_argument('--validate',action='store_true')
    args=ap.parse_args()
    shapes=compile_shapes(args.ontology)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    # Stable bnode-free named graph; canonical order of Turtle is irrelevant to SPARQL.
    # N-Triples is a Turtle-compatible strict subset and has a byte-stable order.
    data='\n'.join(sorted(shapes.serialize(format='nt').splitlines()))+'\n'
    args.output.write_text(data,encoding='utf8',newline='\n')
    print('Generated SHACL',len(shapes),'triples /',len(data.encode('utf8')),'bytes:',args.output)
    if args.validate:
        try:from pyshacl import validate
        except ImportError:
            print('pySHACL not installed: install `pip install pyshacl` to execute SHACL; shapes generated only.',file=sys.stderr)
            return 2
        data_graph=Graph().parse(str(args.core),format='turtle')
        data_graph.parse(str(args.process),format='turtle')
        conforms,report,_=validate(data_graph,shacl_graph=shapes,inference='none',abort_on_first=False)
        print('SHACL conforms:',conforms,'\n',report.serialize(format='turtle')[:7000])
        return 0 if conforms else 1
    return 0

if __name__=='__main__':sys.exit(main())
