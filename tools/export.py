#!/usr/bin/env python3
"""EN: Export each module as JSON-LD and RDF/XML, write a JSON-LD context per module and the VoID description of the whole.
LA: Quamque partem ut JSON-LD et RDF/XML exporta, contextum JSON-LD cuique parti et descriptionem VoID totius scribe.

EN: Turtle stays the edited source. The exports are regenerated, never edited by hand.
LA: Turtle fons emendandus manet. Exportata regenerantur, numquam manu mutantur.
"""

import json
from pathlib import Path

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, XSD

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://aenigma.criptasemantica.it/"
MODULES = {
    "dubium": ("dub", "https://aenigma.criptasemantica.it/dubium#"),
    "trivium": ("trv", "https://aenigma.criptasemantica.it/trivium#"),
    "metrum": ("mtr", "https://aenigma.criptasemantica.it/metrum#"),
}
COMMON = {
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "prov": "http://www.w3.org/ns/prov#",
    "dcterms": "http://purl.org/dc/terms/",
    "schema": "https://schema.org/",
    "vann": "http://purl.org/vocab/vann/",
    "wd": "http://www.wikidata.org/entity/",
}
VOID = Namespace("http://rdfs.org/ns/void#")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
AEN = Namespace("https://aenigma.criptasemantica.it/aenigma#")


def context(prefix, namespace):
    # EN: A context is a reading aid for JSON-LD clients; it declares no new terms.
    # LA: Contextus auxilium legendi clientibus JSON-LD est; nullum vocabulum novum declarat.
    mapping = {"@version": 1.1, prefix: namespace}
    for code, (other, uri) in MODULES.items():
        mapping.setdefault(other, uri)
    mapping.update(COMMON)
    return {"@context": mapping}


def export_module(name):
    prefix, namespace = MODULES[name]
    folder = ROOT / name
    graph = Graph().parse(folder / f"{name}.ttl", format="turtle")
    for code, uri in {prefix: namespace, **COMMON}.items():
        graph.bind(code, uri, replace=True)
    (folder / f"{name}.jsonld").write_text(
        graph.serialize(format="json-ld", context=context(prefix, namespace)["@context"], indent=1), encoding="utf-8")
    (folder / f"{name}.rdf").write_text(graph.serialize(format="pretty-xml"), encoding="utf-8")
    (folder / "context.jsonld").write_text(json.dumps(context(prefix, namespace), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return graph


def export_void(graphs):
    # EN: Describe the published files so that aggregators can find every serialisation and its size.
    # LA: Tabulas publicatas describe, ut collectores quamque formam eiusque magnitudinem reperiant.
    void = Graph()
    for code, uri in {"void": str(VOID), "dcat": str(DCAT), "aen": str(AEN), **COMMON}.items():
        void.bind(code, uri, replace=True)
    dataset = AEN.dataset
    void.add((dataset, RDF.type, VOID.Dataset))
    void.add((dataset, RDF.type, DCAT.Dataset))
    void.add((dataset, DCTERMS.title, Literal("Aenigma. Ontologia della Cripta Semantica", lang="it")))
    void.add((dataset, DCTERMS.title, Literal("Aenigma. Ontology of the Cripta Semantica", lang="en")))
    void.add((dataset, DCTERMS.title, Literal("Aenigma. Ontologia Cryptae Semanticae", lang="la")))
    void.add((dataset, DCTERMS.license, URIRef("https://creativecommons.org/licenses/by/4.0/")))
    void.add((dataset, DCTERMS.publisher, URIRef("https://criptasemantica.it/")))
    void.add((dataset, VOID.uriSpace, Literal(SITE)))
    void.add((dataset, DCTERMS.modified, Literal("2026-11-11", datatype=XSD.date)))
    total = 0
    for name, graph in graphs.items():
        prefix, namespace = MODULES[name]
        subset = AEN[f"dataset-{name}"]
        void.add((dataset, VOID.subset, subset))
        void.add((subset, RDF.type, VOID.Dataset))
        void.add((subset, DCTERMS.title, Literal(name.capitalize())))
        void.add((subset, VOID.uriSpace, Literal(namespace)))
        void.add((subset, VOID.triples, Literal(len(graph), datatype=XSD.integer)))
        void.add((subset, VOID.vocabulary, URIRef(namespace)))
        total += len(graph)
        for extension, media in (("ttl", "text/turtle"), ("jsonld", "application/ld+json"), ("rdf", "application/rdf+xml")):
            url = URIRef(f"{SITE}{name}/{name}.{extension}")
            void.add((subset, VOID.dataDump, url))
            distribution = AEN[f"distribution-{name}-{extension}"]
            void.add((subset, DCAT.distribution, distribution))
            void.add((distribution, RDF.type, DCAT.Distribution))
            void.add((distribution, DCAT.downloadURL, url))
            void.add((distribution, DCAT.mediaType, Literal(media)))
    void.add((dataset, VOID.triples, Literal(total, datatype=XSD.integer)))
    (ROOT / "void.ttl").write_text(void.serialize(format="turtle"), encoding="utf-8")
    return total


def main():
    graphs = {name: export_module(name) for name in MODULES if (ROOT / name / f"{name}.ttl").is_file()}
    total = export_void(graphs)
    print("exported", ", ".join(f"{name}={len(graph)}" for name, graph in graphs.items()), f"total={total}")


if __name__ == "__main__":
    main()
