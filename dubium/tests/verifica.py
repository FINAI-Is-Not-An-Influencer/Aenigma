"""EN: Verify Dubium with local RDFLib, OWL-RL and pySHACL.
LA: Dubium ope RDFLib, OWL-RL et pySHACL localiter proba.
"""

from pathlib import Path

from owlrl import DeductiveClosure, OWLRL_Semantics
from pyshacl import validate
from rdflib import Graph, Literal, Namespace, OWL, RDF, RDFS, URIRef

DUB = Namespace("https://aenigma.criptasemantica.it/dubium#")
ROOT = Path(__file__).resolve().parents[1]


def load_data():
    return Graph().parse(ROOT / "dubium.ttl", format="turtle")


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check_question(data, item, concept):
    query = """
        ASK { ?item a dub:Question ; dub:concerns ?concept .
              FILTER NOT EXISTS { ?item dub:formula ?formula } }
    """
    return bool(data.query(query, initNs={"dub": DUB}, initBindings={"item": item, "concept": concept}))


def relation(data, position, subject, kind, obj):
    query = """
        ASK {
            ?arc a dub:RelationAssertion ; dub:belongsTo ?position ;
                 dub:subjectConcept ?subject ; dub:relationKind ?kind ; dub:objectConcept ?obj .
            ?position dub:derivedFrom/dub:partOfSource ?source .
        }
    """
    bindings = {"position": position, "subject": subject, "kind": DUB["rel-" + kind], "obj": obj}
    return bool(data.query(query, initNs={"dub": DUB}, initBindings=bindings))


def check_content(data):
    # EN: Stable IRIs and the distinction between source and context are part of the public contract.
    # LA: IRI stabilia et distinctio fontis a contextu ad conventionem publicam pertinent.
    ontology = URIRef(str(DUB))
    require(set(data.subjects(RDF.type, OWL.Ontology)) == {ontology}, "IRI di Dubium non preservato")
    require(not list(data.triples((None, OWL.imports, None))), "Importazione OWL imprevista")
    require(not list(data.triples((None, OWL.sameAs, None))), "Equivalenza di risorse introdotta")
    manifest = URIRef("https://criptasemantica.it/")
    passages = set(data.subjects(DUB.partOfSource, manifest))
    require(passages == {DUB[f"P{number}"] for number in range(9)}, "Passi del manifesto incompleti")
    positions = set(data.subjects(RDF.type, DUB.Position))
    for position in positions:
        source = data.value(data.value(position, DUB.derivedFrom), DUB.partOfSource)
        extension = data.value(position, DUB.status) == DUB.Estensione
        require(extension == (source != manifest), f"Fonte primaria o estensione confusa in {position}")
    covered = {data.value(p, DUB.derivedFrom) for p in positions}
    require(passages <= covered, "Un passo del manifesto è privo di una posizione")

    examples = [
        (DUB.F13, DUB.contenuto, "accessibileA", DUB.esserci),
        (DUB.F13, DUB.significato, "accessibileA", DUB.macchinaConcreta),
        (DUB.F17, DUB.ontologiaInformatica, "presuppone", DUB.ontologiaAnalitica),
        (DUB.F21, DUB.ontologiaAnalitica, "dipendeDa", DUB.ontologiaFenomenologica),
        (DUB.F22, DUB.ontologiaFenomenologica, "siArticolaIn", DUB.ontologiaFormale),
        (DUB.F22, DUB.ontologiaFenomenologica, "siArticolaIn", DUB.ontologiaRegionale),
        (DUB.F25, DUB.quantificazioneOntologica, "relativaA", DUB.ambitoOggettuale),
        (DUB.F26, DUB.ontologiaEnte, "studia", DUB.enteComeCosa),
        (DUB.F27, DUB.ontologiaEnte, "studia", DUB.essereDiEnte),
        (DUB.F28, DUB.ontologiaFondamentale, "studia", DUB.essereInQuantoTale),
        (DUB.F30, DUB.enteOntico, "haFiguraLimite", DUB.nulla),
        (DUB.F31, DUB.ontologiaEnte, "riceveSensoDa", DUB.ontologiaFondamentale),
        (DUB.F35, DUB.iperscritturaFondamentale, "produce", DUB.criptaIpertesto),
        (DUB.X03, DUB.ontologiaInformatica, "sostieneOnticamente", DUB.ricercaFondamentale),
    ]
    # EN: Confirm the qualified path exists and the flattened triple is absent.
    # LA: Viam qualificatam adesse et triplum simplicatum abesse confirma.
    for position, subject, kind, obj in examples:
        require(relation(data, position, subject, kind, obj), f"Raccordo mancante in {position}")
        require((subject, DUB["rel-" + kind], obj) not in data, f"Tesi asserita direttamente in {position}")

    for item, concept in [(DUB.Q01, DUB.essenteEspressione), (DUB.Q04, DUB.nulla), (DUB.Q06, DUB.sensoEssere)]:
        require(check_question(data, item, concept), f"Domanda o distinzione mancante in {item}")
    require(set(data.objects(DUB.nulla, RDF.type)) == {DUB.Concept}, "Il nulla va indicizzato come riferimento")
    counts = {name: len(set(data.subjects(RDF.type, DUB[name])))
              for name in ("Concept", "RelationKind", "Position", "RelationAssertion", "Question", "Passage")}
    print("OK copertura e 17 interrogazioni. " + ", ".join(f"{k}={v}" for k, v in counts.items()))


