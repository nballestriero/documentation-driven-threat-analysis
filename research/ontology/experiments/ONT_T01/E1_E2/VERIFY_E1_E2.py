#!/usr/bin/env python3
"""Recheck E1/E2 originals and frozen checks. Requires Python 3.9+."""
import json, hashlib, csv, pathlib, collections, sys
root=pathlib.Path(__file__).resolve().parent
checks=json.loads((root/'ONT_T01_E1_E2_CHECKS_R1.json').read_text(encoding='utf-8'))
source=(root/'SOURCE_ONT_T01_R3.txt').read_text(encoding='utf-8').strip()
for model,expected in checks.items():
 p=root/('ONT_T01_ORA_V1_'+model.upper()+'_ORIGINAL.json');raw=p.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==expected['sha256'], ('SHA mismatch',model)
 d=json.loads(raw); assert d.get('testId')=='ONT-T01'
 assert all(isinstance(d.get(k),list) for k in ('objects','relations','actions','ambiguities'))
 assert {k:len(d[k]) for k in ('objects','relations','actions','ambiguities')}==expected['counts']
 ids=[v['id'] for group in ('objects','relations','actions') for v in d[group]]
 assert [x for x,n in collections.Counter(ids).items() if n>1]==expected['duplicate_ids']
 objids={v['id'] for v in d['objects']};broken=[];unevid=[];nrefs=0
 for group in ('objects','relations','actions','ambiguities'):
  for i,v in enumerate(d[group],1):
   if not isinstance(v.get('evidence'),str) or v['evidence'] not in source:unevid.append({'section':group,'id':v.get('id','ambiguity-index-'+str(i)),'evidence':v.get('evidence')})
   refs=[]
   if group in ('relations','actions'): refs +=[t.get('objectId') for t in v.get('participants',[])]
   if group=='actions': refs += ([v['actorId']] if v.get('actorId') else []) +v.get('resultIds',[])
   for ref in refs:
    if ref is not None:
     nrefs+=1
     if ref not in objids:broken.append([group,v.get('id'),ref])
 assert broken==expected['dangling_refs'] and unevid==expected['nonliteral_evidence'] and nrefs==expected['references_checked'], model
 print('PASS',model,expected['counts'],'nonliteral evidence:',len(unevid))
print('PASS E1/E2: three archived originals; Gemini NOT CHECKED')
