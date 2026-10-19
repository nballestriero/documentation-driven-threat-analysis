"""R2 regression and selection integrity tests: no third-party dependencies."""
import copy
import re
import unittest
from pathlib import Path
from ddta_temporal_query import (load,validate,QueryError,present,related,nearby,closure,
                                 query,dispatch,select_propositions,projection,mmd_report,temporal_projection)
D=load(Path(__file__).with_name('CASO_DERMATRIAGE_PESI.md'))
S=lambda x:"SELECT HISTORY FROM BA WHERE REFERENT = '"+x+"';"
P=lambda x:dispatch(D,x)[1]

class DDTAWeightsR2(unittest.TestCase):
 def test_01_schema_valid(self):self.assertTrue(validate(D))
 def test_02_stable_identity(self):self.assertEqual(sum(r['id']=='EfficientNetB4WeightsArtifact' for r in D['referents']),1)
 def test_03_baseline_only(self):self.assertEqual(len(D['versions']),1)
 def test_04_transfer_roles(self):
  p=next(p for p in D['propositions'] if p['id']=='BAP-FRC6-01-03A1-04')
  self.assertEqual((p['roles']['source'],p['roles']['content'],p['roles']['destination']),('GoogleDriveModelStore','EfficientNetB4WeightsArtifact','ActiveClassifierStore'))
 def test_05_no_retraining_run(self):self.assertFalse(any(o['context']=='T_RETRAIN' for o in D['occurrences']))
 def test_06_unknown_retraining_presence(self):self.assertIn('UNKNOWN',present(D,'EfficientNetB4WeightsArtifact','T_RETRAIN'))
 def test_07_known_setup_presence(self):self.assertIn('PRESENT',present(D,'EfficientNetB4WeightsArtifact','T_SETUP'))
 def test_08_temporal_partial_order(self):
  c=closure(D['precedes'],{x['id'] for x in D['contexts']})
  self.assertNotIn('T_RUNTIME',c['T_RETRAIN']);self.assertNotIn('T_RETRAIN',c['T_RUNTIME'])
 def test_09_all_bap_roles_validated(self):
  d=copy.deepcopy(D);d['propositions'][0]['roles'].pop('source')
  with self.assertRaises(QueryError):validate(d)
 def test_10_no_precedence_cycle(self):
  d=copy.deepcopy(D);d['precedes'].append(['T_QUALIFY','T_SETUP'])
  with self.assertRaises(QueryError):validate(d)
 def test_11_prohibit_unsupported_version_presence(self):
  d=copy.deepcopy(D);d['presence']=[x for x in d['presence'] if x['subject']!='EfficientNetB4WeightsArtifact@baseline-1.0.0']
  with self.assertRaises(QueryError):validate(d)
 def test_12_discovery(self):
  v,m=dispatch(D,'SHOW REFERENTS FROM BA;');self.assertIsNone(m);self.assertIn('`ImageUrgencyAnalysis`',v);self.assertIn('`ActiveClassifierStore`',v)
 def test_13_discovery_count(self):
  v,_=dispatch(D,'SHOW REFERENTS FROM BA;');self.assertEqual(len([line for line in v.splitlines() if line.startswith('| `')]),len(D['referents']))
 def test_14_describe(self):
  v,m=dispatch(D,"DESCRIBE REFERENT 'ActiveClassifierStore';")
  self.assertIsNone(m);self.assertIn('BAP-FRC6-01-03A1-04',v);self.assertIn('BAP-FRC6-01-03A1-08',v)
 def test_15_describe_unknown(self):
  with self.assertRaises(QueryError):dispatch(D,"DESCRIBE REFERENT 'NoSuchReferent';")
 def test_16_history_text(self):
  txt,m=dispatch(D,S('EfficientNetB4WeightsArtifact'))
  self.assertIn('EF06',txt);self.assertIn('UNKNOWN',txt);self.assertIsNotNone(m)
 def test_17_direct_weights_ids(self):
  inc,exc,refs=select_propositions(D,P(S('EfficientNetB4WeightsArtifact')))
  self.assertEqual({p['id'] for p,h in inc},{'BAP-FRC6-01-03A1-04','BAP-FRC6-01-03A1-07','BAP-FRC6-01-03A1-08'})
 def test_18_direct_store_ids(self):
  inc,exc,refs=select_propositions(D,P(S('ActiveClassifierStore')))
  self.assertEqual({p['id'] for p,h in inc},{'BAP-FRC6-01-03A1-04','BAP-FRC6-01-03A1-08'})
 def test_19_direct_analysis_ids(self):
  inc,exc,refs=select_propositions(D,P(S('ImageUrgencyAnalysis')))
  self.assertEqual({p['id'] for p,h in inc},{'BAP-FR03-01-01','BAP-FR03-01-02'})
 def test_20_three_views_differ(self):
  m=[projection(D,P(S(f)))[0] for f in ('EfficientNetB4WeightsArtifact','ActiveClassifierStore','ImageUrgencyAnalysis')]
  self.assertEqual(len(set(m)),3)
 def test_21_weights_without_fabricated_model_edge(self):
  m,*_=projection(D,P(S('EfficientNetB4WeightsArtifact')))
  self.assertNotIn('R_EfficientNet_B4',m);self.assertNotIn('R_ClassifierAdaptationCycle',m)
 def test_22_produce_realize_correct(self):
  m,*_=projection(D,P(S('ImageUrgencyAnalysis')))
  self.assertIn('R_EfficientNet_B4 -.->|realize| R_ImageUrgencyAnalysis',m)
  self.assertIn('R_LesionImage --> R_ImageUrgencyAnalysis',m)
  self.assertIn('R_ImageUrgencyAnalysis -->|"produce<br/>BAP-FR03-01-01"| R_ImageUrgencyClassification',m)
 def test_23_haspart_without_arrow(self):
  m,*_=projection(D,P(S('EfficientNetB4WeightsArtifact')))
  self.assertIn('subgraph HP_GoogleDriveModelStore',m)
  self.assertIn('subgraph HP_ActiveClassifierStore',m)
  self.assertNotIn('|"hasPart',m)
 def test_24_project_style_external_boundary(self):
  m,*_=projection(D,P(S('EfficientNetB4WeightsArtifact')))
  self.assertRegex(m,r'style HP_GoogleDriveModelStore[^\n]*stroke:#C62828[^\n]*stroke-dasharray:7 5[;,]')
 def test_25_transfer_complete(self):
  m,*_=projection(D,P(S('EfficientNetB4WeightsArtifact')))
  self.assertIn('R_GoogleDriveModelStore -->|"transfer',m)
  self.assertIn('R_EfficientNetB4WeightsArtifact --> R_ActiveClassifierStore',m)
 def test_26_behavior_helper_marked_non_ba(self):
  m,*_=projection(D,P(S('EfficientNetB4WeightsArtifact')))
  self.assertIn('behavior role / projection only',m)
  self.assertIn('stroke:#909090',m)
 def test_27_candidate_preserved(self):
  m,es,inc,exc,used=projection(D,P(S('BaselineClassifierMetricEvaluation')))
  self.assertIn('CANDIDATE',m);self.assertIn('produce<br/>',m)
  self.assertEqual(inc[0][0]['status'],'CANDIDATE')
 def test_28_depth_expansion(self):
  sql="SELECT NEIGHBORHOOD 3 FROM BA WHERE REFERENT = 'EfficientNetB4WeightsArtifact';"
  inc,exc,refs=select_propositions(D,P(sql))
  self.assertIn('BAP-FRC6-01-03A1-09',{p['id'] for p,h in inc})
  self.assertNotIn('BAP-FR03-01-01',{p['id'] for p,h in inc})
 def test_29_limit_excludes_entire_proposition(self):
  inc,exc,refs=select_propositions(D,P(S('EfficientNetB4WeightsArtifact')),max_nodes=2)
  self.assertTrue(exc);self.assertTrue(all(set(p['roles'].values())<=refs for p,h in inc));self.assertLessEqual(len(refs),2)
 def test_30_excluded_visible_in_report(self):
  _,md=mmd_report(D,P(S('EfficientNetB4WeightsArtifact')),S('EfficientNetB4WeightsArtifact'),2)
  self.assertIn('MAX_NODES',md);self.assertIn('non inclusa parzialmente',md)
 def test_31_at_retrain_no_invention(self):
  sql="SELECT AT 'T_RETRAIN' FROM BA WHERE REFERENT = 'EfficientNetB4WeightsArtifact';"
  m,es,inc,exc,refs=projection(D,P(sql))
  self.assertEqual(len(inc),0);self.assertNotIn(' -->',m);self.assertIn('R_EfficientNetB4WeightsArtifact',m)
 def test_32_at_setup(self):
  sql="SELECT AT 'T_SETUP' FROM BA WHERE REFERENT = 'EfficientNetB4WeightsArtifact';"
  m,es,inc,exc,refs=projection(D,P(sql));self.assertEqual(len(inc),3)
 def test_33_look_no_source_from_mermaid(self):
  _,md=mmd_report(D,P(S('ImageUrgencyAnalysis')),S('ImageUrgencyAnalysis'))
  self.assertIn('BAP-FR03-01-02',md);self.assertIn('## Perché questi elementi sono inclusi',md)
 def test_34_styles_contiguous(self):
  for focus in ('EfficientNetB4WeightsArtifact','ActiveClassifierStore','ImageUrgencyAnalysis','BaselineClassifierMetricEvaluation'):
   with self.subTest(focus=focus):
    m,es,_,_,_=projection(D,P(S(focus)))
    nums=[int(x) for x in re.findall(r'^\s*linkStyle\s+(\d+)\s',m,re.M)]
    self.assertEqual(nums,list(range(len(es))))
 def test_35_no_unrecognized_query(self):
  with self.assertRaises(QueryError):dispatch(D,"SELECT * FROM BA;")
 def test_36_reject_missing_focus(self):
  with self.assertRaises(QueryError):select_propositions(D,P(S('NoSuchReferent')))
 def test_37_no_fake_retrain_bap(self):
  self.assertFalse(any('retrain' in p['id'].lower() for p in D['propositions']))
 def test_38_mermaid_matches_report(self):
  for focus in ('EfficientNetB4WeightsArtifact','ActiveClassifierStore','ImageUrgencyAnalysis'):
   sql=S(focus);m,md=mmd_report(D,P(sql),sql)
   self.assertIn('```mermaid\n'+m.rstrip()+'\n```',md)


 def test_39_temporal_panel_separate_from_ba_topology(self):
  m,*_=projection(D,P(S('EfficientNetB4WeightsArtifact')))
  self.assertNotIn('TEMPORAL_PANEL',m)
  self.assertNotIn('TC_T_RUNTIME',m)
  timeline=temporal_projection(D,P(S('EfficientNetB4WeightsArtifact')))
  self.assertIn('TC_T_RUNTIME',timeline)
  self.assertIn('TC_T_RETRAIN',timeline)
  self.assertIn('UNKNOWN',timeline)
 def test_40_no_unproven_concurrency_edge(self):
  timeline=temporal_projection(D,P(S('EfficientNetB4WeightsArtifact')))
  self.assertNotIn('TC_T_RUNTIME -.->|"precedes / NON BA"| TC_T_RETRAIN',timeline)
  self.assertNotIn('TC_T_RETRAIN -.->|"precedes / NON BA"| TC_T_RUNTIME',timeline)
 def test_41_time_contexts_do_not_make_haspart(self):
  m,*_=projection(D,P(S('EfficientNetB4WeightsArtifact')))
  self.assertNotIn('HP_T_RETRAIN',m)
  self.assertNotIn('TEMPORAL_PANEL',m)
 def test_43_plain_produce_edge_is_explicit_and_unambiguous(self):
  m,*_=projection(D,P(S('ImageUrgencyAnalysis')))
  self.assertIn('R_LesionImage --> R_ImageUrgencyAnalysis',m)
  self.assertIn('R_ImageUrgencyAnalysis -->|"produce<br/>BAP-FR03-01-01"| R_ImageUrgencyClassification',m)
  self.assertIn('produce<br/>BAP-FR03-01-01',m)
  self.assertIn('-->|"produce',m)
  self.assertIn('R_EfficientNet_B4 -.->|realize| R_ImageUrgencyAnalysis',m)
  self.assertIn('BAP-FR03-01-02',m)
  self.assertIn('BAP-FR03-01-01"|',m)
 def test_44_time_query_only_selected_context(self):
  q="SELECT AT 'T_RETRAIN' FROM BA WHERE REFERENT = 'EfficientNetB4WeightsArtifact';"
  tm=temporal_projection(D,P(q))
  self.assertIn('TC_T_RETRAIN',tm)
  self.assertNotIn('TC_T_RUNTIME',tm)
 def test_45_analysis_topology_has_no_isolated_nodes(self):
  m,*_=projection(D,P(S('ImageUrgencyAnalysis')))
  self.assertNotIn('TEMPORAL_PANEL',m)
  for node in ('R_LesionImage','R_ImageUrgencyAnalysis','R_ImageUrgencyClassification','R_EfficientNet_B4'):
   self.assertGreater(m.count(node),1)
 def test_46_time_projection_explicit_in_report(self):
  _,md=mmd_report(D,P(S('ImageUrgencyAnalysis')),S('ImageUrgencyAnalysis'))
  self.assertIn('## Tempo logico — diagramma SEPARATO',md)
  self.assertIn('```mermaid\nflowchart LR\n  %% Pure temporal metadata',md)

 def test_42_no_temporal_retraining_observation(self):
  txt,_=dispatch(D,"SELECT AT 'T_RETRAIN' FROM BA WHERE REFERENT = 'EfficientNetB4WeightsArtifact';")
  self.assertIn('UNKNOWN',txt)
  self.assertNotIn('W_O0',txt)

 def test_fix2_produce_has_two_unlabelled_directed_arrows(self):
  m,*_=projection(D,P(S('ImageUrgencyAnalysis')))
  self.assertIn('R_LesionImage --> R_ImageUrgencyAnalysis',m)
  self.assertIn('R_ImageUrgencyAnalysis -->|"produce<br/>BAP-FR03-01-01"| R_ImageUrgencyClassification',m)
  self.assertEqual(len([e for e in m.splitlines() if e.strip().startswith('R_LesionImage -->')]),1)
  self.assertNotIn('R_LesionImage -->|transfer',m)
 def test_fix2_produce_bap_in_actor_not_edge_label(self):
  m,*_=projection(D,P(S('ImageUrgencyAnalysis')))
  self.assertRegex(m,r'R_ImageUrgencyAnalysis\("ImageUrgencyAnalysis<br/>.*BAP-FR03-01-01')
  self.assertIn('R_ImageUrgencyAnalysis -->|',m)
 def test_fix2_other_views_still_generated(self):
  for f in ('ActiveClassifierStore','EfficientNetB4WeightsArtifact'):
   m,*_=projection(D,P(S(f)))
   self.assertIn('flowchart LR',m)
   self.assertNotIn('R_ImageUrgencyAnalysis -->',m)

