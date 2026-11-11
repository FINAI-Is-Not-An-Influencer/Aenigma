# Trivium. Una guida per iniziare

[English](README.en.md) · [Latine](README.la.md) · [Formalizzazione e metodo](FORMALIZZAZIONE.md)

Trivium è il secondo modulo di [Aenigma](../README.md). Dà un nome stabile, in tre lingue, alle **arti e discipline** con cui il sito della [Cripta Semantica](https://criptasemantica.it/) ordina i suoi articoli, alle sue **sezioni editoriali**, alle sue **linee di programma** e alle **stanze** allegoriche che il visitatore attraversa. La fonte è la tassonomia pubblica del sito: duecentodue categorie, con le descrizioni scritte dall'autore dove esistono.

Se non hai mai usato un vocabolario controllato, pensa a Trivium come a un indice ragionato: ogni voce ha un indirizzo che non cambia, un nome in italiano, inglese e latino, un posto nella gerarchia e, quando è stato possibile verificarlo, un rimando a Wikidata e al campo di ricerca corrispondente nella classificazione FORD usata da [Metrum](../metrum/README.md).

## Perché si chiama Trivium

Le tre categorie fondanti del sito sono Grammatica, Dialettica e Retorica: il trivio delle arti liberali, le arti del discorso. Accanto a esse il sito tiene Matematica, Musica, Astronomia e Geografia, cioè un quadrivio in cui la geografia, «mappatura e misurazione del cosmo sublunare», prende il posto della geometria. Il modulo conserva questa architettura in due collezioni, [Trivio](term/trivio.html) e [Quadrivio](term/quadrivio.html), e vi fa discendere tutte le altre discipline. L'ordine medievale del sapere diventa così una mappa navigabile del lavoro editoriale.

## La prima visita

1. Apri il [catalogo di Trivium](index.html) e cerca **Dialettica**. La scheda riporta la descrizione d'autore, i rami che ne discendono (epistemologia, ermeneutica, storia della filosofia e molti altri), la corrispondenza con Wikidata e il campo FORD «Filosofia, etica e religione».
2. Apri [Retorica](term/retorica.html). Vedrai che il sito vi colloca economia, giurisprudenza, sociologia e cultura: la retorica come «architettura del potere», secondo la descrizione.
3. Passa alle [stanze](index.html#rooms). La [Stanza di FINAI](term/stanza-di-finai.html) e la [Stanza della Rosa Blu](term/stanza-della-rosa-blu.html) sono i luoghi delle due persone che iperscrivono la Cripta.
4. Cambia lingua con i collegamenti in alto: la stessa scheda esiste in italiano, inglese e latino.

## Come leggere una scheda

| Campo | Che cosa significa |
| --- | --- |
| Etichetta preferita | Il nome nelle tre lingue. L'italiano è quello del sito; inglese e latino sono traduzioni editoriali. |
| Notazione | Lo *slug* della categoria sul sito, per esempio `dialettica`. |
| Identificativo della categoria | Il numero che WordPress assegna alla categoria. Serve a confrontare sito e modulo. |
| Fonte | La pagina pubblica della categoria. |
| Concetto più ampio / più specifici | La gerarchia dichiarata dal sito. |
| Nota d'ambito | La descrizione scritta dall'autore, in italiano, con traduzione. |
| Corrispondenza vicina (Wikidata) | Un elemento Wikidata verificato. È `skos:closeMatch`, mai un'equivalenza. |
| Campo FORD di riferimento | Il campo di ricerca e sviluppo in cui la disciplina si colloca, secondo Metrum. |
| Concetti collegati | Un concetto di Dubium che il modulo propone come lettura, oppure un'altra voce di Trivium. |

Quattro schemi tengono separate le funzioni: le **discipline**, i **generi e le sezioni** (notizie, recensioni, autori, profili, prodotti, sinergie, canali), le **linee di programma** (comunismo digitale, rete semantica mondiale, motore di ricerca ermeneutico, programmazione filosofica, metafisica del gioco, studi accademici) e le **stanze**. La [gerarchia](schema.html) mostra i quattro alberi.

## Identificatori e prefissi

`trv:dialettica` abbrevia `https://aenigma.criptasemantica.it/trivium#dialettica`. Nei file e negli esempi compaiono anche `wd:` per Wikidata, `mtr:` per i campi FORD di Metrum e `dub:` per i concetti di Dubium. Due categorie del sito si chiamano entrambe «Logica»: la prima, di vertice, è `trv:logica`; la seconda, dentro Dialettica, è `trv:logica-dialettica`, con lo stesso suffisso che il sito usa per «Antropologia».

## Dal file alla prima interrogazione

```python
from rdflib import Graph

graph = Graph().parse("trivium/trivium.ttl", format="turtle")
query = """
PREFIX trv: <https://aenigma.criptasemantica.it/trivium#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT ?nome ?wikidata WHERE {
  ?concetto skos:broader trv:dialettica ; skos:prefLabel ?nome .
  FILTER ( lang(?nome) = "it" )
  OPTIONAL { ?concetto skos:closeMatch ?wikidata }
} ORDER BY ?nome
"""
for nome, wikidata in graph.query(query):
    print(nome, wikidata or "")
```

Ottieni le discipline che il sito colloca sotto Dialettica, con l'eventuale elemento Wikidata. Cambia `trv:dialettica` in `trv:retorica` o `trv:grammatica` per percorrere il trivio.

## Usare Trivium fuori da Aenigma

In un articolo del sito, o nel grafo del servizio semantico della Cripta, una categoria può essere dichiarata come soggetto con il suo IRI: `schema:about trv:dialettica` oppure `dcterms:subject trv:dialettica`. Chi legge il grafo trova nome, gerarchia, Wikidata e campo FORD senza bisogno di altre tabelle. Il servizio semantico collega i propri «Temi Cripta» a Trivium con `skos:closeMatch`, non con un'equivalenza.

## Costruire e verificare

Il file `trivium.ttl` è generato da [tools/trivium_from_taxonomy.py](../tools/trivium_from_taxonomy.py) a partire dall'istantanea `fonti/categorie-criptasemantica-2026-11-11.json`. Le etichette, le traduzioni, le corrispondenze e i ponti sono scritti nel generatore. Dalla radice del repository:

```bash
python3 tools/trivium_from_taxonomy.py
python3 tests/verifica.py
python3 tools/build_site.py
```

I [vincoli SHACL](shapes.ttl) controllano che ogni concetto abbia tre etichette, uno schema, una notazione e una fonte pubblica, che le corrispondenze puntino solo a Wikidata e che nessun concetto abbia un padre in un altro schema. Il [programma di verifica](../tests/verifica.py) prova anche undici alterazioni volute, che devono essere respinte.

## Contribuire

Una nuova categoria del sito entra in Trivium con una nuova istantanea e con le sue etichette inglese e latina nel generatore. Una corrispondenza Wikidata si aggiunge solo dopo averla verificata e si dichiara sempre come `skos:closeMatch`. Un ponte FORD richiede che la disciplina rientri davvero in quel campo secondo il Manuale di Frascati. Un legame con Dubium è una lettura: va motivato nella [formalizzazione](FORMALIZZAZIONE.md).
