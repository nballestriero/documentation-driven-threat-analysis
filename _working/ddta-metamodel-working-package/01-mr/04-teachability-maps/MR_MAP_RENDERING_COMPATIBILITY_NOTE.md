# MR Macro Project Map - rendering compatibility note

> Non-canonical implementation observation for later work.

## ThreatForge DFD rendering path inspected

Pinned ThreatForge planning baseline: `44f77796469465a6a076596b1b1ba1afdde92db7`.

Active files inspected:

- `tools/MR-0003/contracts/base-dfd-projection.contract.mjs`
- `tools/MR-0003/lib/base-dfd-projector.mjs`
- `tools/MR-0005/lib/dfd-html-renderer.mjs`
- `tools/MR-0005/materialize-base-dfd-html.mjs`

The active DFD implementation does **not** rely on Graphviz or Mermaid. It uses a custom Node/ESM pipeline:

`canonical BAE inventory -> renderer-neutral semantic DFD projection -> deterministic renderer layout -> self-contained HTML + embedded SVG`

The semantic DFD contract explicitly forbids renderer-owned fields such as coordinates, layout, color, fill, stroke, class, HTML and SVG. The renderer owns those concerns.

The HTML renderer also provides useful accessibility/teaching patterns:

- `role="img"`;
- SVG `<title>` and `<desc>`;
- visible identity/title labels;
- deterministic ordering/layout;
- traceability metadata and textual trace cards;
- a light monochrome visual language with meaning carried by labels rather than color alone.

## Reuse direction for MR maps

Future MR maps should reuse the **rendering method and visual system**, not DFD semantics.

Recommended shared architecture to evaluate later:

`MR set -> MR-map semantic projection -> shared diagram rendering shell/style/layout utilities -> HTML/SVG`

`BAE inventory -> DFD semantic projection -> shared diagram rendering shell/style/layout utilities -> HTML/SVG`

Possible shared pieces:

- page/panel shell;
- typography and spacing tokens;
- accessible SVG wrapper;
- label wrapping;
- deterministic layout utilities;
- arrow/edge-label rendering;
- traceability-card rendering;
- output materialization/check pattern.

Pieces that must remain separate:

- DFD node roles (`external_entity`, `process`, `data_store`);
- DFD flows and trust-boundary semantics;
- BAE-to-DFD projection rules;
- MR relation semantics and teachability rules.

## Current study artifacts

The HTML/SVG maps in this folder intentionally imitate the current DFD visual language (monochrome panels, rounded blocks, labeled arrows, identities, traceability and accessible text) while preserving distinct MR semantics. They are reference artifacts, not a production renderer implementation or a ThreatForge refactor.