if __name__=='__main__':unittest.main(verbosity=2)

# Structural check: all four nodes in the selected produce/realize projection
# are part of a single weakly connected BA component, not just text snippets.
class VisualConnectivityRegression(unittest.TestCase):
 def test_analysis_nodes_are_topologically_connected(self):
  graph,*_=projection(D,P(S('ImageUrgencyAnalysis')))
  edges=[]
  for line in graph.splitlines():
   # Both standard and edge-labelled directed/dashed arrows.
   line=line.strip()
   if not line.startswith('R_'): continue
   m=re.match(r'(R_[A-Za-z0-9_]+)\s+(?:-->|-\.->)(?:\|(?:"[^"]*"|[A-Za-z]+)\|)?\s+(R_[A-Za-z0-9_]+)$',line)
   if m:edges.append(m.groups())
  adj={}
  for a,b in edges:
   adj.setdefault(a,set()).add(b)
   adj.setdefault(b,set()).add(a)
  seen={'R_ImageUrgencyAnalysis'}
  todo=list(seen)
  while todo:
   a=todo.pop()
   for b in adj.get(a,set())-seen:
    seen.add(b);todo.append(b)
  self.assertEqual(seen,{'R_ImageUrgencyAnalysis','R_LesionImage','R_ImageUrgencyClassification','R_EfficientNet_B4'})
  self.assertEqual(len(edges),3)

