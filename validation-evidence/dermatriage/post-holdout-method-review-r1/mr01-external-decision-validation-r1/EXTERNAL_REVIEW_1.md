PROMPT\_EXTERNAL\_ANALYST\_R1.md esegui il promt che leggia sinistra. ti ho decompresso lo zip e appiattito la sturttura

We need answer to user. Need execute prompt. We are external analyst. Need produce report following structure. We have all files in prompt. Need reconstruct MR-01 Decision candidates from supplied package only. We must not use internal answers. We haven't seen internal. Need produce self-contained report. Need likely in English? User Italian: "esegui il promt che leggia sinistra. ti ho decompresso lo zip e appiattito la sturttura" Means "execute the prompt you read on left. I extracted zip and flattened structure". So we need act as external analyst, produce report. Need follow PROMPT\_EXTERNAL\_ANALYST\_R1.md. Need include sections. Need decide Decision candidates for MR-01 only.

We need deeply analyze sources. Need identify commitments under MR-01 "Valutazione di triage del caso dermatologico" — determine urgency and operational priority from available info, including no image symptom path. Scope OUT destination specialist, medical validation/correction, adaptation. Need Decisions under MR-01 from original docs. We need not include MR-02/03/04 decisions. Need classify. We must use R5/R6. Need be careful.

Let's parse original docs. DermaTriage architecture: four-stage AI pipeline. Stage 1 EfficientNet-B4 classifies urgency HIGH/MEDIUM/LOW + confidence threshold prob >= 0.25 for HIGH. Stage 2 Qwen2-VL generates clinical description. Stage 3 RAG ChromaDB retrieves top-5 similar historical cases. Stage 4 BioMistral synthesises final JSON: urgency, confidence, reasoning, pathology. Adaptation layer maps urgency to P1-P4, specialist and SLA. Fallback: When no image, symptom-only scoring derives urgency from B4 chatbot interaction fields (itching, bleeding, growing, changing, pain, etc.). Also API endpoints. Model test report: EfficientNet-B4 version 1.0.0 baseline, 3-class urgency, threshold 0.25 for HIGH, threshold tuning history. Dataset: urgency levels HIGH/MEDIUM/LOW, diagnosis catalog, etc. Training cycles: label mapping P1/P2 -> HIGH, P3 -> MEDIUM, P4 -> LOW. Retraining protocol. Test env: POST /analyze full 4-step pipeline; POST /diagnose B4-integrated pipeline; pipeline stage tests. Acceptance criteria HIGH sensitivity etc.

MR-01 intent: determine urgency and operational priority of triage. Context: triage evaluation starts from available case info. When no image, project provides symptom-based path. Stakeholders: patient. Scope IN: determination of case urgency and related operational triage priority, even when image absent. OUT: specialist destination; medical validation/correction; subsequent adaptation.

So Decisions under MR-01 likely:

- Adoption of a four-stage AI pipeline? But is that MR-01? The pipeline produces final triage urgency. The decision to use image-based AI pipeline with stages may be under MR-01? R5 example says DEC-12 Adozione di una pipeline AI image-based a quattro stadi, under MR-01. But that's in method guide DermaTriage example. However prompt says guides' DermaTriage examples are method illustrations, never project evidence. But we can use them to understand method? It says treat examples only as method illustrations, never as project evidence. But they are from method guide; they mention DEC-12. But we should not use as evidence for reconstruction? We can use method to classify, but not as project evidence. However original docs clearly document four-stage pipeline. So candidate likely.
- Decision to use EfficientNet-B4 as urgency classifier? Or is that realization? R5 says DEC-12 governs pipeline; FR-16 preserves EfficientNet-B4. But Decision might be adoption of image-based AI pipeline. Then specific models might be FRs under Decision, not separate Decisions. But MR-01 scope includes urgency determination. The commitment to use a CNN classifier for urgency (Stage 1) could be a Decision: "Use image-based classifier to determine urgency" or "Adopt AI image-based pipeline". The specific model EfficientNet-B4 might be technology choice at Decision level? R5 says technical choice routing: if project governs material choice, name must remain. But Decision could be "Adoption of a four-stage AI pipeline" with concrete components? Actually R5 example: DEC-12 Adozione di una pipeline AI image-based a quattro stadi; FR-16 EfficientNet-B4 MUST produce HIGH/MEDIUM/LOW. So model names are in FR, not Decision. The Decision is pipeline architecture. So candidate: EXT-DEC-01 Adozione di pipeline AI image-based a quattro stadi. But MR-01 only? The pipeline includes Stage 2 clinical description, Stage 3 RAG, Stage 4 synthesis. But MR-01 is urgency and priority. Stage 2/3/4 may be for final urgency? The final JSON includes urgency. So pipeline is to determine urgency? Actually Stage 4 synthesises final JSON decision. So yes.
- Decision on urgency taxonomy: HIGH/MEDIUM/LOW? The system uses 3-class urgency. Is that a Decision? It restricts MR-01: determine urgency. The specific scale (HIGH/MEDIUM/LOW) is a project commitment. Could be a Decision: "Adoption of three-level urgency classification". Or is it part of pipeline? The original docs show Stage 1 outputs HIGH/MEDIUM/LOW; adaptation layer maps to P1-P4. MR-01 includes urgency and operational priority. The P-scale mapping is priority. So Decision could be "Mapping from urgency to P-scale/SLA" or "Adoption of P1-P4 operational priority scale". But SLA and specialist destination might be MR-02? Scope OUT says specialist destination; but priority includes SLA? MR-01 says "urgenza del caso e relativa priorita' operativa di triage". The adaptation layer maps urgency to P1-P4, specialist and SLA. Specialist is MR-02. SLA maybe operational priority? MR-01 includes priority. So P-scale mapping is under MR-01. But the mapping table includes specialist? Actually OR2 page 1: Adaptation Layer: map\_urgency\_to\_p\_scale() assigns P1-P4, specialist and SLA. Table: HIGH + confidence > 0.85 -> P1 24 hours; HIGH -> P2 48 hours; MEDIUM -> P3 72 hours; LOW -> P4 7 giorni. The specialist column not in table? It says "Urgency + Condition P-Scale SLA". No specialist column. So P-scale/SLA is under MR-01 priority. Decision: mapping rule from urgency (and confidence) to P-scale/SLA. This is a conditional selection rule. R5 example FR-02: HIGH + confidence >0.85 -> P1, HIGH -> P2, MEDIUM -> P3, LOW -> P4. It says this is a true governed conditional rule, belongs to FR semantics. But is it a Decision? The Decision might be "Adoption of P-scale and SLA mapping" or maybe the mapping is an FR under a Decision about operational priority. The Decision could be "Use P1-P4 operational priority scale with SLA". But the exact mapping might be FR. However Decision is a commitment that restricts MR. The choice of P-scale and SLA is material. Could be Decision: "Adozione di una scala di priorità operativa P1-P4 con SLA associati". Then FRs encode mapping. Or the mapping itself could be the Decision? R5 says Decision fixes position, policy, convention, strategy. A mapping rule is a policy/convention. But R5 also says FR is operational obligation; conditional selection rule belongs to FR. Hmm.
- Decision on fallback symptom-only path when no image. MR-01 context explicitly says "Quando non e' presente un'immagine della lesione, il progetto prevede un percorso basato sui sintomi disponibili." Scope IN includes even when image absent. Original docs: Fallback: When no image is available, symptom-only scoring derives urgency from B4 chatbot interaction fields (itching, bleeding, growing, changing, pain, etc.). This is a commitment to support no-image path. Likely a Decision: "Adoption of symptom-only triage fallback when image absent". Or maybe it's part of pipeline? It's a separate path. Decision candidate.
- Decision on threshold for HIGH? The model test report says inference threshold 0.25 for HIGH, tuned from 0.60 -> 0.70 -> 0.40 -> 0.25. This is a configuration/parameter. Is it a Decision? It materially affects urgency determination. But is it governed project commitment? The source documents it as final value selected to maximise HIGH sensitivity. It could be a Decision: "Set HIGH classification threshold to 0.25 to prioritise sensitivity". But R5/R6 says parameter governance: source numeric/config value -> semantic owner -> lifecycle/purpose -> requirement/property classification -> parameter boundary -> current concrete binding. The threshold might be a configuration/parameter under an FR, not a Decision. But it could be a Decision if project governs the trade-off. The Decision could be "Adoption of a safety-biased threshold strategy for HIGH urgency". The specific 0.25 might be current binding. Need classify.
- Decision on using RAG top-5 similar historical cases? Is that under MR-01? It supports final decision. Could be part of pipeline Decision. Maybe not separate.
- Decision on final synthesis by BioMistral? Part of pipeline.
- Decision on clinical description by Qwen? Part of pipeline.
- Decision on image-based path vs symptom-only? The project has both. The Decision could be "Support both image-based and symptom-only triage paths". But MR-01 context already says no-image path. Is that MR wording or Decision? The MR input says "Quando non e' presente un'immagine della lesione, il progetto prevede un percorso basato sui sintomi disponibili." That is in MR Context. But Context of MR can include project framing. However the Decision to implement fallback is a commitment. Could be a Decision under MR-01.
- Decision on output format JSON? That's likely lower-level (FR/interface).
- Decision on model version 1.0.0? Realization/configuration.
- Decision on using confidence >0.85 for P1? That's part of mapping rule. Could be Decision or FR.
- Decision on urgency distribution? No.
- Decision on retraining loop? That's MR-04 adaptation, not MR-01.
- Decision on doctor validation? MR-03.
- Decision on specialist destination? MR-02.

