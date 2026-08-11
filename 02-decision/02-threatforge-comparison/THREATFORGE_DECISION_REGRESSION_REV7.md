# ThreatForge Decision regression after model-layering Revision 7

> **Non-canonical research checkpoint.**
>
> Baseline of the study: Decision model Revision 7 after separating L1 conceptual semantics, L2 representation contracts, L3 realization principles and L4 tool support/conformance.
> Construction corpus only: the sixteen revised candidate ADRs historically associated with ThreatForge MR-0001 and MR-0002. ThreatForge MR-0003, MR-0004 and MR-0005 remain untouched holdouts.

## Purpose

This checkpoint re-runs the construction corpus after discovering that `R-CLOSED-04` had been used at the wrong level. Executable projections remain a useful L3 realization principle, but they are not an L1 semantic invariant inherited by every governed project. Therefore a ThreatForge ADR is not redundant merely because it chooses a concrete way to realize that principle.

Each candidate is reviewed through four questions:

1. Is there a significant choice rather than a consequence, requirement or explanation?
2. Who owns the choice semantically: DDTA method/metamodel, canonical representation, ThreatForge product/tool, or ThreatForge project operations?
3. Is the historical parent Macro Requirement the natural semantic owner?
4. Does the candidate contribute a non-redundant choice without using L2/L3 principles as if they were L1 semantics?

## Regression table

\small

| Historical slot | Revised candidate | Revision 7 result | Rationale |
|---|---|---|---|
| `MR-0001 / ADR-0001` | Diátaxis come classificazione comune della funzione documentale | **RELOCATE - Decision DDTA method** | Scelta reale (Diátaxis vs classificazioni locali), ma la candidata attribuisce la scelta al metodo DDTA. Non è una Decision figlia naturale del progetto/tool ThreatForge. |
| `MR-0001 / ADR-0002` | Vocabolario governato come fonte unica del linguaggio condiviso | **RELOCATE - DDTA/cross-document candidate** | Scelta reale (significati governati vs convenzioni locali), ma l'owner è DDTA/cross-document governance. Resta aperto se il controlled vocabulary sia universale, opzionale o profile-specific. |
| `MR-0001 / ADR-0003` | Supporto ThreatForge alla tracciabilità della realizzazione governata | **REWRITE + REPARENT candidate** | Tolto l'uso improprio di R-CLOSED-04, il tema può contenere una vera scelta ThreatForge; la rewrite corrente però dichiara soprattutto supporto senza scegliere abbastanza. Il concern è più naturale sotto MR-0002. |
| `MR-0001 / ADR-0004` | Risoluzione contestuale dei valori controllati da fonti governate | **FITS** | Scelta ThreatForge autonoma: risolvere i valori nel contesto posseduto dalle fonti governate invece di codificare enum/global interpretations nei consumer. L3 non prescrive semanticamente questa scelta. |
| `MR-0001 / ADR-0006` | Handoff governato per la continuità dello sviluppo ThreatForge | **FITS - parent unresolved** | Scelta reale fra continuità informale e handoff governato ricostruibile. È una ThreatForge project-operation; il parent MR corrente non va forzato e deve essere riesaminato. |
| `MR-0001 / ADR-0007` | Contratti eseguibili dei modelli documentali consumati da ThreatForge | **FITS** | Scelta architetturale reale: consumer che ricodificano separatamente struttura/regole vs una proiezione/contratto eseguibile comune. R-CLOSED-04 è L3 e non rende questa ADR semanticamente ridondante. |
| `MR-0001 / ADR-0008` | Rappresentazione Doc-as-Code canonica dei riferimenti governati | **RELOCATE - L2 representation candidate** | La grammatica [id] title è una scelta reale di rappresentazione, non una Decision del tool. Va rivalutata nella futura fase identity/reference/mapping. |
| `MR-0001 / ADR-0009` | Supporto ThreatForge a obblighi di sicurezza governati derivati dall'analisi | **NOT STANDALONE DECISION candidate** | Non viene eliminata da L3, ma H-CLOSED-02 resta decisivo: nella rewrite corrente supportare Security tramite contratti sembra coverage/conformance di ADR-0007 + ADR-0010, non una nuova scelta autonoma. |
| `MR-0001 / ADR-0010` | Consumer ThreatForge estensibili dall'inventario governato dei modelli | **FITS** | Scelta autonoma: inventario/dispatch derivato da catalogo/proiezione governata vs liste locali, cardinalità fisse o discovery indipendente. Distinta dal modo in cui i contratti sono consumati. |
| `MR-0002 / ADR-0001` | Separazione tra capacità ThreatForge, orchestrazione applicativa e adapter | **FITS - minor cleanup** | Scelta architetturale autonoma. La Decision deve possedere il confine capability/application/adapter senza anticipare quale adapter concreto venga scelto; VS Code resta ADR-0005. |
| `MR-0002 / ADR-0002` | Pubblicazione governata del repository ThreatForge | **FITS** | Scelta di project operation: Git manuale vs operazione governata con precondizioni. Il parent MR-0002 è naturale. |
| `MR-0002 / ADR-0003` | Supporto ThreatForge all'avvio governato della realizzazione | **FITS** | Scelta di prodotto: scaffold governato e collegato al contesto vs creazione tecnica scollegata. Stati/lifecycle formali restano downstream. |
| `MR-0002 / ADR-0004` | Authoring ThreatForge guidato dai contratti governati del modello | **FITS** | Scelta capability autonoma: sola validazione a posteriori vs assistenza proattiva derivata dai contratti durante authoring. ADR-0007 può fornire la fonte senza imporre questa capability. |
| `MR-0002 / ADR-0005` | VS Code task come adapter locale sottile di ThreatForge | **FITS** | Scelta concreta di prima integrazione: task sottili vs custom extension/altro adapter. Distinta dal confine architetturale generale di ADR-0001. |
| `MR-0002 / ADR-0006` | Core ThreatForge condiviso per assistenza Markdown contestuale | **FITS** | Scelta autonoma su dove vive l'analisi live: core editor-independent vs regole replicate negli editor. Distinta da authoring guidato e scelta dei task. |
| `MR-0002 / ADR-0007` | Architettura applicativa ThreatForge indipendente dai delivery adapter | **FITS** | Scelta architetturale più specifica di ADR-0001: application services + ports/adapters + composition boundary. Può cambiare indipendentemente dal macro-confine capability/app/adapter. |

