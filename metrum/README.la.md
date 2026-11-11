# Metrum. Dux ad primam lectionem

[Italiano](README.md) · [English](README.en.md) · [Formalizatio](FORMALIZZAZIONE.la.md)

Metrum est tertia pars [Aenigmatis](../README.la.md). Ad id valet ut dicatur **quomodo** mensura investigationis obtenta sit, non quis pluris sit. Quisque numerus qui circa investigationem circumfertur (citationes, index h, index impulsus, partes aditus aperti, usus iterati datorum et programmatum) e protocollo nascitur ad corpus adhibito, intra tempus, certo ambitu et e certo fonte. Sine his quinque notitiis duo numeri comparari non possunt. Metrum eas necessarias reddit.

Si scientometriam numquam tractavisti, tres regulas quas pars continet memento: datum absens non est nihil; duae mensurae tantum comparantur si idem pactum habent; principium aestimationis responsabilis mensuram non vetat, usum improprium finit. Pagina «De nobis» Cryptae dicit nullas mensuras neutrales qualitatis scientiae exstare, sed systemata technica quae eam mutant: Metrum est modus hanc conscientiam intra graphum servandi.

## Cur Metrum

*Metrum* est mensura, sed etiam metrum versus: regula quae comparabile reddit quod aliter solus sonus esset. Prooemium Cryptae in discrimine anni 1936 initium «quantificationis scripturae» describit ([F08 Dubii](../dubium/la/term/F08.html)). Scientometria una est ex formis illius quantificationis. Metrum eam ut rem ontologiae cum origine sua recipit, non ut sententiam patitur.

## Prima visitatio

1. Aperi [indicem partis Metrum](la/index.html) et quaere **Citationes receptas**. Schedula protocolli familiam (receptionem), ambitum (opus vel editionem), unitatem, methodum tribus linguis, fontem et principia quae eam dirigunt ostendit.
2. Aperi [DORA](la/term/principle-dora.html). Schedula protocolla enumerat quorum usum principium finit: septem indices sedium, ab indice impulsus incipiens.
3. Aperi campum FORD [Philosophia, ethica et religio](la/term/ford-6-3.html): campum parentem et disciplinas Trivii quae ad eum pontem faciunt videbis.
4. Aperi [hierarchiam](la/schema.html): classes, proprietates, quattuordecim familias et duodesexaginta protocolla congregata.

## Quomodo protocollum legatur

| Campus | Quid significet |
| --- | --- |
| Familia | Coetus cui pertinet: receptio, sedes, apertura, translatio, data, programmata, methodus, studia humanitatis, investigatio socialis, clinica, technica, agraria, artes, interventus. |
| Pertinet ad | Ambitus subiecti: opus, sedes, persona vel institutio, data, programma, artefactum, interventus, fructus. Mensura sedis ad auctorem non transfertur. |
| Genus valoris | Numerus integer, decimalis, pars centesima, pars computata vel testimonium textuale. |
| Unitas | Citationes, opera, anni, pars centesima, textus. |
| Methodus | Quid fiat ut valor obtineatur. Methodo mutata ministerium versionem novam postulat. |
| Coetum comparandum requirit | Verum pro indicibus normatis (vis ad disciplinam relata, centesimae partes). |
| Fons | Documentum publicum quod indicem definit vel disputat. |
| Principio directum | Principia DORA, Leiden, CoARA, FAIR, FORCE11 vel CRediT pertinentia. |

## Quomodo observatio scribatur

Observatio est una adhibitio protocolli. Hoc est exemplum fictum in [esempi.ttl](esempi.ttl) inclusum: opus, corpus et valores ficti sunt, lexicon verum.