class WorkingR50GrammarConformance(unittest.TestCase):
 def test_actor_and_document_shapes_match_user_verified_profile_B(self):
  m,*_=projection(D,P(S('ImageUrgencyAnalysis')))
  self.assertRegex(m,r'R_ImageUrgencyAnalysis\("ImageUrgencyAnalysis')
  self.assertIn('R_LesionImage@{ shape: doc, label: "LesionImage" }',m)
  self.assertIn('R_ImageUrgencyClassification@{ shape: doc, label: "ImageUrgencyClassification" }',m)
  self.assertIn('subgraph BA_VIEW_WHITE["BA view — layout only"]',m)
  self.assertIn('style BA_VIEW_WHITE fill:#FFFFFF',m)
  self.assertNotIn('"flowchart":{"curve"',m)
 def test_produce_and_realize_are_cumulative_style(self):
  m,*_=projection(D,P(S('ImageUrgencyAnalysis')))
  self.assertIn('R_LesionImage --> R_ImageUrgencyAnalysis',m)
  self.assertIn('R_ImageUrgencyAnalysis -->|"produce<br/>BAP-FR03-01-01"| R_ImageUrgencyClassification',m)
  self.assertIn('R_EfficientNet_B4 -.->|realize| R_ImageUrgencyAnalysis',m)
  self.assertIn('classDef BAProduceActor fill:#212121',m)
  self.assertIn('classDef BALogicalData fill:#FFFFFF',m)
 def test_no_one_way_dead_end_due_to_wrong_ids(self):
  m,edgeops,inc,exc,used=projection(D,P(S('ImageUrgencyAnalysis')))
  self.assertEqual(len(edgeops),3)
  expected={'R_LesionImage','R_ImageUrgencyAnalysis','R_ImageUrgencyClassification','R_EfficientNet_B4'}
  tokens=set(re.findall(r'\bR_[A-Za-z_0-9]+\b',m))
  self.assertTrue(expected<=tokens)
  self.assertEqual({p['id'] for p,h in inc},{'BAP-FR03-01-01','BAP-FR03-01-02'})

