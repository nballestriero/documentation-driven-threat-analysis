import csv,hashlib,json,pathlib,sys
repo=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(__file__).resolve().parents[5]
base=repo/'research/ontology/experiments/ONT_T01'; e=base/'E3'; orig=base/'E1_E2/ONT_T01_ORA_V1_DEEPSEEK_ORIGINAL.json'
def read(path):
 with path.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
pilot=read(e/'ONT_T01_E3_DEEPSEEK_PILOT_MATCH_R1.csv');blind=read(e/'ONT_T01_E3_PR10_BLIND_SAMPLE_R1.csv');delta=read(e/'ONT_T01_E3_PR08_REASSESSMENT_CANDIDATE_R1.csv');rec=read(e/'ONT_T01_E3_PR10_RECONCILIATION_TEMPLATE_R1.csv')
assert len(pilot)==64 and len(blind)==len(rec)==23 and len(delta)==1
p={x['gold_id']:x for x in pilot}
assert len(set(x['gold_id'] for x in blind))==23
assert sum(p[x['gold_id']]['assessment']=='PARTIAL' for x in blind)==9
assert sum(p[x['gold_id']]['assessment']=='MATCH' for x in blind)==14
assert all(x['independent_assessment']=='' and x['extracted_ids']=='' for x in blind)
assert all(x['independent_assessment']=='' and x['adjudicated_assessment']=='' for x in rec)
assert delta[0]['gold_id']=='R3-057' and p['R3-057']['assessment']=='PARTIAL' and delta[0]['candidate_assessment']=='MISSING'
d=json.loads(orig.read_text(encoding='utf-8'));assert len(d['objects'])==34 and len(d['actions'])==17
print('PASS PR08/PR10: input readable; 9 PARTIAL + 14 MATCH sampled; independent annotations empty; historic pilot unchanged by script')
