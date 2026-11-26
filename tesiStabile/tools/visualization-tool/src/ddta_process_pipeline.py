#!/usr/bin/env python3
"""DDTA PROCESS R6: deterministic source -> CORE -> PROCESS pilot.

No edits/imports of the existing CORE renderer. This is a deterministic
orchestrator for the R4.x Mermaid-composition pilot, NOT the future unified
CORE/PROCESS IR renderer. Both executions use the same input files and must
produce byte-identical artifacts before a result is published.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

from ddta_integrated_projection import build_core_visual_projection
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_json(path: Path, obj: object) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2) + '\n', encoding='utf-8', newline='\n')


def checked_run(argv: list[str], label: str) -> None:
    result = subprocess.run(argv, text=True, encoding='utf-8', errors='replace', capture_output=True,
                            env={**os.environ, 'PYTHONDONTWRITEBYTECODE':'1'})
    if result.returncode:
        raise RuntimeError(f'{label} (exit={result.returncode})\n{result.stdout[-3500:]}\n{result.stderr[-3500:]}')


def require_input(path: Path, label: str) -> Path:
    path = path.resolve()
    if not path.is_file():
        raise FileNotFoundError(f'{label}: {path}')
    return path


def trace_projection(ir_path: Path, path: Path) -> None:
    """Trace RDF IRIs, not Mermaid IDs or guessed runtime data transfers."""
    ir = json.loads(ir_path.read_text(encoding='utf-8'))
    transitions = [{
        'transitionIRI': t['iri'], 'processIRI': t['process'],
        'fromStepIRI': t['from'], 'toStepIRI': t['to'],
        'guardIRI': t['guard'],
        'sourceRelation': t['sourceRelation'],
        'branch': t.get('branch'),
    } for t in ir['transitions']]
    contracts = []
    for step_iri, node in sorted(ir['nodes'].items()):
        for role, key in [('INPUT', 'inputContracts'), ('OUTPUT', 'outputContracts')]:
            for c in sorted(node.get(key, [])):
                contracts.append({
                    'stepIRI': step_iri, 'role': role, 'contractIRI': c,
                    'elementIRIs': sorted(e['iri'] for e in ir['contracts'][c]['elements']),
                })
    operands = [{
        'operandIRI': p['operand'], 'contractElementIRI': p['contractElement'],
        'producerStepIRI': p['declaredOutputStep'],
        'candidateProducerStepIRIs': p.get('candidateOutputSteps', []),
        'rdfPredicate': 'https://w3id.org/ddta/process#referencesContractElement',
        'isDataTransfer': False,
    } for p in ir['operandProvenance']]
    write_json(path, {
        'schema': 'ddta-process-rdf-trace-v1',
        'transitions': sorted(transitions, key=lambda x:(x['processIRI'],x['fromStepIRI'],x['toStepIRI'],x['sourceRelation'],x['transitionIRI'] or '')),
        'stepContracts': sorted(contracts,key=lambda x:(x['stepIRI'],x['role'],x['contractIRI'])),
        'initialEntries': sorted([{'processIRI':p['iri'],'stepIRI':entry,'rdfPredicate':'https://w3id.org/ddta/process#hasInitialStep'} for p in ir['processes'] for entry in p.get('initials',([p['initial']] if p['initial'] else []))],key=lambda x:(x['processIRI'],x['stepIRI'])),
        'processCompositions': sorted([{'parentProcessIRI':p['iri'],'childProcessIRI':child,'rdfPredicate':'https://w3id.org/ddta/process#hasSubProcess','isInvocation':False} for p in ir['processes'] for child in p.get('subProcesses',[])],key=lambda x:(x['parentProcessIRI'],x['childProcessIRI'])),
        'controlParticipants': sorted([{'controlIRI':n['iri'],'participantIRI':m,'rdfPredicate':'https://w3id.org/ddta/process#hasParticipantStep','isControlFlow':False,'isDataTransfer':False} for n in ir['nodes'].values() for m in n.get('participantSteps',[])], key=lambda x:(x['controlIRI'],x['participantIRI'])),
        'controlCompletionPolicies': sorted([{'controlIRI':n['iri'],'policy':n['joinPolicy'],'requiredCount':n['requiredCount'],'completionCriterion':n['completionCriterion'],'participantCount':len(n.get('participantSteps',[]))} for n in ir['nodes'].values() if n.get('participantSteps')], key=lambda x:x['controlIRI']),
        'operandReferences': sorted(operands,key=lambda x:x['operandIRI']),
        'realizations': sorted(ir['realizations'],key=lambda x:(x['process'],x['function'])),
        'diagnostics': ir['diagnostics'],
    })


def main(argv=None) -> int:
    ap=argparse.ArgumentParser(description='Deterministic DDTA CORE+PROCESS pilot, two independent runs verified byte for byte')
    source=ap.add_mutually_exclusive_group(required=True)
    source.add_argument('--core-generator', type=Path, help='Installed CORE scripts/pipeline.py, called unchanged (live mode)')
    source.add_argument('--core-mermaid', type=Path, help='CORE output provided; offline comparison only, NOT live CORE generation')
    ap.add_argument('--core-guide', type=Path, required=True)
    ap.add_argument('--core-ttl', type=Path)
    ap.add_argument('--process-guide', type=Path, required=True)
    ap.add_argument('--process-ttl', type=Path)
    ap.add_argument('--ttl', type=Path, help='Unico Turtle integrato CORE+PROCESS (alternativa a --core-ttl e --process-ttl)')
    ap.add_argument('--out-dir', type=Path, required=True)
    ap.add_argument('--show-operand-resource-references',action='store_true',help='Abilita proiezione opzionale RDF process:referencesResource')
    a=ap.parse_args(argv)
    root = Path(__file__).resolve().parent
    renderer=require_input(root/'ddta_process.py','Python PROCESS')
    if a.ttl is not None:
        if a.core_ttl is not None or a.process_ttl is not None:
            ap.error('--ttl non puo essere combinato con --core-ttl/--process-ttl')
        a.core_ttl = a.ttl
        a.process_ttl = a.ttl
    elif a.core_ttl is None or a.process_ttl is None:
        ap.error('specificare --ttl oppure entrambi --core-ttl e --process-ttl')
    for field in ('core_guide','core_ttl','process_guide','process_ttl'):
        setattr(a,field,require_input(getattr(a,field),field))
    if a.core_generator is not None:a.core_generator=require_input(a.core_generator,'core_generator')
    if a.core_mermaid is not None:a.core_mermaid=require_input(a.core_mermaid,'core_mermaid')
    # In live mode the CORE renderer receives an internal RDF view; the original
    # Turtle is always passed unchanged to the PROCESS projector.
    destination=a.out_dir.resolve()
    if destination.exists() and not destination.is_dir():raise ValueError('out-dir non e una directory')
    if destination in [a.core_guide.parent,a.core_ttl.parent,a.process_guide.parent,a.process_ttl.parent]:
        raise ValueError('out-dir non deve coincidere con una directory di input')

    integrated=(a.core_ttl==a.process_ttl and a.core_generator is not None)

    def once(run_dir:Path,core_visual_ttl:Path) -> list[str]:
        # Every generated CORE Mermaid comes from the same CORE entrypoint and
        # unchanged guide/Turtle, never from a retained previous-run output.
        core=run_dir/'core'
        core.mkdir(parents=True)
        if a.core_generator is not None:
            checked_run([sys.executable,str(a.core_generator),'--guides-md',str(a.core_guide),
                         '--ttl',str(core_visual_ttl),'--view','functional-flow','--out-dir',str(core)], 'CORE live')
            core_mmd=require_input(core/'05_graph.mmd','CORE generato')
        else:
            core_mmd=core/'05_graph.mmd'
            shutil.copyfile(a.core_mermaid,core_mmd)
            core.joinpath('05_graph.md').write_bytes(b'```mermaid\n'+core_mmd.read_bytes()+
                (b'' if core_mmd.read_bytes().endswith(b'\n') else b'\n')+b'```\n')
        first=sha(core_mmd)
        base=[sys.executable,str(renderer),'--core-ttl',str(a.core_ttl),
              '--process-ttl',str(a.process_ttl),'--process-guide',str(a.process_guide),
              '--core-guide',str(a.core_guide),'--core-mermaid',str(core_mmd)]
        if a.show_operand_resource_references:
            base+=['--show-operand-resource-references']
        if integrated:
            base+=['--integrated-splice']
        only=run_dir/'core_only';only.mkdir()
        checked_run(base+['--modules','core','--out-dir',str(only)],'CORE-only passthrough')
        if sha(only/'05_graph.mmd')!=first:raise RuntimeError('CORE-only non conserva i byte originali')
        for view in ('compact','extended'):
            folder=run_dir/('core_process_'+view);folder.mkdir()
            checked_run(base+['--modules','core,process','--contract-view',view,
                              '--out-dir',str(folder)],'CORE+PROCESS '+view)
            trace_projection(folder/'04_process_projection.json',folder/'07_rdf_trace.json')
        if sha(core_mmd)!=first:raise RuntimeError('Il renderer PROCESS ha alterato il Mermaid CORE')
        # CORE may write temporary build metadata containing its run-directory
        # path (e.g. 02_rules_compiled.yaml.sources).  This is intentionally
        # not a semantic render artifact and cannot be compared byte-for-byte
        # across independent directories.  Check the projected IR and final
        # graph, without changing CORE or sanitizing any of its output files.
        stable_core={'04_projection.json','05_graph.mmd','05_graph.md','06_diagnostics.json'}
        return [str(f.relative_to(run_dir)).replace('\\','/')
                for f in sorted(run_dir.rglob('*')) if f.is_file()
                and (f.parent!=core or f.name in stable_core)]

    # Snapshot input hashes before both runs.  If another process edits
    # the RDF, guides, or Python during generation, refuse to publish.
    input_paths={
        'core-ttl': a.core_ttl,
        'core-guide': a.core_guide,
        'process-ttl': a.process_ttl,
        'process-guide': a.process_guide,
        'process-python': renderer,
        'orchestrator-python': Path(__file__).resolve(),
        'integrated-projection-python': root/'ddta_integrated_projection.py',
    }
    if a.core_generator is not None:input_paths['core-generator-python']=a.core_generator
    if a.core_mermaid is not None:input_paths['core-mermaid-offline']=a.core_mermaid
    initial_hashes={k:sha(v) for k,v in sorted(input_paths.items())}

    # Two independent runs in temporary directories. Publish only if the
    # comparison succeeds; leave the user's inputs completely untouched.
    with tempfile.TemporaryDirectory(prefix='ddta-process-deterministic-') as tmp:
        temp=Path(tmp)
        projection_stats = None
        core_visual_ttl = a.core_ttl
        if integrated:
            core_visual_ttl = temp/'core_visual_view.ttl'
            projection_stats = build_core_visual_projection(a.core_ttl,core_visual_ttl)
        left=temp/'first';right=temp/'second';left.mkdir();right.mkdir()
        first_files=once(left,core_visual_ttl)
        second_files=once(right,core_visual_ttl)
        if first_files!=second_files:
            raise RuntimeError('Determinismo fallito: la lista dei file varia fra due esecuzioni')
        differences=[f for f in first_files if sha(left/f)!=sha(right/f)]
        if differences:raise RuntimeError('Determinismo fallito (byte differenti): '+', '.join(differences))
        if any(initial_hashes[k]!=sha(v) for k,v in input_paths.items()):
            raise RuntimeError('Uno o piu input sono cambiati durante la doppia esecuzione')
        manifest={
            'schema':'ddta-process-deterministic-run-v1',
            'coreMode':'live' if a.core_generator is not None else 'offline-snapshot',
            'independentRuns':2,
            'deterministicByteForByte':True,
            'coreOnlyByteForByte':True,
            'coreVisualProjection':projection_stats,
            'singleIntegratedTurtle':a.core_ttl == a.process_ttl,
            'inputSha256':initial_hashes,
            'outputSha256':{key:sha(left/key) for key in first_files},
            'limitations':[
                'PROCESS projector covers the validated R4.5 subset and the candidate R6 direct binary branches and compound concurrent control, not every PROCESS ontology class',
                'Integrated composition splices PROCESS Steps into CORE Process occurrences; unified IR renderer is not implemented',
                'Geometric positioning and SVG rendering in Mermaid ELK require separate visual review',
            ]
        }
        # No file modification if output destination exists with unknown files:
        # safely replace only generated files, preserving user-created files.
        destination.mkdir(parents=True,exist_ok=True)
        for rel in first_files:
            target=destination/rel
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(left/rel,target)
        write_json(destination/'manifest.json',manifest)
    print(json.dumps({'status':'OK','mode':manifest['coreMode'],
        'runs':2,'files':len(first_files),'coreOnlyPreserved':True,
        'outDir':str(destination)},ensure_ascii=False,indent=2))
    return 0


if __name__=='__main__':
    try:raise SystemExit(main())
    except (OSError,ValueError,RuntimeError) as exc:
        print(f'ERRORE: {exc}',file=sys.stderr)
        raise SystemExit(1)