class UserVerifiedProfileB(unittest.TestCase):
 def test_document_shapes_actor_and_edges_all_present(self):
  m,edgeops,inc,ex,used=projection(D,P(S('ImageUrgencyAnalysis')))
  self.assertIn('R_LesionImage@{ shape: doc, label: "LesionImage" }',m)
  self.assertIn('R_ImageUrgencyClassification@{ shape: doc, label: "ImageUrgencyClassification" }',m)
  self.assertIn('R_LesionImage --> R_ImageUrgencyAnalysis',m)
  self.assertIn('R_ImageUrgencyAnalysis -->|"produce<br/>BAP-FR03-01-01"| R_ImageUrgencyClassification',m)
  self.assertIn('R_EfficientNet_B4 -.->|realize| R_ImageUrgencyAnalysis',m)
  self.assertEqual(len(edgeops),3)
 def test_contrast_and_visual_frame_are_non_semantic(self):
  m,edgeops,inc,ex,used=projection(D,P(S('ImageUrgencyAnalysis')))
  self.assertIn('style BA_VIEW_WHITE fill:#FFFFFF',m)
  self.assertIn('linkStyle 1 stroke:#171717,stroke-width:3px',m)
  self.assertNotIn('BA_VIEW_WHITE -->',m)
  self.assertNotIn('BA_VIEW_WHITE -.->',m)
 def test_artifact_content_document_icon_all_views(self):
  for f in ('EfficientNetB4WeightsArtifact','ActiveClassifierStore'):
   m,*_=projection(D,P(S(f)))
   self.assertIn('R_EfficientNetB4WeightsArtifact@{ shape: doc',m)
 def test_no_semantic_changes(self):
  m,edges,included,excluded,used=projection(D,P(S('ImageUrgencyAnalysis')))
  self.assertEqual({p['id'] for p,_ in included},{'BAP-FR03-01-01','BAP-FR03-01-02'})
  self.assertEqual(edges,['realize','produce','produce'])

class OccurrenceVisualIdentityStyle(unittest.TestCase):
 def test_haspart_artifact_occurrences_use_bacontent(self):
  m,*_=projection(D,P(S('EfficientNetB4WeightsArtifact')))
  self.assertIn('O_BAP_FRC6_01_03A1_07@{ shape: doc',m)
  self.assertIn('O_BAP_FRC6_01_03A1_08@{ shape: doc',m)
  for line in m.splitlines():
   if line.strip().startswith('class ') and ' BAContent;' in line:
    self.assertIn('O_BAP_FRC6_01_03A1_07',line)
    self.assertIn('O_BAP_FRC6_01_03A1_08',line)
    break
  else:self.fail('missing BAContent class on occurrences')
