# Aenigma

[Italiano](README.md) · [English](README.en.md) · [Situs indicis](https://aenigma.criptasemantica.it/) · [Tabula documentorum](https://aenigma.criptasemantica.it/la/documentazione.html) · [Vicipagina](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA)

Aenigma est ontologia retialis [Cryptae Semanticae](https://criptasemantica.it/), hypertextus ontologici fundamentalis. A versione 0.2.0 est **rete trium partium**, quarum quaeque spatium nominum, versionem, tres linguas et regulas proprias habet:

| Pars | Praefixum | Quid nominet | Versio |
| --- | --- | --- | --- |
| [Dubium](dubium/README.la.md) · quaestio | `dub:` | Notiones, sententiae, quaestiones et loci prooemii philosophici, cum fonte cuiusque sententiae | 0.2.0 |
| [Trivium](trivium/README.la.md) · artes | `trv:` | Ducentae disciplinae, genera, lineae consilii et cellae situs, cum Wikidata et campis FORD | 0.1.0 |
| [Metrum](metrum/README.la.md) · mensura | `mtr:` | Observatio scientometrica qualificata: protocolla, familiae, ambitus, ambitus corporis, campi FORD et principia aestimationis responsabilis | 0.1.0 |

[Radix `aenigma.ttl`](aenigma.ttl) tres partes importat et describit; [`void.ttl`](void.ttl) distributiones enumerat. Nomen ex aenigmate Graeco venit: formula quae celat quod ostendit. Nomina ontologiae res non exhauriunt; quaestionem de sensu essendi apertam servant dum eam hominibus et programmatibus consultabilem reddunt.

## A philosophia ad graphum

Prooemium Cryptae a perplexitate *Sophistae* de voce «ens» incipit et quaestionem de esse cum historia scripturae conectit: cum machina abstracta anni 1936 hyperhistoria incipit et scriptura quantificatur; hyperscriptura hypertextus gignit et Rete capitale semanticum per ontologias accumulat. Dubium hunc textum locum post locum formalizat. Trivium rationem qua situs scientiam ordinat serio accipit: trivium artium sermonis et quadrivium in quo geographia geometriam substituit. Metrum quantificationem scripturae ut rem ontologiae cum origine sua recipit, non ut sententiam patitur. Coniunctae tres partes viam a quaestione ad nomina et a nominibus ad mensuram, et retro, delineant. [Caput 14 Vicipaginae](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-14)

## Prima visitatio

1. Aperi [schedulam F27](https://aenigma.criptasemantica.it/dubium/la/term/F27.html) Dubii: sententiam prooemii, locum qui eam fulcit, formulam et relationes.
2. Aperi [Dialecticam](https://aenigma.criptasemantica.it/trivium/la/term/dialettica.html) in Trivio: descriptionem auctoris, ramos, consensionem Wikidata et campum FORD.
3. Aperi [Citationes receptas](https://aenigma.criptasemantica.it/metrum/la/term/p-citazioni.html) in Metro: familiam, ambitum, unitatem, methodum et principia quae usum finiunt.
4. Linguam superne muta: quaeque pagina Italice, Anglice et Latine exstat.

## Quid repositorium contineat

| Via | Materia |
| --- | --- |
| `aenigma.ttl`, `void.ttl` | Radix retis et descriptio distributionum |
| `dubium/`, `trivium/`, `metrum/` | Cuique parti: graphus Turtle, JSON-LD, RDF/XML, contextus JSON-LD, regulae SHACL, duces et formalizationes tribus linguis, paginae situs |
| `metrum/esempi.ttl`, `metrum/fonti/`, `trivium/fonti/` | Exempla ficta et exemplaria fontium publicorum quibus generatores utuntur |
| `tools/` | Generatores partium (`trivium_from_taxonomy.py`, `metrum_from_dictionary.py`), exportator (`export.py`), generator situs (`build_site.py`), tabulae documentorum (`doc_tables.py`), probator nexuum (`check_site.py`) |
| `tests/verifica.py`, `dubium/tests/verifica.py` | Probatio retis et probatio Dubii |
| `index.src.html`, `minify.sh`, `style.css`, `reference.css`, `search.js` | Pagina prima et compages visualis situs |
| `DOCUMENTAZIONE*.md`, `CHANGELOG.md` | Tabula documentorum et index versionum |

## Datis uti

Quaeque pars per se oneratur (`dubium/dubium.ttl`, `trivium/trivium.ttl`, `metrum/metrum.ttl`) vel omnes simul a radice. Praefixa praelata sunt `dub:`, `trv:`, `mtr:` et `aen:`; `wd:` Wikidata significat. Ope RDFLib:

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
SELECT ?disciplina ?campus ?notio WHERE {
  ?disciplina skos:broadMatch ?campus ; skos:related ?notio .
  ?campus a mtr:Discipline . ?notio a dub:Concept .
}
"""
for row in graph.query(query):
    print(*row)
```

Interrogatio tres partes transit: disciplinas situs, campum FORD in quo collocantur, notionem prooemii qua legantur. Relationes inter lexica semper sunt `skos:closeMatch`, `skos:broadMatch`, `skos:related` vel subclasses: numquam aequivalentiae.

## Localiter probare et exstruere

Requiruntur Python 3 cum RDFLib, pySHACL et OWL-RL, Raptor (`rapper`), Pandoc, OpenSSL et Clean CSS (`cleancss`). A radice repositorii:

```bash
python3 tests/verifica.py
python3 dubium/tests/verifica.py
python3 tools/export.py
python3 tools/build_site.py
bash minify.sh
python3 tools/check_site.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Primum programma quamque partem duobus interpretibus legit, capita et versiones probat, relationes inter partes resolvit, SHACL validat et undecim mutationes recusat, illationes OWL RL computat et probat nullam classem disiunctam individua communia accipere. Generator situs rete non petit; probatio ultima omnem nexum et ancoram paginarum resolvit. [Caput 08](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-08) · [Caput 15](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-15)

## Conferre

Nova lectio prooemii in Dubium ut sententia nova cum origine propria intrat ([via](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-07)). Nova categoria situs in Trivium cum novo exemplari et titulis trium linguarum intrat. Novum protocollum in Metrum cum familia, ambitu, unitate, methodo tribus linguis, fonte et principiis intrat. Nova pars spatium nominum proprium, vocem in radice et in generatore situs, et probationem accipit ([via](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-15)). Signa edita numquam mutantur; versiones per `owl:versionIRI` et `owl:priorVersion` declarantur.

## Licentiae et citatio

Materia ontologiae (graphi, textus, paginae) sub [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) editur et FINAI atque Alexandro Sevardi tribuenda est; programmata instrumentorum sub [GNU GPL v3 vel posteriore](LICENSE). Ad citandum: «Aenigma. Ontologia Cryptae Semanticae, versio 0.2.0, 2026, https://aenigma.criptasemantica.it/». Repositorium in GitHub fons veritatis est; situs a GitHub Pages editur et etiam e dominio Cryptae praebetur.
