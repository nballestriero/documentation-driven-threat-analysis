import csv,json,hashlib,pathlib,sys
base=pathlib.Path(__file__).resolve().parent
repo=base.parents[4] # repo root? E3=.../research/ontology/experiments/ONT_T01/E3; parents[4] is repo
orig=repo/'research/ontology/experiments/ONT_T01/E1_E2/ONT_T01_ORA_V1_DEEPSEEK_ORIGINAL.json'
gold=repo/'research/ontology/ONT_T01_GOLD_FACTS_R3.csv'
rows=list(csv.DictReader((base/'ONT_T01_E3_DEEPSEEK_PILOT_MATCH_R1.csv').open(encoding='utf-8',newline='')))
g=list(csv.DictReader(gold.open(encoding='utf-8',newline='')))
d=json.load(orig.open(encoding='utf-8')); ids={x['id'] for key in ('objects','relations','actions') for x in d[key]}
assert len(rows)==len(g)==64
assert {x['gold_id'] for x in rows}=={x['id'] for x in g}
assert len({x['gold_id'] for x in rows})==64
sha=(base/'ONT_T01_E3_PILOT_INPUT_SHA256_R1.txt').read_text().split()[0]
assert hashlib.sha256(orig.read_bytes()).hexdigest()==sha
for row in rows:
 assert row['assessment'] in ('MATCH','PARTIAL','MISSING')
 assert row['review_status']=='PROVISIONAL_NEEDS_HUMAN_REVIEW'
 for ref in filter(None,row['extracted_ids'].split(';')):
  assert ref in ids or ref in ('ambiguities[0]','ambiguities[1]'),ref
print('PASS E3 DeepSeek pilot: 64 gold rows, valid refs, SHA256 unchanged, all assessments provisional')
