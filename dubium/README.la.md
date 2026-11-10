# Dubium. Dux ad primam lectionem

[Italiano](README.md) · [English](README.en.md)

Dubium nomen ducit a dubitatione qua incipit [prooemium Cryptae Semanticae](https://criptasemantica.it/). In *Sophista* Platonis is qui loquitur sibi antea persuasit se intellegere quid vox «ens» significaret. Dialogus hanc fiduciam labefacit. Hinc oritur quaestio de ratione inquirendi. Quomodo inter se conectuntur res quas investigamus, sensus quo eas esse dicimus, atque amplior quaestio de esse?

**Ontologia philosophica** esse et ea quae sunt investigat. **Ontologia retialis** nomina et regulas communes hominibus machinisque praebet, quibus certum rerum ambitum describant. Dubium est ontologia retialis qua textus ontologiae philosophicae explorari potest. Qui interpretationem aestimat ad fontem redeat.

## Prima visitatio

1. Aperi [indicem Dubii](la/index.html) et quaere **esse entis**. Schedula notionem breviter exponit et ad sententias in quibus occurrit ducit.
2. Sequere [F27](la/term/F27.html). Prooemium hic esse ad ens refert. Schedula formulam, rationem legendi et nexus ad eam pervestigandam ostendit.
3. Aperi [P7](la/term/P7.html), ut locum fontis invenias, deinde [F28](la/term/F28.html), ubi esse ipsum tractatur. [Quaestio Q04](la/term/Q04.html) difficultatem ex hac distinctione ortam apertam servat.

Incipere etiam licet a [capitali semantico](la/term/capitaleSemantico.html). Hinc ab iis quae lector intellegit ad significationes a machina tractabiles proceditur.

Etiam [hierarchiam classium et tabulam proprietatum](la/schema.html) inspicere potes. Quaeque vox [paginam propriam](la/term/F27.html) aperit cum nexibus pertinentibus et, ubi adest, exemplo forma Turtle e grapho sumpto.

## Quomodo schedula legatur

**Notio** est relatio ad sensum, cui nomen, explicatio brevis et signum stabile tribuuntur. **Sententia** est propositum, interpretatio vel nexus ad contextum, cui locus fontis assignatur. **Nexus qualificatus** duas notiones intra talem sententiam conectit. **Quaestio** indicat quid adhuc inquirendum sit.

Forma [OWL](https://www.w3.org/TR/owl2-syntax/) genera et proprietates graphi describit. Exempli gratia, a sententia ad nexus eius itur via inversa eius qua quisque nexus ad sententiam pertinet. Regulae [SHACL](https://www.w3.org/TR/shacl/) probant num schedula integra sit, velut num sententiae fons adsit. Formulae philosophicae ut textus leguntur. Earum signa in [formalizatione](FORMALIZZAZIONE.la.md) explicantur.

## Signa et praefixa

**IRI** est nomen integrum rei. `dub:essereDiEnte` est breviatio pro `https://aenigma.criptasemantica.it/dubium#essereDiEnte`. Haec inscriptio ad indicem Italicum et ad locum notionis ducit. Editiones Anglica et Latina eodem grapho utuntur.

| Ubi | Praefixum | IRI fundamentale |
| --- | --- | --- |
| Dubium, in his ducibus | `dub:` | `https://aenigma.criptasemantica.it/dubium#` |
| Exemplaria editorialia Cryptae in RDFa | `cs:` | `https://aenigma.criptasemantica.it/dubium#` |
| Cripta Semantic Service | `cs:` | `https://criptasemantica.it/ns/semantic-service#` |

Praefixum intra documentum quo declaratur valet. Secunda declaratione adhibita, `cs:essereDiEnte` eandem rem designat ac `dub:essereDiEnte`. Ut utroque lexico in eodem documento utaris, `dub:` Dubio et `cs:` ministerio tribue. Cum data coniungis, nomina integra compara. Ministerium indice proprio relationum admissarum utitur. Ut singula schedula per eum indicem praebeatur, ministerium ipsum renovandum est.

## A tabula ad primam interrogationem

[Turtle](https://www.w3.org/TR/turtle/) est forma textualis qua graphus RDF servatur. Enuntiatum RDF subiectum, proprietatem et valorem conectit. [dubium.ttl](dubium.ttl) in editore textus aperi aut ope RDFLib lege. Si Python et RDFLib praesto sunt, hoc exemplum a radice repositorii exsequere.

```python
from rdflib import Graph

graph = Graph().parse("dubium/dubium.ttl", format="turtle")
query = """
PREFIX dub: <https://aenigma.criptasemantica.it/dubium#>
SELECT ?locus ?fons WHERE {
  dub:F27 dub:derivedFrom ?locus .
  ?locus dub:partOfSource ?fons .
}
"""
for locus, fons in graph.query(query):
    print(locus, fons)
```

Accipies IRI loci P7 et inscriptionem prooemii. In programmate, Turtle ex exemplari probato lege, nominibus integris utere et, cum sententiam ostendis, fontem conserva. [shapes.ttl](shapes.ttl) ad formam novi graphi probandam adhibe. Si interpretationem aliam addis, sententiam propriam cum signo et fonte constitue.

## Situm exstruere et probare

Situs e tabulis staticis constat. Ad eas gignendas requiruntur Python 3 cum RDFLib, Pandoc, OpenSSL et Clean CSS (`cleancss`). Ad graphum probandum pySHACL et OWL-RL quoque requiruntur. A radice repositorii exsequere.

```bash
bash minify.sh
python3 tools/build_site.py
python3 dubium/tests/verifica.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Indicem Latinum in computatro tuo aperi apud `http://127.0.0.1:8000/dubium/la/`. Generator Turtle et duces locales legit. Ubi explicatio conversa deest, textus Italicus indicatur. Index etiam sine JavaScript perlegi potest. Filtrum, si adhibetur, intra navigatrum operatur. [Exemplum formalizationis](FORMALIZZAZIONE.la.md#exemplum-interrogationis) ostendit quomodo nexum una cum loco qui eum sustinet invenias.
