# Trivium. A beginner's guide

[Italiano](README.md) · [Latine](README.la.md) · [Formalisation and method](FORMALIZZAZIONE.en.md)

Trivium is the second module of [Aenigma](../README.en.md). It gives a stable name, in three languages, to the **arts and disciplines** by which the site of the [Cripta Semantica](https://criptasemantica.it/) orders its articles, to its **editorial sections**, to its **programme lines** and to the allegorical **rooms** the visitor walks through. The source is the public taxonomy of the site: two hundred and two categories, with the descriptions written by the author where they exist.

If you have never used a controlled vocabulary, think of Trivium as an annotated index: every entry has an address that does not change, a name in Italian, English and Latin, a place in the hierarchy and, where it could be verified, a reference to Wikidata and to the matching field of research in the FORD classification used by [Metrum](../metrum/README.en.md).

## Why Trivium

The three founding categories of the site are Grammar, Dialectic and Rhetoric: the trivium of the liberal arts, the arts of discourse. Next to them the site keeps Mathematics, Music, Astronomy and Geography, a quadrivium in which geography, "mapping and measurement of the sublunar cosmos", takes the place of geometry. The module keeps this architecture in two collections, [Trivium](en/term/trivio.html) and [Quadrivium](en/term/quadrivio.html), and hangs all the other disciplines from them. The medieval order of knowledge becomes a navigable map of the editorial work.

## A first visit

1. Open the [Trivium catalogue](en/index.html) and search for **Dialectic**. The entry shows the author's description, the branches that descend from it (epistemology, hermeneutics, history of philosophy and many more), the Wikidata correspondence and the FORD field "Philosophy, ethics and religion".
2. Open [Rhetoric](en/term/retorica.html). You will see that the site places economics, jurisprudence, sociology and culture under it: rhetoric as the "architecture of power", in the words of the description.
3. Move to the [rooms](en/index.html#rooms). The [Room of FINAI](en/term/stanza-di-finai.html) and the [Room of the Blue Rose](en/term/stanza-della-rosa-blu.html) belong to the two people who hyperwrite the Cripta.
4. Switch language with the links at the top: the same entry exists in Italian, English and Latin.

## How to read an entry

| Field | Meaning |
| --- | --- |
| Preferred label | The name in the three languages. Italian is the site's; English and Latin are editorial translations. |
| Notation | The category *slug* on the site, for example `dialettica`. |
| Category identifier | The number WordPress assigns to the category, useful for comparing site and module. |
| Source | The public page of the category. |
| Broader / narrower concepts | The hierarchy declared by the site. |
| Scope note | The author's description, in Italian, with a translation. |
| Close match (Wikidata) | A verified Wikidata item. It is `skos:closeMatch`, never an equivalence. |
| Reference FORD field | The field of research and development in which the discipline sits, according to Metrum. |
| Related concepts | A Dubium concept the module proposes as a reading, or another Trivium entry. |

Four schemes keep the functions apart: the **disciplines**, the **genres and sections** (news, reviews, authors, profiles, products, synergies, channels), the **programme lines** (digital communism, world-wide semantic web, hermeneutic search engine, philosophical programming, metaphysics of play, academic studies) and the **rooms**. The [hierarchy](en/schema.html) shows the four trees.

## Identifiers and prefixes

`trv:dialettica` abbreviates `https://aenigma.criptasemantica.it/trivium#dialettica`. The files and examples also use `wd:` for Wikidata, `mtr:` for the FORD fields of Metrum and `dub:` for the concepts of Dubium. Two categories of the site are both called "Logica": the top-level one is `trv:logica`; the one nested under Dialectic is `trv:logica-dialettica`, with the same suffix the site uses for "Antropologia".

## From the file to a first query

```python
from rdflib import Graph

graph = Graph().parse("trivium/trivium.ttl", format="turtle")
query = """
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?name ?wikidata WHERE {
  ?concept skos:broader trv:dialettica ; skos:prefLabel ?name .
  FILTER ( lang(?name) = "en" )
  OPTIONAL { ?concept skos:closeMatch ?wikidata }
} ORDER BY ?name
"""
for name, wikidata in graph.query(query):
    print(name, wikidata or "")
```

You obtain the disciplines the site places under Dialectic, with the Wikidata item where present. Change `trv:dialettica` to `trv:retorica` or `trv:grammatica` to walk the trivium.

## Using Trivium outside Aenigma

In an article of the site, or in the graph of the Cripta semantic service, a category can be declared as a subject by its IRI: `schema:about trv:dialettica` or `dcterms:subject trv:dialettica`. Whoever reads the graph finds name, hierarchy, Wikidata and FORD field without further tables. The semantic service links its own "Cripta topics" to Trivium with `skos:closeMatch`, not with an equivalence.

## Building and verifying

The file `trivium.ttl` is generated by [tools/trivium_from_taxonomy.py](../tools/trivium_from_taxonomy.py) from the snapshot `fonti/categorie-criptasemantica-2026-11-11.json`. Labels, translations, correspondences and bridges are written in the generator. From the repository root:

```bash
python3 tools/trivium_from_taxonomy.py
python3 tests/verifica.py
python3 tools/build_site.py
```

The [SHACL constraints](shapes.ttl) check that every concept has three labels, a scheme, a notation and a public source, that correspondences point only to Wikidata and that no concept has a parent in another scheme. The [verification program](../tests/verifica.py) also tries eleven deliberate alterations, which must be rejected.

## Contributing

A new category of the site enters Trivium with a new snapshot and with its English and Latin labels in the generator. A Wikidata correspondence is added only after verification and is always declared as `skos:closeMatch`. A FORD bridge requires that the discipline really falls within that field according to the Frascati Manual. A link to Dubium is a reading: it must be motivated in the [formalisation](FORMALIZZAZIONE.en.md).
