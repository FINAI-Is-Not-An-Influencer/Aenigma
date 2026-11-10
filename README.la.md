# Aenigma

[Italiano](README.md) · [English](README.en.md)

Aenigma est ontologia retialis Cryptae Semanticae. **Dubium**, pars prima, notiones, quaestiones et sententias prooemii philosophici cum locis quibus fulciuntur conectit. Consilium graphum machinis, indicem lectoribus et Vicipaginam studio atque usui praebet. [Situs Aenigmatis](https://aenigma.criptasemantica.it/) · [Vicipagina Latina](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA)

## A philosophia ad graphum

Epigraphe prooemii dubitationem e *Sophista* Platonis de significatione vocis «ens» resumit. Prooemium deinde quaestionem de esse cum scriptura, inquisitione philosophica et ontologia informatica conectit. Dubium has distinctiones ad fontem usque persequi sinit. Esse entis et esse ipsum, exempli gratia, schedulas distinctas habent quae ad eundem locum ducunt. [Prooemium Cryptae Semanticae](https://criptasemantica.it/) · [De ratione philosophica](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-01)

## Prima visitatio

1. Indicem aperi et *esse entis* quaere. Schedula nomen, glossam et sententias in quibus notio occurrit ostendit.
2. F27 aperi, deinde P7. Illa schedula sententiam exponit. Haec locum prooemii indicat.
3. F28 et Q04 compara. Linguam mutare et eandem schedulam sequi potes.

[Index](https://aenigma.criptasemantica.it/dubium/la/) · [Dux incipientium](dubium/README.la.md) · [Exercitatio](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-03)

## Quae Dubium contineat

| Res | Quid praebeat |
| --- | --- |
| [Graphus Turtle](dubium/dubium.ttl) | Notiones, sententias, quaestiones, fontes, relationes et formam OWL |
| [Formalizatio](dubium/FORMALIZZAZIONE.la.md) | Tabulam locorum, rationes interpretandi et indicem formularum |
| [Regulae SHACL](dubium/shapes.ttl) | Regulas ad structuram schedularum probandam |
| [Scriptum probationis](dubium/tests/verifica.py) | Interrogationes, consequentias OWL RL et casus datorum mancorum |
| [Generator indicis](tools/build_site.py) | Paginas trilingues e grapho et ducibus Markdown genitas |

RDF data per relationes inter res exprimit. OWL classes et proprietates graphi describit. SHACL campos requisitos examinat. Formulae philosophicae signa et fontes suos servant. Illatio automatica ad structuram datorum pertinet. [Exemplar graphi](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-02)

## Datis uti

Tabulam Turtle lege et per SPARQL graphum interroga. A sententia ad locum `derivedFrom` sequere, deinde a loco ad paginam `partOfSource`. Hanc viam serva cum sententiam ostendis aut citas. [Prima interrogatio](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-05)

`dub:` breviat `https://aenigma.criptasemantica.it/dubium#`. Exemplaria RDFa Cryptae etiam `cs:` huic spatio tribuunt. Cripta Semantic Service `cs:` suo lexico tribuit. Cum utroque uteris, IRI integra compara et `dub:` Dubio declara. [Signa et usus editorialis](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-06)

## Adicere et localiter probare

Ut lectionem addas, locum reperi, signa exsistentia conserva et novam sententiam cum fonte, statu et formula constitue. Tres editiones linguarum adde et graphum proba. [Via adiciendi](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-07)

Requiruntur Python cum RDFLib, pySHACL et OWL-RL, praeterea Pandoc, OpenSSL et Clean CSS (`cleancss`). A radice repositorii exsequere:

```bash
python3 dubium/tests/verifica.py
bash minify.sh
python3 tools/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Aperi `http://127.0.0.1:8000/dubium/la/` et quaestionem, fontes et mutationem linguae proba. [Dux probationis](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-08)

## Ad ulteriorem lectionem

Vicipagina rationem philosophicam, tabulam locorum, exercitationes, vias operandi, glossarium et quaestiones frequentes continet. [Index capitum](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA) · [Tabula locorum](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-04) · [Glossarium et quaestiones](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/LA-09) · [Licentia repositorii](LICENSE)
