from pathlib import Path
import csv,json
p=Path(__file__).resolve().parent
repo=p.parent
fn=p/'ONT_T01_E3_V1_EXTRA_GOLD_SEMANTIC_ASSESSMENT_R3.csv'
rows=list(csv.DictReader(fn.open(encoding='utf-8-sig',newline='')))
assert len(rows)==190
models={'DEEPSEEK':(34,7,17,2),'QWEN':(31,13,20,3),'MISTRAL':(31,9,18,5)}
for model,(o,r,a,u) in models.items():
    orig=repo/'E1_E2'/f'ONT_T01_ORA_V1_{model}_ORIGINAL.json'
    data=json.loads(orig.read_text(encoding='utf-8-sig'))
    assert tuple(len(data[x]) for x in ['objects','relations','actions','ambiguities'])==(o,r,a,u)
    expected={(col,(f'ambiguities[{i}]' if col=='ambiguities' else x['id'])) for col in ['objects','relations','actions','ambiguities'] for i,x in enumerate(data[col])}
    actual={(z['collection'],z['record_id']) for z in rows if z['model']==model}
    assert expected==actual and len(actual)==o+r+a+u
assert all(z['assessment_stage']=='SINGLE_REVIEW_CANDIDATE' and z['independent_confirmation']=='PENDING' for z in rows)
assert sum(z['record_level_assessment']=='POTENTIALLY_UNSUPPORTED' for z in rows)==1
print('PASS: 190/190 candidate semantic assessments; real original IDs; independent review pending; no original files rewritten')
