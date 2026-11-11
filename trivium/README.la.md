# Trivium. Dux ad primam lectionem

[Italiano](README.md) · [English](README.en.md) · [Formalizatio et methodus](FORMALIZZAZIONE.la.md)

Trivium est secunda pars [Aenigmatis](../README.la.md). Nomen stabile, tribus linguis, tribuit **artibus et disciplinis** quibus situs [Cryptae Semanticae](https://criptasemantica.it/) articulos suos ordinat, **partibus editoriis**, **lineis consilii** et **cellis** allegoricis quas visitator peragrat. Fons est taxonomia publica situs: ducentae et duae categoriae, cum descriptionibus ab auctore scriptis ubi exstant.

Si lexico definito numquam usus es, Trivium ut indicem explicatum cogita: quaeque vox inscriptionem immutabilem habet, nomen Italicum, Anglicum et Latinum, locum in hierarchia et, ubi probari potuit, relationem ad Wikidata et ad campum investigationis congruentem in classificatione FORD, qua [Metrum](../metrum/README.la.md) utitur.

## Cur Trivium

Tres categoriae situs fundamentales sunt Grammatica, Dialectica et Rhetorica: trivium artium liberalium, artes sermonis. Iuxta eas situs Mathematicam, Musicam, Astronomiam et Geographiam servat, quadrivium scilicet in quo geographia, «descriptio et mensura cosmi sublunaris», locum geometriae tenet. Pars hanc architecturam in duabus collectionibus, [Trivio](la/term/trivio.html) et [Quadrivio](la/term/quadrivio.html), conservat et ceteras disciplinas inde pendere facit. Ordo medii aevi scientiarum ita fit tabula operis editorii percurrenda.

## Prima visitatio

1. Aperi [indicem Trivii](la/index.html) et quaere **Dialecticam**. Schedula descriptionem auctoris refert, ramos inde descendentes (epistemologiam, hermeneuticam, historiam philosophiae aliosque multos), consensionem cum Wikidata et campum FORD «Philosophia, ethica et religio».
2. Aperi [Rhetoricam](la/term/retorica.html). Videbis situm oeconomiam, iurisprudentiam, sociologiam et culturam sub ea collocare: rhetoricam ut «architecturam potestatis», secundum descriptionem.
3. Transi ad [cellas](la/index.html#rooms). [Cella FINAI](la/term/stanza-di-finai.html) et [Cella Rosae Caeruleae](la/term/stanza-della-rosa-blu.html) loca sunt duorum hominum qui Cryptam hyperscribunt.
4. Linguam nexibus superioribus muta: eadem schedula Italice, Anglice et Latine exstat.

## Quomodo schedula legatur

| Campus | Quid significet |
| --- | --- |
| Titulus praelatus | Nomen tribus linguis. Italicum est situs; Anglicum et Latinum versiones editoriae sunt. |
| Notatio | Clavis (*slug*) categoriae in situ, exempli gratia `dialettica`. |
| Index categoriae | Numerus quem WordPress categoriae tribuit, ad situm et partem comparandos utilis. |
| Fons | Pagina publica categoriae. |
| Notio latior / angustiores | Hierarchia a situ declarata. |
| Nota ambitus | Descriptio ab auctore scripta, Italice, cum versione. |
| Consensio proxima (Wikidata) | Res Wikidata probata. Est `skos:closeMatch`, numquam aequivalentia. |
| Campus FORD comparandus | Campus investigationis in quo disciplina collocatur, secundum Metrum. |
| Notiones cognatae | Notio Dubii quam pars ut lectionem proponit, vel alia vox Trivii. |

Quattuor schemata munera separant: **disciplinae**, **genera et partes** (nuntii, recensiones, auctores, vitae, merces, synergiae, canales), **lineae consilii** (communismus digitalis, rete semantica universalis, machina quaerendi hermeneutica, programmatio philosophica, metaphysica ludi, studia academica) et **cellae**. [Hierarchia](la/schema.html) quattuor arbores ostendit.

## Signa et praefixa

`trv:dialettica` breviat `https://aenigma.criptasemantica.it/trivium#dialettica`. In tabulis et exemplis etiam `wd:` pro Wikidata, `mtr:` pro campis FORD partis Metrum et `dub:` pro notionibus Dubii occurrunt. Duae categoriae situs ambae «Logica» vocantur: prior, summa, est `trv:logica`; altera, sub Dialectica, est `trv:logica-dialettica`, eodem suffixo quo situs «Antropologia» distinguit.

## A tabula ad primam interrogationem

```python
from rdflib import Graph

graph = Graph().parse("trivium/trivium.ttl", format="turtle")
query = """
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?nomen ?wikidata WHERE {
  ?notio skos:broader trv:dialettica ; skos:prefLabel ?nomen .
  FILTER ( lang(?nomen) = "la" )
  OPTIONAL { ?notio skos:closeMatch ?wikidata }
} ORDER BY ?nomen
"""
for nomen, wikidata in graph.query(query):
    print(nomen, wikidata or "")
```

Accipies disciplinas quas situs sub Dialectica collocat, cum re Wikidata ubi adest. Muta `trv:dialettica` in `trv:retorica` vel `trv:grammatica` ut trivium percurras.

## Trivio extra Aenigma uti

In articulo situs, vel in grapho ministerii semantici Cryptae, categoria ut subiectum suo IRI declarari potest: `schema:about trv:dialettica` vel `dcterms:subject trv:dialettica`. Qui graphum legit nomen, hierarchiam, Wikidata et campum FORD sine aliis tabulis reperit. Ministerium semanticum «argumenta Cryptae» sua cum Trivio per `skos:closeMatch`, non per aequivalentiam, conectit.

## Exstruere et probare

Tabula `trivium.ttl` a [tools/trivium_from_taxonomy.py](../tools/trivium_from_taxonomy.py) ex exemplari `fonti/categorie-criptasemantica-2026-11-11.json` gignitur. Tituli, versiones, consensiones et pontes in generatore scripti sunt. A radice repositorii:

```bash
python3 tools/trivium_from_taxonomy.py
python3 tests/verifica.py
python3 tools/build_site.py
```

[Regulae SHACL](shapes.ttl) probant quamque notionem tres titulos, schema, notationem et fontem publicum habere, consensiones ad solam Wikidata spectare et nullam notionem parentem in alio schemate habere. [Programma probationis](../tests/verifica.py) etiam undecim mutationes consulto factas temptat, quae recusari debent.

## Conferre

Nova categoria situs in Trivium intrat cum novo exemplari et cum titulis Anglico et Latino in generatore. Consensio Wikidata tantum post probationem additur et semper ut `skos:closeMatch` declaratur. Pons FORD postulat disciplinam re vera in illum campum secundum Manuale Frascati cadere. Nexus cum Dubio lectio est: in [formalizatione](FORMALIZZAZIONE.la.md) motivanda est.
