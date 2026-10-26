#!/usr/bin/env python3
"""Create blind candidate Gold-scoring sheet; score manually adjudicated judgments."""
import argparse,csv,json,pathlib,collections
MODELS=['nuextra_tiny','qwen25_coder_3b','llama32_3b','qwen25_7b']
SCORES={'MATCH':1.0,'PARTIAL':0.5,'MISSING':0.0}

def main():
    p=argparse.ArgumentParser();sp=p.add_subparsers(dest='cmd',required=True)
    x=sp.add_parser('prepare');x.add_argument('--gold-matrix',required=True);x.add_argument('--output',required=True)
    x=sp.add_parser('score');x.add_argument('--sheet',required=True);x.add_argument('--output',required=True)
    a=p.parse_args()
    if a.cmd=='prepare':
        with open(a.gold_matrix,encoding='utf-8-sig',newline='') as f: gold=list(csv.DictReader(f))
        if not gold or not {'gold_id','dimension','gold_fact','gold_evidence'}<=gold[0].keys():raise ValueError('Expected ONT-T01 E3 Gold matrix format')
        if len(gold)!=64:raise ValueError('Expected exactly 64 Gold units')
        rows=[]
        for g in gold:
            for alias in MODELS:
                for version in ('V1','V2'):
                    rows.append({'gold_id':g['gold_id'],'dimension':g['dimension'],'gold_fact':g['gold_fact'],
                                 'gold_evidence':g['gold_evidence'],'model':alias,'version':version,
                                 'assessment':'','matched_ids':'','reason':'','review_status':'PENDING'})
        fieldnames=list(rows[0]);pathlib.Path(a.output).parent.mkdir(parents=True,exist_ok=True)
        with open(a.output,'w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fieldnames);w.writeheader();w.writerows(rows)
        print('PASS: 512 blank judgments (64 Gold x 4 LLM x V1/V2); NO scores fabricated')
    else:
        with open(a.sheet,encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
        if len(rows)!=512:raise ValueError('Expected 512 judgments')
        groups=collections.defaultdict(list);keys=set()
        for r in rows:
            key=(r['gold_id'],r['model'],r['version'])
            if key in keys:raise ValueError('Duplicate '+str(key))
            keys.add(key)
            if r['assessment'] not in SCORES:raise ValueError('Missing/invalid assessment '+str(key))
            if r['review_status'] not in ('REVIEWED','APPROVED'):raise ValueError('Unreviewed '+str(key))
            groups[(r['model'],r['version'],r['dimension'])].append(SCORES[r['assessment']])
        result=[]
        for (model,version,dimension),v in sorted(groups.items()):
            result.append({'model':model,'version':version,'dimension':dimension,'n_gold_units':len(v),
                           'candidate_coverage_index_percent':round(100*sum(v)/len(v),4)})
        by=collections.defaultdict(dict)
        for r in result:by[(r['model'],r['version'])][r['dimension']]=r['candidate_coverage_index_percent']
        for (model,version),d in by.items():
            if not {'O','R','A'}<=d.keys():raise ValueError('Missing O/R/A for '+model+' '+version)
            result.append({'model':model,'version':version,'dimension':'BALANCED_ORA','n_gold_units':'OVERLAPPING',
                           'candidate_coverage_index_percent':round(sum(d[x] for x in ('O','R','A'))/3,4)})
        pathlib.Path(a.output).write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
        print('PASS: manually reviewed 512 judgments scored; N/polarity kept separate')
if __name__=='__main__':main()
