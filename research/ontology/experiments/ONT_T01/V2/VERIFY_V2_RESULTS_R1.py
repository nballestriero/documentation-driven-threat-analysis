from pathlib import Path
import json,csv
here=Path(__file__).resolve().parent
models=('DEEPSEEK','QWEN','MISTRAL')
summary=json.loads((here/'ONT_T01_V2_STRUCTURAL_CHECK_R1.json').read_text(encoding='utf-8'))
rows=list(csv.DictReader((here/'ONT_T01_V2_ALL_RECORDS_VERIFICATION_R1.csv').open(encoding='utf-8',newline='')))
for m in models:
 extraction=json.loads((here/f'ONT_T01_V2_{m}_EXTRACTION_R1.json').read_text(encoding='utf-8'))
 findings=json.loads((here/f'ONT_T01_V2_{m}_REVIEW_FINDINGS_R1.json').read_text(encoding='utf-8'))
 changes=json.loads((here/f'ONT_T01_V2_{m}_CHANGE_LOG_R1.json').read_text(encoding='utf-8'))
 assert len(findings['review_findings'])==summary[m]['findings']
 assert len(changes['change_log'])==summary[m]['changes']
 assert not summary[m]['invalid_refs'],(m,summary[m]['invalid_refs'])
 for key in ('objects','relations','actions','ambiguities'):
  assert len(extraction[key])==summary[m]['n'][key]
 assert sum(r['model']==m for r in rows)==sum(summary[m]['n'].values())
print(f"PASS: all three V2 JSONs; {len(rows)} V2 records; internal links valid; full raw responses retained")
for m in models:
 print(m,'nonliteral evidence',len(summary[m]['nonliteral_evidence']),'finding reference anomalies',len(summary[m]['invalid_finding_targets']),'finding-id anomalies',summary[m]['invalid_finding_ids'])
