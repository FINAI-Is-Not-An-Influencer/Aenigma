#!/usr/bin/env python3
"""EN: Verify the whole Aenigma network: parsing, headers, cross-references, SHACL, mutations and OWL RL consistency.
LA: Totum rete Aenigmatis proba: lectionem, capita, relationes mutuas, SHACL, mutationes et constantiam OWL RL.

EN: Run from the repository root with RDFLib, pySHACL and OWL-RL available. Dubium keeps its own
    test in dubium/tests/verifica.py; this program adds the checks that span modules.
LA: A radice repositorii exsequere, RDFLib, pySHACL et OWL-RL praesentibus. Dubium probationem
    propriam in dubium/tests/verifica.py servat; hoc programma probationes inter partes addit.
"""

from pathlib import Path
import subprocess

from owlrl import DeductiveClosure, OWLRL_Semantics
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, OWL, RDF, RDFS, SKOS, URIRef
from rdflib.namespace import DCTERMS, XSD

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://aenigma.criptasemantica.it/"
MODULES = {
    "dubium": Namespace(SITE + "dubium#"),
    "trivium": Namespace(SITE + "trivium#"),
    "metrum": Namespace(SITE + "metrum#"),
}
AEN = Namespace(SITE + "aenigma#")
TRV, MTR, DUB = MODULES["trivium"], MODULES["metrum"], MODULES["dubium"]
WD = "http://www.wikidata.org/entity/"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def parse(path):
    # EN: Two independent parsers must agree that the file is Turtle.
    # LA: Duo interpretes independentes consentire debent tabulam esse Turtle.
    subprocess.run(["rapper", "-q", "-i", "turtle", "-c", str(path)], check=True)
    return Graph().parse(path, format="turtle")


def check_headers(graphs, root):
    for name, graph in graphs.items():
        ontology = URIRef(str(MODULES[name]))
        require(set(graph.subjects(RDF.type, OWL.Ontology)) == {ontology}, f"{name}: IRI dell'ontologia non univoco")
        for predicate in (OWL.versionIRI, OWL.versionInfo, DCTERMS.license, DCTERMS.issued, DCTERMS.modified):
            require(graph.value(ontology, predicate) is not None, f"{name}: manca {predicate}")
        for predicate in (RDFS.label, DCTERMS.title, RDFS.comment, DCTERMS.description):
            langs = {o.language for o in graph.objects(ontology, predicate) if isinstance(o, Literal)}
            require({"it", "en", "la"} <= langs, f"{name}: {predicate} non è in tre lingue")
        require(not list(graph.triples((None, OWL.imports, None))), f"{name}: un modulo non importa")
        require(not list(graph.triples((None, OWL.sameAs, None))), f"{name}: owl:sameAs non ammesso")
        require(not list(graph.triples((None, SKOS.exactMatch, None))), f"{name}: skos:exactMatch non ammesso")
        require((ontology, DCTERMS.isPartOf, URIRef(str(AEN))) in graph, f"{name}: non dichiara la radice")
    imports = set(root.objects(URIRef(str(AEN)), OWL.imports))
    expected = {URIRef(f"{SITE}{name}/{name}.ttl") for name in graphs}
    require(imports == expected, "La radice non importa esattamente i tre documenti pubblicati")
    for name in graphs:
        require((URIRef(str(MODULES[name])), RDF.type, AEN.Modulo) in root, f"{name}: assente dal registro della radice")
    print("OK intestazioni, versioni, licenze e registro della radice")


def check_references(graphs):
    # EN: Every IRI in a module namespace that is used as an object must be described in that module, except version IRIs.
    # LA: Quodque IRI in spatio partis ut obiectum adhibitum in ea parte describi debet, praeter IRI versionum.
    dangling = []
    for name, graph in graphs.items():
        for other, namespace in MODULES.items():
            for obj in set(graph.objects()):
                if isinstance(obj, URIRef) and str(obj).startswith(str(namespace)) and obj != URIRef(str(namespace)):
                    if "#v" in str(obj):
                        continue
                    if (obj, None, None) not in graphs[other]:
                        dangling.append(f"{name} -> {obj}")
    require(not dangling, "Riferimenti pendenti: " + ", ".join(dangling[:10]))
    bridges = len(list(graphs["trivium"].triples((None, SKOS.broadMatch, None))))
    links = len(list(graphs["trivium"].triples((None, SKOS.related, None))))
    print(f"OK riferimenti fra moduli: {bridges} ponti FORD e {links} legami con Dubium o interni risolti")


