"""Valida il contratto YAML, gli IRI e le dipendenze fra moduli.

Le funzioni seguenti non generano RDF e non scrivono file. I riferimenti
incrociati devono risolversi nell’insieme delle schede selezionate.
"""

from collections import Counter
from typing import Any

from rdflib import URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD

from .config import OntologyConfig
from .errors import OntologySourceError, require
from .models import Record

def _nonblank(value: Any, where: str) -> str:
    """Restituisce un testo non vuoto, altrimenti segnala il campo errato."""
    require(isinstance(value, str) and bool(value.strip()), f"{where}: expected nonempty text")
    return value

def _fields(obj: dict[str, Any], keys: set[str], required: set[str], ctx: str) -> None:
    """Controlla campi ammessi e obbligatori di una mapping YAML."""
    require(isinstance(obj, dict), f"{ctx}: expected mapping")
    extra = set(obj) - keys
    absent = required - set(obj)
    require(not extra, f"{ctx}: unsupported fields: {sorted(extra)}")
    require(not absent, f"{ctx}: required fields missing: {sorted(absent)}")

def _texts(v: Any, context: str) -> dict[str, str]:
    """Valida label/definition bilingui (inglese e italiano)."""
    require(isinstance(v, dict) and set(v) == {"en", "it"},
             f"{context}: expected bilingual mapping with exactly en and it")
    return {lang: _nonblank(v[lang], f"{context}.{lang}") for lang in ("en", "it")}

def expand_iri(iri: Any, context: str, config: OntologyConfig) -> URIRef:
    """Espande un QName come ddta:System a un URIRef RDFLib."""
    value = _nonblank(iri, context)
    prefix, sep, local = value.partition(":")
    require(bool(sep) and bool(local) and prefix in config.prefixes,
             f"{context}: unknown or malformed QName {value!r}")
    require(not any(x.isspace() for x in local) and all(c not in local for c in '<>"{}|\\^`'),
             f"{context}: invalid QName {value!r}")
    return URIRef(config.prefixes[prefix] + local)

def _status(value: Any, ctx: str) -> None:
    """Accetta esclusivamente lo stato `approved` nei blocchi normativi."""
    require(value == "approved", f"{ctx}: status is {value!r}, expected approved")

