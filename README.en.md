# Aenigma

[Italiano](README.md) · [Latine](README.la.md)

Aenigma is the web ontology of Cripta Semantica. **Dubium**, its first module, connects the philosophical manifesto's ideas, questions and positions to their supporting passages. The project includes a graph for software, a catalogue for readers and a Wiki for study and practical use. [Aenigma site](https://aenigma.criptasemantica.it/) · [English Wiki](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN)

## From philosophy to graph

The manifesto's epigraph takes up the doubt about the meaning of “being” in Plato's *Sophist*. The rest of the manifesto connects the question of being to writing, philosophical inquiry and computational ontology. Dubium lets you follow these distinctions back to their source. Being of an entity and being as such, for instance, have separate entries pointing to the same passage. [Cripta Semantica manifesto](https://criptasemantica.it/) · [Philosophical background in the Wiki](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-01)

## A first visit

1. Open the catalogue and search for *being of an entity*. The entry shows its name, gloss and the positions in which the concept occurs.
2. Open F27, then P7. The first entry presents a position. The second locates its passage in the manifesto.
3. Compare F28 and Q04. You can switch languages and follow the same entry.

[Catalogue](https://aenigma.criptasemantica.it/dubium/en/) · [Beginner's guide](dubium/README.en.md) · [Wiki exercise](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-03)

## What Dubium contains

| Resource | What it provides |
| --- | --- |
| [Turtle graph](dubium/dubium.ttl) | Concepts, positions, questions, sources, relations and OWL schema |
| [Formalisation](dubium/FORMALIZZAZIONE.en.md) | Passage map, interpretation notes and formula catalogue |
| [SHACL constraints](dubium/shapes.ttl) | Rules for checking the structure of entries |
| [Verification script](dubium/tests/verifica.py) | Queries, OWL RL inferences and incomplete data cases |
| [Catalogue builder](tools/build_site.py) | Trilingual pages generated from the graph and Markdown guides |

RDF expresses data as relations between resources. OWL describes the graph's classes and properties. SHACL checks required fields. The philosophical formulas preserve the project's notation and provenance. Automatic inference concerns the structure of the data. [Graph model](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-02)

## Reuse the data

Load the Turtle file and query it with SPARQL. Follow `derivedFrom` from the position to the passage and `partOfSource` from the passage to the page. Keep this path when you display or cite a position. [First query](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-05)

`dub:` abbreviates `https://aenigma.criptasemantica.it/dubium#`. The Cripta RDFa previews also use `cs:` for that namespace. Cripta Semantic Service uses `cs:` for its own vocabulary. When using both, compare full IRIs and declare `dub:` for Dubium. [Identifiers and editorial integration](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-06)

## Contribute and preview locally

To add a reading, find the passage, preserve existing identifiers and create a new position with its source, status and formula. Add the three language editions and verify the graph. [Contribution procedure](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-07)

You need Python with RDFLib, pySHACL and OWL-RL, plus Pandoc, OpenSSL and Clean CSS (`cleancss`). From the repository root:

```bash
python3 dubium/tests/verifica.py
bash minify.sh
python3 tools/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/dubium/en/` and try searching, following sources and switching languages. [Build and release guide](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-08)

## Further reading

The Wiki includes the philosophical background, a passage map, exercises, procedures, a glossary and frequently asked questions. [Chapter index](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN) · [Passage map](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-04) · [Glossary and questions](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/EN-09) · [Repository licence](LICENSE)
