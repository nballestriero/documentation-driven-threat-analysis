#!/usr/bin/env python3
"""ONT-T01 four-model local ontology extraction and partner rotation. Python >=3.10; stdlib only."""
from __future__ import annotations
import argparse, csv, datetime as dt, hashlib, json, pathlib, re, sys, time, gc, urllib.request, urllib.error

HERE = pathlib.Path(__file__).resolve().parent
COLLS = ('objects', 'relations', 'actions', 'ambiguities')
ROLES = {'objects':'O', 'relations':'R', 'actions':'A'}


def read_json(path):
    return json.loads(pathlib.Path(path).read_text(encoding='utf-8-sig'))

def save_json(path, data):
    path=pathlib.Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_suffix(path.suffix+'.tmp')
    temp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    temp.replace(path)

def hash_text(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()

def as_text(path):return pathlib.Path(path).read_text(encoding='utf-8-sig')

def schema():
    string={'type':'string'}; nullable={'type':['string','null']}
    participant={'type':'object','additionalProperties':False,'required':['objectId','role'],
                 'properties':{'objectId':string,'role':string}}
    objects={'type':'object','additionalProperties':False,
      'required':['id','name','candidateCategory','evidence','uncertainty'],
      'properties':{'id':string,'name':string,'candidateCategory':string,'evidence':string,'uncertainty':nullable}}
    relations={'type':'object','additionalProperties':False,
      'required':['id','description','participants','evidence','uncertainty'],
      'properties':{'id':string,'description':string,'participants':{'type':'array','items':participant},'evidence':string,'uncertainty':nullable}}
    actions={'type':'object','additionalProperties':False,
      'required':['id','verb','actorId','participants','resultIds','condition','evidence','uncertainty'],
      'properties':{'id':string,'verb':string,'actorId':nullable,'participants':{'type':'array','items':participant},
                    'resultIds':{'type':'array','items':string},'condition':nullable,'evidence':string,'uncertainty':nullable}}
    ambiguity={'type':'object','additionalProperties':False,'required':['description','evidence','possibleInterpretations'],
       'properties':{'description':string,'evidence':string,'possibleInterpretations':{'type':'array','items':string}}}
    return {'type':'object','additionalProperties':False,
            'required':['testId',*COLLS],
            'properties':{'testId':string,'objects':{'type':'array','items':objects},
              'relations':{'type':'array','items':relations},'actions':{'type':'array','items':actions},
              'ambiguities':{'type':'array','items':ambiguity}}}

SCHEMA=schema()

def validate(doc,source,test_id):
    """No external dependencies. Structural, referential, evidence checks. No false semantic adjudication."""
    errors=[]
    def fail(msg):errors.append(msg)
    if not isinstance(doc,dict):return ['JSON root must be object']
    if set(doc)!={'testId',*COLLS}:fail('Root keys must be exactly testId, objects, relations, actions, ambiguities')
    if doc.get('testId')!=test_id:fail('testId must equal '+test_id)
    ids={}
    for coll,prefix in ROLES.items():
        values=doc.get(coll)
        if not isinstance(values,list):fail(coll+' must be array');continue
        seen=set()
        req={'objects':{'id','name','candidateCategory','evidence','uncertainty'},
             'relations':{'id','description','participants','evidence','uncertainty'},
             'actions':{'id','verb','actorId','participants','resultIds','condition','evidence','uncertainty'}}[coll]
        for i,row in enumerate(values):
            p=f'{coll}[{i}]'
            if not isinstance(row,dict):fail(p+' must be object');continue
            if set(row)!=req:fail(p+' keys mismatch: '+str(sorted(set(row)^req)))
            ident=row.get('id')
            if not isinstance(ident,str) or not re.fullmatch(prefix+r'-\d{3,}',ident):fail(p+'.id invalid')
            elif ident in seen:fail(p+'.id duplicate')
            else:seen.add(ident)
            for field in ('name','candidateCategory') if coll=='objects' else (('description',) if coll=='relations' else ('verb',)):
                if not isinstance(row.get(field),str) or not row.get(field).strip():fail(p+'.'+field+' must be nonempty string')
            if not isinstance(row.get('uncertainty'),(str,type(None))):fail(p+'.uncertainty invalid')
            if coll=='actions':
                if not isinstance(row.get('actorId'),(str,type(None))):fail(p+'.actorId invalid')
                if not isinstance(row.get('condition'),(str,type(None))):fail(p+'.condition invalid')
                if not isinstance(row.get('resultIds'),list) or not all(isinstance(x,str) for x in row['resultIds']):fail(p+'.resultIds invalid')
            if coll!='objects':
                if not isinstance(row.get('participants'),list):fail(p+'.participants invalid')
                else:
                    for j,x in enumerate(row['participants']):
                        if not isinstance(x,dict) or set(x)!={'objectId','role'} or not all(isinstance(y,str) and y.strip() for y in x.values()):fail(f'{p}.participants[{j}] invalid')
            evidence=row.get('evidence')
            if not isinstance(evidence,str) or not evidence.strip():fail(p+'.evidence missing')
            elif evidence.strip() not in source:fail(p+'.evidence not literal contiguous source excerpt')
        ids[coll]=seen
    values=doc.get('ambiguities')
    if not isinstance(values,list):fail('ambiguities must be array')
    else:
        for i,row in enumerate(values):
            p=f'ambiguities[{i}]'
            if not isinstance(row,dict) or set(row)!={'description','evidence','possibleInterpretations'}:fail(p+' keys mismatch');continue
            if not isinstance(row.get('description'),str) or not row['description'].strip():fail(p+'.description invalid')
            if not isinstance(row.get('evidence'),str) or row['evidence'].strip() not in source:fail(p+'.evidence not literal source')
            if not isinstance(row.get('possibleInterpretations'),list) or not all(isinstance(x,str) and x.strip() for x in row['possibleInterpretations']):fail(p+'.possibleInterpretations invalid')
    valid_objects=ids.get('objects',set())
    for coll in ('relations','actions'):
        for i,row in enumerate(doc.get(coll,[]) if isinstance(doc.get(coll),list) else []):
            if not isinstance(row,dict):continue
            for participant in row.get('participants',[]) if isinstance(row.get('participants'),list) else []:
                if isinstance(participant,dict) and participant.get('objectId') not in valid_objects:fail(f'{coll}[{i}] unknown participant {participant.get("objectId")}')
            if coll=='actions':
                if row.get('actorId') is not None and row['actorId'] not in valid_objects:fail(f'actions[{i}] unknown actor {row["actorId"]}')
                for x in row.get('resultIds',[]) if isinstance(row.get('resultIds'),list) else []:
                    if x not in valid_objects:fail(f'actions[{i}] unknown result {x}')
    return errors

SYSTEM=('Sei un estrattore ontologico documentale. Restituisci ESCLUSIVAMENTE un oggetto JSON conforme al contratto. '
        'Ontologia base: objects = referenti nominali espliciti; relations = fatti strutturali fra referenti; '
        'actions = comportamenti con attore, partecipanti, risultati e condizioni; ambiguities = lacune o incertezze. '
        'Rappresenta negazioni, guardie, sequenze temporali, modalità (richiesta diversa da esecuzione), forme passive. '
        'Non inventare fatti, tecnologie, destinatari o identità. Non trattare una mancanza di specifica come esistenza dimostrata. '
        'Per ogni evidence usa una sottostringa LETTERALE contigua del testo fonte. '
        'IDs locali O-001..., R-001..., A-001...; tutti i riferimenti agli oggetti devono esistere. '
        'Mantieni i fatti supportati anche se un partner li ha omessi. Nessuna spiegazione fuori JSON.')

def messages(source,test_id,own=None,peer=None,peer_name=None):
    user=('TEST ID: '+test_id+'\nTESTO FONTE (unica autorità fattuale):\n'+source+'\n\n'
          'Produci JSON completo con testId, objects, relations, actions, ambiguities. '
          'L\'estrazione deve essere completa, non un delta. evidence deve essere una citazione letterale contigua.\n')
    if own is not None:
        user+='\nTUO OUTPUT PRECEDENTE (per la revisione; non è fonte di verità):\n'+json.dumps(own,ensure_ascii=False)+'\n'
    if peer is not None:
        user+='\nOUTPUT DEL PARTNER '+peer_name+' (confronta criticamente; non è fonte di verità):\n'+json.dumps(peer,ensure_ascii=False)+'\n'
        user+='\nSei un revisore CRITICO: le proposte del partner sono ipotesi, non verità. Per ogni elemento contestato confronta evidence e significato con la fonte. RIFIUTA modifiche non supportate, conserva quelle corrette della tua versione, recupera omissioni solo se dimostrabili. Non introdurre fatti per raggiungere consenso. Rivedi TUTTI i fatti e restituisci JSON completo (non delta).\n'
    return [{'role':'system','content':SYSTEM},{'role':'user','content':user}]

def http_json(url,data=None,timeout=600):
    payload=None if data is None else json.dumps(data).encode('utf-8')
    req=urllib.request.Request(url,data=payload,headers={'Content-Type':'application/json'} if payload else {},method='POST' if payload else 'GET')
    with urllib.request.urlopen(req,timeout=timeout) as r:return json.loads(r.read().decode('utf-8'))

def invoke(base,model,msgs,source,test_id,attempts,timeout,seed,num_ctx,logpath):
    problems=[]
    last_raw=''
    for attempt in range(1,attempts+1):
        prompt=msgs[:]
        if problems:
            prompt=prompt+[{'role':'user','content':'La risposta precedente è INVALIDA. Restituisci l\'intero JSON corretto, senza testo extra. Errori:\n'+'\n'.join(problems[:40])+'\nRISPOSTA PRECEDENTE INVALIDA (estratto):\n'+last_raw[:12000]}]
        payload={'model':model,'messages':prompt,'stream':False,'format':SCHEMA,
                 'options':{'temperature':0,'seed':seed,'num_ctx':num_ctx},'keep_alive':'0'}
        raw_info={'attempt':attempt,'model':model,'request_sha256':hash_text(json.dumps(payload,sort_keys=True,ensure_ascii=False))}
        try:
            response=http_json(base.rstrip('/')+'/api/chat',payload,timeout)
            raw=response.get('message',{}).get('content','')
            last_raw=raw
            raw_info.update({'raw_content':raw,'ollama_metadata':{k:response.get(k) for k in ('model','created_at','done_reason','done','prompt_eval_count','eval_count','total_duration')}})
            try:
                parsed=json.loads(raw)
                problems=validate(parsed,source,test_id)
            except json.JSONDecodeError as exc:problems=['Invalid JSON: '+str(exc)]
            raw_info['validation_errors']=problems
        except (urllib.error.URLError,TimeoutError,ValueError) as exc:
            problems=['Ollama request failed: '+str(exc)]
            raw_info['validation_errors']=problems
        logpath.parent.mkdir(parents=True,exist_ok=True)
        with logpath.open('a',encoding='utf-8') as f:f.write(json.dumps(raw_info,ensure_ascii=False)+'\n')
        if not problems:return parsed,attempt
    raise RuntimeError(f'{model}: no valid JSON after {attempts} attempts; see {logpath}: {problems[:3]}')

def rotation(names, cycles=1):
    """Pilot: two models; each reviews the other exactly once."""
    if len(names)!=2 or len(set(names))!=2 or cycles!=1:
        raise ValueError('R3 pilot requires two distinct models and exactly one partner review')
    return [{'cycle':1,'target':names[0],'partner':names[1]},
            {'cycle':1,'target':names[1],'partner':names[0]}]

def unload(base, model, timeout=90):
    """Ask Ollama to unload resident model weights. This does not clear OS-managed RAM."""
    response=http_json(base.rstrip('/')+'/api/generate',
                       {'model':model,'prompt':'','stream':False,'keep_alive':0},timeout)
    gc.collect()
    return response.get('done', False)

def run(args):
    config=read_json(args.config);names=list(config['models'])
    if len(names)!=2 or len(set(names))!=2:raise ValueError('R3 pilot requires exactly two unique model keys')
    cycles=int(config.get('collaboration_cycles',1))
    steps=rotation(names,cycles)
    source=as_text(args.source)
    if not source.strip():raise ValueError('Empty source')
    output=pathlib.Path(args.output).resolve();output.mkdir(parents=True,exist_ok=True)
    fingerprint={'protocol_version':'R3_TWO_MODEL_SINGLE_PEER_COOLDOWN','test_id':args.test_id,'source_sha256':hash_text(source),
       'models':config['models'],'temperature':0,'seed':config.get('seed',42),
       'num_ctx':config.get('num_ctx',8192),'max_attempts':config.get('max_attempts',3),
       'collaboration_cycles':cycles,'cooldown_seconds':config.get('cooldown_seconds',120),'steps':steps,'schema_sha256':hash_text(json.dumps(SCHEMA,sort_keys=True))}
    manifest=output/'protocol.json'
    if manifest.exists():
        if read_json(manifest)!=fingerprint:raise ValueError('Run parameters differ from existing protocol; use new output directory')
    else:save_json(manifest,fingerprint)
    if not args.skip_preflight:
        tags=http_json(config.get('host','http://localhost:11434').rstrip('/')+'/api/tags',timeout=30)
        available={x.get('name') for x in tags.get('models',[])}|{x.get('model') for x in tags.get('models',[])}
        for alias,model in config['models'].items():
            if model not in available:raise RuntimeError(f'Missing Ollama model for {alias}: {model}. Run `ollama list` and correct config; no automatic pull.')
    def load_checked(path):
        doc=read_json(path);errors=validate(doc,source,args.test_id)
        if errors:raise ValueError(f'Invalid existing artifact {path}: {errors[:3]}')
        return doc
    def make(path,model,msgs,log):
        if path.exists():
            load_checked(path);print('SKIP '+str(path),flush=True);return
        print('RUN '+str(path),flush=True)
        try:
            doc,tries=invoke(config.get('host','http://localhost:11434'),config['models'][model],msgs,source,args.test_id,
                config.get('max_attempts',3),config.get('timeout_seconds',900),config.get('seed',42),config.get('num_ctx',8192),log)
            save_json(path,doc);print(f'PASS {model} attempts={tries}',flush=True)
        finally:
            try:
                unload(config.get('host','http://localhost:11434'),config['models'][model])
                print(f'UNLOAD requested for {model}',flush=True)
            except Exception as exc:
                print(f'WARNING: could not confirm Ollama unload for {model}: {exc}',flush=True)
                raise RuntimeError(f'Model unload failed: {model}') from exc
    for name in names:
        make(output/'initial'/(name+'.json'),name,messages(source,args.test_id),output/'logs'/('initial_'+name+'.jsonl'))
    # Two independent initial results finished; cool down before peer review.
    marker=output/'cooldown_completed.json'
    if not marker.exists():
        seconds=int(config.get('cooldown_seconds',120))
        if seconds < 120:raise ValueError('cooldown_seconds must be >= 120')
        print(f'COOLDOWN: {seconds} seconds before partner review',flush=True)
        time.sleep(seconds)
        save_json(marker,{'seconds':seconds,'phase':'between_initial_and_peer_review'})
    # Live state advances immediately after the first partner review.
    # Future partners can therefore see earlier corrections, intentionally.
    current={name:load_checked(output/'initial'/(name+'.json')) for name in names}
    for k,step in enumerate(steps,1):
        target,partner=step['target'],step['partner']
        dest=output/'steps'/f'{k:03d}_{target}_with_{partner}.json'
        if dest.exists():
            current[target]=load_checked(dest)
            print(f'SKIP step={k} {target} <- {partner}',flush=True)
            continue
        make(dest,target,messages(source,args.test_id,current[target],current[partner],partner),output/'logs'/f'step_{k:03d}_{target}_with_{partner}.jsonl')
        current[target]=load_checked(dest)
    final=output/'final';final.mkdir(exist_ok=True)
    for name in names:
        dest=final/(name+'.json')
        if dest.exists():
            if load_checked(dest)!=current[name]:raise ValueError(f'Existing final disagrees with completed steps: {dest}')
        else:save_json(dest,current[name])
    summary={'protocol':fingerprint,'initial':{},'final':{},'collaboration_steps':len(steps)}
    for name in names:
        for key,doc in (('initial',load_checked(output/'initial'/(name+'.json'))),('final',current[name])):
            summary[key][name]={k:len(doc[k]) for k in COLLS}
    save_json(output/'summary.json',summary)
    print(f'PASS: 2 initial + {len(steps)} partner revisions + 2 final JSON; 1 peer meeting per model',flush=True)

def check(args):
    config=read_json(args.config);names=list(config['models']);source=as_text(args.source)
    root=pathlib.Path(args.output); manifest=read_json(root/'protocol.json')
    steps=manifest['steps'];errs=[]
    for name in names:
        for stage in ('initial','final'):
            f=root/stage/(name+'.json')
            if not f.exists():errs.append('missing '+str(f));continue
            errs.extend(str(f)+': '+e for e in validate(read_json(f),source,args.test_id))
    for k,step in enumerate(steps,1):
        f=root/'steps'/f"{k:03d}_{step['target']}_with_{step['partner']}.json"
        if not f.exists():errs.append('missing '+str(f));continue
        errs.extend(str(f)+': '+e for e in validate(read_json(f),source,args.test_id))
    if errs:print('\n'.join(errs[:100]));raise SystemExit(1)
    print(f'PASS: {len(steps)+4} validated JSON files; 2 initial + {len(steps)} revisions + 2 final',flush=True)

def main():
    ap=argparse.ArgumentParser(description=__doc__);sp=ap.add_subparsers(dest='cmd',required=True)
    for cmd in ('run','check'):
        p=sp.add_parser(cmd);p.add_argument('--config',default=str(HERE/'models.example.json'));p.add_argument('--source',required=True)
        p.add_argument('--test-id',default='ONT-T01');p.add_argument('--output',required=True)
        if cmd=='run':p.add_argument('--skip-preflight',action='store_true')
    args=ap.parse_args()
    (run if args.cmd=='run' else check)(args)
if __name__=='__main__':main()
