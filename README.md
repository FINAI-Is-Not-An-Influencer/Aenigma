# Aenigma

[English](README.en.md) · [Latine](README.la.md)

Aenigma è l'ontologia web della Cripta Semantica. **Dubium**, il primo modulo, mette in relazione le idee, le domande e le posizioni del manifesto filosofico con i passi che le sostengono. Il progetto comprende un grafo leggibile dai programmi, un catalogo per i lettori e una Wiki per lo studio e l'uso pratico. [Sito di Aenigma](https://aenigma.criptasemantica.it/) · [Wiki in italiano](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT)

## Dalla filosofia al grafo

L'epigrafe del manifesto riprende il dubbio del *Sofista* di Platone sul significato di «essente». Nel resto del testo la Cripta Semantica collega la domanda sull'essere alla scrittura, all'indagine filosofica e all'ontologia informatica. Dubium offre un modo per seguire queste distinzioni fino alla fonte. L'essere di un ente e l'essere in quanto tale, per esempio, hanno schede distinte che rimandano allo stesso passaggio. [Manifesto della Cripta Semantica](https://criptasemantica.it/) · [Quadro filosofico nella Wiki](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-01)

## Una prima visita

1. Apri il catalogo e cerca *essere di un ente*. La scheda mostra il nome, la glossa e le posizioni in cui il concetto compare.
2. Apri F27, poi P7. La prima scheda espone la posizione, la seconda indica il passo del manifesto.
3. Confronta F28 e Q04. Puoi cambiare lingua e seguire la stessa voce.

[Catalogo](https://aenigma.criptasemantica.it/dubium/) · [Guida per iniziare](dubium/README.md) · [Esercizio nella Wiki](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-03)

## Che cosa contiene Dubium

| Risorsa | Che cosa trovi |
| --- | --- |
| [Grafo Turtle](dubium/dubium.ttl) | Concetti, posizioni, domande, fonti, relazioni e schema OWL |
| [Formalizzazione](dubium/FORMALIZZAZIONE.md) | Mappa dei passi, lettura delle scelte e repertorio delle formule |
| [Vincoli SHACL](dubium/shapes.ttl) | Regole per verificare la struttura delle schede |
| [Programma di verifica](dubium/tests/verifica.py) | Interrogazioni, inferenze OWL RL e casi di dati incompleti |
| [Costruzione del catalogo](tools/build_site.py) | Generazione delle pagine trilingui dal grafo e dalle guide Markdown |

RDF esprime dati come relazioni fra risorse. OWL descrive le classi e le proprietà del grafo. SHACL verifica i campi richiesti. Le formule filosofiche conservano la notazione del progetto e la provenienza. Le inferenze automatiche riguardano la struttura dei dati. [Modello del grafo](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-02)

## Riutilizzare i dati

Carica il file Turtle e interroga il grafo con SPARQL. Per arrivare dalla posizione alla fonte, segui `derivedFrom` fino al passo e `partOfSource` fino alla pagina. Conserva questo percorso quando mostri o citi una posizione. [Prima interrogazione](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-05)

`dub:` abbrevia `https://aenigma.criptasemantica.it/dubium#`. Nelle anteprime RDFa della Cripta si incontra anche `cs:` per quello spazio di nomi. Cripta Semantic Service usa a sua volta `cs:` per il proprio vocabolario. Quando usi entrambi, confronta gli IRI completi e dichiara `dub:` per Dubium. [Identificatori e integrazione editoriale](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-06)

## Contribuire e provare in locale

Per aggiungere una lettura, individua il passo, conserva gli identificatori esistenti e crea una nuova posizione con fonte, statuto e formula. Aggiungi le tre edizioni linguistiche e verifica il grafo. [Procedura per contribuire](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-07)

Servono Python con RDFLib, pySHACL e OWL-RL, oltre a Pandoc, OpenSSL e Clean CSS (`cleancss`). Dalla radice del repository:

```bash
python3 dubium/tests/verifica.py
bash minify.sh
python3 tools/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Apri `http://127.0.0.1:8000/dubium/` e prova ricerca, fonti e cambio lingua. [Guida al collaudo](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-08)

## Per approfondire

La Wiki comprende il percorso filosofico, la mappa del manifesto, gli esercizi, le procedure e un glossario con domande frequenti. [Indice dei capitoli](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT) · [Mappa del manifesto](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-04) · [Glossario e domande](https://github.com/FINAI-Is-Not-An-Influencer/Aenigma/wiki/IT-09) · [Licenza del repository](LICENSE)