Need determine set. We need produce external report with candidates. We can include candidates that are accepted, rework, reject, lower-level. Need be thorough. The prompt asks independent decision discovery. We can propose maybe 3-5 accepted Decisions. Need not match internal. We must justify.

Let's read method guides for Decision definition. R5: Decision is significant project commitment that restricts exactly one MR fixing position, boundary, policy, convention, strategy, technology/architecture choice or other materially relevant commitment. Consequences describes system. Technical choice routing: if project governs concrete choice, name must stay at semantic owner. DermaTriage DEC-12 example: "Adozione di una pipeline AI image-based a quattro stadi" under MR-01. FR-16..19 preserve concrete names. So pipeline adoption is a Decision. Also FR-02 mapping P-scale is an FR under some Decision. What Decision? Maybe "Adozione di una scala di priorità operativa P1-P4" or the mapping is FR under DEC about triage evaluation? Actually R5 example: MR-01 -> DEC-12 -> FR-16..19. It doesn't mention FR-02. R5 section 11.4 says DermaTriage FR-02 mapping P-scale. It says "HIGH + confidence > 0.85 -> P1 ..." This is a true conditional rule, belongs to FR semantics. So there must be a Decision parent for FR-02. Which Decision? Possibly DEC-01? Not shown. Could be a Decision about "Adozione della scala P1-P4 e SLA". We can infer.

R6 candidate has section 26 DermaTriage explicit documentation gaps: diagnostic authority boundary; no-image required/optional symptom inputs and missing-value semantics; P-scale complete input semantics and no-image binding; SLA trigger/outcome/owner/normative binding; predicted pathology obligation/authority; specialist selection vocabulary/rule/input/fallback/booking; review content, lifecycle e disagreement binding; adaptation counting e threshold authority; prompt evidence window ordering/membership/underfill/dedup/reuse/overlap; supervision input invalid/missing/conflicting semantics; deployment authority/automaticity; acceptance e rollback binding; evaluation consistency tra sensitivity/recall/correct-count.

These gaps indicate many things are NOT SPECIFIED. So we should not invent Decisions for missing semantics. We can record gaps. The Decision candidates should be supported.

Original docs show:

- Four-stage AI pipeline (image-based)
- Stage 1 EfficientNet-B4 fine-tuned, threshold 0.25 for HIGH
- Stage 2 Qwen2-VL-7B-Instruct
- Stage 3 RAG ChromaDB top-5
- Stage 4 BioMistral-7B final JSON
- Adaptation layer maps urgency to P1-P4, specialist, SLA
- Fallback symptom-only scoring when no image
- API endpoints
- Self-learning loops (MR-04)
- Storage architecture
- Technology stack
- Live system status
- Model test report: model, threshold, safety metrics
- Dataset metadata
- Training cycles
- Test environment

MR-01 is urgency and operational priority. So relevant commitments:

1. Use a four-stage AI pipeline to determine triage urgency? This includes image-based path.
2. Use a three-level urgency classification (HIGH/MEDIUM/LOW).
3. Use a P1-P4 operational priority scale with SLA mapping.
4. Use a symptom-only fallback path when image absent.
5. Use a threshold-based HIGH urgency classification with threshold 0.25? Maybe lower-level/parameter.
6. Use confidence >0.85 for P1? Part of mapping.
7. Use RAG top-5 historical cases to inform final urgency? Part of pipeline.
8. Use BioMistral final synthesis? Part of pipeline.
9. Use EfficientNet-B4 specifically? Part of pipeline realization or FR.

Maybe Decision: "Adoption of image-based AI pipeline for triage evaluation" (covers stages 1-4). Then specific models are FRs. But MR-01 scope includes no-image fallback. The pipeline is only image-based. The fallback is separate. So another Decision: "Adoption of symptom-only triage path when image not available". Could be combined? "Adoption of dual-path triage evaluation: image-based AI pipeline and symptom-only fallback". But R5 example DEC-12 is specifically "Adozione di una pipeline AI image-based a quattro stadi". The fallback might be a separate Decision or FR under same? The MR context mentions it. Could be Decision: "Supporto del percorso sintomi quando l'immagine non è disponibile". This restricts MR-01.

Decision on urgency taxonomy: The MR intent says determine urgency. The specific classification HIGH/MEDIUM/LOW is a commitment. Could be Decision: "Adozione di una scala di urgenza a tre livelli HIGH/MEDIUM/LOW". Or is that part of pipeline? Stage 1 outputs it. It's a convention. It restricts MR. Yes.

Decision on P-scale: The MR scope includes operational priority. The P1-P4 scale and SLA mapping is a commitment. Could be Decision: "Adozione di priorità operativa P1-P4 con SLA". But the mapping rule might be FR. The Decision could be "Adozione della scala P1-P4 e associazione SLA". The exact mapping HIGH+conf>0.85->P1 etc. is the conditional selection rule. Could be FR. But is the Decision the adoption of the scale? Yes.

Maybe also Decision on confidence-based escalation: HIGH + confidence >0.85 -> P1, else HIGH -> P2. That's a policy. Could be part of P-scale mapping.

Decision on using AI models at all? The pipeline Decision covers.

Decision on threshold 0.25 for HIGH? This is a parameter. Could be Decision: "Adozione di una soglia di classificazione HIGH pari a 0.25 per massimizzare sensibilità". But R6 parameter governance says numeric value requires semantic owner, lifecycle, purpose. It might be a configuration binding, not a Decision. However the choice to prioritise HIGH sensitivity over accuracy is a safety policy. The threshold tuning history shows trade-off. The Decision could be "Prioritise HIGH sensitivity over overall accuracy by setting threshold 0.25". That is a material commitment. But is it governed by MR-01? Yes, urgency determination. Could be Decision. But R5/R6 warns not to promote every numeric value to Decision. It might be a parameter under an FR for Stage 1. But the policy of threshold selection might be a Decision. Let's classify as REWORK or LOWER\_LEVEL? We can include as candidate and lower-level.

Decision on final synthesis using multiple sources? Part of pipeline.

Decision on RAG retrieval top-5? Part of pipeline.

Decision on output JSON fields? Lower-level.

Decision on fallback symptom scoring from B4 chatbot fields? The specific fields (itching, bleeding, growing, changing, pain, etc.) are listed. Is that a Decision? The existence of fallback is a Decision. The exact scoring algorithm is not specified. R6 gap: no-image required/optional symptom inputs and missing-value semantics. So we should not invent scoring rule. The Decision is "Support symptom-only triage when image absent". The specific inputs/scoring are gap/FR.

Decision on adaptation layer mapping to specialist? Specialist is MR-02 OUT. So not MR-01. But SLA is MR-01? The adaptation layer assigns specialist and SLA. We must separate: P-scale and SLA are priority; specialist is MR-02. So Decision on P-scale/SLA is MR-01. The mapping to specialist should be excluded.

Decision on live system status? Not a Decision.

Decision on technology stack? Specific models are realization, not Decisions unless project governs them as commitments. R5 says if project governs material choice, name must stay at semantic owner. But Decision could be pipeline adoption; FRs preserve names. So we don't need separate Decisions for each model. However the choice of EfficientNet-B4 as classifier might be a technical choice under pipeline Decision. It could be a Decision if it restricts MR-01: "Use EfficientNet-B4 for urgency classification". But R5 example suggests it's an FR under DEC-12. So we can reject/lower-level specific model choices as FR/realization.

Need produce report with sections. We can use template. Need include source-coverage gate. We inspected all files. We can state checked and relevant/not relevant etc. We have all in prompt. Need maybe mention page/section.

Need restate MR-01 boundary.

Need candidate inventory. Let's decide final candidates. I think we can accept 4 Decisions:

EXT-DEC-01: Adozione di una pipeline AI image-based a quattro stadi per la valutazione di triage.
EXT-DEC-02: Adozione di una scala di urgenza a tre livelli HIGH/MEDIUM/LOW.
EXT-DEC-03: Adozione di una scala di priorità operativa P1-P4 con SLA associati.
EXT-DEC-04: Supporto di un percorso sintomi-only in assenza di immagine.

Maybe also EXT-DEC-05: Adozione di una soglia di classificazione HIGH pari a 0.25 per privilegiare la sensibilità. But is that a Decision? Let's analyze. The model test report says "Inference threshold 0.25 for HIGH (tuned from 0.60 > 0.70 > 0.40 > 0.25)" and "Final value of 0.25 selected to maximise HIGH sensitivity to meet the >90% clinical target." This is a project commitment to a safety-biased threshold. It restricts MR-01: how urgency is determined. It is a policy/strategy. It could be a Decision. But R6 says parameter governance: numeric/config value -> semantic owner -> lifecycle/purpose -> requirement/property classification -> parameter boundary -> current concrete binding. The threshold is a parameter. The Decision might be "Adozione di una strategia di soglia per massimizzare sensibilità HIGH". The specific 0.25 is current binding. Is this a Decision or FR? It could be a Decision because it's a policy choice. But R5 example FR-02 mapping is FR. Threshold might be FR. However the choice to set threshold to 0.25 is a configuration decision. The prompt says do not assume every technology or configuration fact is a Decision. So likely LOWER\_LEVEL or HOLD. We can include as candidate and classify as LOWER\_LEVEL (parameter binding) or REWORK. But maybe the Decision is "Priorità alla sensibilità HIGH" which is a safety policy. That might be a Decision. But is it under MR-01? Yes. Let's include as EXT-DEC-05 candidate and disposition LOWER\_LEVEL? Or ACCEPT? Need decide.

