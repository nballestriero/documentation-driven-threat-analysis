#!/usr/bin/env python3
"""Non distruttivo: worklist dei 190 record, nessuna inferenza automatica SUPPORTED."""
from pathlib import Path
import csv, json, sys
here=Path(__file__).resolve().parent
inv=here/'ONT_T01_E3_V1_EXTRA_GOLD_INVENTORY_R1.csv'
tri=here/'ONT_T01_E3_V1_EXTRA_GOLD_TRIAGE_R2.csv'
out=here/'ONT_T01_E3_V1_EXTRA_GOLD_REVIEW_WORKLIST_R2.csv'
base=here.parent/'E1_E2'
with inv.open(encoding='utf-8-sig',newline='') as f: original=list(csv.DictReader(f))
with tri.open(encoding='utf-8-sig',newline='') as f: triage=list(csv.DictReader(f))
assert len(original)==190, f'inventory expected 190: {len(original)}'
assert len(triage)==13 and len({(r['model'],r['collection'],r['record_id']) for r in triage})==13
bykey={(x['model'],x['collection'],x['record_id']):x for x in triage}
assert all((r['model'],r['collection'],r['record_id']) in {(x['model'],x['collection'],x['record_id']) for x in original} for r in triage)
model_paths={m:base/f'ONT_T01_ORA_V1_{m}_ORIGINAL.json' for m in ('DEEPSEEK','QWEN','MISTRAL')}
models={m:json.loads(p.read_text(encoding='utf-8-sig')) for m,p in model_paths.items()}
assert {m:sum(x['model']==m for x in original) for m in models}=={'DEEPSEEK':60,'QWEN':67,'MISTRAL':63}
output=[]
for r in original:
 m,coll,rid=r['model'],r['collection'],r['record_id']; idx=int(r['record_index']);rec=models[m][coll][idx]
 assert (f'ambiguities[{idx}]' if coll=='ambiguities' else rec['id'])==rid,(m,coll,rid)
 key=(m,coll,rid);f=bykey.get(key)
 output.append({'model':m,'collection':coll,'record_id':rid,'record_index':idx,
  'candidate_finding': 'YES' if f else 'NO',
  'triage_disposition':f['proposed_disposition'] if f else '',
  'content_summary':rec.get('name') or rec.get('description') or rec.get('verb') or '',
  'record_review_status':'PENDING_HUMAN_SEMANTIC_REVIEW',
  'claim_count_confirmed':'','reviewer':'','review_note':'',
  'record_conclusion':'NOT_ASSESSED'})
with out.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=output[0].keys());w.writeheader();w.writerows(output)
print('PASS: 190/190 verified and indexed; 13 triage findings linked; worklist pending individual review; original JSON unchanged')