def check_shapes(data):
    shapes = Graph().parse(ROOT / "shapes.ttl", format="turtle")
    conforms, _, report = validate(data, shacl_graph=shapes, inference="none")
    require(conforms, report)
    print("OK SHACL sul modulo completo")

    # EN: Change one record at a time so each test exercises the relevant constraint.
    # LA: Singulas schedulas muta, ut quaeque probatio regulam ad rem pertinentem exploret.
    bad_cases = [
        ("fonte assente", (DUB.F01, DUB.derivedFrom, None), None),
        ("formula assente", (DUB.F30, DUB.formula, None), None),
        ("statuto non ammesso", (DUB.F31, DUB.status, None), (DUB.F31, DUB.status, DUB.Fondamentale)),
        ("arco senza posizione", (DUB["F13-r01"], DUB.belongsTo, None), None),
        ("oggetto non concettuale", (DUB["F30-r02"], DUB.objectConcept, None), (DUB["F30-r02"], DUB.objectConcept, DUB.P7)),
        ("domanda con tesi implicita", None, (DUB.Q06, DUB.formula, Literal("Risposta"))),
        ("arco senza tipo", (DUB["F30-r02"], RDF.type, DUB.RelationAssertion), None),
        ("formula su una glossa", None, (DUB.nulla, DUB.formula, Literal("Formula spuria"))),
        ("scheda di ricerca senza tipo", (DUB.Q06, RDF.type, DUB.Question), None),
        ("etichetta non letterale", None, (DUB.nulla, RDFS.label, DUB.essere)),
    ]
    for name, removal, addition in bad_cases:
        mutant = load_data()
        if removal:
            mutant.remove(removal)
        if addition:
            mutant.add(addition)
        require(not validate(mutant, shacl_graph=shapes, inference="none")[0], f"SHACL ha accettato: {name}")
    print(f"OK {len(bad_cases)} mutazioni SHACL respinte")


def check_inference(data):
    arc = DUB["F30-r02"]
    triple = (DUB.F30, DUB.hasAssertion, arc)
    require(triple not in data, "Il test dell'inversa richiede una tripla da inferire")
    # EN: Materialise only structural consequences through the supported OWL RL rules.
    # LA: Sola consectaria structurae per regulas OWL RL manifestentur.
    DeductiveClosure(OWLRL_Semantics).expand(data)
    require(triple in data, "Inferenza OWL inversa mancante")
    require((DUB.F30, RDF.type, DUB.ResearchItem) in data, "Inferenza di sottoclasse mancante")
    require((DUB.enteOntico, DUB["rel-haFiguraLimite"], DUB.nulla) not in data, "Inferenza filosofica indesiderata")
    require((DUB.nulla, RDF.type, DUB.Position) not in data, "Una glossa è stata inferita come tesi")
    print("OK inferenze OWL RL sull'inversa e sulla sottoclasse")


def main():
    data = load_data()
    check_content(data)
    check_shapes(data)
    check_inference(data)


if __name__ == "__main__":
    main()