def check_trivium(graph):
    concepts = set(graph.subjects(RDF.type, TRV.Disciplina)) | set(graph.subjects(RDF.type, TRV.Genere)) \
        | set(graph.subjects(RDF.type, TRV.Programma)) | set(graph.subjects(RDF.type, TRV.Stanza))
    require(len(concepts) >= 211, "Trivium: concetti insufficienti")
    for concept in concepts:
        langs = {o.language for o in graph.objects(concept, SKOS.prefLabel)}
        require(langs == {"it", "en", "la"}, f"Trivium: etichette incomplete in {concept}")
        for match in graph.objects(concept, SKOS.closeMatch):
            require(str(match).startswith(WD), f"Trivium: corrispondenza non Wikidata in {concept}")

    def cycle(node, seen):
        return any(parent in seen or cycle(parent, seen | {parent}) for parent in graph.objects(node, SKOS.broader))
    require(not any(cycle(c, {c}) for c in concepts), "Trivium: ciclo nella gerarchia")
    for collection in (TRV.trivio, TRV.quadrivio):
        require(len(set(graph.objects(collection, SKOS.member))) >= 3, "Trivium: collezione incompleta")
    print(f"OK Trivium: {len(concepts)} concetti in tre lingue, gerarchia senza cicli, corrispondenze solo Wikidata")


def check_metrum(graph, examples):
    protocols = set(graph.subjects(RDF.type, MTR.Protocol))
    fields = set(graph.subjects(RDF.type, MTR.Discipline))
    principles = set(graph.subjects(RDF.type, MTR.Principle))
    require(len(protocols) == 58 and len(fields) == 48 and len(principles) >= 30, "Metrum: conteggi inattesi")
    for protocol in protocols:
        require(graph.value(protocol, MTR.family) is not None and graph.value(protocol, DCTERMS.source) is not None, f"Metrum: protocollo incompleto {protocol}")
    for field in fields:
        notation = str(graph.value(field, SKOS.notation))
        if "." in notation:
            require((field, SKOS.broader, MTR[f"ford-{notation.split('.')[0]}"]) in graph, f"Metrum: {notation} senza campo padre")
    cautioned = set(graph.objects(MTR["principle-dora"], MTR.cautions))
    require(MTR["p-jif"] in cautioned, "Metrum: DORA deve mettere in guardia sul JIF")
    for principle in principles:
        require(graph.value(principle, DCTERMS.source) is not None, f"Metrum: principio senza fonte {principle}")
    query = """
        ASK { ?o a mtr:Observation ; mtr:protocol mtr:p-citazioni ; mtr:state mtr:state-observed ; mtr:value ?v ;
              mtr:discipline mtr:ford-6-3 ; mtr:evidence ?e . FILTER ( ?v > 10 ) }
    """
    require(bool(examples.query(query, initNs={"mtr": MTR})), "Metrum: l'interrogazione d'esempio non trova l'osservazione")
    print(f"OK Metrum: {len(protocols)} protocolli, {len(fields)} campi FORD, {len(principles)} principi, esempi interrogabili")