```turtle
@prefix mtr: <https://aenigma.criptasemantica.it/metrum#> .
@prefix ex: <https://aenigma.criptasemantica.it/metrum/esempi#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:osservazione-1 a mtr:Observation ;
    mtr:protocol mtr:p-citazioni ;            # quod pactum mensurae
    mtr:about ex:opera-dimostrativa ;         # de qua re
    mtr:state mtr:state-observed ;            # observatum, absens, suppressum, non applicabile
    mtr:coverage mtr:coverage-complete ;      # quanta pars corporis examinata sit
    mtr:corpusLabel "Corpus sintetico di prova" ;
    mtr:periodStart "2024-01-01"^^xsd:date ; mtr:periodEnd "2024-12-31"^^xsd:date ;
    mtr:acquiredOn "2025-07-01"^^xsd:date ;   # quando lectum sit
    mtr:discipline mtr:ford-6-3 ;             # quo in campo
    mtr:source <https://example.org/corpus> ; # unde corpus veniat
    mtr:evidence <https://example.org/evidence/1> ;  # testimonium observationis
    mtr:value 12 .
```

Tres lineae maximi momenti sunt `state`, `coverage` et `evidence`. Status dicit num numerus exstet; ambitus quanti valeat; testimonium ubi probetur. [Regulae SHACL](shapes.ttl) observationem «observatam» sine valore, datum absens cum valore, ambitum partialem sine lectione editoria, tempus inversum recusant.

## A tabula ad primam interrogationem

```python
from rdflib import Graph

graph = Graph().parse("metrum/metrum.ttl", format="turtle")
graph.parse("metrum/esempi.ttl", format="turtle")
query = """
PREFIX mtr: <https://aenigma.criptasemantica.it/metrum#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?observatio ?valor ?protocollum WHERE {
  ?observatio a mtr:Observation ; mtr:state mtr:state-observed ;
      mtr:value ?valor ; mtr:protocol ?p ; mtr:discipline mtr:ford-6-3 .
  ?p skos:prefLabel ?protocollum . FILTER ( lang(?protocollum) = "la" )
}
"""
for row in graph.query(query):
    print(*row)
```

Accipies observationes cum valore in campo FORD philosophiae, cum nomine protocolli. Ut scias num duae observationes comparari possint, `mtr:Comparison` inter eas declara et formis proba: comparatio admittitur tantum si subiectum, protocollum, corpus, tempus et disciplinas communicant, ambitu declarato.

## Pontes ad ceteras partes

Cum **Dubio**: caput partis ad `dub:F08` et `dub:F19` remittit, sententias de quantificatione scripturae et de quantificatione ontologica, et ad capitale semanticum. Cum **Trivio**: disciplinae situs per `skos:broadMatch` campum FORD in quo collocantur declarant, ut observatio de articulo «Dialecticae» campum suum reperiat. Cum **ministerio semantico Cryptae**: classes lexici operativi ministerii subclasses classium Metrum declarantur, et protocolla eius eandem clavem habent: `citazioni@1.0.0` in ministerio est `mtr:p-citazioni` hic.

## Exstruere et probare

Tabula `metrum.ttl` a [tools/metrum_from_dictionary.py](../tools/metrum_from_dictionary.py) gignitur, quod exemplar lexici protocollorum in `fonti/` legit et formam, principia, ambitus et ambitus corporis manu scriptos continet. A radice repositorii:

```bash
python3 tools/metrum_from_dictionary.py
python3 tests/verifica.py
python3 tools/build_site.py
```

Programma probationis numeros (58 protocolla, 48 campos, 35 principia), fontes, pontes, regulas SHACL in exemplis et sex mutationes partis Metrum consulto factas probat, omnes recusatas.

## Conferre

Novum protocollum postulat: clavem minusculis litteris, familiam, ambitus, genus valoris, unitatem et methodum tribus linguis, fontem publicum, principia pertinentia. Si methodus protocolli exsistentis mutatur, clavis manet et ministerium versionem novam inscribit: IRI partis Metrum pactum designat, non eius versionem. Novum principium fontem publicum et titulum tribus linguis postulat; si usum alicuius protocolli finit, id per `mtr:cautions` declarat.
