# Aenigma

[Italiano](README.md) · [Latine](README.la.md) · [Reference site](https://aenigma.criptasemantica.it/) · [Documentation map](https://aenigma.criptasemantica.it/en/documentazione.html) · [Wiki](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN)

Aenigma is the web ontology of the [Cripta Semantica](https://criptasemantica.it/), the fundamental ontological hypertext. Since version 0.2.0 it is a **network of three modules**, each with its own namespace, version, three languages and constraints:

| Module | Prefix | What it names | Version |
| --- | --- | --- | --- |
| [Dubium](dubium/README.en.md) · the question | `dub:` | Concepts, positions, questions and passages of the philosophical manifesto, with the source of every claim | 0.2.0 |
| [Trivium](trivium/README.en.md) · the arts | `trv:` | The two hundred disciplines, genres, programme lines and rooms of the site, with Wikidata and the FORD fields | 0.1.0 |
| [Metrum](metrum/README.en.md) · the measure | `mtr:` | The qualified scientometric observation: protocols, families, scopes, coverages, FORD fields and principles of responsible assessment | 0.1.0 |

The [root `aenigma.ttl`](aenigma.ttl) imports the three modules and describes them; [`void.ttl`](void.ttl) lists their distributions. The name comes from the Greek enigma: a formulation that hides what it shows. The names of the ontology do not exhaust things; they keep the question of the sense of being open while making it consultable by people and programs.

## From philosophy to the graph

The Cripta manifesto starts from the perplexity of the *Sophist* about the word "being" and ties the question of being to the history of writing: with the abstract machine of 1936 hyperhistory begins and writing is quantified; hyperwriting produces hypertexts and the Web accumulates semantic capital by means of ontologies. Dubium formalises this text passage by passage. Trivium takes seriously the way the site orders knowledge: the trivium of the arts of discourse and a quadrivium in which geography replaces geometry. Metrum takes in the quantification of writing as an object of the ontology, with its provenance, instead of suffering it as a verdict. Together the three modules trace the path from the question to the names and from the names to the measure, and back. [Wiki chapter 14](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-14)

## A first visit

1. Open [entry F27](https://aenigma.criptasemantica.it/dubium/en/term/F27.html) of Dubium: a position of the manifesto, its supporting passage, the formula and the relations.
2. Open [Dialectic](https://aenigma.criptasemantica.it/trivium/en/term/dialettica.html) in Trivium: the author's description, the branches, the Wikidata correspondence and the FORD field.
3. Open [Incoming citations](https://aenigma.criptasemantica.it/metrum/en/term/p-citazioni.html) in Metrum: family, scope, unit, method and the principles that limit its use.
4. Switch language at the top: every page exists in Italian, English and Latin.

## What the repository contains

| Path | Content |
| --- | --- |
| `aenigma.ttl`, `void.ttl` | Root of the network and description of the distributions |
| `dubium/`, `trivium/`, `metrum/` | For each module: Turtle graph, JSON-LD, RDF/XML, JSON-LD context, SHACL constraints, guides and formalisations in three languages, site pages |
| `metrum/esempi.ttl`, `metrum/fonti/`, `trivium/fonti/` | Synthetic examples and snapshots of the public sources used by the generators |
| `tools/` | Module generators (`trivium_from_taxonomy.py`, `metrum_from_dictionary.py`), exporter (`export.py`), site generator (`build_site.py`), documentation tables (`doc_tables.py`), link checker (`check_site.py`) |
| `tests/verifica.py`, `dubium/tests/verifica.py` | Network test and Dubium test |
| `index.src.html`, `minify.sh`, `style.css`, `reference.css`, `search.js` | Homepage and visual frame of the site |
| `DOCUMENTAZIONE*.md`, `CHANGELOG.md` | Documentation map and changelog |

## Reusing the data

Each module loads on its own (`dubium/dubium.ttl`, `trivium/trivium.ttl`, `metrum/metrum.ttl`) or all together from the root. The preferred prefixes are `dub:`, `trv:`, `mtr:` and `aen:`; `wd:` denotes Wikidata. With RDFLib:

```python
from rdflib import Graph

graph = Graph()
for module in ("dubium", "trivium", "metrum"):
    graph.parse(f"{module}/{module}.ttl", format="turtle")
query = """
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX dub: <https://aenigma.criptasemantica.it/dubium#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?discipline ?field ?concept WHERE {
  ?discipline skos:broadMatch ?field ; skos:related ?concept .
  ?field a mtr:Discipline . ?concept a dub:Concept .
}
"""
for row in graph.query(query):
    print(*row)
```

The query crosses the three modules: disciplines of the site, the FORD field in which they sit, the concept of the manifesto with which to read them. Relations between vocabularies are always `skos:closeMatch`, `skos:broadMatch`, `skos:related` or subclasses: never equivalences.

## Verifying and building locally

You need Python 3 with RDFLib, pySHACL and OWL-RL, Raptor (`rapper`), Pandoc, OpenSSL and Clean CSS (`cleancss`). From the repository root:

```bash
python3 tests/verifica.py
python3 dubium/tests/verifica.py
python3 tools/export.py
python3 tools/build_site.py
bash minify.sh
python3 tools/check_site.py
python3 -m http.server 8000 --bind 127.0.0.1
```

The first program reads every module with two parsers, checks headers and versions, resolves cross-module references, validates with SHACL and rejects eleven alterations, computes OWL RL inferences and verifies that no disjoint classes receive common individuals. The site generator makes no network request; the final check resolves every link and anchor of the pages. [Chapter 08](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-08) · [Chapter 15](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-15)

## Contributing

A new reading of the manifesto enters Dubium as a new position with its own provenance ([procedure](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-07)). A new category of the site enters Trivium with a new snapshot and labels in the three languages. A new protocol enters Metrum with family, scope, unit, method in three languages, source and principles. A new module takes a namespace of its own, an entry in the root and in the site generator, and a test ([procedure](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-15)). Published identifiers are never changed; versions are declared with `owl:versionIRI` and `owl:priorVersion`.

## Licences and citation

The content of the ontology (graphs, texts, pages) is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and is to be attributed to FINAI and Alessandro Sevardi; the code of the tools is under [GNU GPL v3 or later](LICENSE). To cite: "Aenigma. The ontology of the Cripta Semantica, version 0.2.0, 2026, https://aenigma.criptasemantica.it/". The GitHub repository is the source of truth; the site is published by GitHub Pages and also served from the Cripta domain.