\normalsize

## Cross-case findings

### F1 - Realization principles do not erase tool Decisions

`R-CLOSED-04` can motivate ThreatForge architecture but cannot be used as an L1 inheritance rule. In particular, choosing shared executable contracts rather than independently coded consumer rules remains a real ThreatForge Decision.

### F2 - Ownership-correct is not sufficient

A rewrite that merely says 'ThreatForge supports governed semantics without owning them' may still fail the Decision-contribution test. The corrected candidate must identify a genuine alternative in the behavior or architecture of ThreatForge.

### F3 - Re-parent after ownership correction

When a rewrite changes the semantic owner or narrows the problem, its parent relation must be re-evaluated. Historical parentage is evidence, not an immutable truth.

### F4 - Support/conformance is not automatically a Decision

Supporting one concrete model extension through already-chosen generic contracts may be L4 coverage rather than another Decision. MR-0001/ADR-0009 is the primary construction example.

### F5 - The construction corpus remains evidence, not migration

This checkpoint does not modify historical ThreatForge ADRs. It classifies revised candidates so that the next rewrite can test whether the Decision metamodel produces a smaller, ownership-correct and non-redundant set.

## Disposition summary

- Retain and rewrite/clean as ThreatForge Decisions: MR-0001/ADR-0003, ADR-0004, ADR-0007, ADR-0010 and MR-0002/ADR-0001..ADR-0007.
- Retain as a meaningful ThreatForge Decision but keep parent unresolved: MR-0001/ADR-0006 handoff.
- Relocate outside the ThreatForge Decision hierarchy: MR-0001/ADR-0001 Diátaxis, ADR-0002 vocabulary, ADR-0008 reference representation.
- Remove as standalone Decision candidate and use as L4 support/conformance case: MR-0001/ADR-0009 Security support.

## Next step

Write a corrected candidate corpus using `Context + Decision + Consequences` for actual Decisions, with study-only annotations for semantic owner, proposed parent and DDTA contract supported. These annotations are not new canonical fields of the Decision metamodel.
