# Dubium. A guide for first-time readers

[Italiano](README.md) · [Latine](README.la.md)

Dubium takes its name from the doubt at the opening of the [Cripta Semantica manifesto](https://criptasemantica.it/). In Plato's *Sophist*, the speaker once thought they knew what “being” meant. The dialogue unsettles that confidence. It raises a question of method. How do we connect the things we study, the sense in which we say they are, and the wider question of being?

**Philosophical ontology** investigates being and what is. A **web ontology** gives people and software shared names and rules for describing a domain. Dubium is a web ontology that makes a text of philosophical ontology explorable. Return to the source when assessing a reading.

## Your first visit

1. Open the [Dubium catalogue](en/index.html) and look for **being of an entity**. Its entry gives a definition and links to positions in which it occurs.
2. Follow [F27](en/term/F27.html). Here the manifesto treats being in relation to an entity. The entry shows the formula, the mode of reading and the relations that help you navigate it.
3. Open [P7](en/term/P7.html) to find the paragraph, then [F28](en/term/F28.html), where the inquiry takes up being as such. [Question Q04](en/term/Q04.html) keeps the difficulty raised by that distinction open.

You can also start with [semantic capital](en/term/capitaleSemantico.html). This route goes from content a reader can understand to meanings organised for a machine to process.

You can also browse the [class hierarchy and property table](en/schema.html). Each entry opens a [reference page](en/term/F27.html) with relevant links and, where available, a Turtle example from the graph.

## Read an entry

A **concept** is a reference with a name, a gloss and a stable identifier. A **position** is a thesis, a reading or a contextual link attributed to a passage. A **qualified relation** connects two concepts within that position. A **question** identifies something that remains open.

The [OWL](https://www.w3.org/TR/owl2-syntax/) schema describes the graph's categories and properties. For instance, going from a position to its relations reverses the link from each relation back to the position. [SHACL](https://www.w3.org/TR/shacl/) constraints check that entries are complete, such as whether a position has a source. The philosophical formulas are readable text. The [formalisation](FORMALIZZAZIONE.en.md) explains their notation.

## Identifiers and prefixes

An **IRI** is the full name of a resource. `dub:essereDiEnte` abbreviates `https://aenigma.criptasemantica.it/dubium#essereDiEnte`. That address leads to the Italian catalogue and the term's anchor. The English and Latin editions use the same graph.

| Where | Prefix | Base IRI |
| --- | --- | --- |
| Dubium, in these guides | `dub:` | `https://aenigma.criptasemantica.it/dubium#` |
| Cripta editorial RDFa previews | `cs:` | `https://aenigma.criptasemantica.it/dubium#` |
| Cripta Semantic Service | `cs:` | `https://criptasemantica.it/ns/semantic-service#` |

A prefix is local to the document that declares it. Under the second declaration, `cs:essereDiEnte` identifies the same resource as `dub:essereDiEnte`. To use both vocabularies in one document, declare `dub:` for Dubium and `cs:` for the service. Compare expanded IRIs when joining data. The service still uses its own list of accepted references. Offering an individual entry through that list requires an explicit update to the service.

## From the file to your first query

[Turtle](https://www.w3.org/TR/turtle/) is a text format for saving an RDF graph. An RDF statement connects a subject, a property and a value. Open [dubium.ttl](dubium.ttl) in a text editor or read it with RDFLib. With Python and RDFLib available, run this example from the repository root.

```python
from rdflib import Graph

graph = Graph().parse("dubium/dubium.ttl", format="turtle")
query = """
PREFIX dub: <https://aenigma.criptasemantica.it/dubium#>
SELECT ?passage ?source WHERE {
  dub:F27 dub:derivedFrom ?passage .
  ?passage dub:partOfSource ?source .
}
"""
for passage, source in graph.query(query):
    print(passage, source)
```

You get P7's IRI and the manifesto's address. In an application, load Turtle from a reviewed copy, use full IRIs as keys and keep the source when displaying a position. Use [shapes.ttl](shapes.ttl) to check a new graph's structure. If you add a competing reading, give it a separate position with its own identifier and provenance.

## Build and check the site

The site uses static files. Building them requires Python 3 with RDFLib, Pandoc, OpenSSL and the Clean CSS CLI (`cleancss`). The graph checks also need pySHACL and OWL-RL. Run from the repository root.

```bash
bash minify.sh
python3 tools/build_site.py
python3 dubium/tests/verifica.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Preview the English catalogue at `http://127.0.0.1:8000/dubium/en/`. The builder reads the local Turtle and guides. Italian glosses are identified where a translation is unavailable. You can browse the catalogue with JavaScript disabled. When enabled, the filter runs in the browser. The [query in the formalisation](FORMALIZZAZIONE.en.md#example-query) shows how to retrieve a relation with its supporting passage.

## What changes in version 0.2.0

Dubium is now the first module of a network, next to [Trivium](../trivium/README.en.md) and [Metrum](../metrum/README.en.md), imported by the [Aenigma root](../aenigma.ttl). No identifier changed and the prior version (`dub:v0.1.0-draft`) remains citable. What is new is metadata and alignment: the header declares title, description, CC BY 4.0 licence, authors, publisher and dates; concepts are also `skos:Concept`, gathered in the `dub:concetti` scheme with preferred labels, so SKOS tools can browse them; positions, questions, passages and assertions are `prov:Entity` and `derivedFrom` is a subproperty of `prov:wasDerivedFrom`, so provenance can be read with PROV-O too; sources are `schema:CreativeWork`. The graph is also available as [JSON-LD](dubium.jsonld) and [RDF/XML](dubium.rdf), with a [context](context.jsonld) for developers. The [network test](../tests/verifica.py) complements the module test.
