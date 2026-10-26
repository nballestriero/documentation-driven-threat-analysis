#!/usr/bin/env python3
"""Verify final candidate Gold matching without changing historical inputs."""
import csv, pathlib
D=pathlib.Path(__file__).resolve().parent
records=list(csv.DictReader((D/'ONT_T01_V1_V2_GOLD_COMPARISON_R1.csv').open(encoding='utf-8-sig',newline='')))
metrics=list(csv.DictReader((D/'ONT_T01_V1_V2_STRATIFIED_METRICS_R1.csv').open(encoding='utf-8-sig',newline='')))
assert len(records)==64 and {r['gold_id'] for r in records}=={f'R3-{i:03d}' for i in range(1,65)}
assert len(metrics)==18
W={'MATCH':1,'PARTIAL':0.5,'MISSING':0,'REVIEW_REQUIRED':0.5}
for model in ('DEEPSEEK','QWEN','MISTRAL'):
 for metric in [r for r in metrics if r['model']==model]:
  subs=[r for r in records if r['scoring_layer']==metric['layer']]
  assert len(subs)==int(metric['units'])
  for ver,col in [('v1','v1'),('v2','v2_candidate')]:
   vals=[r[model.lower()+'_'+col] for r in subs]
   for lab in ('MATCH','PARTIAL','MISSING'):
    assert vals.count(lab)==int(metric[ver+'_'+lab.lower()])
   assert abs(sum(W[v] for v in vals)/len(vals)*100-float(metric[ver+'_index_pct']))<0.011
  assert abs(float(metric['v2_index_pct'])-float(metric['v1_index_pct'])-float(metric['delta_pp']))<0.03
print('PASS: 64 Gold units; 18 stratified metrics; 3 model candidate comparisons; historical sources not modified')
