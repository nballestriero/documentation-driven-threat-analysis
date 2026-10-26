#!/usr/bin/env python3
"""Read-only exhaustive record inventory and candidate finding reference validation.
Run from repository or anywhere; discovers project root from script location.
"""
import csv, json, pathlib, sys
here=pathlib.Path(__file__).resolve().parent
base=here.parent/'E1_E2'
models=['DEEPSEEK','QWEN','MISTRAL']
findings=here/'ONT_T01_E3_V1_EXTRA_GOLD_FINDINGS_CANDIDATE_R1.csv'
out=here/'ONT_T01_E3_V1_EXTRA_GOLD_INVENTORY_R1.csv'
items=[];known={}
for m in models:
    p=base/f'ONT_T01_ORA_V1_{m}_ORIGINAL.json'
    data=json.loads(p.read_text(encoding='utf-8'))
    seen=set()
    for coll in ('objects','relations','actions','ambiguities'):
        for ix,record in enumerate(data[coll]):
            rid=record.get('id') if coll!='ambiguities' else f'ambiguities[{ix}]'
            if not rid or (coll,rid) in seen:raise ValueError(f'duplicate/missing id {m} {coll} {rid}')
            seen.add((coll,rid));known[(m,coll,rid)]=record
            items.append(dict(model=m,collection=coll,record_id=rid,record_index=ix,
                 review_status='NOT_YET_SEMANTICALLY_ADJUDICATED',extra_claim_status='NOT_ASSESSED',
                 reviewer='',review_note=''))
with findings.open(encoding='utf-8',newline='') as f:
    fr=list(csv.DictReader(f))
for x in fr:
    key=(x['model'],x['collection'],x['record_id'])
    if key not in known:raise ValueError(f'Unknown finding reference {key}')
    if x['review_status']!='REVIEW_CANDIDATE':raise ValueError('unexpected status')
with out.open('w',encoding='utf-8',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(items[0]));writer.writeheader();writer.writerows(items)
from collections import Counter
c=Counter(x['model'] for x in items)
print(f'PASS: {len(items)} original records inventoried; {len(fr)} candidate findings with valid references; no historical inputs rewritten; {dict(c)}')
