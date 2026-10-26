from pathlib import Path
import csv
here=Path(__file__).resolve().parent
p=here/'ONT_T01_E3_V1_EXTRA_GOLD_REVIEW_WORKLIST_R2.csv'
with p.open(encoding='utf-8-sig',newline='') as f:r=list(csv.DictReader(f))
assert len(r)==190
assert sum(x['candidate_finding']=='YES' for x in r)==13
assert all(x['record_review_status']=='PENDING_HUMAN_SEMANTIC_REVIEW' and x['record_conclusion']=='NOT_ASSESSED' for x in r)
print('PASS: full worklist created; 13 linked; no record falsely declared reviewed')