def check_shapes(graphs, examples):
    union = Graph()
    for graph in graphs.values():
        union += graph
    union += examples
    for name in ("trivium", "metrum"):
        shapes = Graph().parse(ROOT / name / "shapes.ttl", format="turtle")
        conforms, _, report = validate(union, shacl_graph=shapes, inference="none", advanced=True)
        require(conforms, f"{name}: SHACL respinge il grafo\n{report}")
    print("OK SHACL su Trivium, Metrum ed esempi")

    # EN: Each mutation removes or adds one triple; the shapes must reject it.
    # LA: Quaeque mutatio unum triplum tollit vel addit; regulae id recusare debent.
    EX = Namespace(SITE + "metrum/esempi#")
    cases = [
        ("trivium", "etichetta latina assente", (TRV.dialettica, SKOS.prefLabel, Literal("Dialectica", lang="la")), None),
        ("trivium", "corrispondenza non Wikidata", None, (TRV.dialettica, SKOS.closeMatch, URIRef("https://example.org/dialettica"))),
        ("trivium", "equivalenza vietata", None, (TRV.dialettica, SKOS.exactMatch, URIRef(WD + "Q9453"))),
        ("trivium", "concetto senza schema", (TRV.ecologia, SKOS.inScheme, TRV.discipline), None),
        ("trivium", "padre in un altro schema", None, (TRV.cronaca, SKOS.broader, TRV.dialettica)),
        ("metrum", "osservazione senza protocollo", (EX["osservazione-1"], MTR.protocol, MTR["p-citazioni"]), None),
        ("metrum", "valore su un dato assente", None, (EX["osservazione-3"], MTR.value, Literal(3))),
        ("metrum", "copertura parziale senza lettura", (EX["osservazione-3"], MTR.editorialReading, None), None),
        ("metrum", "periodo rovesciato", (EX["osservazione-1"], MTR.periodEnd, None), (EX["osservazione-1"], MTR.periodEnd, Literal("2023-01-01", datatype=XSD.date))),
        ("metrum", "confronto con protocolli diversi", (EX["osservazione-2"], MTR.protocol, MTR["p-citazioni"]), (EX["osservazione-2"], MTR.protocol, MTR["p-opere-citanti"])),
        ("metrum", "protocollo senza fonte", (MTR["p-fwci"], DCTERMS.source, None), None),
    ]
    for name, label, removal, addition in cases:
        mutant = Graph()
        mutant += union
        if removal:
            mutant.remove(removal)
        if addition:
            mutant.add(addition)
        shapes = Graph().parse(ROOT / name / "shapes.ttl", format="turtle")
        require(not validate(mutant, shacl_graph=shapes, inference="none", advanced=True)[0], f"SHACL ha accettato: {label}")
    print(f"OK {len(cases)} mutazioni SHACL respinte")


def check_inference(graphs, root, examples):
    union = Graph()
    for graph in list(graphs.values()) + [root, examples]:
        union += graph
    DeductiveClosure(OWLRL_Semantics).expand(union)
    require((DUB.nulla, RDF.type, SKOS.Concept) in union, "Dubium: l'allineamento SKOS non è inferito")
    require((TRV.dialettica, RDF.type, SKOS.Concept) in union, "Trivium: una disciplina deve essere un concetto SKOS")
    # EN: SKOS inverses are not inferred without the SKOS vocabulary; the explicit hierarchy must be present instead.
    # LA: Inversae SKOS sine lexico SKOS non inferuntur; hierarchia expressa adesse debet.
    require((TRV.epistemologia, SKOS.broader, TRV.dialettica) in union, "Trivium: gerarchia esplicita assente")
    require((DUB.F30, DUB.hasAssertion, DUB["F30-r02"]) in union, "Dubium: l'inversa hasAssertion non è inferita")
    require((MTR["p-citazioni"], RDF.type, SKOS.Concept) in union, "Metrum: un protocollo deve essere un concetto SKOS")
    require(not list(union.subjects(RDF.type, OWL.Nothing)), "Incoerenza: un individuo appartiene alla classe vuota")
    # EN: Check declared disjointness explicitly; the reasoner does not always raise it.
    # LA: Disiunctionem declaratam expresse proba; ratiocinator eam non semper tollit.
    for graph in graphs.values():
        for axiom in graph.subjects(RDF.type, OWL.AllDisjointClasses):
            members = list(graph.items(graph.value(axiom, OWL.members)))
            for i, first in enumerate(members):
                for second in members[i + 1:]:
                    shared = set(union.subjects(RDF.type, first)) & set(union.subjects(RDF.type, second))
                    require(not shared, f"Classi disgiunte con individui comuni: {first} {second} {list(shared)[:3]}")
    print("OK inferenze OWL RL: allineamenti, inversa di Dubium, nessuna classe disgiunta violata")


def main():
    graphs = {name: parse(ROOT / name / f"{name}.ttl") for name in MODULES}
    root = parse(ROOT / "aenigma.ttl")
    examples = parse(ROOT / "metrum" / "esempi.ttl")
    check_headers(graphs, root)
    check_references(graphs)
    check_trivium(graphs["trivium"])
    check_metrum(graphs["metrum"], examples)
    check_shapes(graphs, examples)
    check_inference(graphs, root, examples)
    print("OK rete Aenigma: " + ", ".join(f"{name}={len(graph)} triple" for name, graph in graphs.items()))


if __name__ == "__main__":
    main()
