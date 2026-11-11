#!/usr/bin/env python3
"""EN: Fill the tables of the module guides from the graphs, so documentation and data cannot diverge.
LA: Tabulas ducum partium e graphis comple, ne documenta et data inter se discrepent.

EN: Each FORMALIZZAZIONE file may contain markers such as <!-- table:principles --> ... <!-- /table -->.
    The content between the markers is regenerated; the rest of the file is left untouched.
LA: Quaeque tabula FORMALIZZAZIONE signa continere potest velut <!-- table:principles --> ... <!-- /table -->.
    Materia inter signa regeneratur; cetera tabulae intacta manent.
"""

import re
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF, RDFS, SKOS
from rdflib.namespace import DCTERMS

REPO = Path(__file__).resolve().parents[1]
SITE = "https://aenigma.criptasemantica.it/"
TRV, MTR, DUB = Namespace(SITE + "trivium#"), Namespace(SITE + "metrum#"), Namespace(SITE + "dubium#")
WD = "http://www.wikidata.org/entity/"
HEAD = {
    "it": {"concept": "Concetto", "item": "Elemento Wikidata", "field": "Campo FORD", "dubium": "Concetto di Dubium", "key": "Chiave",
           "family": "Famiglia", "scope": "Ambito", "unit": "Unità", "source": "Fonte", "principle": "Principio", "cautions": "Mette in guardia su", "count": "Protocolli"},
    "en": {"concept": "Concept", "item": "Wikidata item", "field": "FORD field", "dubium": "Dubium concept", "key": "Key",
           "family": "Family", "scope": "Scope", "unit": "Unit", "source": "Source", "principle": "Principle", "cautions": "Cautions against", "count": "Protocols"},
    "la": {"concept": "Notio", "item": "Res Wikidata", "field": "Campus FORD", "dubium": "Notio Dubii", "key": "Clavis",
           "family": "Familia", "scope": "Ambitus", "unit": "Unitas", "source": "Fons", "principle": "Principium", "cautions": "Cavet de", "count": "Protocolla"},
}


def label(graph, node, lang):
    for predicate in (SKOS.prefLabel, RDFS.label):
        for value in graph.objects(node, predicate):
            if isinstance(value, Literal) and value.language == lang:
                return str(value)
    return str(node).split("#")[-1]


def name(node):
    # EN: Local names follow the hash; Wikidata items follow the last slash.
    # LA: Nomina localia post signum #; res Wikidata post ultimam virgulam.
    return str(node).split("#")[-1] if "#" in str(node) else str(node).rstrip("/").rsplit("/", 1)[-1]


def table(rows, header):
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    lines += ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join(lines)


def trivium_tables(lang):
    g = Graph().parse(REPO / "trivium" / "trivium.ttl", format="turtle")
    m = Graph().parse(REPO / "metrum" / "metrum.ttl", format="turtle")
    d = Graph().parse(REPO / "dubium" / "dubium.ttl", format="turtle")
    h = HEAD[lang]
    wikidata = sorted((label(g, s, lang), name(s), f"[{name(o)}](https://www.wikidata.org/wiki/{name(o)})") for s, o in g.subject_objects(SKOS.closeMatch) if str(o).startswith(WD))
    ford = sorted((label(g, s, lang), name(s), f"{m.value(o, SKOS.notation)} · {label(m, o, lang)}") for s, o in g.subject_objects(SKOS.broadMatch))
    dubium = sorted((label(g, s, lang), name(s), f"`dub:{name(o)}` · {label(d, o, lang)}") for s, o in g.subject_objects(SKOS.related) if str(o).startswith(str(DUB)))
    return {
        "wikidata": table([(a, f"`trv:{b}`", c) for a, b, c in wikidata], (h["concept"], "IRI", h["item"])),
        "ford": table([(a, f"`trv:{b}`", c) for a, b, c in ford], (h["concept"], "IRI", h["field"])),
        "dubium": table([(a, f"`trv:{b}`", c) for a, b, c in dubium], (h["concept"], "IRI", h["dubium"])),
    }


def metrum_tables(lang):
    g = Graph().parse(REPO / "metrum" / "metrum.ttl", format="turtle")
    h = HEAD[lang]
    protocols = []
    for p in sorted(g.subjects(RDF.type, MTR.Protocol), key=lambda n: str(g.value(n, SKOS.notation))):
        unit = next((str(u) for u in g.objects(p, MTR.unit) if u.language == lang), "")
        scopes = ", ".join(sorted(label(g, s, lang) for s in g.objects(p, MTR.scope)))
        protocols.append((f"`{g.value(p, SKOS.notation)}`", label(g, p, lang), label(g, g.value(p, MTR.family), lang), scopes, unit))
    families = []
    for f in sorted(g.subjects(RDF.type, MTR.Family), key=lambda n: str(g.value(n, SKOS.notation))):
        count = len(list(g.subjects(MTR.family, f)))
        definition = next((str(v) for v in g.objects(f, SKOS.definition) if v.language == lang), "")
        families.append((f"`{g.value(f, SKOS.notation)}`", label(g, f, lang), str(count), definition))
    principles = []
    for p in sorted(g.subjects(RDF.type, MTR.Principle), key=lambda n: str(g.value(n, SKOS.notation))):
        cautions = ", ".join(sorted(f"`{g.value(c, SKOS.notation)}`" for c in g.objects(p, MTR.cautions))) or "—"
        principles.append((str(g.value(p, SKOS.notation)), label(g, p, lang), f"[{h['source']}]({g.value(p, DCTERMS.source)})", cautions))
    return {
        "protocols": table(protocols, (h["key"], h["concept"], h["family"], h["scope"], h["unit"])),
        "families": table(families, (h["key"], h["family"], h["count"], "")),
        "principles": table(principles, (h["key"], h["principle"], h["source"], h["cautions"])),
    }


def fill(path, tables):
    text = path.read_text(encoding="utf-8")

    def replace(match):
        key = match.group(1)
        return f"<!-- table:{key} -->\n{tables[key]}\n<!-- /table -->"

    new = re.sub(r"<!-- table:([a-z]+) -->.*?<!-- /table -->", replace, text, flags=re.S)
    if new != text:
        path.write_text(new, encoding="utf-8")
        print("tabelle aggiornate:", path.relative_to(REPO))


def main():
    for lang in ("it", "en", "la"):
        suffix = "" if lang == "it" else f".{lang}"
        fill(REPO / "trivium" / f"FORMALIZZAZIONE{suffix}.md", trivium_tables(lang))
        fill(REPO / "metrum" / f"FORMALIZZAZIONE{suffix}.md", metrum_tables(lang))


if __name__ == "__main__":
    main()
