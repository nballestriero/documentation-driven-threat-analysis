#!/usr/bin/env python3
"""Create three identical-content one-round peer review prompts using LOCAL original V1 JSONs."""
import csv, json, hashlib, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parents[5]
E12 = ROOT / 'research/ontology/experiments/ONT_T01/E1_E2'
E3 = ROOT / 'research/ontology/experiments/ONT_T01/E3'
OUT = pathlib.Path(__file__).resolve().parent
TEXT = '''Una piattaforma di commercio elettronico permette ai clienti di acquistare prodotti disponibili nel catalogo. Ogni prodotto possiede un identificativo, una descrizione e un prezzo. Il catalogo viene mantenuto dal Catalog Service, mentre le informazioni sulla disponibilità sono conservate nell'Inventory Store.

Quando un cliente conferma un acquisto, l'Order Service riceve la richiesta contenente l'identificativo del cliente, i prodotti selezionati e le quantità richieste. L'Order Service verifica la disponibilità interrogando l'Inventory Service, che consulta l'Inventory Store e restituisce le quantità disponibili.

Se tutti i prodotti richiesti sono disponibili, l'Order Service crea un ordine e lo registra nell'Order Store. Successivamente richiede al Payment Service l'autorizzazione del pagamento. Il Payment Service comunica con un Payment Provider esterno e restituisce l'esito dell'autorizzazione.

Quando il pagamento viene autorizzato, l'Order Service richiede all'Inventory Service di riservare le quantità ordinate. Dopo la conferma della riserva, l'ordine assume lo stato Confirmed e viene inviata una notifica al cliente tramite il Notification Service.

Se il pagamento non viene autorizzato, l'ordine viene contrassegnato come Rejected. Se la disponibilità è insufficiente, la richiesta viene rifiutata prima di contattare il Payment Service.

Il Payment Provider è gestito da un'organizzazione esterna. La piattaforma utilizza il suo servizio, ma non ne gestisce l'infrastruttura. La documentazione non specifica il protocollo di comunicazione utilizzato né il meccanismo di annullamento delle autorizzazioni di pagamento.'''
INSTRUCTIONS = '''# ONT-T01 V2 — SINGLE-ROUND MULTI-PEER REVIEW

Sei uno dei tre analisti LLM che svolgono una seconda estrazione indipendente condizionata alla visione simultanea di tre estrazioni precedenti. Devi completare L'INTERO lavoro in questa unica risposta. Non attendere un secondo prompt.

## Compito
Leggi il TESTO FONTE e i tre JSON V1 (DeepSeek, Qwen, Mistral). Sono tre ipotesi fallibili, non fonti di verità. Analizza tutti i campi, comprese identità, ruoli/participants, condizioni, evidence e uncertainty. Confronta criticamente tutti e tre i JSON in un solo passaggio: errori di commissione, omissioni, confusione tra concetti, modalità, negazione, ruoli non documentati, temporalità. NON ricevi il Gold Standard.

Usa SOLO il testo fonte per decidere cosa sia attestato. Non scambiare richiesta, esecuzione e conferma della riserva; non scambiare capacità con evento avvenuto; non inventare attori delle azioni passive. In particolare, la fonte non afferma l'equivalenza tra quantità richieste e quantità ordinate. Non dedurre protocolli, rollback, mittenti o infrastrutture non esplicitati. Incertezze reali vanno espresse come incertezze, non come fatti positivi.

## Output obbligatorio in questa stessa risposta
1. Un blocco JSON valido `review_findings` con una lista di finding. Ogni finding deve avere `findingId`, `targetModel` (DEEPSEEK/QWEN/MISTRAL), `targetCollection` (objects/relations/actions/ambiguities), `targetRecordId` (per ambiguities usare `ambiguities[0]` etc.), `issueType` (SUPPORTED_CORRECTION / OMISSION / UNSUPPORTED / CONTRADICTED / IDENTITY / MODALITY / CONDITION / OTHER), `explanation`, `exactSourceEvidence` (citazione contigua esatta dalla fonte oppure stringa vuota se non esiste), `suggestedCorrection`. Non inventare ID storici.
2. Un blocco JSON valido `v2_extraction` completo con esattamente le chiavi `testId`, `objects`, `relations`, `actions`, `ambiguities`, mantenendo una struttura compatibile con i JSON V1 (id, name, candidateCategory, evidence, uncertainty per oggetti; id, description, participants, evidence, uncertainty per relazioni; id, verb, actorId, participants, resultIds, condition, evidence, uncertainty per azioni). Usa ID nuovi O-001..., R-001..., A-001... INTERNI ALLA TUA V2, non riutilizzare gli ID per fingere continuità; traccia le corrispondenze nel blocco 3.
3. Un blocco JSON valido `change_log` con lista di cambiamenti `changeId`, `newV2RecordId`, `changeType` (ADDED/CORRECTED/REMOVED/UNCHANGED), `relatedV1` (array di stringhe tipo `QWEN:actions:A-016`), `reason`, `contributionAttribution` (OWN_REANALYSIS / INFORMED_BY_DEEPSEEK / INFORMED_BY_QWEN / INFORMED_BY_MISTRAL / MULTIPLE / UNDETERMINED), `attributionExplanation`. Le attribuzioni sono descrittive, NON provano causalità.
4. Un breve riepilogo dei principali miglioramenti e possibili regressioni.

Non ridurre arbitrariamente la completezza per brevità. Non produrre giudizi sul Gold Standard. Non utilizzare codice eseguibile per sostituire il contenuto JSON. Se la chat limita la lunghezza, priorità al JSON `v2_extraction` completo e poi agli altri blocchi; dichiara chiaramente l'eventuale troncamento.
'''