R5/R6: Decision is commitment restricting MR. The threshold choice restricts how urgency is computed. It is material. But the guide also says "inventare threshold... per rendere un FR piu' testabile" is bad. But here threshold is documented. The threshold is a parameter. R6 Step 12: "source numeric/config value -> semantic owner -> lifecycle / purpose -> requirement/property classification -> parameter boundary -> current concrete binding". It doesn't say numeric value cannot be Decision. It says classify according to semantic owner. The semantic owner might be an FR for Stage 1 classification. The threshold is a parameter of that FR. So I lean LOWER\_LEVEL. But the policy of prioritising sensitivity could be a Decision. The document says "Final value of 0.25 selected to maximise HIGH sensitivity to meet the >90% clinical target." That is a project commitment to meet clinical target. The target >90% sensitivity might be a requirement/quality property. The Decision could be "Adozione di una soglia di sensibilità HIGH >90%". But that's a requirement. Hmm.

Also decision on using confidence >0.85 for P1: part of P-scale mapping. That mapping is a conditional selection rule. R5 says it belongs to FR semantics. So the P-scale Decision is the scale adoption, and the mapping is FR. So we don't need separate Decision for confidence.

Decision on using RAG top-5: part of pipeline. Not separate.

Decision on model selection: part of pipeline or FR.

Decision on fallback symptom-only: yes.

Decision on urgency taxonomy: is that a Decision or part of pipeline? It could be part of pipeline Decision. But MR-01 intent says determine urgency. The specific scale is a convention. It restricts MR. I think it's a Decision. But maybe it's an FR under pipeline Decision. The pipeline outputs HIGH/MEDIUM/LOW. The scale is a project convention. Could be a Decision. Let's accept as Decision. But we must avoid redundancy with pipeline. The pipeline Decision could be "Adozione di una pipeline AI image-based a quattro stadi" and the urgency scale is part of Stage 1 output. Is it separate? It might be too granular. However the MR scope includes urgency determination. The scale is a commitment. I'd include it as separate because it's a policy/convention. But we can note overlap and maybe merge? R5 says Decision restricts exactly one MR. Multiple Decisions can restrict same MR if independent commitments. The pipeline adoption and urgency scale are independent: you could change scale while keeping pipeline. So separate.

Decision on P-scale/SLA: independent.

Decision on fallback: independent.

Decision on threshold: independent? Could change threshold while keeping pipeline. It's a parameter, but it's a commitment. Maybe accept as Decision? Let's think. The Decision definition: "commitment ... fissando posizione, boundary, policy, convention, strategy, technology/architecture choice". A threshold value is a configuration, not a strategy. The strategy might be "massimizzare HIGH sensitivity". The threshold is the realization. So I'd classify as LOWER\_LEVEL (parameter/binding). But we can mention in not promoted.

What about decision on using confidence to modulate P-scale? That's part of P-scale mapping. Could be FR.

What about decision on final output including predicted pathology? Predicted pathology is in Stage 4 JSON. But MR-01 scope is urgency and priority. Predicted pathology might be outside MR-01? The MR-01 scope OUT does not mention pathology. But the pipeline outputs pathology. Is pathology part of MR-01? The Intent: "determinare l'urgenza del caso e la relativa priorita' operativa". Pathology not mentioned. So predicted pathology might be outside MR-01, or a downstream obligation. R6 gap mentions "predicted pathology obligation/authority". So we should not include as MR-01 Decision. Could be evidence not promoted.

What about decision on using image vs symptoms? The pipeline is image-based. The fallback is symptom-only. The Decision to support both paths? The MR context says no-image path. The Decision could be "Supporto di entrambi i percorsi: image-based e symptom-only". But the pipeline Decision is image-based. The fallback Decision is symptom-only. They are separate. Could be one Decision "Adozione di percorsi di triage image-based e symptom-only". But R5 example separates DEC-12 pipeline image-based. I'd keep separate.

What about decision on using RAG? Part of pipeline.

What about decision on using a 4-stage pipeline specifically? Yes.

What about decision on using confidence from Stage 1? Part of pipeline.

What about decision on mapping P1/P2 -> HIGH etc. for retraining? That's MR-04 adaptation. Not MR-01.

What about decision on acceptance criteria for model (HIGH sensitivity >90%, false LOW <5%)? These are quality gates. Are they Decisions under MR-01? They govern the classifier's performance. They are requirements/quality properties. Could be a Decision: "Adozione di criteri di sicurezza per il classificatore HIGH sensitivity >90% e false LOW <5%". But these are targets. The MR-01 scope includes urgency determination. The safety criteria are material commitments. However they might be requirements/verification criteria, not Decisions. R5/R6 says Decision is commitment. The choice to set safety targets could be a Decision. But the original docs present them as targets, some FAIL. They are not fully met. But they are documented. Could be a Decision: "Adozione di target di sicurezza per il triage". But the MR-01 intent doesn't mention safety. However it's about urgency. I'd classify as LOWER\_LEVEL (quality/verification criteria) or HOLD. Not a core Decision.

What about decision on using P1-P4 scale? Yes.

What about decision on SLA times? The table gives 24h, 48h, 72h, 7 days. Is that a Decision? It's part of P-scale mapping. Could be a Decision: "Adozione di SLA per priorità P1-P4". The exact times are parameters. The Decision is adoption of SLA. The mapping is FR. So P-scale/SLA Decision covers.

What about decision on specialist destination? MR-02 OUT.

What about decision on doctor validation? MR-03 OUT.

What about decision on adaptation? MR-04 OUT.

Now we need write report. We can include candidates:

EXT-DEC-01: Adozione di una pipeline AI image-based a quattro stadi per la valutazione di triage.
EXT-DEC-02: Adozione di una scala di urgenza a tre livelli HIGH/MEDIUM/LOW.
EXT-DEC-03: Adozione di una scala di priorità operativa P1-P4 con SLA associati.
EXT-DEC-04: Supporto di un percorso sintomi-only in assenza di immagine.
EXT-DEC-05: Adozione di una soglia di classificazione HIGH pari a 0.25 per privilegiare la sensibilità. (maybe LOWER\_LEVEL)
EXT-DEC-06: Adozione di una strategia di classificazione basata su modelli AI specifici (EfficientNet-B4, Qwen2-VL, ChromaDB, BioMistral). (maybe part of pipeline, reject/lower)
EXT-DEC-07: Adozione di RAG top-5 casi storici per supportare la decisione finale. (part of pipeline)
EXT-DEC-08: Adozione di un output JSON finale con urgenza, confidence, reasoning, pathology. (lower-level)
EXT-DEC-09: Adozione di target di sicurezza HIGH sensitivity >90%, false LOW <5%. (lower-level/quality)

But maybe too many. The prompt says identify every project commitment that may qualify. We can include candidates and then in family regression merge/reject. Final closure table can show accepted vs lower-level. That's good.

Need follow structure: Section 0 Analyst declaration. Section 1 Source-coverage gate. Section 2 Complete MR-01 boundary. Section 3 Candidate inventory. Section 4 Candidate reviews. Section 5 Inspected evidence not promoted. Section 6 Decision-family regression. Section 7 Closure result. Section 8 Methodology observations.

We need produce in Italian? The prompt is in English, but user Italian. The prompt says return report following structure. We can write in English or Italian. The original prompt is English. The MR is Italian. I can write in English for method, with Italian titles. That's fine. Maybe answer in Italian? The user said "esegui il promt". I can produce report in English as prompt. But maybe better in Italian? The prompt is in English, so English is acceptable. However to be safe, I can write in English with Italian titles. The report is long. Desired oververbosity 5. We need be thorough but not insane. We have token budget.

Need ensure we don't claim we inspected files we didn't? We have all files in prompt. We can say inspected via provided extraction. We can't actually open PDFs, but content is provided. We can state "inspected (extracted text)". That's fine.

Need include verbatim source quotes. We can quote from provided content. Need be accurate.

Let's draft.

Section 0: Analyst declaration. Analyst: external AI analyst. Date: 2026-09-15? Today's date? System current date 2026-09-15. Prior exposure: NO. Package identifier: DDTA\_MR01\_EXTERNAL\_BLIND\_REVIEW\_R1. Package ZIP SHA-256: not provided? The user said flattened. We don't have ZIP hash. We can put "not available in flattened extraction; package metadata records operational subset ZIP SHA-256 e9e54d...". But template asks package ZIP SHA-256. We can state not computed; metadata records e9e54... for operational subset. But we are not given actual zip. We can put "N/A (flattened extraction; per metadata: e9e54...)". Good.

Section 1 Source-coverage gate: table with six PDFs, inspected? yes, relevant to MR-01? yes for some, state checked and relevant/ambiguous. Notes.

OR2\_Architecture\_Document.pdf: checked and relevant: pipeline, stages, adaptation layer, fallback.
OR2\_Model\_Test\_Report.pdf: checked and relevant: threshold, metrics, classes.
OR3\_Dataset\_Metadata\_Catalog.pdf: checked, relevant for urgency taxonomy and diagnosis catalog, but mostly dataset facts.
OR4\_Training\_Environment\_Config.pdf: checked, mostly environment/realization, not MR-01 Decision except model paths.
OR4\_Training\_Cycles\_Report.pdf: checked, relevant for training/retraining (MR-04), label mapping, but not MR-01 Decisions.
OR5\_Test\_Environment\_Setup.pdf: checked, relevant for API/pipeline tests, no-image? not much.

Also MR input checked.

