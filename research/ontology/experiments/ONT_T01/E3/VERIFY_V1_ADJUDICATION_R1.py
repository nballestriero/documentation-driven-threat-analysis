import csv
from pathlib import Path
p=Path(__file__).parent/'ONT_T01_E3_V1_ADJUDICATION_CANDIDATES_R1.csv'
r=list(csv.DictReader(p.open(encoding='utf-8',newline='')))
assert len(r)==8
assert len(set(x['finding_id'] for x in r))==8
assert all(x['decision_status'] in {'RECOMMEND_CANDIDATE','KEEP_CANDIDATE','EXTRA_GOLD_AUDIT_OPEN'} for x in r)
print('PASS: eight candidate adjudication records; historical files untouched by verifier')