def validate_original(path):
    content=path.read_text(encoding='utf-8-sig')
    j=json.loads(content)
    if not all(isinstance(j.get(k),list) for k in ('objects','relations','actions','ambiguities')):raise ValueError(f'Not valid ORA: {path}')
    for k in ('objects','relations','actions'):
        ids=[x['id'] for x in j[k]]
        if len(ids)!=len(set(ids)):raise ValueError('Duplicate ids '+str(path))
    return j,content


def main():
    originals={}
    for model in ('DEEPSEEK','QWEN','MISTRAL'):
        p=E12 / f'ONT_T01_ORA_V1_{model}_ORIGINAL.json'
        if not p.exists():raise SystemExit(f'ERROR original missing: {p}')
        originals[model]=validate_original(p)
    matrix=E3/'ONT_T01_E3_V1_COMPARATIVE_MATRIX_R1.csv'
    if not matrix.exists():raise SystemExit('ERROR missing comparison matrix')
    rows=list(csv.DictReader(matrix.open(encoding='utf-8-sig',newline='')))
    if len(rows)!=64:raise SystemExit(f'ERROR expected 64 Gold check units; got {len(rows)}')
    assessments=E3/'ONT_T01_E3_V1_EXTRA_GOLD_SEMANTIC_ASSESSMENT_R3.csv'
    assessment_note='R3 semantic candidate file not present locally: excluded from aggregated summary.'
    counter={}
    if assessments.exists():
        ar=list(csv.DictReader(assessments.open(encoding='utf-8-sig',newline='')))
        if len(ar)!=190:raise SystemExit(f'ERROR R3 assessment has {len(ar)} records; expected 190')
        field='assessment' if 'assessment' in ar[0] else next((c for c in ar[0] if 'class' in c.lower() or 'conclusion' in c.lower() or 'status' in c.lower()),None)
        counter=dict(collections.Counter((r.get('model',''),r.get(field,'')) for r in ar)) if field else {}
        assessment_note='R3 semantic candidate file present locally: 190 records; status REVIEW CANDIDATE. Counts by source columns are not approved metrics.'
    dists={model:dict(collections.Counter((r[col] or 'BLANK') for r in rows)) for model,col in [('DEEPSEEK','deepseek_assessment_historic'),('QWEN','qwen_assessment_candidate'),('MISTRAL','mistral_assessment_candidate')]}
    lines=['# ONT-T01 — Chiusura V1 provvisoria e avvio V2', '', '**Status: REVIEW CANDIDATE — baseline sperimentale non validata indipendentemente.**', '','## Fonti operative', '', '- 3 JSON originali V1 (immutati)', '- Gold R3: 64 unità di verifica sovrapposte, NON 64 osservazioni indipendenti', '- Matrice comparativa V1: giudizi storici DeepSeek e candidati per Qwen/Mistral',f'- {assessment_note}', '- PR-10 blind independent review: NON ESEGUITA; non dichiarare riproducibilità dimostrata', '', '## Conteggi descrittivi delle etichette nella matrice V1', '', '| Modello | MATCH | PARTIAL | MISSING | Altro |','|---|---:|---:|---:|---:|']
    for m in ('DEEPSEEK','QWEN','MISTRAL'):
        d=dists[m];other=sum(v for k,v in d.items() if k not in ('MATCH','PARTIAL','MISSING'))
        lines.append(f'| {m} | {d.get("MATCH",0)} | {d.get("PARTIAL",0)} | {d.get("MISSING",0)} | {other} |')
    lines+=['', 'I conteggi sono etichette per unità di verifica e NON tassi di accuratezza. I giudizi semantici restano candidati e alcuni richiedono riconciliazione.','', '## Limiti non bloccanti V2', '', '- Qwen A-016: possibile inferenza non documentata di esecuzione autonoma della riserva.', '- Potenziale fusione quantità ordinate/richieste e perdita di modalità temporali.', '- Controllo PR-10 indipendente e adjudication atomica non conclusi.', '- Le citazioni evidence rappresentano provenienza, non provano che la semantica sia codificata nei campi.', '', '## Protocollo V2', '', 'Una singola esecuzione per modello, ciascuno riceve lo stesso testo e tutti e tre i JSON V1. Nessuna risposta V2 precedente è visibile ad altri modelli. Tre output totali; Gold e giudizi di valutazione esclusi dall’input. Confronto finale V1-V2 separato per categorie e regressioni. Attribuzione contributi dichiarativa, non causale.','']
    (OUT/'ONT_T01_V1_PROVISIONAL_CLOSURE_R1.md').write_text('\n'.join(lines),encoding='utf-8')
    manifest={'protocol':'ONT_T01_V2_SINGLE_ROUND_R1','status':'READY_FOR_EXTERNAL_LLM_EXECUTION','review_model_runs':3,'gold_in_prompt':False,'inputs':{k:{'sha256':hashlib.sha256(s.encode('utf-8')).hexdigest(),'counts':{c:len(j[c]) for c in ('objects','relations','actions','ambiguities')}} for k,(j,s) in originals.items()}}
    full='\n\n## TESTO FONTE (unica fonte di verità)\n\n'+TEXT+'\n\n## TRE ESTRAZIONI ORIGINALI V1 (ipotesi da criticare)\n'
    for m,(j,s) in originals.items():full+=f'\n### {m} V1\n```json\n'+s+'\n```\n'
    for m in originals:
        prompt=INSTRUCTIONS+f'\n## Identità del revisore\nSei {m}. Non alterare il protocollo in base alla tua identità.\n'+full
        (OUT/f'ONT_T01_V2_PROMPT_{m}_R1.txt').write_text(prompt,encoding='utf-8')
        manifest.setdefault('prompts',{})[m]={'file':f'ONT_T01_V2_PROMPT_{m}_R1.txt','sha256':hashlib.sha256(prompt.encode('utf-8')).hexdigest()}
    (OUT/'ONT_T01_V2_MANIFEST_R1.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS: three full V2 prompts built from three actual original JSON files; 64 matrix rows; Gold excluded; no originals overwritten')
    print('Counts:',{m:manifest['inputs'][m]['counts'] for m in originals})
    print('R3 status:',assessment_note)

if __name__=='__main__':main()