Section 2: Restate MR-01. Intent, Context, Stakeholders, Scope IN, OUT, Assumptions, dependsOn. Macro-boundary interpretation: MR-01 owns urgency and operational priority, including no-image path. Must not absorb specialist destination (MR-02), medical validation (MR-03), adaptation (MR-04). Note predicted pathology is not in MR-01 scope; if present, belongs elsewhere or gap.

Section 3 Candidate inventory table: EXT-DEC-01..09.

Section 4 Candidate reviews. For each, do sub-sections. This will be long. We can be concise but complete.

Let's define candidates:

EXT-DEC-01 — Adozione di una pipeline AI image-based a quattro stadi per la valutazione di triage.
Evidence: OR2 Architecture p1: four-stage AI pipeline table, pipeline flow. Verbatim: "DermaTriage processes patient-submitted skin lesion images through a sequential four-stage AI pipeline..." and table. Establishes: image-based path uses four stages: EfficientNet-B4 urgency, Qwen clinical description, RAG top-5, BioMistral final JSON. Not establish: exact binding of models as immutable? Ambiguity: stage 4 outputs final JSON with urgency, pathology; MR-01 scope? We interpret urgency part. Decision: Context: need to determine urgency from image. Decision: adopt four-stage image-based pipeline. Consequences: stages, dependencies, model names. Classification: Decision vs MR: restricts MR-01; not FR because it's architecture strategy. R5 DEC-12 example supports. Disposition: ACCEPT AS DECISION CANDIDATE. MR stability: can change components while MR same; pipeline adoption may be stable. Downstream: FRs for each stage.

EXT-DEC-02 — Adozione di una scala di urgenza a tre livelli HIGH/MEDIUM/LOW.
Evidence: OR2 Architecture stage 1 output HIGH/MEDIUM/LOW; OR2 Model Test Report task 3-class; OR3 urgency\_level column. Verbatim: "Task 3-class skin lesion urgency: HIGH / MEDIUM / LOW". Establishes: project uses three-level urgency. Not establish: exact semantic definitions of each level? Ambiguity: MEDIUM underrepresented. Decision: adopt three-level urgency taxonomy. Classification: Decision vs MR: convention restricting urgency determination. Not FR. Disposition: ACCEPT. MR stability: scale can change while MR same? Maybe if changed, MR still urgency. But it's a convention. Accept.

EXT-DEC-03 — Adozione di una scala di priorità operativa P1-P4 con SLA associati.
Evidence: OR2 Architecture adaptation layer mapping table. Verbatim: "Adaptation Layer: map\_urgency\_to\_p\_scale() assigns P1-P4, specialist and SLA" and table. Establishes: P1-P4 with SLA; mapping from urgency and confidence. Not establish: full input semantics for no-image binding; SLA owner/trigger. Ambiguity: specialist assignment is MR-02; we exclude. Decision: adopt P1-P4 operational priority scale with SLA. The exact mapping HIGH+conf>0.85->P1 etc. may be FR. Classification: Decision vs FR: adoption of scale is Decision; mapping is FR. Disposition: ACCEPT. MR stability: yes. Downstream: FR for mapping.

EXT-DEC-04 — Supporto di un percorso sintomi-only in assenza di immagine.
Evidence: MR input Context says project provides symptom path; OR2 Architecture fallback: "When no image is available, symptom-only scoring derives urgency from B4 chatbot interaction fields (itching, bleeding, growing, changing, pain, etc.)." Establishes: fallback exists, uses symptom fields. Not establish: required/optional inputs, missing-value semantics, scoring algorithm. Ambiguity: R6 gap. Decision: support symptom-only triage when image absent. Classification: Decision vs MR: Context mentions it, but the commitment to implement is Decision. Not FR because it's a path/boundary. Disposition: ACCEPT. MR stability: yes. Downstream: FR for symptom scoring, input semantics gap.

EXT-DEC-05 — Adozione di una soglia di classificazione HIGH pari a 0.25 per privilegiare la sensibilità.
Evidence: OR2 Model Test Report: "Inference threshold 0.25 for HIGH (tuned from 0.60 > 0.70 > 0.40 > 0.25)" and "Final value of 0.25 selected to maximise HIGH sensitivity to meet the >90% clinical target." Establishes: threshold value and rationale. Not establish: threshold authority/lifecycle? Ambiguity: parameter vs Decision. Decision: Context: safety target. Decision: set threshold 0.25. Consequences: increases HIGH sensitivity, lowers accuracy. Classification: LOWER\_LEVEL / configuration parameter. R6 parameter governance. Disposition: LOWER\_LEVEL (not Decision). But we can include as candidate and reject. Or maybe REWORK to a Decision about sensitivity policy. I'll put LOWER\_LEVEL.

EXT-DEC-06 — Adozione di modelli AI specifici (EfficientNet-B4, Qwen2-VL-7B-Instruct, ChromaDB/all-MiniLM-L6-v2, BioMistral-7B).
Evidence: OR2 Architecture four-stage table, technology stack. Establishes: current models. Not establish: whether model choices are governed commitments or current realization. R5 technical choice routing: if project governs material choice, name stays at semantic owner; but Decision could be pipeline adoption, FRs preserve names. Ambiguity: could be Decision if model selection is material. Disposition: LOWER\_LEVEL / REJECT AS DECISION (components are realization/FR under pipeline Decision). We can put LOWER\_LEVEL.

EXT-DEC-07 — Adozione di RAG top-5 casi storici per supportare la decisione finale.
Evidence: OR2 Architecture stage 3: "ChromaDB retrieves top-5 similar cases by cosine similarity". Establishes: top-5 retrieval. Not establish: selection semantics beyond top-5? R6 gap. Classification: part of pipeline Decision; lower-level FR. Disposition: LOWER\_LEVEL.

EXT-DEC-08 — Adozione di output JSON finale con urgenza, confidence, reasoning, pathology.
Evidence: OR2 Architecture stage 4: JSON: urgency, confidence, reasoning, pathology. Establishes: output format. Not establish: pathology authority. Classification: interface/output detail, FR/realization. Disposition: LOWER\_LEVEL.

EXT-DEC-09 — Adozione di target di sicurezza HIGH sensitivity >90%, false LOW <5%, accuracy >85%.
Evidence: OR2 Model Test Report safety metrics. Establishes: targets. Not establish: governance authority. Classification: quality/verification criteria, not Decision under MR-01? Could be requirement. Disposition: LOWER\_LEVEL / HOLD.

Maybe also EXT-DEC-10 — Adozione di una strategia di classificazione basata su soglia per HIGH. But covered by EXT-DEC-05.

We can include these. In family regression, we can say accepted family: EXT-DEC-01, 02, 03, 04. Maybe EXT-DEC-05 could be reworked as Decision "Adozione di una policy di sensibilità HIGH >90% con soglia regolabile" but we keep as lower-level. We need be honest.

Section 5: Inspected evidence not promoted to Decision. Table with many facts: model versions, endpoints, storage, training config, retraining threshold, etc. Classification.

Section 6: Decision-family regression. Pairwise overlap: EXT-DEC-01 and 02/03/04 distinct. EXT-DEC-02 and 03 both scales but different (urgency vs priority). EXT-DEC-01 and 04 both paths but distinct. Too broad/technical: EXT-DEC-06/07/08 lower. Unowned commitments: predicted pathology? specialist? review? adaptation? We note they belong to other MRs or gaps. Semantic ownership: EXT-DEC-01 can have FRs for stages; EXT-DEC-03 for mapping. MR wording pressure: MR-01 Context already mentions no-image path; might be better as Decision not MR Context? But no need to rewrite. New candidates: none beyond those.

Section 7: Closure result table with final classification and disposition. Accepted: EXT-DEC-01, 02, 03, 04. Lower-level: EXT-DEC-05, 06, 07, 08, 09. Maybe EXT-DEC-05 HOLD? I'll put LOWER\_LEVEL. Closure gates: Source coverage sufficient PASS. Decision discovery complete for supplied source set PASS? Maybe PASS with gaps. Pairwise non-overlap PASS. MR wording requires review: YES? The MR Context includes no-image path; that's fine. Maybe NO. Remaining HOLD: no-image input semantics, P-scale input binding, SLA ownership, predicted pathology authority. These are gaps.

Section 8: Methodology observations. R5 rules clear: Decision definition, technical routing, parameter governance. Required interpretation: Decision vs FR for mapping, threshold. R6 refinements: pipeline membership/order vs dependency, selection semantics, parameter governance. Tensions: R5 example DEC-12 vs our need to separate scale Decisions; R6 candidate non-normative. Cases multiple classifications: EXT-DEC-02 could be part of pipeline or separate. Guide wording uncertainty: "Decision" vs "convention" for urgency scale.

Need ensure no R7 proposals.

Now write final answer. Need be self-contained. We'll use markdown. It will be long. Desired oververbosity 5, but prompt requires detailed report. We'll produce comprehensive but not excessive. We can be concise per candidate.

Let's start.

We need mention we are using extracted text from files. No internal reference. Analyst declaration: Prior exposure NO. Package ZIP SHA-256: not computed; metadata says operational subset e9e54... But we can put N/A.

Let's write.

Check verbatim quotes:

