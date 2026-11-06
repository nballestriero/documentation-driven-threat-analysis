"""Read-only inventory of DDTA MR Turtle declarations for Graph L3 review.

Run from the workspace root:
    python experiments/graph-l3-general/audit_mr_sources.py
    python experiments/graph-l3-general/audit_mr_sources.py --json

This is not a semantic completeness checker. It performs the Core validator's
available structural checks and describes what source RDF actually declares.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rdflib import RDF, Graph, Namespace  # noqa: E402
from rdflib.term import URIRef  # noqa: E402
from tools.graph_pipeline.compose import compose, load_schema, validate  # noqa: E402

DDTA = Namespace("https://w3id.org/ddta/core#")
DOC_IDS = ("MR-01", "MR-02", "MR-03", "MR-04", "MR-C6", "MR-C7")
PROPS = (
    "hasPrimaryFunction", "providesFunction", "hasOperationalEnvironment",
    "hasPart", "hasInput", "hasOutput", "hasMode", "modeHasInput",
    "guaranteesOutput", "requiresPresent", "requiresAbsent", "constrainedBy",
    "specifiesInformation", "minOccurs", "maxOccurs", "prepares", "verifies",
    "adapts", "concernsEntity", "gapSource", "gapPredicate", "gapTarget",
)


def short(value) -> str:
    text = str(value)
    if text.startswith(str(DDTA)):
        return "ddta:" + text.rsplit("#", 1)[-1]
    if "#" in text:
        return text.rsplit("#", 1)[-1]
    if "/" in text and isinstance(value, URIRef):
        return text.rsplit("/", 1)[-1]
    return text


def summarize(g: Graph) -> dict:
    types = sorted((short(s), short(o)) for s, o in g.subject_objects(RDF.type))
    props = {}
    for p in PROPS:
        edges = sorted((short(s), short(o)) for s, o in g.subject_objects(DDTA[p]))
        if edges:
            props[p] = edges
    return {"triple_count": len(g), "types": types, "properties": props}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mr-dir", type=Path, default=ROOT / "dermatriage" / "mr")
    parser.add_argument("--schema", type=Path, default=ROOT / "ontology" / "core.ttl")
    parser.add_argument("--json", action="store_true", help="Print stable JSON inventory")
    parser.add_argument("--baseline", type=Path, help="Compare source hashes with a previous inventory JSON")
    args = parser.parse_args(argv)
    try:
        files = [args.mr_dir / (doc_id + ".md") for doc_id in DOC_IDS]
        missing = [p for p in files if not p.is_file()]
        if missing:
            raise FileNotFoundError("Missing MR documents: " + ", ".join(map(str, missing)))
        merged = compose(files)
        validate(merged, load_schema(args.schema))
        rows = []
        for doc_id, path in zip(DOC_IDS, files):
            source = path.read_bytes()
            parsed = compose([path])
            rows.append({
                "id": doc_id,
                "source": path.name,
                "sha256": hashlib.sha256(source).hexdigest().upper(),
                **summarize(parsed),
            })
        report = {
            "validation": "PASS",
            "document_count": len(rows),
            "unique_merged_triples": len(merged),
            "documents": rows,
            "untyped_composition_targets": sorted({short(o) for _, o in merged.subject_objects(DDTA.hasPart)
                                                   if (o, RDF.type, None) not in merged}),
        }
        if args.baseline:
            baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
            expected = {row["id"]: row["sha256"] for row in baseline["documents"]}
            report["baseline_comparison"] = {
                row["id"]: ("MATCH" if expected.get(row["id"]) == row["sha256"] else "DIFFERENT")
                for row in rows
            }
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
        else:
            print(f"MR Graph L3 source audit: {len(rows)} documents, {len(merged)} unique triples, Core validation PASS")
            for row in rows:
                print(f"  {row['id']}: {row['triple_count']} triples; SHA256={row['sha256']}")
                for pred, edges in row['properties'].items():
                    print(f"    {pred}: " + "; ".join(f"{a} -> {b}" for a, b in edges))
            if args.baseline:
                print("  Baseline comparison: " + ", ".join(
                    f"{doc_id}={status}" for doc_id, status in report["baseline_comparison"].items()))
            print("  Untyped hasPart targets (merged MR RDF): "
                  + (", ".join(report['untyped_composition_targets']) or "none"))
            print("NOTE: Structural validation is not a test of semantic completeness or DDTA approval.")
        return 0
    except Exception as exc:
        print(f"MR L3 AUDIT ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
