# Dubium. Una guida per iniziare

[English](README.en.md) · [Latine](README.la.md)

Dubium prende il nome dal dubbio che apre il [manifesto della Cripta Semantica](https://criptasemantica.it/). Chi parla nel *Sofista* pensava di sapere che cosa voleva dire «essente». Il dialogo incrina quella certezza. Da questa difficoltà nasce una domanda di metodo. Come mettere in relazione le cose che indaghiamo, il senso in cui diciamo che sono e la domanda più ampia sull'essere?

Un'**ontologia filosofica** indaga l'essere e ciò che è. Un'**ontologia web** offre a lettori e programmi nomi e regole condivisi per descrivere un ambito. Dubium è un'ontologia web che rende esplorabile un testo di ontologia filosofica. La fonte rimane il punto da cui partire per discutere le letture.

## La prima visita

1. Apri il [catalogo di Dubium](index.html) e cerca **essere di un ente**. La voce offre una definizione e rimanda alle posizioni in cui compare.
2. Segui [F27](term/F27.html). Il manifesto tratta qui l'essere in relazione a un ente. La scheda mostra la formula, il modo di lettura e le relazioni che aiutano a navigarla.
3. Apri [P7](term/P7.html) per ritrovare il capoverso e poi [F28](term/F28.html), dove l'indagine tematizza l'essere in quanto tale. La [domanda Q04](term/Q04.html) tiene aperta la difficoltà che nasce da questa distinzione.

Puoi cominciare anche dal [capitale semantico](term/capitaleSemantico.html). Il percorso passa da contenuti comprensibili a chi legge a significati organizzati per essere trattati da una macchina.

Puoi anche consultare la [gerarchia e la tabella delle proprietà](schema.html). Ogni voce apre una [pagina di riferimento](term/F27.html) con i collegamenti pertinenti e, quando disponibile, un esempio Turtle tratto dal grafo.

## Come leggere una scheda

Un **concetto** è un riferimento con un nome, una glossa e un identificatore stabile. Una **posizione** è una tesi, una lettura oppure un raccordo attribuito a un passo. Una **relazione qualificata** collega due concetti entro quella posizione. Una **domanda** indica che cosa è ancora in questione.

Lo schema [OWL](https://www.w3.org/TR/owl2-syntax/) descrive le categorie e le proprietà del grafo. Per esempio, risalire da una posizione alle sue relazioni è l'inverso del collegamento di ciascuna relazione alla posizione. I vincoli [SHACL](https://www.w3.org/TR/shacl/) controllano che le schede siano complete, per esempio che una posizione abbia una fonte. Le formule filosofiche sono leggibili come testo e sono spiegate nella [formalizzazione](FORMALIZZAZIONE.md).

## Identificatori e prefissi

Un **IRI** è il nome completo di una risorsa. `dub:essereDiEnte` è un'abbreviazione per `https://aenigma.criptasemantica.it/dubium#essereDiEnte`. Il catalogo italiano è la pagina a cui conduce quell'indirizzo, con un'ancora per il termine. Le versioni inglese e latina consultano lo stesso grafo.

| Dove | Prefisso | IRI di base |
| --- | --- | --- |
| Dubium, in queste guide | `dub:` | `https://aenigma.criptasemantica.it/dubium#` |
| Anteprime editoriali RDFa della Cripta | `cs:` | `https://aenigma.criptasemantica.it/dubium#` |
| Cripta Semantic Service | `cs:` | `https://criptasemantica.it/ns/semantic-service#` |

Il prefisso vale nel documento che lo dichiara. `cs:essereDiEnte` in un'anteprima con la seconda dichiarazione identifica la stessa risorsa di `dub:essereDiEnte`. Per usare entrambi i vocabolari nello stesso documento, dichiara `dub:` per Dubium e `cs:` per il servizio. Verifica gli IRI dopo aver espanso i prefissi. Il servizio continua a usare il proprio elenco di riferimenti ammessi. Per aggiungere una singola scheda a quell'elenco serve un aggiornamento esplicito del servizio.

## Dal file alla prima interrogazione

[Turtle](https://www.w3.org/TR/turtle/) è un formato testuale per salvare un grafo RDF. Una riga RDF collega un soggetto, una proprietà e un valore. Puoi aprire [dubium.ttl](dubium.ttl) in un editor di testo oppure leggerlo con RDFLib. Con Python e RDFLib già disponibili, esegui questo esempio dalla radice del repository.

```python
from rdflib import Graph

graph = Graph().parse("dubium/dubium.ttl", format="turtle")
query = """
PREFIX dub: <https://aenigma.criptasemantica.it/dubium#>
SELECT ?passo ?fonte WHERE {
  dub:F27 dub:derivedFrom ?passo .
  ?passo dub:partOfSource ?fonte .
}
"""
for passo, fonte in graph.query(query):
    print(passo, fonte)
```

Ottieni l'IRI di P7 e l'indirizzo del manifesto. Per un'applicazione, carica il Turtle da una copia controllata, usa gli IRI completi come chiavi e mantieni la fonte quando mostri una posizione. Per verificare la struttura di un nuovo grafo, usa [shapes.ttl](shapes.ttl). Se vuoi aggiungere una lettura concorrente, crea una posizione con il proprio identificatore e la propria provenienza.

## Costruire e verificare il sito

Il sito usa file statici. Per rigenerarli servono Python 3 con RDFLib, Pandoc, OpenSSL e la CLI Clean CSS (`cleancss`). Per i controlli del grafo servono anche pySHACL e OWL-RL. Esegui dalla radice del repository.

```bash
bash minify.sh
python3 tools/build_site.py
python3 dubium/tests/verifica.py
python3 -m http.server 8000 --bind 127.0.0.1
```

L'anteprima locale del catalogo è su `http://127.0.0.1:8000/dubium/`. Il generatore legge il Turtle e le guide locali. Le glosse della fonte italiana sono indicate quando non esiste una glossa tradotta. Il catalogo si naviga anche con JavaScript disattivato. Il filtro, quando attivo, lavora nel browser. L'[esempio della formalizzazione](FORMALIZZAZIONE.md#interrogazione-di-esempio) mostra come recuperare una relazione insieme al passo che la sostiene.

## Che cosa cambia nella versione 0.2.0

Dubium è ora il primo modulo di una rete, accanto a [Trivium](../trivium/README.md) e [Metrum](../metrum/README.md), importati dalla [radice di Aenigma](../aenigma.ttl). Nessun identificatore è cambiato e la versione precedente (`dub:v0.1.0-draft`) resta citabile. Le novità sono metadati e allineamenti: l'intestazione dichiara titolo, descrizione, licenza CC BY 4.0, autori, editore e date; i concetti sono anche `skos:Concept`, raccolti nello schema `dub:concetti` con etichette preferite, così gli strumenti SKOS li possono sfogliare; posizioni, domande, passi e asserzioni sono `prov:Entity` e `derivedFrom` è una sottoproprietà di `prov:wasDerivedFrom`, così la provenienza si legge anche con PROV-O; le fonti sono `schema:CreativeWork`. Il grafo è disponibile anche come [JSON-LD](dubium.jsonld) e [RDF/XML](dubium.rdf), con un [contesto](context.jsonld) per gli sviluppatori. Il [collaudo della rete](../tests/verifica.py) si aggiunge a quello del modulo.