- OR2 Architecture: "DermaTriage processes patient-submitted skin lesion images through a sequential four-stage AI pipeline, each stage enriching the clinical context before the final triage decision."
- Table: Stage 1 EfficientNet-B4 ... HIGH / MEDIUM / LOW + confidence. Stage 4 BioMistral ... JSON: urgency, confidence, reasoning, pathology.
- Adaptation: "map\_urgency\_to\_p\_scale() assigns P1-P4, specialist and SLA"
- Table: "HIGH + confidence > 0.85 P1 24 hours; HIGHP2 48 hours; MEDIUMP3 72 hours; LOWP4 7 giorni"
- Fallback: "When no image is available, symptom-only scoring derives urgency from B4 chatbot interaction fields (itching, bleeding, growing, changing, pain, etc.)."
- Model test: "Task 3-class skin lesion urgency: HIGH / MEDIUM / LOW"
- "Inference threshold 0.25 for HIGH (tuned from 0.60 > 0.70 > 0.40 > 0.25)"
- "Final value of 0.25 selected to maximise HIGH sensitivity to meet the >90% clinical target."
- R6 gaps: no-image required/optional symptom inputs and missing-value semantics; P-scale complete input semantics and no-image binding; SLA trigger/outcome/owner/normative binding; predicted pathology obligation/authority.

We can cite R5 rules: Decision definition section 10; technical routing 10.5; parameter governance R6 20.1.

Now produce.

# DDTA MR-01 External Decision Reconstruction — Independent Result

## 0. Analyst declaration

- **Analyst / model:** external AI analyst (no internal DDTA access)
- **Date:** 2026-09-15
- **Prior exposure to internal DermaTriage MR-01 Decision results:** NO
- **If YES, disclose remembered content before continuing:** N/A
- **Package identifier:** `DDTA_MR01_EXTERNAL_BLIND_REVIEW_R1`
- **Package ZIP SHA-256:** not computed on flattened extraction. Package metadata records operational subset SHA-256 `e9e54d3ba7c06a5a4c215d015bc741e99a254f7337900ad60b783420039a6fed`; full pinned package SHA-256 `E9ED2C507BEFB95F54A52084687CD1E8798863AE81CF69D09568864D8CBF280E`.

I used only the supplied files. R5 is treated as current authority; R6 Candidate R2 is treated as non-normative clarification where explicitly helpful. R7 is not used.

---

## 1. Source-coverage gate

| **SourceInspected?Relevant to MR-01?StateNotes** |     |           |                                            |                                                                                |
| ------------------------------------------------ | --- | --------- | ------------------------------------------ | ------------------------------------------------------------------------------ |
| `OR2_Architecture_Document.pdf`                  | Yes | Yes       | Checked and relevant                       | Four-stage image pipeline; adaptation layer; fallback symptom path; endpoints. |
| `OR2_Model_Test_Report.pdf`                      | Yes | Yes       | Checked and relevant                       | 3-class urgency; EfficientNet-B4; threshold 0.25; safety metrics.              |
| `OR3_Dataset_Metadata_Catalog.pdf`               | Yes | Partially | Checked and relevant for context           | Urgency labels HIGH/MEDIUM/LOW; diagnosis catalog; data quality.               |
| `OR4_Training_Environment_Config.pdf`            | Yes | Weakly    | Checked, mostly realization                | Environment, dependencies, storage, model paths. Not MR-01 Decision authority. |
| `OR4_Training_Cycles_Report.pdf`                 | Yes | Partially | Checked, relevant to MR-04 more than MR-01 | Training cycles, label mapping, retraining protocol.                           |
| `OR5_Test_Environment_Setup.pdf`                 | Yes | Partially | Checked and relevant for verification      | API endpoints, pipeline stage tests, acceptance criteria.                      |
| `DDTA_DERMATRIAGE_MR_ONLY_INPUT_R1.md`           | Yes | Yes       | Checked; governs experiment boundary       | Supplies MR-01 and macro-boundary context.                                     |

No supplied source was left unchecked. “Not found” in this report means “not found in the supplied extracted text”, not “does not exist”.

---

## 2. Complete MR-01 boundary

### Intent

Determinare, a partire dalle informazioni disponibili sul caso dermatologico, l’urgenza del caso e la relativa priorita’ operativa di triage.

### Context

La valutazione di triage parte dalle informazioni disponibili sul caso. Quando non e’ presente un’immagine della lesione, il progetto prevede un percorso basato sui sintomi disponibili.

### Stakeholders

Paziente.

### Scope IN

- determinazione dell’urgenza del caso e della relativa priorita’ operativa di triage;
- anche quando l’immagine non e’ presente.

### Scope OUT

- indicazione della destinazione specialistica;
- validazione o correzione medica dell’esito;
- adattamento successivo del comportamento del sistema sulla base della revisione clinica.

### Assumptions / Constraints

\--

### dependsOn

None

### Macro-boundary interpretation

MR-01 owns the production of urgency and operational triage priority. It must not absorb:

- specialist destination selection (MR-02);
- medical validation/correction (MR-03);
- controlled adaptation from clinical review (MR-04).

Predicted pathology appears in the pipeline output, but MR-01 does not explicitly own pathology determination. It should therefore not be promoted to an MR-01 Decision in this reconstruction; it remains a downstream/gap question unless separately governed.

---

## 3. Candidate inventory before detailed review

| **External IDWorking titleInitial classification** |                                                                                              |                                          |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------- |
| EXT-DEC-01                                         | Adozione di una pipeline AI image-based a quattro stadi per la valutazione di triage         | Candidate Decision                       |
| EXT-DEC-02                                         | Adozione di una scala di urgenza a tre livelli HIGH/MEDIUM/LOW                               | Candidate Decision                       |
| EXT-DEC-03                                         | Adozione di una scala di priorità operativa P1-P4 con SLA associati                          | Candidate Decision                       |
| EXT-DEC-04                                         | Supporto di un percorso sintomi-only in assenza di immagine                                  | Candidate Decision                       |
| EXT-DEC-05                                         | Adozione di una soglia HIGH pari a 0.25 per privilegiare la sensibilità                      | Candidate Decision / parameter           |
| EXT-DEC-06                                         | Adozione di modelli AI specifici: EfficientNet-B4, Qwen2-VL, ChromaDB/all-MiniLM, BioMistral | Candidate technical choice               |
| EXT-DEC-07                                         | Adozione di RAG top-5 casi storici per supportare la decisione finale                        | Candidate technical choice               |
| EXT-DEC-08                                         | Adozione di output JSON finale con urgenza, confidence, reasoning, pathology                 | Candidate interface detail               |
| EXT-DEC-09                                         | Adozione di target di sicurezza HIGH sensitivity >90%, false LOW <5%, accuracy >85%          | Candidate quality/verification criterion |

---

## 4. Candidate reviews

### EXT-DEC-01 — Adozione di una pipeline AI image-based a quattro stadi per la valutazione di triage

#### A. Original documentation evidence

**Source:** `OR2_Architecture_Document.pdf`
**Page/section:** Page 1, “Four-Stage AI Pipeline” and “Pipeline Flow”

**VERBATIM SOURCE**

> “DermaTriage processes patient-submitted skin lesion images through a sequential four-stage AI pipeline, each stage enriching the clinical context before the final triage decision.”

> Stage 1: EfficientNet-B4 (fine-tuned) — Skin lesion image — HIGH / MEDIUM / LOW + confidence
> Stage 2: Qwen2-VL-7B-Instruct — Skin lesion image — Clinical text description (5-bullet format)
> Stage 3: RAG — ChromaDB — Clinical text — Top-5 similar historical cases
> Stage 4: BioMistral-7B — Stage 1+2+3 + symptoms — JSON: urgency, confidence, reasoning, pathology

**PARAPHRASE**

The project documents an image-based triage pipeline that processes a skin lesion image through four sequential stages and produces a final triage decision.

**INTERPRETATION**

This is a material architecture/strategy commitment. It restricts how MR-01 urgency is produced when an image is available. It is not merely an implementation detail because it establishes the pipeline composition and order.

#### B. Minimum source-supported meaning

**Established:**

- image-based triage uses a sequential four-stage AI pipeline;
- the stages are concrete and ordered;
- the final output includes urgency and confidence.

**Not established:**

- whether every named model is an immutable project commitment or current realization;
- how pipeline membership/order should be converted into downstream dependency semantics;
- whether Stage 4 pathology output belongs to MR-01 or elsewhere.

**Ambiguity / conflict:**
R5/R6 distinguish pipeline membership/order from `dependOn` or prerequisite dependency. The source documents sequence, not necessarily dependency semantics.

#### C. Candidate Decision

**Context**
When an image is available, the project needs a governed strategy to determine triage urgency from the image and related case information.

**Decision**
Adopt a sequential four-stage AI image-based pipeline for triage evaluation.

**Consequences**

- the project owns a multi-stage image-based triage path;
- stages are ordered: urgency classifier, clinical description, RAG retrieval, medical synthesis;
- concrete component names must be preserved at the correct semantic owner, likely FR level, not erased;
- pipeline order does not automatically become `dependOn`.

#### D. Classification gate

**Decision vs MR:** Restricts MR-01 by fixing an architecture/strategy for urgency evaluation.
**Decision vs FR / operational obligation:** It is broader than a single operational obligation; individual stage behaviors are FR-level.
**Decision vs realization / configuration / binding / evidence:** It is a project commitment, not mere evidence, because it fixes pipeline composition and order.
**R5/R6 rule(s) applied:** R5 Decision definition; R5 technical choice routing; R6 pipeline membership/order non-dependency.

#### E. MR stability / boundary effect

MR-01 can remain “valutazione di triage” while pipeline components change. Accepting this candidate leaves MR-01 unchanged. It may expose downstream FR ownership but does not require rewriting MR-01.

#### F. Downstream pressure — non-authoring note