def validate_records(records: list[Record], config: OntologyConfig) -> dict[str, int]:
    """Controlla tipi, duplicati, riferimenti e conta le dichiarazioni.

    Lavoro in due passaggi: registra tutte le definizioni e poi verifica le
    relazioni trasversali. Non genera file e non aggiunge stub mancanti.
    """
    # The QName namespace registry is resolved per execution, not globally.
    def resolve(iri: Any, context: str) -> URIRef:
        return expand_iri(iri, context, config)

    vocabulary: dict[str, str] = {}
    counts = Counter()

    def register(iri: Any, kind: str, context: str) -> None:
        """Registra un IRI, rifiutando definizioni duplicate tra moduli."""
        term = str(resolve(iri, f"{context}.iri"))
        require(term not in vocabulary,
                 f"{context}: duplicate IRI {iri!r} (first seen as {vocabulary.get(term)})")
        vocabulary[term] = kind
        counts[kind] += 1

    for rec in records:
        b = rec.body
        kind, ctx = b["record"], rec.context
        if kind == "class":
            _fields(b, {"record", "module", "iri", "status", "subClassOf", "label", "definition"},
                    {"record", "module", "iri", "status", "label", "definition"}, ctx)
            _status(b["status"], ctx)
            register(b["iri"], "class", ctx)
            _texts(b["label"], f"{ctx}.label")
            _texts(b["definition"], f"{ctx}.definition")
            if "subClassOf" in b:
                resolve(b["subClassOf"], f"{ctx}.subClassOf")
        elif kind in ("object-properties", "datatype-properties"):
            _fields(b, {"record", "module", "owner", "properties"},
                    {"record", "module", "owner", "properties"}, ctx)
            resolve(b["owner"], f"{ctx}.owner")
            props = b["properties"]
            require(isinstance(props, list) and bool(props), f"{ctx}: expected nonempty properties list")
            for i, p in enumerate(props, 1):
                pc = f"{ctx}.properties[{i}]"
                _fields(p, {"iri", "status", "subPropertyOf", "domain", "range", "label", "definition"},
                        {"iri", "status", "domain", "range", "label", "definition"}, pc)
                _status(p["status"], pc)
                register(p["iri"], "object-property" if kind == "object-properties" else "datatype-property", pc)
                _texts(p["label"], f"{pc}.label")
                _texts(p["definition"], f"{pc}.definition")
                for field in ("domain", "range"):
                    _check_expression(p[field], f"{pc}.{field}", config)
                if "subPropertyOf" in p:
                    resolve(p["subPropertyOf"], f"{pc}.subPropertyOf")
        elif kind == "named-individuals":
            _fields(b, {"record", "module", "status", "class", "individuals"},
                    {"record", "module", "status", "class", "individuals"}, ctx)
            _status(b["status"], ctx)
            resolve(b["class"], f"{ctx}.class")
            items = b["individuals"]
            require(isinstance(items, list) and bool(items), f"{ctx}: expected nonempty individuals")
            for i, p in enumerate(items, 1):
                pc = f"{ctx}.individuals[{i}]"
                _fields(p, {"iri", "label"}, {"iri", "label"}, pc)
                register(p["iri"], "individual", pc)
                _texts(p["label"], f"{pc}.label")

    # References must be either defined by one of the selected modules, or a
    # deliberately supported standard RDF/OWL/XSD term. Never create stubs.
    external_classes = {
        str(OWL.Thing), str(RDFS.Literal), str(RDF.Property), str(XSD.string),
        str(XSD.integer), str(XSD.nonNegativeInteger), str(XSD.positiveInteger), str(XSD.boolean),
    }

    def check_ref(value: str, expected: set[str], context: str) -> None:
        """Verifica che un QName esista e abbia una categoria corretta."""
        term = str(resolve(value, context))
        actual = vocabulary.get(term)
        require(actual in expected or (term in external_classes and "external" in expected),
                 f"{context}: unresolved or invalid reference {value!r} (type {actual!r})")

    def check_expr(value: Any, context: str) -> None:
        """Verifica il riferimento o ogni elemento di una unionOf."""
        if isinstance(value, dict):
            for i, item in enumerate(value["unionOf"], 1):
                check_ref(item, {"class", "external"}, f"{context}.unionOf[{i}]")
        else:
            check_ref(value, {"class", "external"}, context)

    for rec in records:
        b, ctx = rec.body, rec.context
        if b["record"] == "class" and "subClassOf" in b:
            check_ref(b["subClassOf"], {"class"}, f"{ctx}.subClassOf")
        elif b["record"] in ("object-properties", "datatype-properties"):
            check_ref(b["owner"], {"class"}, f"{ctx}.owner")
            for i, p in enumerate(b["properties"], 1):
                pc = f"{ctx}.properties[{i}]"
                check_expr(p["domain"], f"{pc}.domain")
                check_expr(p["range"], f"{pc}.range")
                if "subPropertyOf" in p:
                    check_ref(p["subPropertyOf"],
                              {"object-property" if b["record"] == "object-properties" else "datatype-property"},
                              f"{pc}.subPropertyOf")
        elif b["record"] == "named-individuals":
            check_ref(b["class"], {"class"}, f"{ctx}.class")

    return dict(sorted(counts.items()))

def _check_expression(value: Any, ctx: str, config: OntologyConfig) -> None:
    """Valida un tipo semplice oppure una unionOf con almeno due classi."""
    def resolve(value: Any, ctx: str) -> URIRef:
        return expand_iri(value, ctx, config)
    if isinstance(value, str):
        resolve(value, ctx)
    elif isinstance(value, dict):
        require(set(value) == {"unionOf"}, f"{ctx}: only unionOf expressions are supported")
        values = value["unionOf"]
        require(isinstance(values, list) and len(values) >= 2,
                 f"{ctx}: unionOf requires at least two class names")
        require(len(values) == len(set(values)), f"{ctx}: unionOf has repeated operands")
        for i, item in enumerate(values, 1):
            resolve(item, f"{ctx}.unionOf[{i}]")
    else:
        raise OntologySourceError(f"{ctx}: unsupported class expression {value!r}")
