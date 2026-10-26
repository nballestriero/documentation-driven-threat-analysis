#!/usr/bin/env python3
"""Generate full 64-row candidate comparison from tracked original repository data."""
import csv, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
HERE=Path(__file__).resolve().parent
GOLD=ROOT/'research/ontology/ONT_T01_GOLD_FACTS_R3.csv'
ORIG=ROOT/'research/ontology/experiments/ONT_T01/E1_E2'
DEEP=HERE/'ONT_T01_E3_DEEPSEEK_PILOT_MATCH_R1.csv'
CAND=HERE/'ONT_T01_E3_V1_QWEN_MISTRAL_CANDIDATE_R1.csv'
OUT=HERE/'ONT_T01_E3_V1_COMPARATIVE_MATRIX_R1.csv'
def read(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def refok(raw,ref):
 if re.fullmatch(r'ambiguities\[\d+\]',ref):return int(ref[12:-1]) < len(raw['ambiguities'])
 for k in ('objects','relations','actions'):
  if any(e['id']==ref for e in raw[k]):return True
 return False
G=read(GOLD);D={r['gold_id']:r for r in read(DEEP)};C={r['gold_id']:r for r in read(CAND)}
expected={f'R3-{i:03d}' for i in range(1,65)}
assert {x['id'] for x in G}==expected and set(D)==expected and set(C)==expected,'Gold/pilot/candidate coverage mismatch'
raw={m:json.loads((ORIG/f'ONT_T01_ORA_V1_{m}_ORIGINAL.json').read_text(encoding='utf-8')) for m in ('DEEPSEEK','QWEN','MISTRAL')}
cols=['gold_id','dimension','scoring_layer','gold_fact','gold_qualification','gold_evidence','deepseek_assessment_historic','deepseek_ids','qwen_assessment_candidate','qwen_ids','mistral_assessment_candidate','mistral_ids','review_status']
with OUT.open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
 for g in G:
  k=g['id'];d=D[k];c=C[k]
  for model,cell in [('DEEPSEEK',d['extracted_ids']),('QWEN',c['qwen_extracted_ids']),('MISTRAL',c['mistral_extracted_ids'])]:
   for ref in filter(None,cell.split(';')):
    assert refok(raw[model],ref),(k,model,ref)
  assert c['qwen_assessment_candidate'] in ('MATCH','PARTIAL','MISSING','REVIEW_REQUIRED')
  assert c['mistral_assessment_candidate'] in ('MATCH','PARTIAL','MISSING','REVIEW_REQUIRED')
  w.writerow(dict(gold_id=k,dimension=g['dimension'],scoring_layer=g['scoring_layer'],gold_fact=g['fact'],gold_qualification=g['qualification'],gold_evidence=g['evidence'],deepseek_assessment_historic=d['assessment'],deepseek_ids=d['extracted_ids'],qwen_assessment_candidate=c['qwen_assessment_candidate'],qwen_ids=c['qwen_extracted_ids'],mistral_assessment_candidate=c['mistral_assessment_candidate'],mistral_ids=c['mistral_extracted_ids'],review_status='REVIEW_CANDIDATE'))
print('PASS: 64 Gold units, 3 original JSON files, IDs valid, historical DeepSeek preserved; created',OUT)