Downstream FRs will likely need to express Stage 1 urgency classification, Stage 2 description, Stage 3 retrieval, and Stage 4 synthesis. This report does not author those FRs.

#### G. Disposition

`ACCEPT AS DECISION CANDIDATE`

**Rationale:** It is a material architecture/strategy commitment that restricts MR-01 and is supported by the original architecture document.

---

### EXT-DEC-02 — Adozione di una scala di urgenza a tre livelli HIGH/MEDIUM/LOW

#### A. Original documentation evidence

**Source:** `OR2_Model_Test_Report.pdf`; `OR2_Architecture_Document.pdf`; `OR3_Dataset_Metadata_Catalog.pdf`
**Page/section:** Model Test Report p.1; Architecture p.1; Dataset Catalog schema

**VERBATIM SOURCE**

> “Task 3-class skin lesion urgency: HIGH / MEDIUM / LOW”

> Stage 1 output: “HIGH / MEDIUM / LOW + confidence”

> Dataset column: “urgency\_level string HIGH / MEDIUM / LOW”

**PARAPHRASE**

The project consistently uses a three-level urgency classification.

**INTERPRETATION**

This is a project convention/policy for urgency representation. It restricts how MR-01 urgency is expressed.

#### B. Minimum source-supported meaning

**Established:**

- urgency is represented as HIGH, MEDIUM, or LOW;
- the classifier is trained/tested as a 3-class task;
- the dataset uses the same urgency levels.

**Not established:**

- precise clinical definitions of each level;
- whether the three-level scale is immutable or replaceable;
- how no-image symptom scoring maps to these levels in all cases.

**Ambiguity / conflict:**
MEDIUM is underrepresented in the test set, but this is a data limitation, not a semantic conflict.

#### C. Candidate Decision

**Context**
MR-01 requires determining urgency. The project needs a governed urgency vocabulary.

**Decision**
Adopt a three-level urgency scale: HIGH, MEDIUM, LOW.

**Consequences**

- urgency outputs and downstream mappings use this vocabulary;
- changes to the scale would affect classifier labels, dataset semantics, and priority mapping;
- the scale can remain stable while implementation models change.

#### D. Classification gate

**Decision vs MR:** Restricts MR-01 by fixing the urgency outcome vocabulary.
**Decision vs FR:** It is a convention/policy, not an operational obligation.
**Decision vs realization:** It is not merely a model artifact; it is the project’s urgency vocabulary.
**R5/R6 rule(s) applied:** R5 Decision definition; R5 allowed result domain vs conditional selection rule.

#### E. MR stability / boundary effect

MR-01 remains stable. The scale is a convention under the same macro responsibility.

#### F. Downstream pressure — non-authoring note

Downstream FRs may need to define how the classifier produces each level and how the levels map to priority.

#### G. Disposition

`ACCEPT AS DECISION CANDIDATE`

**Rationale:** It is a stable project convention that restricts MR-01’s urgency determination.

---

### EXT-DEC-03 — Adozione di una scala di priorità operativa P1-P4 con SLA associati

#### A. Original documentation evidence

**Source:** `OR2_Architecture_Document.pdf`
**Page/section:** Page 1, “Adaptation Layer Mapping”

**VERBATIM SOURCE**

> “Adaptation Layer: map\_urgency\_to\_p\_scale() assigns P1-P4, specialist and SLA”

> \| Urgency + Condition | P-Scale | SLA |
> \| HIGH + confidence > 0.85 | P1 | 24 hours |
> \| HIGH | P2 | 48 hours |
> \| MEDIUM | P3 | 72 hours |
> \| LOW | P4 | 7 giorni |

**PARAPHRASE**

The project maps urgency to an operational priority scale P1–P4 with associated SLA times.

**INTERPRETATION**

The adoption of the P-scale and SLA association is a material priority policy under MR-01. The exact conditional mapping is a governed rule that likely belongs to FR semantics. The specialist destination part of the adaptation layer belongs to MR-02 and must not be absorbed here.

#### B. Minimum source-supported meaning

**Established:**

- P1–P4 priority scale exists;
- SLA times are associated with P-levels;
- mapping uses urgency and, for P1, confidence > 0.85.

**Not established:**

- full input semantics for the mapping, especially no-image cases;
- SLA trigger/outcome/owner/normative binding;
- whether specialist assignment is part of the same Decision or MR-02.

**Ambiguity / conflict:**
R6 explicitly lists “P-scale complete input semantics and no-image binding” and “SLA trigger/outcome/owner/normative binding” as open gaps.

#### C. Candidate Decision

**Context**
MR-01 includes operational triage priority. The project needs a governed priority scale and SLA association.

**Decision**
Adopt a P1–P4 operational priority scale with associated SLA times.

**Consequences**

- triage output can be translated into operational priority;
- SLA times are linked to priority levels;
- the exact conditional mapping remains a downstream operational rule;
- specialist destination must remain owned by MR-02.

#### D. Classification gate

**Decision vs MR:** Restricts MR-01’s priority scope.
**Decision vs FR:** Adoption of the scale is a Decision; the mapping rule is likely FR-level.
**Decision vs configuration:** SLA times are parameters, but the scale and association are policy.
**R5/R6 rule(s) applied:** R5 Decision definition; R5 FR-02 example; R6 selection semantics.

#### E. MR stability / boundary effect

MR-01 remains stable. The Decision exposes boundary pressure: specialist assignment must not leak into MR-01.

#### F. Downstream pressure — non-authoring note

Downstream FRs will need to define the conditional mapping and preserve no-image binding. The specialist part belongs to MR-02.

#### G. Disposition

`ACCEPT AS DECISION CANDIDATE`

**Rationale:** It is a material priority policy under MR-01, supported by the adaptation layer documentation.

---

### EXT-DEC-04 — Supporto di un percorso sintomi-only in assenza di immagine

#### A. Original documentation evidence

**Source:** `OR2_Architecture_Document.pdf`; `DDTA_DERMATRIAGE_MR_ONLY_INPUT_R1.md`
**Page/section:** Architecture p.1, “Fallback”; MR-01 Context

**VERBATIM SOURCE**

> “Fallback: When no image is available, symptom-only scoring derives urgency from B4 chatbot interaction fields (itching, bleeding, growing, changing, pain, etc.).”

> MR-01 Context: “Quando non e’ presente un’immagine della lesione, il progetto prevede un percorso basato sui sintomi disponibili.”

**PARAPHRASE**

The project supports a no-image triage path that derives urgency from symptom fields.

**INTERPRETATION**

The existence of the fallback path is a material boundary/strategy commitment under MR-01, because MR-01 explicitly includes urgency determination even without an image.

#### B. Minimum source-supported meaning

**Established:**

- a no-image path exists;
- it uses symptom-only scoring;
- example inputs include itching, bleeding, growing, changing, pain.

**Not established:**

- which symptoms are required vs optional;
- missing-value semantics;
- scoring algorithm, thresholds, or confidence;
- how the result binds to P-scale.

**Ambiguity / conflict:**
R6 lists “no-image required/optional symptom inputs and missing-value semantics” as an explicit documentation gap.

#### C. Candidate Decision

**Context**
Images are not always available, but MR-01 still requires urgency and operational priority.

**Decision**
Support a symptom-only triage path when no image is available.

**Consequences**

- the project owns a no-image branch;
- symptom inputs become relevant to triage;
- the scoring rule and missing-value semantics remain unresolved gaps;
- the no-image branch must still feed priority determination.

#### D. Classification gate

**Decision vs MR:** Restricts MR-01 by fixing a fallback path.
**Decision vs FR:** The path existence is a Decision/boundary commitment; the scoring behavior is FR-level.
**Decision vs realization:** It is not merely a technical artifact; it is a project-supported alternate route.
**R5/R6 rule(s) applied:** R5 Decision definition; R6 source-gap preservation.

#### E. MR stability / boundary effect

MR-01 remains stable. The MR Context already mentions the no-image path, but the commitment to support it is still a Decision under MR-01.

#### F. Downstream pressure — non-authoring note

Downstream FRs/gaps include symptom input semantics, scoring, and binding to P-scale.

#### G. Disposition

`ACCEPT AS DECISION CANDIDATE`

**Rationale:** It is a material alternate triage path governed under MR-01.

---

### EXT-DEC-05 — Adozione di una soglia HIGH pari a 0.25 per privilegiare la sensibilità

#### A. Original documentation evidence

**Source:** `OR2_Model_Test_Report.pdf`
**Page/section:** p.1, “Model Architecture”; p.4, “Threshold Analysis”

**VERBATIM SOURCE**

> “Inference threshold 0.25 for HIGH (tuned from 0.60 > 0.70 > 0.40 > 0.25)”

> “Final value of 0.25 selected to maximise HIGH sensitivity to meet the >90% clinical target.”

**PARAPHRASE**

The project tuned the HIGH classification threshold to 0.25 to increase HIGH sensitivity.

**INTERPRETATION**

This is a numeric parameter and a safety-oriented tuning result. R6 parameter governance requires distinguishing the literal value from the semantic owner, lifecycle, and purpose.

#### B. Minimum source-supported meaning

**Established:**

- threshold 0.25 is the final inference threshold for HIGH;
- it was selected to meet a >90% sensitivity target.

**Not established:**

- who owns the threshold;
- whether it is a Decision, an FR parameter, or a configuration binding;
- how it behaves in no-image cases.

**Ambiguity / conflict:**
The threshold is material, but the guides warn against promoting every numeric/config value to a Decision.

#### C. Candidate Decision

