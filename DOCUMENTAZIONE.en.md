# Map of the Aenigma documentation

[Italiano](documentazione.html) · [Latine](la/documentazione.html)

The documentation of Aenigma lives in three places that refer to one another. **This site** is the reference: for every module it offers the catalogue, the hierarchy, a beginner's guide, the formalisation and a page for every term, in Italian, English and Latin. **The repository** keeps the graphs, the constraints, the tools, the tests and the changelog. **The Wiki** gathers the encyclopaedic chapters, the step-by-step exercises and the procedures. None of the three is enough on its own; together they form a single work, designed so that the work of encoding is also an experience of study.

## Four reading paths

| If you are… | Start from | Then |
| --- | --- | --- |
| New to ontologies | the [Dubium guide](dubium/en/guide.html), which starts from an example and reaches a first query | [Wiki chapter 01](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-01) and the [exercise of chapter 03](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-03) |
| A user of the data (developers, editors, services) | the "Files for reuse" of each catalogue: Turtle, JSON-LD, RDF/XML, context, SHACL | [chapters 05 and 06](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-05) on querying and identifiers, the [procedures of chapter 15](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-15) |
| A scholar (ontology, semiotics, scientometrics) | the formalisations of [Dubium](dubium/en/formal.html), [Trivium](trivium/en/formal.html) and [Metrum](metrum/en/formal.html) | [chapters 02, 04, 10–13](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN) on the model, the map of the manifesto and the bridge between ontology and scientometrics |
| A philosopher | the [Cripta Semantica manifesto](https://criptasemantica.it/) and the entry [F28](dubium/en/term/F28.html), where being is thematised without a chosen thing | [chapter 14](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-14) on the names of Aenigma, Dubium, Trivium and Metrum and [chapter 16](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-16) on the open questions |

## The three modules, page by page

| Module | Catalogue | Hierarchy | Guide | Formalisation | Graph | Constraints | Examples |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dubium 0.2.0 · the question | [catalogue](dubium/en/index.html) | [hierarchy](dubium/en/schema.html) | [guide](dubium/en/guide.html) | [formalisation](dubium/en/formal.html) | [dubium.ttl](dubium/dubium.ttl) · [JSON-LD](dubium/dubium.jsonld) · [RDF/XML](dubium/dubium.rdf) | [shapes.ttl](dubium/shapes.ttl) | [F27](dubium/en/term/F27.html) |
| Trivium 0.1.0 · the arts | [catalogue](trivium/en/index.html) | [hierarchy](trivium/en/schema.html) | [guide](trivium/en/guide.html) | [formalisation](trivium/en/formal.html) | [trivium.ttl](trivium/trivium.ttl) · [JSON-LD](trivium/trivium.jsonld) · [RDF/XML](trivium/trivium.rdf) | [shapes.ttl](trivium/shapes.ttl) | [Dialectic](trivium/en/term/dialettica.html) |
| Metrum 0.1.0 · the measure | [catalogue](metrum/en/index.html) | [hierarchy](metrum/en/schema.html) | [guide](metrum/en/guide.html) | [formalisation](metrum/en/formal.html) | [metrum.ttl](metrum/metrum.ttl) · [JSON-LD](metrum/metrum.jsonld) · [RDF/XML](metrum/metrum.rdf) | [shapes.ttl](metrum/shapes.ttl) | [esempi.ttl](metrum/esempi.ttl) · [Incoming citations](metrum/en/term/p-citazioni.html) |

The [root aenigma.ttl](aenigma.ttl) imports the three modules and describes them; [void.ttl](void.ttl) lists the distributions and the number of triples. The [changelog](CHANGELOG.md) tells what changed and why.

## The Wiki chapters

1. [Ontology and the question of being](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-01)
2. [The graph model](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-02)
3. [Browsing the catalogue step by step](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-03)
4. [Reading the formalisation of the manifesto](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-04)
5. [Downloading, querying and verifying](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-05)
6. [IRIs, prefixes and editorial integration](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-06)
7. [Adding an entry or a reading](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-07)
8. [Building the site and testing a release](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-08)
9. [Glossary and frequently asked questions](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-09)
10. [Aenigma as a network of modules](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-10)
11. [Trivium: the arts and disciplines of the Cripta](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-11)
12. [Metrum: measuring research with provenance](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-12)
13. [From ontology to scientometrics and back](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-13)
14. [The names: enigma, doubt, trivium, measure](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-14)
15. [Procedures: adding a module, releasing a version, aligning a vocabulary](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-15)
16. [Versions, changes and open questions](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-16)

## How to verify by yourself

Whoever clones the [repository](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma) can reproduce every check offline: `python3 tests/verifica.py` tests the whole network (parsing with two parsers, headers, cross-module references, SHACL with eleven alterations, OWL RL inferences); `python3 dubium/tests/verifica.py` tests Dubium; `python3 tools/export.py`, `python3 tools/build_site.py` and `bash minify.sh` regenerate exports and site; `python3 tools/check_site.py` resolves every link and anchor. If the site you read and the site you generate coincide, the documentation is that of the graph.

## Licence and citation

The graphs, texts and pages of Aenigma are released under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/); the code of the tools under GNU GPL v3 or later. To cite: "Aenigma. The ontology of the Cripta Semantica, version 0.2.0, FINAI and Alessandro Sevardi, 2026, https://aenigma.criptasemantica.it/". To cite a term, use its IRI: pages are stable and prior versions remain citable.
