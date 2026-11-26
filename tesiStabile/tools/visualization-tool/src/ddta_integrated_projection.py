#!/usr/bin/env python3
"""Internal visual ownership projection for a single CORE+PROCESS Turtle.

The input RDF is immutable. CORE owns systems, functions, communication,
functional contracts, environments and their resources. PROCESS owns its Steps,
ControlNodes, conditions, internal-only contracts and implementation-only
resources. Removing a redundant graphical occurrence does not delete a triple
from the source ontology or infer a new RDF relationship.
"""
from __future__ import annotations
from pathlib import Path
from rdflib import Graph, RDF, RDFS, URIRef, Namespace, Literal

CORE = Namespace('https://w3id.org/ddta/core#')
PROCESS = Namespace('https://w3id.org/ddta/process#')

_PROCESS_CORE_PREDICATES = {CORE.hasStep, CORE.hasNextStep}
_STEP_CONTRACT_PROPERTIES = {PROCESS.declaresInputContract, PROCESS.declaresOutputContract}
_PROCESS_RESOURCE_PROPERTIES = {PROCESS.implementedBy, PROCESS.usesConfiguration, PROCESS.referencesResource}
_FUNCTION_CONTRACT_PROPERTIES = {CORE.hasInputContract, CORE.hasOutputContract}


def select_core_visual_graph(source: Graph) -> tuple[Graph,dict]:
    """Choose graphical ownership from types/predicates, not resource names.

    Process-owned individuals are drawn by the specialized PROCESS renderer.
    A Contract or Resource is omitted from CORE only when it is referenced
    exclusively by PROCESS and has no independent CORE semantic attachment.
    Shared/CORE-attached contracts and resources remain in CORE.
    """
    process_nodes = set()
    for subj,_,typ in source.triples((None,RDF.type,None)):
        if typ == CORE.ProcessStep or str(typ).startswith(str(PROCESS)):
            process_nodes.add(subj)
    # Some steps are not explicitly typed as ProcessStep (e.g. ControlNode).
    # Explicit ddta:hasStep / process branching identifies them as PROCESS-owned.
    process_nodes.update(source.objects(None, CORE.hasStep))
    process_nodes.update(source.subjects(CORE.hasNextStep,None))
    process_nodes.update(source.objects(None, CORE.hasNextStep))
    for rel in (PROCESS.hasTrueNextStep, PROCESS.hasFalseNextStep):
        process_nodes.update(source.subjects(rel,None))
        process_nodes.update(source.objects(None,rel))

    # Retain CORE semantic attachments, excluding process-only nodes/relations.
    kept=set()
    for s,p,o in source:
        if s in process_nodes or o in process_nodes:continue
        if str(p).startswith(str(PROCESS)) or p in _PROCESS_CORE_PREDICATES:continue
        kept.add((s,p,o))

    # The same ddta:Contract can be shared by a Function and ProcessStep.
    # Remove only contracts reached exclusively via process:declares*, then
    # remove contract elements exclusively owned by those contracts.
    process_contracts={o for p in _STEP_CONTRACT_PROPERTIES for o in source.objects(None,p)}
    functional_contracts={o for p in _FUNCTION_CONTRACT_PROPERTIES for o in source.objects(None,p)}
    process_only_contracts=process_contracts - functional_contracts
    # If a non-function CORE edge explicitly references a Contract, retain it.
    process_only_contracts={c for c in process_only_contracts if not any(
        p != RDF.type and (s==c or o==c) and p != CORE.hasContractElement
        for s,p,o in kept)}
    kept={t for t in kept if t[0] not in process_only_contracts and t[2] not in process_only_contracts}

    # A technical Resource belongs inside its ProcessStep when only referenced
    # through process:implementedBy/usesConfiguration/referencesResource.
    process_resources={o for p in _PROCESS_RESOURCE_PROPERTIES for o in source.objects(None,p)}
    process_only_resources={r for r in process_resources if not any(
        p not in (RDF.type, RDFS.label, RDFS.comment) and (s==r or o==r)
        for s,p,o in kept)}
    kept={t for t in kept if t[0] not in process_only_resources and t[2] not in process_only_resources}

    # Remove an orphaned ContractElement only when no retained Contract refers
    # to it and it has no separate CORE relationship.
    removed_elements={o for c in process_only_contracts for o in source.objects(c,CORE.hasContractElement)}
    process_only_elements={e for e in removed_elements if not any(
        p != RDF.type and (s==e or o==e) for s,p,o in kept)}
    kept={t for t in kept if t[0] not in process_only_elements and t[2] not in process_only_elements}

    g=Graph()
    for prefix,uri in source.namespaces():g.bind(prefix,uri)
    for triple in kept:g.add(triple)
    if any((s in process_nodes or o in process_nodes or str(p).startswith(str(PROCESS))) for s,p,o in g):
        raise AssertionError('Proiezione CORE contiene ancora nodi/relazioni PROCESS')
    # Fail closed if source CORE responsibilities were lost in the projection.
    for prop in (CORE.hasPrimaryFunction,CORE.hasSupportFunction,CORE.providesFunction,
                 CORE.usesChannelForInput,CORE.usesChannelForOutput,CORE.hasInputContract,
                 CORE.hasOutputContract,CORE.hasContractElement,CORE.makesAvailable,
                 CORE.hasOperationalEnvironment):
        for t in source.triples((None,prop,None)):
            if t[0] not in process_nodes and t[2] not in process_nodes and t not in kept and t[0] not in process_only_contracts:
                raise ValueError('Relazione CORE persa: '+str(t))
    stats={
        'sourceTriples':len(source),
        'coreVisualTriples':len(g),
        'processOwnedIndividuals':len(process_nodes),
        'processOnlyContracts':len(process_only_contracts),
        'processOnlyContractElements':len(process_only_elements),
        'processOnlyResources':len(process_only_resources),
        'sourceUntouched':True,
    }
    return g,stats


def build_core_visual_projection(input_ttl:Path,output_ttl:Path)->dict:
    input_ttl=Path(input_ttl)
    source=Graph().parse(str(input_ttl),format='turtle')
    core,stats=select_core_visual_graph(source)
    output_ttl=Path(output_ttl)
    output_ttl.parent.mkdir(parents=True,exist_ok=True)
    # All N-Triples statements are legal Turtle. Sorting guarantees stable
    # bytes regardless of rdflib graph iteration order.
    content=''.join(' '.join(x.n3() for x in t)+' .\n' for t in sorted(core,key=lambda t:tuple(x.n3() for x in t)))
    output_ttl.write_text(content,encoding='utf-8',newline='\n')
    check=Graph().parse(str(output_ttl),format='turtle')
    if not source or set(check)!=set(core):
        raise RuntimeError('Proiezione CORE non round-trip o input RDF vuoto')
    return stats