**Context**
The classifier must balance HIGH sensitivity against overall accuracy.

**Decision**
Set the HIGH inference threshold to 0.25 to prioritise HIGH sensitivity.

**Consequences**

- HIGH sensitivity increases;
- overall accuracy and false LOW rate remain problematic;
- threshold changes are parameter changes with safety impact.

#### D. Classification gate

**Decision vs MR:** It restricts how urgency is determined, but it is more naturally a parameter under an FR for Stage 1.
**Decision vs FR / parameter:** R6 parameter governance places numeric config values under a semantic owner; this is likely a parameter/binding, not a standalone Decision.
**R5/R6 rule(s) applied:** R6 Step 12 and 20.1 parameter governance boundary.

#### E. MR stability / boundary effect

MR-01 unchanged. The threshold can change without changing the macro responsibility.

#### F. Downstream pressure — non-authoring note

Downstream FR/parameter governance should record the threshold, its owner, lifecycle, and purpose.

#### G. Disposition

`LOWER_LEVEL`

**Rationale:** It is a material parameter/configuration binding under the Stage 1 urgency classifier, not a standalone Decision. If the project later governs the safety policy explicitly, the policy could be a Decision; the literal 0.25 should remain a binding.

---

### EXT-DEC-06 — Adozione di modelli AI specifici: EfficientNet-B4, Qwen2-VL, ChromaDB/all-MiniLM, BioMistral

#### A. Original documentation evidence

**Source:** `OR2_Architecture_Document.pdf`; `OR4_Training_Environment_Config.pdf`
**Page/section:** Architecture p.1; Technology Stack p.4

**VERBATIM SOURCE**

> Stage 1: EfficientNet-B4 (fine-tuned)
> Stage 2: Qwen2-VL-7B-Instruct
> Stage 3: RAG — ChromaDB
> Stage 4: BioMistral-7B

**PARAPHRASE**

The current realization uses these specific models and libraries.

**INTERPRETATION**

R5 technical choice routing says concrete names should remain where they materially participate. However, the Decision candidate is the pipeline adoption; the specific models are likely FR-level realization details under that Decision.

#### B. Minimum source-supported meaning

**Established:**

- current models are named and used in the pipeline.

**Not established:**

- whether each model choice is an immutable governed commitment or replaceable realization;
- whether the project would treat model replacement as a new Decision.

**Ambiguity / conflict:**
R5’s DermaTriage example places EfficientNet-B4 etc. in FRs under DEC-12, not as separate Decisions.

#### C. Candidate Decision

**Context**
The image-based pipeline needs concrete components.

**Decision**
Use EfficientNet-B4, Qwen2-VL-7B-Instruct, ChromaDB/all-MiniLM-L6-v2, and BioMistral-7B.

**Consequences**

- current realization binds to these components;
- replacement may affect behavior and performance;
- names must not be genericized away if they remain material.

#### D. Classification gate

**Decision vs FR / realization:** These are concrete component choices under the pipeline Decision.
**R5/R6 rule(s) applied:** R5 technical choice routing; R5 DermaTriage DEC-12 example.

#### E. MR stability / boundary effect

MR-01 unchanged.

#### F. Downstream pressure — non-authoring note

FRs under EXT-DEC-01 should preserve the concrete names.

#### G. Disposition

`LOWER_LEVEL`

**Rationale:** These are realization/FR-level commitments under the pipeline Decision, not separate MR-01 Decisions.

---

### EXT-DEC-07 — Adozione di RAG top-5 casi storici per supportare la decisione finale

#### A. Original documentation evidence

**Source:** `OR2_Architecture_Document.pdf`
**Page/section:** Page 1, Stage 3

**VERBATIM SOURCE**

> “Stage 3: find\_similar\_cases() — ChromaDB retrieves top-5 similar cases by cosine similarity”

**PARAPHRASE**

The pipeline retrieves five similar historical cases to enrich the final decision.

**INTERPRETATION**

This is a specific operational behavior within the pipeline. It is likely FR-level.

#### B. Minimum source-supported meaning

**Established:**

- top-5 retrieval is part of Stage 3.

**Not established:**

- full selection semantics, deduplication, underfill behavior, or reuse rules.

**Ambiguity / conflict:**
R6 lists prompt evidence window/selection semantics as gaps.

#### C. Candidate Decision

**Context**
The final triage synthesis uses historical cases.

**Decision**
Retrieve top-5 similar historical cases via ChromaDB cosine similarity.

**Consequences**

- retrieval enriches Stage 4 input;
- selection semantics remain partly unspecified.

#### D. Classification gate

**Decision vs FR / operational obligation:** It is an operational behavior under the pipeline Decision.
**R5/R6 rule(s) applied:** R5 FR definition; R6 selection semantics.

#### E. MR stability / boundary effect

MR-01 unchanged.

#### F. Downstream pressure — non-authoring note

FR-level selection semantics may need clarification.

#### G. Disposition

`LOWER_LEVEL`

**Rationale:** It is a pipeline stage behavior, not a standalone MR-01 Decision.

---

### EXT-DEC-08 — Adozione di output JSON finale con urgenza, confidence, reasoning, pathology

#### A. Original documentation evidence

**Source:** `OR2_Architecture_Document.pdf`
**Page/section:** Page 1, Stage 4

**VERBATIM SOURCE**

> “Stage 4: BioMistral-7B — Stage 1+2+3 + symptoms — JSON: urgency, confidence, reasoning, pathology”

**PARAPHRASE**

The final output includes urgency, confidence, reasoning, and pathology in JSON.

**INTERPRETATION**

This is an output/interface detail. Urgency is relevant to MR-01; pathology is not clearly owned by MR-01. It is not a Decision candidate.

#### B. Minimum source-supported meaning

**Established:**

- final JSON structure includes those fields.

**Not established:**

- pathology authority/obligation;
- whether the JSON format is a governed commitment or current binding.

**Ambiguity / conflict:**
R6 lists “predicted pathology obligation/authority” as a gap.

#### C. Candidate Decision

**Context**
The pipeline must return a result.

**Decision**
Return JSON with urgency, confidence, reasoning, pathology.

**Consequences**

- output consumers depend on the format;
- pathology ownership remains unclear.

#### D. Classification gate

**Decision vs FR / interface detail:** It is an output/interface detail, likely FR-level.
**R5/R6 rule(s) applied:** R5 FR definition; R6 source gaps.

#### E. MR stability / boundary effect

MR-01 unchanged.

#### F. Downstream pressure — non-authoring note

Pathology ownership is a gap; do not absorb into MR-01 without evidence.

#### G. Disposition

`LOWER_LEVEL`

**Rationale:** Interface/output detail, not a Decision under MR-01.

---

### EXT-DEC-09 — Adozione di target di sicurezza HIGH sensitivity >90%, false LOW <5%, accuracy >85%

#### A. Original documentation evidence

**Source:** `OR2_Model_Test_Report.pdf`; `OR5_Test_Environment_Setup.pdf`
**Page/section:** Model Test Report p.3–4; Test Environment p.4

**VERBATIM SOURCE**

> “HIGH Sensitivity 90.24% (target: >90%) PASS”
> “False LOW rate 7.93% (target: <5%) FAIL”
> “Overall Accuracy 81.74% (target: >85%) FAIL”

**PARAPHRASE**

The project records safety and quality targets for the urgency classifier.

**INTERPRETATION**

These are quality/verification criteria. They may be requirements or acceptance gates, not Decisions.

#### B. Minimum source-supported meaning

**Established:**

- targets exist;
- current values are recorded.

**Not established:**

- governance authority for the targets;
- whether they are Decision-level policy or verification requirements.

**Ambiguity / conflict:**
They are documented but not clearly owned at Decision level.

#### C. Candidate Decision

**Context**
The classifier must be evaluated.

**Decision**
Adopt safety targets for HIGH sensitivity, false LOW, and accuracy.

**Consequences**

- evaluation criteria exist;
- current model fails some targets.

#### D. Classification gate

**Decision vs requirement/verification:** Likely verification/quality requirements, not a Decision.
**R5/R6 rule(s) applied:** R5 Requirement vs Decision; R6 parameter/verification evidence.

#### E. MR stability / boundary effect

MR-01 unchanged.

#### F. Downstream pressure — non-authoring note

They belong to verification/quality governance.

#### G. Disposition

`LOWER_LEVEL`

**Rationale:** Verification/quality criteria, not a Decision candidate under MR-01.

---

## 5. Inspected evidence not promoted to Decision

| **Evidence/factSourceClassificationWhy not a Decision?Preserved downstream question** |                              |                         |                                           |                               |
| ------------------------------------------------------------------------------------- | ---------------------------- | ----------------------- | ----------------------------------------- | ----------------------------- |
| API endpoints list                                                                    | OR2 p.2, OR5 p.1             | Interface detail        | Operational interface, not MR-01 Decision | Which endpoints serve triage? |
| B4 integration calls                                                                  | OR2 p.2                      | Integration realization | External platform integration             | How B4 binds to triage?       |
| Storage architecture                                                                  | OR2 p.3                      | Realization             | Persistence detail                        | Not MR-01 priority            |
| Technology stack versions                                                             | OR2 p.4                      | Realization/config      | Current bindings                          | Revalidation if changed       |
| Live system status                                                                    | OR2 p.4                      | Runtime state           | Not governance commitment                 | Operational monitoring        |
| Training configuration                                                                | OR2 Model Test Report p.2    | Model realization       | Training detail                           | Model quality                 |
| Confusion matrix                                                                      | OR2 Model Test Report p.3    | Evidence                | Performance evidence                      | Safety evaluation             |
| Dataset schema/class distribution                                                     | OR3                          | Data facts              | Dataset description                       | Data quality                  |
| ChromaDB file sizes                                                                   | OR3 p.3                      | Storage fact            | Realization                               | Performance                   |
| Retraining trigger 50 corrections                                                     | OR4 Training Cycles p.3      | MR-04 adaptation        | Adaptation threshold                      | MR-04 ownership               |
| Label mapping P1/P2→HIGH etc.                                                         | OR4 Training Cycles p.3      | MR-04 adaptation        | Retraining label mapping                  | MR-04 ownership               |
| Prompt evolution 10 corrections                                                       | OR4 Training Cycles p.4      | MR-04 adaptation        | Prompt update                             | MR-04 ownership               |
| Environment variables                                                                 | OR4 Environment Config p.2   | Configuration           | Runtime config                            | Deployment                    |
| Directory structure                                                                   | OR4 Environment Config p.2–3 | Realization             | Repo layout                               | Maintenance                   |
| Test data example                                                                     | OR5 p.3                      | Test evidence           | Test fixture                              | Verification                  |
| Known limitations                                                                     | OR5 p.3                      | Evidence/gap            | Limitations                               | Risk review                   |
| Predicted pathology                                                                   | OR2 p.1                      | Gap/other MR            | Not clearly MR-01                         | Pathology authority           |
| Specialist destination                                                                | OR2 p.1                      | MR-02                   | Out of MR-01 scope                        | MR-02                         |
| Medical validation                                                                    | OR2 p.2–3                    | MR-03                   | Out of MR-01 scope                        | MR-03                         |
| Adaptation loops                                                                      | OR2 p.3                      | MR-04                   | Out of MR-01 scope                        | MR-04                         |

---

## 6. Decision-family regression

### 6.1 Pairwise overlap / duplication

- EXT-DEC-01 (pipeline) and EXT-DEC-02 (urgency scale) are distinct: pipeline composition vs outcome vocabulary.
- EXT-DEC-02 (urgency scale) and EXT-DEC-03 (P-scale/SLA) are distinct: clinical urgency vs operational priority.
- EXT-DEC-01 (image-based pipeline) and EXT-DEC-04 (symptom-only path) are distinct alternate routes.
- EXT-DEC-05/06/07/08/09 are lower-level and do not compete as Decisions.

### 6.2 Too broad / too technical candidates

- EXT-DEC-06 is too technical as a Decision; it belongs under EXT-DEC-01.
- EXT-DEC-07 and EXT-DEC-08 are pipeline/interface details.
- EXT-DEC-09 is verification/quality criteria.
- EXT-DEC-05 is a parameter binding.

### 6.3 Unowned source-supported commitments

- Predicted pathology appears in the pipeline output but is not clearly owned by MR-01. Record as gap/other MR.
- Specialist destination is explicitly MR-02.
- Medical validation/correction is explicitly MR-03.
- Adaptation is explicitly MR-04.

### 6.4 Semantic ownership / later one-parent readiness

Accepted Decisions can support later one-parent FR ownership:

- EXT-DEC-01 → stage FRs;
- EXT-DEC-02 → urgency classification FRs;
- EXT-DEC-03 → mapping/SLA FRs;
- EXT-DEC-04 → symptom-path FRs.

No obvious one-parent contradiction was found, provided pipeline order is not treated as dependency and specialist assignment is kept under MR-02.

### 6.5 MR wording pressure

MR-01 Context already mentions the no-image path. This is not a contradiction, but it means the no-image commitment is partly pre-encoded at MR level. It does not require rewriting MR-01 in this experiment; it is recorded as a Decision under MR-01.

### 6.6 Newly discovered candidate(s), if any

No new candidate beyond those reviewed above was discovered during family regression.

---

## 7. Closure result

| **External IDTitleMain source(s)Final classificationDispositionMR impactOpen downstream pressure** |                                                                |                                                             |                      |              |                              |                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------------------------------------------------- | -------------------- | ------------ | ---------------------------- | ---------------------------------------------------------- |
| EXT-DEC-01                                                                                         | Adozione di una pipeline AI image-based a quattro stadi        | OR2 Architecture p.1                                        | Decision candidate   | ACCEPT       | None                         | FRs for stages; pipeline order ≠ dependency                |
| EXT-DEC-02                                                                                         | Adozione di una scala di urgenza a tre livelli HIGH/MEDIUM/LOW | OR2 Model Test Report p.1; OR2 Architecture p.1; OR3 schema | Decision candidate   | ACCEPT       | None                         | Clinical definitions of levels                             |
| EXT-DEC-03                                                                                         | Adozione di una scala di priorità operativa P1-P4 con SLA      | OR2 Architecture p.1                                        | Decision candidate   | ACCEPT       | Boundary pressure with MR-02 | Mapping rule; no-image binding; SLA ownership              |
| EXT-DEC-04                                                                                         | Supporto di un percorso sintomi-only in assenza di immagine    | OR2 Architecture p.1; MR input Context                      | Decision candidate   | ACCEPT       | None                         | Required/optional inputs; missing-value semantics; scoring |
| EXT-DEC-05                                                                                         | Soglia HIGH 0.25                                               | OR2 Model Test Report p.1, p.4                              | Parameter/binding    | LOWER\_LEVEL | None                         | Threshold owner/lifecycle                                  |
| EXT-DEC-06                                                                                         | Modelli AI specifici                                           | OR2 Architecture p.1, p.4                                   | Realization/FR-level | LOWER\_LEVEL | None                         | Replaceability                                             |
| EXT-DEC-07                                                                                         | RAG top-5                                                      | OR2 Architecture p.1                                        | Pipeline behavior    | LOWER\_LEVEL | None                         | Selection semantics                                        |
| EXT-DEC-08                                                                                         | Output JSON                                                    | OR2 Architecture p.1                                        | Interface detail     | LOWER\_LEVEL | None                         | Pathology authority                                        |
| EXT-DEC-09                                                                                         | Safety targets                                                 | OR2 Model Test Report p.3–4                                 | Verification/quality | LOWER\_LEVEL | None                         | Acceptance/rollback binding                                |

### Closure gates

- **Source coverage sufficient:** PASS
- **Decision discovery complete for supplied source set:** PASS (with explicit gaps recorded)
- **Pairwise non-overlap:** PASS
- **MR wording requires review:** NO / UNCERTAIN. The no-image path is already in MR Context; no rewrite is required for this reconstruction, but the boundary should be reviewed if the experiment wants Context to contain only framing and not commitments.
- **Remaining HOLD items:**
  - no-image required/optional symptom inputs and missing-value semantics;
  - P-scale complete input semantics and no-image binding;
  - SLA trigger/outcome/owner/normative binding;
  - predicted pathology obligation/authority;
  - specialist selection vocabulary/rule/input/fallback/booking (MR-02);
  - review content/lifecycle/disagreement binding (MR-03);
  - adaptation counting/threshold authority (MR-04);
  - deployment authority/automaticity;
  - acceptance/rollback binding.

---

## 8. METHODOLOGY OBSERVATIONS — POST-RECONSTRUCTION

### 8.1 R5 rules that were clear

- Decision definition: significant commitment restricting exactly one MR.
- Technical choice routing: concrete names should remain at the correct semantic owner.
- Decision vs FR: FRs are operational obligations under exactly one Decision.
- Consequences should describe the system, not method instructions.
- Pipeline membership/order is not automatically `dependOn`.

### 8.2 R5 rules that required interpretation

- Whether a scale/vocabulary (HIGH/MEDIUM/LOW) is a Decision or an FR convention.
- Whether a priority mapping table is a Decision or an FR conditional selection rule.
- Whether a numeric threshold is a Decision, an FR parameter, or a configuration binding.
- Whether the no-image path is a Decision under MR-01 or already fully captured by MR Context.

### 8.3 R6 refinements that materially changed or clarified the analysis

- Parameter governance boundary helped classify the 0.25 threshold as lower-level.
- Selection semantics helped distinguish candidate population, criterion, bound, and selected result for RAG top-5.
- Pipeline membership/order non-dependency helped avoid turning stage order into `dependOn`.
- Explicit gap list helped preserve no-image and P-scale gaps instead of inventing semantics.

### 8.4 R5/R6 tensions or ambiguity

- R5’s DermaTriage DEC-12 example places the four-stage pipeline as a Decision and concrete models as FRs. That supported EXT-DEC-01 and LOWER\_LEVEL for EXT-DEC-06.
- R6 Candidate R2 is non-normative; I used it only where it clarified R5, not as authority.
- The priority mapping is a true conditional rule; R5 suggests it belongs to FR semantics, but the adoption of the P-scale is still a Decision. This split was the main interpretive step.

### 8.5 Cases where multiple materially different classifications remained compatible with the guides

- EXT-DEC-02: could be a separate Decision or part of EXT-DEC-01. I kept it separate because the urgency vocabulary is independently changeable.
- EXT-DEC-03: the P-scale adoption could be a Decision; the mapping table could be an FR. I split accordingly.
- EXT-DEC-05: could be a Decision about safety policy or an FR parameter. I chose LOWER\_LEVEL under R6 parameter governance.

### 8.6 Guide wording that caused uncertainty

- “Decision” vs “convention” for urgency levels.
- “Decision” vs “parameter” for thresholds and SLA times.
- “Consequences” vs “downstream pressure” for unresolved gaps.
- How much MR Context may already encode a commitment that would otherwise be a Decision.

No R7 text is proposed in this report.